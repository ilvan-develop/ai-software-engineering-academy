#!/usr/bin/env python3
"""
sequence.py
Gera diagrama de sequencia em SVG.

Entrada:
{
  "title": "Fluxo de Autenticacao",
  "participants": ["Cliente", "API", "Banco"],
  "messages": [
    {"from": 0, "to": 1, "label": "POST /login"},
    {"from": 1, "to": 2, "label": "SELECT * FROM users"},
    {"from": 2, "to": 1, "label": "user data"},
    {"from": 1, "to": 0, "label": "200 OK + JWT"}
  ]
}
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

COLORS = {"fill": "#1A237E", "alt": "#00BFA5", "bg": "#FAFAFA", "text": "#212121", "line": "#BDBDBD"}


def create_svg(data: dict[str, Any], width: int = 800, height: int = 500) -> str:
    title = data.get("title", "Diagrama de Sequencia")
    participants = data.get("participants", [])
    messages = data.get("messages", [])

    ns = "http://www.w3.org/2000/svg"
    svg = ET.Element("svg", {
        "xmlns": ns, "viewBox": f"0 0 {width} {height}",
        "width": str(width), "height": str(height),
        "font-family": "Segoe UI, sans-serif",
    })
    ET.SubElement(svg, "rect", {"x": "0", "y": "0", "width": str(width), "height": str(height), "fill": COLORS["bg"], "rx": "8"})

    # Title
    t = ET.SubElement(svg, "text", {"x": str(width // 2), "y": "35", "text-anchor": "middle", "font-size": "20", "font-weight": "bold", "fill": COLORS["fill"]})
    t.text = title

    n = max(len(participants), 2)
    col_w = (width - 100) / n
    start_x = 50
    lifeline_y = 100

    # Participant boxes and lifelines
    for i, name in enumerate(participants):
        cx = start_x + col_w * i + col_w / 2
        bw = min(len(name) * 12 + 20, col_w - 20)
        bx = cx - bw / 2
        ET.SubElement(svg, "rect", {"x": str(bx), "y": str(lifeline_y), "width": str(bw), "height": "30", "rx": "4", "fill": COLORS["fill"]})
        pt = ET.SubElement(svg, "text", {"x": str(cx), "y": str(lifeline_y + 20), "text-anchor": "middle", "font-size": "12", "fill": "white", "font-weight": "bold"})
        pt.text = name
        ET.SubElement(svg, "line", {"x1": str(cx), "y1": str(lifeline_y + 30), "x2": str(cx), "y2": str(height - 40), "stroke": COLORS["line"], "stroke-width": "2", "stroke-dasharray": "6,4"})

    # Messages
    msg_y = lifeline_y + 60
    for msg in messages:
        fi = msg.get("from", 0)
        ti = msg.get("to", 0)
        label = msg.get("label", "")
        x1 = start_x + col_w * fi + col_w / 2
        x2 = start_x + col_w * ti + col_w / 2
        mx = (x1 + x2) / 2

        if fi == ti:
            xr = x1 - 20
            ET.SubElement(svg, "path", {"d": f"M {x1} {msg_y} Q {xr} {msg_y} {xr} {msg_y + 15} L {x1} {msg_y + 15}", "fill": "none", "stroke": "#555", "stroke-width": "1.5"})
            lbl = ET.SubElement(svg, "text", {"x": str(xr - 10), "y": str(msg_y + 10), "text-anchor": "end", "font-size": "10", "fill": COLORS["text"]})
        else:
            arrow = 1 if ti > fi else -1
            if arrow > 0:
                ET.SubElement(svg, "line", {"x1": str(x1), "y1": str(msg_y), "x2": str(x2), "y2": str(msg_y), "stroke": "#555", "stroke-width": "1.5"})
                ET.SubElement(svg, "polygon", {"points": f"{x2},{msg_y} {x2 - 8},{msg_y - 4} {x2 - 8},{msg_y + 4}", "fill": "#555"})
                lbl = ET.SubElement(svg, "text", {"x": str(mx), "y": str(msg_y - 8), "text-anchor": "middle", "font-size": "10", "fill": COLORS["fill"], "font-weight": "bold"})
            else:
                ET.SubElement(svg, "line", {"x1": str(x1), "y1": str(msg_y), "x2": str(x2), "y2": str(msg_y), "stroke": "#888", "stroke-width": "1.5", "stroke-dasharray": "4,3"})
                lbl = ET.SubElement(svg, "text", {"x": str(mx), "y": str(msg_y - 8), "text-anchor": "middle", "font-size": "10", "fill": "#555", "font-style": "italic"})
        lbl.text = label
        msg_y += 40

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
