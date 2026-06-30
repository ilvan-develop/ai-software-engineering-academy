# Learning Design Audit — IA para Desenvolvedores

**Agente:** learning-designer
**Data:** 2026-06-28
**Versao:** 1.0.0
**Consome:** compiled/book.md (2353 linhas)

---

## 1. Taxonomia de Bloom — Cobertura por Capitulo

### Niveis Cognitivos Atendidos

| Nivel Bloom | Cap 1 | Cap 2 | Cap 3 | Total | Ideal |
|-------------|-------|-------|-------|-------|-------|
| Lembrar | 10% | 15% | 20% | 15% | 10% |
| Entender | 35% | 40% | 35% | 37% | 30% |
| Aplicar | 30% | 25% | 25% | 27% | 30% |
| Analisar | 15% | 10% | 10% | 12% | 15% |
| Avaliar | 10% | 5% | 5% | 7% | 10% |
| Criar | 0% | 5% | 5% | 3% | 5% |

### Mapa de Atividades por Nivel

```
Cap 1:
  LEMBRAR: Tabela de 5 erros na conclusao
  ENTENDER: Explicacao de cada erro com exemplos
  APLICAR: Exercicio de reescrever prompt
  ANALISAR: Desafio final — auditoria de codigo
  AVALIAR: "Pare e pense" — autoavaliacao
  CRIAR: --- (lacuna)

Cap 2:
  LEMBRAR: Tabela de 17 agentes
  ENTENDER: Anatomia de agente, diagramas de pipeline
  APLICAR: --- (lacuna)
  ANALISAR: --- (lacuna)
  AVALIAR: Comparacao agente generico vs. especializado
  CRIAR: Como criar novo agente (secao 4)

Cap 3:
  LEMBRAR: Checklist de boas praticas
  ENTENDER: Explicacao de CI/CD, IaC, deploys
  APLICAR: Exemplos de codigo executavel
  ANALISAR: --- (lacuna)
  AVALIAR: --- (lacuna)
  CRIAR: --- (lacuna)
```

### Lacunas por Nivel

| Nivel | Lacuna | Exemplo do que inserir |
|-------|--------|----------------------|
| **Criar (Cap 1)** | Leitor nao cria nada | "Escreva um prompt para sua ferramenta de IA seguindo o template" |
| **Aplicar (Cap 2)** | So teoria sobre agentes | "Configure um agente no OpenCode seguindo o template da secao 4" |
| **Analisar (Cap 3)** | Nenhum exercicio de analise | "Compare GitHub Actions vs GitLab CI para o mesmo cenario" |
| **Avaliar (Cap 3)** | Nenhum exercicio de avaliacao | "Qual estrategia de deploy escolher para cada cenario?" |

---

## 2. Tecnica de Feynman

### Aplicacao Atual

A tecnica de Feynman (explicar em linguagem simples) aparece em:

- **Analogia do estagiario brilhante** (Cap 1, conclusao) — 5/5
- **"E como perguntar 'Me recomenda um filme?'"** (Cap 1, Erro 2) — 4/5
- **Metafora do piloto automatico** (Cap 3) — 3/5 (sub-utilizada)

### Oportunidades de Feynman

| Conceito Complexo | Explicacao Atual | Explicacao Feynman Sugerida |
|-------------------|-----------------|---------------------------|
| CI/CD | "Integracao continua e deploy continuo" | "E como ter um robo que testa cada peca do carro assim que ela fica pronta, e se passar, ja leva pra linha de montagem" |
| Infrastructure as Code | "Gerenciamento de infra via arquivos versionados" | "E como ter a planta da sua casa em vez de decorar onde cada fio passa — se mudar, edita a planta, nao o fio" |
| Canary Deploy | "Porcentagem do trafego para nova versao" | "E como um chef que prova um pedaco antes de servir o prato inteiro — se estiver bom, serve; se nao, refaz" |
| Blue-Green | "Duas versoes do ambiente" | "E como ter dois aeroportos: enquanto um opera, voce reforma o outro. Quando ficar pronto, todo mundo voa do novo" |
| Self-healing | "Sistema que se recupera automaticamente" | "E como ter um medico de plantao 24h que monitora seus sinais vitais e ja aplica o remedio antes de voce sentir febre" |

### Checklist Feynman

- [ ] Cada conceito novo e explicado em analogia do mundo real? **PARCIAL** (so 2 boas analogias)
- [ ] A linguagem e simples o suficiente para um junior entender? **SIM** (Cap 1), **PARCIAL** (Cap 2), **NAO** (Cap 3)
- [ ] Ha "traducao" de jargao tecnico para linguagem cotidiana? **PARCIAL** — so no Cap 1
- [ ] O leitor consegue explicar o conceito para outro dev depois de ler? **PARCIAL**

---

## 3. Active Recall

### Mecanismos de Active Recall Existentes

| Mecanismo | Local | Eficacia |
|-----------|-------|----------|
| "Pare e pense" | Cap 1, linhas 43, 259 | 3/5 — aparece 2x, poderia ser mais |
| Exercicio pratico (diagnosticar prompt) | Cap 1, secao "Exercicio pratico" | 5/5 — bem estruturado com gabarito |
| Desafio final (auditar codigo) | Cap 1, secao "Desafio final" | 5/5 — excelente aplicacao pratica |
| Checklist de boas praticas | Cap 3, final | 2/5 — passivo, leitor so le |

### Lacunas de Active Recall

| Onde | O que falta | Sugestao |
|------|-------------|----------|
| Fim de cada erro (Cap 1) | Pergunta de revisao | "Antes de continuar: qual dos 4 tipos de bug voce acha mais comum em IA?" |
| Meio do Cap 2 | Pergunta de conexao | "Qual a diferenca entre um agente generico e um especializado? Tente explicar sem olhar a secao anterior" |
| Fim do Cap 2 | Mini-quiz | "3 perguntas sobre anatomia de agente" |
| Apos cada ferramenta no Cap 3 | Pergunta de comparacao | "O que o Terraform faz que o Pulumi tambem faz? E qual a diferenca?" |
| Final do livro | Revisao cumulativa | "Voce lembra dos 5 erros do capitulo 1? Liste-os antes de virar a pagina" |

### Estrategia de Spaced Repetition (para o livro inteiro)

```
Cap 1, Erro 1: Conceito apresentado
Cap 1, Erro 3: "Lembra do erro 1? Aqui ele aparece de novo no code review"
Cap 2, Secao 5: "Os 5 erros do cap 1 se aplicam a agentes tambem — como?"
Cap 3, Secao 12: "Checklist final referencia os 5 erros"
```

Atualmente so ha **1 referencia cruzada** (fraca) entre capitulos. Recomendo **5+ conexoes explicitas**.

---

## 4. Scaffolding (Andaime Pedagogico)

### Estrutura de Scaffolding Atual

```
Cap 1:        [Suporte total] → Exercicio guiado → Desafio semi-guiado
Cap 2:        [Suporte total] → (sem pratica)
Cap 3:        [Suporte parcial] → (sem pratica)
```

### Problema: Andaime Quebrado

```
Suporte
  ^
5 |████          Cap 1: suporte alto, pratica guiada
4 |████
3 |███           Cap 2: suporte alto, ZERO pratica
2 |██            Cap 3: suporte medio, ZERO pratica
1 |█
  +────────────────────────────►
   Cap 1         Cap 2         Cap 3
```

O livro comeca bem (Cap 1: explica → exemplo → pratica) mas o scaffolding desaparece nos capitulos seguintes.

### Scaffolding Recomendado

```
Cap 1 — "Eu faco, nos fazemos, voce faz"
  [EU FICO] Autor mostra o erro
  [NOS] Leitor e autor analisam juntos
  [VOCE] Exercicio diagnostico
  [VOCE SOZINHO] Desafio final

Cap 2 — "Modelagem + Template + Criacao"
  [MODELO] Anatomia de agente pronta
  [TEMPLATE] Estrutura para criar agente (secao 4)
  [PRATICA GUIADA] "Crie um agente para seu projeto atual"
  [PRATICA LIVRE] "Adapte o template para sua stack"

Cap 3 — "Exemplo + Contexto + Decisao + Automacao"
  [EXEMPLO] Pipeline pronta (GitHub Actions)
  [CONTEXTO] Variacoes (GitLab CI, Jenkins)
  [DECISAO] "Qual ferramenta escolher para cada cenario?"
  [AUTOMACAO] "Crie sua propria pipeline do zero"
```

---

## 5. Objetivos de Aprendizagem

### Objetivos Atuais (implicitos)

| Capitulo | Objetivo Atual | Problema |
|----------|---------------|----------|
| 1 | "Evitar erros ao usar IA" | OK, mas mensuravel? Como saber se evitou? |
| 2 | "Criar agentes especializados" | Nenhum criterio de "criou com sucesso" |
| 3 | "Automatizar ciclo de desenvolvimento" | Muito amplo — o que exatamente o leitor consegue automatizar? |

### Objetivos SMART Sugeridos

**Cap 1:**
- "Ao final deste capitulo, voce sera capaz de identificar e corrigir cada um dos 5 erros comuns em prompts e codigo gerado por IA, com 100% de acuracia no diagnostico"

**Cap 2:**
- "Ao final deste capitulo, voce sera capaz de estruturar um agente de IA especializado (com README, workflow, checklist e prompts) para qualquer dominio tecnico"

**Cap 3:**
- "Ao final deste capitulo, voce sera capaz de configurar uma pipeline CI/CD completa no GitHub Actions, incluindo lint, testes, build, deploy e rollback automatico"

---

## 6. Mecanismos de Retencao (Score Atual: 88/100)

### Problemas Identificados

| Mecanismo | Presente? | Nota | Melhoria |
|-----------|-----------|------|----------|
| Repeticoes espacadas | Nao | 2/5 | Adicionar referencias entre capitulos |
| Pratica distribuida | Parcial | 3/5 | Exercicios so no Cap 1 |
| Elaboracao | Parcial | 3/5 | Analogias boas mas raras |
| Dual coding (texto + imagem) | Parcial | 4/5 | Diagramas bons, mas com redundancia ASCII |
| Storytelling | Parcial | 3/5 | Bom no Cap 1, ausente nos demais |
| Perguntas de revisao | Parcial | 2/5 | So "Pare e pense" (2x) |
| Mnemonics | Nao | 1/5 | Criar acronimo para os 5 erros |
| Conexao com conhecimento previo | Parcial | 3/5 | Assume que leitor e dev — OK |

### Acronimo Sugerido: "C.A.P.R.I"

Para memorizar os 5 erros:

| Letra | Erro | Mnemonico |
|-------|------|-----------|
| **C** | Confiar cegamente | "C" de "Cego" |
| **A** | Ausencia de contexto | "A" de "Achar que IA advinha" |
| **P** | Pular code review | "P" de "Pular" |
| **R** | Regras nao configuradas | "R" de "Regras" |
| **I** | Iterar? Nao, primeira resposta | "I" de "Inicio = Fim" |

**Frase mnemonica:** "**C**ada **A**migo **P**recisa **R**ever **I**sso"

---

## 7. Mapa de Aprendizagem Integrado

### Progresao Recomendada

```
MODULO 1 — CONSCIENCIA (Bloom: Lembrar + Entender)
  ├── Pre-teste: "Voce comete esses 5 erros?"
  ├── Cap 1: Os 5 Erros
  │   ├── Cada erro: Exemplo → Consequencia → Correcao
  │   ├── Exercicio: Diagnosticar prompt ruim
  │   └── Desafio: Auditar codigo gerado por IA
  └── Pos-teste: Mesmo pre-teste — voce mudou?

MODULO 2 — CONSTRUCAO (Bloom: Aplicar + Analisar)
  ├── Cap 2: Agentes de IA
  │   ├── Template de agente (scaffolding)
  │   ├── Pratica guiada: Criar agente para projeto proprio
  │   └── Revisao por pares (ou autoavaliacao com checklist)
  └── Conexao: "Qual erro do Cap 1 seu agente vai ajudar a evitar?"

MODULO 3 — AUTOMACAO (Bloom: Analisar + Avaliar + Criar)
  ├── Cap 3a: Automacao Fundamental
  │   ├── CI/CD com template
  │   ├── Decisao: Qual ferramenta para cada caso?
  │   └── Projeto: Pipeline do zero
  ├── Cap 3b: Automacao Avancada
  │   ├── IaC + Seguranca + Monitoramento
  │   ├── Analise: Compare estrategias de deploy
  │   └── Projeto final: Pipeline completa com rollback
  └── Avaliacao final: "Sua pipeline esta pronta para producao?"

RETENCAO (Spaced Repetition)
  ├── Fim Cap 1: "Lembre dos 5 erros"
  ├── Fim Cap 2: "Como os erros se aplicam a agentes?"
  ├── Fim Cap 3: "Checklist completo"
  └── Extra: Flashcards mentais no final do livro
```

---

## 8. Metricas de Efetividade de Aprendizagem

| Indicador | Atual | Alvo | Gap |
|-----------|-------|------|-----|
| Exercicios por capitulo | 0.7 | 2 | -1.3 |
| Perguntas de revisao | 2 | 10+ | -8 |
| Referencias entre capitulos | 1 | 5+ | -4 |
| Analogias/metáforas | 3 | 8+ | -5 |
| Objetivos SMART | 0 | 3 | -3 |
| Mnemonics | 0 | 1-2 | -1 |
| Pratica guiada (scaffolding) | 1 | 6 | -5 |
| Momentos de autoavaliacao | 2 | 6+ | -4 |
| Nivel "Criar" (Bloom) | 1 secao | 3 secoes | -2 |
| Dual coding consistente | PARCIAL | SIM | --- |

---

*Fim do relatorio do learning-designer. Proximo: visual-comm-design.md*
