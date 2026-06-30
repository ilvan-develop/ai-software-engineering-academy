#!/usr/bin/env python3
"""
quiz_engine.py
Gera 10 perguntas de multipla escolha (2 facil, 5 medio, 3 dificil)
a partir de aula.md. Template-based (nao requer LLM).
"""

import argparse
import sys
import re
from pathlib import Path


def extract_title(text: str) -> str:
    for line in text.split("\n"):
        m = re.match(r"^#\s+(.+)$", line.strip())
        if m:
            return m.group(1).strip()
    return "Modulo"


def extract_headings(text: str) -> list:
    headings = []
    for line in text.split("\n"):
        m = re.match(r"^#{2,3}\s+(.+)$", line.strip())
        if m:
            headings.append(m.group(1).strip())
    return headings


def extract_key_concepts(text: str) -> list:
    concepts = []
    lines = text.split("\n")
    for line in lines:
        s = line.strip()
        if re.match(r"^#{2,3}\s+", s):
            concepts.append(re.sub(r"^#+\s+", "", s))
        elif re.match(r"^\d+\.\s+\*\*", s):
            c = re.sub(r"^\d+\.\s+\*\*", "", s)
            c = c.replace("**", "")
            concepts.append(c.strip())
    return concepts


def extract_tables(text: str) -> list:
    tables = []
    lines = text.split("\n")
    in_table = False
    table_lines = []
    for line in lines:
        s = line.strip()
        if s.startswith("|") and s.endswith("|"):
            table_lines.append(s)
            in_table = True
        else:
            if in_table and len(table_lines) >= 2:
                tables.append("\n".join(table_lines))
            in_table = False
            table_lines = []
    if in_table and len(table_lines) >= 2:
        tables.append("\n".join(table_lines))
    return tables


def generate_quiz(title: str, concepts: list, tables: list) -> str:
    topic = title.replace("Módulo", "").replace("—", "-").strip()

    q_pool = []

    # Easy questions (2)
    q_pool.append(f"""## Pergunta 1 (Fácil)

Qual é o conceito principal abordado em "{title}"?

- [ ] A) {concepts[-1] if len(concepts) > 3 else "Um tópico avançado"}
- [ ] B) {concepts[0] if concepts else "O tema central"}
- [ ] C) {concepts[1] if len(concepts) > 1 else "Um conceito periférico"}
- [ ] D) {concepts[2] if len(concepts) > 2 else "Um detalhe secundário"}

**Resposta correta:** B
**Explicação:** O conceito principal do módulo é "{concepts[0] if concepts else topic}", que serve como fundamento para todo o conteúdo abordado.
**Nível:** Fácil""")

    q_pool.append(f"""## Pergunta 2 (Fácil)

Segundo o módulo, qual das alternativas melhor descreve a aplicação prática do conteúdo?

- [ ] A) Apenas contextos acadêmicos e teóricos
- [ ] B) Situações hipotéticas sem aplicação real
- [ ] C) Problemas reais do dia a dia de desenvolvimento de software
- [ ] D) Exclusivamente para projetos de grande escala

**Resposta correta:** C
**Explicação:** O conteúdo do módulo é direcionado para aplicação prática em situações reais de engenharia de software, independentemente da escala do projeto.
**Nível:** Fácil""")

    # Medium questions (5)
    m_topics = concepts[1:6] if len(concepts) > 5 else concepts + ["Conceitos avançados"] * 5

    q_pool.append(f"""## Pergunta 3 (Médio)

Qual das seguintes afirmações sobre "{m_topics[0]}" está correta?

- [ ] A) É um conceito opcional que pode ser ignorado na maioria dos projetos
- [ ] B) Deve ser aplicado apenas em cenários específicos definidos pelo arquiteto
- [ ] C) Representa um princípio fundamental que impacta diretamente a qualidade do software
- [ ] D) É uma prática ultrapassada substituída por abordagens mais modernas

**Resposta correta:** C
**Explicação:** O conceito de "{m_topics[0]}" é fundamental para a qualidade do software, conforme demonstrado ao longo do módulo.
**Nível:** Médio""")

    q_pool.append(f"""## Pergunta 4 (Médio)

Ao implementar {m_topics[1] if len(m_topics) > 1 else 'os conceitos do módulo'}, qual é a principal armadilha a ser evitada?

- [ ] A) Seguir estritamente as boas práticas
- [ ] B) Ignorar o contexto e as restrições do projeto
- [ ] C) Documentar excessivamente as decisões
- [ ] D) Testar a solução antes de implementar

**Resposta correta:** B
**Explicação:** Ignorar o contexto e as restrições do projeto é um erro comum, pois cada situação requer adaptação dos conceitos aprendidos.
**Nível:** Médio""")

    q_pool.append(f"""## Pergunta 5 (Médio)

Qual a relação entre "{concepts[0] if concepts else 'o tema central'}" e os demais tópicos do módulo?

- [ ] A) São independentes e podem ser estudados separadamente
- [ ] B) Os demais tópicos são aplicações diretas do conceito central
- [ ] C) Não há relação direta entre os tópicos
- [ ] D) O conceito central contradiz os demais tópicos

**Resposta correta:** B
**Explicação:** O conceito central serve como base sobre a qual os demais tópicos são construídos e aplicados.
**Nível:** Médio""")

    q_pool.append(f"""## Pergunta 6 (Médio)

Em qual cenário a aplicação do conteúdo deste módulo traria MAIS benefícios?

- [ ] A) Um projeto legacy sem testes automatizados
- [ ] B) Um novo projeto seguindo as práticas recomendadas desde o início
- [ ] C) Uma migração de monólito para microsserviços
- [ ] D) Um projeto de curta duração com escopo bem definido

**Resposta correta:** B
**Explicação:** Aplicar os conceitos desde o início de um novo projeto maximiza os benefícios, evitando retrabalho e dívida técnica.
**Nível:** Médio""")

    q_pool.append(f"""## Pergunta 7 (Médio)

Qual métrica ou indicador melhor reflete o domínio do conteúdo deste módulo?

- [ ] A) Quantidade de código produzido
- [ ] B) Velocidade de execução das tarefas
- [ ] C) Qualidade das decisões técnicas tomadas
- [ ] D) Número de ferramentas dominadas

**Resposta correta:** C
**Explicação:** O módulo enfatiza que a qualidade das decisões técnicas é o principal diferencial, não a quantidade de código ou ferramentas.
**Nível:** Médio""")

    # Difficult questions (3)
    q_pool.append(f"""## Pergunta 8 (Difícil)

Analise as seguintes afirmações sobre "{topic}" e assinale a alternativa que contém APENAS afirmações corretas:

I. A aplicação correta dos conceitos reduz dívida técnica a longo prazo
II. Os princípios são universais e devem ser aplicados sem adaptação
III. O custo de implementação aumenta nas fases iniciais do projeto
IV. A documentação das decisões é tão importante quanto a implementação

- [ ] A) I, II e III
- [ ] B) I, III e IV
- [ ] C) II, III e IV
- [ ] D) I, II e IV

**Resposta correta:** B
**Explicação:** As afirmações I, III e IV estão corretas. A afirmação II é falsa porque os princípios devem ser adaptados ao contexto de cada projeto.
**Nível:** Difícil""")

    q_pool.append(f"""## Pergunta 9 (Difícil)

Um time está implementando um sistema complexo e precisa decidir entre duas abordagens: a abordagem A segue estritamente os conceitos do módulo; a abordagem B é mais pragmática e ignora alguns princípios em prol da velocidade. Qual deve ser a decisão do arquiteto?

- [ ] A) Escolher a abordagem A, pois principios jamais devem ser comprometidos
- [ ] B) Escolher a abordagem B, pois velocidade é sempre prioridade
- [ ] C) Analisar os trade-offs de cada abordagem no contexto especifico e decidir com base em criterios objetivos
- [ ] D) Combinar elementos de ambas sem criterio definido

**Resposta correta:** C
**Explicação:** A analise de trade-offs contextualizada é a abordagem mais madura. O modulo ensina conceitos, mas sua aplicação deve considerar o contexto real do projeto.
**Nível:** Difícil""")

    q_pool.append(f"""## Pergunta 10 (Difícil)

Considere o seguinte caso: uma empresa aplicou todos os conceitos do módulo mas ainda enfrenta problemas de qualidade. Qual é a causa MAIS provável?

- [ ] A) Os conceitos do módulo estao incorretos ou desatualizados
- [ ] B) A equipe nao compreendeu profundamente os conceitos, aplicando-os de forma mecanica
- [ ] C) Problemas de qualidade sao inevitaveis em projetos complexos
- [ ] D) A empresa deveria ter usado ferramentas diferentes

**Resposta correta:** B
**Explicação:** A aplicação mecânica sem compreensão profunda é uma das maiores causas de falha. Os conceitos precisam ser entendidos em sua essência para serem eficazes.
**Nível:** Difícil""")

    # Shuffle and number
    header = [
        f"# Quiz — {title}",
        "",
        "**Total de perguntas:** 10",
        "**Distribuição:** 2 Fáceis, 5 Médias, 3 Difíceis",
        "**Tempo estimado:** 20 minutos",
        "",
        "---",
        "",
    ]

    # Re-number questions 1-10
    renumbered = []
    for i, q in enumerate(q_pool, 1):
        q = re.sub(r"^## Pergunta \d+", f"## Pergunta {i}", q)
        renumbered.append(q)

    return "\n\n".join(header + renumbered)


def main():
    parser = argparse.ArgumentParser(description="Gerador de Quiz Template-Based")
    parser.add_argument("--input", required=True, help="Caminho para aula.md")
    parser.add_argument("--output", required=True, help="Pasta de saida (quiz/)")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERRO: Arquivo nao encontrado: {input_path}")
        sys.exit(1)

    text = input_path.read_text(encoding="utf-8")
    title = extract_title(text)
    concepts = extract_key_concepts(text)
    tables = extract_tables(text)

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    quiz = generate_quiz(title, concepts, tables)
    (output_dir / "quiz.md").write_text(quiz, encoding="utf-8")
    print(f"  OK Quiz: {output_dir / 'quiz.md'}")
    print(f"  [DONE] Quiz gerado para: {title}")


if __name__ == "__main__":
    main()
