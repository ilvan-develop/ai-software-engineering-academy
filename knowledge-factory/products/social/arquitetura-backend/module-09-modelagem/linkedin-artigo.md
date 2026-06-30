==================================================
LINKEDIN — Artigo
==================================================

Titulo: Módulo 09 - Modelagem de Dados: Prisma e PostgreSQL: O Que Todo Arquiteto Deveria Saber


## 1. Por que modelagem importa

- Modelagem de dados é a **fundação** do sistema. Erros aqui são os mais caros de corrigir.
- ┌──────────────────────────────────────────┐
- │  Tabela sem índices → query lenta        │

## 2. Entidades e Relacionamentos

- 1:1  — Um usuário tem um perfil
- 1:N  — Um usuário tem muitos pedidos
- N:M  — Um produto está em muitas categorias

## 3. Soft Delete e Audit Trail

- Nunca delete dados definitivamente em sistemas Enterprise.
- id        String    @id @default(cuid())
- email     String    @unique

## 4. Índices e Performance

- id         String   @id @default(cuid())
- status     OrderStatus
- createdAt  DateTime @default(now())

## 5. Migrações Seguras

- npx prisma migrate dev --name create-user-table
- npx prisma migrate deploy
- npx prisma migrate reset


---

🔥 Gostou? Compartilhe e marque alguem que precisa ler isso.

#ArquiteturaDeSoftware #EngenhariaDeSoftware #CarreiraDev
