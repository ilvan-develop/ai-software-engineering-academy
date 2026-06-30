#!/usr/bin/env python3
"""
book_architect.py
Lê um Book Manifest (YAML), agrega módulos dos cursos,
gera front/back matter, e produz Markdown estruturado.
"""

import argparse
import sys
from pathlib import Path
import yaml
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils.template_engine import generate_frontmatter
from utils.cover_builder import CoverBuilder
from cache import BuildCache
from config import BOOKS_MANIFESTS_DIR


def load_manifest(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def find_module_dir(curriculum_base: Path, course: str, module: str) -> Path:
    course_dir = curriculum_base / course
    if not course_dir.exists():
        raise FileNotFoundError(f"Curso não encontrado: {course_dir}")

    module_path = course_dir / module
    if not module_path.exists():
        alt_module_path = course_dir / f"module-{module}"
        if alt_module_path.exists():
            return alt_module_path
        modules = [d for d in course_dir.iterdir() if d.is_dir()]
        raise FileNotFoundError(
            f"Módulo '{module}' não encontrado em {course_dir}. "
            f"Disponíveis: {[m.name for m in modules]}"
        )

    return module_path


def extract_module_content(module_path: Path) -> dict:
    aula_dir = module_path / "aula"
    if aula_dir.exists():
        md_files = list(aula_dir.glob("*.md"))
        if md_files:
            content = md_files[0].read_text(encoding="utf-8")
            readme = module_path / "README.md"
            meta = {}
            if readme.exists():
                meta_text = readme.read_text(encoding="utf-8")
                lines = meta_text.split("\n")[:10]
                for line in lines:
                    if line.startswith("# "):
                        meta["title"] = line[2:].strip()
            return {"content": content, "meta": meta, "source": str(md_files[0])}

    md_files = list(module_path.glob("*.md"))
    if md_files:
        readme = next((f for f in md_files if f.name == "README.md"), None)
        aula = next((f for f in md_files if f.name != "README.md"), md_files[0])
        content = aula.read_text(encoding="utf-8")
        return {"content": content, "meta": {}, "source": str(aula)}

    return None


def build_toc(chapters: list) -> str:
    lines = ["# Sumário\n", ""]
    for i, ch in enumerate(chapters, 1):
        ch_type = ch.get("type", "body")
        if ch_type == "frontmatter":
            lines.append(f"- {ch.get('title', ch['id'])}")
        else:
            title = ch.get("title", f"Capítulo {i}")
            lines.append(f"- **{i}. {title}**")
    lines.append("")
    return "\n".join(lines)


def build_book_content(manifest: dict, curriculum_base: Path, book_dir: Path) -> Path:
    book = manifest["book"]
    book_id = book["id"]

    compiled_dir = book_dir / "compiled"
    compiled_dir.mkdir(parents=True, exist_ok=True)

    book_header = [
        f"# {book['title']}",
        "",
        f"*{book.get('subtitle', '')}*" if book.get("subtitle") else "",
        "",
        f"**Autor:** {book['author']}",
        f"**Idioma:** {book.get('language', 'pt-BR')}",
        f"**Edição:** {book.get('edition', 1)} — {book.get('year', datetime.now().year)}",
        "",
        "---",
        "",
    ]

    chapters: list[dict] = book.get("chapters", [])
    all_content = list(book_header)
    chapter_files = []

    for i, ch in enumerate(chapters):
        ch_type = ch.get("type", "body")

        if ch_type == "frontmatter" and ch.get("auto_generate"):
            continue

        if ch_type == "backmatter" and ch.get("auto_generate"):
            continue

        if "source" not in ch:
            continue

        src = ch["source"]
        course = src["course"]
        modules_list = src.get("modules", [])

        chapter_content = [f"\n# {ch['title']}\n"]

        for module_id in modules_list:
            try:
                module_path = find_module_dir(curriculum_base, course, module_id)
                result = extract_module_content(module_path)
                if result:
                    chapter_content.append(result["content"])
                    chapter_content.append("")
            except FileNotFoundError as e:
                print(f"  [AVISO] {e}")

        chapter_text = "\n".join(chapter_content)
        filename = f"{ch['id']}.md"
        chapter_path = compiled_dir / filename
        chapter_path.write_text(chapter_text, encoding="utf-8")
        chapter_files.append(chapter_path)
        all_content.append(chapter_text)

    # Generate frontmatter
    rendered = generate_frontmatter(
        Path(__file__).resolve().parent / "templates",
        {
            "title": book["title"],
            "author": book["author"],
            "year": book.get("year", datetime.now().year),
            "isbn": book.get("distribution", {}).get("isbn", ""),
            "edition": book.get("edition", 1),
            "generate_preface": True,
            "generate_copyright": True,
            "generate_about": True,
            "course_names": [],
            "author_description": "",
        },
    )

    for key, text in rendered.items():
        if text:
            cp = compiled_dir / f"{key}.md"
            cp.write_text(text, encoding="utf-8")

    # TOC
    toc = build_toc(chapters)
    (compiled_dir / "sumario.md").write_text(toc, encoding="utf-8")

    # Full book
    book_md = "\n\n".join(all_content)
    book_path = compiled_dir / "book.md"
    book_path.write_text(book_md, encoding="utf-8")

    return book_path


def generate_cover(manifest: dict, book_dir: Path):
    book = manifest["book"]
    cover_cfg = book.get("cover", {})
    style = cover_cfg.get("style", "tech-minimalist")

    builder = CoverBuilder(book_dir / "assets")
    prompt = builder.build_prompt(book["title"], style)

    # Generate text-only cover as fallback
    builder.build_text_cover(
        title=book["title"],
        subtitle=book.get("subtitle", ""),
        author=book["author"],
    )

    # Save prompt for DALL-E / Midjourney
    prompt_path = book_dir / "assets" / "cover-prompt.txt"
    prompt_path.write_text(prompt, encoding="utf-8")

    print(f"  Cover prompt salvo em: {prompt_path}")
    print(f"  Cover texto gerado em: {book_dir / 'assets' / 'capa.png'}")


def collect_source_paths(manifest: dict, curriculum_base: Path) -> list[Path]:
    """Collect all source aula.md paths referenced by the manifest."""
    sources = []
    for ch in manifest["book"].get("chapters", []):
        src = ch.get("source")
        if not src:
            continue
        course = src.get("course")
        modules_list = src.get("modules", [])
        for module_id in modules_list:
            try:
                module_path = find_module_dir(curriculum_base, course, module_id)
                aula_dir = module_path / "aula"
                if aula_dir.exists():
                    md_files = list(aula_dir.glob("*.md"))
                    if md_files:
                        sources.append(md_files[0])
                        continue
                md_files = list(module_path.glob("*.md"))
                aula = next((f for f in md_files if f.name != "README.md"), None)
                if aula:
                    sources.append(aula)
            except FileNotFoundError:
                pass
    return sources


def main():
    parser = argparse.ArgumentParser(description="Book Architect — Agregador de Módulos")
    parser.add_argument("--manifest", required=True, help="Caminho do Book Manifest YAML")
    parser.add_argument(
        "--curriculum-base",
        default="curriculum/sources",
        help="Diretorio base dos cursos (curriculum/sources/)",
    )
    parser.add_argument(
        "--output",
        default="knowledge-factory/products/books",
        help="Diretorio de saida dos livros (knowledge-factory/products/books/)",
    )
    parser.add_argument("--force", action="store_true", help="Ignora cache e regenera")
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    if not manifest_path.exists():
        print(f"ERRO: Manifest não encontrado: {manifest_path}")
        sys.exit(1)

    manifest = load_manifest(manifest_path)
    book_id = manifest["book"]["id"]

    curriculum_base = Path(args.curriculum_base).resolve()
    if not curriculum_base.exists():
        # Try relative to project root
        curriculum_base = Path(__file__).resolve().parent.parent / args.curriculum_base

    book_dir = Path(args.output) / book_id
    book_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n[BOOK] Book Architect: {manifest['book']['title']}")
    print(f"   ID: {book_id}")
    print(f"   Output: {book_dir}\n")

    cache = BuildCache()
    sources = [manifest_path.resolve()] + collect_source_paths(manifest, curriculum_base)
    book_md_path = book_dir / "compiled" / "book.md"

    if not args.force and not cache.is_stale(book_id, "book_architect", sources):
        print("  [CACHE] Nada mudou. Pulando agregacao de modulos.")
        if not book_md_path.exists():
            print("  Aviso: book.md nao existe no cache. Reconstruindo...")
        else:
            print(f"  OK Markdown existente: {book_md_path}")
            print("  Gerando assets de capa...")
            generate_cover(manifest, book_dir)
            print(f"\n[OK] Book Architect concluído (cache)!\n   -> {book_dir}\n")
            return

    print("  Agregando módulos...")
    book_path = build_book_content(manifest, curriculum_base, book_dir)
    print(f"  OK Markdown agregado: {book_path}")
    cache.mark_done(book_id, "book_architect", sources)

    print("  Gerando assets de capa...")
    generate_cover(manifest, book_dir)

    print(f"\n[OK] Book Architect concluído!\n   -> {book_dir}\n")


if __name__ == "__main__":
    main()
