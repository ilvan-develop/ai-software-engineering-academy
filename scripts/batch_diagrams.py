#!/usr/bin/env python3
"""
batch_diagrams.py
Gera diagramas SVG para todos os modulos que possuem arquivos
*.diagram-*.json em seus diretorios assets/.

Uso:
  python scripts/batch_diagrams.py
"""

import subprocess
import sys
from pathlib import Path

from config import PROJECT_ROOT, SCRIPTS_DIR, COURSES_DIR as KF_DIR
from cache import BuildCache
FACTORY_SCRIPT = SCRIPTS_DIR / "diagram_factory.py"


def main():
    generated = 0
    skipped = 0
    cache = BuildCache()

    for course_dir in sorted(KF_DIR.iterdir()):
        if not course_dir.is_dir():
            continue
        for module_dir in sorted(course_dir.iterdir()):
            if not module_dir.is_dir():
                continue
            assets_dir = module_dir / "assets"
            if not assets_dir.exists():
                continue

            for input_file in sorted(assets_dir.glob("diagram-*.json")):
                output_file = input_file.with_suffix(".svg")
                cache_key = f"{course_dir.name}/{module_dir.name}/{input_file.stem}"

                if not cache.is_stale(cache_key, "diagram", [input_file]) and output_file.exists():
                    skipped += 1
                    continue

                result = subprocess.run([
                    sys.executable, str(FACTORY_SCRIPT),
                    f"--input={input_file}",
                    f"--output={output_file}",
                ], capture_output=True, text=True)

                if result.returncode == 0:
                    generated += 1
                    cache.mark_done(cache_key, "diagram", [input_file])
                    print(f"  {module_dir.name}: {output_file.name}")
                else:
                    print(f"  ERRO {module_dir.name}: {result.stderr.strip()}")

    print(f"\nDiagramas gerados: {generated}")
    print(f"Ja existiam (cache): {skipped}")


if __name__ == "__main__":
    main()
