#!/usr/bin/env python3
# build_pdf_digital.py
# Converte Markdown -> PDF digital usando fpdf2 + LayoutEngine

import argparse
import sys
import re
from pathlib import Path
from fpdf import FPDF

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils.md_parser import parse_markdown, BlockType, parse_inline
from utils.layout_engine import LayoutEngine


MM_PER_INCH = 25.4
BLEED_MM = 3


class BookPDF(FPDF):
    def __init__(self, engine: LayoutEngine, title="", subtitle="", author="",
                 print_mode=False, trim_size="6x9in"):
        self.print_mode = print_mode
        self.trim_size = trim_size
        self._parse_trim_size()

        if print_mode:
            pw = self._trim_w + 2 * BLEED_MM
            ph = self._trim_h + 2 * BLEED_MM
            fmt = (pw, ph)
        else:
            fmt = engine.page_size()

        super().__init__("P", "mm", fmt)
        self.engine = engine
        self.book_title = title
        self.book_subtitle = subtitle
        self.book_author = author
        self._chapter_title = ""
        self._chapter_number = 0
        self._family = "Helvetica"
        self._mono_family = "Courier"
        self._heading_family = "Helvetica"
        self._font_map = {
            "Segoe UI": "SegoeUI",
            "Georgia": "Georgia",
            "Cascadia Code": self._mono_family,
            "Consolas": "Consolas",
            "Courier": "Courier",
            "Helvetica": "Helvetica",
        }

        if print_mode:
            lm, tm, rm = engine.margins()
            self.set_margins(lm + BLEED_MM, tm + BLEED_MM, rm + BLEED_MM)
            self.set_auto_page_break(auto=True, margin=engine.auto_page_break_margin() + BLEED_MM)
        else:
            lm, tm, rm = engine.margins()
            self.set_margins(lm, tm, rm)
            self.set_auto_page_break(auto=True, margin=engine.auto_page_break_margin())
        self._setup_fonts()

    def _parse_trim_size(self):
        parts = self.trim_size.lower().replace("in", "").split("x")
        if len(parts) == 2:
            try:
                self._trim_w = float(parts[0]) * MM_PER_INCH
                self._trim_h = float(parts[1]) * MM_PER_INCH
            except ValueError:
                self._trim_w, self._trim_h = 152.4, 228.6
        else:
            self._trim_w, self._trim_h = 152.4, 228.6

    def _add_crop_marks(self):
        if not self.print_mode:
            return
        b = BLEED_MM
        tw, th = self._trim_w, self._trim_h
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.2)
        # Top-left corner
        self.line(b, b - 3, b, b + 5)
        self.line(b - 3, b, b + 5, b)
        # Top-right corner
        self.line(b + tw, b - 3, b + tw, b + 5)
        self.line(b + tw + 3, b, b + tw - 5, b)
        # Bottom-left corner
        self.line(b, b + th + 3, b, b + th - 5)
        self.line(b - 3, b + th, b + 5, b + th)
        # Bottom-right corner
        self.line(b + tw, b + th + 3, b + tw, b + th - 5)
        self.line(b + tw + 3, b + th, b + tw - 5, b + th)

    def _setup_fonts(self):
        georgia = "C:/Windows/Fonts/georgia.ttf"
        georgia_b = "C:/Windows/Fonts/georgiab.ttf"
        georgia_i = "C:/Windows/Fonts/georgiai.ttf"
        georgia_bi = "C:/Windows/Fonts/georgiaz.ttf"
        if Path(georgia).exists():
            try:
                self.add_font("Georgia", "", georgia)
                if Path(georgia_b).exists():
                    self.add_font("Georgia", "B", georgia_b)
                if Path(georgia_i).exists():
                    self.add_font("Georgia", "I", georgia_i)
                if Path(georgia_bi).exists():
                    self.add_font("Georgia", "BI", georgia_bi)
                self._family = "Georgia"
            except RuntimeError:
                pass

        segoe = "C:/Windows/Fonts/segoeui.ttf"
        segoe_b = "C:/Windows/Fonts/segoeuib.ttf"
        segoe_i = "C:/Windows/Fonts/segoeuii.ttf"
        segoe_bi = "C:/Windows/Fonts/segoeuiz.ttf"
        if Path(segoe).exists():
            try:
                self.add_font("SegoeUI", "", segoe)
                if Path(segoe_b).exists():
                    self.add_font("SegoeUI", "B", segoe_b)
                if Path(segoe_i).exists():
                    self.add_font("SegoeUI", "I", segoe_i)
                if Path(segoe_bi).exists():
                    self.add_font("SegoeUI", "BI", segoe_bi)
                self._heading_family = "SegoeUI"
            except RuntimeError:
                pass

        mono_candidates = [
            ("CascadiaCode.ttf", "CascadiaCode"),
            ("cascadia.ttf", "Cascadia"),
            ("consola.ttf", "Consolas"),
            ("consolab.ttf", "Consolas"),
        ]
        user_fonts = Path.home() / "AppData/Local/Microsoft/Windows/Fonts"
        for fname, family in mono_candidates:
            p = Path(f"C:/Windows/Fonts/{fname}")
            if not p.exists():
                p = user_fonts / fname
            if p.exists():
                try:
                    self.add_font(family, "", str(p))
                    self._mono_family = family
                    break
                except RuntimeError:
                    continue

    def _resolve_family(self, yaml_family: str) -> str:
        return self._font_map.get(yaml_family, yaml_family)

    def _normalize_text(self, text: str) -> str:
        replacements = {
            "\u2014": "--", "\u2013": "-",
            "\u2018": "'", "\u2019": "'",
            "\u201c": '"', "\u201d": '"',
            "\u2026": "...", "\u00a0": " ",
            "\u2192": "->",
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text

    def header(self):
        if self.page_no() <= 2:
            return
        self.set_font(self._family, "I", 7)
        self.set_text_color(158, 158, 158)
        text = self.book_title
        if self._chapter_title:
            text = f"{self._chapter_title} | {text}"
        self.cell(0, 5, text, align="C")
        self.ln(8)

    def footer(self):
        if self.page_no() <= 2:
            return
        self.set_y(-(15 + (BLEED_MM if self.print_mode else 0)))
        self.set_font(self._family, "", 9)
        self.set_text_color(26, 35, 126)
        self.cell(0, 10, str(self.page_no()), align="C")

    def cover_page(self):
        self.add_page()
        w = self.w
        h = self.h
        colors = [(26, 35, 126), (24, 38, 130), (22, 41, 134), (20, 44, 138),
                  (18, 47, 142), (16, 50, 146), (14, 53, 150), (13, 56, 154),
                  (11, 59, 158), (10, 62, 162)]
        band_h = h / len(colors)
        for i, col in enumerate(colors):
            self.set_fill_color(*col)
            self.rect(0, i * band_h, w, band_h + 1, style="F")

        self.set_y(h * 0.26)
        self.set_font(self._heading_family, "B", 28)
        self.set_text_color(255, 255, 255)
        self.multi_cell(0, 14, self.book_title, align="C")
        self.ln(10)

        if self.book_subtitle:
            self.set_font(self._family, "", 16)
            self.set_text_color(0, 191, 165)
            self.multi_cell(0, 10, self.book_subtitle, align="C")
            self.ln(20)

        if self.book_author:
            self.set_font(self._family, "", 14)
            self.set_text_color(158, 158, 158)
            self.multi_cell(0, 8, self.book_author, align="C")

        self.ln(40)
        self.set_draw_color(0, 191, 165)
        self.set_line_width(0.5)
        x = w / 4
        y = self.get_y()
        self.line(x, y, w - x, y)

    # ── Render methods ─────────────────────────────────────

    def render_heading(self, text, level):
        if level == 1:
            self._chapter_number += 1
            self._chapter_title = text
            self.add_page()

        self.ln(self.engine.spacing_before_heading(level))

        key = f"heading_h{level}"
        family, style, size = self.engine.font_for(key)
        color = self.engine.color_for(key)
        lh = self.engine.line_height_mm(key)

        self.set_font(self._resolve_family(family), style, size)
        self.set_text_color(*color)
        self.multi_cell(0, lh, self._normalize_text(text))

        if level == 1:
            self.set_draw_color(0, 191, 165)
            self.set_line_width(0.3)
            self.line(self.l_margin, self.get_y() + 1, self.w - self.r_margin, self.get_y() + 1)

        self.ln(self.engine.heading_after_spacing())

    def render_paragraph(self, text):
        segments = parse_inline(text)
        if not segments:
            return

        family, _, size = self.engine.font_for("body")
        lh = self.engine.line_height_mm("body")
        self.set_text_color(*self.engine.color_for("body"))

        for seg in segments:
            if seg.code:
                self.set_font(self._mono_family, "", self.engine.font_size_pt("code"))
            else:
                style = ""
                if seg.bold:
                    style += "B"
                if seg.italic:
                    style += "I"
                self.set_font(self._resolve_family(family), style, size)
            self.write(lh, self._normalize_text(seg.text))

    def render_code_block(self, code, language=""):
        lines = code.split("\n")
        x = self.l_margin + 3
        w = self.w - x - self.r_margin - 3
        line_h = 4.5
        y0 = self.get_y()
        badge_h = 3.5 if language else 0
        total_h = len(lines) * line_h + 3 + badge_h

        bg, txt_c, bdr_c = self.engine.code_colors()
        self.set_fill_color(*bg)
        self.set_draw_color(*bdr_c)
        self.rect(x - 1, y0, w + 2, total_h, style="F")

        if language:
            self.set_xy(x, y0 + 0.5)
            self.set_font(self._family, "B", 6.5)
            self.set_text_color(158, 158, 158)
            self.cell(w, 3, f"[{language}]")
            y0 += 3.5

        self.set_font(self._mono_family, "", self.engine.font_size_pt("code"))
        self.set_text_color(*txt_c)
        y = y0 + 1.5
        for line in lines:
            self.set_xy(x, y)
            self.cell(w, line_h, self._normalize_text(line))
            y += line_h
        self.set_y(y)

    def render_mermaid(self, code):
        lines = [l for l in code.split("\n") if l.strip()]
        if not lines:
            return
        x = self.l_margin
        w = self.w - x - self.r_margin
        line_h = 4.5
        y0 = self.get_y()
        badge_h = 4
        total_h = len(lines) * line_h + 3 + badge_h

        self.set_fill_color(227, 242, 253)
        self.set_draw_color(21, 101, 192)
        self.rect(x, y0, w, total_h, style="DF")

        self.set_xy(x + 2, y0 + 1)
        self.set_font(self._heading_family, "B", 7)
        self.set_text_color(21, 101, 192)
        self.cell(0, 3, "[Diagrama] Mermaid")

        self.set_font(self._mono_family, "", 8)
        self.set_text_color(33, 33, 33)
        y = y0 + 6
        for line in lines:
            self.set_xy(x + 2, y)
            self.cell(w - 4, line_h, self._normalize_text(line))
            y += line_h
        self.set_y(y + 1)

    def render_bullet_list(self, items):
        self.set_font(self._family, "", self.engine.font_size_pt("body"))
        self.set_text_color(*self.engine.color_for("body"))
        for item in items:
            self.set_x(self.l_margin + 5)
            self.cell(5, 5.5, "\u2022")
            self.multi_cell(0, 5.5, self._normalize_text(item))
            self.ln(1)

    def render_numbered_list(self, items):
        self.set_font(self._family, "", self.engine.font_size_pt("body"))
        self.set_text_color(*self.engine.color_for("body"))
        for i, item in enumerate(items, 1):
            self.set_x(self.l_margin + 5)
            self.cell(8, 5.5, f"{i}.")
            self.multi_cell(0, 5.5, self._normalize_text(item))
            self.ln(1)

    def render_callout(self, block):
        ct_map = {
            BlockType.TIP: "tip",
            BlockType.WARNING: "warning",
            BlockType.DEFINICAO: "definition",
            BlockType.INFO: "info",
            BlockType.RECAPITULANDO: "recap",
        }
        ctype = ct_map.get(block.type, "info")
        bg, txt_c, bdr_c = self.engine.callout_colors(ctype)
        label, font_style = self.engine.callout_label(ctype)

        text = self._normalize_text(block.content)
        segments = parse_inline(text)
        x = self.l_margin
        w = self.w - x - self.r_margin
        y0 = self.get_y()

        first_pass = True
        for _ in range(2):
            if not first_pass:
                self.set_xy(x, y0)
                self.set_text_color(*txt_c)
            self.set_font(self._family, font_style, 9)
            if label:
                self.write(5, label)
            for seg in segments:
                if seg.code:
                    self.set_font(self._mono_family, "", 8)
                else:
                    style = ""
                    if seg.bold:
                        style += "B"
                    if seg.italic:
                        style += "I"
                    self.set_font(self._family, style, 9)
                self.write(5, seg.text)
            if first_pass:
                y_end = self.get_y()
                self.set_fill_color(*bg)
                self.set_draw_color(*bdr_c)
                self.rect(x, y0, w, y_end - y0, style="DF")
                first_pass = False

        self.set_fill_color(*bdr_c)
        self.set_line_width(0.5)
        self.rect(x, y0, 1.5, y_end - y0, style="F")
        self.set_y(max(y_end, self.get_y()))

    def render_table(self, table_text):
        rows = table_text.strip().split("\n")
        data = []
        for row in rows:
            row = row.strip()
            if row.startswith("|"):
                data.append([c.strip() for c in row.strip(" |").split("|")])
        if len(data) < 2:
            return
        data = [r for r in data if not all(c.startswith("-") for c in r)]
        if not data:
            return

        col_count = len(data[0])
        usable = self.w - self.l_margin - self.r_margin
        col_width = usable / col_count
        line_h = 5
        tc = self.engine.table_colors()

        for i, row_data in enumerate(data):
            row_heights = []
            for cell in row_data:
                text = self._normalize_text(cell)
                cw = self.get_string_width("a")
                cpl = max(int(col_width / cw), 1) if cw > 0 else 50
                num = max(1, -(-len(text) // cpl))
                row_heights.append(num * line_h)
            row_h = max(line_h, max(row_heights))

            y_start = self.get_y()
            for j, cell in enumerate(row_data):
                x = self.l_margin + j * col_width
                self.set_xy(x, y_start)
                if i == 0:
                    self.set_font(self._family, "B", 9)
                    self.set_fill_color(*tc["header_bg"])
                    self.set_text_color(255, 255, 255)
                    fill = True
                else:
                    self.set_font(self._family, "", 9)
                    self.set_text_color(*self.engine.color_for("body"))
                    fill = (i % 2 == 0)
                    if fill:
                        self.set_fill_color(*tc["alt_row"])
                self.multi_cell(col_width, line_h, self._normalize_text(cell),
                                border=1, fill=fill,
                                new_x="RIGHT", new_y="TOP")
            self.set_y(y_start + row_h)

    def render_blockquote(self, text):
        x = self.l_margin + 5
        w = self.w - x - self.r_margin - 5
        text = self._normalize_text(text)
        y0 = self.get_y()
        self.set_font(self._family, "I", self.engine.font_size_pt("body"))
        self.set_text_color(66, 66, 66)
        self.set_x(x)
        self.multi_cell(w, self.engine.line_height_mm("body"), text)
        y_end = self.get_y()
        self.set_draw_color(*self.engine.color_for("heading_h1"))
        self.set_line_width(0.5)
        self.line(self.l_margin + 2, y0, self.l_margin + 2, y_end + 2)

    def render_hr(self):
        y = self.get_y()
        self.set_draw_color(*self.engine.hr_color())
        self.line(self.l_margin, y, self.w - self.r_margin, y)


def build_pdf(input_path, output_path, title, subtitle, author, engine,
              include_cover, print_mode=False, trim_size="6x9in"):
    md_text = input_path.read_text(encoding="utf-8")
    doc = parse_markdown(md_text)
    pdf_title = title or doc.title or input_path.stem

    pdf = BookPDF(engine, pdf_title, subtitle, author, print_mode, trim_size)

    if include_cover:
        pdf.cover_page()
    else:
        pdf.add_page()

    if print_mode:
        pdf._add_crop_marks()

    for block in doc.blocks:
        if block.type == BlockType.HEADING:
            pdf.render_heading(block.content, block.level)
        elif block.type == BlockType.PARAGRAPH:
            pdf.render_paragraph(block.content)
        elif block.type == BlockType.CODE:
            pdf.render_code_block(block.content, block.language)
        elif block.type == BlockType.MERMAID:
            pdf.render_mermaid(block.content)
        elif block.type == BlockType.LIST:
            has_numbers = any(c.isdigit() for c in str(block.items[:1]))
            if has_numbers:
                pdf.render_numbered_list(block.items)
            else:
                pdf.render_bullet_list(block.items)
        elif block.type == BlockType.TABLE:
            pdf.render_table(block.content)
        elif block.type in (BlockType.TIP, BlockType.WARNING,
                            BlockType.DEFINICAO, BlockType.INFO, BlockType.RECAPITULANDO):
            pdf.render_callout(block)
        elif block.type == BlockType.BLOCKQUOTE:
            pdf.render_blockquote(block.content)
        elif block.type == BlockType.HR:
            pdf.render_hr()

        spacing = engine.spacing_after(block.type)
        pdf.ln(spacing)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    if hasattr(pdf, "set_title"):
        pdf.set_title(pdf_title)
    if hasattr(pdf, "set_author"):
        pdf.set_author(author)
    if hasattr(pdf, "set_subject"):
        pdf.set_subject(pdf_title)
    if hasattr(pdf, "set_keywords"):
        pdf.set_keywords("")
    pdf.output(str(output_path))
    print(f"  OK PDF salvo: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Build PDF Digital/Print from Markdown")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--title", default="")
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--author", default="AI Software Engineering Academy")
    parser.add_argument("--book-id", default="ia-para-devs", help="Book ID para encontrar layout-book.yaml")
    parser.add_argument("--cover", action="store_true")
    parser.add_argument("--print-mode", action="store_true",
                        help="Gera PDF pronto para grafica (com sangria e marcas de corte)")
    parser.add_argument("--trim-size", default="6x9in",
                        help="Tamanho do livro para modo grafica (ex: 6x9in, 7x10in)")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERRO: Arquivo nao encontrado: {input_path}")
        sys.exit(1)

    layout_path = (
        Path(__file__).resolve().parent.parent
        / "knowledge-factory" / "products" / "books" / args.book_id / "assets" / "layout-book.yaml"
    )
    if not layout_path.exists():
        layout_path = Path(__file__).resolve().parent.parent / "config" / "editora" / "design-system" / "layout-book.yaml"
    if not layout_path.exists():
        print(f"  Aviso: layout-book.yaml nao encontrado, usando defaults")
        engine = LayoutEngine.__new__(LayoutEngine)
        engine._raw = engine._lay = engine._typ = engine._col = engine._spc = {}
    else:
        engine = LayoutEngine(layout_path)

    mode_label = "PDF grafica" if args.print_mode else "PDF digital"
    title = args.title or input_path.stem
    print(f"  Convertendo {input_path.name} -> {mode_label}...")
    build_pdf(input_path, Path(args.output), title, args.subtitle, args.author,
              engine, args.cover, args.print_mode, args.trim_size)


if __name__ == "__main__":
    main()
