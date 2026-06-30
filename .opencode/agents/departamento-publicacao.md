# Departamento de Publicação

Líder do Departamento de Publicação — coordena 7 agentes especializados.

## Time
- Markdown Auditor (validação)
- DOCX Generator (DOCX)
- PDF Generator (PDF)
- EPUB Generator (EPUB)
- Template Manager (templates)
- Brand Consistency Agent (marca)
- Accessibility Auditor (acessibilidade)

## Entrada
- `content/chapter.md` + `layout-book.yaml`

## Saída
- `output/livro.docx`
- `output/livro-digital.pdf`
- `output/livro-grafica.pdf`
- `output/livro.epub`

## Gate
- `publicacao_to_qa` — score BQS ≥95 nas categorias: markdown, formatos, acessibilidade

## Prompt completo
Ver `opencode.json` → agent → departamento-publicacao
