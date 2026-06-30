#!/usr/bin/env python3
"""
slide_engine.py
Gera slides de apresentacao (Marp Markdown) a partir de aula.md.
Template-based, max 15 slides, prioriza diagramas e codigo.
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


def extract_objectives(text: str) -> list:
    in_obj = False
    objectives = []
    for line in text.split("\n"):
        s = line.strip()
        if re.match(r"^##?\s*Objetivos?", s):
            in_obj = True
            continue
        if in_obj and s.startswith("##"):
            break
        if in_obj and re.match(r"^\d+\.\s+", s):
            obj = re.sub(r"^\d+\.\s*\*\*", "", s)
            obj = obj.replace("**", "")
            objectives.append(obj)
    return objectives


def generate_slides(title: str, sections: list, objectives: list, code_blocks: list) -> str:
    course_short = title.replace("Modulo", "").replace("—", "-").strip()
    slides = []
    total_sections = len(sections)

    # Slide 1: Title
    slides.append(f"---\nmarp: true\ntheme: uncover\nclass:\n  - lead\n  - invert\n---\n\n# {title}\n\n## {course_short}\n\n---\n")

    # Slide 2: Objectives
    if objectives:
        slides.append("## Objetivos\n\n")
        for obj in objectives:
            slides.append(f"- {obj}\n")
        slides.append("\n---\n")

    # Content slides (max 12)
    max_content = min(total_sections, 12)
    used_sections = set()

    for i, sec in enumerate(sections[:max_content]):
        sec_title = sec["title"]
        if not sec_title or sec_title.startswith("Introdu"):
            continue
        used_sections.add(sec_title)

        lines = sec["content"]
        # Filter out empty lines and extract key points
        key_points = [l for l in lines if l.strip() and not l.strip().startswith("```")]
        key_points = key_points[:6]  # max 6 bullets

        slides.append(f"## {sec_title}\n\n")
        for kp in key_points:
            kp_clean = kp.strip().lstrip("-* ")
            if kp_clean.startswith("#"):
                continue
            if len(kp_clean) > 120:
                kp_clean = kp_clean[:117] + "..."
            slides.append(f"- {kp_clean}\n")
        slides.append("\n---\n")

    # Code slides (max 2)
    code_slides = 0
    for cb in code_blocks[:2]:
        code_lines = cb["code"].split("\n")
        if len(code_lines) > 15:
            code_lines = code_lines[:12] + ["..."]
        code_display = "\n".join(code_lines)
        slides.append(f"## Exemplo: {cb['lang']}\n\n```{cb['lang']}\n{code_display}\n```\n\n---\n")
        code_slides += 1

    # Summary slide
    slides.append("## Recap\n\n")
    for sec in sections[:max_content]:
        t = sec["title"]
        if t and not t.startswith("Introdu"):
            slides.append(f"- {t}\n")
    slides.append("\n---\n")

    # Final slide
    slides.append("# Obrigado!\n\n## Perguntas?\n")

    return "".join(slides)


def main():
    parser = argparse.ArgumentParser(description="Gerador de Slides (Marp)")
    parser.add_argument("--input", required=True, help="Caminho para aula.md")
    parser.add_argument("--output", required=True, help="Pasta de saida (slides/)")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERRO: Arquivo nao encontrado: {input_path}")
        sys.exit(1)

    text = input_path.read_text(encoding="utf-8")
    title = extract_title(text)
    sections = extract_sections(text)
    objectives = extract_objectives(text)
    code_blocks = extract_code_blocks(text)

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    slides = generate_slides(title, sections, objectives, code_blocks)
    slides_path = output_dir / "slides.md"
    slides_path.write_text(slides, encoding="utf-8")
    print(f"  OK Slides: {slides_path} ({len(slides.split('---')) - 1} slides)")

    # Also generate speaker notes version
    notes = []
    for sec in sections:
        notes.append(f"## {sec['title']}\n\n")
        lines = [l for l in sec["content"] if l.strip() and not l.strip().startswith("```")]
        notes.append("\n".join(lines[:8]))
        notes.append("\n\n---\n")
    notes_path = output_dir / "speaker-notes.md"
    notes_path.write_text("".join(notes), encoding="utf-8")
    print(f"  OK Speaker Notes: {notes_path}")

    print(f"  [DONE] Slides gerados para: {title}")


if __name__ == "__main__":
    main()
