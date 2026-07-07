#!/usr/bin/env python3
"""
agents_sync.py
Analisa a sincronizacao entre config/editora/departamentos.yaml e opencode.json.
Gera relatorio de gaps e, opcionalmente, um opencode.json atualizado.

USO:
    python scripts/agents_sync.py                    # apenas relatorio
    python scripts/agents_sync.py --apply            # gera opencode.json.new
    python scripts/agents_sync.py --apply --force    # sobrescreve opencode.json
"""

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DEPARTAMENTOS = ROOT / "config" / "editora" / "departamentos.yaml"
OPENCODE_JSON = ROOT / "opencode.json"
OUTPUT_JSON = ROOT / "opencode.json.new"


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def get_yaml_agent_ids(departamentos: dict) -> list[tuple[str, str, str]]:
    """Returns list of (agent_id, agent_name, department_id) from YAML."""
    agents = []
    for dept in departamentos.get("departments", []):
        dept_id = dept.get("id", "unknown")
        for agent in dept.get("agents", []):
            agents.append((agent["id"], agent.get("name", ""), dept_id))
    return agents


def get_json_agent_ids(opencode: dict) -> set[str]:
    """Returns set of agent IDs registered in opencode.json (under 'agent' key)."""
    agents = opencode.get("agent", {})
    return {
        key
        for key in agents.keys()
        if isinstance(agents[key], dict) and "mode" in agents[key]
    }


def classify_missing_agent(agent_id: str, name: str, dept_id: str) -> dict:
    """Gera uma configuracao basica para um agente faltante."""

    # Permissoes padrao por departamento
    dept_permissions = {
        "conteudo": {"write": "allow", "read": "allow", "glob": "allow", "grep": "allow", "edit": "deny", "bash": "deny"},
        "editorial": {"write": "allow", "read": "allow", "glob": "allow", "grep": "allow", "edit": "deny", "bash": "deny"},
        "design": {"write": "allow", "read": "allow", "glob": "allow", "grep": "allow", "edit": "deny", "bash": "deny"},
        "publicacao": {"write": "allow", "read": "allow", "glob": "allow", "grep": "allow", "edit": "deny", "bash": "deny"},
        "qa": {"read": "allow", "glob": "allow", "grep": "allow", "write": "deny", "edit": "deny", "bash": "deny"},
    }

    permissions = dept_permissions.get(dept_id, dept_permissions["conteudo"])

    prompt_templates = {
        "conteudo": f"Você é {name}, membro do Departamento de Conteudo. Sua funcao e definida em config/editora/teams/01-conteudo/. Siga as diretrizes do departamento.",
        "editorial": f"Você é {name}, membro do Departamento Editorial. Sua funcao e definida em config/editora/teams/02-editorial/. Siga as diretrizes do departamento.",
        "design": f"Você é {name}, membro do Departamento de Design. Sua funcao e definida em config/editora/teams/03-design/. Siga as diretrizes do departamento.",
        "publicacao": f"Você é {name}, membro do Departamento de Publicacao. Sua funcao e definida em config/editora/teams/04-publicacao/. Siga as diretrizes do departamento.",
        "qa": f"Você é {name}, membro do Departamento de QA Editorial. Sua funcao e definida em config/editora/teams/05-qa/. Siga as diretrizes do departamento.",
    }

    return {
        "description": f"{name} — {dept_id}",
        "mode": "subagent",
        "permission": {
            tool: perm
            for tool, perm in sorted(permissions.items())
        },
        "prompt": prompt_templates.get(dept_id, f"Você é {name}. Consulte config/editora/teams/ para instrucoes especificas."),
    }


def build_prompt_from_team_file(agent_id: str, dept_id: str) -> str | None:
    """Tenta carregar prompt do arquivo de time do departamento."""
    team_dir = ROOT / "config" / "editora" / "teams"
    dept_map = {
        "conteudo": "01-conteudo",
        "editorial": "02-editorial",
        "design": "03-design",
        "publicacao": "04-publicacao",
        "qa": "05-qa",
        "branding": "06-branding",
    }
    dir_name = dept_map.get(dept_id)
    if not dir_name:
        return None
    # Procura por arquivo com nome do agente no diretorio
    prompt_dir = team_dir / dir_name
    if not prompt_dir.exists():
        return None
    for f in prompt_dir.iterdir():
        if f.stem == agent_id or f.stem.startswith(agent_id):
            return f.read_text(encoding="utf-8")
    return None


def main():
    parser = argparse.ArgumentParser(description="Sync agents between YAML and opencode.json")
    parser.add_argument("--apply", action="store_true", help="Generate opencode.json.new")
    parser.add_argument("--force", action="store_true", help="Overwrite opencode.json directly")
    args = parser.parse_args()

    departamentos = load_yaml(DEPARTAMENTOS)
    opencode = load_json(OPENCODE_JSON)

    yaml_agents = get_yaml_agent_ids(departamentos)
    json_agents = get_json_agent_ids(opencode)

    yaml_ids = {a[0] for a in yaml_agents}
    # Also include department leaders and separators
    json_ids_only_agents = {k for k in json_agents if not k.startswith("-----") and k != "build" and k != "plan"}

    missing = yaml_ids - json_ids_only_agents
    extra_json = json_ids_only_agents - yaml_ids
    common = yaml_ids & json_ids_only_agents

    print("=" * 60)
    print("AGENTS SYNC REPORT")
    print("=" * 60)
    print(f"\nYAML agents (departamentos.yaml):   {len(yaml_ids)}")
    print(f"JSON agents (opencode.json):        {len(json_ids_only_agents)}")
    print(f"Common:                             {len(common)}")
    print(f"Missing from JSON (to add):          {len(missing)}")
    print(f"Extra in JSON (not in YAML):         {len(extra_json)}")
    print()

    if missing:
        print("--- MISSING AGENTS (need to be added to opencode.json) ---")
        for agent_id in sorted(missing):
            name_info = next(((n, d) for aid, n, d in yaml_agents if aid == agent_id), (agent_id, "unknown"))
            print(f"  [{name_info[1]}] {agent_id} ({name_info[0]})")

    if extra_json:
        print("\n--- EXTRA AGENTS (in opencode.json but not in YAML departments) ---")
        for agent_id in sorted(extra_json):
            print(f"  {agent_id}")

    print()
    print(f"--- SYNC STATUS: {len(missing)} missing, {len(extra_json)} extra ---")

    if not args.apply:
        print("\nDica: Use --apply para gerar opencode.json.new com as adicoes.")
        return

    # Gerar opencode.json atualizado
    updated = json.loads(json.dumps(opencode))  # deep copy
    if "agent" not in updated:
        updated["agent"] = {}

    added = []
    for agent_id, name, dept_id in yaml_agents:
        if agent_id in json_ids_only_agents:
            continue
        config = classify_missing_agent(agent_id, name, dept_id)
        team_prompt = build_prompt_from_team_file(agent_id, dept_id)
        if team_prompt:
            config["prompt"] = team_prompt
        updated["agent"][agent_id] = config
        added.append(agent_id)

    if args.force:
        output_path = OPENCODE_JSON
    else:
        output_path = OUTPUT_JSON

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(updated, f, indent=2, ensure_ascii=False)

    print(f"\n--- {len(added)} agentes adicionados a {output_path} ---")
    if added:
        print("Adicionados:", ", ".join(sorted(added)))

    # Mostrar diff summary
    if not args.force:
        print(f"\nRevise o arquivo {OUTPUT_JSON} e, se estiver correto, substitua opencode.json:")
        print(f"  copy {OUTPUT_JSON} opencode.json")


if __name__ == "__main__":
    main()
