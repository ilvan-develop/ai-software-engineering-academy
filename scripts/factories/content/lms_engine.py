#!/usr/bin/env python3
"""
lms_engine.py
Formata conteudo para plataformas de curso online (Udemy, Hotmart, Teachable).
Estrutura em secoes e aulas. Cada aula tem: titulo, descricao, recurso, duracao estimada, material complementar.
Inclui tags SEO, legenda e descricao.
"""

import argparse
import sys
import re
from pathlib import Path


def extract_title(text: str) -> str:
    for line in text.split("\n"):
        m = re.match(r"^#\s+(.+)$", line.strip())
        if m:
            return m.group(1).strip()
    return "Modulo"


def extract_sections(text: str) -> list:
    sections = []
    current_h2 = "Introducao"
    current_content = []
    for line in text.split("\n"):
        s = line.strip()
        m = re.match(r"^##\s+(.+)$", s)
        if m:
            if current_content:
                sections.append({"title": current_h2, "content": current_content})
            current_h2 = m.group(1).strip()
            current_content = []
        else:
            current_content.append(s)
    if current_content:
        sections.append({"title": current_h2, "content": current_content})
    return sections


def extract_code_blocks(text: str) -> list:
    blocks = re.findall(r"```(\w*)\n(.*?)```", text, re.DOTALL)
    return [{"lang": lang or "text", "code": code.strip()} for lang, code in blocks]


def generate_lms_structure(course_name: str, modules: list) -> str:
    total_video_minutes = 0

    lines = [
        f"# Estrutura LMS — {course_name}",
        "",
        "---",
        "",
        "## Metadados do Curso",
        "",
        f"**Titulo:** [Titulo para plataforma]",
        f"**Subtitulo:** {course_name}",
        f"**Categoria:** Desenvolvimento de Software",
        f"**Subcategoria:** Arquitetura de Software",
        f"**Nivel:** Intermediario",
        f"**Idioma:** Portugues (Brasil)",
        f"**Legendas:** Portugues, Ingles",
        "",
        "**Tags SEO:** arquitetura de software, enterprise, typescript, ddd, clean architecture,"
        " design patterns, solid, nestjs, nextjs, devops, agentes de IA\n",
        "---\n",
        "## Estrutura do Curso\n",
        "",
        "| Secao | Aulas | Duracao Total |",
        "|-------|-------|---------------|",
    ]

    secao_num = 1
    for mod in modules:
        title = mod["title"]
        sections = mod["sections"]
        has_code = len(mod["code_blocks"]) > 0

        # Estimate video duration: ~3 min per section + 4 min per code block
        section_count = len([s for s in sections if not s["title"].startswith("Introdu")])
        code_count = len(mod["code_blocks"])
        est_minutes = section_count * 3 + code_count * 4
        total_video_minutes += est_minutes

        aulas = []
        for sec in sections:
            if not sec["title"].startswith("Introdu"):
                aulas.append(sec["title"])

        aula_count = len(aulas) + (1 if has_code else 0)
        lines.append(f"| {secao_num}. {title} | {aula_count} aulas | {est_minutes} min |")
        secao_num += 1

    total_hours = total_video_minutes // 60
    total_remainder = total_video_minutes % 60
    lines.append(f"| **Total** | **{sum(len([s for s in m['sections'] if not s['title'].startswith('Introdu')]) + (1 if m['code_blocks'] else 0) for m in modules)} aulas** | **{total_hours}h{total_remainder}min** |")
    lines.append("")
    lines.append("---\n")

    # Detail per module
    for mod in modules:
        title = mod["title"]
        sections = mod["sections"]
        code_blocks = mod["code_blocks"]

        lines.extend([
            f"### Secao {modules.index(mod)+1}: {title}",
            "",
            f"**Descricao:** {title} — conceitos fundamentais com exemplos praticos.",
            "",
            "| # | Aula | Tipo | Duracao | Material |",
            "|---|------|------|---------|----------|",
        ])

        aula_num = 1
        for sec in sections:
            if sec["title"].startswith("Introdu"):
                continue
            lines.append(f"| {aula_num} | {sec['title']} | Video | ~3 min | Slides |")
            aula_num += 1

        if code_blocks:
            lines.append(f"| {aula_num} | Demo pratica | Codigo | ~4 min | Repositorio |")

        lines.append("")
        lines.append("**Material complementar:**")
        lines.append(f"- Slides da secao")
        if code_blocks:
            lines.append(f"- Codigo fonte ({code_blocks[0]['lang']})")
        lines.append("- Exercicios praticos")
        lines.append("- Quiz de fixacao")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## Requisitos",
        "",
        "- Conhecimento basico de TypeScript/JavaScript",
        "- Node.js 20+",
        "- Git",
        "- VSCode ou similar",
        "",
        "## Publico-alvo",
        "",
        "- Desenvolvedores full-stack que querem migrar para arquitetura",
        "- Arquitetos de software em inicio de carreira",
        "- Tech leads que querem formalizar conhecimento",
        "- Desenvolvedores senior que atuam como arquitetos sem titulo formal",
        "",
        "## O que o aluno aprendera",
        "",
    ])
    for mod in modules[:6]:
        lines.append(f"- {mod['title']}")
    lines.append("")

    lines.extend([
        "---",
        "",
        "## SEO Detalhado",
        "",
        "**Titulo SEO:** [Curso] {course_name} — Formacao Completa",
        "**URL amigavel:** /curso/arquitetura-software-enterprise",
        "**Meta descricao:** Aprenda arquitetura de software enterprise com TypeScript, "
        "DDD, Clean Architecture, NestJS, Next.js, DevOps e Agentes de IA. "
        "Formacao completa com 21 modulos e projetos praticos.",
        "",
        "**Palavras-chave:**",
        "- arquitetura de software enterprise",
        "- clean architecture typescript",
        "- ddd na pratica",
        "- nestjs enterprise",
        "- nextjs para empresas",
        "- devops para arquitetos",
        "- agentes de ia desenvolvimento",
        "- multi-tenant saas",
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Gerador de Estrutura LMS")
    parser.add_argument("--modules-dir", required=True, help="Diretorio com modulos do curso")
    parser.add_argument("--course", required=True, help="Nome do curso")
    parser.add_argument("--output", required=True, help="Pasta de saida (lms/)")
    args = parser.parse_args()

    modules_dir = Path(args.modules_dir)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    modules = []
    for mod_dir in sorted(modules_dir.iterdir()):
        if not mod_dir.is_dir():
            continue
        aula_path = mod_dir / "aula" / "aula.md"
        if aula_path.exists():
            text = aula_path.read_text(encoding="utf-8")
            modules.append({
                "id": mod_dir.name,
                "title": extract_title(text),
                "sections": extract_sections(text),
                "code_blocks": extract_code_blocks(text),
            })

    if not modules:
        print("ERRO: Nenhum modulo encontrado em", modules_dir)
        sys.exit(1)

    structure = generate_lms_structure(args.course, modules)
    path = output_dir / f"lms-estrutura-{args.course}.md"
    path.write_text(structure, encoding="utf-8")
    print(f"  OK {path.name}")

    # Also generate upload-ready CSV-like sheet
    csv_lines = ["secao, aula, tipo, duracao_min, descricao"]
    for mod in modules:
        for sec in mod["sections"]:
            if sec["title"].startswith("Introdu"):
                continue
            desc = sec["content"][0][:80] if sec["content"] else ""
            desc = desc.replace('"', "'")
            csv_lines.append(f'"{mod["title"]}","{sec["title"]}","video","3","{desc}"')
    csv_path = output_dir / f"lms-upload-{args.course}.csv"
    csv_path.write_text("\n".join(csv_lines), encoding="utf-8")
    print(f"  OK {csv_path.name}")

    print(f"  [DONE] Estrutura LMS gerada para: {args.course}")


if __name__ == "__main__":
    main()
