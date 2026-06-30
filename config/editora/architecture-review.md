# Architecture Review — Knowledge Factory

## Current State

### Structural Problems

| # | Problema | Severidade | Impacto em 200k itens |
|---|----------|-----------|----------------------|
| 1 | 6 pastas de curso duplicadas na raiz de `knowledge-factory/` (`arquitetura-backend/`, `product-design/`, etc.) são IDs de curso soltos no root | 🔴 Critico | Multiplicaria para dezenas de pastas soltas |
| 2 | `curriculum/cursos/` (source) vs `knowledge-factory/cursos/` (output) compartilham mesmo nome "cursos" | 🔴 Critico | Confusao entre source e output escala linearmente |
| 3 | Pipeline reports soltos na raiz (`pipeline-relatorio-*.md`) | 🟡 Moderado | Com 200k itens, centenas de reports poluiriam o root |
| 4 | `auditoria/` vazio — placeholder sem proposito | 🟢 Leve | Ponto cego: sem auditoria, sem governanca |
| 5 | 38 `.gitkeep` files (parte dos 111 "no ext") | 🟢 Leve | Ruido no versionamento |

### Architectural Problems

| # | Problema | Severidade | Impacto em 200k itens |
|---|----------|-----------|----------------------|
| 6 | Hierarquia unidimensional: `course > module > type` | 🔴 Critico | Impossivel navegar por topico, formato, audiencia |
| 7 | Sem catalog/registry — nenhum metadata sobre o que existe | 🔴 Critico | Sem catalog, 200k itens = caos total |
| 8 | Sem content graph — relações entre itens nao existem | 🟡 Moderado | Nao da para rastrear "quais livros usam este modulo" |
| 9 | Sem versionamento — quando um modulo muda, outputs ficam obsoletos sem aviso | 🟡 Moderado | 200k itens sem versao = confianca zero |
| 10 | Sem taxonomia — tags, nivel de dificuldade, audiencia, prereqs | 🟡 Moderado | Impossivel filtrar ou recomendar |
| 11 | `batch_remaining.py` escreve em `KF_DIR / course_name` (root) em vez de `KF_DIR / "cursos" / course_name` | 🔴 Critico | Causa raiz do problema #1 |

### Root Cause

`scripts/batch_remaining.py:58`:
```python
output_dir = KF_DIR / course_name / mod_id / "projeto"  # BUG
# Deveria ser:
output_dir = KF_DIR / "cursos" / course_name / mod_id / "projeto"
```

Isso fez com que `process_projects()` criasse `knowledge-factory/arquitetura-backend/`, `knowledge-factory/product-design/`, etc. — 6 pastas de curso no root, DUPLICANDO o que ja existe em `knowledge-factory/cursos/`.

---

## Proposed Architecture

### Principle: Content Supply Chain

```
SOURCES → REGISTRY → PIPELINES → PRODUCTS
                            ↓
                       ASSETS (shared)
                            ↓
                       INDEX (search)
```

### Directory Structure (target)

```
knowledge-factory/
├── MANIFEST.yaml                        # Metadado raiz: versão, schema, último build
│
├── registry/                            ← NOVO: metadata backbone
│   ├── catalog.yaml                     # TODO item registrado com id, tipo, fonte, versão
│   ├── taxonomy.yaml                    # Tags, categorias, niveis, audiencias
│   └── graph.yaml                       # Relações entre itens (modulo → livro, modulo → modulo)
│
├── sources/                             ← REFORMULADO: apenas referências imutáveis
│   └── modules/                         # Espelha curriculum/cursos/ (link simbolico ou copia)
│
├── pipeline/                            ← NOVO: orquestração e auditoria
│   ├── runs/                            # Logs de execução (data, modulo, engine, resultado)
│   ├── reports/                         # Pipeline reports (movido do root)
│   └── gates/                           # Quality gates (BQS) por produto
│
├── products/                            ← REFORMULADO: todo output por FORMATO
│   ├── books/{book-id}/                 # Livros (compiled/ + output/ + kdp/)
│   ├── courses/{course}/{module}/       # Conteudo por modulo (slides, videos, exercicios, quiz, projeto, workshop)
│   ├── social/{campaign}/               # Redes sociais (LinkedIn, Twitter, Instagram)
│   ├── newsletters/{issue-id}/          # Newsletters por edicao
│   ├── certificates/{cert-id}/          # Certificacoes
│   ├── online-courses/{course-id}/      # LMS-ready (Udemy, Hotmart)
│   └── presentations/                   # Apresentacoes cross-cutting
│
├── assets/                              ← NOVO COMPARTILHADO: deduplicado
│   ├── diagrams/                        # SVGs, diagrams
│   ├── covers/                          # Capas de livros
│   ├── templates/                       # Templates DOCX, EPUB, LaTeX
│   └── fonts/                           # Fontes customizadas
│
└── index/                               ← FUTURO: camada de busca
    ├── catalog.json                     # Catalogo pesquisável
    └── graph.json                       # Grafo de conhecimento
```

### Catalog Registry Schema

```yaml
# registry/catalog.yaml
items:
  - id: "mod-08-arquitetura"
    type: module
    title: "Fundamentos de Arquitetura"
    source: "curriculum/cursos/arquitetura-backend/module-08-arquitetura/aula/aula.md"
    version: 1
    taxonomy:
      topics: ["arquitetura", "clean-architecture", "ddd"]
      level: intermediate
      audience: ["devs", "architects"]
    relationships:
      used_in: ["book-backend-architecture", "book-formacao-completa"]
      prerequisites: []
    outputs:
      slides: "products/courses/arquitetura-backend/module-08-arquitetura/slides/"
      video: "products/courses/arquitetura-backend/module-08-arquitetura/videos/"
      exercicios: "products/courses/arquitetura-backend/module-08-arquitetura/exercicios/"
      quiz: "products/courses/arquitetura-backend/module-08-arquitetura/quiz/"
      projeto: "products/courses/arquitetura-backend/module-08-arquitetura/projeto/"
```

### Taxonomy Schema

```yaml
# registry/taxonomy.yaml
topics:
  - id: arquitetura
    label: "Arquitetura de Software"
    subtopics: [clean-architecture, hexagonal, microservices, event-driven]
  - id: product-design
    label: "Product Design"
    subtopics: [discovery, ux, ui, design-system]

levels:
  - id: beginner
    label: "Iniciante"
  - id: intermediate
    label: "Intermediario"
  - id: advanced
    label: "Avancado"

audiences:
  - id: devs
    label: "Desenvolvedores"
  - id: architects
    label: "Arquitetos"
  - id: designers
    label: "Designers"
  - id: managers
    label: "Gestores"
```

---

## Migration Plan

### Phase 1 — Fix the Bug (immediate)

1. Corrigir `batch_remaining.py:58`: `KF_DIR / course_name` → `KF_DIR / "cursos" / course_name`
2. Mover arquivos das 6 pastas duplicadas para dentro de `cursos/`

### Phase 2 — Clean up (today)

3. Mover `pipeline-relatorio-*.md` para `pipeline/reports/`
4. Remover `auditoria/` (vazio)
5. Criar `registry/` com catalog.yaml vazio + taxonomy.yaml
6. Criar `assets/` shared structure

### Phase 3 — Refactor (this week)

7. Renomeie `knowledge-factory/cursos/` → `knowledge-factory/products/courses/`
8. Renomeie `curriculum/cursos/` → `curriculum/sources/`
9. Atualizar todos os scripts que referenciam os paths antigos
10. Atualizar `AGENTS.md` com a nova estrutura

### Phase 4 — Scale (next weeks)

11. Implementar `registry/catalog.yaml` populado programaticamente
12. Implementar `registry/graph.yaml` via analise de manifests
13. Adicionar versionamento de conteudo no catalog
14. Criar `products/catalog-index.py` para gerar index/search layer

### Scripts that need path updates

| Script | Old Path | New Path |
|--------|----------|----------|
| `batch_remaining.py:58` | `KF_DIR / course_name / mod_id / "projeto"` | `KF_DIR / "cursos" / course_name / mod_id / "projeto"` |
| `batch_social.py` | `KF_DIR / "social-media"` | `KF_DIR / "products" / "social"` |
| `batch_newsletter.py` | `KF_DIR / "newsletter"` | `KF_DIR / "products" / "newsletters"` |
| `build_book_components.py` | `KF_DIR / "livros"` | `KF_DIR / "products" / "books"` _(manter backward compat)_ |
| `book_architect.py` | `KF_DIR / "livros"` | `KF_DIR / "products" / "books"` |
| `book_publisher.py` | `KF_DIR / "livros"` | `KF_DIR / "products" / "books"` |
| `pipeline_manager.py` | references | to update |

---

## Why this scales to 200k

| Requirement | Current | Proposed |
|-------------|---------|----------|
| Find content by topic | ❌ | ✅ taxonomy.yaml |
| Find content by format | ❌ | ✅ products/{format}/ |
| Trace content usage | ❌ | ✅ graph.yaml + catalog |
| Version content | ❌ | ✅ catalog.version |
| Search across all | ❌ | ✅ index/ layer |
| Deduplicate assets | ❌ | ✅ assets/ shared |
| Audit pipeline runs | ❌ | ✅ pipeline/runs/ |
| Scale horizontally | ❌ | ✅ products/ by format |
