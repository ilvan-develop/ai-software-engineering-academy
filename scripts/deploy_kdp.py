#!/usr/bin/env python3
"""
deploy_kdp.py
Prepara pacote de publicacao para Amazon KDP.

Gera:
  - kdp/livro-grafica.pdf        (miolo validado para KDP)
  - kdp/capa.pdf                 (capa KDP pronta)
  - kdp/metadata.csv             (metadados para upload)
  - kdp/kdp-package.zip          (pacote completo para upload manual)
  - kdp/validation-report.md     (relatorio de validacao KDP)
"""

import argparse
import sys
import csv
import zipfile
import yaml
from pathlib import Path
from datetime import datetime


KDP_REQUIREMENTS = {
    "paperback": {
        "min_pages": 24,
        "max_pages": 828,
        "min_bleed_mm": 3.0,
        "allowed_sizes": [
            "5x8in", "5.06x7.81in", "5.25x8in", "5.5x8.5in",
            "6x9in", "6.14x9.21in", "6.69x9.61in",
            "7x10in", "7.44x9.69in", "7.5x9.25in",
            "8x10in", "8.25x11in", "8.5x8.5in", "8.5x11in",
        ],
    },
    "ebook": {
        "min_pages": 0,
        "max_pages": 9999,
    },
}

MM_PER_INCH = 25.4


def load_manifest(manifest_path: Path) -> dict:
    with open(manifest_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_metadata(metadata_path: Path) -> dict:
    if metadata_path.exists():
        with open(metadata_path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    return {}


def validate_pdf(pdf_path: Path, trim_size: str) -> list:
    issues = []
    if not pdf_path.exists():
        issues.append(("[ERRO]", "PDF nao encontrado", str(pdf_path)))
        return issues

    size_kb = pdf_path.stat().st_size / 1024
    if size_kb > 200 * 1024:
        issues.append(("[AVISO]", "PDF muito grande para KDP (>200MB)", f"{size_kb/1024:.0f}MB"))

    if trim_size not in KDP_REQUIREMENTS["paperback"]["allowed_sizes"]:
        issues.append(("[AVISO]", f"Tamanho '{trim_size}' pode nao ser suportado KDP",
                       f"Tamanhos suportados: {', '.join(KDP_REQUIREMENTS['paperback']['allowed_sizes'])}"))

    return issues


def generate_metadata_csv(book: dict, metadata: dict, output_path: Path):
    fields = [
        "title", "subtitle", "author", "edition", "language",
        "isbn", "publisher", "publication_date",
        "trim_size", "page_count_est",
        "description", "categories", "keywords",
        "royalty_plan", "pricing",
    ]
    row = {
        "title": book.get("title", ""),
        "subtitle": book.get("subtitle", ""),
        "author": book.get("author", ""),
        "edition": str(book.get("edition", 1)),
        "language": book.get("language", "pt-BR"),
        "isbn": metadata.get("isbn", ""),
        "publisher": metadata.get("publisher", "AI Software Engineering Academy"),
        "publication_date": datetime.now().strftime("%Y-%m-%d"),
        "trim_size": book.get("output", {}).get("pdf_print", {}).get("trim_size", "6x9in"),
        "page_count_est": str(metadata.get("pages_estimate", 200)),
        "description": metadata.get("description", ""),
        "categories": "; ".join(metadata.get("categories", [])),
        "keywords": "; ".join(metadata.get("tags", [])),
        "royalty_plan": "70%",
        "pricing": "9.99",
    }
    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter=",")
        writer.writeheader()
        writer.writerow(row)
    print(f"  OK Metadados KDP: {output_path}")


def generate_validation_report(issues: list, output_path: Path):
    lines = [
        f"# KDP Validation Report",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"",
        f"## Issues ({len(issues)})",
        f"",
    ]
    if not issues:
        lines.append("Nenhum issue encontrado. Pronto para publicar!")
    else:
        for severity, title, detail in issues:
            lines.append(f"- {severity} **{title}:** {detail}")
    lines.append("")
    lines.append("---")
    lines.append("*Relatorio gerado automaticamente por deploy_kdp.py*")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  OK Relatorio de validacao: {output_path}")


def create_package(book_id: str, kdp_dir: Path, output_dir: Path):
    zip_path = output_dir / f"{book_id}-kdp-package.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in kdp_dir.iterdir():
            if f.suffix in (".pdf", ".csv", ".md"):
                zf.write(f, f.name)
    print(f"  OK Pacote KDP: {zip_path}")
    return zip_path


def main():
    parser = argparse.ArgumentParser(description="Preparar pacote para Amazon KDP")
    parser.add_argument("--manifest", required=True, help="Book Manifest YAML")
    parser.add_argument("--pdf", default=None, help="Caminho para PDF do miolo (opcional)")
    parser.add_argument("--cover", default=None, help="Caminho para PDF da capa (opcional)")
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    if not manifest_path.exists():
        print(f"ERRO: Manifest nao encontrado: {manifest_path}")
        sys.exit(1)

    manifest = load_manifest(manifest_path)
    book = manifest["book"]
    book_id = book["id"]
    title = book["title"]
    trim_size = book.get("output", {}).get("pdf_print", {}).get("trim_size", "6x9in")

    output_base = Path("knowledge-factory/products/books") / book_id
    kdp_dir = output_base / "kdp"
    kdp_dir.mkdir(parents=True, exist_ok=True)

    metadata = load_metadata(output_base / "metadata.yaml")

    # PDF path
    if args.pdf:
        pdf_path = Path(args.pdf)
    else:
        pdf_path = output_base / "output" / "livro-grafica.pdf"

    print(f"\n{'='*60}")
    print(f"  [KDP] Preparando publicacao: {title}")
    print(f"  ID: {book_id}")
    print(f"  Trim: {trim_size}")
    print(f"{'='*60}\n")

    # 1. Validate PDF
    print("Fase 1/4: Validando PDF para KDP...")
    issues = validate_pdf(pdf_path, trim_size)
    for severity, title_issue, detail in issues:
        print(f"  {severity} {title_issue}")

    # Copy validated PDF to kdp dir
    kdp_pdf = kdp_dir / "livro-grafica.pdf"
    if pdf_path.exists():
        import shutil
        shutil.copy2(pdf_path, kdp_pdf)
        print(f"  OK PDF copiado: {kdp_pdf}")

    # 2. Cover
    print("\nFase 2/4: Capa...")
    if args.cover:
        cover_path = Path(args.cover)
        if cover_path.exists():
            kdp_cover = kdp_dir / "capa.pdf"
            import shutil
            shutil.copy2(cover_path, kdp_cover)
            print(f"  OK Capa copiada: {kdp_cover}")
        else:
            print(f"  AVISO: Capa nao encontrada: {cover_path}")
    else:
        print("  AVISO: Nenhuma capa fornecida. Gere a capa separadamente.")

    # 3. Metadata CSV
    print("\nFase 3/4: Gerando metadados KDP...")
    csv_path = kdp_dir / "metadata.csv"
    generate_metadata_csv(book, metadata, csv_path)

    # 4. Validation report
    print("\nFase 4/4: Relatorio de validacao...")
    report_path = kdp_dir / "validation-report.md"
    generate_validation_report(issues, report_path)

    # Package
    package_path = create_package(book_id, kdp_dir, output_base / "output")

    print(f"\n{'='*60}")
    print(f"  [OK] Pacote KDP gerado!")
    print(f"  [FOLDER] {kdp_dir}")
    print(f"  [ZIP] {package_path}")
    print(f"\n  Proximos passos:")
    print(f"  1. Acesse https://kdp.amazon.com")
    print(f"  2. Crie novo titulo -> 'Paperback'")
    print(f"  3. Faca upload do miolo: {kdp_pdf}")
    print(f"  4. Preencha metadados conforme: {csv_path}")
    if (kdp_dir / "capa.pdf").exists():
        print(f"  5. Faca upload da capa: {kdp_dir / 'capa.pdf'}")
    print(f"  6. Revise e publique")
    print(f"{'='*60}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
