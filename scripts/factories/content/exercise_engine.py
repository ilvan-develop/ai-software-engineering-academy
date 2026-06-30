#!/usr/bin/env python3
"""
exercise_engine.py
Gera 3 exercicios (facil/medio/dificil) + 1 mini-projeto a partir de aula.md.
Template-based (nao requer LLM).
"""

import argparse
import sys
import re
from pathlib import Path


def extract_headings(text: str) -> list:
    headings = []
    for line in text.split("\n"):
        m = re.match(r"^#{2,3}\s+(.+)$", line.strip())
        if m:
            headings.append(m.group(1).strip())
    return headings


def extract_learning_objectives(text: str) -> list:
    in_obj = False
    objectives = []
    for line in text.split("\n"):
        s = line.strip()
        if re.match(r"^##?\s*Objetivos?", s):
            in_obj = True
            continue
        if in_obj and s.startswith("##"):
            break
        if in_obj and re.match(r"^\d+\.\s+", s):
            obj = re.sub(r"^\d+\.\s*\*\*", "", s)
            obj = obj.replace("**", "")
            objectives.append(obj)
    return objectives


def extract_prerequisites(text: str) -> list:
    in_pre = False
    prereqs = []
    for line in text.split("\n"):
        s = line.strip()
        if re.match(r"##?\s*Pré-requisitos", s):
            in_pre = True
            continue
        if in_pre and s.startswith("##"):
            break
        if in_pre and s.startswith("- "):
            prereqs.append(s[2:])
    return prereqs


def extract_title(text: str) -> str:
    for line in text.split("\n"):
        m = re.match(r"^#\s+(.+)$", line.strip())
        if m:
            return m.group(1).strip()
    return "Modulo"


def generate_exercises(title: str, headings: list, objectives: list, prereqs: list) -> str:
    topic = title.replace("Módulo", "").replace("—", "-").strip()

    # Pick 3 sub-topics from headings
    sub_topics = [h for h in headings if not h.startswith("Introdu")]
    sub_topics = sub_topics[:5] if sub_topics else ["Conceitos principais"]

    lines = [
        f"# Exercícios — {title}",
        "",
        "---",
        "",
        "## Exercício 1 — Fácil: Verificação de Compreensão",
        "",
        f"**Contexto:** Você acabou de estudar '{topic}' e precisa verificar se entendeu os conceitos fundamentais.",
        "",
        "**Instruções:**",
        "1. Explique com suas palavras o conceito principal abordado no módulo",
        "2. Liste pelo menos 3 pontos-chave que você considerou mais importantes",
        "3. Dê um exemplo prático de como esse conhecimento se aplica no dia a dia",
        "",
        "**Critérios de sucesso:**",
        "- A explicação está coerente com o conteúdo do módulo",
        "- Os pontos-chave estão corretos e bem fundamentados",
        "- O exemplo prático é relevante e factível",
        "",
        "**Tempo estimado:** 15 minutos",
        "",
        "---",
        "",
        "## Exercício 2 — Médio: Aplicação Prática",
        "",
        f"**Contexto:** Seu time está implementando um sistema que envolve {sub_topics[0] if sub_topics else 'o tema abordado'}. Você precisa aplicar os conceitos do módulo para resolver um problema real.",
        "",
        "**Instruções:**",
        "1. Descreva uma situação real onde o conteúdo deste módulo seria aplicado",
        "2. Proponha uma solução passo a passo usando os conceitos aprendidos",
        "3. Identifique possíveis desafios ou armadilhas na implementação",
        "4. Compare sua abordagem com alternativas viáveis",
        "",
        "**Critérios de sucesso:**",
        "- A situação descrita é realista e relevante",
        "- A solução segue a metodologia apresentada no módulo",
        "- Os desafios identificados são pertinentes",
        "- A comparação com alternativas demonstra domínio do assunto",
        "",
        "**Tempo estimado:** 30 minutos",
        "",
        "---",
        "",
        "## Exercício 3 — Difícil: Análise Crítica",
        "",
        f"**Contexto:** Você é o arquiteto responsável por um projeto que utiliza {sub_topics[1] if len(sub_topics) > 1 else 'conceitos avançados do módulo'}. Um colega propôs uma abordagem diferente da ensinada no módulo.",
        "",
        "**Instruções:**",
        "1. Analise criticamente as duas abordagens (a do módulo vs. a proposta do colega)",
        "2. Crie uma tabela comparativa com prós e contras de cada uma",
        "3. Defina critérios objetivos para escolher entre as abordagens",
        "4. Recomende qual abordagem usar e justifique tecnicamente",
        "5. Inclua considerações sobre trade-offs (custo, performance, manutenibilidade)",
        "",
        "**Critérios de sucesso:**",
        "- A análise demonstra compreensão profunda dos conceitos",
        "- A tabela comparativa é objetiva e completa",
        "- Os critérios de decisão são mensuráveis e relevantes",
        "- A recomendação é justificada com argumentos técnicos sólidos",
        "- Os trade-offs são honestamente considerados",
        "",
        "**Tempo estimado:** 45 minutos",
        "",
        "---",
        "",
        "## Mini-Projeto: Aplicação Completa",
        "",
        f"**Tema:** Implementar uma solução completa usando os conceitos de '{topic}'",
        "",
        "**Cenário:**",
        f"Você foi contratado para resolver um problema real usando {sub_topics[2] if len(sub_topics) > 2 else 'os conceitos do módulo'}. O cliente espera uma solução bem documentada e testada.",
        "",
        "**Requisitos funcionais:**",
        "1. A solução deve abordar o problema central do módulo",
        "2. Deve incluir documentação explicando as decisões técnicas",
        "3. Deve ter pelo menos 2 exemplos de uso",
        "4. Deve considerar edge cases e tratamento de erros",
        "",
        "**Requisitos não-funcionais:**",
        "- Código legível e bem estruturado",
        "- Seguir as boas práticas discutidas no módulo",
        "- Incluir comentários explicativos nas partes complexas",
        "",
        "**Entregáveis:**",
        "1. Código fonte da solução",
        "2. README com instruções de uso",
        "3. Exemplos de execução",
        "4. Breve relatório (máx 1 página) explicando as decisões técnicas",
        "",
        "**Critérios de avaliação:**",
        "| Critério | Peso | Descrição |",
        "|----------|------|-----------|",
        "| Correção técnica | 40% | A solução resolve o problema proposto |",
        "| Qualidade do código | 25% | Organização, legibilidade, boas práticas |",
        "| Documentação | 20% | README, comentários, exemplos |",
        "| Análise crítica | 15% | Relatório com decisões e trade-offs |",
        "",
        "**Tempo estimado:** 2-3 horas",
    ]
    return "\n".join(lines)


def generate_gabarito(title: str, exercises: str) -> str:
    lines = [
        f"# Gabarito — Exercícios: {title}",
        "",
        "> ⚠️ Este gabarito é um guia de correção. Respostas podem variar desde que tecnicamente corretas.",
        "",
        "---",
        "",
        "## Exercício 1 (Fácil) — Critérios de Correção",
        "",
        "**O que verificar:**",
        "- O aluno identificou corretamente o conceito principal?",
        "- Os pontos-chave estão alinhados com o conteúdo do módulo?",
        "- O exemplo prático é coerente e viável?",
        "",
        "**Pontuação sugerida (0-10):**",
        "- 0-4: Não demonstra compreensão básica",
        "- 5-7: Compreensão parcial, mas com falhas",
        "- 8-10: Compreensão sólida e exemplo relevante",
        "",
        "---",
        "",
        "## Exercício 2 (Médio) — Critérios de Correção",
        "",
        "**O que verificar:**",
        "- A situação descrita é relevante para o conteúdo?",
        "- A solução segue a metodologia apresentada?",
        "- Os desafios identificados são pertinentes?",
        "- A comparação com alternativas demonstra domínio?",
        "",
        "**Pontuação sugerida (0-10):**",
        "- 0-4: Solução superficial ou incorreta",
        "- 5-7: Solução adequada mas sem profundidade",
        "- 8-10: Solução completa com análise crítica",
        "",
        "---",
        "",
        "## Exercício 3 (Difícil) — Critérios de Correção",
        "",
        "**O que verificar:**",
        "- A análise crítica considera múltiplas perspectivas?",
        "- A tabela comparativa é objetiva e completa?",
        "- Os critérios de decisão são mensuráveis?",
        "- A recomendação é bem justificada?",
        "- Os trade-offs são honestamente considerados?",
        "",
        "**Pontuação sugerida (0-10):**",
        "- 0-4: Análise superficial",
        "- 5-7: Análise adequada mas sem profundidade",
        "- 8-10: Análise excelente com considerações de trade-offs",
        "",
        "---",
        "",
        "## Mini-Projeto — Rubrica de Avaliação",
        "",
        "| Critério | Peso | Insuficiente (0-4) | Adequado (5-7) | Excelente (8-10) |",
        "|----------|------|-------------------|-----------------|-------------------|",
        "| Correção técnica | 40% | Solução não funciona ou errada | Funciona para caso básico | Robusta, cobre edge cases |",
        "| Qualidade do código | 25% | Código desorganizado | Organizado, boas práticas | Excelente, seguindo padrões |",
        "| Documentação | 20% | Sem documentação | README básico | Documentação completa |",
        "| Análise crítica | 15% | Sem relatório | Relatório superficial | Decisões bem justificadas |",
        "",
        "**Nota final:** Soma dos (pontos × peso) ÷ 10",
        "",
        "**Aprovação:** Mínimo 7.0 na média final",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Gerador de Exercicios Template-Based")
    parser.add_argument("--input", required=True, help="Caminho para aula.md")
    parser.add_argument("--output", required=True, help="Pasta de saida (exercicios/)")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERRO: Arquivo nao encontrado: {input_path}")
        sys.exit(1)

    text = input_path.read_text(encoding="utf-8")
    title = extract_title(text)
    headings = extract_headings(text)
    objectives = extract_learning_objectives(text)
    prereqs = extract_prerequisites(text)

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    exercises = generate_exercises(title, headings, objectives, prereqs)
    (output_dir / "exercicios.md").write_text(exercises, encoding="utf-8")
    print(f"  OK Exercicios: {output_dir / 'exercicios.md'}")

    gabarito = generate_gabarito(title, exercises)
    (output_dir / "gabarito.md").write_text(gabarito, encoding="utf-8")
    print(f"  OK Gabarito: {output_dir / 'gabarito.md'}")

    print(f"  [DONE] Exercicios gerados para: {title}")


if __name__ == "__main__":
    main()
