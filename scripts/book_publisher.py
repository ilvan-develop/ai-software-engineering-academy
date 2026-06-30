#!/usr/bin/env python3
"""
book_publisher.py
Orquestrador completo do pipeline de publicação.
Roda book_architect + todos os builders sequencialmente.
"""

import argparse
import sys
import subprocess
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cache import BuildCache


def check_pandoc() -> bool:
    try:
        subprocess.run(["pandoc", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def run_script(script_path: str, *args) -> bool:
    cmd = [sys.executable, str(script_path)] + list(args)
    print(f"  $ {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=False)
    return result.returncode == 0


def main():
    parser = argparse.ArgumentParser(description="Book Publisher — Pipeline Completo")
    parser.add_argument("--manifest", required=True, help="Book Manifest YAML")
    parser.add_argument(
        "--formats",
        default="docx,epub,pdf-digital",
        help="Formatos separados por vírgula: docx,epub,pdf-digital,pdf-print,all",
    )
    parser.add_argument("--no-architect", action="store_true", help="Pular fase de arquitetura")
    parser.add_argument("--no-cover", action="store_true", help="Pular capa no PDF/DOCX")
    parser.add_argument("--toc", action="store_true", help="Incluir sumário no DOCX")
    parser.add_argument("--force", action="store_true", help="Ignora cache e regenera todos os formatos")
    args = parser.parse_args()

    scripts_dir = Path(__file__).resolve().parent
    manifest_path = Path(args.manifest)

    if not manifest_path.exists():
        print(f"ERRO: Manifest não encontrado: {manifest_path}")
        sys.exit(1)

    import yaml
    with open(manifest_path, encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    book = manifest["book"]
    book_id = book["id"]
    title = book["title"]
    subtitle = book.get("subtitle", "")
    author = book["author"]

    # Output dir base
    output_base = Path("knowledge-factory/products/books") / book_id

    print(f"\n{'='*60}")
    print(f"  [BOOK] Book Publisher: {title}")
    print(f"  ID: {book_id}")
    print(f"  Formatos: {args.formats}")
    print(f"{'='*60}\n")

    # Phase 1: Architect
    if not args.no_architect:
        print("Fase 1/2: Book Architect (agregando módulos)...")
        ok = run_script(
            scripts_dir / "book_architect.py",
            f"--manifest={manifest_path}",
            f"--output={output_base.parent}",
        )
        if not ok:
            print("ERRO: Book Architect falhou.")
            sys.exit(1)
        print()
    else:
        print("(Fase 1 pulada via --no-architect)\n")

    # Input: compiled/book.md
    compiled_md = output_base / "compiled" / "book.md"
    if not compiled_md.exists():
        print(f"ERRO: Markdown compilado não encontrado: {compiled_md}")
        print("Execute sem --no-architect primeiro.")
        sys.exit(1)

    # Phase 2: Builders
    print("Fase 2/2: Gerando formatos...")
    formats = [f.strip().lower() for f in args.formats.split(",")]

    if "all" in formats:
        formats = ["docx", "epub", "pdf-digital", "pdf-print"]

    output_dir = output_base / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    cache = BuildCache()
    sources = [compiled_md]
    success = True

    def _args(*pairs):
        return [a for a in pairs if a]

    def _skip_cached(fmt: str, output_path: Path) -> bool:
        if args.force:
            return False
        if not cache.is_stale(book_id, fmt, sources):
            print(f"\n  >> {fmt.upper()}... [CACHE] Pulando (book.md nao mudou).")
            return True
        return False

    if "docx" in formats:
        output_path = output_dir / "livro.docx"
        if not _skip_cached("docx", output_path):
            print("\n  >> DOCX...")
            ok = run_script(
                scripts_dir / "build_docx.py",
                *_args(
                    f"--input={compiled_md}",
                    f"--output={output_path}",
                    f"--title={title}",
                    f"--subtitle={subtitle}",
                    f"--author={author}",
                    "--cover" if not args.no_cover else None,
                    "--toc" if args.toc else None,
                )
            )
            if ok:
                cache.mark_done(book_id, "docx", sources)
            success = success and ok

    if "epub" in formats:
        output_path = output_dir / "livro.epub"
        if not _skip_cached("epub", output_path):
            print("\n  >> EPUB...")
            ok = run_script(
                scripts_dir / "build_epub.py",
                f"--input={compiled_md}",
                f"--output={output_path}",
                f"--title={title}",
                f"--author={author}",
            )
            if ok:
                cache.mark_done(book_id, "epub", sources)
            success = success and ok

    if "pdf-digital" in formats or "pdf" in formats:
        output_path = output_dir / "livro-digital.pdf"
        if not _skip_cached("pdf-digital", output_path):
            print("\n  >> PDF Digital...")
            ok = run_script(
                scripts_dir / "build_pdf_digital.py",
                *_args(
                    f"--input={compiled_md}",
                    f"--output={output_path}",
                    f"--title={title}",
                    f"--subtitle={subtitle}",
                    f"--author={author}",
                    f"--book-id={book_id}",
                    "--cover" if not args.no_cover else None,
                )
            )
            if ok:
                cache.mark_done(book_id, "pdf-digital", sources)
            success = success and ok

    if "pdf-print" in formats:
        output_path = output_dir / "livro-grafica.pdf"
        if not _skip_cached("pdf-print", output_path):
            trim = book.get("output", {}).get("pdf_print", {}).get("trim_size", "6x9in")
            if check_pandoc():
                print("\n  >> PDF Gráfica (Pandoc + LaTeX)...")
                ok = run_script(
                    scripts_dir / "build_pdf_print.py",
                    f"--input={compiled_md}",
                    f"--output={output_path}",
                    f"--title={title}",
                    f"--author={author}",
                    f"--trim-size={trim}",
                )
            else:
                print("\n  >> Pandoc não encontrado. Usando fallback fpdf2 print-mode...")
                ok = False

            if not ok:
                print("\n  >> PDF Gráfica (fpdf2 print-mode)...")
                ok = run_script(
                    scripts_dir / "build_pdf_digital.py",
                    f"--input={compiled_md}",
                    f"--output={output_path}",
                    f"--title={title}",
                    f"--subtitle={subtitle}",
                    f"--author={author}",
                    f"--book-id={book_id}",
                    f"--trim-size={trim}",
                    "--print-mode",
                    "--cover" if not args.no_cover else None,
                )
            if ok:
                cache.mark_done(book_id, "pdf-print", sources)
            success = success and ok

    print(f"\n{'='*60}")
    if success:
        print(f"  [OK] Pipeline concluído com sucesso!")
        print(f"  [FOLDER] Output: {output_dir}")
    else:
        print(f"  ! Pipeline concluído com alguns erros.")
    print(f"{'='*60}\n")

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
