# Exercícios — Capítulo 5: Multi-Tenant — Conceitos e Estratégias

> **Progressão:** Fácil → Médio → Difícil  
> **Total:** 4 exercícios

---

## Exercício 1 — Fácil: Identifique a Estratégia de Isolamento

**Tema:** Estratégias de isolamento de dados

Para cada cenário, indique qual estratégia de isolamento é mais adequada:

| # | Cenário | Estratégia |
|---|---------|------------|
| 1 | SaaS para pequenas empresas, 500 tenants, cada um com poucos dados. Orçamento limitado. | ? |
| 2 | Sistema financeiro regulado onde cada cliente exige isolamento físico dos dados. | ? |
| 3 | Plataforma de médio porte, 200 tenants, alguns com dados sensíveis que exigem isolamento intermediário. | ? |

**Opções:** Banco por Tenant | Schema por Tenant | Coluna Discriminadora (discriminator column)

---

## Exercício 2 — Médio: Middleware de Tenant

**Tema:** Identificação e resolução de tenant

Implemente um middleware NestJS que:
1. Extrai o tenantId do header `X-Tenant-Id`
2. Valida se o tenant existe e está ativo
3. Injeta o tenant no `request.tenant` (disponível para guards, services, etc.)
4. Retorna 400 se o header estiver ausente
5. Retorna 404 se o tenant não existir

```typescript
@Injectable()
export class TenantMiddleware implements NestMiddleware {
  constructor(private tenantService: TenantService) {}
  use(req: Request, res: Response, next: NextFunction) { /* ... */ }
}
```

---

## Exercício 3 — Médio: Análise Comparativa

**Tema:** Trade-offs entre estratégias

Complete a tabela comparativa das 3 estratégias de isolamento:

| Dimensão | Banco por Tenant | Schema por Tenant | Coluna Discriminadora |
|----------|:----------------:|:-----------------:|:---------------------:|
| Isolamento | ? | ? | ? |
| Custo | ? | ? | ? |
| Complexidade | ? | ? | ? |
| Backup/Restore | ? | ? | ? |
| Cross-tenant queries | ? | ? | ? |
| Número máximo de tenants | ? | ? | ? |

---

## Exercício 4 — Difícil: Tenant por Schema no Prisma

**Tema:** Implementação de multi-tenancy via schema

Modele o schema Prisma para um sistema multi-tenant usando a estratégia de **coluna discriminadora** (tenantId em cada tabela).

**Entidades:** `Tenant`, `User`, `Project`, `Task`

**Requisitos:**
- Cada tenant tem seus próprios usuários, projetos e tarefas
- Nenhum tenant pode ver dados de outro tenant
- Índices apropriados para queries por tenant
- `Tenant` deve ter: id, nome, slug (único globalmente), plano, ativo
- Queries globais de tenant devem ser automáticas (middleware Prisma)

```prisma
// Escreva o schema completo
model Tenant { /* ... */ }
model User { /* ... */ }
model Project { /* ... */ }
model Task { /* ... */ }
```
