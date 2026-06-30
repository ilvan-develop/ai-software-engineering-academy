# Book Factory — Orquestrador da Editora Enterprise

Orquestrador completo do pipeline editorial de 5 estágios com gates BQS.

## Departamento
Orquestração (coordena os 5 departamentos)

## Pipeline
```
Conteúdo → Editorial → Design → Publicação → QA → Publicado
```

## Comandos
- `pipeline status` — estado atual de todos os livros
- `pipeline run <book-id>` — pipeline completo
- `pipeline stage <book-id> <stage>` — estágio específico
- `pipeline gate <book-id> <gate-id>` — verificar gate
- `pipeline score <book-id>` — calcular BQS score
- `pipeline audit <book-id>` — verificar audit trail

## Regras
- Ordem obrigatória: Conteúdo → Editorial → Design → Publicação → QA
- Cada gate exige score ≥95 em TODAS as categorias relevantes
- Ninguém aprova o próprio trabalho
- Audit trail imutável para cada execução

## Prompt completo
Ver `opencode.json` → agent → book-factory
