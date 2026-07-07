# ENTERPRISE ARCHITECTURE — Fase 4

**Orquestrador:** Chief Orchestrator
**Data:** 2026-07-07
**Base:** GAP_ANALYSIS.md (Fase 3) + estruturas existentes

---

## Principio Arquitetural

> Nao construir do zero. Evoluir a arquitetura existente adicionando as camadas que faltam, com interfaces claras entre elas.

O projeto ja tem 4 das 5 camadas em estado embrionario. O que falta e:
- **Conectar** as camadas entre si (hoje saem ilhas)
- **Automatizar** o fluxo entre elas (hoje manual)
- **Adicionar** a camada de distribuicao (hoje inexistente)

---

## Arquitetura em 5 Camadas

```
┌─────────────────────────────────────────────────────────────┐
│  5. DISTRIBUTION & EXPERIENCE                               │
│  Web App · API · LMS · Marketplace · Social · Certificates  │
│  ── responsabilidade: consumir, interagir, aprender        │
├─────────────────────────────────────────────────────────────┤
│  4. PRODUCTS                                                │
│  Books · Courses · Slides · Videos · Social · Newsletters   │
│  ── responsabilidade: gerar outputs multi-formato          │
├─────────────────────────────────────────────────────────────┤
│  3. KNOWLEDGE (Registry & Intelligence)                     │
│  Catalog · Taxonomy · Graph · Search · RAG · Recommender   │
│  ── responsabilidade: organizar, descobrir, recomendar     │
├─────────────────────────────────────────────────────────────┤
│  2. PIPELINE & ORCHESTRATION                                │
│  Agents · Scripts · CI/CD · Quality Gates · BQS · Tests    │
│  ── responsabilidade: automatizar, verificar, orquestrar   │
├─────────────────────────────────────────────────────────────┤
│  1. SOURCE (Curriculum)                                     │
│  Modules · Lessons · Exercises · Quizzes · Projects        │
│  ── responsabilidade: armazenar o conhecimento canonico   │
└─────────────────────────────────────────────────────────────┘
```

### Fluxo entre camadas

```
Layer 1 (Source) ──[git push]──→ Layer 2 (Pipeline)
                                       │
                              ┌────────┴────────┐
                              ▼                  ▼
                     Layer 3 (Knowledge)   Layer 4 (Products)
                              │                  │
                              └────────┬─────────┘
                                       ▼
                              Layer 5 (Distribution)
```

---

## Layer 1 — Source (curriculum/)

**Estado atual:** Funcional, 26 modulos, 6 cursos, 4 livros. A camada mais madura.

**Gaps enderecados:** GAP 7 (i18n), GAP 10 (governance)

### Estrutura-alvo

```
curriculum/sources/{curso}/{modulo}/
├── aula/aula.md                     ← OK (ja existe)
├── slides/slides.md                 ← OK
├── exercicios/                      ← OK
├── quiz/                            ← OK
├── projeto/                         ← OK
├── agentes/                         ← OK (prompts de IA)
├── i18n/                            ← NOVO
│   ├── en-US/aula.md
│   ├── en-US/slides.md
│   └── es/aula.md
└── METADATA.yaml                    ← NOVO (metadados do modulo)
    ├── id, titulo, descricao
    ├── topicos (vinculados a taxonomy.yaml)
    ├── prerequisitos (ids de modulos)
    ├── autor, revisores, versao
    └── changelog
```

### Dependencias
- Nao depende de outras camadas
- Layer 2 consome esta camada

---

## Layer 2 — Pipeline & Orchestration

**Estado atual:** Scripts Python existem mas sem automacao, sem CI/CD, sem testes. ~20 de 42 agentes registrados.

**Gaps enderecados:** GAP 2 (CI/CD), GAP 3 (quality/BQS), GAP 4 (agents), GAP 9 (tests), GAP 10 (governance)

### Componentes-alvo

```
scripts/
├── pipeline_manager.py           ← REFATORAR: adicionar modo CI
├── book_architect.py             ← OK
├── book_publisher.py             ← OK (avaliar substituir por Pandoc/Quarto)
├── bqs_compute.py                ← NOVO: computa BQS para modulo/livro
├── bqs_dashboard.py              ← NOVO: gera dashboard de qualidade
├── catalog_populator.py          ← NOVO: popula catalog.yaml a partir dos sources
├── link_checker.py               ← NOVO: verifica links em todo conteudo
├── code_verifier.py              ← NOVO: testa exemplos de codigo
├── i18n_pipeline.py              ← NOVO: coordena traducao + revisao nativa
├── agents_sync.py                ← NOVO: sincroniza departamentos.yaml → opencode.json
│
.github/workflows/
├── ci.yml                        ← NOVO: lint + test + BQS em cada PR
├── publish.yml                   ← NOVO: trigger manual, build + publish
├── nightly-bqs.yml               ← NOVO: BQS recorrente em todos os modulos
├── catalog-sync.yml              ← NOVO: re-popula catalogo semanalmente
│
.github/ISSUE_TEMPLATE/
├── new-module.md                 ← NOVO
├── module-update.md              ← NOVO
└── bug-report.md                 ← NOVO
```

### Fluxo CI/CD

```
Push / PR na Layer 1
    ↓
ci.yml:
    ├── ruff + mypy (scripts/)
    ├── pytest (tests/)
    ├── link_checker.py (todos os .md)
    ├── code_verifier.py (exemplos de codigo)
    └── bqs_compute.py (modulos alterados) → report
    ↓
Se PR aprovado + merge:
    └── publish.yml:
        ├── book_architect.py (se book manifest alterado)
        ├── book_publisher.py → outputs
        ├── batch_*.py → conteudo complementar
        ├── catalog_populator.py → atualiza catalog.yaml
        └── deploy (se houver Layer 5)
```

### Agentes

Sincronizar departamentos.yaml → opencode.json:
- Script agents_sync.py le departamentos.yaml e gera/config atualiza opencode.json
- Agentes faltantes (22) sao registrados com permissoes minimas (read, glob, grep inicialmente)
- Agentes com permissoes write so apos gatekeeper approval

---

## Layer 3 — Knowledge (Registry & Intelligence)

**Estado atual:** catalog.yaml vazio, taxonomy.yaml preenchido mas isolado, graph.yaml nao existe, search/RAG inexistente.

**Gaps enderecados:** GAP 1 (catalog), GAP 8 (metrics)

### Componentes-alvo

```
knowledge-factory/registry/
├── catalog.yaml                  ← POPULAR: items com id, titulo, tipo, topicos, nivel, audiencia, prereqs
├── taxonomy.yaml                 ← OK (ja preenchido)
├── graph.yaml                    ← NOVO: grafo de dependencias entre modulos/livros
├── embeddings/                   ← NOVO
│   ├── modules.embeddings        ← embeddings de cada modulo (para RAG/search)
│   └── books.embeddings          ← embeddings de cada livro
└── search/                       ← NOVO
    ├── search_engine.py          ← search hibrido (BM25 + embeddings + RRF)
    └── rag_engine.py             ← Graph RAG sobre modulos + catalog
```

### Catalog Schema (atualizar catalog.schema.json se necessario)

```yaml
items:
  - id: "modulo-arquitetura-backend-08"
    type: "module"
    titulo: "Domain-Driven Design"
    curso: "arquitetura-backend"
    topicos: ["ddd", "dominio", "linguagem-ubiqua"]
    nivel: "avancado"
    audiencia: ["backend-dev", "architect"]
    prerequisitos: ["modulo-fundamentos-07"]
    livros: ["formacao-completa", "backend-architecture"]
    status: "published"
    bqs_score: 92.8
    updated_at: "2026-06-01"
```

---

## Layer 4 — Products

**Estado atual:** 4 livros em 4 formatos, conteudo complementar (slides, videos, exercicios, quiz, projetos, workshops, social, newsletters, LMS-ready). A camada mais proxima do ideal.

**Gaps enderecados:** GAP 3 (quality), GAP 7 (i18n)

### Melhorias-alvo

```
knowledge-factory/products/
├── books/{id}/
│   ├── compiled/book.md           ← OK
│   ├── output/                    ← OK (docx, epub, pdf_digital, pdf_print)
│   ├── i18n/                      ← NOVO
│   │   ├── en-US/compiled/book.md
│   │   └── en-US/output/
│   └── qa/                        ← NOVO (relatorios BQS archivados)
│       ├── bqs-{id}.yaml
│       └── gatekeeper-decision.md
├── courses/{curso}/{modulo}/
│   ├── slides/                    ← OK
│   ├── videos/                    ← OK
│   ├── exercicios/                ← OK
│   ├── quiz/                      ← OK
│   ├── projeto/                   ← OK
│   └── workshop/                  ← OK
└── metrics/                       ← NOVO
    ├── modules.csv                ← BQS historico por modulo
    ├── books.csv                  ← BQS historico por livro
    └── trends.json                ← tendencias de qualidade
```

---

## Layer 5 — Distribution & Experience

**Estado atual:** Inexistente. Zero plataforma de consumo.

**Gaps enderecados:** GAP 5 (branding), GAP 6 (platform), GAP 8 (metrics)

Esta camada e a maior adicao arquitetural. Requer decisoes de produto antes de implementacao.

### Opcoes Arquiteturais

| Opcao | Descricao | Esforco | Ideal para |
|---|---|---|---|
| **Static Site** (Next.js/Vite) | Site institucional + showcase de livros + blog | Medio | Fase 1 de distribuicao |
| **Web App** (Next.js + DB) | Plataforma completa: progresso, certificados, comunidade | Alto | Fase 2 |
| **Headless CMS** (Strapi/Contentful) | API de conteudo + frontend separado | Alto | Se houver multiplos canais de consumo |
| **White-label API** | API que empresas consomem para seus LMS | Medio | Modelo B2B |

### Recomendacao (Fase 6)

Comecar com **Static Site + API leve**:

```
/
├── web/                             ← NOVO (Next.js ou Vite)
│   ├── public/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   └── lib/api.ts              ← consome catalog.yaml + modulos
├── api/                             ← NOVO (se necessario)
│   ├── modules.ts                   ← endpoints de conteudo
│   ├── search.ts                    ← search endpoint
│   └── certificates.ts             ← verificacao de certificados
└── branding/                        ← NOVO
    ├── brand-book.md                ← expandir (missao, visao, tom de voz)
    ├── style-guide-web.md           ← guia de estilo para web
    └── social-calendar.yaml         ← calendario editorial de redes sociais
```

### Funcionalidades Minimas (Static Site V1)

1. Pagina inicial com showcase dos 4 livros + 6 cursos
2. Pagina de cada livro com preview, download, metadata
3. Blog com artigos extraidos dos modulos
4. Search estatico (fuse.js sobre catalog.yaml)
5. Formulario de lead capture (newsletter)
6. Seção "Sobre" com missao, visao, manifesto da editora

---

## Cross-Cutting Concerns

### Observabilidade (GAP 8)

```
knowledge-factory/pipeline/
├── runs/                          ← logs de execucao (ja existe)
├── reports/                       ← relatorios (ja existe)
├── gates/                         ← decisoes de gatekeeper (ja existe)
└── dashboards/                    ← NOVO
    ├── quality-over-time.html     ← BQS trending
    └── catalog-coverage.html      ← % de catalog populado
```

### Versionamento

Tudo em git. Cada modulo e um diretorio versionado. Tags semânticas para releases de livros.

```
git tag v1.0.0-formacao-completa  # release do livro
git tag v1.1.0-atualiza-modulo-08 # atualizacao de modulo
```

---

## Mapeamento Gaps → Camadas

| Gap | Camada(s) | Solucao |
|---|---|---|
| GAP 1 — Catalogacao | Layer 3 | catalog_populator.py + catalog.yaml populado |
| GAP 2 — Pipeline/CI | Layer 2 | .github/workflows/ + pytest + lint |
| GAP 3 — Qualidade/BQS | Layer 2 + 4 | bqs_compute.py + rotina CI |
| GAP 4 — Agentes | Layer 2 | agents_sync.py + registro dos 22 faltantes |
| GAP 5 — Branding | Layer 5 (nova) | Site institucional + brand book expandido |
| GAP 6 — Plataforma | Layer 5 (nova) | Static site + API + progresso |
| GAP 7 — Multi-idioma | Layer 1 + 4 | i18n/ diretorios + i18n_pipeline.py |
| GAP 8 — Metricas | Cross-cutting | BQS trending + dashboards + analytics |
| GAP 9 — Testes | Layer 2 | pytest + ruff + mypy + CI |
| GAP 10 — Governanca | Layer 2 + 3 | Initial screening + double-anonymous + METADATA.yaml |

---

## Roadmap de Implementacao (proximas fases)

```
Fase 5: Execution Plan (detalhamento das sprints)
Fase 6: Bootstrap inicial
    Sprint 1: catalog_populator.py + catalog.yaml populado (GAP 1)
    Sprint 2: ci.yml + bqs_compute.py (GAP 2 + 3)
    Sprint 3: agents_sync.py + registro dos 22 agentes (GAP 4)
    Sprint 4: Static site V1 (GAP 5 + 6 minimal)
    Sprint 5: i18n pipeline + METADATA.yaml (GAP 7 + 10)
```
