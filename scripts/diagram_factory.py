#!/usr/bin/env python3
"""
diagram_factory.py
Orquestrador de geracao de diagramas e infograficos em SVG.

Arquitetura:
  Input JSON/YAML descrevendo o diagrama
    ↓
  diagram_factory.py seleciona o engine certo
    ↓
  SVG de alta resolucao

Engines suportados:
  - comparison  (Python nativo)
  - timeline    (Python nativo)
  - flowchart   (Python nativo)
  - mermaid     (externo, se disponivel)
  - graphviz    (externo, se disponivel)
  - d2          (externo, se disponivel)
  - plantuml    (externo, se disponivel)
"""

import argparse
import json
import shutil
import subprocess
import sys
import yaml
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DIAGRAMS_DIR = PROJECT_ROOT / "scripts" / "diagrams"


def engine_available(name: str) -> bool:
    return shutil.which(name) is not None


def generate_native(engine: str, data: dict, output_path: Path) -> bool:
    script = DIAGRAMS_DIR / f"{engine}.py"
    if not script.exists():
        print(f"ERRO: gerador nativo nao encontrado: {script}")
        return False

    input_path = output_path.with_suffix(".input.json")
    input_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    result = subprocess.run([
        sys.executable, str(script),
        f"--input={input_path}",
        f"--output={output_path}",
    ], capture_output=True, text=True)

    input_path.unlink(missing_ok=True)

    if result.returncode != 0:
        print(f"ERRO {engine}: {result.stderr}")
        return False

    print(f"OK SVG {engine}: {output_path}")
    return True


def generate_mermaid(data: dict, output_path: Path) -> bool:
    if not engine_available("mmdc") and not engine_available("mermaid-cli"):
        print("Mermaid CLI (mmdc) nao encontrado. Pulando.")
        return False
    # TODO: implementar chamada ao mmdc
    return False


def generate_graphviz(data: dict, output_path: Path) -> bool:
    if not engine_available("dot"):
        print("Graphviz (dot) nao encontrado. Pulando.")
        return False
    # TODO: implementar chamada ao dot
    return False


def generate_diagram(input_path: Path, output_path: Path, engine: str | None = None) -> bool:
    with open(input_path, encoding="utf-8") as f:
        if input_path.suffix == ".json":
            data = json.load(f)
        else:
            data = yaml.safe_load(f)

    requested_engine = engine or data.get("engine", "comparison")

    native_engines = {"comparison", "timeline", "flowchart", "mindmap", "comparison_matrix", "architecture", "sequence", "er_diagram", "c4_model", "gantt", "bpmn"}
    if requested_engine in native_engines:
        return generate_native(requested_engine, data, output_path)

    if requested_engine == "mermaid":
        return generate_mermaid(data, output_path)
    if requested_engine == "graphviz":
        return generate_graphviz(data, output_path)

    print(f"ERRO: engine desconhecido: {requested_engine}")
    return False


def main():
    parser = argparse.ArgumentParser(description="Diagram Factory — SVG generator")
    parser.add_argument("--input", required=True, help="JSON/YAML descrevendo o diagrama")
    parser.add_argument("--output", required=True, help="Caminho do SVG de saida")
    parser.add_argument("--engine", help="Forcar engine (comparison, timeline, flowchart, mermaid, graphviz)")
    args = parser.parse_args()

    ok = generate_diagram(Path(args.input), Path(args.output), args.engine)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
