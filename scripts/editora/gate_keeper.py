#!/usr/bin/env python3
"""
gate_keeper.py
Verifica scores BQS e libera/nega avanço entre estágios do pipeline.
Garante que ninguém aprova o próprio trabalho.
"""
import yaml
import json
import sys
from pathlib import Path
from datetime import datetime

from config import PROJECT_ROOT, STATUS_PATH, BQS_DIR, GATES_DIR, BOOKS_DIR

GATE_POLICY_PATH = BQS_DIR / "gate-policy.yaml"
PIPELINE_PATH = PROJECT_ROOT / "config" / "editora" / "pipeline-gate.yaml"


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_status() -> dict:
    if not STATUS_PATH.exists():
        return {"books": {}, "gates": {}}
    return load_yaml(STATUS_PATH)


def save_status(data: dict):
    with open(STATUS_PATH, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)


def check_gate(gate_id: str, score_card: dict, producer_id: str, reviewer_id: str) -> dict:
    """
    Verifica se um gate pode ser aprovado.
    - score_card: dict com scores por categoria
    - producer_id: quem produziu o conteúdo
    - reviewer_id: quem está auditando (NÃO pode ser o mesmo)
    """
    gate_policy = load_yaml(GATE_POLICY_PATH)
    gates = gate_policy.get("gates", [])

    gate = None
    for g in gates:
        if g["id"] == gate_id:
            gate = g
            break

    if not gate:
        return {"approved": False, "reason": f"Gate {gate_id} não encontrado na política"}

    results = []
    all_approved = True

    # Rule 1: No self-approval
    if producer_id == reviewer_id:
        results.append({
            "rule": "no-self-approval",
            "passed": False,
            "message": f"{reviewer_id} produziu o conteúdo e não pode auditar"
        })
        all_approved = False
    else:
        results.append({
            "rule": "no-self-approval",
            "passed": True,
            "message": f"{reviewer_id} ≠ {producer_id}"
        })

    # Rule 2: Score minimum per category
    categories_checked = gate.get("categories_checked", [])
    if categories_checked == "*":
        categories_checked = [c["name"] for c in score_card.get("categories", [])]

    min_score = gate.get("min_score", 95)
    for cat in score_card.get("categories", []):
        if cat["name"] in categories_checked or "*" in gate.get("categories_checked", []):
            passed = cat["score"] >= min_score
            if not passed:
                all_approved = False
            results.append({
                "rule": "score-minimum",
                "category": cat["name"],
                "score": cat["score"],
                "minimum": min_score,
                "passed": passed
            })

    # Rule 3: Handoff artifacts
    artifacts_required = gate.get("artifacts_required", [])
    for artifact in artifacts_required:
        artifact_path = PROJECT_ROOT / "knowledge-factory" / artifact
        exists = artifact_path.exists()
        if not exists:
            all_approved = False
        results.append({
            "rule": "handoff-artifacts",
            "artifact": artifact,
            "exists": exists,
            "passed": exists
        })

    return {
        "gate_id": gate_id,
        "gate_name": gate.get("name", gate_id),
        "approved": all_approved,
        "results": results,
        "timestamp": datetime.now().isoformat()
    }


def execute_gate(gate_id: str, book_id: str, score_card_path: str,
                 producer_id: str, reviewer_id: str, output_dir: str = None) -> dict:
    """Executa um gate e registra o resultado"""
    if output_dir:
        out = Path(output_dir)
    else:
        out = BOOKS_DIR / book_id / "gates"
    out.mkdir(parents=True, exist_ok=True)

    # Load score card
    sc_path = Path(score_card_path)
    if not sc_path.exists():
        return {"error": f"Score-card não encontrado: {sc_path}"}

    with open(sc_path, encoding="utf-8") as f:
        if sc_path.suffix == ".yaml":
            score_card = yaml.safe_load(f)
        else:
            score_card = json.load(f)

    # Check gate
    result = check_gate(gate_id, score_card, producer_id, reviewer_id)

    # Save gate result
    gate_report_path = out / f"gate-{gate_id}-{book_id}.yaml"
    with open(gate_report_path, "w", encoding="utf-8") as f:
        yaml.dump(result, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    # Update status
    status = load_status()
    if "gates" not in status:
        status["gates"] = {}
    if gate_id not in status["gates"]:
        status["gates"][gate_id] = {}
    status["gates"][gate_id][book_id] = {
        "approved": result["approved"],
        "timestamp": result["timestamp"],
        "reviewer": reviewer_id,
        "producer": producer_id
    }
    save_status(status)

    # Print result
    status_icon = "✅" if result["approved"] else "❌"
    print(f"\n{status_icon} Gate: {result['gate_name']} ({gate_id})")
    print(f"   Aprovado: {result['approved']}")
    for r in result["results"]:
        icon = "✅" if r["passed"] else "❌"
        msg = r.get("message", r.get("category", r.get("artifact", "")))
        print(f"   {icon} {r['rule']}: {msg}")
    print(f"   Relatório: {gate_report_path}")

    return result


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Gate Keeper — Pipeline Editorial Gates")
    parser.add_argument("--gate-id", required=True, help="ID do gate (ex: conteudo_to_editorial)")
    parser.add_argument("--book-id", required=True, help="ID do livro")
    parser.add_argument("--score-card", required=True, help="Caminho do score-card YAML/JSON")
    parser.add_argument("--producer", required=True, help="ID do agente que produziu o conteúdo")
    parser.add_argument("--reviewer", required=True, help="ID do agente que está auditando")
    parser.add_argument("--output", help="Diretório de saída do relatório do gate")

    args = parser.parse_args()
    result = execute_gate(
        args.gate_id, args.book_id, args.score_card,
        args.producer, args.reviewer, args.output
    )

    if "error" in result:
        print(f"ERRO: {result['error']}")
        sys.exit(1)

    sys.exit(0 if result["approved"] else 2)


if __name__ == "__main__":
    main()
