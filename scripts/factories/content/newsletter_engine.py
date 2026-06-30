#!/usr/bin/env python3
"""
newsletter_engine.py
Compila multiplos modulos em uma newsletter semanal.
Estrutura: assunto + introducao + 3 secoes de conteudo + CTA.
Maximo 5 minutos de leitura.
"""

import argparse
import sys
import re
from pathlib import Path
from datetime import datetime, timedelta


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


def extract_key_points(lines: list, max_lines: int = 3) -> list:
    points = []
    for l in lines:
        s = l.strip()
        if s and not s.startswith("```") and not s.startswith("#"):
            clean = s.lstrip("-* ")
            if len(clean) > 30 and len(points) < max_lines:
                points.append(clean)
    return points


def generate_newsletter(modules: list) -> str:
    week_num = (datetime.now() - datetime(2026, 1, 5)).days // 7 + 1
    date_str = datetime.now().strftime("%d/%m/%Y")

    main_module = modules[0] if modules else {"title": "Modulo", "sections": []}
    topic = main_module["title"].replace("Modulo", "").replace("—", "-").strip()

    sections_out = []
    for i, mod in enumerate(modules[:3]):
        secs = [s for s in mod["sections"] if s["title"] and not s["title"].startswith("Introdu")]
        if secs:
            sec = secs[0]
            kp = extract_key_points(sec["content"])
            body = " ".join(kp[:2]) if kp else "Leia o artigo completo para mais detalhes."
            sections_out.append({
                "title": mod["title"].replace("Modulo", "").replace("—", "-").strip(),
                "body": body,
                "emoji": ["🔥", "⚙️", "💡", "📐", "🔧", "🎯"][i % 6],
            })

    # Build newsletter
    lines = [
        f"{'='*50}",
        f"NEWSLETTER — Semana #{week_num}",
        f"{'='*50}",
        "",
        f"**Assunto:** {topic} — O que voce precisa saber esta semana",
        f"**Data:** {date_str}",
        f"**Tempo de leitura:** ~5 min",
        "",
        "---",
        "",
        "## Introducao",
        "",
        f"Esta semana exploramos {topic.lower()}. "
        "Um tema essencial para quem trabalha com arquitetura de software enterprise. "
        "Vamos direto aos pontos principais.",
        "",
        "---",
        "",
    ]

    for sec in sections_out:
        lines.extend([
            f"## {sec['emoji']} {sec['title']}",
            "",
            sec["body"],
            "",
            "---",
            "",
        ])

    lines.extend([
        "## 🎯 Para levar para o seu dia a dia",
        "",
        "1. Revise os conceitos abordados nos links acima",
        "2. Aplique pelo menos um deles no seu projeto atual",
        "3. Compartilhe com seu time o que aprendeu",
        "",
        "---",
        "",
        "## 🔗 Links da Semana",
        "",
    ])
    for mod in modules[:3]:
        clean = mod["title"].replace("Modulo", "").replace("—", "-").strip()
        lines.append(f"- [{clean}](curriculum/sources/{mod['course']}/{mod['module_id']}/aula/aula.md)")
    lines.append("")

    lines.extend([
        "---",
        "",
        "## 💬 Feedback",
        "",
        "Respondeu a este email? O que voce gostaria de ver na proxima edicao?",
        "",
        "---",
        "",
        "*Recebeu este email porque se inscreveu na AI Software Engineering Academy.*",
        "*Para cancelar, responda com 'SAIR'*.",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Gerador de Newsletter Semanal")
    parser.add_argument("--input-dir", required=True, help="Pasta raiz dos modulos (curriculum/sources/)")
    parser.add_argument("--output", required=True, help="Pasta de saida (newsletter/)")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Collect all modules
    modules = []
    for course_dir in sorted(input_dir.iterdir()):
        if not course_dir.is_dir():
            continue
        for mod_dir in sorted(course_dir.iterdir()):
            if not mod_dir.is_dir():
                continue
            aula_path = mod_dir / "aula" / "aula.md"
            if not aula_path.exists():
                continue
            text = aula_path.read_text(encoding="utf-8")
            title = extract_title(text)
            sections = extract_sections(text)
            modules.append({
                "course": course_dir.name,
                "module_id": mod_dir.name,
                "title": title,
                "sections": sections,
                "path": aula_path,
            })

    # Group into batches of 3 for weekly newsletters
    batch_size = 3
    total_newsletters = (len(modules) + batch_size - 1) // batch_size

    generated = 0
    for week in range(total_newsletters):
        batch = modules[week * batch_size:(week + 1) * batch_size]
        if not batch:
            continue

        newsletter = generate_newsletter(batch)
        week_num = week + 1
        filename = f"newsletter-semana-{week_num:02d}.md"
        n_path = output_dir / filename
        n_path.write_text(newsletter, encoding="utf-8")
        print(f"  OK {filename} ({len(batch)} modulos)")
        generated += 1

    print(f"  [DONE] {generated} newsletters geradas")


if __name__ == "__main__":
    main()
