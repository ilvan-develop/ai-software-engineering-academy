# Prompt: Analisar Query Lenta

Analise e otimize a query abaixo.

## Query

```sql
[query lenta]
```

## Contexto

- **Tabelas envolvidas:** [nomes e volumes]
- **Índices existentes:** [lista]
- **Frequência de execução:** [100x/dia, etc.]
- **Tempo atual:** [X ms]

## Análise esperada

1. **EXPLAIN ANALYZE** interpretado
2. **Problema identificado** (full scan, N+1, falta de índice)
3. **Solução proposta** (índice novo, reescrita da query, cache)
4. **Tempo estimado após correção**

## Regras

- Preferir índices compostos a múltiplos índices simples
- Evitar subqueries correlated (preferir JOIN ou CTE)
- Usar paginação cursor-based para grandes datasets
- Considerar materialized views para agregações pesadas
