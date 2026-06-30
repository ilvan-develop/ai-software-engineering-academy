#!/usr/bin/env python3
"""
build_component_pdf.py
Pipeline demonstração da nova arquitetura editorial:

  Markdown
    ↓
  md_to_components.py  →  Component Tree (YAML/JSON)
    ↓
  Renderer (fpdf2 / Typst)  →  PDF

Uso:
  python scripts/build_component_pdf.py --input aula.md --output livro.pdf --renderer fpdf2
  python scripts/build_component_pdf.py --input aula.md --output livro.pdf --renderer typst
"""

import argparse
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def run(cmd: list[str]) -> bool:
    print(f"  $ {' '.join(cmd)}")
    result = subprocess.run(cmd)
    return result.returncode == 0


def main():
    parser = argparse.ArgumentParser(description="Build PDF via Component Tree")
    parser.add_argument("--input", required=True, help="Arquivo Markdown de entrada")
    parser.add_argument("--output", required=True, help="Arquivo PDF de saída")
    parser.add_argument("--renderer", choices=["fpdf2", "typst"], default="fpdf2")
    parser.add_argument("--title", default="AI Software Engineering Academy")
    parser.add_argument("--author", default="AI Software Engineering Academy")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    tree_path = output_path.with_suffix(".tree.yaml")

    if not input_path.exists():
        print(f"ERRO: entrada não encontrada: {input_path}")
        sys.exit(1)

    print("\n[1/3] Markdown -> Component Tree")
    if not run([
        sys.executable, str(PROJECT_ROOT / "scripts" / "md_to_components.py"),
        f"--input={input_path}",
        f"--output={tree_path}",
        "--format=yaml",
    ]):
        print("ERRO: falha na conversão para Component Tree")
        sys.exit(1)

    print("\n[2/3] Component Tree -> PDF")
    if args.renderer == "fpdf2":
        ok = run([
            sys.executable, str(PROJECT_ROOT / "scripts" / "renderers" / "fpdf2_components.py"),
            f"--input={tree_path}",
            f"--output={output_path}",
        ])
    else:
        ok = run([
            sys.executable, str(PROJECT_ROOT / "scripts" / "build_pdf_typst.py"),
            f"--input={tree_path}",
            f"--output={output_path}",
            f"--title={args.title}",
            f"--author={args.author}",
        ])

    if not ok:
        print("ERRO: falha na renderização do PDF")
        sys.exit(1)

    print(f"\n[3/3] OK: {output_path}")


if __name__ == "__main__":
    main()
