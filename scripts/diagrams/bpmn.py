#!/usr/bin/env python3
"""
bpmn.py
Gera diagrama de processo de negocios (BPMN-like) em SVG.

Entrada:
{
  "title": "Fluxo de Aprovacao",
  "steps": [
    {"type": "start", "label": "Pedido criado"},
    {"type": "task", "label": "Validar dados"},
    {"type": "gateway", "label": "Aprovado?"},
    {"type": "task", "label": "Processar pagamento"},
    {"type": "task", "label": "Enviar email"},
    {"type": "end", "label": "Concluido"}
  ],
  "connections": [
    {"from": 0, "to": 1},
    {"from": 1, "to": 2},
    {"from": 2, "to": 3, "label": "Sim"},
    {"from": 2, "to": 4, "label": "Nao"},
    {"from": 3, "to": 5},
    {"from": 4, "to": 5}
  ]
}
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

BG = "#FAFAFA"


def create_svg(data: dict[str, Any], width: int = 800, height: int = 350) -> str:
    title = data.get("title", "Processo")
    steps = data.get("steps", [])
    connections = data.get("connections", [])

    ns = "http://www.w3.org/2000/svg"
    svg = ET.Element("svg", {
        "xmlns": ns, "viewBox": f"0 0 {width} {height}",
        "width": str(width), "height": str(height),
        "font-family": "Segoe UI, sans-serif",
    })
    ET.SubElement(svg, "rect", {"x": "0", "y": "0", "width": str(width), "height": str(height), "fill": BG, "rx": "8"})

    t = ET.SubElement(svg, "text", {"x": str(width // 2), "y": "30", "text-anchor": "middle", "font-size": "18", "font-weight": "bold", "fill": "#1A237E"})
    t.text = title

    n = len(steps)
    usable_w = width - 80
    usable_h = height - 80
    step_w = min(usable_w / max(n, 1), 120)
    gap = (usable_w - n * step_w) / (n + 1) if n > 0 else 0
    y_center = 60 + usable_h / 2

    positions = []
    for i, step in enumerate(steps):
        sx = 40 + gap + i * (step_w + gap)
        sy = y_center - 22
        stype = step.get("type", "task")
        label = step.get("label", "")
        cx = sx + step_w / 2
        cy = sy + 22

        if stype == "start":
            ET.SubElement(svg, "circle", {"cx": str(cx), "cy": str(cy), "r": "22", "fill": "#C8E6C9", "stroke": "#2E7D32", "stroke-width": "2"})
            lbl = ET.SubElement(svg, "text", {"x": str(cx), "y": str(cy + 4), "text-anchor": "middle", "font-size": "8", "fill": "#1B5E20", "font-weight": "bold"})
            lbl.text = label[:12]
        elif stype == "end":
            ET.SubElement(svg, "circle", {"cx": str(cx), "cy": str(cy), "r": "22", "fill": "#FFCDD2", "stroke": "#C62828", "stroke-width": "2"})
            ET.SubElement(svg, "circle", {"cx": str(cx), "cy": str(cy), "r": "18", "fill": "none", "stroke": "#C62828", "stroke-width": "1.5"})
            lbl = ET.SubElement(svg, "text", {"x": str(cx), "y": str(cy + 4), "text-anchor": "middle", "font-size": "8", "fill": "#B71C1C", "font-weight": "bold"})
            lbl.text = label[:12]
        elif stype == "gateway":
            diamond = f"{cx},{sy} {sx + step_w},{cy} {cx},{sy + 44} {sx},{cy}"
            ET.SubElement(svg, "polygon", {"points": diamond, "fill": "#FFF9C4", "stroke": "#F57F17", "stroke-width": "2"})
            lbl = ET.SubElement(svg, "text", {"x": str(cx), "y": str(cy + 4), "text-anchor": "middle", "font-size": "8", "fill": "#F57F17", "font-weight": "bold"})
            lbl.text = "?"
        else:
            ET.SubElement(svg, "rect", {"x": str(sx), "y": str(sy), "width": str(step_w), "height": "44", "rx": "6", "fill": "#E3F2FD", "stroke": "#1565C0", "stroke-width": "2"})
            lbl = ET.SubElement(svg, "text", {"x": str(cx), "y": str(cy + 4), "text-anchor": "middle", "font-size": "9", "fill": "#1565C0", "font-weight": "bold"})
            lbl.text = label[:16]

        positions.append((cx, cy))

    # Connections
    for conn in connections:
        fi = conn.get("from", 0)
        ti = conn.get("to", 0)
        clabel = conn.get("label", "")
        if fi < len(positions) and ti < len(positions):
            x1, y1 = positions[fi]
            x2, y2 = positions[ti]
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            ET.SubElement(svg, "line", {"x1": str(x1), "y1": str(y1), "x2": str(x2), "y2": str(y2), "stroke": "#555", "stroke-width": "1.5"})
            if clabel:
                lbl = ET.SubElement(svg, "text", {"x": str(mx), "y": str(my - 10), "text-anchor": "middle", "font-size": "9", "fill": "#555", "font-weight": "bold"})
                lbl.text = clabel

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
