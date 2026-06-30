#!/usr/bin/env python3
"""
svg_to_fpdf.py
Renderiza SVG nativo em PDF via fpdf2.
Suporta o subconjunto de SVG usado pelos geradores de diagrama da Diagram Factory:
  rect, circle, ellipse, line, polygon, polyline, path, text, g, defs, marker, svg

Dependencias: fpdf2, xml.etree.ElementTree (stdlib)
"""

import re
import math
import xml.etree.ElementTree as ET
from pathlib import Path
from fpdf import FPDF
from fpdf.drawing import PaintedPath, GraphicsStyle, PathPaintRule, DeviceRGB

# ---------------------------------------------------------------------------
# Helpers de cor
# ---------------------------------------------------------------------------

SVG_COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 128, 0),
    "blue": (0, 0, 255),
    "gray": (128, 128, 128),
    "grey": (128, 128, 128),
    "silver": (192, 192, 192),
    "maroon": (128, 0, 0),
    "purple": (128, 0, 128),
    "fuchsia": (255, 0, 255),
    "lime": (0, 255, 0),
    "olive": (128, 128, 0),
    "yellow": (255, 255, 0),
    "navy": (0, 0, 128),
    "teal": (0, 128, 128),
    "aqua": (0, 255, 255),
    "orange": (255, 165, 0),
    "transparent": None,
}


def parse_color(value, default=(0, 0, 0)):
    if not value or value == "none":
        return None
    value = value.strip()
    if value.startswith("#"):
        h = value.lstrip("#")
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        if len(h) == 6:
            try:
                return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))
            except ValueError:
                return default
        return default
    if value.startswith("rgb("):
        m = re.match(r"rgb\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", value)
        if m:
            return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
        return default
    return SVG_COLORS.get(value.lower(), default)


def parse_alpha(value):
    if value is None or value == "":
        return 1.0
    try:
        return float(value)
    except ValueError:
        return 1.0


def parse_float(val, default=0.0):
    if val is None:
        return default
    try:
        return float(val)
    except (ValueError, TypeError):
        return default


# ---------------------------------------------------------------------------
# Parser de path d
# ---------------------------------------------------------------------------

_PATH_CMD = re.compile(r"([MLHVZCQTAmlhvzcqta])")
_FLOAT_RE = re.compile(r"-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?")


def tokenize_path(d):
    tokens = []
    parts = _PATH_CMD.split(d)
    for part in parts:
        if not part.strip():
            continue
        if part.strip() in "MLHVZCQTAmlhvzcqta":
            tokens.append(part.strip())
        else:
            for match in _FLOAT_RE.finditer(part):
                tokens.append(float(match.group()))
    return tokens


def parse_path_data(d):
    tokens = tokenize_path(d)
    ops = []
    i = 0
    current_pos = (0.0, 0.0)
    start_pos = (0.0, 0.0)
    last_control = None
    implicit = False

    while i < len(tokens):
        if isinstance(tokens[i], str):
            cmd = tokens[i]
            i += 1
            implicit = False
            if cmd in "MLHVZCQTA":
                is_relative = False
            else:
                is_relative = True
                cmd = cmd.upper()
        elif implicit:
            cmd = prev_cmd if prev_cmd in "MLHVZCQTA" else "L"
            is_relative = False
        else:
            i += 1
            continue

        prev_cmd = cmd

        if cmd == "M":
            x, y = tokens[i], tokens[i + 1]
            i += 2
            if is_relative:
                x += current_pos[0]
                y += current_pos[1]
            ops.append(("M", x, y))
            current_pos = (x, y)
            start_pos = (x, y)
            last_control = None

        elif cmd == "L":
            while i < len(tokens) and not isinstance(tokens[i], str):
                x, y = tokens[i], tokens[i + 1]
                i += 2
                if is_relative:
                    x += current_pos[0]
                    y += current_pos[1]
                ops.append(("L", x, y))
                current_pos = (x, y)
                last_control = None
            implicit = True

        elif cmd == "H":
            while i < len(tokens) and not isinstance(tokens[i], str):
                x = tokens[i]
                i += 1
                if is_relative:
                    x += current_pos[0]
                ops.append(("L", x, current_pos[1]))
                current_pos = (x, current_pos[1])
                last_control = None
            implicit = True

        elif cmd == "V":
            while i < len(tokens) and not isinstance(tokens[i], str):
                y = tokens[i]
                i += 1
                if is_relative:
                    y += current_pos[1]
                ops.append(("L", current_pos[0], y))
                current_pos = (current_pos[0], y)
                last_control = None
            implicit = True

        elif cmd == "C":
            while i < len(tokens) and not isinstance(tokens[i], str):
                x1, y1, x2, y2, x, y = tokens[i:i + 6]
                i += 6
                if is_relative:
                    x1 += current_pos[0]
                    y1 += current_pos[1]
                    x2 += current_pos[0]
                    y2 += current_pos[1]
                    x += current_pos[0]
                    y += current_pos[1]
                ops.append(("C", x1, y1, x2, y2, x, y))
                current_pos = (x, y)
                last_control = (x2, y2)
            implicit = True

        elif cmd == "Q":
            while i < len(tokens) and not isinstance(tokens[i], str):
                x1, y1, x, y = tokens[i:i + 4]
                i += 4
                if is_relative:
                    x1 += current_pos[0]
                    y1 += current_pos[1]
                    x += current_pos[0]
                    y += current_pos[1]
                ops.append(("C",
                            current_pos[0] + (x1 - current_pos[0]) * 2 / 3,
                            current_pos[1] + (y1 - current_pos[1]) * 2 / 3,
                            x + (x1 - x) * 2 / 3,
                            y + (y1 - y) * 2 / 3,
                            x, y))
                current_pos = (x, y)
                last_control = (x1, y1)
            implicit = True

        elif cmd == "A":
            while i < len(tokens) and not isinstance(tokens[i], str):
                rx, ry, x_rot, large_flag, sweep_flag, x, y = tokens[i:i + 7]
                i += 7
                large_flag = bool(int(large_flag))
                sweep_flag = bool(int(sweep_flag))
                if is_relative:
                    x += current_pos[0]
                    y += current_pos[1]
                # Approximate arc with cubic bezier
                _append_arc(ops, current_pos, (x, y), rx, ry, x_rot, large_flag, sweep_flag)
                current_pos = (x, y)
                last_control = None
            implicit = True

        elif cmd == "Z":
            ops.append(("Z",))
            current_pos = start_pos
            last_control = None
            implicit = True

    return ops


def _append_arc(ops, start, end, rx, ry, x_rot, large, sweep):
    """Aproxima arco com curvas de bezier (abordagem simplificada)."""
    x1, y1 = start
    x2, y2 = end
    if abs(x1 - x2) < 0.001 and abs(y1 - y2) < 0.001:
        return
    if rx < 0.001 or ry < 0.001:
        ops.append(("L", x2, y2))
        return
    num_segments = 4
    theta1 = math.atan2(y1, x1)
    theta2 = math.atan2(y2, x2)
    dtheta = (theta2 - theta1) % (2 * math.pi)
    if large and dtheta < math.pi:
        dtheta -= 2 * math.pi
    elif not large and dtheta > math.pi:
        dtheta -= 2 * math.pi
    seg = dtheta / num_segments
    for i in range(num_segments):
        a1 = theta1 + i * seg
        a2 = a1 + seg
        cx1 = x1 + rx * math.cos(a1)
        cy1 = y1 + ry * math.sin(a1)
        cx2 = x2 - rx * math.cos(a2)
        cy2 = y2 - ry * math.sin(a2)
        ex = x1 + rx * math.cos(a2)
        ey = y1 + ry * math.sin(a2)
        ops.append(("C", cx1, cy1, cx2, cy2, ex, ey))
        x1, y1 = ex, ey


# ---------------------------------------------------------------------------
# Transform parser
# ---------------------------------------------------------------------------

_TRANSFORM_RE = re.compile(
    r"(translate|scale|rotate|skewX|skewY|matrix)\s*\(([^)]*)\)"
)


def parse_transform(transform_str):
    if not transform_str:
        return None
    transforms = []
    for match in _TRANSFORM_RE.finditer(transform_str):
        name = match.group(1)
        args_str = match.group(2).strip()
        args = [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", args_str)]
        transforms.append((name, args))
    return transforms


def apply_transform_list(ops, transform_list):
    """Aplica uma lista de transformacoes a uma lista de operacoes de path."""
    if not transform_list:
        return
    for name, args in transform_list:
        if name == "translate":
            tx, ty = args[0] if len(args) > 0 else 0, args[1] if len(args) > 1 else 0
            for i in range(len(ops)):
                op = ops[i]
                if op[0] in ("M", "L"):
                    ops[i] = (op[0], op[1] + tx, op[2] + ty)
                elif op[0] == "C":
                    ops[i] = (op[0], op[1] + tx, op[2] + ty, op[3] + tx, op[4] + ty, op[5] + tx, op[6] + ty)
        elif name == "scale":
            sx = args[0] if len(args) > 0 else 1
            sy = args[1] if len(args) > 1 else sx
            for i in range(len(ops)):
                op = ops[i]
                if op[0] in ("M", "L"):
                    ops[i] = (op[0], op[1] * sx, op[2] * sy)
                elif op[0] == "C":
                    ops[i] = (op[0], op[1] * sx, op[2] * sy, op[3] * sx, op[4] * sy, op[5] * sx, op[6] * sy)
        elif name == "rotate":
            angle = math.radians(args[0])
            cx, cy = args[1] if len(args) > 1 else 0, args[2] if len(args) > 2 else 0
            c = math.cos(angle)
            s = math.sin(angle)
            for i in range(len(ops)):
                op = ops[i]
                if op[0] in ("M", "L"):
                    x, y = op[1] - cx, op[2] - cy
                    ops[i] = (op[0], x * c - y * s + cx, x * s + y * c + cy)
                elif op[0] == "C":
                    x, y = op[1] - cx, op[2] - cy
                    x2, y2 = op[3] - cx, op[4] - cy
                    x3, y3 = op[5] - cx, op[6] - cy
                    ops[i] = (op[0],
                              x * c - y * s + cx, x * s + y * c + cy,
                              x2 * c - y2 * s + cx, x2 * s + y2 * c + cy,
                              x3 * c - y3 * s + cx, x3 * s + y3 * c + cy)
    return ops


# ---------------------------------------------------------------------------
# Renderizador principal
# ---------------------------------------------------------------------------


class SvgRenderer:
    """Renderiza SVG em um objeto FPDF existente."""

    def __init__(self, pdf: FPDF, margin_left=20, margin_top=20, margin_right=20):
        self.pdf = pdf
        self.ml = margin_left
        self.mt = margin_top
        self.mr = margin_right
        self.available_width = pdf.w - pdf.l_margin - pdf.r_margin
        self.scale = 1.0
        self.origin_x = 0.0
        self.origin_y = 0.0
        self.markers = {}
        self._current_opacity = 1.0

    def render(self, svg_text: str):
        root = ET.fromstring(svg_text)
        self._render_element(root)

    def render_file(self, path: str | Path):
        with open(path, encoding="utf-8") as f:
            self.render(f.read())

    def _local_name(self, tag: str) -> str:
        idx = tag.find("}")
        return tag[idx + 1:] if idx >= 0 else tag

    def _get_attrib(self, el: ET.Element, name: str, default=None):
        value = el.get(name)
        if value is not None:
            return value
        # Try namespaced version
        for key, val in el.attrib.items():
            if key.endswith(name):
                return val
        return default

    # ---------------------------------------------------------------
    # Renderizacao de elementos
    # ---------------------------------------------------------------

    def _render_element(self, el: ET.Element, parent_transform=None):
        tag = self._local_name(el.tag)
        transform_str = self._get_attrib(el, "transform")

        if tag == "svg":
            self._setup_svg(el)

        elif tag == "g":
            self._render_group(el, transform_str)

        elif tag == "rect":
            self._draw_rect(el, transform_str)

        elif tag == "circle":
            self._draw_circle(el, transform_str)

        elif tag == "ellipse":
            self._draw_ellipse(el, transform_str)

        elif tag == "line":
            self._draw_line(el, transform_str)

        elif tag == "polygon":
            self._draw_polygon(el, transform_str)

        elif tag == "polyline":
            self._draw_polyline(el, transform_str)

        elif tag == "path":
            self._draw_path_el(el, transform_str)

        elif tag == "text":
            self._draw_text(el, transform_str)

        elif tag == "defs":
            self._collect_defs(el)

        elif tag == "marker":
            self._collect_marker(el)

    # ---------------------------------------------------------------
    # Setup SVG
    # ---------------------------------------------------------------

    def _setup_svg(self, el: ET.Element):
        viewbox = self._get_attrib(el, "viewBox")
        if viewbox:
            parts = viewbox.strip().split()
            if len(parts) == 4:
                vx, vy, vw, vh = map(float, parts)
                self.origin_x = vx
                self.origin_y = vy
                scale_x = self.available_width / vw if vw > 0 else 1
                page_h = self.pdf.h - self.pdf.t_margin - self.pdf.b_margin
                scale_y = page_h / vh if vh > 0 else 1
                self.scale = min(scale_x, scale_y)
        for child in el:
            self._render_element(child)

    def _map(self, x: float, y: float):
        sx = (x - self.origin_x) * self.scale + self.pdf.l_margin
        sy = (y - self.origin_y) * self.scale + self.pdf.t_margin
        return sx, sy

    def _map_x(self, x: float):
        return (x - self.origin_x) * self.scale + self.pdf.l_margin

    def _map_y(self, y: float):
        return (y - self.origin_y) * self.scale + self.pdf.t_margin

    def _map_len(self, length: float):
        return length * self.scale

    # ---------------------------------------------------------------
    # Estilo
    # ---------------------------------------------------------------

    def _apply_fill(self, el: ET.Element, default="black"):
        color = parse_color(self._get_attrib(el, "fill", default))
        alpha = parse_alpha(self._get_attrib(el, "fill-opacity"))
        if color is not None:
            self.pdf.set_fill_color(*color)
            return "F"
        return ""

    def _apply_stroke(self, el: ET.Element):
        color = parse_color(self._get_attrib(el, "stroke"))
        width = parse_float(self._get_attrib(el, "stroke-width"), 1.0)
        alpha = parse_alpha(self._get_attrib(el, "stroke-opacity"))
        if color is not None:
            self.pdf.set_draw_color(*color)
            self.pdf.set_line_width(self._map_len(width))
            return "D"
        self.pdf.set_line_width(0)  # invisible
        return ""

    def _get_style(self, el):
        fill_val = self._get_attrib(el, "fill")
        stroke_val = self._get_attrib(el, "stroke")
        fill_style = ""
        stroke_style = ""
        if fill_val and fill_val != "none":
            self.pdf.set_fill_color(*parse_color(fill_val, (0, 0, 0)))
            fill_style = "F"
        if stroke_val and stroke_val != "none":
            self.pdf.set_draw_color(*parse_color(stroke_val, (0, 0, 0)))
            sw = parse_float(self._get_attrib(el, "stroke-width"), 1.0)
            self.pdf.set_line_width(self._map_len(sw))
            stroke_style = "D"
        return fill_style + stroke_style if fill_style or stroke_style else "DF"

    # ---------------------------------------------------------------
    # Primitivas graficas
    # ---------------------------------------------------------------

    def _draw_rect(self, el, transform_str):
        x = parse_float(self._get_attrib(el, "x"))
        y = parse_float(self._get_attrib(el, "y"))
        w = parse_float(self._get_attrib(el, "width"))
        h = parse_float(self._get_attrib(el, "height"))
        rx = parse_float(self._get_attrib(el, "rx"))
        ry = parse_float(self._get_attrib(el, "ry"))
        rx = max(rx, ry) if rx > 0 else 0
        style = self._get_style(el)
        px, py = self._map(x, y)
        pw = self._map_len(w)
        ph = self._map_len(h)
        prx = self._map_len(rx) if rx > 0 else 0
        if prx > 0:
            self.pdf.rect(px, py, pw, ph, style=style, round_corners=True, corner_radius=prx)
        else:
            self.pdf.rect(px, py, pw, ph, style=style)

    def _draw_circle(self, el, transform_str):
        cx = parse_float(self._get_attrib(el, "cx"))
        cy = parse_float(self._get_attrib(el, "cy"))
        r = parse_float(self._get_attrib(el, "r"))
        style = self._get_style(el)
        p_cx, p_cy = self._map(cx, cy)
        pr = self._map_len(r)
        self.pdf.circle(p_cx, p_cy, pr, style=style)

    def _draw_ellipse(self, el, transform_str):
        cx = parse_float(self._get_attrib(el, "cx"))
        cy = parse_float(self._get_attrib(el, "cy"))
        rx = parse_float(self._get_attrib(el, "rx"))
        ry = parse_float(self._get_attrib(el, "ry"))
        style = self._get_style(el)
        p_cx, p_cy = self._map(cx, cy)
        prx = self._map_len(rx)
        pry = self._map_len(ry)
        self.pdf.ellipse(p_cx, p_cy, prx, pry, style=style)

    def _draw_line(self, el, transform_str):
        x1 = parse_float(self._get_attrib(el, "x1"))
        y1 = parse_float(self._get_attrib(el, "y1"))
        x2 = parse_float(self._get_attrib(el, "x2"))
        y2 = parse_float(self._get_attrib(el, "y2"))
        style = self._get_style(el)
        p1x, p1y = self._map(x1, y1)
        p2x, p2y = self._map(x2, y2)
        self.pdf.line(p1x, p1y, p2x, p2y)
        self._draw_marker(el, (p1x, p1y), (p2x, p2y))

    def _draw_polygon(self, el, transform_str):
        points_str = self._get_attrib(el, "points", "")
        pts = self._parse_points(points_str)
        if len(pts) < 3:
            return
        style = self._get_style(el)
        mapped = [self._map(x, y) for x, y in pts]
        self.pdf.polygon(mapped, style=style)

    def _draw_polyline(self, el, transform_str):
        points_str = self._get_attrib(el, "points", "")
        pts = self._parse_points(points_str)
        if len(pts) < 2:
            return
        style = self._get_style(el)
        mapped = [self._map(x, y) for x, y in pts]
        self.pdf.polyline(mapped)

    def _parse_points(self, s):
        nums = [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", s)]
        return [(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)]

    # ---------------------------------------------------------------
    # Path
    # ---------------------------------------------------------------

    def _draw_path_el(self, el, transform_str):
        d = self._get_attrib(el, "d", "")
        if not d:
            return
        ops = parse_path_data(d)

        path = PaintedPath()
        fill_color = parse_color(self._get_attrib(el, "fill"))
        stroke_color = parse_color(self._get_attrib(el, "stroke"))
        sw = parse_float(self._get_attrib(el, "stroke-width"), 1.0)

        for op in ops:
            if op[0] == "M":
                x, y = self._map(op[1], op[2])
                path.move_to(x, y)
            elif op[0] == "L":
                x, y = self._map(op[1], op[2])
                path.line_to(x, y)
            elif op[0] == "C":
                x1, y1 = self._map(op[1], op[2])
                x2, y2 = self._map(op[3], op[4])
                x, y = self._map(op[5], op[6])
                path.curve_to(x1, y1, x2, y2, x, y)
            elif op[0] == "Z":
                path.close()

        if fill_color:
            path.style.fill_color = DeviceRGB(fill_color[0]/255, fill_color[1]/255, fill_color[2]/255)
        if stroke_color:
            path.style.stroke_color = DeviceRGB(stroke_color[0]/255, stroke_color[1]/255, stroke_color[2]/255)
            path.style.stroke_width = self._map_len(sw)
            paint_rule = PathPaintRule.FILL_THEN_STROKE if fill_color else PathPaintRule.STROKE
            path.style.paint_rule = paint_rule
        elif fill_color:
            path.style.paint_rule = PathPaintRule.FILL

        self.pdf.draw_path(path)

        # Draw marker at end of path
        if ops:
            last_op = ops[-1]
            if last_op[0] in ("L", "C") and self._get_attrib(el, "marker-end"):
                end_x, end_y = self._map(last_op[-2], last_op[-1])
                prev_x, prev_y = self._map(ops[-2][-2], ops[-2][-1]) if len(ops) >= 2 else (end_x, end_y)
                angle = math.atan2(end_y - prev_y, end_x - prev_x)
                self._draw_marker_shape(end_x, end_y, angle, self._get_attrib(el, "marker-end"))

    # ---------------------------------------------------------------
    # Marker
    # ---------------------------------------------------------------

    def _collect_defs(self, el):
        for child in el:
            self._render_element(child)

    def _collect_marker(self, el):
        marker_id = self._get_attrib(el, "id")
        if marker_id:
            self.markers[marker_id] = el

    def _draw_marker(self, el, p1, p2):
        marker_end = self._get_attrib(el, "marker-end")
        if marker_end and marker_end.startswith("url(#"):
            mid = marker_end[5:-1]
            if mid in self.markers:
                angle = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
                self._draw_marker_shape(p2[0], p2[1], angle, marker_end)
        marker_start = self._get_attrib(el, "marker-start")
        if marker_start and marker_start.startswith("url(#"):
            mid = marker_start[5:-1]
            if mid in self.markers:
                angle = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
                self._draw_marker_shape(p1[0], p1[1], angle + math.pi, marker_start)

    def _draw_marker_shape(self, x, y, angle, marker_url):
        mid = marker_url[5:-1]
        marker_el = self.markers.get(mid)
        if marker_el is None:
            return
        marker_w = parse_float(self._get_attrib(marker_el, "markerWidth"), 10)
        marker_h = parse_float(self._get_attrib(marker_el, "markerHeight"), 7)
        ref_x = parse_float(self._get_attrib(marker_el, "refX"), 0)
        ref_y = parse_float(self._get_attrib(marker_el, "refY"), 0)
        scale = self.scale
        for child in marker_el:
            ctag = self._local_name(child.tag)
            if ctag == "polygon":
                pts_str = self._get_attrib(child, "points", "")
                pts = self._parse_points(pts_str)
                fill_color = parse_color(self._get_attrib(child, "fill", "black"))
                if fill_color:
                    self.pdf.set_fill_color(*fill_color)
                mapped = []
                for px, py in pts:
                    rx = (px - ref_x) * scale
                    ry = (py - ref_y) * scale
                    tx = rx * math.cos(angle) - ry * math.sin(angle) + x
                    ty = rx * math.sin(angle) + ry * math.cos(angle) + y
                    mapped.append((tx, ty))
                if len(mapped) >= 3:
                    self.pdf.polygon(mapped, style="F")

    # ---------------------------------------------------------------
    # Texto
    # ---------------------------------------------------------------

    def _draw_text(self, el, transform_str):
        x = parse_float(self._get_attrib(el, "x"))
        y = parse_float(self._get_attrib(el, "y"))
        fill = parse_color(self._get_attrib(el, "fill", "black"))
        font_size = parse_float(self._get_attrib(el, "font-size"), 12)
        font_weight = self._get_attrib(el, "font-weight", "normal")
        text_anchor = self._get_attrib(el, "text-anchor", "start")
        text = el.text or ""

        if fill:
            self.pdf.set_text_color(*fill)
        size_mm = font_size * self.scale * 0.3528  # pt -> mm
        is_bold = font_weight.lower() in ("bold", "700", "800", "900")
        family = "Helvetica"
        if is_bold:
            self.pdf.set_font(family, "B", max(size_mm, 6))
        else:
            self.pdf.set_font(family, "", max(size_mm, 6))

        px = self._map_x(x)
        py = self._map_y(y)

        if text_anchor == "middle":
            w = self.pdf.get_string_width(text)
            px -= w / 2
        elif text_anchor == "end":
            w = self.pdf.get_string_width(text)
            px -= w

        self.pdf.set_xy(px, py - size_mm * 0.75)
        self.pdf.cell(0, size_mm * 1.2, text)

    def _render_group(self, el, transform_str):
        for child in el:
            self._render_element(child, transform_str)
