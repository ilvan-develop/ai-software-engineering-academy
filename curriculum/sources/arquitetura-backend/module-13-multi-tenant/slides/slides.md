# Módulo 13 — Slides

---

## Slide 1: Título

**Multi-Tenant: Construindo SaaS Escalável**

Como isolar dados, identidade e recursos entre clientes em uma única aplicação

Módulo 13 — Transição de Dev para Enterprise

---

## Slide 2: O que é Multi-Tenancy?

```
┌──────────────────────────────────────┐
│           UMA INSTÂNCIA               │
│                                       │
│  Tenant A   Tenant B   Tenant C      │
│  (Acme)     (Zeta)     (Omega)       │
│                                       │
│  ──────────────┬───────────────────   │
│                │                      │
│            API + DB                   │
└──────────────────────────────────────┘
```

Uma única aplicação servindo múltiplos clientes com dados isolados

Exemplos: Slack (workspaces), Shopify (lojas), Notion (equipes), GitHub (orgs)

---

## Slide 3: Abordagens de Isolamento

| Abordagem | Isolamento | Custo | Complexidade | Ideal para |
|-----------|:----------:|:-----:|:------------:|:----------:|
| DB per Tenant | ⭐⭐⭐ Alto | Alto | Baixa | Enterprise |
| Schema per Tenant | ⭐⭐ Médio | Médio | Média | Pro |
| Shared Database | ⭐ Baixo | Baixo | Alta | Free |

**Regra:** Quanto maior o plano, maior o isolamento

---

## Slide 4: Database per Tenant

```
  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
  │   DB Acme   │     │  DB Zeta    │     │  DB Omega   │
  │  ┌───────┐  │     │  ┌───────┐  │     │  ┌───────┐  │
  │  │ users │  │     │  │ users │  │     │  │ users │  │
  │  │orders │  │     │  │orders │  │     │  │orders │  │
  │  └───────┘  │     │  └───────┘  │     │  └───────┘  │
  └─────────────┘     └─────────────┘     └─────────────┘
```

✅ Isolamento total — nem SQL injection vaza dados
💰 Custo mais alto — N bancos = N × preço
🔧 Backup/restore independente por tenant

---

## Slide 5: Schema per Tenant

```
  ┌────────────────────────────────────┐
  │         Banco Compartilhado         │
  │  ┌──────────┐  ┌──────────┐       │
  │  │tenant_a  │  │tenant_b  │       │
  │  │  users   │  │  users   │       │
  │  │  orders  │  │  orders  │       │
  │  └──────────┘  └──────────┘       │
  └────────────────────────────────────┘
```

✅ Bom custo-benefício para planos Pro
⚠️ Queries pesadas de um tenant afetam os outros
🔄 Migrations rodam para N schemas

---

## Slide 6: Shared Database

```
Tabela única com tenant_id como discriminador

  users
  ┌──────┬───────────┬───────┬───────────┐
  │ id   │ tenant_id │ name  │ email     │
  ├──────┼───────────┼───────┼───────────┤
  │ 1    │ acme      │ João  │ joao@...  │
  │ 2    │ zeta      │ Maria │ maria@... │
  │ 3    │ acme      │ Pedro │ pedro@... │
  └──────┴───────────┴───────┴───────────┘
```

⚠️ Um `SELECT` sem `WHERE tenant_id` vaza dados de todos os tenants
🔑 Índices compostos com `tenant_id` na primeira posição
🛡️ Row-Level Security (RLS) como camada extra

---

## Slide 7: Identificação do Tenant

| Método | Exemplo | Segurança |
|--------|---------|:---------:|
| Subdomínio | `acme.app.com` | Média |
| Header HTTP | `X-Tenant-Id: acme` | Média |
| JWT Claim | `{ "tid": "acme" }` | Alta |
| Path Parameter | `/api/acme/users` | Baixa |

**Middleware extrai e valida antes de qualquer controller**

Prioridade: JWT → Header → Subdomínio

---

## Slide 8: Middleware de Tenant (NestJS)

```typescript
@Injectable()
export class TenantMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    const tenantId = this.extractFromJwt(req)
      ?? req.headers['x-tenant-id'] as string
      ?? req.hostname.split('.')[0];

    const tenant = this.validateTenant(tenantId);
    if (!tenant) throw new UnauthorizedException();

    req.tenant = tenant;
    req.tenantId = tenant.id;
    next();
  }
}
```

AsyncLocalStorage mantém o contexto vivo durante toda a requisição

---

## Slide 9: Dados Compartilhados vs Por Tenant

```
┌────────────────────────────────────┐
│       GLOBAIS (todos os tenants)    │
│  • Planos e preços                 │
│  • Feature flags                   │
│  • Configurações do sistema        │
├────────────────────────────────────┤
│       POR TENANT (isolados)        │
│  • Usuários e permissões           │
│  • Pedidos e faturas               │
│  • Projetos e tarefas              │
│  • Configurações do tenant         │
└────────────────────────────────────┘
```

Sempre pergunte: "esse dado é do sistema ou do cliente?"

---

## Slide 10: Migrations Multi-Tenant

```typescript
// Schema per tenant — aplicar em cada schema
async function migrateSchema(schema: string) {
  for (const migration of MIGRATIONS) {
    const sql = migration.sql.replace(/__SCHEMA__/g, `"${schema}"`);
    await client.query('BEGIN');
    try {
      await client.query(sql);
      await client.query('COMMIT');
    } catch {
      await client.query('ROLLBACK');
      throw error;
    }
  }
}
```

⚠️ Falha em um tenant não deve bloquear os demais (ou deve?)

---

## Slide 11: Performance

**Pool por tenant:**
- Free: max 2 conexões
- Pro: max 10 conexões
- Enterprise: max 25 conexões

**Índices:**
- Sempre `(tenant_id, ...)` como prefixo
- Índices parciais para tenants grandes

**Rate limiting:**
- Free: 100 req/min
- Pro: 1000 req/min
- Enterprise: 10000 req/min

---

## Slide 12: Backup e Restore

| Plano | Backup | RPO | RTO |
|-------|--------|:---:|:---:|
| Free | Diário compartilhado | 24h | 4h |
| Pro | Diário + PITR | 1h | 1h |
| Enterprise | Dedicado + PITR + Réplica | 5min | 15min |

```bash
# DB per Tenant — backup individual
pg_dump "postgresql://.../acme_db" \
  --file="backups/acme_$(date +%Y%m%d).dump"

# Schema per Tenant — backup de schema
pg_dump "postgresql://.../shared" \
  --schema="tenant_acme" \
  --file="backups/schema_acme.dump"
```

---

## Slide 13: Pricing e Planos

| Plano | Isolamento | Usuários | Preço |
|-------|-----------|:--------:|:-----:|
| **Free** | Shared DB | 5 | Grátis |
| **Pro** | Schema per Tenant | 50 | $29/mês |
| **Enterprise** | DB per Tenant | ∞ | $499/mês |

**Feature flags controlam o que cada plano libera:**
```typescript
const PLANS = {
  free:  { customDomain: false, apiAccess: false },
  pro:   { customDomain: false, apiAccess: true },
  enterprise: { customDomain: true, apiAccess: true },
};
```

---

## Slide 14: Testes de Isolamento

```typescript
it('Tenant A não vê dados do Tenant B', async () => {
  await asTenant('acme').post('/users')
    .send({ email: 'joao@acme.com' });

  const res = await asTenant('zeta')
    .get('/users');

  expect(res.body).not.toContainEqual(
    expect.objectContaining({ email: 'joao@acme.com' })
  );
});
```

**Testes obrigatórios:**
- Vazamento zero
- Concorrência entre tenants
- Injeção de tenant_id
- Rate limit por plano
- Quebra proposital do filtro

---

## Slide 15: Anti-padrões

```
❌ Esquecer tenant_id em uma query — dados vazam
❌ Pool único para todos os tenants — um pesado degrada os outros
❌ Migration sem rollback individual — um tenant quebra o deploy
❌ Seed manual — cada novo tenant precisa setup manual
❌ Backup só global — restaurar um tenant vira pesadelo
❌ Sem testes de isolamento — até que um cliente descubra
❌ tenant_id vindo do body da requisição — injeção
```

---

## Slide 16: Para Refletir

> "Multi-tenancy não é só sobre código. É sobre produto, preço e a promessa que você faz ao cliente."

> "O nível de isolamento que você escolhe define o quanto você dorme tranquilo quando um cliente tem um problema."

**Perguntas:**
1. Sua arquitetura atual suportaria 1000 tenants?
2. Você sabe exatamente qual é o custo por tenant?
3. Seus testes provam que Tenant A nunca vê dados do Tenant B?
