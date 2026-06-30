#!/usr/bin/env python3
"""
batch_remaining.py
Orquestrador final — processa Projetos, Social Media, Videos, Slides,
Exercicios, Quiz, Newsletter, Workshop e LMS.
Usa cache incremental em todas as etapas.
"""

import sys, subprocess
from pathlib import Path

from config import (SCRIPTS_DIR, STATUS_PATH, SOURCES_DIR as CURRICULUM_DIR,
                     COURSES_DIR, SOCIAL_DIR, NEWSLETTERS_DIR, ONLINE_COURSES_DIR,
                     KF_DIR, PROJECT_ROOT)
from cache import BuildCache

import yaml


def load_status() -> dict:
    with open(STATUS_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)

def save_status(data: dict):
    with open(STATUS_PATH, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)


def run_engine(script: str, args_list: list) -> bool:
    cmd = [sys.executable, str(script)] + args_list
    print(f"  $ {' '.join(str(a) for a in cmd[:4])} ...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        for line in result.stderr.split("\n")[-3:]:
            if line.strip():
                print(f"  ERRO: {line}")
        return False
    for line in result.stdout.split("\n"):
        if line.strip():
            print(f"    {line}")
    return True


def _process_type(
    data: dict, engine_name: str, output_key: str,
    output_dir_fn, cache_type: str,
) -> tuple:
    engine = SCRIPTS_DIR / "factories" / "content" / engine_name
    modules = data.get("modules", {})
    cache = BuildCache()
    total = ok = skipped = 0
    print(f"\n{'='*50}\n  PIPELINE: {output_key.title()}\n{'='*50}")

    for course_name, mods in modules.items():
        for mod_id, mod in mods.items():
            aula_path = CURRICULUM_DIR / course_name / mod_id / "aula" / "aula.md"
            if not aula_path.exists():
                continue
            output_dir = output_dir_fn(course_name, mod_id)
            item_id = f"{course_name}/{mod_id}"

            if not cache.is_stale(item_id, cache_type, sources=[aula_path]):
                skipped += 1
                continue

            total += 1
            print(f"\n  [{total}] {course_name}/{mod_id}: {mod.get('title', mod_id)}")
            if run_engine(engine, [f"--input={aula_path}", f"--output={output_dir}"]):
                mod.setdefault("outputs", {})[output_key] = "gerado"
                cache.mark_done(item_id, cache_type, sources=[aula_path])
                ok += 1

    print(f"\n  {output_key.title()}: {ok}/{total} (+{skipped} cache)")
    return total + skipped, ok + skipped


def process_projects(data: dict) -> tuple:
    return _process_type(
        data, "project_engine.py", "projeto",
        lambda c, m: COURSES_DIR / c / m / "projeto", "projeto"
    )


def process_social_media(data: dict) -> tuple:
    return _process_type(
        data, "social_engine.py", "social_media",
        lambda c, m: SOCIAL_DIR / c / m, "social"
    )


def process_newsletter(data: dict) -> tuple:
    engine = SCRIPTS_DIR / "factories" / "content" / "newsletter_engine.py"
    output_dir = NEWSLETTERS_DIR
    courses = sorted(d for d in CURRICULUM_DIR.iterdir() if d.is_dir())
    cache = BuildCache()
    print(f"\n{'='*50}\n  PIPELINE: Newsletter\n{'='*50}")
    total = ok = 0
    for course_dir in courses:
        course = course_dir.name
        out = output_dir / course
        sources = sorted(course_dir.rglob("aula.md"))
        if not cache.is_stale(course, "newsletter", sources=sources):
            total += 1
            ok += 1
            continue
        total += 1
        print(f"\n  {course}")
        if run_engine(engine, [f"--modules-dir={course_dir}", f"--course={course}", f"--output={out}"]):
            cache.mark_done(course, "newsletter", sources=sources)
            ok += 1
    print(f"\n  Newsletters: {ok}/{total}")
    return total, ok


def process_workshops(data: dict) -> tuple:
    engine = SCRIPTS_DIR / "factories" / "content" / "workshop_engine.py"
    courses = list(data.get("modules", {}).keys())
    cache = BuildCache()
    print(f"\n{'='*50}\n  PIPELINE: Workshops\n{'='*50}")
    total = ok = skipped = 0
    for course in courses:
        for duration in [4, 8]:
            output_dir = COURSES_DIR / course / "workshop"
            sources = sorted((CURRICULUM_DIR / course).rglob("aula.md"))
            item_id = f"{course}/workshop-{duration}h"
            if not cache.is_stale(item_id, "workshop", sources=sources):
                skipped += 1
                continue
            total += 1
            print(f"\n  [{total}] {course} ({duration}h)")
            if run_engine(engine, [f"--curso={course}", f"--duration={duration}", f"--output={output_dir}"]):
                cache.mark_done(item_id, "workshop", sources=sources)
                ok += 1
    print(f"\n  Workshops: {ok}/{total} (+{skipped} cache)")
    return total + skipped, ok + skipped


def process_lms(data: dict) -> tuple:
    engine = SCRIPTS_DIR / "factories" / "content" / "lms_engine.py"
    courses = list(data.get("modules", {}).keys())
    cache = BuildCache()
    output_base = ONLINE_COURSES_DIR
    print(f"\n{'='*50}\n  PIPELINE: LMS\n{'='*50}")
    total = ok = skipped = 0
    for course in courses:
        output_dir = output_base / course
        sources = sorted((CURRICULUM_DIR / course).rglob("aula.md"))
        if not cache.is_stale(course, "lms", sources=sources):
            skipped += 1
            continue
        total += 1
        print(f"\n  [{total}] {course}")
        if run_engine(engine, [f"--curso={course}", f"--output={output_dir}"]):
            cache.mark_done(course, "lms", sources=sources)
            ok += 1
    print(f"\n  LMS: {ok}/{total} (+{skipped} cache)")
    return total + skipped, ok + skipped


def main():
    data = load_status()

    results = {
        "projetos": process_projects(data),
        "social_media": process_social_media(data),
        "newsletter": process_newsletter(data),
        "workshops": process_workshops(data),
        "lms": process_lms(data),
    }

    save_status(data)

    print(f"\n{'='*60}")
    print("  BATCH REMAINING — RESUMO FINAL")
    print(f"{'='*60}")
    total_all = ok_all = 0
    for name, (total, ok) in results.items():
        status = "OK" if ok == total else "INCOMPLETO"
        print(f"  {status:>10}  {name}: {ok}/{total}")
        total_all += total
        ok_all += ok
    print(f"\n  TOTAL: {ok_all}/{total_all} processados")
    print(f"{'='*60}")

    return 0 if ok_all == total_all else 1


if __name__ == "__main__":
    sys.exit(main())
