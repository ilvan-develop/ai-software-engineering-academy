# EXECUTION PLAN — Fase 5

**Orquestrador:** Chief Orchestrator
**Data:** 2026-07-07
**Base:** ENTERPRISE_ARCHITECTURE.md (Fase 4)

---

## Estrategia de Execucao

1. **Uma sprint por vez** — nunca pular para a proxima sem validar a anterior
2. **Cada sprint produz artefato tangivel** — script, config, ou documento executavel
3. **Validacao** — ao final de cada sprint, rodar o artefato e registrar resultado no ORCHESTRATION_LOG.md
4. **Nao construir plataforma antes de catalogar** — Layer 3 (catalog) e prerequisito para Layer 5 (distribution)
5. **Primeiro BQS, depois CI** — BQS define o que e "qualidade", CI automatiza a verificacao

---

## Sprint 0 — Populate Catalog (GAP 1)

**Objetivo:** catalog.yaml deixa de estar vazio. Todos os 26 modulos e 4 livros catalogados.

### Tarefas

| # | Tarefa | Tipo | Depende |
|---|---|---|---|
| 0.1 | Criar `scripts/catalog_populator.py` | Script | — |
| 0.2 | Ler `curriculum/status.yaml` e extrair modulos + livros | Implementacao | 0.1 |
| 0.3 | Para cada modulo, extrair: id, titulo, curso, topicos, nivel, audiencia, prerequisitos | Implementacao | 0.2 |
| 0.4 | Para cada livro, extrair: id, titulo, capitulos, formatos, status | Implementacao | 0.2 |
| 0.5 | Popular `knowledge-factory/registry/catalog.yaml` | Implementacao | 0.3 + 0.4 |
| 0.6 | Validar contra `schemas/catalog.schema.json` | Validacao | 0.5 |
| 0.7 | Criar `scripts/graph_populator.py` — gera `graph.yaml` a partir dos prerequisitos entre modulos | Script | 0.5 |
| 0.8 | Validacao: rodar catalog_populator.py, verificar catalog.yaml populado | QA | 0.5-0.7 |

### Criterio de Aceite
- `catalog.yaml` contem items para todos os 26 modulos + 4 livros
- Cada item tem: id, titulo, tipo, topicos (vinculados a taxonomy.yaml), nivel, audiencia, status
- Schema validation passa
- `graph.yaml` gerado com dependencias entre modulos

### Esforco Estimado: 2-3 blocos de trabalho

---

## Sprint 1 — BQS Baseline (GAP 3)

**Objetivo:** BQS computado para todos os modulos e livros, nao apenas ia-para-devs.

### Tarefas

| # | Tarefa | Tipo | Depende |
|---|---|---|---|
| 1.1 | Auditar `curriculum/bqs/bqs-core.yaml` — 16 categorias estao completas? | Auditoria | — |
| 1.2 | Criar `scripts/bqs_compute.py` — le modulo.md + BQS schema → computa score por categoria | Script | 1.1 |
| 1.3 | Testar em 1 modulo (ia-para-devs) para verificar se o score bate com 92.8 | Validacao | 1.2 |
| 1.4 | Rodar bqs_compute.py para todos os 26 modulos | Batch | 1.3 |
| 1.5 | Rodar bqs_compute.py para os 4 livros (book.md) | Batch | 1.3 |
| 1.6 | Salvar resultados em `knowledge-factory/products/metrics/modules.csv` | Persistencia | 1.4 |
| 1.7 | Gerar relatorio: "BQS Baseline — Julho 2026" | Documento | 1.5 |

### Criterio de Aceite
- Todos os 26 modulos tem score BQS
- Scores sao salvos em CSV com data
- Relatorio gerado destacando modulos abaixo de 80

### Esforco Estimado: 3-4 blocos de trabalho

---

## Sprint 2 — CI/CD Foundations (GAP 2 + GAP 9)

**Objetivo:** CI basico rodando no GitHub Actions.

### Tarefas

| # | Tarefa | Tipo | Depende |
|---|---|---|---|
| 2.1 | Criar `tests/` com estrutura basica (tests/test_*.py) | Estrutura | — |
| 2.2 | Adicionar pytest + ruff + mypy ao requirements.txt | Config | — |
| 2.3 | Criar `.github/workflows/ci.yml` — roda em todo PR | CI | 2.1-2.2 |
| 2.4 | Criar `scripts/link_checker.py` — varre .md em busca de links quebrados | Script | — |
| 2.5 | Adicionar link_checker ao ci.yml | CI | 2.3, 2.4 |
| 2.6 | Criar `.github/workflows/nightly-bqs.yml` — roda BQS todo sabado | CI | Sprint 1 |
| 2.7 | Testar: abrir PR, verificar CI passa | Validacao | 2.3 |

### Criterio de Aceite
- PR aberto dispara ci.yml automaticamente
- Ruff + mypy + pytest passam
- Link checker identifica links quebrados existentes (se houver)
- Nightly BQS roda em schedule

### Esforco Estimado: 3-4 blocos de trabalho

---

## Sprint 3 — Agents Sync (GAP 4)

**Objetivo:** 42 agentes registrados no opencode.json, espelhando departamentos.yaml.

### Tarefas

| # | Tarefa | Tipo | Depende |
|---|---|---|---|
| 3.1 | Analisar `config/editora/departamentos.yaml` — mapear 42 agentes com permissoes | Auditoria | — |
| 3.2 | Analisar `opencode.json` — identificar os ~20 agentes ja registrados | Auditoria | — |
| 3.3 | Criar `scripts/agents_sync.py` — le YAML e gera/config atualiza opencode.json | Script | 3.1, 3.2 |
| 3.4 | Para cada agente faltante, definir permissoes minimas (read, glob, grep) | Decisao | 3.3 |
| 3.5 | Agentes com permissoes write: justificar e registrar no log | Decisao | 3.4 |
| 3.6 | Gerar opencode.json atualizado + diff | Implementacao | 3.5 |
| 3.7 | Validar: opencode.json e valido? Orquestrador consegue chamar novos agentes? | QA | 3.6 |

### Criterio de Aceite
- agents_sync.py executavel
- opencode.json atualizado com os 22 agentes faltantes
- Diff claro do que foi adicionado
- Orquestrador principal consegue chamar pelo menos 1 novo agente

### Esforco Estimado: 2-3 blocos de trabalho

---

## Sprint 4 — METADATA.yaml + Governance (GAP 10)

**Objetivo:** Cada modulo passa a ter metadados estruturados.

### Tarefas

| # | Tarefa | Tipo | Depende |
|---|---|---|---|
| 4.1 | Definir schema de `METADATA.yaml` por modulo | Schema | — |
| 4.2 | Criar `scripts/metadata_populator.py` — gera METADATA.yaml para cada modulo | Script | 4.1 |
| 4.3 | Adicionar campos: id, topicos, prerequisitos, autor, revisores, versao, changelog | Implementacao | 4.2 |
| 4.4 | Popular 26 modulos com METADATA.yaml | Batch | 4.3 |
| 4.5 | Validar: CI verifica METADATA.yaml em cada PR | CI | Sprint 2 |

### Criterio de Aceite
- Todo modulo tem METADATA.yaml
- Schema validado
- CI verifica metadata em PRs

### Esforco Estimado: 2 blocos de trabalho

---

## Sprint 5 — Static Site V1 (GAP 5 + GAP 6)

**Objetivo:** Site institucional com showcase + blog + search estatico.

**Nota:** Esta sprint requer decisoes de framework e design. Opcao recomendada: Next.js (SSG) + Tailwind + Fuse.js.

### Tarefas

| # | Tarefa | Tipo | Depende |
|---|---|---|---|
| 5.1 | Decidir framework (recomendado: Next.js + Tailwind) | Decisao | — |
| 5.2 | Criar `web/` com Next.js e configuracao basica | Tech setup | 5.1 |
| 5.3 | Pagina inicial: showcase 4 livros + 6 cursos | Implementacao | 5.2 |
| 5.4 | Pagina de livro: descricao, metadata, download links | Implementacao | 5.3 |
| 5.5 | Blog: extrair artigos dos modulos (via catalog.yaml) | Implementacao | Sprint 0 |
| 5.6 | Search: fuse.js sobre catalog.yaml | Implementacao | Sprint 0 |
| 5.7 | Formulario de lead capture (newsletter) | Implementacao | 5.5 |
| 5.8 | Seção "Sobre" com manifesto da editora | Conteudo | — |
| 5.9 | Deploy (Vercel / GitHub Pages) | Infra | 5.2 |
| 5.10 | CI/CD do site: deploy automatico em push na web/ | CI | Sprint 2 |

### Criterio de Aceite
- Site publicado (URL acessivel)
- 4 livros com pagina propria + download
- Search funcional
- Blog com posts
- Lead capture funcionando

### Esforco Estimado: 5-7 blocos de trabalho

---

## Sprint 6 — i18n Pipeline (GAP 7)

**Objetivo:** Pipeline de internacionalizacao com foco en-US.

### Tarefas

| # | Tarefa | Tipo | Depende |
|---|---|---|---|
| 6.1 | Criar `scripts/i18n_pipeline.py` — coordena tradutor + revisor nativo | Script | — |
| 6.2 | Criar `curriculum/i18n/` com estrutura de diretorios | Estrutura | — |
| 6.3 | Traduzir 1 modulo piloto (ia-para-devs) para en-US | Piloto | 6.1 |
| 6.4 | Revisao por nativo (humano ou agente com prompt apropriado) | QA | 6.3 |
| 6.5 | CI: verificar integridade das traducoes (mesmo numero de secoes, links, etc) | CI | Sprint 2 |

### Criterio de Aceite
- 1 modulo traduzido e revisado
- Pipeline documentado
- CI verifica estrutura

### Esforco Estimado: 3-4 blocos de trabalho

---

## Backlog Priorizado

| Prioridade | Item | Sprint | GAP | Esforco | Impacto |
|---|---|---|---|---|---|
| P0 | catalog_populator.py | Sprint 0 | GAP 1 | Medio | **Catalogo deixa de ser vazio** |
| P0 | bqs_compute.py + baseline | Sprint 1 | GAP 3 | Medio | **Qualidade verificavel** |
| P0 | ci.yml + lint + test | Sprint 2 | GAP 2, 9 | Alto | **Pipeline automatizado** |
| P0 | link_checker.py | Sprint 2 | GAP 2 | Baixo | **Links quebrados identificados** |
| P1 | agents_sync.py | Sprint 3 | GAP 4 | Medio | **42 agentes operacionais** |
| P1 | METADATA.yaml | Sprint 4 | GAP 10 | Medio | **Governanca editorial** |
| P1 | Static site V1 | Sprint 5 | GAP 5, 6 | Alto | **Presenca web + showcase** |
| P2 | i18n pipeline | Sprint 6 | GAP 7 | Medio | **Expansao internacional** |
| P2 | Graph RAG | Futuro | GAP 1 | Alto | **Search semântico** |
| P2 | Plataforma web full | Futuro | GAP 6 | Muito Alto | **Experiencia completa** |
| P2 | Chief Branding Officer | Futuro | GAP 5 | Medio | **Departamento de branding** |

---

## Matriz de Dependencias entre Sprints

```
Sprint 0 (Catalog) ────→ Sprint 5 (Static Site — precisa catalog.yaml)
     │
     └──→ Sprint 1 (BQS — precisa modulos) ──→ Sprint 2 (CI — precisa BQS + tests)
              │                                          │
              └──────────────────────────────────────────┘
                                 │
                          Sprint 3 (Agents — independente)
                          Sprint 4 (Metadata — independente)
                          Sprint 6 (i18n — independente, mas ideal apos CI)
```

Sprints 3, 4, e 6 podem rodar em paralelo com Sprints 0-2 se houver recursos.

---

## Time Estimado

| Sprint | Blocos | Paralelizavel? | Estimativa |
|---|---|---|---|
| Sprint 0 — Catalog | 3 | Sim | 1 sessao |
| Sprint 1 — BQS | 4 | Sim | 1-2 sessoes |
| Sprint 2 — CI/CD | 4 | Parcial | 1-2 sessoes |
| Sprint 3 — Agents | 3 | Sim (com 0-2) | 1 sessao |
| Sprint 4 — Metadata | 2 | Sim (com 0-2) | 1 sessao |
| Sprint 5 — Static Site | 7 | Parcial | 2-3 sessoes |
| Sprint 6 — i18n | 4 | Sim (com 5) | 1-2 sessoes |
| **Total** | **27** | — | **7-12 sessoes** |

---

## Risco e Mitigacao

| Risco | Probabilidade | Impacto | Mitigacao |
|---|---|---|---|
| catalog.yaml populado mas schema quebrado | Baixa | Medio | Validar contra schema.json |
| BQS scores baixos em modulos (abaixo de 70) | Media | Alto | Aceitar baseline honesto; plano de melhoria depois |
| CI nao passa por configuracao do GitHub | Media | Alto | Testar localmente antes de push |
| Static site sem designer visual | Alta | Medio | Usar template Tailwind pronto (shadcn/ui) |
| Agentes novos causam conflito no opencode.json | Baixa | Alto | agents_sync.py faz diff antes de aplicar |
| Escopo cresce durante execucao | Alta | Medio | Manter uma tarefa por vez; backlog separado |

---

## Proximo Passo

Fase 6 — Bootstrap Inicial: executar Sprint 0 (Catalog Populator).
