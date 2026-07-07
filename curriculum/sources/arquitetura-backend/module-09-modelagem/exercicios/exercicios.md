# Exercícios — Módulo 09

## Exercício 1: Modelando relacionamentos

Modelo no Prisma os relacionamentos para:

**Sistema de Biblioteca:**
- Livro: título, autor, ISBN (único), ano, cópias disponíveis
- Usuário: nome, email, telefone
- Empréstimo: data retirada, data devolução, status
- Cada empréstimo tem 1 usuário e 1 livro
- Usuário pode ter múltiplos empréstimos
- Livro pode estar em múltiplos empréstimos (ao longo do tempo)

Inclua: índices, soft delete, audit trail, timestamps.

---

## Exercício 2: Soft Delete

Converta o schema abaixo para usar soft delete em vez de delete físico:

```prisma
model Post {
  id        String   @id @default(cuid())
  title     String
  content   String
  authorId  String
  author    User     @relation(fields: [authorId], references: [id])
  createdAt DateTime @default(now())
}
```sql

Além do soft delete:
- O service deve filtrar posts deletados automaticamente
- O admin deve poder ver posts deletados (opção `includeDeleted`)
- O service deve ter `restore(id)` para recuperar posts

---

## Exercício 3: Audit Trail

Implemente um audit trail para o módulo de pedidos:

```prisma
model Order {
  id        String   @id @default(cuid())
  status    OrderStatus
  total     Decimal
  userId    String
  // ...
}
```yaml

Crie:
1. Um audit log que registra cada mudança de status
2. Um middleware Prisma que captura as mudanças
3. Um endpoint para consultar o histórico de um pedido

Formato do log:
```json
{
  "entity": "Order",
  "entityId": "abc123",
  "action": "UPDATE",
  "changes": {
    "before": { "status": "PENDING" },
    "after": { "status": "CONFIRMED" }
  },
  "userId": "user123",
  "timestamp": "..."
}
```markdown

---

## Exercício 4: Índices e performance

Analise o schema abaixo e identifique:
1. Quais índices estão faltando
2. Quais índices são desnecessários
3. Quais consultas serão lentas

```prisma
model Transaction {
  id            String   @id @default(cuid())
  accountId     String
  type          String   // "CREDIT", "DEBIT"
  amount        Decimal
  description   String?
  createdAt     DateTime @default(now())

  @@index([type])
}
```text

Consultas comuns:
1. Buscar todas as transações de uma conta
2. Buscar transações de uma conta por tipo
3. Buscar transações de uma conta por data (últimos 30 dias)
4. Buscar transações de todas as contas por tipo e data
5. Relatório mensal de transações por tipo

---

## Exercício 5: Migração sem downtime

Você precisa renomear a coluna `fullname` para `name` na tabela `users`.

Descreva o plano completo usando a estratégia expand-migrate-contract:

1. **Expand** — qual migration criar primeiro
2. **Migrate** — qual script rodar para preencher dados
3. **Contract** — qual migration rodar na próxima release

Inclua os comandos Prisma e scripts necessários.
