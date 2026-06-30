#!/usr/bin/env python3
"""
er_diagram.py
Gera diagrama entidade-relacionamento em SVG.

Entrada:
{
  "title": "Modelo de Dados - E-commerce",
  "entities": [
    {"name": "Usuario", "attrs": ["id (PK)", "nome", "email"]},
    {"name": "Pedido", "attrs": ["id (PK)", "usuario_id (FK)", "total", "status"]},
    {"name": "Produto", "attrs": ["id (PK)", "nome", "preco"]}
  ],
  "relationships": [
    {"from": 0, "to": 1, "label": "1:N"},
    {"from": 1, "to": 2, "label": "N:M"}
  ]
}
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

COLORS = {"fill": "#1A237E", "bg": "#FAFAFA", "alt": "#E3F2FD", "stroke": "#1565C0", "text": "#212121", "line": "#757575"}


def create_svg(data: dict[str, Any], width: int = 800, height: int = 500) -> str:
    title = data.get("title", "Diagrama ER")
    entities = data.get("entities", [])
    relationships = data.get("relationships", [])

    ns = "http://www.w3.org/2000/svg"
    svg = ET.Element("svg", {
        "xmlns": ns, "viewBox": f"0 0 {width} {height}",
        "width": str(width), "height": str(height),
        "font-family": "Segoe UI, sans-serif",
    })
    ET.SubElement(svg, "rect", {"x": "0", "y": "0", "width": str(width), "height": str(height), "fill": COLORS["bg"], "rx": "8"})

    t = ET.SubElement(svg, "text", {"x": str(width // 2), "y": "35", "text-anchor": "middle", "font-size": "20", "font-weight": "bold", "fill": COLORS["fill"]})
    t.text = title

    n = max(len(entities), 1)
    box_w = 180
    gap = min((width - n * box_w) / (n + 1), 40)
    y_top = 80

    centers = []
    for i, ent in enumerate(entities):
        attrs = ent.get("attrs", [])
        box_h = 50 + max(len(attrs) * 20, 20)
        ex = gap + i * (box_w + gap)
        ey = y_top

        ET.SubElement(svg, "rect", {"x": str(ex), "y": str(ey), "width": str(box_w), "height": str(box_h), "rx": "6", "fill": COLORS["alt"], "stroke": COLORS["stroke"], "stroke-width": "2"})
        ename = ET.SubElement(svg, "text", {"x": str(ex + box_w / 2), "y": str(ey + 22), "text-anchor": "middle", "font-size": "14", "font-weight": "bold", "fill": COLORS["fill"]})
        ename.text = ent.get("name", "")
        ET.SubElement(svg, "line", {"x1": str(ex + 10), "y1": str(ey + 32), "x2": str(ex + box_w - 10), "y2": str(ey + 32), "stroke": COLORS["stroke"], "stroke-width": "1"})

        for j, attr in enumerate(attrs):
            at = ET.SubElement(svg, "text", {"x": str(ex + 12), "y": str(ey + 50 + j * 20), "font-size": "11", "fill": COLORS["text"]})
            at.text = f"  {attr}"

        centers.append((ex + box_w / 2, ey + box_h))

    # Relationships
    for rel in relationships:
        fi = rel.get("from", 0)
        ti = rel.get("to", 0)
        label = rel.get("label", "")
        x1, y1 = centers[fi] if fi < len(centers) else (width // 2, y_top)
        x2, y2 = centers[ti] if ti < len(centers) else (width // 2, y_top)
        mid_y = y1 + (y2 - y1) / 2 + 30

        ET.SubElement(svg, "line", {"x1": str(x1), "y1": str(y1), "x2": str(x2), "y2": str(mid_y), "stroke": COLORS["line"], "stroke-width": "1.5", "stroke-dasharray": "4,3"})
        lbl = ET.SubElement(svg, "text", {"x": str((x1 + x2) / 2), "y": str(mid_y - 5), "text-anchor": "middle", "font-size": "11", "fill": COLORS["fill"], "font-weight": "bold"})
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
