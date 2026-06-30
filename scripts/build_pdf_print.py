#!/usr/bin/env python3
"""
build_pdf_print.py
Converte Markdown -> PDF pronto para gráfica via Pandoc + LaTeX KDP template.

Requerimentos:
- Pandoc instalado (https://pandoc.org/installing.html)
- LaTeX (MiKTeX/TinyTeX) com pacotes: geometry, fontspec, titling, fancyhdr, xcolor, listings, booktabs
"""

import argparse
import sys
import subprocess
from pathlib import Path


def check_pandoc() -> bool:
    try:
        subprocess.run(["pandoc", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def build_pdf_print(
    input_path: Path,
    output_path: Path,
    template_path: Path,
    title: str,
    author: str,
    trim_size: str = "6x9in",
):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "pandoc",
        str(input_path),
        "--pdf-engine=xelatex",
        f"--template={template_path}",
        f"-V=title:{title}",
        f"-V=author:{author}",
        f"-V=trimsize:{trim_size}",
        f"-o={output_path}",
        "-f", "markdown",
        "--metadata", f"title:{title}",
        "--metadata", f"author:{author}",
    ]

    print(f"  Executando: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"  ERRO Pandoc: {result.stderr}")
        print("\n  Dica: Instale Pandoc (https://pandoc.org/) e LaTeX (MiKTeX/TinyTeX).")
        print("  Ou use 'build_pdf_digital.py' para PDF sem dependências externas.")
        return False

    print(f"  OK PDF gráfica salvo: {output_path}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Build PDF Print-ready from Markdown")
    parser.add_argument("--input", required=True, help="Arquivo Markdown de entrada")
    parser.add_argument("--output", required=True, help="Arquivo PDF de saída")
    parser.add_argument("--title", default="", help="Título do livro")
    parser.add_argument("--author", default="AI Software Engineering Academy", help="Autor")
    parser.add_argument("--trim-size", default="6x9in", help="Tamanho do livro (ex: 6x9in, 7x10in)")
    parser.add_argument(
        "--template",
        default=None,
        help="Template LaTeX personalizado (default: scripts/templates/latex_kdp.tex)",
    )
    args = parser.parse_args()

    if not check_pandoc():
        print("ERRO: Pandoc não encontrado. Instale em: https://pandoc.org/")
        print("Após instalar, certifique-se de que está no PATH.")
        sys.exit(1)

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERRO: Arquivo não encontrado: {input_path}")
        sys.exit(1)

    if args.template:
        template_path = Path(args.template)
    else:
        template_path = Path(__file__).resolve().parent / "templates" / "latex_kdp.tex"

    if not template_path.exists():
        print(f"ERRO: Template LaTeX não encontrado: {template_path}")
        sys.exit(1)

    title = args.title or input_path.stem
    print(f"  Convertendo {input_path.name} -> PDF gráfica (pandoc + xelatex)...")
    build_pdf_print(input_path, Path(args.output), template_path, title, args.author, args.trim_size)


if __name__ == "__main__":
    main()
