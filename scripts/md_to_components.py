#!/usr/bin/env python3
"""
md_to_components.py
Converte Markdown em uma Component Tree semanticamente enriquecida.

Pipeline:
  Markdown
    ↓
  parse_markdown()
    ↓
  Component Tree (JSON/YAML)
    ↓
  Renderers (fpdf2, Typst, DOCX, EPUB, HTML)

Nao depende de Pandoc — usa parser Python nativo.
Para producao, pode ser trocado por Pandoc AST JSON filter.
"""

import argparse
import json
import re
import sys
import yaml
from dataclasses import dataclass, field
from pathlib import Path
from config import PROJECT_ROOT

COMPONENT_LIBRARY_PATH = PROJECT_ROOT / "config" / "editora" / "component-library.yaml"


@dataclass
class Component:
    type: str
    props: dict[str, Any] = field(default_factory=dict)
    children: list["Component"] = field(default_factory=list)
    text: str = ""


def load_component_library() -> dict:
    with open(COMPONENT_LIBRARY_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def infer_callout_variant(text: str) -> str | None:
    lowered = text.lower()
    if any(tag in lowered for tag in ["> [!tip]", "> [!note]", "dica"]):
        return "tip"
    if any(tag in lowered for tag in ["> [!warning]", "aviso", "atenção"]):
        return "warning"
    if any(tag in lowered for tag in ["> [!caution]", "erro comum", "cuidado"]):
        return "caution"
    if any(tag in lowered for tag in ["> [!important]", "boa prática", "best practice"]):
        return "best-practice"
    if "> [!info]" in lowered or "> [!note]" in lowered:
        return "info"
    return "info"


def detect_codeblock_language(info: str) -> str:
    return info.strip().split()[0] if info.strip() else "text"


def parse_table(lines: list[str]) -> Component:
    """Parse Markdown table into Table component."""
    header = lines[0]
    rows = lines[2:]  # skip separator line

    def parse_row(line: str) -> list[str]:
        return [cell.strip() for cell in line.strip("|").split("|")]

    headers = parse_row(header)
    body = [parse_row(row) for row in rows if row.strip()]

    return Component(
        type="Table",
        props={"column_count": len(headers)},
        children=[
            Component(type="TableHeader", children=[Component(type="TableCell", text=h) for h in headers]),
            Component(type="TableBody", children=[
                Component(type="TableRow", children=[Component(type="TableCell", text=cell) for cell in row])
                for row in body
            ]),
        ]
    )


def parse_inline(text: str) -> list[Component]:
    """Parse inline Markdown: bold, italic, code, links."""
    children = []
    patterns = [
        (r"`([^`]+)`", "InlineCode"),
        (r"\*\*([^*]+)\*\*", "Bold"),
        (r"\*([^*]+)\*", "Italic"),
        (r"\[([^\]]+)\]\(([^)]+)\)", "Link"),
    ]

    pos = 0
    while pos < len(text):
        best_match = None
        best_type = None
        best_start = len(text)

        for pattern, comp_type in patterns:
            m = re.search(pattern, text[pos:])
            if m and pos + m.start() < best_start:
                best_match = m
                best_type = comp_type
                best_start = pos + m.start()

        if best_match is None:
            children.append(Component(type="Text", text=text[pos:]))
            break

        if best_start > pos:
            children.append(Component(type="Text", text=text[pos:best_start]))

        if best_type == "Link":
            children.append(Component(type="Link", text=best_match.group(1), props={"url": best_match.group(2)}))
        else:
            children.append(Component(type=best_type, text=best_match.group(1)))

        pos = best_start + len(best_match.group(0))

    return children


def parse_markdown(md_text: str) -> Component:
    """Main parser. Converts Markdown into Component Tree."""
    lines = md_text.splitlines()
    root = Component(type="Document")

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Blank line
        if not stripped:
            i += 1
            continue

        # ATX Heading
        m = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if m:
            level = len(m.group(1))
            text = m.group(2)
            comp_type = {1: "ChapterTitle", 2: "Section", 3: "Subsection", 4: "Subsubsection", 5: "ParagraphHeading", 6: "ParagraphHeading"}.get(level, "Heading")
            root.children.append(Component(type=comp_type, text=text, props={"level": level}, children=parse_inline(text)))
            i += 1
            continue

        # Code block
        if stripped.startswith("```"):
            lang = detect_codeblock_language(stripped[3:])
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            root.children.append(Component(
                type="Code",
                text="\n".join(code_lines),
                props={"language": lang}
            ))
            continue

        # Table
        if "|" in stripped:
            table_lines = []
            while i < len(lines) and "|" in lines[i]:
                table_lines.append(lines[i])
                i += 1
            if len(table_lines) >= 2 and "---" in table_lines[1]:
                root.children.append(parse_table(table_lines))
                continue

        # Callout / blockquote
        if stripped.startswith(">"):
            bq_lines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                bq_lines.append(lines[i].lstrip("> "))
                i += 1
            bq_text = "\n".join(bq_lines)
            variant = infer_callout_variant(bq_text)
            root.children.append(Component(
                type="Callout",
                text=bq_text,
                props={"variant": variant},
                children=parse_inline(bq_text)
            ))
            continue

        # Image
        m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)", stripped)
        if m:
            root.children.append(Component(
                type="Figure",
                props={"src": m.group(2), "alt": m.group(1)},
                children=[Component(type="Caption", text=m.group(1))]
            ))
            i += 1
            continue

        # Horizontal rule / page break marker
        if re.match(r"^---\s*$", stripped):
            root.children.append(Component(type="PageBreak"))
            i += 1
            continue

        # Paragraph
        para_lines = []
        while i < len(lines) and lines[i].strip():
            para_lines.append(lines[i])
            i += 1
        para_text = " ".join(para_lines)
        root.children.append(Component(
            type="Paragraph",
            text=para_text,
            children=parse_inline(para_text)
        ))

    return root


def component_to_dict(comp: Component) -> dict:
    return {
        "type": comp.type,
        "text": comp.text,
        "props": comp.props,
        "children": [component_to_dict(c) for c in comp.children],
    }


def main():
    parser = argparse.ArgumentParser(description="Markdown to Component Tree")
    parser.add_argument("--input", required=True, help="Arquivo Markdown de entrada")
    parser.add_argument("--output", required=True, help="Arquivo JSON/YAML de saida")
    parser.add_argument("--format", choices=["json", "yaml"], default="yaml")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"ERRO: arquivo nao encontrado: {input_path}")
        sys.exit(1)

    md_text = input_path.read_text(encoding="utf-8")
    doc = parse_markdown(md_text)
    tree = component_to_dict(doc)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    if args.format == "json":
        output_path.write_text(json.dumps(tree, indent=2, ensure_ascii=False), encoding="utf-8")
    else:
        output_path.write_text(yaml.dump(tree, allow_unicode=True, sort_keys=False), encoding="utf-8")

    print(f"Component tree salva: {output_path}")
    print(f"Componentes raiz: {len(doc.children)}")


if __name__ == "__main__":
    main()
