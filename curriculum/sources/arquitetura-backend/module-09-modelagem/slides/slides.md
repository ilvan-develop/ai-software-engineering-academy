# Módulo 09 — Slides

---

## Slide 1: Título

**Modelagem de Dados**
Prisma, PostgreSQL e boas práticas

---

## Slide 2: Por que modelagem importa

```text
Modelagem ruim:               Modelagem boa:
Query lenta                   Queries rápidas
Dados inconsistentes          Dados íntegros
Perda de dados                Dados seguros
Horas de migração             Migrações testadas
```markdown

Erro de modelagem é o mais caro de corrigir

---

## Slide 3: Relacionamentos

```yaml
1:1  → User ── Profile
1:N  → User ──< Order
N:M  → Product >─< Category
```sql

No Prisma: `@relation`, `@unique` (1:1), `@@id([a, b])` (N:M)

---

## Slide 4: Soft Delete

```prisma
model User {
  id        String
  deletedAt DateTime?   // Nunca deletar fisicamente
}
```text

```typescript
// Service
async softDelete(id: string) {
  await prisma.user.update({
    where: { id },
    data: { deletedAt: new Date() },
  });
}
```markdown

---

## Slide 5: Audit Trail

```prisma
model AuditLog {
  entity   String
  entityId String
  action   String   // CREATE, UPDATE, DELETE
  changes  Json?    // { before, after }
  userId   String?
}
```javascript

Toda ação importante é registrada

---

## Slide 6: Índices

```prisma
@@index([userId])              // FK
@@index([userId, status])      // Filtro comum
@@index([createdAt])           // Ordenação
```yaml

Regras:
- Toda FK precisa de índice
- Índices compostos para filtros comuns
- Evite índices em boolean/campos de baixa cardinalidade

---

## Slide 7: N+1 vs Eager Loading

```typescript
// ❌ N+1: 1 query + N queries
const orders = await prisma.order.findMany();
for (const order of orders) {
  const items = await prisma.orderItem.findMany(
    { where: { orderId: order.id } }
  );
}

// ✅ Eager: 1 query (JOIN)
const orders = await prisma.order.findMany({
  include: { items: true, user: true },
});
```markdown

---

## Slide 8: Migrações seguras

```text
Expand → Migrate → Contract

Passo 1: Adicionar coluna (nullable)
Passo 2: Preencher dados
Passo 3: Remover coluna antiga (próxima release)
```yaml

Nunca: renomear/deletar coluna diretamente

---

## Slide 9: Backup

```yaml
Full:       Diário, cópia completa
Incremental: Horário, só mudanças
WAL:         Contínuo, point-in-time recovery

Regra: teste o restore periodicamente!
```markdown

---

## Slide 10: Schema completo

```text
tenants → users → orders → order_items
                        ↓
                  products ← audit_logs
```sql

Índices, soft delete, audit trail, enums

---

## Slide 11: Anti-padrões

- **Deletar fisicamente** — sem chance de recuperação
- **Sem audit trail** — impossível saber quem fez o quê
- **FK sem índice** — JOIN lento
- **N+1 queries** — N pequeno vira N grande
- **Migration destrutiva** — sem rollback
- **Backup sem teste** — "o backup funciona" (será?)
- **Schema sem documentação** — ninguém sabe o que cada campo significa

---

## Slide 12: Para refletir

> "Seu schema é o contrato mais importante do sistema. Trate-o como tal."

> "Modelagem boa é invisível. Modelagem ruim aparece em toda query."
