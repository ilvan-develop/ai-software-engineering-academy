# Product Design Audit — IA para Desenvolvedores

**Agente:** product-designer
**Data:** 2026-06-28
**Versao:** 1.0.0
**Consome:** compiled/book.md, design-tokens.yaml, brand-book.md, layout-grid.yaml

---

## 1. JTBD (Jobs to Be Done) Analise

### Job Principal
"Quando estou comecando a usar IA para programar, quero aprender a usar essas ferramentas sem introduzir bugs e divida tecnica no meu codigo, para poder entregar mais rapido com confianca."

### Jobs Secundarios
1. "Quero saber quais erros evitar antes de comete-los" — **Cap 1 atende bem**
2. "Quero configurar agentes de IA no meu projeto atual" — **Cap 2 atende parcialmente (falta tutorial pratico)**
3. "Quero automatizar meu workflow de desenvolvimento com IA" — **Cap 3 atende, mas com salto de complexidade**
4. "Quero justificar o uso de IA para meu tech lead/gerente" — **Nao atendido explicitamente**
5. "Quero entender quais ferramentas de IA existem e qual escolher" — **Nao atendido (gap critico)**

### Mapa de JTBD vs. Capitulos

```
JTBD                        Cap 1    Cap 2    Cap 3    Gap?
─────────────────────────────────────────────────────────────
Evitar erros ao usar IA     [SIM]    [NAO]    [NAO]    ---
Configurar agentes           [PARCIAL] [SIM]   [NAO]    Tutorial pratico
Automatizar workflow         [NAO]    [PARCIAL] [SIM]   Ponte entre caps
Justificar uso de IA        [NAO]    [NAO]    [NAO]    GRAVE
Escolher ferramentas         [NAO]    [NAO]    [NAO]    GRAVE
Manter codigo gerado por IA [NAO]    [NAO]    [NAO]    GRAVE
Depurar codigo de IA        [NAO]    [NAO]    [NAO]    GRAVE
```

---

## 2. Jornada do Leitor (Micro-UX)

### Jornada Atual (Mapeada)

```
┌─────────────────────────────────────────────────────────────────┐
│ JORNADA DO LEITOR — Estado Atual                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ [Entrada]                                                        │
│   Leitor quer aprender a usar IA para programar                  │
│       │                                                          │
│       v                                                          │
│ [Capa & Titulo]                                                  │
│   "IA para Desenvolvedores" — expectativa: guia pratico          │
│       │                                                          │
│       v                                                          │
│ [Introducao: 63% dos devs erraram]                               │
│   ✅ Gancho forte — dados que geram identificacao                │
│       │                                                          │
│       v                                                          │
│ [Erro 1 → Erro 2 → Erro 3 → Erro 4 → Erro 5]                   │
│   ✅ Estrutura clara, exemplos reais                             │
│   ⚠️ Sequencia pode ser melhorada (ver IA audit)                 │
│   ⚠️ Sem callouts visuais — texto denso                          │
│       │                                                          │
│       v                                                          │
│ [Conclusao Cap 1: 5 Mandamentos]                                 │
│   ✅ Resumo forte, tabela util                                   │
│       │                                                          │
│       v                                                          │
│ [Transicao para Cap 2]                                           │
│   ⚠️ Transicao abrupta — sem introducao entre capitulos         │
│       │                                                          │
│       v                                                          │
│ [Cap 2: Agentes de IA]                                           │
│   ⚠️ Comeca com "Quando montei meu primeiro time" — bom, mas     │
│      leitor pode pensar "ainda nao montei time nenhum"           │
│   ⚠️ Muitas tabelas e diagramas sem contexto textual previo      │
│       │                                                          │
│       v                                                          │
│ [Transicao para Cap 3]                                           │
│   ⚠️ Quase inexistente — so um titulo de parte                  │
│       │                                                          │
│       v                                                          │
│ [Cap 3: Automacao]                                               │
│   ⚠️ Salto de senioridade abrupto                               │
│   ⚠️ Longo (1354 linhas) — fadiga a partir da secao 7           │
│   ⚠️ Secoes finais (10-12) parecem apressadas, menos exemplos   │
│       │                                                          │
│       v                                                          │
│ [Saida]                                                          │
│   ❌ Sem "E agora?" — o que o leitor faz depois?                 │
│   ❌ Sem chamada para acao final                                 │
│   ❌ Sem curadoria de proximos passos                            │
└─────────────────────────────────────────────────────────────────┘
```

### Pontos de Atrito na Jornada

| Ponto | Problema | Impacto | Severidade |
|-------|----------|---------|------------|
| Transicao Cap 1 → 2 | Sem pre-texto ou introducao | Quebra de fluxo | Media |
| Transicao Cap 2 → 3 | Part-title generico ("---") | Perda de contexto | Alta |
| Meio do Cap 3 (secao 6+) | Carga cognitiva excessiva | Abandono | Alta |
| Final do livro | Nenhum "proximo passo" | Sensacao de incompletude | Alta |
| Sempre que ha tabela longa | Quebra o ritmo narrativo | Cansaço visual | Media |

---

## 3. Carga Cognitiva por Capitulo

### Analise de Carga (SWAT — Subjective Workload Assessment)

| Elemento | Cap 1 | Cap 2 | Cap 3 | Ideal |
|----------|-------|-------|-------|-------|
| Novos conceitos por pagina | 2.1 | 3.4 | 5.8 | ≤3 |
| Exemplos de codigo | 6 | 2 | 15 | 4-6 |
| Diagramas | 2 | 6 | 1 | 2-4 |
| Tabelas | 7 | 3 | 5 | 3-4 |
| Termos tecnicos novos | 8 | 15 | 28 | ≤10 |
| Exercicios praticos | 2 | 0 | 0 | 1-2 |

### Pico de Carga Cognitiva

```
Carga
  ^
10 |                    ██
 9 |                    ██
 8 |                    ██
 7 |                    ██
 6 |  ██               ██
 5 |  ██  ██           ██
 4 |  ██  ██  ██       ██
 3 |  ██  ██  ██  ██   ██
 2 |  ██  ██  ██  ██   ██
 1 |  ██  ██  ██  ██   ██
 0 +──────────────────────────►
    Cap1  Cap2  Cap3  Cap3   Cap3
    geral       sec1-6  sec7-9  sec10-12
```

**Nota:** Cap 3 secoes 10-12 tem densidade de conceitos 3x maior que Cap 1. O leitor provavelmente chegara exausto nessas secoes e retera menos.

### Recomendacoes para Reducao de Carga

1. **Quebrar blocos de texto longos** com subtitulos H3 a cada 15-20 linhas de texto corrido
2. **Adicionar caixas "Pare e Recapitule"** a cada 3 secoes no Cap 3
3. **Substituir 2 tabelas grandes** no Cap 1 por diagramas visuais
4. **Adicionar sumario executivo** no inicio de cada secao do Cap 3 ("O que voce vai aprender aqui:")
5. **Glossario lateral** para termos tecnicos na primeira aparicao

---

## 4. Micro-UX: Friccoes Identificadas

### Problemas de Navegacao

| Friccao | Local | Solucao |
|---------|-------|---------|
| Titulos H1 duplicados | book.md:22-24 | Remover duplicacao (ja reportado) |
| Dois H1 consecutivos | Transicoes de parte | Usar part-title como H2 ou separador visual |
| Links sem descricao | "Leituras complementares" | Adicionar descricao do que esperar em cada link |
| Codigo sem indicacao de linguagem em 1 bloco | Cap 3 | Adicionar ```yaml ou ```typescript |
| Tabelas sem cabecalho visivel em P&B | Cap 1, tabela de 5 erros | Adicionar indicadores B&W-safe |
| Caminho de leitura nao-linear | Todo o livro | Adicionar "Se voce tem pressa, leia:" no inicio |

### Problemas de Formatacao

| Problema | Impacto |
|----------|---------|
| Listas muito longas (10+ itens) sem quebra visual | Leitor perde o fim da lista |
| Tabelas com celulas de texto longo | Dificil leitura em mobile/EPUB |
| Codigo com linhas > 80 chars | Quebra feia em impressao |
| Diagramas ASCII redundantes com Mermaid | Espaco desperdicado |

---

## 5. Heuristicas de Produto (Nielsen Aplicado a Livros)

| Heuristica | Nota (1-5) | Problemas |
|------------|-------------|-----------|
| Visibilidade do estado do sistema | 4 | Sumario claro, mas sem indicador de progresso no capitulo |
| Correspondencia com o mundo real | 5 | Excelente — exemplos reais, analogia do estagiario |
| Controle e liberdade do usuario | 2 | Sem saidas de emergencia (secoes muito longas sem checkpoint) |
| Consistencia e padroes | 3 | Tabelas tem formatos variados; diagramas em estilos diferentes |
| Prevencao de erros | 4 | Boa, mas falta alerta sobre "este topico requer X conhecimento" |
| Reconhecimento vs. recordacao | 3 | Termos tecnicos sem glossario; leitor precisa lembrar o que significa |
| Flexibilidade e eficiencia | 2 | Sem atalhos para leitores avancados (skimming guides) |
| Design estetico e minimalista | 3 | Informacao densa, falta espaco para respirar |
| Ajuda para diagnosticar erros | 4 | Bons exemplos de codigo RUIM vs BOM |
| Documentacao e ajuda | 2 | Falta "O que fazer se..." e guia de troubleshooting |

**Score geral de usabilidade:** 3.2/5

---

## 6. Recomendacoes Prioritarias

### Criticas (fazer antes da proxima edicao)

1. **Adicionar transicoes entre capitulos** — mini-introducoes de 2-3 paragrafos conectando o fim de um ao inicio do proximo
2. **Criar um "Proximo Passos" no final** — 3-5 acoes concretas que o leitor pode tomar apos terminar o livro
3. **Adicionar checkpoint "Pare e Recapitule"** a cada 3 secoes no Cap 3
4. **Inserir avisos de pre-requisito** "Esta secao assume que voce conhece Docker. Se nao, pule para X"

### Importantes

5. **Criar mapa de navegacao por nivel de experiencia** (ver IA audit)
6. **Adicionar glossario pop-up/nota de rodape** para primeiras aparicoes de termos
7. **Reduzir tabelas a 5-7 linhas maximo** — dividir tabelas grandes em 2+ menores
8. **Adicionar progress bar** no EPUB/PDF digital ("Voce esta em 45% do livro")

### Desejaveis

9. **Adicionar "Para quem tem pressa" boxes** no inicio de cada secao longa
10. **Criar versao "skimmable"** com highlights do conteudo mais importante
11. **Adicionar checklists de acao** no final de cada capitulo (alem dos exercicios)

---

*Fim do relatorio do product-designer. Proximo: reading-experience-audit.md*
