# Prompt: Modelar Schema Prisma

Você é um Prisma Expert Agent.

Modele o schema Prisma para a funcionalidade abaixo.

## Requisitos

- **Entidades:** [lista]
- **Relações:** [1:1, 1:N, N:M]
- **Requisitos especiais:**
  - Soft delete
  - Audit trail
  - Multi-tenant (row-level isolation)
  - Search via índices

## Saída esperada

```prisma
// Schema Prisma completo com:
// - Models com campos, tipos e relações
// - Enums
// - Índices compostos
// - Comentários de documentação
// - @map para tabelas
```

Regras:
- Usar cuid para IDs
- Timestamps (createdAt, updatedAt) em todos os modelos
- Índices em campos de busca e foreign keys
- Relações com onDelete: Cascade quando apropriado
- Nomes em português (entidades) ou inglês (conforme padrão do projeto)
