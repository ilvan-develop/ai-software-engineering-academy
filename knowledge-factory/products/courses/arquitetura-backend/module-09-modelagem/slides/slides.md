---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 09 — Modelagem de Dados: Prisma e PostgreSQL

## Módulo 09 - Modelagem de Dados: Prisma e PostgreSQL

---
## 1. Por que modelagem importa

- Modelagem de dados é a **fundação** do sistema. Erros aqui são os mais caros de corrigir.
- Modelagem ruim:
- ┌──────────────────────────────────────────┐
- │  Tabela sem índices → query lenta        │
- │  Relação errada → dados inconsistentes   │

---
## 2. Entidades e Relacionamentos

- 1:1  — Um usuário tem um perfil
- 1:N  — Um usuário tem muitos pedidos
- N:M  — Um produto está em muitas categorias
- // 1:1

---
## 3. Soft Delete e Audit Trail

- Nunca delete dados definitivamente em sistemas Enterprise.
- model User {
- id        String    @id @default(cuid())
- email     String    @unique
- name      String

---
## 4. Índices e Performance

- model Order {
- id         String   @id @default(cuid())
- userId     String
- status     OrderStatus
- total      Decimal

---
## 5. Migrações Seguras

- npx prisma migrate dev --name create-user-table
- npx prisma migrate deploy

---
## 6. Estratégias de Backup

- Full:     Cópia completa do banco
- Quando: Diário
- Tempo:  Lento, ocupa espaço
- Restore: Completo, mais simples
- Incremental: Apenas mudanças desde o último backup

---
## 7. Schema completo de exemplo

- O diagrama abaixo resume as entidades, atributos e cardinalidades do schema:
- ![Modelo Entidade-Relacionamento Enterprise](/knowledge-factory/products/courses/arquitetura-backend/module-09-modela...
- generator client {
- provider = "prisma-client-js"
- }
- datasource db {

---
## Resumo

- 1. **Modelagem é a fundação** — erros aqui são os mais caros
- 2. **1:1, 1:N, N:M** — conheça os 3 tipos de relacionamento
- 3. **Soft Delete** — nunca delete dados (deletedAt)
- 4. **Audit Trail** — toda ação importante deve ser registrada
- 5. **Índices** — toda FK precisa de índice; índices compostos para filtros comuns
- 6. **Eager Loading** — previne N+1

---
## Exemplo: text

```text
Modelagem ruim:
  ┌──────────────────────────────────────────┐
  │  Tabela sem índices → query lenta        │
  │  Relação errada → dados inconsistentes   │
  │  Falta de soft delete → perda de dados   │
  │  Sem audit trail → impossível auditar    │
  │  Migração corretiva → horas de trabalho  │
  └──────────────────────────────────────────┘

Modelagem boa:
  ┌──────────────────────────────────────────┐
  │  Índices certos → queries rápidas        │
...
```

---
## Exemplo: text

```text
1:1  — Um usuário tem um perfil
1:N  — Um usuário tem muitos pedidos
N:M  — Um produto está em muitas categorias
```

---
## Recap

- 1. Por que modelagem importa
- 2. Entidades e Relacionamentos
- 3. Soft Delete e Audit Trail
- 4. Índices e Performance
- 5. Migrações Seguras
- 6. Estratégias de Backup
- 7. Schema completo de exemplo
- Resumo

---
# Obrigado!

## Perguntas?
