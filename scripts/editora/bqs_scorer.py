#!/usr/bin/env python3
"""
bqs_scorer.py
Calcula scores BQS (Book Quality Standard) por categoria e geral.
Usa os critérios definidos em curriculum/bqs/bqs-core.yaml
"""
import yaml
import json
import sys
from pathlib import Path
from datetime import datetime

BQS_PATH = Path(__file__).resolve().parent.parent.parent / "curriculum" / "bqs" / "bqs-core.yaml"
REPORTS_DIR = Path(__file__).resolve().parent.parent.parent / "knowledge-factory" / "reports"


def load_bqs() -> dict:
    with open(BQS_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def calculate_score(category_id: str, audit_scores: dict) -> dict:
    """
    Calcula score de uma categoria BQS.
    audit_scores: dict com {criterion_id: score} (0-100)
    """
    bqs = load_bqs()
    categories = bqs.get("categories", [])

    for cat in categories:
        if cat["id"] != category_id:
            continue

        weighted_sum = 0
        total_weight = 0
        details = []

        for criterion in cat.get("criteria", []):
            cid = criterion["id"]
            weight = criterion.get("weight_within", 100)
            score = audit_scores.get(cid, 0)
            weighted_sum += score * weight
            total_weight += weight
            details.append({
                "criterion_id": cid,
                "name": criterion["name"],
                "score": score,
                "weight": weight,
                "weighted": round(score * weight / 100, 2)
            })

        final_score = round(weighted_sum / total_weight, 2) if total_weight > 0 else 0

        return {
            "category_id": cat["id"],
            "name": cat["name"],
            "weight": cat["weight"],
            "score": final_score,
            "passed": final_score >= bqs.get("minimum_score", 95),
            "details": details
        }

    return {"error": f"Category {category_id} not found"}


def calculate_overall(scores: list) -> dict:
    """Calcula score geral ponderado"""
    weighted_sum = 0
    total_weight = 0
    min_score = float("inf")
    min_category = ""

    for s in scores:
        w = s["weight"]
        score = s["score"]
        weighted_sum += score * w
        total_weight += w
        if score < min_score:
            min_score = score
            min_category = s["name"]

    overall = round(weighted_sum / total_weight, 2) if total_weight > 0 else 0

    return {
        "overall_score": overall,
        "minimum_score": min_score,
        "minimum_category": min_category,
        "passed_all": all(s["passed"] for s in scores),
        "timestamp": datetime.now().isoformat()
    }


def generate_score_card(book_id: str, audit_scores: dict) -> dict:
    """Gera score-card completo para um livro"""
    bqs = load_bqs()
    categories = bqs.get("categories", [])
    scores = []

    for cat in categories:
        # Match by explicit criteria IDs (not prefix — avoids collisions like qt for both qualidade_tecnica and qualidade_tipografica)
        criteria_ids = [c["id"] for c in cat.get("criteria", [])]
        cat_scores = {k: v for k, v in audit_scores.items() if k in criteria_ids}
        if not cat_scores:
            cat_scores = audit_scores.get(cat["id"], {})

        if isinstance(cat_scores, dict):
            result = calculate_score(cat["id"], cat_scores)
        else:
            result = {
                "category_id": cat["id"],
                "name": cat["name"],
                "weight": cat["weight"],
                "score": cat_scores if isinstance(cat_scores, (int, float)) else 0,
                "passed": (cat_scores if isinstance(cat_scores, (int, float)) else 0) >= bqs.get("minimum_score", 95),
                "details": []
            }
        scores.append(result)

    overall = calculate_overall(scores)

    return {
        "book_id": book_id,
        "bqs_version": bqs.get("bqs_version"),
        "minimum_required": bqs.get("minimum_score"),
        "categories": scores,
        "overall": overall
    }


def save_score_card(book_id: str, score_card: dict, output_dir: Path = None):
    """Salva score-card em YAML"""
    if not output_dir:
        output_dir = REPORTS_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    path = output_dir / f"score-card-{book_id}.yaml"
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(score_card, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    # Also save as JSON for programmatic use
    json_path = output_dir / f"score-card-{book_id}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(score_card, f, ensure_ascii=False, indent=2)

    return path


def print_report(score_card: dict):
    """Exibe relatório visual no terminal"""
    import sys
    bqs = score_card
    use_emoji = not sys.platform.startswith("win")

    def icon(passed):
        return "[OK]" if passed else "[--]" if use_emoji else ("[OK]" if passed else "[--]")

    def bar(score, size=20):
        full = int(score / 5)
        empty = size - full
        return "#" * full + "." * empty

    print(f"\n{'='*55}")
    print(f"  BQS SCORE CARD -- {bqs['book_id']}")
    print(f"  Versao: {bqs['bqs_version']}  |  Minimo: {bqs['minimum_required']}")
    print(f"{'='*55}")

    for cat in bqs["categories"]:
        status = "[OK]" if cat["passed"] else "[--]"
        print(f"  {status} {cat['name']:<30} {cat['score']:>5.1f} {bar(cat['score'])}")

    print(f"{'-'*55}")
    overall = bqs["overall"]
    final = "[OK] APROVADO" if overall["passed_all"] else "[--] REPROVADO"
    print(f"  Score Geral:      {overall['overall_score']:.1f}")
    print(f"  Score Minimo:     {overall['minimum_score']:.1f} ({overall['minimum_category']})")
    print(f"  {final}")
    print(f"{'='*55}\n")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="BQS Scorer — Book Quality Standard Calculator")
    parser.add_argument("--book-id", required=True, help="ID do livro (ex: ia-para-devs)")
    parser.add_argument("--scores", required=True, help="JSON com scores por categoria/critério")
    parser.add_argument("--output", help="Diretório de saída (default: knowledge-factory/reports/)")

    args = parser.parse_args()

    try:
        audit_scores = json.loads(args.scores)
    except json.JSONDecodeError:
        print("ERRO: --scores deve ser um JSON válido")
        sys.exit(1)

    score_card = generate_score_card(args.book_id, audit_scores)
    output_path = save_score_card(args.book_id, score_card, Path(args.output) if args.output else None)

    print_report(score_card)
    print(f"Score-card salvo: {output_path}")


if __name__ == "__main__":
    main()
