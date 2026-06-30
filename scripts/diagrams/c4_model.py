#!/usr/bin/env python3
"""
c4_model.py
Gera diagrama C4 de arquitetura em SVG (Contexto, Container ou Componente).

Entrada:
{
  "title": "Sistema de Pagamentos",
  "level": "container",
  "elements": [
    {"name": "Web App", "tech": "Next.js", "type": "web"},
    {"name": "API Gateway", "tech": "Kong", "type": "api"},
    {"name": "Payment Service", "tech": "Node.js", "type": "service"},
    {"name": "DB", "tech": "PostgreSQL", "type": "database"}
  ],
  "connections": [
    {"from": 0, "to": 1, "label": "HTTPS"},
    {"from": 1, "to": 2, "label": "gRPC"},
    {"from": 2, "to": 3, "label": "SQL"}
  ]
}
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

TYPE_COLORS = {
    "web": ("#1565C0", "white"),
    "api": ("#00BFA5", "white"),
    "service": ("#FF8F00", "white"),
    "database": ("#E91E63", "white"),
    "external": ("#757575", "white"),
    "user": ("#1A237E", "white"),
}
BG = "#FAFAFA"


def create_svg(data: dict[str, Any], width: int = 800, height: int = 500) -> str:
    title = data.get("title", "Diagrama C4")
    elements = data.get("elements", [])
    connections = data.get("connections", [])

    ns = "http://www.w3.org/2000/svg"
    svg = ET.Element("svg", {
        "xmlns": ns, "viewBox": f"0 0 {width} {height}",
        "width": str(width), "height": str(height),
        "font-family": "Segoe UI, sans-serif",
    })
    ET.SubElement(svg, "rect", {"x": "0", "y": "0", "width": str(width), "height": str(height), "fill": BG, "rx": "8"})

    t = ET.SubElement(svg, "text", {"x": str(width // 2), "y": "35", "text-anchor": "middle", "font-size": "20", "font-weight": "bold", "fill": "#1A237E"})
    t.text = title

    n = max(len(elements), 1)
    cols = min(n, 4)
    rows = (n + cols - 1) // cols
    cell_w = width / cols
    cell_h = (height - 80) / rows
    box_w = min(cell_w * 0.7, 200)
    box_h = 70

    centers = []
    for i, el in enumerate(elements):
        col = i % cols
        row = i // cols
        cx = cell_w * col + cell_w / 2
        cy = 80 + cell_h * row + cell_h / 2
        bx = cx - box_w / 2
        by = cy - box_h / 2
        el_type = el.get("type", "service")
        fg, txt_color = TYPE_COLORS.get(el_type, ("#757575", "white"))

        ET.SubElement(svg, "rect", {"x": str(bx), "y": str(by), "width": str(box_w), "height": str(box_h), "rx": "6", "fill": fg})
        en = ET.SubElement(svg, "text", {"x": str(cx), "y": str(cy - 5), "text-anchor": "middle", "font-size": "13", "font-weight": "bold", "fill": txt_color})
        en.text = el.get("name", "")
        tech_text = el.get("tech", "")
        if tech_text:
            ett = ET.SubElement(svg, "text", {"x": str(cx), "y": str(cy + 15), "text-anchor": "middle", "font-size": "10", "fill": txt_color, "font-style": "italic"})
            ett.text = f"[{tech_text}]"

        centers.append((cx, cy))

    # Connections
    for conn in connections:
        fi = conn.get("from", 0)
        ti = conn.get("to", 0)
        label = conn.get("label", "")
        if fi < len(centers) and ti < len(centers):
            x1, y1 = centers[fi]
            x2, y2 = centers[ti]
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            ET.SubElement(svg, "line", {"x1": str(x1), "y1": str(y1), "x2": str(x2), "y2": str(y2), "stroke": "#555", "stroke-width": "1.5"})
            if label:
                lbl = ET.SubElement(svg, "text", {"x": str(mx), "y": str(my - 8), "text-anchor": "middle", "font-size": "10", "fill": "#555"})
                lbl.text = label

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
