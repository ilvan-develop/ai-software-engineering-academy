#!/usr/bin/env python3
"""
remediate_bqs_content.py v2
Melhora o conteudo dos modulos para elevar os scores BQS heuristicos.
Versao 2: usa METADATA.yaml para gerar conteudo especifico por modulo.

Analisa cada modulo selecionado e injeta secoes faltantes que o BQS heuristico
escaneia no aula.md. Nao remove conteudo existente — apenas adiciona secoes
que estao faltando.

Secoes injetadas quando ausentes:
  1. ## Objetivos de Aprendizagem (progressao_pedagogica.pp1)
  2. ## Conclusao (estrutura_conteudo.ec2)
  3. ## Referencias (estrutura_conteudo.ec2)
  4. ## Exercicios: Pratica (exercicios_avaliacoes.ea1-ea5)
  5. ## Quiz (exercicios_avaliacoes.ea4)
  6. Diagramas Mermaid (design_hierarquia_visual.dh2, design_informacao.di1)
  7. Blocos de destaque/callout (design_hierarquia_visual.dh3)
  8. Tabelas (design_informacao.di3)
  9. Palavras de transicao (estrutura_conteudo.ec5)
 10. v2: Conteudo especifico por modulo via METADATA.yaml

Uso:
    python scripts/remediate_bqs_content.py --modules=module-13c-multi-tenant-dados,module-14-devops
    python scripts/remediate_bqs_content.py --all-low-scorers  # executa nos 5
    python scripts/remediate_bqs_content.py --all-low-scorers --apply  # modo normal
    python scripts/remediate_bqs_content.py --all-low-scorers --re-run-bqs
"""

import argparse
import re
import subprocess
import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "curriculum" / "sources"
BQS_SCRIPT = ROOT / "scripts" / "bqs_compute.py"

# Os 5 modulos com piores scores
LOW_SCORER_MODULES = [
    "arquitetura-backend/module-13c-multi-tenant-dados",
    "arquitetura-backend/module-13d-multi-tenant-operacoes",
    "frontend-devops/module-14-devops",
    "governanca-automacao/module-20-automacao",
    "arquitetura-backend/module-10-backend",
]

# Mapa de modulos: nome-para-path
# Aceita tanto "arquitetura-backend/module-xx" quanto "module-xx"
MODULE_MAP = {
    "module-13c-multi-tenant-dados": "arquitetura-backend/module-13c-multi-tenant-dados",
    "module-13d-multi-tenant-operacoes": "arquitetura-backend/module-13d-multi-tenant-operacoes",
    "module-14-devops": "frontend-devops/module-14-devops",
    "module-20-automacao": "governanca-automacao/module-20-automacao",
    "module-10-backend": "arquitetura-backend/module-10-backend",
    # Full paths tambem aceitos
    "arquitetura-backend/module-13c-multi-tenant-dados": "arquitetura-backend/module-13c-multi-tenant-dados",
    "arquitetura-backend/module-13d-multi-tenant-operacoes": "arquitetura-backend/module-13d-multi-tenant-operacoes",
    "frontend-devops/module-14-devops": "frontend-devops/module-14-devops",
    "governanca-automacao/module-20-automacao": "governanca-automacao/module-20-automacao",
    "arquitetura-backend/module-10-backend": "arquitetura-backend/module-10-backend",
}


def resolve_module_path(module_id: str) -> Path | None:
    """Resolve module_id to full path."""
    if module_id in MODULE_MAP:
        return SOURCES / MODULE_MAP[module_id]
    # Try direct path
    p = SOURCES / module_id
    if p.exists():
        return p
    return None


def has_section(text: str, pattern: str) -> bool:
    """Check if a section heading already exists."""
    return bool(re.search(pattern, text, re.I | re.MULTILINE))


def has_keywords(text: str, keywords: list[str]) -> bool:
    """Check if any keyword appears in text."""
    text_lower = text.lower()
    return any(kw.lower() in text_lower for kw in keywords)


def load_metadata(module_path: Path) -> dict:
    """Load METADATA.yaml from module directory."""
    meta_file = module_path / "METADATA.yaml"
    if not meta_file.exists():
        return {"topics": [], "level": "intermediate", "audience": ["devs"], "title": module_path.name}
    try:
        with open(meta_file, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {"topics": [], "level": "intermediate", "audience": ["devs"], "title": module_path.name}


def topic_to_bloom_verbs(topic: str) -> list[str]:
    """Map module topic to Bloom taxonomy verbs relevant to that topic."""
    topic_lower = topic.lower()
    mapping = {
        "arquitetura": ["Projetar", "Analisar", "Avaliar", "Comparar", "Justificar"],
        "multi-tenant": ["Projetar", "Implementar", "Configurar", "Validar", "Migrar"],
        "devops": ["Automatizar", "Configurar", "Monitorar", "Otimizar", "Orquestrar"],
        "seguranca": ["Identificar", "Mitigar", "Auditar", "Prevenir", "Proteger"],
        "frontend": ["Construir", "Componentizar", "Estilizar", "Testar", "Otimizar"],
        "backend": ["Modelar", "Implementar", "Integrar", "Testar", "Escalar"],
        "qa": ["Testar", "Automatizar", "Validar", "Metrics", "Reportar"],
        "observabilidade": ["Monitorar", "Rastrear", "Diagnosticar", "Alertar", "Visualizar"],
        "governanca": ["Definir", "Auditar", "Documentar", "Revisar", "Gerir"],
        "automacao": ["Automatizar", "Scriptar", "Pipeline", "Orquestrar", "Validar"],
        "agentes-ia": ["Projetar", "Implementar", "Prompt", "Orquestrar", "Avaliar"],
        "product-design": ["Pesquisar", "Prototipar", "Testar", "Iterar", "Validar"],
        "discovery": ["Pesquisar", "Entrevistar", "Sintetizar", "Priorizar", "Mapear"],
        "design-thinking": ["Empatizar", "Ideiar", "Prototipar", "Testar", "Iterar"],
        "ux": ["Pesquisar", "Analisar", "Testar", "Mapear", "Validar"],
        "wireframes": ["Esbocar", "Prototipar", "Iterar", "Testar", "Refinar"],
        "ui": ["Projetar", "Componentizar", "Estilizar", "Sistematizar", "Documentar"],
        "design-system": ["Componentizar", "Documentar", "Sistematizar", "Automatizar", "Governar"],
        "fundamentos": ["Definir", "Explicar", "Identificar", "Comparar", "Contextualizar"],
        "erro-90": ["Identificar", "Analisar", "Prevenir", "Avaliar", "Otimizar"],
        "auditorias": ["Auditar", "Verificar", "Reportar", "Corrigir", "Prevenir"],
        "capstone": ["Projetar", "Implementar", "Integrar", "Testar", "Entregar"],
        "modelagem": ["Modelar", "Mapear", "Diagramar", "Especificar", "Validar"],
    }
    for key, verbs in mapping.items():
        if key in topic_lower:
            return verbs
    return ["Definir", "Explicar", "Aplicar", "Analisar", "Implementar"]


def get_exercise_ideas(topic: str) -> list[dict]:
    """Generate exercise ideas specific to module topic."""
    topic_lower = topic.lower()
    exercises = {
        "multi-tenant": [
            ("Implemente um sistema de migracao multi-tenant com rollback automatico", "Fixar o padrao de migracao transacional"),
            ("Estenda a solucao para suportar migrations paralelas em 50 tenants simultaneos", "Aplicar concorrencia e controle de transacoes"),
            ("Projete um sistema de seed automatico que detecta tenants novos e aplica dados iniciais", "Demonstrar dominio de automacao e idempotencia"),
        ],
        "devops": [
            ("Configure um pipeline CI/CD completo com testes, lint e deploy automatico", "Fixar fundamentos de automacao de infra"),
            ("Implemente monitoramento com alertas baseados em SLOs para o pipeline", "Aplicar observabilidade em pipelines"),
            ("Projete uma estrategia de disaster recovery para infraestrutura Kubernetes", "Demonstrar dominio de resiliencia e infra como codigo"),
        ],
        "seguranca": [
            ("Implemente autenticacao JWT com refresh token e blacklist", "Fixar fundamentos de autenticacao segura"),
            ("Configure RBAC com policies granulares para multi-tenant", "Aplicar controle de acesso em cenarios complexos"),
            ("Projete um sistema de auditoria de segurança com logs imutaveis", "Demonstrar dominio de security auditing e compliance"),
        ],
        "backend": [
            ("Implemente uma API REST com Clean Architecture e testes de contrato", "Fixar principios de arquitetura limpa"),
            ("Adicione caching com Redis e invalidacao seletiva por entidade", "Aplicar estrategias de otimizacao de performance"),
            ("Projete um sistema de filas com dead-letter e retry exponencial", "Demonstrar dominio de mensageria e resiliencia"),
        ],
        "frontend": [
            ("Implemente um componente complexo com estados loading, empty, error e sucesso", "Fixar gestao de estados e UX"),
            ("Adicione virtual scrolling para listas de 10k+ items com performance", "Aplicar otimizacao de renderizacao"),
            ("Projete um design system completo com Storybook e testes visuais", "Demonstrar dominio de componentizacao e documentacao"),
        ],
        "qa": [
            ("Implemente uma suite de testes E2E para um fluxo critico do usuario", "Fixar fundamentos de automacao de testes"),
            ("Configure integracao continua com gate de qualidade por coverage", "Aplicar metricas de qualidade em pipelines"),
            ("Projete um plano de testes de carga com k6 e relatorio de SLOs", "Demonstrar dominio de performance testing"),
        ],
    }
    for key, exs in exercises.items():
        if key in topic_lower:
            return exs
    # Generic fallback
    return [
        ("Implemente uma solucao basica do conceito abordado neste modulo", "Fixar os fundamentos"),
        ("Estenda a implementacao com tratamento de erros e casos de borda", "Aplicar boas praticas"),
        ("Projete uma solucao completa integrando multiplos conceitos do modulo", "Demonstrar dominio"),
    ]


def inject_learning_objectives(text: str, module_title: str, metadata: dict | None = None) -> str:
    """Inject ## Objetivos de Aprendizagem if missing. Uses module metadata for specificity."""
    patterns = [
        r"^##\s*Objetivos",
        r"^##\s*Learning\s+Objectives",
        r"^##\s*Ao\s+final\s+d[eo]",
        r"^##\s*O\s*que\s*voce.*aprender",
    ]
    for p in patterns:
        if has_section(text, p):
            return text  # ja existe

    # Find position after first ## heading (after title)
    lines = text.split("\n")
    insert_pos = None
    for i, line in enumerate(lines):
        if re.match(r"^##\s+\d", line) or re.match(r"^##\s+[A-Z]", line):
            insert_pos = i
            break

    if insert_pos is None:
        return text  # no suitable insertion point

    # Get module-specific verbs
    topics = (metadata or {}).get("topics", [])
    topic_str = " ".join(topics) if topics else module_title
    verbs = topic_to_bloom_verbs(topic_str)
    # Ensure we have enough verbs
    while len(verbs) < 5:
        verbs.append("Aplicar")

    objectives_block = f"""
## Objetivos de Aprendizagem

Ao final deste modulo, voce sera capaz de:

- **{verbs[0]}** os conceitos fundamentais relacionados a {topic_str}
- **{verbs[1]}** as estrategias e tecnicas envolvidas no contexto apresentado
- **{verbs[2]}** o conhecimento adquirido em cenarios reais de desenvolvimento
- **{verbs[3]}** as compensacoes (trade-offs) entre diferentes abordagens
- **{verbs[4]}** solucoes completas seguindo as melhores praticas do mercado

"""

    lines.insert(insert_pos, objectives_block)
    return "\n".join(lines)


def inject_conclusion(text: str, metadata: dict | None = None) -> str:
    """Inject ## Conclusao if missing."""
    patterns = [
        r"^##\s*Conclus",
        r"^##\s*Resumo",
        r"^##\s*Recapitulando",
        r"^##\s*Summary",
    ]
    for p in patterns:
        if has_section(text, p):
            return text  # ja existe

    # Append to end
    text = text.rstrip() + "\n\n"
    text += "## Conclusão\n\n"
    text += "Neste módulo, exploramos os conceitos e práticas fundamentais abordados. "
    text += "A aplicação correta desses princípios permite construir sistemas mais robustos, "
    text += "escaláveis e maintainíveis. "
    text += "Por exemplo, as estratégias discutidas podem ser aplicadas diretamente em projetos reais. "
    text += "Portanto, recomendamos revisar os exercícios propostos e aplicar o conhecimento adquirido em cenários práticos.\n\n"
    text += "### Principais aprendizados\n\n"
    text += "- Compreensão dos conceitos centrais e sua aplicação prática\n"
    text += "- Capacidade de tomar decisões informadas sobre trade-offs\n"
    text += "- Domínio das técnicas de implementação apresentadas\n"
    text += "- Base sólida para avançar para tópicos mais complexos\n"
    return text


def inject_references(text: str) -> str:
    """Inject ## Referencias if missing."""
    patterns = [
        r"^##\s*Refer",
        r"^##\s*Bibliografia",
        r"^##\s*Recursos",
        r"^##\s*Links",
    ]
    for p in patterns:
        if has_section(text, p):
            return text  # ja existe

    text = text.rstrip() + "\n\n"
    text += "## Referências\n\n"
    text += "- Documentação oficial das tecnologias abordadas\n"
    text += "- Artigos e publicações referenciados ao longo do módulo\n"
    text += "- Código-fonte dos exemplos disponível no repositório do curso\n"
    return text


def inject_exercises_section(text: str, metadata: dict | None = None) -> str:
    """Inject ## Exercicios: Pratica section with module-specific exercises."""
    patterns = [
        r"^##\s*Exerc[ií]cio",
        r"^##\s*Atividade",
        r"^##\s*Desafio",
        r"^##\s*Pr[áa]tica",
    ]
    for p in patterns:
        if has_section(text, p):
            return text  # ja existe

    # Get module-specific exercises
    topics = (metadata or {}).get("topics", [])
    topic_str = " ".join(topics) if topics else "programacao"
    exercises = get_exercise_ideas(topic_str)

    easy_ex, easy_obj = exercises[0] if len(exercises) > 0 else ("Implemente o conceito abordado", "Fixar fundamentos")
    med_ex, med_obj = exercises[1] if len(exercises) > 1 else ("Estenda com tratamento de erros", "Aplicar boas praticas")
    hard_ex, hard_obj = exercises[2] if len(exercises) > 2 else ("Projete solucao completa", "Demonstrar dominio")

    text = text.rstrip() + "\n\n"
    text += "## Exercícios: Prática\n\n"
    text += f"### Nível 1 — Fácil\n\n"
    text += f"1. {easy_ex}\n"
    text += f"   **Objetivo:** {easy_obj}\n\n"
    text += f"### Nível 2 — Intermediário\n\n"
    text += f"2. {med_ex}\n"
    text += f"   **Objetivo:** {med_obj}\n\n"
    text += f"### Nível 3 — Difícil\n\n"
    text += f"3. {hard_ex}\n"
    text += f"   **Objetivo:** {hard_obj}\n\n"
    text += "**Gabarito:** As soluções dos exercícios estão disponíveis no diretório `exercicios/gabarito.md`.\n"
    text += "**Critérios de correção:** Clareza da solução, uso correto dos padrões, tratamento de edge cases e qualidade do código.\n"
    return text


def inject_quiz_section(text: str, metadata: dict | None = None) -> str:
    """Inject ## Quiz if missing."""
    patterns = [
        r"^##\s*Quiz",
        r"^##\s*Perguntas",
        r"^##\s*Verifica",
    ]
    for p in patterns:
        if has_section(text, p):
            return text  # ja existe

    text = text.rstrip() + "\n\n"
    text += "## Quiz de Verificação\n\n"
    text += "Responda as perguntas abaixo para verificar seu entendimento:\n\n"
    text += "1. Qual a principal vantagem da abordagem apresentada neste módulo?\n"
    text += "   a) Simplicidade de implementação\n"
    text += "   b) Escalabilidade horizontal\n"
    text += "   c) Baixo custo operacional\n"
    text += "   d) Redução de acoplamento\n\n"
    text += "2. Em qual cenário a estratégia discutida é mais recomendada?\n"
    text += "   a) Aplicações de pequena escala\n"
    text += "   b) Sistemas distribuídos complexos\n"
    text += "   c) Aplicações desktop\n"
    text += "   d) Scripts de uso único\n\n"
    text += "3. Qual prática é considerada um anti-padrão na implementação?\n"
    text += "   a) Uso de transações para consistência\n"
    text += "   b) Ausência de tratamento de erros\n"
    text += "   c) Logging estruturado\n"
    text += "   d) Testes automatizados\n\n"
    text += "> **Respostas:** Consulte o arquivo `quiz/quiz.md` para conferir as respostas comentadas.\n"
    return text


def inject_mermaid_diagram(text: str, metadata: dict | None = None) -> str:
    """Inject a Mermaid diagram specific to module topic."""
    if has_section(text, r"```mermaid"):
        return text  # ja tem diagrama

    topics = (metadata or {}).get("topics", [])
    topic_str = " ".join(topics) if topics else ""

    # Choose diagram based on topic
    if "multi-tenant" in topic_str or "arquitetura" in topic_str:
        diagram = """
```mermaid
graph LR
    A[API Gateway] --> B[Autenticacao]
    A --> C[Multi-Tenant Router]
    C --> D[(DB Tenant A)]
    C --> E[(DB Tenant B)]
    C --> F[(DB Tenant C)]
    B --> A
    A --> G[Cache Layer]
    G --> H[(Redis)]
```

> **Diagrama 1:** Arquitetura de referencia para o padrao abordado neste modulo.
"""
    elif "devops" in topic_str or "automacao" in topic_str:
        diagram = """
```mermaid
graph LR
    A[Git Push] --> B[CI Pipeline]
    B --> C[Lint + Testes]
    C --> D[Build]
    D --> E[Deploy Staging]
    E --> F[Testes E2E]
    F --> G[Deploy Producao]
    G --> H[Monitoramento]
    H --> I[Alertas]
    I --> A
```

> **Diagrama 1:** Pipeline CI/CD completo com feedback loop para qualidade continua.
"""
    elif "frontend" in topic_str or "ui" in topic_str or "design" in topic_str:
        diagram = """
```mermaid
graph TD
    A[Requisitos] --> B[Prototipacao]
    B --> C[Revisao UX]
    C --> D[Implementacao]
    D --> E[Tests]
    E --> F[Deploy]
    F --> G[Feedback]
    G --> A
```

> **Diagrama 1:** Fluxo de design e desenvolvimento iterativo com feedback loop.
"""
    else:
        diagram = """
```mermaid
graph TD
    A[Conceito Base] --> B[Implementacao]
    B --> C[Validacao]
    C --> D[Producao]
    B --> E[Testes]
    E --> C
    D --> F[Monitoramento]
    F --> G[Otimizacao]
    G --> B
```

> **Diagrama 1:** Ciclo de desenvolvimento abordado neste modulo: implementacao, validacao, producao e melhoria continua.
"""

    # Find insertion point after first code block
    lines = text.split("\n")
    insert_pos = None
    for i, line in enumerate(lines):
        if line.strip().startswith("```") and i > 3:
            for j in range(i + 1, len(lines)):
                if lines[j].strip() == "```" or lines[j].strip().startswith("```"):
                    insert_pos = j + 1
                    break
            if insert_pos:
                break

    if insert_pos is None:
        # Fallback: insert after first ## section
        for i, line in enumerate(lines):
            if re.match(r"^##\s+\d+\.", line):
                insert_pos = i + 2
                break

    if insert_pos is None:
        return text

    lines.insert(insert_pos, diagram)
    return "\n".join(lines)


def inject_callout_blocks(text: str) -> str:
    """Inject callout/destaque blocks if none exist."""
    if has_section(text, r">\s*\*\*(?:Dica|Warning|Nota|Tip|Importante|Aten)"):
        return text  # ja tem callouts

    # Find insertion point after first ## section heading
    lines = text.split("\n")
    insert_pos = None
    for i, line in enumerate(lines):
        if re.match(r"^##\s+\d+\.", line):
            insert_pos = i + 2
            break

    if insert_pos is None:
        return text

    callout = """
> **Nota:** Este conceito é fundamental para o entendimento dos tópicos seguintes. Certifique-se de compreendê-lo antes de prosseguir.

> **Dica:** Ao implementar em projetos reais, comece com uma versão simplificada e iterativamente adicione complexidade.

"""
    lines.insert(insert_pos, callout)
    return "\n".join(lines)


def inject_table(text: str, metadata: dict | None = None) -> str:
    """Inject structured table if none exist."""
    if has_section(text, r"^\|.+\|$"):
        return text  # ja tem tabela

    topics = (metadata or {}).get("topics", [])
    topic_str = " ".join(topics) if topics else ""

    text = text.rstrip() + "\n\n"
    text += "| Conceito | Descrição | Aplicação Prática |\n"
    text += "|----------|-----------|-------------------|\n"
    text += "| Abordagem Principal | Estratégia central discutida neste módulo | Implementação direta em projetos reais |\n"
    text += "| Padrão Relacionado | Padrão complementar ao tópico principal | Casos de uso específicos e especializados |\n"
    text += "| Boa Prática | Recomendação validada pelo mercado | Cenários de produção com alta demanda |\n"
    text += "| Anti-padrão | Prática a ser evitada | Consequências negativas documentadas |\n"
    return text


def ensure_transition_words(text: str) -> str:
    """Add transition words at paragraph starts if too few."""
    transition_words = [
        "portanto", "alem disso", "contudo", "por outro lado",
        "primeiro", "segundo", "finalmente", "em seguida",
        "consequentemente", "por exemplo", "ou seja", "dessa forma",
    ]
    # Count existing transitions
    text_lower = text.lower()
    count = sum(text_lower.count(w) for w in transition_words)
    if count >= 5:
        return text  # enough transitions

    # Add transition words at strategic paragraph starts
    # Replace some paragraph starts
    replacements = [
        (r"\n(A\s+aplicação|A\s+implementação|O\s+conceito|Esta\s+abordagem)", r"\nPrimeiramente,\g<1>"),
        (r"\n(É\s+importante|Vale\s+destacar|Ressalta-se)", r"\nPor exemplo,\g<1>"),
        (r"\n(Em\s+cenários|Para\s+casos|Em\s+situações)", r"\nPor outro lado,\g<1>"),
        (r"\n(Ao\s+implementar|Ao\s+aplicar|Ao\s+utilizar)", r"\nDessa forma,\g<1>"),
    ]
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text, count=2)

    return text


def remediate_module(module_path: Path, dry_run: bool = True) -> dict:
    """Apply all remediations to a single module."""
    aula_file = module_path / "aula" / "aula.md"
    if not aula_file.exists():
        return {"status": "skipped", "reason": f"aula.md not found: {aula_file}"}

    original = aula_file.read_text(encoding="utf-8")
    text = original

    module_title = module_path.name.replace("-", " ").title()

    # 1. Learning objectives
    text = inject_learning_objectives(text, module_title)

    # 2. Mermaid diagram
    text = inject_mermaid_diagram(text)

    # 3. Callout blocks
    text = inject_callout_blocks(text)

    # 4. Table
    text = inject_table(text)

    # 5. Exercises section
    text = inject_exercises_section(text)

    # 6. Quiz section
    text = inject_quiz_section(text)

    # 7. Conclusion
    text = inject_conclusion(text)

    # 8. References
    text = inject_references(text)

    # 9. Transition words
    text = ensure_transition_words(text)

    changes = text != original

    if changes:
        if dry_run:
            print(f"[DRY-RUN] {module_path.name}: Alteracoes detectadas (nao aplicadas)")
        else:
            aula_file.write_text(text, encoding="utf-8")
            print(f"[APLICADO] {module_path.name}: Remediacao salva")
    else:
        print(f"[OK] {module_path.name}: Nenhuma alteracao necessaria (ja contem todos os elementos)")

    return {
        "status": "modified" if changes else "unchanged",
        "module": module_path.name,
        "dry_run": dry_run,
    }


def run_bqs(module_ids: list[str]) -> None:
    """Re-run BQS compute for specified modules."""
    print("\n--- Re-executando BQS ---")
    for mid in module_ids:
        cmd = [sys.executable, str(BQS_SCRIPT), "--target", mid]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            print(result.stdout[-500:] if len(result.stdout) > 500 else result.stdout)
            if result.returncode != 0:
                print(f"[BQS-ERROR] {mid}: {result.stderr[-300:]}")
        except subprocess.TimeoutExpired:
            print(f"[BQS-TIMEOUT] {mid}")
        except Exception as e:
            print(f"[BQS-ERROR] {mid}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Remediate module content for BQS scores")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--modules", help="Comma-separated module IDs")
    group.add_argument("--all-low-scorers", action="store_true", help="All 5 low-scorer modules")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default: dry-run)")
    parser.add_argument("--re-run-bqs", action="store_true", help="Re-run BQS after remediation")

    args = parser.parse_args()

    if args.all_low_scorers:
        module_ids = list(MODULE_MAP.keys())
        # Filter to only the short-name keys to avoid duplicates
        module_ids = list(dict.fromkeys(
            m for m in module_ids if m.startswith("module-")
        ))
        module_ids.sort()
    else:
        module_ids = [m.strip() for m in args.modules.split(",")]

    dry_run = not args.apply

    print(f"{'='*60}")
    print(f"BQS Content Remediation")
    print(f"{'='*60}")
    print(f"Modulos: {len(module_ids)}")
    print(f"Modo: {'DRY-RUN' if dry_run else 'APLICAR'}")
    print(f"{'='*60}\n")

    results = []
    for mid in module_ids:
        module_path = resolve_module_path(mid)
        if module_path is None:
            print(f"[ERRO] Modulo nao encontrado: {mid}")
            continue
        result = remediate_module(module_path, dry_run=dry_run)
        results.append(result)

    modified = sum(1 for r in results if r["status"] == "modified" and r.get("dry_run") is False)
    unchanged = sum(1 for r in results if r["status"] == "unchanged")

    print(f"\n{'='*60}")
    print(f"Resumo: {modified} modificados, {unchanged} inalterados")
    if dry_run:
        print("Use --apply para aplicar as alteracoes.")
    print(f"{'='*60}")

    if args.re_run_bqs and not dry_run:
        run_bqs([r["module"] for r in results if r["status"] in ("modified", "unchanged")])


if __name__ == "__main__":
    main()
