# Exercícios — Capítulo 2: Modelagem de Sistemas

> **Progressão:** Fácil → Médio → Difícil  
> **Total:** 4 exercícios

---

## Exercício 1 — Fácil: Identifique Problemas de Modelagem

**Tema:** Boas práticas de modelagem de dados

Analise o schema Prisma abaixo e identifique **3 problemas**:

```prisma
model User {
  id      Int     @id @default(autoincrement())
  name    String
  email   String
  posts   Post[]
  profile Profile?
}

model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String
  authorId  Int
  author    User     @relation(fields: [authorId], references: [id])
}
```

**Problemas a considerar:** índices faltantes, soft delete, auditoria, campos opcionais.

---

## Exercício 2 — Médio: Modele um Sistema de E-commerce

**Tema:** Modelagem relacional com Prisma

Modele as seguintes entidades para um sistema de e-commerce:

- **Produto**: id, nome, descrição, preço, estoque, sku, ativo
- **Cliente**: id, nome, email, telefone, endereços
- **Pedido**: id, cliente, itens, status, total, data de criação
- **Item do Pedido**: produto, quantidade, preço unitário

**Requisitos:**
- Um cliente pode ter múltiplos endereços
- Pedido deve ter status (enum: PENDENTE, PAGO, ENVIADO, ENTREGUE, CANCELADO)
- Quando o preço do produto mudar, o pedido deve manter o preço da compra
- Adicione índices apropriados
- Adicione campos de auditoria (createdAt, updatedAt)

---

## Exercício 3 — Médio: Migração com Seed

**Tema:** Migrations e seeds no Prisma

Crie uma migration que adiciona um campo `deletedAt` (soft delete) na tabela `Product`. Em seguida, crie um seed que popula a tabela com 3 produtos iniciais.

```prisma
// schema.prisma (trecho)
model Product {
  id          String   @id @default(cuid())
  name        String
  price       Float
  stock       Int      @default(0)
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
}
```

**Tarefas:**
1. Escreva o Prisma schema atualizado com soft delete
2. Escreva o conteúdo do arquivo `seed.ts` que cria 3 produtos
3. Explique como a migration afeta queries existentes

---

## Exercício 4 — Difícil: Performance com Índices

**Tema:** Índices compostos e performance de queries

Dado o schema:

```prisma
model Order {
  id          String   @id @default(cuid())
  tenantId    String
  customerId  String
  status      OrderStatus
  total       Float
  createdAt   DateTime @default(now())
  paidAt      DateTime?
  cancelledAt DateTime?
  
  @@index([tenantId])
}
```

As queries mais comuns no sistema são:
1. `WHERE tenantId = ? AND status = ? ORDER BY createdAt DESC`
2. `WHERE tenantId = ? AND customerId = ?`
3. `WHERE tenantId = ? AND createdAt BETWEEN ? AND ?`
4. `WHERE tenantId = ? AND status = ? AND total > ?`

**Tarefa:** Proponha os índices ideais para cada query. Considere índices compostos e a ordem das colunas. Explique por que a ordem importa.
