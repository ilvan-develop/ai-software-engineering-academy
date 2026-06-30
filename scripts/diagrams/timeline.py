#!/usr/bin/env python3
"""
timeline.py
Gera linha do tempo em SVG.

Exemplo de entrada:
{
  "title": "Evolucao do Design Thinking",
  "events": [
    {"year": "1969", "label": "Herbert Simon"},
    {"year": "1991", "label": "IDEO"},
    {"year": "2005", "label": "d.school Stanford"}
  ]
}
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


def create_svg(data: dict[str, Any], width: int = 800, height: int = 300) -> str:
    title = data.get("title", "Timeline")
    events = data.get("events", [])

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

    margin = 80
    usable_width = width - 2 * margin
    y_line = 160
    n = max(len(events), 1)

    # Main line
    ET.SubElement(svg, "line", {
        "x1": str(margin), "y1": str(y_line),
        "x2": str(width - margin), "y2": str(y_line),
        "stroke": "#1A237E", "stroke-width": "4"
    })

    for i, event in enumerate(events):
        x = margin + (usable_width * i) // (n - 1) if n > 1 else width // 2
        year = str(event.get("year", ""))
        label = str(event.get("label", ""))

        ET.SubElement(svg, "circle", {
            "cx": str(x), "cy": str(y_line), "r": "10",
            "fill": "#00BFA5", "stroke": "#1A237E", "stroke-width": "3"
        })

        year_text = ET.SubElement(svg, "text", {
            "x": str(x), "y": str(y_line - 30),
            "text-anchor": "middle", "font-size": "18", "font-weight": "bold", "fill": "#1A237E"
        })
        year_text.text = year

        label_text = ET.SubElement(svg, "text", {
            "x": str(x), "y": str(y_line + 45),
            "text-anchor": "middle", "font-size": "14", "fill": "#212121"
        })
        label_text.text = label

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
