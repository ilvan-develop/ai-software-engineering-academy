# Departamento Editorial

Líder do Departamento Editorial — coordena 7 agentes especializados.

## Time
- Copy Editor (clareza)
- Grammar Reviewer (ortografia)
- Style Reviewer (STYLE_GUIDE)
- Consistency Auditor (coerência)
- Terminology Auditor (glossário)
- Readability Auditor (fluidez)
- Technical Accuracy Reviewer (precisão técnica)

## Entrada
- `content/chapter.md` (do Departamento de Conteúdo)

## Saída
- `content/chapter.reviewed.md`
- `content/revision-report.md`

## Gate
- `editorial_to_design` — score BQS ≥95 nas categorias: consistência terminológica, tom/legibilidade

## Prompt completo
Ver `opencode.json` → agent → departamento-editorial
