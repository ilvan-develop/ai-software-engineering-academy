# Exercícios — Capítulo 7: Multi-Tenant — Migrations, Dados e Seed

> **Progressão:** Fácil → Médio → Difícil  
> **Total:** 4 exercícios

---

## Exercício 1 — Fácil: Seed de Tenant Padrão

**Tema:** Dados iniciais para novos tenants

Crie um arquivo `seed.ts` que:

1. Cria 2 tenants: "Acme Corp" (slug: acme) e "Zeta Inc" (slug: zeta)
2. Para cada tenant, cria 1 usuário admin
3. Para cada tenant, cria 1 projeto exemplo

```typescript
// seed.ts
import { PrismaClient } from '@prisma/client';
const prisma = new PrismaClient();

async function main() {
  // Implemente o seed
}

main()
  .catch(console.error)
  .finally(() => prisma.$disconnect());
```

---

## Exercício 2 — Médio: Migração com Dados por Tenant

**Tema:** Migrations que respeitam o contexto de tenant

Crie uma migration que adiciona uma tabela `AuditLog` ao schema:

```prisma
model AuditLog {
  id        String   @id @default(cuid())
  tenantId  String
  userId    String
  action    String
  entity    String
  entityId  String
  oldValue  Json?
  newValue  Json?
  createdAt DateTime @default(now())
  
  @@index([tenantId, createdAt])
}
```

**Tarefa:** Adicione a lógica no middleware do Prisma para que:
- Todo `create` em `AuditLog` receba automaticamente o `tenantId`
- Todo `findMany` em `AuditLog` filtre pelo tenant atual
- Explique como garantir que dados de audit não vazem entre tenants

---

## Exercício 3 — Médio: Estratégia de Backup por Tenant

**Tema:** Backup e restore seletivo

Descreva a estratégia para backup e restore de dados de um tenant específico em cada arquitetura:

| Estratégia | Como fazer backup de 1 tenant? | Como restaurar? |
|------------|-------------------------------|-----------------|
| Banco por Tenant | ? | ? |
| Schema por Tenant | ? | ? |
| Coluna Discriminadora | ? | ? |

**Dica:** Considere ferramentas como `pg_dump`, scripts de exportação e janelas de manutenção.

---

## Exercício 4 — Difícil: Data Migration Segura

**Tema:** Migração de dados entre tenants sem downtime

Uma empresa cliente (tenant "alpha") precisa ser dividida em 3 tenants menores ("alpha-br", "alpha-us", "alpha-eu") devido a requisitos regulatórios de soberania de dados.

**Requisitos:**
- Zero downtime durante a migração
- Consistência dos dados garantida
- Rollback possível se algo der errado
- Usuários existentes devem ser redistribuídos

**Tarefa:** Elabore um plano de migração em etapas com:
1. Preparação (schemas, índices, scripts)
2. Execução (como copiar dados, manter sincronia)
3. Validação (como verificar consistência)
4. Cutover (como e quando mudar o DNS/routing)
5. Rollback (procedimento de reversão)
