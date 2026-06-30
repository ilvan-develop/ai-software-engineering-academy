#!/usr/bin/env python3
"""
fpdf2_components.py
Renderer fpdf2 orientado a componentes.
Recebe uma Component Tree (JSON/YAML) e renderiza PDF.

Este é um renderer de demonstração da arquitetura component-based.
Para producao, substituir por Typst renderer ou renderer DOCX/EPUB.
"""

import argparse
import json
import yaml
import sys
from pathlib import Path
from fpdf import FPDF

from svg_to_fpdf import SvgRenderer

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


class ComponentPDF(FPDF):
    def __init__(self):
        super().__init__("P", "mm", "A4")
        self.set_auto_page_break(auto=True, margin=20)
        self.set_margins(20, 20, 20)
        # Default fallbacks (core fonts are Latin-1 only)
        self.font_regular = "Arial"
        self.font_bold = "Arial"
        self.font_mono = "Courier"
        self._setup_fonts()
        self.add_page()
        self.set_font(self.font_regular, "", 11)
        self.set_text_color(33, 33, 33)

    def _setup_fonts(self):
        # Heading / UI font: Segoe UI
        segoe = "C:/Windows/Fonts/segoeui.ttf"
        segoe_b = "C:/Windows/Fonts/segoeuib.ttf"
        if Path(segoe).exists():
            try:
                self.add_font("SegoeUI", "", segoe)
                if Path(segoe_b).exists():
                    self.add_font("SegoeUI", "B", segoe_b)
                self.font_bold = "SegoeUI"
            except RuntimeError:
                pass

        # Body font: Georgia
        georgia = "C:/Windows/Fonts/georgia.ttf"
        if Path(georgia).exists():
            try:
                self.add_font("Georgia", "", georgia)
                self.font_regular = "Georgia"
            except RuntimeError:
                pass

        # Monospace font: Consolas or Cascadia
        mono_candidates = [
            ("C:/Windows/Fonts/consola.ttf", "Consolas"),
            ("C:/Windows/Fonts/cascadia.ttf", "Cascadia"),
            ("C:/Windows/Fonts/CascadiaCode.ttf", "CascadiaCode"),
        ]
        for path_str, family in mono_candidates:
            p = Path(path_str)
            if p.exists():
                try:
                    self.add_font(family, "", str(p))
                    self.font_mono = family
                    break
                except RuntimeError:
                    continue

    def render_component(self, comp: dict):
        comp_type = comp.get("type", "Unknown")
        text = comp.get("text", "")
        props = comp.get("props", {})
        children = comp.get("children", [])

        if comp_type == "ChapterTitle":
            self.set_font(self.font_bold, "B", 20)
            self.set_text_color(26, 35, 126)
            self.ln(10)
            self.multi_cell(0, 10, text)
            self.ln(8)
            # Decorative line
            self.set_draw_color(0, 191, 165)
            self.set_line_width(0.8)
            y = self.get_y()
            self.line(20, y, 80, y)
            self.ln(4)
            self.set_draw_color(0, 0, 0)

        elif comp_type in ("Section", "Subsection"):
            size = 16 if comp_type == "Section" else 13
            self.set_font(self.font_bold, "B", size)
            self.set_text_color(26, 35, 126)
            self.ln(6)
            self.multi_cell(0, 8, text)
            self.ln(4)

        elif comp_type == "Paragraph":
            self.set_font(self.font_regular, "", 11)
            self.set_text_color(33, 33, 33)
            self.multi_cell(0, 6, self._inline_text(children))
            self.ln(4)

        elif comp_type == "Code":
            self.set_font(self.font_mono, "", 9)
            self.set_text_color(224, 224, 224)
            self.ln(2)
            start_y = self.get_y()
            # Measure height by rendering once (fpdf2 cannot easily measure)
            self.multi_cell(0, 5, text)
            end_y = self.get_y()
            # Draw background behind the text
            self.set_xy(20, start_y)
            self.set_fill_color(38, 50, 56)
            self.rect(18, start_y - 2, 174, end_y - start_y + 4, style="F")
            # Re-render text on top
            self.set_xy(20, start_y)
            self.set_text_color(224, 224, 224)
            self.multi_cell(0, 5, text)
            self.ln(4)
            self.set_text_color(33, 33, 33)

        elif comp_type == "Callout":
            variant = props.get("variant", "info")
            colors = {
                "info": (21, 101, 192),
                "warning": (245, 127, 23),
                "tip": (46, 125, 50),
                "caution": (198, 40, 40),
                "best-practice": (46, 125, 50),
            }
            r, g, b = colors.get(variant, colors["info"])
            self.set_font(self.font_regular, "", 10)
            self.set_text_color(33, 33, 33)
            self.ln(2)
            start_y = self.get_y()
            self.multi_cell(0, 6, self._inline_text(children))
            end_y = self.get_y()
            self.set_draw_color(r, g, b)
            self.set_line_width(1.0)
            self.rect(20, start_y - 2, 170, end_y - start_y + 4, style="D")
            self.set_draw_color(0, 0, 0)
            self.ln(4)

        elif comp_type == "Figure":
            src = props.get("src", "")
            caption = props.get("alt", "")
            img_path = Path(src)
            if not img_path.is_absolute():
                if src.startswith("/"):
                    img_path = PROJECT_ROOT / src.lstrip("/")
                else:
                    img_path = PROJECT_ROOT / src

            if img_path.suffix.lower() == ".svg" and img_path.exists():
                self.ln(4)
                svg_renderer = SvgRenderer(self)
                svg_renderer.render_file(str(img_path))
                self.ln(4)
            elif img_path.exists():
                try:
                    self.image(str(img_path), x=20, w=170)
                    self.ln(4)
                except RuntimeError:
                    self._draw_placeholder(img_path)
            else:
                self._draw_placeholder(img_path)

            if caption:
                self.set_font(self.font_regular, "", 9)
                self.set_text_color(117, 117, 117)
                self.cell(0, 6, caption, align="C")
                self.ln(8)
            self.set_text_color(33, 33, 33)

        elif comp_type == "Table":
            self.set_font(self.font_bold, "", 10)
            self.set_fill_color(26, 35, 126)
            self.set_text_color(255, 255, 255)
            header = children[0] if children else None
            if header and header.get("type") == "TableHeader":
                cells = header.get("children", [])
                col_width = 170 / max(len(cells), 1)
                for cell in cells:
                    self.cell(col_width, 7, cell.get("text", "")[:25], border=1, fill=True)
                self.ln()
            self.set_font(self.font_regular, "", 9)
            self.set_text_color(33, 33, 33)
            body = children[1] if len(children) > 1 else None
            if body and body.get("type") == "TableBody":
                for row in body.get("children", []):
                    cells = row.get("children", [])
                    col_width = 170 / max(len(cells), 1)
                    for cell in cells:
                        self.cell(col_width, 6, cell.get("text", "")[:25], border=1)
                    self.ln()
            self.ln(4)

        elif comp_type == "PageBreak":
            self.add_page()

        # Recurse into container children that haven't been explicitly rendered
        if comp_type not in ("Document", "Paragraph", "Callout", "Table"):
            for child in children:
                self.render_component(child)

    def _draw_placeholder(self, img_path: Path):
        self.set_draw_color(26, 35, 126)
        self.set_fill_color(245, 245, 245)
        self.set_line_width(0.5)
        start_y = self.get_y()
        self.rect(20, start_y, 170, 80, style="DF")
        self.set_xy(20, start_y + 30)
        self.set_font(self.font_regular, "", 10)
        self.set_text_color(117, 117, 117)
        self.cell(170, 10, f"[Figura nao encontrada: {img_path.name}]", align="C")
        self.set_xy(20, start_y + 80)
        self.ln(4)

    def _inline_text(self, children: list) -> str:
        result = []
        for child in children:
            child_type = child.get("type", "Text")
            text = child.get("text", "")
            if child_type == "Bold":
                result.append(f"**{text}**")
            elif child_type == "Italic":
                result.append(f"*{text}*")
            elif child_type == "InlineCode":
                result.append(f"`{text}`")
            elif child_type == "Link":
                result.append(text)
            else:
                result.append(text)
        return "".join(result)


def render_component_tree(tree_path: Path, output_path: Path):
    with open(tree_path, encoding="utf-8") as f:
        if tree_path.suffix == ".json":
            tree = json.load(f)
        else:
            tree = yaml.safe_load(f)

    pdf = ComponentPDF()
    for child in tree.get("children", []):
        pdf.render_component(child)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(output_path))
    print(f"PDF renderizado: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Render Component Tree to PDF (fpdf2)")
    parser.add_argument("--input", required=True, help="Component tree JSON/YAML")
    parser.add_argument("--output", required=True, help="PDF output path")
    args = parser.parse_args()

    render_component_tree(Path(args.input), Path(args.output))


if __name__ == "__main__":
    main()
