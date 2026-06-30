# Checklist: Database Architect Agent

## Modelagem
- [ ] Normalização até 3NF (ou justificativa para denormalizar)
- [ ] Chaves primárias definidas (UUID/cuid)
- [ ] Chaves estrangeiras com índices
- [ ] Tipos de colunas adequados (varchar vs text, int vs bigint)

## Performance
- [ ] Índices compostos para queries frequentes
- [ ] Índices parciais para dados filtrados
- [ ] Consultas N+1 eliminadas no schema
- [ ] Paginação implementada (cursor-based)

## Integridade
- [ ] Constraints CHECK para validação
- [ ] Unique constraints onde necessário
- [ ] Foreign keys com ON DELETE adequado
- [ ] Soft delete implementado (deleted_at)

## Migrações
- [ ] Migrações testadas em staging
- [ ] Rollback possível
- [ ] Seed data para desenvolvimento
