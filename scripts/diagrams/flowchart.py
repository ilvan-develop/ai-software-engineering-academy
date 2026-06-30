#!/usr/bin/env python3
"""
flowchart.py
Gera fluxograma horizontal simples em SVG.

Exemplo de entrada:
{
  "title": "Processo de Discovery",
  "steps": ["Oportunidade", "Pesquisa", "Ideacao", "Prototipacao", "Validacao"]
}
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


def create_svg(data: dict[str, Any], width: int = 900, height: int = 240) -> str:
    title = data.get("title", "Fluxograma")
    steps = data.get("steps", [])

    ns = "http://www.w3.org/2000/svg"
    svg = ET.Element("svg", {
        "xmlns": ns,
        "viewBox": f"0 0 {width} {height}",
        "width": str(width),
        "height": str(height),
        "font-family": "Segoe UI, sans-serif",
    })

    ET.SubElement(svg, "rect", {
        "x": "0", "y": "0", "width": str(width), "height": str(height),
        "fill": "#FAFAFA", "rx": "8"
    })

    title_el = ET.SubElement(svg, "text", {
        "x": str(width // 2), "y": "40",
        "text-anchor": "middle", "font-size": "22", "font-weight": "bold", "fill": "#1A237E"
    })
    title_el.text = title

    n = len(steps)
    if n == 0:
        return ET.tostring(svg, encoding="unicode")

    margin = 60
    usable_width = width - 2 * margin
    box_w = usable_width // n - 20
    box_h = 70
    y = 110

    for i, step in enumerate(steps):
        x = margin + i * (box_w + 20)

        ET.SubElement(svg, "rect", {
            "x": str(x), "y": str(y), "width": str(box_w), "height": str(box_h),
            "fill": "#E3F2FD", "stroke": "#1A237E", "stroke-width": "2", "rx": "6"
        })

        text = ET.SubElement(svg, "text", {
            "x": str(x + box_w // 2), "y": str(y + box_h // 2 + 6),
            "text-anchor": "middle", "font-size": "14", "font-weight": "600", "fill": "#1A237E"
        })
        text.text = step

        if i < n - 1:
            arrow_x1 = x + box_w
            arrow_x2 = x + box_w + 20
            ET.SubElement(svg, "line", {
                "x1": str(arrow_x1), "y1": str(y + box_h // 2),
                "x2": str(arrow_x2), "y2": str(y + box_h // 2),
                "stroke": "#00BFA5", "stroke-width": "3",
                "marker-end": "url(#arrow-green)"
            })

    # Arrow marker
    defs = ET.SubElement(svg, "defs")
    marker = ET.SubElement(defs, "marker", {
        "id": "arrow-green", "markerWidth": "10", "markerHeight": "7",
        "refX": "9", "refY": "3.5", "orient": "auto"
    })
    ET.SubElement(marker, "polygon", {
        "points": "0 0, 10 3.5, 0 7", "fill": "#00BFA5"
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
    main()
