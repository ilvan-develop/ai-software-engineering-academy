#!/usr/bin/env python3
"""
batch_videos.py
Processa roteiros de video para todos os modulos.
Le o status.yaml, encontra modulos pendentes,
e dispara video_engine.py para cada um.
Usa cache incremental para pular modulos inalterados.
"""

import sys
import subprocess
import yaml
from pathlib import Path

from config import PROJECT_ROOT, SCRIPTS_DIR, STATUS_PATH, SOURCES_DIR as CURRICULUM_DIR, COURSES_DIR
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
    print(f"  $ {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ERRO: {result.stderr}")
        return False
    for line in result.stdout.split("\n"):
        if line.strip():
            print(f"    {line}")
    return True


def main():
    data = load_status()
    modules = data.get("modules", {})
    engine = SCRIPTS_DIR / "factories" / "content" / "video_engine.py"
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

            output_dir = COURSES_DIR / course_name / mod_id / "videos"
            item_id = f"{course_name}/{mod_id}"

            if not cache.is_stale(item_id, "videos", sources=[aula_path]):
                skipped += 1
                continue

            total += 1

            print(f"\n[{total}] {course_name}/{mod_id}: {mod['title']}")
            if run_engine(engine, aula_path, output_dir):
                mod.setdefault("outputs", {})["video"] = "gerado"
                cache.mark_done(item_id, "videos", sources=[aula_path])
                ok += 1
            else:
                print(f"  FALHOU")

    save_status(data)
    print(f"\n---\nVideos: {ok}/{total} processados", end="")
    if skipped:
        print(f" ({skipped} em cache)", end="")
    print()


if __name__ == "__main__":
    main()
