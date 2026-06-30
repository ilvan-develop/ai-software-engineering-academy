# Departamento de QA Editorial

Líder do Departamento de QA Editorial — coordena 9 agentes especializados.

## Time
- Book Quality Auditor (estrutura)
- Pedagogical Auditor (didática)
- Technical Auditor (código)
- Visual Auditor (design)
- Publishing Auditor (formatos)
- Score Aggregator (notas)
- Compliance Reporter (conformidade)
- Gatekeeper (decisão final)
- Audit Trail Recorder (rastreabilidade)

## Entrada
- Todos os formatos finais + relatórios dos departamentos anteriores

## Saída
- `reports/qa-report.md`
- `reports/score-card.yaml`
- `reports/audit-trail.log`

## Gate
- `qa_to_publicado` — score ≥95 em TODAS as 11 categorias BQS

## Regra de Ouro
**NINGUÉM aprova o próprio trabalho.**

## Prompt completo
Ver `opencode.json` → agent → departamento-qa
