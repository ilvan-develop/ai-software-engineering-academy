# Prompt: Estratégia Multi-Tenant

Projete a estratégia de isolamento multi-tenant para o sistema abaixo.

## Opções de isolamento

| Estratégia | Isolamento | Complexidade | Custo |
|------------|------------|--------------|-------|
| Database per tenant | Máximo | Alta | Alto |
| Schema per tenant | Alto | Média | Médio |
| Row-level security | Médio | Baixa | Baixo |

## Contexto

- **Tipo de dados:** [financeiro, saúde, geral]
- **Número de tenants:** [50, 500, 5000+]
- **Regulamentação:** [LGPD, HIPAA, PCI, nenhuma]
- **Compartilhamento:** tenants precisam compartilhar dados? [sim/não]

## Saída esperada

Análise comparativa das opções com recomendação justificada.
Se Row-Level Security, incluir política SQL.
