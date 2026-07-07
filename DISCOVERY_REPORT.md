# DISCOVERY REPORT — Fase 1

**Orquestrador:** Chief Orchestrator
**Data:** 2026-07-07
**Versao:** 1.0

---

## 1. Mapa de Diretorios

```
/
├── AGENTS.md                          # Instrucoes do workspace OpenCode
├── opencode.json                      # 78KB — orquestrador principal com agentes
├── STYLE_GUIDE.md                     # Guia de estilo editorial (168 linhas)
├── ARCHITECTURE_AUDIT.md              # Auditoria previa (nao faz parte do projeto original)
├── BOOTSTRAP_PROMPT.md                # Prompt de bootstrap (criado nesta sessao)
├── requirements.txt                   # Dependencias Python
│
├── curriculum/                        # FONTE: conhecimento canonico
│   ├── sources/                       # 6 cursos, 26 modulos
│   │   ├── fundamentos-enterprise/    # 3 modulos (00, 01, bonus)
│   │   ├── product-design/            # 6 modulos (02-07)
│   │   ├── arquitetura-backend/       # 8 modulos (08-13d)
│   │   ├── frontend-devops/           # 4 modulos (11, 14-16)
│   │   ├── governanca-automacao/     # 4 modulos (17-20)
│   │   └── capstone/                  # 1 modulo (21)
│   ├── books/                         # 4 manifests + 1 template
│   ├── bqs/                           # 7 arquivos de qualidade
│   ├── biblioteca-agentes/            # 15 agentes (cada um com README.md)
│   ├── metodologia/                   # README.md com o ciclo de 10 passos
│   ├── knowledge-factory/             # README.md (copia do conceito)
│   ├── README.md                      # Visao geral do curriculo (190 linhas)
│   └── status.yaml                    # Estado de cada modulo e livro (470 linhas)
│
├── config/
│   └── editora/                       # Governanca da editora
│       ├── departamentos.yaml         # 5 deptos, 42 agentes (405 linhas)
│       ├── pipeline-gate.yaml         # 5 gates, regras de transicao (187 linhas)
│       ├── design-tokens.yaml         # Tokens globais v1.0.0 (253 linhas)
│       ├── brand-book.md              # Manual de identidade visual (185 linhas)
│       ├── layout-grid.yaml           # Grid modular multi-formato (220 linhas)
│       ├── icons.yaml                 # Mapa de icones
│       ├── component-library.yaml     # Componentes reutilizaveis
│       ├── architecture-review.md     # Revisao arquitetural previa
│       └── teams/                     # 5 diretorios com prompts individuais
│           ├── 01-conteudo/           # 10 prompts
│           ├── 02-editorial/          # 7 prompts
│           ├── 03-design/             # 19 prompts
│           ├── 04-publicacao/         # 7 prompts
│           └── 05-qa/                 # 9 prompts
│   └── templates/                     # Templates de conteudo
│       ├── lesson-template.md
│       ├── linkedin-post-template.md
│       ├── workshop-4h.md / 8h.md
│       └── prompts/                   # 16 prompts de template para agentes
│
├── schemas/
│   ├── book-manifest.schema.json      # Schema de validacao de manifests
│   └── catalog.schema.json            # Schema do catalogo
│
├── scripts/                           # ~30 scripts Python
│   ├── pipeline_manager.py            # Orquestrador central
│   ├── pipeline_audit.py              # Auditoria de pipeline
│   ├── consistency_auditor.py         # Auditoria de consistencia
│   ├── book_architect.py              # Agregador de modulos em livros (299 linhas)
│   ├── book_publisher.py              # Conversor de formatos
│   ├── build_docx.py / build_epub.py / build_pdf_digital.py / build_pdf_print.py / build_pdf_typst.py
│   ├── md_to_components.py            # Parseia MD em arvore de componentes
│   ├── diagram_factory.py             # Fabrica de diagramas (11 engines)
│   ├── deploy_kdp.py                  # Prepara artefatos para KDP
│   ├── batch_*.py (9 scripts)         # Processamento batch (content, slides, videos, social, etc)
│   ├── auto_fix_code_languages.py     # Corrige linguagens em code fences
│   ├── config.py / cache.py           # Utilitarios
│   ├── renderers/                     # Renderizadores: fpdf2_components, svg_to_fpdf
│   ├── factories/                     # Engines de conteudo (exercise, quiz, project, slide, video, etc)
│   ├── diagrams/                      # 11 engines de diagrama
│   └── utils/                         # Utilitarios (template_engine, cover_builder)
│
├── knowledge-factory/                 # OUTPUT: conteudo gerado
│   ├── products/
│   │   ├── books/                     # 4 livros
│   │   │   ├── formacao-completa/     # 26 capitulos, 529KB book.md
│   │   │   ├── backend-architecture/  # 8 capitulos, 127KB book.md
│   │   │   ├── product-design-book/   # 6 capitulos
│   │   │   └── ia-para-devs/          # 3 capitulos
│   │   ├── courses/                   # Conteudo por curso/modulo
│   │   ├── social/                    # Posts para redes sociais
│   │   ├── newsletters/               # Newsletters
│   │   ├── online-courses/            # Conteudo LMS-ready
│   │   └── certificates/              # Certificados
│   ├── registry/
│   │   ├── catalog.yaml               # VAZIO (items: [])
│   │   └── taxonomy.yaml              # 6 topicos, 3 niveis, 5 audiencias
│   ├── pipeline/
│   │   ├── reports/                   # Relatorios de pipeline
│   │   └── runs/                      # Logs de execucao
│   └── assets/                        # VAZIO (.gitkeep)
│
├── archive/                           # Conteudo legado (pre-estrutura atual)
│   └── legacy-content/
│       ├── raw/                       # Conteudo bruto original
│       ├── modules/                   # Modulos antigos
│       ├── exercises/ / quizzes/ / slides/
│       └── marketing/                 # Material de marketing antigo
│
└── tests/                             # Testes (conteudo a verificar)
```

---

## 2. Tabela de Agentes (42 + orquestradores)

### Departamento de Conteudo (10 agentes)

| Agente | Input | Output | Gate |
|---|---|---|---|
| chief-editor | book-manifest + raw-content | content-structure.yaml | estrutura_conteudo ≥95 |
| curriculum-architect | content-structure.yaml | curriculum-plan.md | progressao_pedagogica ≥95 |
| subject-matter-expert | chapter-draft.md | sme-validation-report.md | qualidade_tecnica ≥95 |
| technical-writer | raw-content + curriculum-plan.md | chapter-draft.md | tom_legibilidade + estrutura ≥95 |
| educational-designer | chapter-draft.md | educational-review.md | progressao_pedagogica ≥95 |
| research-agent | content-topics.md | research-sources.md | qualidade_tecnica (refs) ≥95 |
| fact-checker | chapter-draft.md + research-sources.md | fact-check-report.md | qualidade_tecnica ≥95 |
| example-creator | chapter-draft.md | examples-section.md | qualidade_exemplos ≥95 |
| exercise-creator | chapter-draft.md + examples-section.md | exercises.md | exercicios_avaliacoes ≥95 |
| quiz-creator | chapter-draft.md | quiz.md | exercicios_avaliacoes ≥95 |

### Departamento Editorial (7 agentes)

| Agente | Input | Output | Gate |
|---|---|---|---|
| copy-editor | chapter.md | copy-edit-report.md | tom_legibilidade ≥95 |
| grammar-reviewer | chapter.md | grammar-review-report.md | tom_legibilidade ≥95 |
| style-reviewer | chapter.md + STYLE_GUIDE.md | style-review-report.md | tom_legibilidade + STYLE 100% |
| consistency-auditor | chapter.md + previous-chapters.md | consistency-report.md | consistencia_terminologica ≥95 |
| terminology-auditor | chapter.md + glossary.md | terminology-report.md | consistencia_terminologica ≥95 |
| readability-auditor | chapter.md | readability-report.md | tom_legibilidade ≥95 |
| technical-accuracy-reviewer | chapter.md | technical-accuracy-report.md | qualidade_tecnica ≥95 |

### Departamento de Design (19 agentes)

| Agente | Input | Output |
|---|---|---|
| book-designer | chapter.reviewed.md | layout-book.yaml |
| layout-designer | chapter.reviewed.md + layout-book.yaml | formatted-content.md |
| typography-specialist | layout-book.yaml | typography-spec.md |
| color-specialist | layout-book.yaml | color-palette.md |
| diagram-designer | chapter.reviewed.md | diagrams-spec.md + diagrams-prompt.txt |
| illustration-planner | chapter.reviewed.md | illustration-plan.md |
| table-designer | chapter.reviewed.md | tables-formatted.md |
| callout-designer | chapter.reviewed.md | callouts-spec.md |
| cover-designer | book-metadata.yaml + layout-book.yaml | cover-spec.md + cover-prompt.txt |
| brand-book-designer | layout-book.yaml + design-tokens.yaml | brand-book.md |
| information-designer | chapter.reviewed.md + design-tokens.yaml | information-design-spec.md |
| epub-css-architect | design-tokens.yaml + layout-grid.yaml | epub-stylesheet.css |
| print-production-specialist | layout-book.yaml + brand-book.md | print-spec.md |
| accessible-design-specialist | book.md + design-tokens.yaml | accessibility-design-report.md |
| visual-hierarchy-auditor | book.md + layout-book.yaml | visual-hierarchy-report.md |
| design-token-manager | brand-book.md + layout-book.yaml | design-tokens.yaml |
| template-developer | design-tokens.yaml + layout-grid.yaml | templates (docx/odt/tex) |
| cover-illustration-director | book-metadata.yaml + brand-book.md | cover-brief.md |
| layout-system-architect | brand-book.md + design-tokens.yaml | layout-grid.yaml |

### Departamento de Publicacao (7 agentes)

| Agente | Input | Output |
|---|---|---|
| markdown-auditor | chapter.md + assets/ | markdown-validation-report.md |
| docx-generator | chapter.md + layout-book.yaml | livro.docx |
| pdf-generator | chapter.md + layout-book.yaml | livro-digital.pdf + livro-grafica.pdf |
| epub-generator | chapter.md | livro.epub |
| template-manager | layout-book.yaml + book.md | templates-applied/ |
| brand-consistency-agent | livro.docx + livro.pdf + layout-book.yaml | brand-consistency-report.md |
| accessibility-auditor | livro.docx + livro.pdf + livro.epub | accessibility-report.md |

### Departamento de QA (9 agentes)

| Agente | Input | Output |
|---|---|---|
| book-quality-auditor | book.md + reports/ | book-quality-report.md |
| pedagogical-auditor | book.md | pedagogical-audit-report.md |
| technical-auditor | book.md | technical-audit-report.md |
| visual-auditor | book.md + layout-book.yaml | visual-audit-report.md |
| publishing-auditor | livro.docx + livro.pdf + livro.epub | publishing-audit-report.md |
| score-aggregator | qa-reports/* | score-card-{id}.yaml |
| compliance-reporter | score-card.yaml + audit-trail.log | compliance-report.md |
| gatekeeper | score-card.yaml + qa-reports/* | gatekeeper-decision.md |
| audit-trail-recorder | pipeline-execution-log/ | audit-trail-{id}.log |

### Agentes no opencode.json (subagent mode)

| Agente | Modo | Permissoes |
|---|---|---|
| curriculum-architect | subagent | write, read, glob, grep (no edit, no bash) |
| technical-writer | subagent | write, read, glob, grep |
| reviewer | subagent | read, glob, grep (no write) |
| linkedin-creator | subagent | write, read, glob, grep |
| slide-creator | subagent | write, read, glob, grep |
| exercise-creator | subagent | write, read, glob, grep |
| quiz-creator | subagent | write, read, glob, grep |
| book-architect | subagent | edit, write, read, bash, glob, grep |
| book-publisher | subagent | edit, write, read, bash, glob, grep |
| designer-visual | subagent | write, read, glob, grep |
| curador-conteudo | subagent | write, read, glob, grep |
| revisor-linguagem | subagent | write, read, glob, grep |
| design-system-editorial | subagent | write, read, glob, grep |
| criador-imagens | subagent | write, read, glob, grep |
| tradutor-conteudo | subagent | write, read, glob, grep |
| indexador-seo | subagent | write, read, glob, grep |
| gestor-pipeline | subagent | edit, write, read, bash, glob, grep |
| departamento-conteudo | subagent | edit, write, read, bash, glob, grep |
| departamento-editorial | subagent | write, read, glob, grep |
| brand-book-designer | subagent | write, read, glob, grep |
| information-designer | subagent | write, read, glob, grep |
| ... (mais design agents) | subagent | write, read, glob, grep |

### Orquestradores no opencode.json (build/plan mode)

| Agente | Modo | Skills | 
|---|---|---|
| build | task | enterprise-*, context7-mcp |
| plan | task | enterprise-*, context7-mcp |

---

## 3. Estado dos Modulos (de status.yaml)

| Curso | Modulos | Status | Outputs |
|---|---|---|---|
| fundamentos-enterprise | 3 | todos `publicado` | aula, slides, video, exercicios, quiz, projeto, workshop |
| product-design | 6 | todos `publicado` | aula, slides, video, exercicios, quiz, projeto, workshop |
| arquitetura-backend | 8 | todos `publicado` | aula, slides, video, exercicios, quiz, projeto, workshop |
| frontend-devops | 4 | todos `publicado` | aula, slides, video, exercicios, quiz, projeto, workshop |
| governanca-automacao | 4 | todos `publicado` | aula, slides, video, exercicios, quiz, projeto, workshop |
| capstone | 1 | todos `publicado` | aula, slides, video, exercicios, quiz, projeto, workshop |
| **Total** | **26 modulos** | **100% publicado** | **7 tipos de output por modulo** |

### Observacao critica
Todos os 26 modulos estao marcados como `publicado`. Todos os outputs (aula, slides, video, exercicios, quiz, projeto, workshop) estao como `gerado` ou `publicado`. Em qualquer sistema editorial real, 20-30% dos itens estariam em revisao ou atualizacao. Isso sugere que o status pode ser aspiracional (marcado como concluido sem verificacao real) ou que nao houve ciclo de revisao desde a publicacao inicial.

---

## 4. Estado dos Livros (de status.yaml)

| Livro | Capitulos | Formatos | Status |
|---|---|---|---|
| formacao-completa | 26 | docx, epub, pdf_digital, pdf_print | todos `publicado` |
| backend-architecture | 8 | docx, epub, pdf_digital, pdf_print | todos `publicado` |
| product-design-book | 6 | docx, epub, pdf_digital, pdf_print | todos `publicado` |
| ia-para-devs | 3 | docx, epub, pdf_digital, pdf_print | todos `publicado` |

---

## 5. Mapa de Scripts

| Script | Funcao | Depende de |
|---|---|---|
| pipeline_manager.py | Orquestrador central | status.yaml, todos os batch_* |
| pipeline_audit.py | Auditoria de pipeline | status.yaml |
| consistency_auditor.py | Auditoria de consistencia | modules/*.md |
| book_architect.py | Agrega modulos em livros | book manifests + sources |
| book_publisher.py | Converte para formatos finais | compiled/book.md |
| build_docx.py | Gera DOCX | python-docx |
| build_epub.py | Gera EPUB | — |
| build_pdf_digital.py | Gera PDF digital | fpdf2 |
| build_pdf_print.py | Gera PDF grafica | Pandoc/LaTeX |
| build_pdf_typst.py | Gera PDF via Typst | Typst |
| md_to_components.py | Parseia MD em componentes | — |
| diagram_factory.py | Fabrica de diagramas | 11 engines em diagrams/ |
| deploy_kdp.py | Prepara para KDP | — |
| batch_content.py | Gera conteudo batch | Todos os modulos |
| batch_diagrams.py | Gera diagramas | diagram_factory.py |
| batch_slides.py | Gera slides | — |
| batch_videos.py | Gera roteiros | — |
| batch_social.py | Gera redes sociais | — |
| batch_newsletter.py | Gera newsletters | — |
| batch_lms.py | Formata para LMS | — |
| batch_workshops.py | Gera workshops | — |
| batch_projects.py | Gera projetos | — |
| batch_remaining.py | Processa pendentes | — |
| auto_fix_code_languages.py | Corrige code fences | — |
| cache.py | Cache de build | — |
| config.py | Configuracoes | — |

---

## 6. Pipeline Atual (Fluxo)

```
Book Manifest (YAML)
    ↓
book_architect.py → compiled/book.md + capitulos individuais
    ↓
book_publisher.py
    ├── build_docx.py → livro.docx
    ├── build_epub.py → livro.epub
    ├── build_pdf_digital.py → livro-digital.pdf
    └── build_pdf_print.py → livro-grafica.pdf
    ↓
batch_*.py (paralelo opcional)
    ├── batch_content.py → exercicios, quizzes
    ├── batch_diagrams.py → diagramas SVG
    ├── batch_slides.py → slides
    ├── batch_videos.py → roteiros de video
    ├── batch_social.py → posts redes sociais
    ├── batch_newsletter.py → newsletters
    ├── batch_lms.py → formato Udemy/Hotmart
    └── batch_workshops.py → workshops
    ↓
pipeline_audit.py → relatorio de auditoria
consistency_auditor.py → consistencia entre modulos
```

### Problemas identificados no fluxo atual:
1. **Pipeline manual** — nada e automatico. Cada execucao requer comando Python.
2. **Sem CI/CD** — nao ha GitHub Actions, triggers, ou automacao.
3. **Sem preview** — nao ha ambiente de staging. Conteudo vai direto para producao.
4. **Sem verificacao de qualidade automatica** — BQS e aspiracional, nao computado.
5. **Sem verificacao de links, codigo, ou acessibilidade** no pipeline.
6. **Sem rollback** — se algo quebra, nao ha mecanismo de voltar versao anterior.

---

## 7. Estado do Catalogo e Taxonomia

| Recurso | Estado | Observacao |
|---|---|---|
| catalog.yaml | VAZIO | Schema definido mas `items: []` |
| taxonomy.yaml | PREENCHIDO | 6 topicos, 3 niveis, 5 audiencias |
| graph.yaml | NAO EXISTE | Mencionado no AGENTS.md mas nao criado |
| book-manifest.schema.json | OK | Schema valido |
| catalog.schema.json | OK | Schema valido |

---

## 8. Problemas Evidentes (pre-analise, sem implementacao)

### Blocker
1. **catalog.yaml vazio** — sem catalogacao de conteudo, impossivel ter busca, recomendacao, ou navegacao structurada
2. **100% publicado** — todos os modulos marcados como concluidos, sem evidencia de qualidade real
3. **BQS nunca computado de fato** — MIGRATION.md mostra que foi rodado uma vez para ia-para-devs (score 92.8), mas nao ha rotina regular
4. **Sem separacao aluno/admin** — nao ha login, nao ha progresso, nao ha permissao

### Critical
5. **Agentes no opencode.json nao espelham departamentos.yaml** — departamentos.yaml tem 42 agentes, opencode.json tem ~20 subagentes. Ha agentes definidos no YAML que nunca foram registrados no OpenCode.
6. **Nao ha agentes de infraestrutura, branding, ou comunidade** — fora do escopo atual
7. **Scripts sao monoliticos** — pipeline_manager.py com 321 linhas, sem testes automatizados
8. **Sem verificacao de erros** — exemplos de codigo nos modulos nunca sao compilados ou testados

### High
9. **Taxonomia nao vinculada ao conteudo** — taxonomy.yaml tem topicos mas catalog.yaml esta vazio
10. **Assets compartilhados vazios** — `knowledge-factory/assets/` tem apenas .gitkeep
11. **Sem metricas de sucesso** — nao ha como medir se o conteudo e eficaz, lido, ou valorizado
12. **Multi-idioma ausente** — tradutor agente existe mas nao ha pipeline de internacionalizacao

---

## 9. Estatisticas Gerais

| Metrica | Valor |
|---|---|
| Departamentos | 5 |
| Agentes definidos (YAML) | 42 |
| Agentes registrados (opencode.json) | ~20 |
| Scripts Python | ~30 |
| Cursos | 6 |
| Modulos | 26 |
| Livros | 4 |
| Capitulos de livro (total) | 43 |
| Modulos "publicado" | 26 (100%) |
| Formatos de output | 7 por modulo |
| Taxonomia: topicos | 6 |
| Taxonomia: niveis | 3 |
| Taxonomia: audiencias | 5 |
| Catalogo populado | 0% |
| CI/CD | Nao existe |
| Testes automatizados | Nao |
| BQS computado | 1 vez (ia-para-devs, score 92.8) |

---

## 10. Proximos Passos (Fase 2)

Concluir Fase 2 — Research & Benchmark, pesquisando:
1. Editoras tecnicas (O'Reilly, Manning): pipelines editoriais, peer review, qualidade
2. Plataformas LMS (Udemy, Coursera): progresso, certificacao, comunidade
3. Knowledge Management (RAG, GraphRAG, search)
4. Multi-agent systems (LangChain, CrewAI, Anthropic)
5. Ferramentas de publicacao (Pandoc, Quarto, Typst)
6. Chief Branding Officer: melhores praticas de branding para edtech
