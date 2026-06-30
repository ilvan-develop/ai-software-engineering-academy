"""
layout_engine.py
Gerencia estilos, spacing e geometria do livro carregando layout-book.yaml.
Fornece uma camada de abstracao entre o builder e a spec de layout.
"""

import yaml
from pathlib import Path


def _hex_to_rgb(hex_color: str):
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def _pt_to_mm(pt: float) -> float:
    return pt * 0.352778


BASELINE = 1.5


def _to_baseline(mm: float) -> float:
    return round(mm / BASELINE) * BASELINE


def _parse_measure(val):
    """Converte '18mm' ou '6pt' para mm float."""
    if isinstance(val, (int, float)):
        return float(val)
    s = str(val).strip()
    if s.endswith("mm"):
        return float(s[:-2])
    if s.endswith("pt"):
        return _pt_to_mm(float(s[:-2]))
    if s.endswith("cm"):
        return float(s[:-2]) * 10
    return float(s)


CALLOUT_COLOR_FALLBACK = {
    "info": ((227, 242, 253), (13, 71, 161), (21, 101, 192)),
    "warning": ((255, 248, 225), (245, 127, 23), (245, 127, 23)),
    "tip": ((232, 245, 233), (46, 125, 50), (46, 125, 50)),
    "caution": ((236, 239, 241), (66, 66, 66), (120, 144, 156)),
}

CALLOUT_LABEL_MAP = {
    "tip": ("Dica: ", "I"),
    "warning": ("Atencao: ", "B"),
    "definition": ("Definicao: ", ""),
    "info": ("", ""),
    "recap": ("Recapitulando: ", "B"),
}


class LayoutEngine:
    """Carrega layout-book.yaml e expoe metodos tipados para o builder."""

    def __init__(self, yaml_path: Path):
        with open(yaml_path, encoding="utf-8") as f:
            self._raw = yaml.safe_load(f)
        self._lay = self._raw.get("layout", {})
        self._typ = self._lay.get("typography", {})
        self._col = self._lay.get("colors", {})
        self._spc = self._lay.get("spacing", {})

    # ── Page geometry ──────────────────────────────────────

    def page_size(self):
        return (152.4, 228.6)

    def margins(self):
        lm = _parse_measure(self._spc.get("margin_inner", "15mm"))
        tm = _parse_measure(self._spc.get("margin_top", "18mm"))
        return (lm, tm, lm)

    def auto_page_break_margin(self):
        return 20

    # ── Typography helpers ─────────────────────────────────

    def font_for(self, element_key: str):
        cfg = self._typ.get(element_key, {})
        family = cfg.get("family", "Georgia")
        weight = cfg.get("weight", "Regular")
        size_pt = cfg.get("size_pt", 11)
        style_map = {
            "Regular": "",
            "Bold": "B",
            "Italic": "I",
            "Semibold": "B",
            "Bold Italic": "BI",
        }
        return (family, style_map.get(weight, ""), size_pt)

    def font_family(self, element_key: str):
        return self.font_for(element_key)[0]

    def font_style(self, element_key: str):
        return self.font_for(element_key)[1]

    def font_size_pt(self, element_key: str):
        return self.font_for(element_key)[2]

    def color_for(self, element_key: str):
        cfg = self._typ.get(element_key, {})
        color_str = cfg.get("color", "#212121")
        if isinstance(color_str, str) and color_str.startswith("#"):
            return _hex_to_rgb(color_str)
        return (33, 33, 33)

    def line_height_mm(self, element_key: str):
        cfg = self._typ.get(element_key, {})
        size_pt = cfg.get("size_pt", 11)
        ratio = cfg.get("line_height", 1.5)
        return _pt_to_mm(size_pt) * ratio

    def color_from_palette(self, palette_key: str, fallback="#212121"):
        raw = self._col.get(palette_key, fallback)
        if isinstance(raw, str) and raw.startswith("#"):
            return _hex_to_rgb(raw)
        return _hex_to_rgb(fallback)

    # ── Spacing ────────────────────────────────────────────

    SPACING_AFTER_MAP = {
        "paragraph": "paragraph_after",
        "code": "code_block",
        "mermaid": "code_block",
        "tip": "callout",
        "warning": "callout",
        "definition": "callout",
        "info": "callout",
        "recap": "callout",
        "blockquote": "callout",
        "list": "paragraph_after",
        "table": "code_block",
        "hr": "paragraph_after",
    }

    def spacing_after(self, block_type: str) -> float:
        key = self.SPACING_AFTER_MAP.get(block_type, "paragraph_after")
        pt = self._spc.get(key, 6)
        return _to_baseline(_parse_measure(pt) if isinstance(pt, str) else _pt_to_mm(pt))

    def spacing_before_heading(self, level: int) -> float:
        hb = self._spc.get("heading_before", {})
        if isinstance(hb, dict):
            pt = hb.get(f"h{level}", 18)
        else:
            pt = 18
        return _to_baseline(_parse_measure(str(pt)) if isinstance(pt, str) else _pt_to_mm(pt))

    def heading_after_spacing(self) -> float:
        pt = self._spc.get("heading_after", 6)
        return _to_baseline(_parse_measure(str(pt)) if isinstance(pt, str) else _pt_to_mm(pt))

    # ── Component colors ───────────────────────────────────

    def callout_colors(self, callout_type: str):
        ck = {
            "tip": "callout_info",
            "warning": "callout_warning",
            "definition": "callout_tip",
            "info": "callout_caution",
            "recap": None,
        }.get(callout_type)
        if ck is None:
            return ((245, 245, 245), (26, 35, 126), (26, 35, 126))
        if ck == "callout_info":
            bg = self.color_from_palette("callout_info", "#E3F2FD")
            txt = self.color_from_palette("secondary", "#0D47A1")
            bdr = self.color_from_palette("secondary", "#1565C0")
            return (bg, txt, bdr)
        if ck == "callout_warning":
            bg = self.color_from_palette("callout_warning", "#FFF8E1")
            txt = self.color_from_palette("accent", "#00BFA5")
            bdr = self.color_from_palette("accent", "#F57F17")
            return (bg, txt, bdr)
        if ck == "callout_tip":
            bg = self.color_from_palette("callout_tip", "#E8F5E9")
            txt = self.color_from_palette("secondary", "#0D47A1")
            bdr = self.color_from_palette("secondary", "#2E7D32")
            return (bg, txt, bdr)
        return CALLOUT_COLOR_FALLBACK.get(callout_type, CALLOUT_COLOR_FALLBACK["info"])

    def callout_label(self, callout_type: str):
        return CALLOUT_LABEL_MAP.get(callout_type, ("", ""))

    def table_colors(self):
        return {
            "header_bg": self.color_from_palette("table_header", "#1A237E"),
            "alt_row": self.color_from_palette("table_alt", "#F5F5F5"),
        }

    def code_colors(self):
        return (
            self.color_from_palette("code_bg", "#263238"),
            self.color_from_palette("code_text", "#E0E0E0"),
            self.color_from_palette("code_bg", "#263238"),
        )

    def hr_color(self):
        return self.color_from_palette("neutral_light", "#757575")
