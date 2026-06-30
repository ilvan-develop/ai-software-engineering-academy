#!/usr/bin/env python3
"""
mindmap.py
Gera mapa mental em SVG.

Exemplo de entrada:
{
  "engine": "mindmap",
  "title": "Product Discovery",
  "center": "Discovery",
  "branches": [
    {
      "label": "Pesquisa",
      "color": "#1A237E",
      "leaves": ["Entrevistas", "Surveys", "Analytics"]
    },
    {
      "label": "Ideacao",
      "color": "#00BFA5",
      "leaves": ["Brainstorm", "JTBD", "Value Proposition"]
    }
  ]
}
"""

import json
import math
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


def create_svg(data: dict[str, Any], width: int = 800, height: int = 600) -> str:
    title = data.get("title", "Mindmap")
    center = data.get("center", "Tema")
    branches = data.get("branches", [])

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

    cx, cy = width // 2, height // 2 + 10

    # Center node
    ET.SubElement(svg, "circle", {
        "cx": str(cx), "cy": str(cy), "r": "55",
        "fill": "#1A237E", "stroke": "#0D47A1", "stroke-width": "3"
    })
    center_text = ET.SubElement(svg, "text", {
        "x": str(cx), "y": str(cy + 6),
        "text-anchor": "middle", "font-size": "16", "font-weight": "bold", "fill": "#FFFFFF"
    })
    center_text.text = center

    n = len(branches)
    radius = 180

    for i, branch in enumerate(branches):
        angle = 2 * math.pi * i / n - math.pi / 2
        bx = cx + radius * math.cos(angle)
        by = cy + radius * math.sin(angle)
        color = branch.get("color", "#00BFA5")
        label = branch.get("label", "")
        leaves = branch.get("leaves", [])

        # Branch line
        ET.SubElement(svg, "line", {
            "x1": str(cx), "y1": str(cy),
            "x2": str(bx), "y2": str(by),
            "stroke": color, "stroke-width": "3"
        })

        # Branch node
        ET.SubElement(svg, "circle", {
            "cx": str(bx), "cy": str(by), "r": "12",
            "fill": color
        })

        # Branch label
        label_x = bx + (20 if bx > cx else -20)
        anchor = "start" if bx > cx else "end"
        label_el = ET.SubElement(svg, "text", {
            "x": str(label_x), "y": str(by + 5),
            "text-anchor": anchor, "font-size": "16", "font-weight": "bold", "fill": color
        })
        label_el.text = label

        # Leaves
        leaf_radius = 120
        sub_n = max(len(leaves), 1)
        spread = math.pi / 3
        base_angle = angle

        for j, leaf in enumerate(leaves):
            sub_angle = base_angle - spread / 2 + (j * spread / max(sub_n - 1, 1))
            lx = bx + leaf_radius * math.cos(sub_angle)
            ly = by + leaf_radius * math.sin(sub_angle)

            ET.SubElement(svg, "line", {
                "x1": str(bx), "y1": str(by),
                "x2": str(lx), "y2": str(ly),
                "stroke": "#BDBDBD", "stroke-width": "1.5"
            })

            ET.SubElement(svg, "circle", {
                "cx": str(lx), "cy": str(ly), "r": "6",
                "fill": "#FFFFFF", "stroke": color, "stroke-width": "2"
            })

            leaf_x = lx + (18 if lx > bx else -18)
            leaf_anchor = "start" if lx > bx else "end"
            leaf_el = ET.SubElement(svg, "text", {
                "x": str(leaf_x), "y": str(ly + 4),
                "text-anchor": leaf_anchor, "font-size": "12", "fill": "#212121"
            })
            leaf_el.text = leaf

    return ET.tostring(svg, encoding="unicode")


def main():
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
    import argparse
    main()
