#!/usr/bin/env python3
"""
prebuild_site.py
Gera web/public/catalog.json a partir de knowledge-factory/registry/catalog.yaml
e web/public/bqs-data.json a partir do JSON detalhado do BQS ou CSV.
"""

import csv
import json
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CATALOG_YAML = ROOT / "knowledge-factory" / "registry" / "catalog.yaml"
CATALOG_JSON = ROOT / "web" / "public" / "catalog.json"
BQS_CSV = ROOT / "knowledge-factory" / "products" / "metrics" / "modules.csv"
BQS_JSON = ROOT / "web" / "public" / "bqs-data.json"
BQS_DETAILED = ROOT / "knowledge-factory" / "products" / "metrics" / "bqs-detailed.json"

if not CATALOG_YAML.exists():
    print("catalog.yaml nao encontrado. Pulando.", file=sys.stderr)
else:
    with open(CATALOG_YAML, encoding="utf-8") as f:
        doc = yaml.safe_load(f)

    simplified = {
        "version": doc.get("version", 1),
        "items": [
            {
                "id": item["id"],
                "type": item.get("type", "unknown"),
                "title": item.get("title", ""),
                "taxonomy": item.get("taxonomy", {}),
            }
            for item in doc.get("items", [])
        ],
    }

    CATALOG_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(CATALOG_JSON, "w", encoding="utf-8") as f:
        json.dump(simplified, f, indent=2, ensure_ascii=False)
    print(f"catalog.json gerado com {len(simplified['items'])} items em {CATALOG_JSON}")

# BQS: prefer detailed JSON from bqs_compute.py (has per-category scores)
if BQS_DETAILED.exists():
    BQS_JSON.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(BQS_DETAILED, BQS_JSON)
    with open(BQS_DETAILED) as f:
        count = len(json.load(f)["targets"])
    print(f"bqs-data.json copiado de bqs_compute.py ({count} targets)")
elif BQS_CSV.exists():
    rows = []
    with open(BQS_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    if rows:
        last_ts = max(r["timestamp"] for r in rows)
        last_run = [r for r in rows if r["timestamp"] == last_ts]

        BQS_JSON.parent.mkdir(parents=True, exist_ok=True)
        with open(BQS_JSON, "w", encoding="utf-8") as f:
            json.dump({"timestamp": last_ts, "targets": last_run}, f, indent=2, ensure_ascii=False)
        print(f"bqs-data.json gerado do CSV com {len(last_run)} targets em {BQS_JSON}")
else:
    print("BQS data nao encontrada. Pulando.", file=sys.stderr)
