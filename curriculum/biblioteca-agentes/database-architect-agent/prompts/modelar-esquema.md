# Prompt: Modelar Esquema de Dados

Modele o esquema de banco de dados para o sistema abaixo.

## Requisitos

- **Domínio:** [nome]
- **Entidades principais:** [lista]
- **Volume estimado:** [registros/dia]
- **Requisitos não-funcionais:**
  - Multi-tenant? [sim/não]
  - Soft delete? [sim/não]
  - Audit trail? [sim/não]

## Saída esperada

```sql
-- Esquema PostgreSQL com:
-- 1. Tabelas e colunas
-- 2. Relações e foreign keys
-- 3. Índices (incluindo compostos e parciais)
-- 4. Constraints
-- 5. Estratégia de particionamento (se aplicável)
-- 6. Comentários de documentação
```

Regras:
- UUID como chave primária
- Timestamps (created_at, updated_at, deleted_at) em todas as tabelas
- Índices em foreign keys e campos de busca
- Nomes em snake_case
