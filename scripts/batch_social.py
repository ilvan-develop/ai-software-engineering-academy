#!/usr/bin/env python3
"""
batch_social.py
Processa conteudo de redes sociais para todos os modulos.
Usa cache incremental para pular modulos inalterados.
"""

import sys
import subprocess
import yaml
from pathlib import Path

from config import PROJECT_ROOT, SCRIPTS_DIR, STATUS_PATH, SOURCES_DIR as CURRICULUM_DIR, SOCIAL_DIR, KF_DIR
from cache import BuildCache


def load_status() -> dict:
    with open(STATUS_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_status(data: dict):
    with open(STATUS_PATH, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)


def run_engine(script: str, input_path: Path, output_dir: Path) -> bool:
    output_dir.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, str(script), f"--input={input_path}", f"--output={output_dir}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ERRO: {result.stderr[:200]}")
        return False
    for line in result.stdout.split("\n"):
        if line.strip():
            print(f"    {line}")
    return True


def main():
    data = load_status()
    modules = data.get("modules", {})
    engine = SCRIPTS_DIR / "factories" / "content" / "social_engine.py"
    cache = BuildCache()

    if not engine.exists():
        print(f"ERRO: engine nao encontrado: {engine}")
        sys.exit(1)

    total = 0
    ok = 0
    skipped = 0
    for course_name, mods in modules.items():
        for mod_id, mod in mods.items():
            aula_path = CURRICULUM_DIR / course_name / mod_id / "aula" / "aula.md"
            if not aula_path.exists():
                continue

            output_dir = SOCIAL_DIR / course_name / mod_id
            item_id = f"{course_name}/{mod_id}"

            if not cache.is_stale(item_id, "social", sources=[aula_path]):
                skipped += 1
                continue

            total += 1

            print(f"\n[{total}] {course_name}/{mod_id}: {mod['title']}")
            if run_engine(engine, aula_path, output_dir):
                mod.setdefault("outputs", {})["social_media"] = "gerado"
                cache.mark_done(item_id, "social", sources=[aula_path])
                ok += 1
            else:
                print(f"  FALHOU")

    save_status(data)
    print(f"\n---\nSocial: {ok}/{total} processados", end="")
    if skipped:
        print(f" ({skipped} em cache)", end="")
    print(f"\nOutput: {SOCIAL_DIR}")


if __name__ == "__main__":
    main()
