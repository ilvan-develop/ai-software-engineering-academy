#!/usr/bin/env python3
"""batch_workshops.py — Gera workshops para todos os modulos.
Usa cache incremental para pular modulos inalterados."""

import sys, subprocess, yaml
from pathlib import Path

from config import PROJECT_ROOT, SCRIPTS_DIR, STATUS_PATH, SOURCES_DIR as CURRICULUM_DIR, COURSES_DIR
from cache import BuildCache

def load_status() -> dict:
    with open(STATUS_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)
def save_status(data: dict):
    with open(STATUS_PATH, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

def run(script, input_path, duration, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, str(script), f"--input={input_path}", f"--duration={duration}", f"--output={output_dir}"]
    print(f"  $ {' '.join(cmd)}")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  ERRO: {r.stderr}")
        return False
    for l in r.stdout.split("\n"):
        if l.strip(): print(f"    {l}")
    return True

def main():
    data = load_status()
    modules = data.get("modules", {})
    engine = SCRIPTS_DIR / "factories" / "content" / "workshop_engine.py"
    cache = BuildCache()
    total = ok = skipped = 0
    for course, mods in modules.items():
        for mid, mod in mods.items():
            aula = CURRICULUM_DIR / course / mid / "aula" / "aula.md"
            if not aula.exists(): continue
            out = COURSES_DIR / course / mid / "workshop"
            item_id = f"{course}/{mid}"
            if not cache.is_stale(item_id, "workshop", sources=[aula]):
                skipped += 1
                continue
            total += 1
            print(f"\n[{total}] {course}/{mid}")
            if run(engine, aula, 4, out):
                mod.setdefault("outputs", {})["workshop"] = "gerado"
                cache.mark_done(item_id, "workshop", sources=[aula])
                ok += 1
    save_status(data)
    print(f"\n---\nWorkshops: {ok}/{total}", end="")
    if skipped:
        print(f" ({skipped} em cache)", end="")
    print()

if __name__ == "__main__":
    main()
