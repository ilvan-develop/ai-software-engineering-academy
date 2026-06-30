#!/usr/bin/env python3
"""
comparison.py
Gera infografico de comparacao em SVG.

Exemplo de entrada:
{
  "title": "Discovery vs Delivery",
  "left": {"label": "Discovery", "items": ["Baixo custo", "Alta incerteza"]},
  "right": {"label": "Delivery", "items": ["Alto custo", "Baixa incerteza"]},
  "center": ["Perguntas", "Hipoteses", "Validacao"]
}
"""

import xml.etree.ElementTree as ET
from typing import Any


def create_svg(data: dict[str, Any], width: int = 800, height: int = 400) -> str:
    title = data.get("title", "Comparação")
    left = data.get("left", {})
    right = data.get("right", {})
    center = data.get("center", [])

    left_label = left.get("label", "A")
    left_items = left.get("items", [])
    right_label = right.get("label", "B")
    right_items = right.get("items", [])

    ns = "http://www.w3.org/2000/svg"
    svg = ET.Element("svg", {
        "xmlns": ns,
        "viewBox": f"0 0 {width} {height}",
        "width": str(width),
        "height": str(height),
        "font-family": "Segoe UI, sans-serif",
    })

    # Background
    ET.SubElement(svg, "rect", {
        "x": "0", "y": "0", "width": str(width), "height": str(height),
        "fill": "#FAFAFA", "rx": "8"
    })

    # Title
    title_el = ET.SubElement(svg, "text", {
        "x": str(width // 2), "y": "40",
        "text-anchor": "middle", "font-size": "24", "font-weight": "bold",
        "fill": "#1A237E"
    })
    title_el.text = title

    # Left box
    ET.SubElement(svg, "rect", {
        "x": "40", "y": "70", "width": "300", "height": "300",
        "fill": "#E3F2FD", "stroke": "#1A237E", "stroke-width": "2", "rx": "8"
    })
    left_title = ET.SubElement(svg, "text", {
        "x": "190", "y": "110", "text-anchor": "middle",
        "font-size": "20", "font-weight": "bold", "fill": "#1A237E"
    })
    left_title.text = left_label

    y = 150
    for item in left_items:
        circle = ET.SubElement(svg, "circle", {
            "cx": "70", "cy": str(y - 6), "r": "6", "fill": "#00BFA5"
        })
        text = ET.SubElement(svg, "text", {
            "x": "90", "y": str(y), "font-size": "16", "fill": "#212121"
        })
        text.text = item
        y += 36

    # Right box
    ET.SubElement(svg, "rect", {
        "x": "460", "y": "70", "width": "300", "height": "300",
        "fill": "#E8F5E9", "stroke": "#2E7D32", "stroke-width": "2", "rx": "8"
    })
    right_title = ET.SubElement(svg, "text", {
        "x": "610", "y": "110", "text-anchor": "middle",
        "font-size": "20", "font-weight": "bold", "fill": "#2E7D32"
    })
    right_title.text = right_label

    y = 150
    for item in right_items:
        circle = ET.SubElement(svg, "circle", {
            "cx": "490", "cy": str(y - 6), "r": "6", "fill": "#00BFA5"
        })
        text = ET.SubElement(svg, "text", {
            "x": "510", "y": str(y), "font-size": "16", "fill": "#212121"
        })
        text.text = item
        y += 36

    # Center arrows / shared concepts
    if center:
        cy = 220
        for i, concept in enumerate(center):
            offset = (i - len(center) / 2 + 0.5) * 40
            ET.SubElement(svg, "path", {
                "d": f"M 350 {cy + offset} L 450 {cy + offset}",
                "stroke": "#9E9E9E", "stroke-width": "2",
                "marker-end": "url(#arrowhead)"
            })
            label = ET.SubElement(svg, "text", {
                "x": str(width // 2), "y": str(int(cy + offset) - 8),
                "text-anchor": "middle", "font-size": "12", "fill": "#757575"
            })
            label.text = concept

        # Arrow marker definition
        defs = ET.SubElement(svg, "defs")
        marker = ET.SubElement(defs, "marker", {
            "id": "arrowhead", "markerWidth": "10", "markerHeight": "7",
            "refX": "9", "refY": "3.5", "orient": "auto"
        })
        ET.SubElement(marker, "polygon", {
            "points": "0 0, 10 3.5, 0 7", "fill": "#9E9E9E"
        })

    return ET.tostring(svg, encoding="unicode")


def main():
    import argparse
    import json
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
    from pathlib import Path
    main()
