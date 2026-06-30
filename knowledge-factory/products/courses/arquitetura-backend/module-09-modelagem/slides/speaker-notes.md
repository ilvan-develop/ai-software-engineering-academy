## Introducao

# Módulo 09 — Modelagem de Dados: Prisma e PostgreSQL
**A base de todo sistema Enterprise.**
---

---
## 1. Por que modelagem importa

Modelagem de dados é a **fundação** do sistema. Erros aqui são os mais caros de corrigir.
### O custo de uma modelagem ruim
Modelagem ruim:
┌──────────────────────────────────────────┐
│  Tabela sem índices → query lenta        │
│  Relação errada → dados inconsistentes   │
│  Falta de soft delete → perda de dados   │
│  Sem audit trail → impossível auditar    │

---
## 2. Entidades e Relacionamentos

### Tipos de Relacionamento
1:1  — Um usuário tem um perfil
1:N  — Um usuário tem muitos pedidos
N:M  — Um produto está em muitas categorias
### Exemplo no Prisma
// 1:1
model User {
id      String  @id @default(cuid())

---
## 3. Soft Delete e Audit Trail

### Soft Delete
Nunca delete dados definitivamente em sistemas Enterprise.
model User {
id        String    @id @default(cuid())
email     String    @unique
name      String
createdAt DateTime  @default(now())
updatedAt DateTime  @updatedAt

---
## 4. Índices e Performance

### Quando criar índices
model Order {
id         String   @id @default(cuid())
userId     String
status     OrderStatus
total      Decimal
createdAt  DateTime @default(now())
// Índice para busca por usuário (foreign key)

---
## 5. Migrações Seguras

### Criando migrações
# Criar migration baseada no schema
npx prisma migrate dev --name create-user-table
# Aplicar em produção
npx prisma migrate deploy
# Resetar banco (dev)
npx prisma migrate reset
### Migrações sem downtime

---
## 6. Estratégias de Backup

### Tipos de backup
Full:     Cópia completa do banco
Quando: Diário
Tempo:  Lento, ocupa espaço
Restore: Completo, mais simples
Incremental: Apenas mudanças desde o último backup
Quando: Horário
Tempo:  Rápido, ocupa pouco espaço

---
## 7. Schema completo de exemplo

O diagrama abaixo resume as entidades, atributos e cardinalidades do schema:
![Modelo Entidade-Relacionamento Enterprise](/knowledge-factory/products/courses/arquitetura-backend/module-09-modelagem/assets/diagram-er-schema-enterprise.svg)
generator client {
provider = "prisma-client-js"
}
datasource db {
provider = "postgresql"
url      = env("DATABASE_URL")

---
## Resumo

1. **Modelagem é a fundação** — erros aqui são os mais caros
2. **1:1, 1:N, N:M** — conheça os 3 tipos de relacionamento
3. **Soft Delete** — nunca delete dados (deletedAt)
4. **Audit Trail** — toda ação importante deve ser registrada
5. **Índices** — toda FK precisa de índice; índices compostos para filtros comuns
6. **Eager Loading** — previne N+1
7. **Migrações seguras** — expand-migrate-contract para mudanças sem downtime
8. **Backup** — full + incremental + WAL; testar restore periodicamente

---
