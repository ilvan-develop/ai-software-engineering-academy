#!/usr/bin/env python3
"""
comparison_matrix.py
Gera matriz de comparacao em SVG.

Exemplo de entrada:
{
  "engine": "comparison_matrix",
  "title": "Frameworks Frontend",
  "rows": ["React", "Vue", "Angular"],
  "columns": ["Curva", "Performance", "Ecossistema"],
  "scores": {
    "React": {"Curva": 3, "Performance": 4, "Ecossistema": 5},
    "Vue": {"Curva": 4, "Performance": 4, "Ecossistema": 3},
    "Angular": {"Curva": 2, "Performance": 3, "Ecossistema": 5}
  }
}
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


def score_color(score: int, max_score: int) -> str:
    if score >= 4:
        return "#2E7D32"
    if score >= 3:
        return "#F57F17"
    return "#C62828"


def create_svg(data: dict[str, Any], width: int = 800, height: int = 400) -> str:
    title = data.get("title", "Comparison Matrix")
    rows = data.get("rows", [])
    columns = data.get("columns", [])
    scores = data.get("scores", {})

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

    margin_x = 140
    margin_y = 80
    col_w = (width - margin_x - 40) / max(len(columns), 1)
    row_h = 50

    # Header row
    for j, col in enumerate(columns):
        x = margin_x + j * col_w
        ET.SubElement(svg, "rect", {
            "x": str(x), "y": str(margin_y), "width": str(col_w), "height": str(row_h),
            "fill": "#1A237E"
        })
        col_text = ET.SubElement(svg, "text", {
            "x": str(x + col_w / 2), "y": str(margin_y + row_h / 2 + 5),
            "text-anchor": "middle", "font-size": "13", "font-weight": "bold", "fill": "#FFFFFF"
        })
        col_text.text = col

    # Row labels and scores
    for i, row in enumerate(rows):
        y = margin_y + (i + 1) * row_h

        # Row label
        ET.SubElement(svg, "rect", {
            "x": "20", "y": str(y), "width": str(margin_x - 20), "height": str(row_h),
            "fill": "#E3F2FD", "stroke": "#BDBDBD", "stroke-width": "0.5"
        })
        row_text = ET.SubElement(svg, "text", {
            "x": str(margin_x - 30), "y": str(y + row_h / 2 + 5),
            "text-anchor": "end", "font-size": "14", "font-weight": "bold", "fill": "#1A237E"
        })
        row_text.text = row

        row_scores = scores.get(row, {})
        for j, col in enumerate(columns):
            x = margin_x + j * col_w
            score = row_scores.get(col, 0)
            color = score_color(score, 5)

            ET.SubElement(svg, "rect", {
                "x": str(x), "y": str(y), "width": str(col_w), "height": str(row_h),
                "fill": "#FFFFFF", "stroke": "#BDBDBD", "stroke-width": "0.5"
            })

            # Score circle
            ET.SubElement(svg, "circle", {
                "cx": str(x + col_w / 2), "cy": str(y + row_h / 2),
                "r": "16", "fill": color
            })
            score_text = ET.SubElement(svg, "text", {
                "x": str(x + col_w / 2), "y": str(y + row_h / 2 + 5),
                "text-anchor": "middle", "font-size": "14", "font-weight": "bold", "fill": "#FFFFFF"
            })
            score_text.text = str(score)

    return ET.tostring(svg, encoding="unicode")


def main():
    import argparse
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
