#!/usr/bin/env python3
"""
catalog_populator.py
Le curriculum/status.yaml e taxonomy.yaml, gera knowledge-factory/registry/catalog.yaml.
Idempotente — seguro rodar multiplas vezes.
"""

import json
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
STATUS_PATH = ROOT / "curriculum" / "status.yaml"
TAXONOMY_PATH = ROOT / "knowledge-factory" / "registry" / "taxonomy.yaml"
CATALOG_PATH = ROOT / "knowledge-factory" / "registry" / "catalog.yaml"
SCHEMA_PATH = ROOT / "schemas" / "catalog.schema.json"

COURSE_TO_TOPIC = {
    "fundamentos-enterprise": "fundamentos",
    "product-design": "product-design",
    "arquitetura-backend": "arquitetura-backend",
    "frontend-devops": "frontend",
    "governanca-automacao": "governanca",
    "capstone": "arquitetura-backend",
}

COURSE_TO_LEVEL = {
    "fundamentos-enterprise": "beginner",
    "product-design": "intermediate",
    "arquitetura-backend": "advanced",
    "frontend-devops": "intermediate",
    "governanca-automacao": "advanced",
    "capstone": "advanced",
}

COURSE_TO_AUDIENCE = {
    "fundamentos-enterprise": ["devs", "architects", "students"],
    "product-design": ["designers", "devs"],
    "arquitetura-backend": ["architects", "devs"],
    "frontend-devops": ["devs"],
    "governanca-automacao": ["architects", "managers"],
    "capstone": ["architects", "devs"],
}

# Subtopics por modulo (inferido do nome do modulo)
MODULE_SUBTOPIC_HINTS = {
    "module-00-introducao": ["introducao"],
    "module-01-mentalidade-enterprise": ["mentalidade"],
    "module-09-erro-90-ia": ["erro-90"],
    "module-02-product-discovery": ["discovery"],
    "module-03-design-thinking": ["design-thinking"],
    "module-04-ux": ["ux"],
    "module-05-wireframes": ["wireframes"],
    "module-06-ui-design": ["ui"],
    "module-07-design-system": ["design-system"],
    "module-08-arquitetura": ["clean-architecture"],
    "module-09-modelagem": ["ddd", "modelagem"],
    "module-10-backend": ["clean-architecture"],
    "module-12-seguranca": ["seguranca"],
    "module-13-multi-tenant": ["multi-tenant"],
    "module-13b-multi-tenant-implementacao": ["multi-tenant"],
    "module-13c-multi-tenant-dados": ["multi-tenant"],
    "module-13d-multi-tenant-operacoes": ["multi-tenant"],
    "module-11-frontend": ["frontend"],
    "module-14-devops": ["devops"],
    "module-15-qa": ["qualidade"],
    "module-16-observabilidade": ["observabilidade"],
    "module-17-governanca": ["governanca"],
    "module-18-agentes-ia": ["agentes-ia"],
    "module-19-auditorias": ["auditorias"],
    "module-20-automacao": ["automacao"],
    "module-21-projeto-final": ["clean-architecture"],
}


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_catalog(items: list) -> bool:
    import jsonschema

    with open(SCHEMA_PATH, encoding="utf-8") as f:
        schema = json.load(f)
    try:
        jsonschema.validate({"version": 1, "items": items}, schema)
        return True
    except jsonschema.ValidationError as e:
        print(f"ERRO de schema: {e}", file=sys.stderr)
        return False


def build_module_items(status: dict) -> list:
    items = []
    modules = status.get("modules", {})
    # Prerequisitos: ordem dos cursos define dependencia linear
    course_order = [
        "fundamentos-enterprise",
        "product-design",
        "arquitetura-backend",
        "frontend-devops",
        "governanca-automacao",
        "capstone",
    ]
    all_module_ids = []
    course_module_map = {}

    for course_name, mods in modules.items():
        course_module_map[course_name] = []
        for mod_key, mod_data in mods.items():
            mod_id = f"{course_name}/{mod_key}"
            course_module_map[course_name].append(mod_id)
            all_module_ids.append(mod_id)

    for course_name, mods in modules.items():
        topic = COURSE_TO_TOPIC.get(course_name, "fundamentos")
        level = COURSE_TO_LEVEL.get(course_name, "intermediate")
        audience = COURSE_TO_AUDIENCE.get(course_name, ["devs"])

        # Encontrar indice do curso para determinar prerequisitos
        course_idx = course_order.index(course_name) if course_name in course_order else -1

        for mod_key, mod_data in mods.items():
            mod_id = f"{course_name}/{mod_key}"
            book_refs = mod_data.get("book_chapters", [])
            used_in_books = [ref.split("/")[0] for ref in book_refs if "/" in ref]

            # Subtopics especificos do modulo
            subtopics = MODULE_SUBTOPIC_HINTS.get(mod_key, [topic])

            # Topic principal + subtopics
            topics = [topic]
            if subtopics:
                topics.extend(subtopics)
            topics = list(dict.fromkeys(topics))  # dedup preserving order

            # Prerequisitos: modulos anteriores no mesmo curso + ultimo do curso anterior
            prereqs = []
            if course_idx > 0:
                prev_course = course_order[course_idx - 1]
                prev_mods = course_module_map.get(prev_course, [])
                if prev_mods:
                    prereqs.append(prev_mods[-1])

            item = {
                "id": mod_id,
                "type": "module",
                "title": mod_data.get("title", mod_key),
                "source": f"curriculum/sources/{course_name}/{mod_key}/aula/aula.md",
                "version": 1,
                "taxonomy": {
                    "topics": topics,
                    "level": level,
                    "audience": audience,
                },
                "relationships": {
                    "used_in": used_in_books,
                    "prerequisites": prereqs,
                },
                "outputs": {
                    fmt: sts
                    for fmt, sts in mod_data.get("outputs", {}).items()
                },
            }
            items.append(item)

    return items


def build_book_items(status: dict) -> list:
    items = []
    books = status.get("books", {})
    for book_id, book_data in books.items():
        item = {
            "id": book_id,
            "type": "book",
            "title": book_data.get("title", book_id),
            "source": f"knowledge-factory/products/books/{book_id}/compiled/book.md",
            "version": 1,
            "taxonomy": {
                "topics": ["fundamentos", "arquitetura-backend", "product-design", "governanca"],
                "level": "advanced",
                "audience": ["architects", "devs"],
            },
            "relationships": {
                "used_in": [],
                "prerequisites": [],
            },
            "outputs": {
                fmt: sts
                for fmt, sts in book_data.get("formats", {}).items()
            },
        }
        items.append(item)
    return items


def build_graph(module_items: list, book_items: list) -> dict:
    nodes = []
    edges = []

    for item in module_items + book_items:
        nodes.append({
            "id": item["id"],
            "type": item["type"],
            "title": item["title"],
        })

    for item in module_items:
        for prereq_id in item["relationships"].get("prerequisites", []):
            edges.append({
                "source": prereq_id,
                "target": item["id"],
                "type": "prerequisite",
            })
        for book_ref in item["relationships"].get("used_in", []):
            edges.append({
                "source": item["id"],
                "target": book_ref,
                "type": "used_in",
            })

    return {
        "version": 1,
        "metadata": {
            "generated_by": "catalog_populator.py",
            "generated_at": __import__("datetime").datetime.now().isoformat(),
        },
        "nodes": nodes,
        "edges": edges,
    }


def main():
    status = load_yaml(STATUS_PATH)
    taxonomy = load_yaml(TAXONOMY_PATH)

    module_items = build_module_items(status)
    book_items = build_book_items(status)
    all_items = module_items + book_items

    print(f"Modulos catalogados: {len(module_items)}")
    print(f"Livros catalogados: {len(book_items)}")
    print(f"Total de items: {len(all_items)}")

    if not validate_catalog(all_items):
        sys.exit(1)

    catalog = {
        "version": 1,
        "items": all_items,
    }

    with open(CATALOG_PATH, "w", encoding="utf-8") as f:
        yaml.dump(catalog, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    print(f"Catalogo escrito em: {CATALOG_PATH}")

    # Gerar graph.yaml
    graph = build_graph(module_items, book_items)
    graph_path = CATALOG_PATH.parent / "graph.yaml"
    with open(graph_path, "w", encoding="utf-8") as f:
        yaml.dump(graph, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"Grafo escrito em: {graph_path}")


if __name__ == "__main__":
    main()
