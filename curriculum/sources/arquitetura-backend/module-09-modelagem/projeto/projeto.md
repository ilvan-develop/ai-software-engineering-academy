# Projeto Módulo 09 — Modelagem de SaaS Multi-tenant

## Objetivo

Modelar o banco de dados completo de um SaaS Enterprise com multi-tenant, soft delete e audit trail.

## Contexto

**SaaS de Gestão de Projetos Enterprise** com:
- Múltiplas empresas (tenants)
- Usuários com perfis (admin, gerente, dev, cliente)
- Projetos com tarefas
- Comentários em tarefas
- Anexos (arquivos)
- Times e membros
- Relatórios

## Entregáveis

### 1. Schema Prisma completo

Modele todas as entidades com:
- Relacionamentos corretos (1:1, 1:N, N:M)
- Índices em FKs e campos de busca
- Soft delete em todas as entidades
- Timestamps (createdAt, updatedAt)

### 2. Estratégia multi-tenant

Defina:
- Como isolar dados entre tenants (tenantId em cada tabela)
- Como garantir que queries sempre filtrem por tenant
- Como fazer backup por tenant

### 3. Audit trail

- Modele a tabela AuditLog
- Crie um middleware Prisma que registra mudanças automaticamente
- Inclua: entidade, ID, ação, before/after, userId, ip

### 4. Índices

- Liste quais índices criar e por quê
- Inclua índices compostos para consultas comuns
- Inclua índices parciais se aplicável

### 5. Queries otimizadas

Escreva as queries Prisma para:
- Listar tarefas de um projeto (com eager loading de autor e comentários)
- Buscar projetos onde o usuário é membro
- Relatório de tarefas por status (agregação)
- Histórico de mudanças de uma tarefa (audit log)

## Critérios de avaliação

- [ ] Schema completo com todas as entidades
- [ ] Relacionamentos corretos (1:1, 1:N, N:M)
- [ ] Soft delete em todas as entidades
- [ ] Audit trail funcional
- [ ] Índices justificados
- [ ] Queries otimizadas (sem N+1)
- [ ] Estratégia multi-tenant clara
