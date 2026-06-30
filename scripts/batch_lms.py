"""batch_lms.py — Gera estrutura LMS por curso. Usa cache incremental."""

import sys, subprocess
from pathlib import Path

from config import (PROJECT_ROOT, SCRIPTS_DIR, SOURCES_DIR as CURRICULUM_DIR,
                     ONLINE_COURSES_DIR)
from cache import BuildCache


def run(script, modules_dir, course, output_dir):
    cmd = [sys.executable, str(script), f"--modules-dir={modules_dir}",
           f"--course={course}", f"--output={output_dir}"]
    print(f"  $ {' '.join(cmd)}")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  ERRO: {r.stderr}")
        return False
    for l in r.stdout.split("\n"):
        if l.strip():
            print(f"    {l}")
    return True


def _course_sources(course_dir: Path) -> list[Path]:
    return sorted(course_dir.rglob("aula.md"))


def main():
    engine = SCRIPTS_DIR / "factories" / "content" / "lms_engine.py"
    courses = sorted(d for d in CURRICULUM_DIR.iterdir() if d.is_dir())
    cache = BuildCache()
    total = ok = skipped = 0
    for course_dir in courses:
        course = course_dir.name
        out = ONLINE_COURSES_DIR / course
        sources = _course_sources(course_dir)
        if not cache.is_stale(course, "lms", sources=sources):
            skipped += 1
            continue
        total += 1
        print(f"\n[{total}] {course}")
        if run(engine, course_dir, course, out):
            cache.mark_done(course, "lms", sources=sources)
            ok += 1
    print(f"\n---\nLMS: {ok}/{total} cursos", end="")
    if skipped:
        print(f" ({skipped} em cache)", end="")
    print()


if __name__ == "__main__":
    main()
