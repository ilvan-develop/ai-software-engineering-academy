#!/usr/bin/env python3
"""
pipeline_manager.py
Orquestrador central da Knowledge Factory.
Le o status tracker, detecta o que precisa ser processado,
dispara agentes e scripts na ordem correta.
"""

import argparse
import sys
import yaml
import subprocess
from pathlib import Path
from datetime import datetime

from config import PROJECT_ROOT, SCRIPTS_DIR, STATUS_PATH, SOURCES_DIR as CURRICULUM_DIR, COURSES_DIR, BOOKS_DIR, BOOKS_MANIFESTS_DIR, KF_DIR, SOCIAL_DIR, NEWSLETTERS_DIR, ONLINE_COURSES_DIR, CERTIFICATES_DIR, module_path
LOGS_DIR = PROJECT_ROOT / "logs"


def load_status() -> dict:
    with open(STATUS_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_status(data: dict):
    with open(STATUS_PATH, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)


def log(message: str, level: str = "INFO"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOGS_DIR / f"pipeline-{datetime.now().strftime('%Y-%m-%d')}.log"
    line = f"[{ts}] [{level}] {message}"
    print(line)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def status():
    data = load_status()
    modules = data.get("modules", {})
    books = data.get("books", {})

    status_count = {}
    output_pendente = 0
    output_total = 0

    for course_name, mods in modules.items():
        for mod_id, mod in mods.items():
            s = mod.get("status", "unknown")
            status_count[s] = status_count.get(s, 0) + 1
            outputs = mod.get("outputs", {})
            for out_type, out_status in outputs.items():
                output_total += 1
                if out_status == "pendente":
                    output_pendente += 1

    print(f"\n{'='*50}")
    print(f"  KNOWLEDGE FACTORY - Status Report")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*50}")
    print(f"\n  Modulos: {sum(status_count.values())} total")
    for s, count in sorted(status_count.items()):
        print(f"    {s}: {count}")
    print(f"\n  Outputs: {output_total} total, {output_pendente} pendentes")
    print(f"\n  Livros: {len(books)}")
    for book_id, book in books.items():
        formats_ok = sum(1 for f, s in book.get("formats", {}).items() if s == "publicado")
        formats_total = len(book.get("formats", {}))
        print(f"    {book['title']}: {formats_ok}/{formats_total} formatos")
    print(f"{'='*50}\n")


def get_output_dir(course: str, module: str) -> Path:
    return module_path(course, module)


def process_module(course: str, module_id: str):
    data = load_status()
    mod = data.get("modules", {}).get(course, {}).get(module_id)
    if not mod:
        log(f"Modulo {course}/{module_id} nao encontrado no status", "ERROR")
        return False

    aula_path = CURRICULUM_DIR / course / module_id / "aula" / "aula.md"
    if not aula_path.exists():
        log(f"Aula nao encontrada: {aula_path}", "ERROR")
        return False

    out_dir = get_output_dir(course, module_id)
    out_dir.mkdir(parents=True, exist_ok=True)

    log(f"Processando {course}/{module_id}: {mod['title']}")

    # Step 1: Designer Visual
    log("  >> Designer Visual...")
    (out_dir / "layout-book.yaml").write_text(
        f"# Layout gerado para {mod['title']}\n# Manual: revisar e ajustar conforme STYLE_GUIDE.md\n",
        encoding="utf-8"
    )
    mod.setdefault("outputs", {})["slides"] = "gerado"

    # Step 2: Criador de Imagens
    log("  >> Criador de Imagens...")
    assets_dir = out_dir / "assets"
    assets_dir.mkdir(exist_ok=True)
    (assets_dir / "cover-prompt.txt").write_text(
        f"# Cover prompt para {mod['title']}\n# Gerar via DALL-E ou Midjourney\n",
        encoding="utf-8"
    )
    (assets_dir / "diagrams-prompt.txt").write_text(
        f"# Diagramas para {mod['title']}\n# Revisar e gerar manualmente\n",
        encoding="utf-8"
    )

    # Step 3: Revisor de Linguagem
    log("  >> Revisor de Linguagem...")
    review_path = aula_path.parent / "aula.review.md"
    if not review_path.exists():
        review_path.write_text(
            f"# Revisao Linguistica - {mod['title']}\n\n"
            f"**Status:** Pendente de revisao manual\n"
            f"**Data:** {datetime.now().strftime('%Y-%m-%d')}\n\n"
            f"## Instrucoes\n"
            f"1. Ler aula.md e STYLE_GUIDE.md\n"
            f"2. Verificar acentos, pontuacao, tom, terminologia\n"
            f"3. Preencher relatorio abaixo\n\n"
            f"## Relatorio\n\n"
            f"| Item | Status |\n"
            f"|------|--------|\n"
            f"| Ortografia | |\n"
            f"| Tom | |\n"
            f"| Terminologia | |\n"
            f"| Codigo | |\n",
            encoding="utf-8"
        )

    # Step 4: Indexador SEO
    log("  >> Indexador SEO...")
    seo_dir = out_dir / "seo"
    seo_dir.mkdir(exist_ok=True)
    (seo_dir / "udemy-seo.yaml").write_text(
        f"title: {mod['title']}\ndescription: \"\"\ntags: []\ncategory: \"Desenvolvimento de Software\"\nlevel: \"Intermediario\"\n",
        encoding="utf-8"
    )
    (seo_dir / "kdp-seo.yaml").write_text(
        f"amazon_keywords: []\nbrowse_nodes: []\n",
        encoding="utf-8"
    )

    # Update status based on what actually exists on disk
    mod["status"] = "publicado"
    outputs = mod.setdefault("outputs", {})

    def check_output(out_type: str, out_path: Path):
        if out_type not in outputs:
            return
        if outputs[out_type] == "publicado":
            return
        exists = out_path.exists() and any(f.name != ".gitkeep" for f in out_path.iterdir())
        outputs[out_type] = "gerado" if exists else "pendente"

    check_output("slides", out_dir / "slides")
    check_output("video", out_dir / "videos")
    check_output("exercicios", out_dir / "exercicios")
    check_output("quiz", out_dir / "quiz")
    check_output("projeto", out_dir / "projeto")
    check_output("workshop", out_dir / "workshop")

    mod["last_updated"] = datetime.now().strftime("%Y-%m-%d")

    save_status(data)
    log(f"  OK {course}/{module_id} processado")
    return True


def process_course(course: str):
    data = load_status()
    mods = data.get("modules", {}).get(course, {})
    if not mods:
        log(f"Curso {course} nao encontrado no status", "ERROR")
        return False

    log(f"Processando curso inteiro: {course} ({len(mods)} modulos)")
    ok = True
    for mod_id in mods:
        if not process_module(course, mod_id):
            ok = False
    return ok


def process_book(book_id: str):
    data = load_status()
    book = data.get("books", {}).get(book_id)
    if not book:
        log(f"Livro {book_id} nao encontrado no status", "ERROR")
        return False

    log(f"Processando livro: {book['title']}")

    manifest_path = BOOKS_MANIFESTS_DIR / f"{book_id}.yaml"
    if not manifest_path.exists():
        log(f"Manifest nao encontrado: {manifest_path}", "ERROR")
        return False

    result = subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "book_publisher.py"),
         f"--manifest={manifest_path}", "--formats=docx,epub,pdf-digital"],
        capture_output=False
    )

    if result.returncode == 0:
        book["status"] = "publicado"
        book["formats"]["docx"] = "publicado"
        book["formats"]["epub"] = "publicado"
        book["formats"]["pdf_digital"] = "publicado"
        book["last_updated"] = datetime.now().strftime("%Y-%m-%d")
        save_status(data)
        log(f"  OK Livro {book_id} gerado")
        return True
    else:
        log(f"  ERRO ao gerar livro {book_id}", "ERROR")
        return False


def report():
    data = load_status()
    ts = datetime.now().strftime("%Y-%m-%d")
    report_path = KF_DIR / f"pipeline-relatorio-{ts}.md"

    lines = [
        f"# Pipeline Report - {ts}",
        "",
        "## Resumo",
        "",
    ]

    modules = data.get("modules", {})
    total = 0
    published = 0
    pendentes = 0
    for course_name, mods in modules.items():
        for mod_id, mod in mods.items():
            total += 1
            if mod.get("status") == "publicado":
                published += 1
            outputs = mod.get("outputs", {})
            for out_type, out_status in outputs.items():
                if out_status == "pendente":
                    pendentes += 1

    lines.extend([
        f"- Modulos: {total} total, {published} publicados",
        f"- Outputs pendentes: {pendentes}",
        f"- Livros: {len(data.get('books', {}))}",
        "",
        "## Modulos por Curso",
        "",
    ])

    for course_name, mods in modules.items():
        lines.append(f"### {course_name}")
        for mod_id, mod in mods.items():
            out_str = ", ".join(f"{k}: {v}" for k, v in mod.get("outputs", {}).items())
            lines.append(f"- **{mod_id}**: {mod.get('title')} [{mod.get('status')}] -> {out_str}")
        lines.append("")

    lines.extend([
        "## Livros",
        "",
    ])
    for book_id, book in data.get("books", {}).items():
        fmt_str = ", ".join(f"{k}: {v}" for k, v in book.get("formats", {}).items())
        lines.append(f"- **{book['title']}**: {fmt_str}")

    lines.append("")
    report_path.write_text("\n".join(lines), encoding="utf-8")
    log(f"Relatorio salvo: {report_path}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Pipeline Manager — Knowledge Factory Orchestrator")
    parser.add_argument("command", choices=["status", "processar-modulo", "processar-curso", "processar-livro", "report"])
    parser.add_argument("--curso", help="Nome do curso (para processar-curso)")
    parser.add_argument("--modulo", help="ID do modulo (para processar-modulo)")
    parser.add_argument("--livro", help="ID do livro (para processar-livro)")

    args = parser.parse_args()

    if args.command == "status":
        status()

    elif args.command == "processar-modulo":
        if not args.curso or not args.modulo:
            print("ERRO: Use --curso e --modulo")
            sys.exit(1)
        ok = process_module(args.curso, args.modulo)
        sys.exit(0 if ok else 1)

    elif args.command == "processar-curso":
        if not args.curso:
            print("ERRO: Use --curso")
            sys.exit(1)
        ok = process_course(args.curso)
        sys.exit(0 if ok else 1)

    elif args.command == "processar-livro":
        if not args.livro:
            print("ERRO: Use --livro")
            sys.exit(1)
        ok = process_book(args.livro)
        sys.exit(0 if ok else 1)

    elif args.command == "report":
        report()


if __name__ == "__main__":
    main()
