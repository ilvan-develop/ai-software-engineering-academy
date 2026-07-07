#!/usr/bin/env python3
"""
metadata_populator.py
Gera METADATA.yaml para cada modulo em curriculum/sources/<curso>/<modulo>/.
Le curriculum/status.yaml e knowledge-factory/registry/catalog.yaml como fontes.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
STATUS_PATH = ROOT / "curriculum" / "status.yaml"
CATALOG_PATH = ROOT / "knowledge-factory" / "registry" / "catalog.yaml"
SCHEMA_PATH = ROOT / "schemas" / "metadata.schema.json"
SOURCES_DIR = ROOT / "curriculum" / "sources"

# Books BQS scores from latest baseline (will be used if available)
BOOK_BQS_SCORES = {}


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def find_catalog_item(items: list, module_id: str) -> dict | None:
    for item in items:
        if item["id"] == module_id:
            return item
    return None


def find_bqs_score(module_id: str) -> float | None:
    csv_path = ROOT / "knowledge-factory" / "products" / "metrics" / "modules.csv"
    if not csv_path.exists():
        return None
    import csv
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        scores = []
        for row in reader:
            if row["target_id"] == module_id:
                scores.append(float(row["overall"]))
        if scores:
            return round(sum(scores) / len(scores), 1)
    return None


def build_metadata(
    course_name: str,
    mod_key: str,
    mod_data: dict,
    catalog_item: dict | None,
) -> dict:
    title = mod_data.get("title", mod_key)
    status = mod_data.get("status", "raw")
    last_updated = mod_data.get("last_updated", datetime.now().strftime("%Y-%m-%d"))

    module_id = f"{course_name}/{mod_key}"

    topics = []
    level = "intermediate"
    audience = ["devs"]
    prereqs = []

    if catalog_item:
        tax = catalog_item.get("taxonomy", {})
        topics = tax.get("topics", [])
        level = tax.get("level", "intermediate")
        audience = tax.get("audience", ["devs"])
        prereqs = catalog_item.get("relationships", {}).get("prerequisites", [])

    bqs_score = find_bqs_score(module_id)

    metadata = {
        "id": module_id,
        "title": title,
        "description": f"Módulo {title} do curso {course_name}.",
        "status": status,
        "version": 1,
        "topics": topics,
        "level": level,
        "audience": audience,
        "prerequisites": prereqs,
        "author": "AI Software Engineering Academy",
        "reviewers": [],
        "bqs_score": bqs_score,
        "duration_minutes": None,
        "changelog": [
            {
                "date": last_updated,
                "version": "1.0",
                "description": "Versão inicial",
                "author": "AI Software Engineering Academy",
            }
        ],
    }

    return metadata


def validate_metadata(metadata: dict) -> bool:
    try:
        import jsonschema
        with open(SCHEMA_PATH, encoding="utf-8") as f:
            schema = json.load(f)
        jsonschema.validate(metadata, schema)
        return True
    except ImportError:
        return True  # skip if jsonschema not available
    except jsonschema.ValidationError as e:
        print(f"  ERRO schema: {e}", file=sys.stderr)
        return False


def main():
    status = load_yaml(STATUS_PATH)
    catalog = load_yaml(CATALOG_PATH)
    catalog_items = catalog.get("items", [])

    modules = status.get("modules", {})
    total = 0
    errors = 0

    for course_name, mods in modules.items():
        for mod_key, mod_data in mods.items():
            module_id = f"{course_name}/{mod_key}"
            catalog_item = find_catalog_item(catalog_items, module_id)
            metadata = build_metadata(course_name, mod_key, mod_data, catalog_item)

            module_dir = SOURCES_DIR / course_name / mod_key
            if not module_dir.exists():
                print(f"[WARN] Diretorio nao encontrado: {module_dir}")
                errors += 1
                continue

            if not validate_metadata(metadata):
                print(f"[ERRO] Metadata invalida para {module_id}")
                errors += 1
                continue

            metadata_path = module_dir / "METADATA.yaml"
            with open(metadata_path, "w", encoding="utf-8") as f:
                yaml.dump(
                    metadata, f, allow_unicode=True,
                    sort_keys=False, default_flow_style=False,
                )

            score_str = f", bqs={metadata['bqs_score']}" if metadata["bqs_score"] else ""
            print(f"[OK] {module_id}{score_str}")
            total += 1

    print(f"\n--- METADATA.yaml gerado para {total} modulos (erros: {errors}) ---")


if __name__ == "__main__":
    main()
