# scripts/

Pipeline de publicacao da Knowledge Factory. Processa modulos em `curriculum/sources/` e gera output em `knowledge-factory/products/{format}/`.

## Pipeline principal

| Comando | Descricao |
|---------|-----------|
| `pipeline_manager.py` | Orquestrador — executa pipelines completos (conteudo, diagramas, livros, redes sociais) |
| `pipeline_audit.py` | Auditoria — verifica status, detecta discrepancias entre modules e outputs |
| `consistency_auditor.py` | Auditoria de consistencia entre modulos, links, tom de voz e referencias |

## Processamento de modulos

| Comando | Descricao |
|---------|-----------|
| `batch_content.py` | Gera conteudo (exercicios, quizzes, projetos, slides, videos, LMS) para todos os modulos |
| `batch_diagrams.py` | Gera diagramas SVG para todos os modulos via `diagram_factory.py` |
| `batch_social.py` | Gera conteudo para redes sociais (LinkedIn, Twitter/X, Instagram, prompts de capa) |
| `batch_newsletter.py` | Gera newsletters a partir dos modulos |
| `batch_videos.py` | Gera roteiros de video |
| `batch_slides.py` | Gera slides |
| `batch_projects.py` | Gera projetos praticos |
| `batch_lms.py` | Formata para plataformas LMS (Udemy, Hotmart) |
| `batch_workshops.py` | Gera material de workshop |
| `batch_remaining.py` | Processa modulos pendentes |

## Geracao de livros

| Comando | Descricao |
|---------|-----------|
| `book_architect.py` | Le o Book Manifest (`curriculum/books/*.yaml`) e agrega modulos em Markdown estruturado |
| `book_publisher.py` | Converte Markword estruturado em DOCX, EPUB e PDF |
| `md_to_components.py` | Parseia Markdown em arvore de componentes (heading, paragraph, figure, code, list) |
| `build_book_components.py` | Constroi componentes de um livro a partir do manifest |
| `build_component_pdf.py` | Gera PDF component-based com fpdf2 + SVG nativo |
| `build_pdf_digital.py` | Gera PDF digital via fpdf2 |
| `build_pdf_print.py` | Gera PDF para impressao (com marcas de corte, sangria) |
| `build_pdf_typst.py` | Gera PDF via Typst (requer Typst instalado) |
| `build_docx.py` | Gera DOCX via python-docx |
| `build_epub.py` | Gera EPUB |
| `deploy_kdp.py` | Prepara artefatos para publicacao no Amazon KDP |

## Renderizadores e engines

| Caminho | Descricao |
|---------|-----------|
| `renderers/fpdf2_components.py` | Renderizador component-based: heading, paragraph, figure (SVG nativo), code, list, table, callout |
| `renderers/svg_to_fpdf.py` | Renderizador SVG nativo para fpdf2 (rect, circle, line, path, text, markers, defs) |
| `diagram_factory.py` | Fabrica de diagramas — 11 engines registrados |
| `diagrams/` | Engines individuais: flowchart, comparison, timeline, mindmap, comparison_matrix, architecture, sequence, er_diagram, c4_model, gantt, bpmn |
| `factories/content/` | Engines de conteudo: exercise, quiz, project, slide, video, social, newsletter, lms, workshop |

## Configuracao

- `curriculum/status.yaml` — estado de cada modulo e livro
- `curriculum/books/*.yaml` — Book Manifests (estrutura de cada livro)
- `opencode.json` — agentes de IA disponiveis

## Uso basico

```bash
# Gerar tudo
python scripts/pipeline_manager.py

# Auditar
python scripts/pipeline_audit.py

# Gerar livro especifico
python scripts/book_publisher.py --manifest=curriculum/books/product-design-book.yaml --formats=component_pipeline

# Processar diagramas
python scripts/batch_diagrams.py

# Publicar redes sociais
python scripts/batch_social.py
```
