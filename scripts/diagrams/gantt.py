#!/usr/bin/env python3
"""
gantt.py
Gera diagrama de Gantt em SVG.

Entrada:
{
  "title": "Cronograma do Projeto",
  "tasks": [
    {"label": "Descoberta", "start": 0, "duration": 3, "group": "Fase 1"},
    {"label": "Design", "start": 3, "duration": 4, "group": "Fase 1"},
    {"label": "Implementacao", "start": 7, "duration": 6, "group": "Fase 2"},
    {"label": "Testes", "start": 13, "duration": 3, "group": "Fase 2"}
  ]
}
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

GROUP_COLORS = {"Fase 1": "#1565C0", "Fase 2": "#00BFA5", "Fase 3": "#FF8F00", "default": "#757575"}
BG = "#FAFAFA"
BAR_H = 20


def create_svg(data: dict[str, Any], width: int = 800, height: int = 400) -> str:
    title = data.get("title", "Cronograma (Gantt)")
    tasks = data.get("tasks", [])

    ns = "http://www.w3.org/2000/svg"
    svg = ET.Element("svg", {
        "xmlns": ns, "viewBox": f"0 0 {width} {height}",
        "width": str(width), "height": str(height),
        "font-family": "Segoe UI, sans-serif",
    })
    ET.SubElement(svg, "rect", {"x": "0", "y": "0", "width": str(width), "height": str(height), "fill": BG, "rx": "8"})

    t = ET.SubElement(svg, "text", {"x": str(width // 2), "y": "30", "text-anchor": "middle", "font-size": "18", "font-weight": "bold", "fill": "#1A237E"})
    t.text = title

    max_end = max((t.get("start", 0) + t.get("duration", 1) for t in tasks), default=10)
    margin_left = 200
    margin_right = 40
    margin_top = 60
    usable_w = width - margin_left - margin_right
    usable_h = height - margin_top - 30
    n = len(tasks)
    row_h = min(usable_h / max(n, 1), 36)
    scale = usable_w / max(max_end, 1)

    # Header days
    for i in range(max_end + 1):
        x = margin_left + i * scale
        d = ET.SubElement(svg, "text", {"x": str(x), "y": str(margin_top - 10), "text-anchor": "middle", "font-size": "9", "fill": "#757575"})
        d.text = f"S{i + 1}"

    # Grid lines
    for i in range(max_end + 1):
        x = margin_left + i * scale
        ET.SubElement(svg, "line", {"x1": str(x), "y1": str(margin_top), "x2": str(x), "y2": str(height - 20), "stroke": "#E0E0E0", "stroke-width": "0.5"})

    # Tasks
    for i, task in enumerate(tasks):
        start = task.get("start", 0)
        dur = task.get("duration", 1)
        label = task.get("label", "")
        group = task.get("group", "default")
        color = GROUP_COLORS.get(group, GROUP_COLORS["default"])
        y = margin_top + i * row_h + 5

        # Label
        lbl = ET.SubElement(svg, "text", {"x": str(margin_left - 10), "y": str(y + BAR_H - 5), "text-anchor": "end", "font-size": "11", "fill": "#212121"})
        lbl.text = label

        # Bar
        bx = margin_left + start * scale
        bw = max(dur * scale, 4)
        ET.SubElement(svg, "rect", {"x": str(bx), "y": str(y), "width": str(bw), "height": str(BAR_H), "rx": "4", "fill": color})
        bar_lbl = ET.SubElement(svg, "text", {"x": str(bx + bw / 2), "y": str(y + BAR_H - 5), "text-anchor": "middle", "font-size": "9", "fill": "white", "font-weight": "bold"})
        bar_lbl.text = f"W{start + 1}-W{start + dur}" if dur > 1 else f"W{start + 1}"

    return ET.tostring(svg, encoding="unicode")


def main():
    import argparse, json
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    with open(args.input, encoding="utf-8") as f:
        data = json.load(f)
    svg = create_svg(data)
    Path(args.output).write_text(svg, encoding="utf-8")
    print(f"SVG salvo: {args.output}")


if __name__ == "__main__":
    main()
