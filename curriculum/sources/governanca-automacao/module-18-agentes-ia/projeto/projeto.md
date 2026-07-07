# Projeto Módulo 18 — Criar um Agente Especializado

## Objetivo

Criar um agente especializado completo utilizando a estrutura padronizada da formação.

## Contexto

Você precisa criar um **Data Science Expert Agent** para ser usado em projetos que envolvem análise de dados, machine learning e visualização.

Este agente será usado por times de engenharia que precisam integrar funcionalidades de dados em seus sistemas Enterprise (dashboards, relatórios, predições).

## Entregáveis

### 1. README.md — Identidade do agente

Defina:
- **Nome:** Data Science Expert Agent
- **Objetivo** (2-3 frases)
- **Domínio:** análise de dados, ML, visualização
- **Stack:** Python, pandas, scikit-learn, matplotlib, Jupyter
- **Responsabilidades** (5-7 itens)
- **Limites** (3-4 itens — o que ele NÃO faz)

### 2. workflow.md — Processo

Descreva o fluxo de trabalho em 7-10 passos:
```text
1. Receber requisição de análise
2. ...
```markdown

### 3. checklist.md — Qualidade

Crie um checklist com 10+ itens de validação, organizado em categorias:
- Qualidade dos dados
- Qualidade do código
- Qualidade da análise
- Documentação
- Reproducibilidade

### 4. prompts/ — Templates

Crie 3 templates de prompt:

1. **analise-dados.md** — "Analise este dataset e produza insights"
   - Inclua: formato de entrada (CSV/JSON), tipo de análise, visualizações esperadas

2. **criar-modelo.md** — "Treine um modelo de ML para este problema"
   - Inclua: tipo de problema (classificação/regressão), métricas, validação

3. **dashboard.md** — "Crie visualizações para este dataset"
   - Inclua: tipo de gráfico, público-alvo, interatividade

### 5. Teste prático

Aplique o agente que você criou para analisar o seguinte cenário:

> "Dataset de vendas com 50.000 registros contendo: data, produto, categoria, região, vendedor, valor, quantidade. O time de negócios quer entender:
> - Top 10 produtos mais vendidos
> - Sazonalidade das vendas por mês
> - Performance por região e vendedor
> - Previsão de vendas para o próximo trimestre"

Escreva o prompt que você usaria para invocar o agente neste cenário.

## Critérios de avaliação

- [ ] Estrutura completa (README, workflow, checklist, 3 prompts)
- [ ] Responsabilidades e limites claros
- [ ] Checklist específico e acionável
- [ ] Prompts seguem o padrão (contexto + requisitos + formato de saída)
- [ ] Prompt do teste prático é eficaz
- [ ] Agente é autocontido (não depende de outros agentes)
