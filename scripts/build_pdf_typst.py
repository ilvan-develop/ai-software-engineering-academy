#!/usr/bin/env python3
"""
build_pdf_typst.py
Converte Component Tree (JSON/YAML) em PDF usando Typst.

Pipeline:
  Component Tree
    ↓
  .typ source (gerado a partir de componentes)
    ↓
  typst compile → PDF

Requerimentos:
  - Typst instalado: https://github.com/typst/typst
  - Fontes: Georgia, Segoe UI, Cascadia Code / Consolas
"""

import argparse
import json
import shutil
import subprocess
import sys
import yaml
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = PROJECT_ROOT / "scripts" / "templates" / "book.typ"


def check_typst() -> bool:
    return shutil.which("typst") is not None


def component_to_typst(comp: dict) -> str:
    comp_type = comp.get("type", "Unknown")
    text = comp.get("text", "").replace('"', '\\"').replace("\\", "\\\\")
    props = comp.get("props", {})
    children = comp.get("children", [])

    if comp_type == "ChapterTitle":
        return f'chapter-title("", "{text}")\n'
    elif comp_type == "Section":
        return f'section("{text}")\n'
    elif comp_type == "Subsection":
        return f'subsection("{text}")\n'
    elif comp_type == "Paragraph":
        inline = " ".join(_inline_to_typst(c) for c in children)
        return f'paragraph("{inline}")\n'
    elif comp_type == "Code":
        lang = props.get("language", "text")
        escaped = text.replace('"', '\\"').replace("\\", "\\\\")
        return f'code-block("{lang}", "{escaped}")\n'
    elif comp_type == "Callout":
        variant = props.get("variant", "info")
        inline = " ".join(_inline_to_typst(c) for c in children)
        return f'callout("{variant}", "{inline}")\n'
    elif comp_type == "Table":
        header = children[0] if children else None
        body = children[1] if len(children) > 1 else None
        headers = []
        rows = []
        if header:
            headers = [c.get("text", "") for c in header.get("children", [])]
        if body:
            for row in body.get("children", []):
                rows.append([c.get("text", "") for c in row.get("children", [])])
        header_str = ", ".join(f'"{h}"' for h in headers)
        rows_str = ", ".join("(" + ", ".join(f'"{c}"' for c in row) + ")" for row in rows)
        return f'editorial-table(({header_str}), ({rows_str}))\n'
    elif comp_type == "PageBreak":
        return "pagebreak()\n"
    elif comp_type == "Document":
        return "\n".join(component_to_typst(c) for c in children)
    else:
        return "\n".join(component_to_typst(c) for c in children)


def _inline_to_typst(child: dict) -> str:
    t = child.get("type", "Text")
    text = child.get("text", "").replace('"', '\\"').replace("\\", "\\\\")
    if t == "Bold":
        return f'*{text}*'
    elif t == "Italic":
        return f'_{text}_'
    elif t == "InlineCode":
        return f'`{text}`'
    elif t == "Link":
        return text
    return text


def build_typst(input_path: Path, output_path: Path, title: str, author: str, subtitle: str = ""):
    with open(input_path, encoding="utf-8") as f:
        if input_path.suffix == ".json":
            tree = json.load(f)
        else:
            tree = yaml.safe_load(f)

    body_typst = component_to_typst(tree)

    typst_source = f'''#import "{TEMPLATE_PATH.as_posix()}": book, chapter-title, section, subsection, paragraph, code-block, callout, editorial-table, figure

#book(
  title: "{title}",
  subtitle: "{subtitle}",
  author: "{author}",
) [
  {body_typst}
]
'''

    typst_path = output_path.with_suffix(".typ")
    typst_path.write_text(typst_source, encoding="utf-8")
    print(f"Fonte Typst gerada: {typst_path}")

    if not check_typst():
        print("\nAVISO: Typst não encontrado no PATH.")
        print("Instale em: https://github.com/typst/typst")
        print(f"Depois compile com: typst compile {typst_path} {output_path}")
        return False

    cmd = ["typst", "compile", str(typst_path), str(output_path)]
    print(f"  Executando: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"ERRO Typst: {result.stderr}")
        return False

    print(f"OK PDF Typst salvo: {output_path}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Build PDF from Component Tree via Typst")
    parser.add_argument("--input", required=True, help="Component tree JSON/YAML")
    parser.add_argument("--output", required=True, help="PDF output path")
    parser.add_argument("--title", default="AI Software Engineering Academy", help="Book title")
    parser.add_argument("--subtitle", default="", help="Book subtitle")
    parser.add_argument("--author", default="AI Software Engineering Academy", help="Author")
    args = parser.parse_args()

    ok = build_typst(Path(args.input), Path(args.output), args.title, args.author, args.subtitle)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
