#!/usr/bin/env python3
"""
prebuild_site.py
Gera web/public/catalog.json a partir de knowledge-factory/registry/catalog.yaml.
"""

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CATALOG_YAML = ROOT / "knowledge-factory" / "registry" / "catalog.yaml"
CATALOG_JSON = ROOT / "web" / "public" / "catalog.json"

if not CATALOG_YAML.exists():
    print("catalog.yaml nao encontrado. Pulando.", file=sys.stderr)
    sys.exit(0)

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
