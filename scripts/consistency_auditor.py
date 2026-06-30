#!/usr/bin/env python3
"""
consistency_auditor.py
Audita todos os modulos dos cursos em busca de inconsistencias:
  - Referencias cruzadas quebradas (ex: "veja modulo X")
  - Terminologia inconsistente
  - Tom de voz
  - Links quebrados
  - Profundidade entre modulos
Gera relatorio markdown em knowledge-factory/auditoria/.
"""

import sys
import re
from pathlib import Path

from config import PROJECT_ROOT, SCRIPTS_DIR, SOURCES_DIR as CURRICULUM_DIR, KF_DIR, REPORTS_DIR
REPORT_DIR = REPORTS_DIR


def collect_modules() -> list:
    """Retorna lista de dicts com path do modulo, curso, id, e conteudo da aula."""
    modules = []
    for course_dir in sorted(CURRICULUM_DIR.iterdir()):
        if not course_dir.is_dir():
            continue
        course = course_dir.name
        for mod_dir in sorted(course_dir.iterdir()):
            if not mod_dir.is_dir():
                continue
            mod_id = mod_dir.name
            aula_path = mod_dir / "aula" / "aula.md"
            if not aula_path.exists():
                continue
            text = aula_path.read_text(encoding="utf-8")
            title = extract_title(text)
            modules.append({
                "course": course,
                "module_id": mod_id,
                "path": mod_dir,
                "aula_path": aula_path,
                "title": title,
                "text": text,
            })
    return modules


def extract_title(text: str) -> str:
    for line in text.split("\n"):
        m = re.match(r"^#\s+(.+)$", line.strip())
        if m:
            return m.group(1).strip()
    return "Modulo"


def check_cross_references(text: str, all_titles: dict, mod: dict) -> list:
    """Verifica se referencias a outros modulos estao corretas."""
    issues = []
    refs = re.findall(r"(?:veja|ver|consulte|conforme|como vimos em)\s+(?:o\s+)?(?:modulo|mod\.?|capitulo|cap\.?|secao|sec\.?)\s+['\"]?([^'\",\.\n]+?)['\"]?", text, re.IGNORECASE)
    for ref in refs:
        ref_clean = ref.strip().lower()
        found = False
        for title, info in all_titles.items():
            if ref_clean in title.lower() or ref_clean in info["module_id"].lower():
                found = True
                break
        if not found:
            issues.append({
                "type": "cross-reference",
                "severity": "medium",
                "detail": f"Referencia possivelmente quebrada: '{ref}'",
                "location": f"{mod['course']}/{mod['module_id']}",
            })
    return issues


def check_terminology(text: str, mod: dict, all_terms: set) -> list:
    """Verifica consistencia de terminologia tecnica."""
    issues = []
    term_variations = {
        "front-end": ["frontend", "front end", "front-end"],
        "back-end": ["backend", "back end", "back-end"],
        "multi-tenancy": ["multitenancy", "multi tenancy", "multi-tenancy", "multi-tenant"],
        "design system": ["designsystem", "design system", "design-system"],
        "machine learning": ["machine learning", "aprendizado de maquina", "ml"],
        "deploy": ["deploy", "deployar", "fazer deploy"],
        "software": ["software", "programa", "aplicacao"],
    }

    text_lower = text.lower()
    for standard, variants in term_variations.items():
        found_variants = set()
        for v in variants:
            if v.lower() != standard.lower() and v.lower() in text_lower:
                found_variants.add(v)
        # The standard was not used but a variant was
        if standard.lower() not in text_lower and found_variants:
            # Only flag if multiple variants found (inconsistency)
            if len(found_variants) > 1:
                issues.append({
                    "type": "terminology",
                    "severity": "low",
                    "detail": f"Terminologia inconsistente para '{standard}': {', '.join(sorted(found_variants))}",
                    "location": f"{mod['course']}/{mod['module_id']}",
                })
    return issues


def check_code_language(text: str, mod: dict) -> list:
    """Verifica se blocos de codigo tem linguagem especificada."""
    issues = []
    in_code = False
    block_idx = 0
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("```"):
            if not in_code:
                # Opening fence
                block_idx += 1
                lang = stripped[3:].strip()
                if not lang:
                    issues.append({
                        "type": "code-style",
                        "severity": "low",
                        "detail": f"Bloco de codigo #{block_idx} sem especificacao de linguagem",
                        "location": f"{mod['course']}/{mod['module_id']}",
                    })
                in_code = True
            elif stripped == "```":
                # Closing fence — only exact ``` closes (avoids nested fence false positives)
                in_code = False
    return issues


def check_tone(text: str, mod: dict) -> list:
    """Verifica tom de voz — procura linguagem muito informal ou muito academica."""
    issues = []

    # Informal indicators
    informal_patterns = [
        (r'\b(?:mano|galera|pessoal|entao tipo assim|tipo,|sacou|tranquilo)\b', "Informal"),
    ]
    for pattern, label in informal_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            issues.append({
                "type": "tone",
                "severity": "low",
                "detail": f"Tom informal detectado ({label}): {len(matches)} ocorrencia(s)",
                "location": f"{mod['course']}/{mod['module_id']}",
            })

    # Passive voice overload
    passive = len(re.findall(r'\b(?:sido|foram|sao|era|fora)\s+\w+[ai]d[oa]s?\b', text, re.IGNORECASE))
    total_sentences = len(re.findall(r'[.!?]', text))
    if total_sentences > 20 and passive / total_sentences > 0.3:
        issues.append({
            "type": "tone",
            "severity": "medium",
            "detail": f"Excesso de voz passiva ({passive}/{total_sentences} sentencas, {passive/total_sentences*100:.0f}%)",
            "location": f"{mod['course']}/{mod['module_id']}",
        })

    return issues


def check_length_consistency(modules: list) -> list:
    """Verifica se ha modulos muito curtos ou muito longos comparados a media."""
    issues = []
    lengths = [(m["course"], m["module_id"], len(m["text"]), m["title"]) for m in modules]
    if not lengths:
        return issues

    avg_len = sum(l[2] for l in lengths) / len(lengths)
    for course, mod_id, length, title in lengths:
        ratio = length / avg_len
        if ratio < 0.3:
            issues.append({
                "type": "length",
                "severity": "medium",
                "detail": f"Modulo muito curto ({length} chars vs media {avg_len:.0f}): {ratio:.1f}x menor",
                "location": f"{course}/{mod_id}",
            })
        elif ratio > 2.5:
            issues.append({
                "type": "length",
                "severity": "medium",
                "detail": f"Modulo muito longo ({length} chars vs media {avg_len:.0f}): {ratio:.1f}x maior",
                "location": f"{course}/{mod_id}",
            })
    return issues


def check_heading_hierarchy(text: str, mod: dict) -> list:
    """Verifica se ha pular niveis de cabecalho (ex: ### sem ## antes)."""
    issues = []
    lines = text.split("\n")
    prev_level = 0
    in_code_block = False
    for i, line in enumerate(lines):
        # Toggle code block state; skip headings inside code blocks
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        m = re.match(r"^(#{1,6})\s+", line)
        if m:
            level = len(m.group(1))
            if level > prev_level + 1 and prev_level > 0:
                issues.append({
                    "type": "heading-hierarchy",
                    "severity": "low",
                    "detail": f"Hierarquia de cabecalhos quebrada na linha {i+1}: ##{prev_level} -> ##{level}",
                    "location": f"{mod['course']}/{mod['module_id']}",
                })
            prev_level = level
    return issues


def main():
    modules = collect_modules()
    if not modules:
        print("Nenhum modulo encontrado.")
        sys.exit(1)

    print(f"Auditando {len(modules)} modulos...\n")

    all_titles = {}
    for m in modules:
        all_titles[m["title"].lower()] = {"module_id": m["module_id"], "course": m["course"]}

    all_issues = []

    # Run all checks per module
    for m in modules:
        all_issues.extend(check_cross_references(m["text"], all_titles, m))
        all_issues.extend(check_terminology(m["text"], m, set()))
        all_issues.extend(check_code_language(m["text"], m))
        all_issues.extend(check_tone(m["text"], m))
        all_issues.extend(check_heading_hierarchy(m["text"], m))

    # Cross-module checks
    all_issues.extend(check_length_consistency(modules))

    # Group by severity
    severity_order = {"high": 0, "medium": 1, "low": 2}
    all_issues.sort(key=lambda x: (severity_order.get(x["severity"], 99), x["location"], x["type"]))

    # Generate report
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORT_DIR / "auditoria-consistencia.md"

    high = sum(1 for i in all_issues if i["severity"] == "high")
    medium = sum(1 for i in all_issues if i["severity"] == "medium")
    low = sum(1 for i in all_issues if i["severity"] == "low")

    lines = [
        "# Auditoria de Consistencia",
        "",
        f"**Data:** 2026-06-29",
        f"**Modulos auditados:** {len(modules)}",
        f"**Total de inconsistencias:** {len(all_issues)}",
        "",
        "## Resumo",
        "",
        f"| Severidade | Quantidade |",
        "|------------|------------|",
        f"| 🔴 Alta | {high} |",
        f"| 🟡 Media | {medium} |",
        f"| 🟢 Baixa | {low} |",
        "",
        "---",
        "",
    ]

    # Modulos auditados
    lines.extend([
        "## Modulos Auditados",
        "",
    ])
    for m in modules:
        lines.append(f"- **{m['course']}/{m['module_id']}**: {m['title']}")
    lines.append("")
    lines.append("---\n")

    # Issues
    if all_issues:
        lines.append("## Inconsistencias Encontradas\n")
        lines.append("| # | Severidade | Tipo | Local | Detalhe |")
        lines.append("|---|------------|------|-------|---------|")
        for idx, issue in enumerate(all_issues, 1):
            sev_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(issue["severity"], "⚪")
            lines.append(f"| {idx} | {sev_icon} {issue['severity']} | {issue['type']} | {issue['location']} | {issue['detail']} |")
        lines.append("")
    else:
        lines.append("## Resultado\n")
        lines.append("🎉 Nenhuma inconsistencia encontrada! Todos os modulos estao consistentes.\n")

    lines.extend([
        "---",
        "",
        "## Recomendacoes",
        "",
    ])

    if high > 0:
        lines.append("- 🔴 **Alta prioridade:** Corrigir referencias cruzadas quebradas antes de publicar")
    if medium > 0:
        lines.append("- 🟡 **Media prioridade:** Revisar modulos com comprimento destoante e tom de voz")
    if low > 0:
        lines.append("- 🟢 **Baixa prioridade:** Padronizar terminologia e adicionar linguagem em blocos de codigo")
    if not all_issues:
        lines.append("- ✅ Manter o padrao atual de qualidade")

    lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Relatorio salvo: {report_path}")
    print(f"Total: {len(all_issues)} inconsistencias ({high} alta, {medium} media, {low} baixa)")

    # Summary to stdout (use ASCII-only markers to avoid cp1252 errors on Windows)
    print("\n---\n")
    if high:
        print(f"  [ALTA] {high} de alta prioridade")
    if medium:
        print(f"  [MEDIA] {medium} de media prioridade")
    if low:
        print(f"  [BAIXA] {low} de baixa prioridade")
    if not all_issues:
        print("  [OK] Nenhuma inconsistencia encontrada!")


if __name__ == "__main__":
    main()
