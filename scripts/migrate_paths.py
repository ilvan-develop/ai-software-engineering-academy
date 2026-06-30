#!/usr/bin/env python3
"""
migrate_paths.py — Migrate knowledge-factory from flat structure to products/{format}/.
Moves directories to match the new architecture defined in config.py.

Phase 3 of architecture migration:
  cursos/  → products/courses/
  livros/  → products/books/
  social-media/ → products/social/
  newsletter/   → products/newsletters/
  curso-online/ → products/online-courses/
  certificacao/ → products/certificates/
"""

import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
KF = PROJECT_ROOT / "knowledge-factory"
PRODUCTS = KF / "products"

MIGRATIONS = [
    (KF / "cursos",        PRODUCTS / "courses"),
    (KF / "livros",        PRODUCTS / "books"),
    (KF / "social-media",  PRODUCTS / "social"),
    (KF / "newsletter",    PRODUCTS / "newsletters"),
    (KF / "curso-online",  PRODUCTS / "online-courses"),
    (KF / "certificacao",  PRODUCTS / "certificates"),
]


def main():
    dry_run = "--dry-run" in sys.argv

    for src, dst in MIGRATIONS:
        if not src.exists():
            print(f"  SKIP {src.name} — not found")
            continue
        if dst.exists():
            print(f"  SKIP {src.name} → {dst.name} — destination already exists")
            continue

        print(f"  MOVE {src.name}/ → products/{dst.name}/")
        if not dry_run:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            print(f"    OK")

    if dry_run:
        print(f"\n  Dry run. Pass --execute to apply.")


if __name__ == "__main__":
    main()
