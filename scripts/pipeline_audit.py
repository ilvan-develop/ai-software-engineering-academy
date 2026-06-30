#!/usr/bin/env python3
"""
pipeline_audit.py
Audita outputs reais no disco contra curriculum/status.yaml.
Gera relatorio markdown com discrepancias em knowledge-factory/auditoria/.
Uso: python scripts/pipeline_audit.py
"""

import yaml
from pathlib import Path
from datetime import datetime

from config import PROJECT_ROOT, SCRIPTS_DIR, STATUS_PATH, SOURCES_DIR as CURRICULUM_DIR, COURSES_DIR, BOOKS_DIR, KF_DIR, REPORTS_DIR
REPORT_DIR = REPORTS_DIR

OUTPUT_TYPES_SOURCE = ["slides", "exercicios", "quiz", "projeto"]
OUTPUT_TYPES_KF = ["slides", "videos", "exercicios", "quiz", "projeto", "assets", "seo", "social-media"]


def load_status() -> dict:
    with open(STATUS_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def has_content(dir_path: Path) -> bool:
    if not dir_path.exists() or not dir_path.is_dir():
        return False
    files = [f for f in dir_path.iterdir() if f.name != ".gitkeep"]
    return len(files) > 0


def audit_source(curso: str, modulo: str) -> list:
    issues = []
    base = CURRICULUM_DIR / curso / modulo
    if not base.exists():
        return issues
    status_yaml = load_status()
    declared_outputs = status_yaml.get("modules", {}).get(curso, {}).get(modulo, {}).get("outputs", {})
    for out_type in OUTPUT_TYPES_SOURCE:
        dir_path = base / out_type
        has = has_content(dir_path)
        claimed = declared_outputs.get(out_type)
        if claimed is None:
            continue
        actual = "gerado" if has else "pendente"
        if claimed != actual:
            issues.append({
                "local": f"curriculum/sources/{curso}/{modulo}/{out_type}/",
                "claimed": claimed,
                "actual": actual,
                "type": "source"
            })
    return issues


def audit_kf_output(curso: str, modulo: str) -> list:
    issues = []
    base = COURSES_DIR / curso / modulo
    if not base.exists():
        return issues
    status_yaml = load_status()
    declared_outputs = status_yaml.get("modules", {}).get(curso, {}).get(modulo, {}).get("outputs", {})
    for out_type in OUTPUT_TYPES_KF:
        dir_path = base / out_type
        has = has_content(dir_path)
        claimed = declared_outputs.get(out_type)
        if claimed is None:
            continue  # not declared in status.yaml — skip to avoid false positives
        actual = "gerado" if has else "pendente"
        if claimed != actual:
            issues.append({
                "local": f"knowledge-factory/products/courses/{curso}/{modulo}/{out_type}/",
                "claimed": claimed,
                "actual": actual,
                "type": "kf_output"
            })
    return issues


def audit_gates() -> list:
    issues = []
    data = load_status()
    gates = data.get("gates", {})
    for gate_name, books in gates.items():
        for book_id, gate in books.items():
            if gate.get("approved") == True:
                pass
    for gate_name, books in gates.items():
        prev_approved = None
        all_gates = list(gates.keys())
        for i, g in enumerate(all_gates):
            for b_id, g_data in gates.get(g, {}).items():
                approved = g_data.get("approved", False)
                if prev_approved is not None and approved and not prev_approved:
                    issues.append({
                        "local": f"gates/{g}/{b_id}",
                        "claimed": "true",
                        "actual": "false nos gates anteriores",
                        "type": "gate_logic"
                    })
                if g == g:
                    prev_approved = approved
    return issues


def audit_books() -> list:
    issues = []
    data = load_status()
    books_dir = BOOKS_DIR
    for book_id, book in data.get("books", {}).items():
        book_path = books_dir / book_id
        compiled = book_path / "compiled"
        output = book_path / "output"
        has_compiled = has_content(compiled)
        has_output = has_content(output)
        claimed_status = book.get("status", "desconhecido")
        if claimed_status == "publicado" and not (has_compiled and has_output):
            issues.append({
                "local": f"knowledge-factory/products/books/{book_id}/",
                "claimed": "publicado (status.yaml)",
                "actual": "compiled ok, output ok" if has_compiled and has_output else f"compiled={has_compiled}, output={has_output}",
                "type": "book"
            })
    return issues


def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d_%H%M")
    report_path = REPORT_DIR / f"pipeline-audit-{ts}.md"

    data = load_status()
    all_issues = []

    for course_name, mods in data.get("modules", {}).items():
        for mod_id in mods:
            all_issues.extend(audit_source(course_name, mod_id))
            all_issues.extend(audit_kf_output(course_name, mod_id))

    all_issues.extend(audit_gates())
    all_issues.extend(audit_books())

    total_source = sum(1 for i in all_issues if i["type"] == "source")
    total_kf = sum(1 for i in all_issues if i["type"] == "kf_output")
    total_gate = sum(1 for i in all_issues if i["type"] == "gate_logic")
    total_book = sum(1 for i in all_issues if i["type"] == "book")

    lines = [
        f"# Pipeline Audit Report - {ts}",
        "",
        "## Resumo",
        "",
        f"- Discrepancias totais: {len(all_issues)}",
        f"  - Source outputs: {total_source}",
        f"  - Knowledge Factory outputs: {total_kf}",
        f"  - Gates logicas: {total_gate}",
        f"  - Livros: {total_book}",
        "",
    ]

    if all_issues:
        lines.append("## Discrepancias Detalhadas")
        lines.append("")
        for i, issue in enumerate(all_issues, 1):
            lines.append(f"### {i}. {issue['type'].upper()} - {issue['local']}")
            lines.append("")
            lines.append(f"| Campo | Valor |")
            lines.append(f"|-------|-------|")
            lines.append(f"| Localizacao | `{issue['local']}` |")
            lines.append(f"| Status.yaml afirma | {issue['claimed']} |")
            lines.append(f"| Real no disco | {issue['actual']} |")
            lines.append("")
    else:
        lines.append("Nenhuma discrepancia encontrada. status.yaml reflete a realidade do disco.")
        lines.append("")

    lines.extend([
        "## Recomendacoes",
        "",
    ])

    if total_source > 0:
        lines.append(f"- Source ({total_source}): gerar conteudo faltante nos diretorios de curriculum/sources/")
    if total_kf > 0:
        lines.append(f"- Knowledge Factory ({total_kf}): executar `python scripts/pipeline_manager.py processar-modulo` para os modulos pendentes")
    if total_gate > 0:
        lines.append(f"- Gates ({total_gate}): revisar cadeia de aprovacao em curriculum/status.yaml secao gates")
    if total_book > 0:
        lines.append(f"- Livros ({total_book}): verificar se os formatos foram gerados corretamente")

    lines.append("")
    lines.append(f"_Gerado automaticamente por pipeline_audit.py em {ts}_")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Relatorio salvo: {report_path}")
    print(f"Discrepancias encontradas: {len(all_issues)}")
    return all_issues


def sync():
    """
    Sincroniza status.yaml com o disco.
    Para cada output que existe no disco mas esta marcado como pendente,
    atualiza status.yaml para 'gerado'.
    """
    data = load_status()
    changes = 0

    for course_name, mods in data.get("modules", {}).items():
        for mod_id, mod in mods.items():
            outputs = mod.setdefault("outputs", {})
            base_kf = COURSES_DIR / course_name / mod_id

            if base_kf.exists():
                for out_type in list(outputs.keys()):
                    dir_path = base_kf / out_type
                    if has_content(dir_path) and outputs.get(out_type) == "pendente":
                        outputs[out_type] = "gerado"
                        changes += 1
                        print(f"  {course_name}/{mod_id}/{out_type}: pendente -> gerado")

            base_src = CURRICULUM_DIR / course_name / mod_id
            for out_type in OUTPUT_TYPES_SOURCE:
                dir_path = base_src / out_type
                if has_content(dir_path) and outputs.get(out_type) == "pendente":
                    outputs[out_type] = "gerado"
                    changes += 1
                    print(f"  {course_name}/{mod_id}/{out_type} (source): pendente -> gerado")

    if changes > 0:
        data["metadata"]["last_updated"] = datetime.now().strftime("%Y-%m-%d")
        with open(STATUS_PATH, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        print(f"\n{changes} outputs sincronizados em status.yaml")
    else:
        print("\nNenhuma alteracao necessaria. status.yaml ja reflete o disco.")

    return changes


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--sync":
        sync()
    else:
        main()
