#!/usr/bin/env python3
"""
architecture.py
Gera diagrama de arquitetura em SVG (caixas e setas).

Exemplo de entrada:
{
  "engine": "architecture",
  "title": "Arquitetura de Referencia",
  "layers": [
    {
      "label": "Frontend",
      "nodes": ["Next.js", "React"],
      "y": 80
    },
    {
      "label": "Backend",
      "nodes": ["API Gateway", "Auth Service", "Core API"],
      "y": 220
    },
    {
      "label": "Dados",
      "nodes": ["PostgreSQL", "Redis"],
      "y": 360
    }
  ],
  "connections": [
    {"from": "Next.js", "to": "API Gateway"},
    {"from": "API Gateway", "to": "Core API"},
    {"from": "Core API", "to": "PostgreSQL"}
  ]
}
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


def create_svg(data: dict[str, Any], width: int = 900, height: int = 500) -> str:
    title = data.get("title", "Architecture")
    layers = data.get("layers", [])
    connections = data.get("connections", [])

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

    node_positions = {}
    node_width = 130
    node_height = 50
    colors = ["#E3F2FD", "#E8F5E9", "#FFF3E0"]

    for i, layer in enumerate(layers):
        label = layer.get("label", "")
        nodes = layer.get("nodes", [])
        y = layer.get("y", 100 + i * 130)
        color = colors[i % len(colors)]

        # Layer label
        layer_text = ET.SubElement(svg, "text", {
            "x": "30", "y": str(y + node_height / 2 + 5),
            "text-anchor": "start", "font-size": "12", "font-weight": "bold", "fill": "#757575"
        })
        layer_text.text = label

        n = len(nodes)
        total_w = n * node_width + (n - 1) * 30
        start_x = (width - total_w) / 2

        for j, node in enumerate(nodes):
            x = start_x + j * (node_width + 30)

            ET.SubElement(svg, "rect", {
                "x": str(x), "y": str(y), "width": str(node_width), "height": str(node_height),
                "fill": color, "stroke": "#1A237E", "stroke-width": "2", "rx": "6"
            })

            node_text = ET.SubElement(svg, "text", {
                "x": str(x + node_width / 2), "y": str(y + node_height / 2 + 5),
                "text-anchor": "middle", "font-size": "13", "font-weight": "600", "fill": "#1A237E"
            })
            node_text.text = node

            node_positions[node] = (x + node_width / 2, y + node_height / 2)

    # Connections
    defs = ET.SubElement(svg, "defs")
    marker = ET.SubElement(defs, "marker", {
        "id": "arrowhead", "markerWidth": "10", "markerHeight": "7",
        "refX": "9", "refY": "3.5", "orient": "auto"
    })
    ET.SubElement(marker, "polygon", {
        "points": "0 0, 10 3.5, 0 7", "fill": "#757575"
    })

    for conn in connections:
        src = conn.get("from")
        dst = conn.get("to")
        if src in node_positions and dst in node_positions:
            x1, y1 = node_positions[src]
            x2, y2 = node_positions[dst]
            ET.SubElement(svg, "line", {
                "x1": str(x1), "y1": str(y1 + node_height / 2),
                "x2": str(x2), "y2": str(y2 - node_height / 2),
                "stroke": "#757575", "stroke-width": "2",
                "marker-end": "url(#arrowhead)"
            })

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
