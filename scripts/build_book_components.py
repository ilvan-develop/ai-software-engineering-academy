#!/usr/bin/env python3
"""
build_book_components.py
Orquestra a geracao de um livro completo usando a nova arquitetura component-based.

Uso:
  python scripts/build_book_components.py \
    --book=product-design-book \
    --renderer=fpdf2
"""

import argparse
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

from cache import BuildCache


def run(cmd: list[str]) -> bool:
    print(f"  $ {' '.join(cmd)}")
    result = subprocess.run(cmd)
    return result.returncode == 0


def main():
    parser = argparse.ArgumentParser(description="Build book via Component Tree")
    parser.add_argument("--book", required=True, help="ID do livro em knowledge-factory/products/books/")
    parser.add_argument("--renderer", choices=["fpdf2", "typst"], default="fpdf2")
    parser.add_argument("--title", default="AI Software Engineering Academy")
    parser.add_argument("--author", default="AI Software Engineering Academy")
    parser.add_argument("--force", action="store_true", help="Ignora cache e regenera")
    args = parser.parse_args()

    book_dir = PROJECT_ROOT / "knowledge-factory" / "products" / "books" / args.book
    input_md = book_dir / "compiled" / "book.md"
    output_pdf = book_dir / "output" / f"{args.book}-component-pipeline.pdf"

    if not input_md.exists():
        print(f"ERRO: livro nao encontrado: {input_md}")
        print("Execute scripts/book_architect.py primeiro.")
        sys.exit(1)

    cache = BuildCache()
    cache_key = f"{args.book}:{args.renderer}"
    if not args.force and not cache.is_stale(cache_key, "component_pipeline", [input_md]):
        print(f"\n[Build Book] {args.book} via component pipeline ({args.renderer})")
        print(f"  [CACHE] book.md nao mudou. Pulando geracao de PDF.")
        print(f"\nOK (cache): {output_pdf}")
        return

    print(f"\n[Build Book] {args.book} via component pipeline ({args.renderer})")
    ok = run([
        sys.executable, str(PROJECT_ROOT / "scripts" / "build_component_pdf.py"),
        f"--input={input_md}",
        f"--output={output_pdf}",
        f"--renderer={args.renderer}",
        f"--title={args.title}",
        f"--author={args.author}",
    ])

    if not ok:
        sys.exit(1)

    cache.mark_done(cache_key, "component_pipeline", [input_md])
    print(f"\nOK: {output_pdf}")


if __name__ == "__main__":
    main()
