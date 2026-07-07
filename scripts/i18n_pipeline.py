#!/usr/bin/env python3
"""
i18n_pipeline.py
Gerencia a internacionalizacao dos modulos.
Workflow:
  1. Estrutura: cria diretorios i18n/<lang>/ para um modulo
  2. Sincroniza: copia estrutura de arquivos do modulo para i18n/<lang>/
  3. Verifica: valida integridade entre original e traducao
  4. Relatorio: mostra status de traducao de todos os modulos

USO:
  python scripts/i18n_pipeline.py status                          # status geral
  python scripts/i18n_pipeline.py init <module-id> --lang en-US   # prepara modulo para traducao
  python scripts/i18n_pipeline.py verify <module-id> --lang en-US # verifica integridade
"""

import argparse
import re
import sys
from pathlib import Path
from datetime import datetime

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "curriculum" / "sources"
STATUS_PATH = ROOT / "curriculum" / "status.yaml"
CATALOG_PATH = ROOT / "knowledge-factory" / "registry" / "catalog.yaml"

SUPPORTED_LANGS = ["en-US", "es"]
SOURCE_LANG = "pt-BR"

TRANSLATABLE_FILES = [
    "aula/aula.md",
    "slides/slides.md",
    "exercicios/exercicios.md",
    "quiz/quiz.md",
    "projeto/projeto.md",
    "METADATA.yaml",
]


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_all_module_ids() -> list[str]:
    status = load_yaml(STATUS_PATH)
    modules = status.get("modules", {})
    return [
        f"{course}/{mod_key}"
        for course, mods in modules.items()
        for mod_key in mod_data
        if isinstance({mod_key: None}.update(mods) or {mod_key: None}, dict)
    ]


def get_all_module_ids_fixed() -> list[str]:
    status = load_yaml(STATUS_PATH)
    modules = status.get("modules", {})
    result = []
    for course, mods in modules.items():
        for mod_key in mods:
            result.append(f"{course}/{mod_key}")
    return result


def init_module(module_id: str, lang: str) -> bool:
    parts = module_id.split("/")
    if len(parts) != 2:
        print(f"ERRO: module-id deve ser curso/modulo (ex: arquitetura-backend/module-13-multi-tenant)")
        return False

    course, mod = parts
    source_dir = SOURCES_DIR / course / mod
    if not source_dir.exists():
        print(f"ERRO: modulo nao encontrado: {source_dir}")
        return False

    i18n_dir = source_dir / "i18n" / lang
    i18n_dir.mkdir(parents=True, exist_ok=True)

    copied = 0
    for rel_path in TRANSLATABLE_FILES:
        src = source_dir / rel_path
        if src.exists():
            dst = i18n_dir / rel_path
            dst.parent.mkdir(parents=True, exist_ok=True)
            content = src.read_text(encoding="utf-8")
            # Add i18n header only to markdown files, not YAML
            if rel_path.endswith(".md"):
                header = f"<!-- i18n: {lang} | source: {SOURCE_LANG} | generated: {datetime.now().strftime('%Y-%m-%d')} -->\n"
                if not content.startswith("<!-- i18n:"):
                    content = header + content
            dst.write_text(content, encoding="utf-8")
            copied += 1
            print(f"  [COPY] {rel_path}")

    print(f"  -> {copied} arquivos copiados para i18n/{lang}/")

    # Se METADATA.yaml foi copiado, adicionar campo de idioma
    metadata_path = i18n_dir / "METADATA.yaml"
    if metadata_path.exists():
        meta = load_yaml(metadata_path)
        meta["lang"] = lang
        meta["source_lang"] = SOURCE_LANG
        meta["translation_status"] = "pending"
        with open(metadata_path, "w", encoding="utf-8") as f:
            yaml.dump(meta, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        print(f"  [META] METADATA.yaml atualizado com lang={lang}")

    return True


def verify_module(module_id: str, lang: str) -> dict:
    """Verifica integridade estrutural entre original e traducao."""
    parts = module_id.split("/")
    course, mod = parts
    source_dir = SOURCES_DIR / course / mod
    i18n_dir = source_dir / "i18n" / lang

    issues = []
    stats = {"files_checked": 0, "ok": 0, "warnings": 0, "errors": 0}

    for rel_path in TRANSLATABLE_FILES:
        src = source_dir / rel_path
        dst = i18n_dir / rel_path

        if not src.exists():
            continue

        stats["files_checked"] += 1

        if not dst.exists():
            issues.append(f"  [ERRO] {rel_path}: tradução nao encontrada")
            stats["errors"] += 1
            continue

        src_text = src.read_text(encoding="utf-8")
        dst_text = dst.read_text(encoding="utf-8")

        # Verificar numero de secoes (H2)
        src_sections = set(re.findall(r"^## (.+)$", src_text, re.MULTILINE))
        dst_sections = set(re.findall(r"^## (.+)$", dst_text, re.MULTILINE))

        missing_in_dst = src_sections - dst_sections
        extra_in_dst = dst_sections - src_sections

        if missing_in_dst:
            issues.append(f"  [ERRO] {rel_path}: secoes faltando na traducao: {missing_in_dst}")
            stats["errors"] += 1

        if extra_in_dst:
            issues.append(f"  [WARN] {rel_path}: secoes extras na traducao: {extra_in_dst}")
            stats["warnings"] += 1

        # Verificar code blocks preservados
        src_blocks = set(re.findall(r"```(\w*)\n", src_text))
        dst_blocks = set(re.findall(r"```(\w*)\n", dst_text))
        if src_blocks and src_blocks != dst_blocks:
            issues.append(f"  [WARN] {rel_path}: linguagens de code block diferem")
            stats["warnings"] += 1

        # Verificar links preservados
        src_links = set(re.findall(r"\[([^\]]+)\]\(([^)]+)\)", src_text))
        dst_links = set(re.findall(r"\[([^\]]+)\]\(([^)]+)\)", dst_text))
        src_urls = {url for _, url in src_links}
        dst_urls = {url for _, url in dst_links}
        missing_urls = src_urls - dst_urls
        if missing_urls:
            issues.append(f"  [WARN] {rel_path}: URLs faltando na traducao: {missing_urls}")
            stats["warnings"] += 1

        if not missing_in_dst and not extra_in_dst:
            stats["ok"] += 1

    return {"module_id": module_id, "lang": lang, "issues": issues, "stats": stats}


def status_report():
    """Gera relatorio de status de i18n para todos os modulos."""
    module_ids = get_all_module_ids_fixed()
    print(f"{'Modulo':<55} {'pt-BR':<8} {'en-US':<8} {'es':<8}")
    print("-" * 80)

    total_ptbr = 0
    total_enus = 0
    total_es = 0

    for mid in sorted(module_ids):
        parts = mid.split("/")
        course, mod = parts
        module_dir = SOURCES_DIR / course / mod

        has_ptbr = module_dir.exists()
        has_enus = (module_dir / "i18n" / "en-US").exists()
        has_es = (module_dir / "i18n" / "es").exists()

        pt_status = "[OK]" if has_ptbr else "[--]"
        en_status = "[OK]" if has_enus else "[--]"
        es_status = "[OK]" if has_es else "[--]"

        if has_ptbr:
            total_ptbr += 1
        if has_enus:
            total_enus += 1
        if has_es:
            total_es += 1

        # Display short name
        display = mid if len(mid) < 55 else mid[:52] + "..."
        print(f"{display:<55} {pt_status:<8} {en_status:<8} {es_status:<8}")

    print("-" * 80)
    print(f"{'TOTAL':<55} {total_ptbr:<8} {total_enus:<8} {total_es:<8}")


def main():
    parser = argparse.ArgumentParser(description="i18n Pipeline")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # status
    subparsers.add_parser("status", help="Status geral de i18n")

    # init
    init_parser = subparsers.add_parser("init", help="Inicializa traducao para um modulo")
    init_parser.add_argument("module_id", help="ID do modulo (curso/modulo)")
    init_parser.add_argument("--lang", default="en-US", choices=SUPPORTED_LANGS)

    # verify
    verify_parser = subparsers.add_parser("verify", help="Verifica integridade da traducao")
    verify_parser.add_argument("module_id", help="ID do modulo (curso/modulo)")
    verify_parser.add_argument("--lang", default="en-US", choices=SUPPORTED_LANGS)

    args = parser.parse_args()

    if args.command == "status":
        status_report()
        return

    if args.command == "init":
        success = init_module(args.module_id, args.lang)
        sys.exit(0 if success else 1)

    if args.command == "verify":
        result = verify_module(args.module_id, args.lang)
        print(f"Verificacao de {args.module_id} ({args.lang}):")
        for issue in result["issues"]:
            print(issue)
        s = result["stats"]
        print(f"\nResumo: {s['files_checked']} arquivos, {s['ok']} ok, {s['warnings']} warnings, {s['errors']} erros")
        sys.exit(0 if s['errors'] == 0 else 1)


if __name__ == "__main__":
    main()
