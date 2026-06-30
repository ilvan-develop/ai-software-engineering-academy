# Projeto Módulo 13 — SaaS Multi-Tenant: TaskHub

## Objetivo

Construir a base de um SaaS multi-tenant do zero, implementando identificação de tenant, isolamento de dados, migrations, seed automático, feature flags por plano, e testes de isolamento.

## Contexto

Você é o engenheiro de software responsável por implementar a arquitetura multi-tenant do **TaskHub**, um SaaS de gestão de tarefas e projetos. O sistema precisa atender múltiplas empresas (tenants) com dados completamente isolados.

Cada empresa que se cadastra no TaskHub vira um **tenant**. Dentro do tenant, os usuários podem criar projetos, tarefas, e gerenciar suas atividades. Nenhum tenant pode ver dados de outro tenant.

### Stack

| Tecnologia | Versão | Uso |
|-----------|--------|-----|
| NestJS | ^10 | Framework backend |
| PostgreSQL | 15+ | Banco de dados |
| Prisma | ^5 | ORM |
| TypeScript | ^5 | Linguagem |
| Jest | ^29 | Testes |
| Supertest | ^6 | Testes HTTP |
| jsonwebtoken | ^9 | JWT |
| pg | ^8 | PostgreSQL driver (para scripts) |

### Estrutura do Projeto

```
taskhub/
├── src/
│   ├── tenant/
│   │   ├── tenant.module.ts
│   │   ├── tenant.service.ts
│   │   ├── tenant.middleware.ts
│   │   ├── tenant.decorator.ts
│   │   └── tenant-context.ts
│   ├── common/
│   │   ├── guards/
│   │   │   ├── feature.guard.ts
│   │   │   └── limit.guard.ts
│   │   └── repositories/
│   │       └── tenant-repository.ts
│   ├── users/
│   │   ├── users.module.ts
│   │   ├── users.controller.ts
│   │   └── users.service.ts
│   ├── projects/
│   │   ├── projects.module.ts
│   │   ├── projects.controller.ts
│   │   └── projects.service.ts
│   ├── tasks/
│   │   ├── tasks.module.ts
│   │   ├── tasks.controller.ts
│   │   └── tasks.service.ts
│   ├── plans/
│   │   ├── plans.module.ts
│   │   ├── plans.service.ts
│   │   └── feature-flags.ts
│   ├── prisma/
│   │   ├── prisma.module.ts
│   │   └── prisma.service.ts
│   └── main.ts
├── prisma/
│   └── schema.prisma
├── scripts/
│   ├── migrate-all.ts
│   ├── seed-tenant.ts
│   └── backup-tenant.ts
├── test/
│   └── tenant-isolation.spec.ts
├── docker-compose.yml
├── package.json
└── tsconfig.json
```

## Entregáveis

### 1. Middleware de Tenant (src/tenant/)

Implemente um middleware NestJS que:

- Extraia o tenant de três fontes com precedência: **JWT** (claim `tid`) → **Header** (`X-Tenant-Id`) → **Subdomínio**
- Valide que o tenant existe em um cache (carregado de uma tabela `tenants` no banco)
- Valide que o tenant está ativo (`active = true`)
- Configure o `AsyncLocalStorage` com o contexto do tenant
- Rejeite requisições sem tenant identificado com `401 Unauthorized`
- Rejeite requisições de tenant inativo com `403 Forbidden`

```typescript
// tenant.middleware.ts — assinatura esperada
@Injectable()
export class TenantMiddleware implements NestMiddleware {
  async use(req: Request, res: Response, next: NextFunction) {
    // 1. Extrair tenant ID
    // 2. Buscar no cache/banco
    // 3. Validar active
    // 4. Configurar AsyncLocalStorage
    // 5. Anexar ao request
    // 6. next()
  }
}
```

Crie também o decorator `@Tenant()`:

```typescript
// tenant.decorator.ts
export const Tenant = createParamDecorator(
  (data: keyof TenantInfo | undefined, ctx: ExecutionContext) => {
    // Retorna o tenant ou uma propriedade específica
  }
);

// Uso:
@Get('profile')
getProfile(@Tenant() tenant: TenantInfo) { ... }
@Get('plan')
getPlan(@Tenant('plan') plan: string) { ... }
```

### 2. TenantRepository Genérico (src/common/repositories/)

Crie uma classe genérica `TenantRepository<T>` que:

- Force `WHERE tenant_id = $1` em TODAS as queries
- Injete automaticamente `tenant_id` em inserts
- Seja extensível para diferentes entidades (User, Project, Task)

```typescript
interface BaseEntity {
  id: string;
  tenantId: string;
  createdAt: Date;
}

class TenantRepository<T extends BaseEntity> {
  constructor(
    protected readonly prisma: PrismaService,
    protected readonly tenantService: TenantService,
    protected readonly model: string,
  ) {}

  async findAll(params?: {
    where?: any;
    orderBy?: any;
    take?: number;
    skip?: number;
  }): Promise<T[]> {
    // Adiciona tenantId no where automaticamente
    return this.prisma[this.model].findMany({
      ...params,
      where: {
        ...params?.where,
        tenantId: this.tenantService.getTenantId(),
      },
    });
  }

  async create(data: Omit<T, 'id' | 'tenantId' | 'createdAt'>): Promise<T> {
    // Adiciona tenantId automaticamente
  }

  async update(id: string, data: Partial<Omit<T, 'id' | 'tenantId'>>): Promise<T> {
    // WHERE id AND tenantId
  }

  async delete(id: string): Promise<void> {
    // WHERE id AND tenantId
  }

  async count(where?: any): Promise<number> {
    // WHERE tenantId + filtros
  }
}
```

### 3. Feature Flags por Plano (src/plans/)

Implemente:

- **3 planos**: Free, Pro, Enterprise
- **Feature flags**: `maxProjects`, `maxMembers`, `customDomain`, `apiAccess`, `advancedReports`, `auditLog`, `ssoEnabled`, `whiteLabel`
- **FeatureFlagService**: métodos para verificar se feature está habilitada e checar limites
- **FeatureGuard**: `@UseGuards(FeatureGuard('apiAccess'))` que bloqueia endpoints se feature não habilitada
- **LimitGuard**: `@UseGuards(LimitGuard('maxUsers'))` que bloqueia se limite excedido
- **Endpoint**: `GET /api/tenant/features` que retorna as features disponíveis para o tenant atual

```typescript
// Exemplo de uso nos controllers
@Controller('projects')
export class ProjectsController {
  @Post()
  @UseGuards(LimitGuard('maxProjects'))
  createProject(@Body() dto: CreateProjectDto) {
    return this.projectsService.create(dto);
  }

  @Get('reports')
  @UseGuards(FeatureGuard('advancedReports'))
  getAdvancedReports() {
    return this.projectsService.generateReports();
  }
}
```

### 4. Prisma Schema e Migrations (prisma/ + scripts/)

**Prisma Schema:**
- Tabela global `Tenant` (id, slug, name, plan, active, createdAt)
- Tabelas por tenant: `User`, `Project`, `Task` — todas com `tenantId`
- Índices: `@@index([tenantId])` e `@@index([tenantId, email])`

**Scripts:**
- `scripts/seed-tenant.ts` — cria estrutura + seed data (admin padrão, configurações) para novos tenants
- `scripts/tenant-create.ts` — comando CLI que cria tenant + roda seed
- `scripts/migrate-all.ts` — aplica migrations em todos os schemas (schema per tenant)

```prisma
// schema.prisma — shared database approach
model Tenant {
  id        String   @id @default(uuid())
  slug      String   @unique
  name      String
  plan      String   @default("free")
  active    Boolean  @default(true)
  createdAt DateTime @default(now()) @map("created_at")
  @@map("tenants")
}

model User {
  id        String   @id @default(uuid())
  tenantId  String   @map("tenant_id")
  name      String
  email     String
  role      String   @default("member")
  createdAt DateTime @default(now()) @map("created_at")
  @@index([tenantId])
  @@index([tenantId, email])
  @@map("users")
}

// Project, Task — similar pattern
```

### 5. Testes de Isolamento (test/tenant-isolation.spec.ts)

Implemente testes automatizados que provem:

1. **Vazamento zero**: criar dados como Tenant A, listar como Tenant B — lista vazia
2. **Concorrência segura**: 5 tenants simultâneos (Promise.all) — cada um vê apenas seus dados
3. **Injeção de tenant_id**: tentar criar dado com tenant_id diferente no body — deve ser ignorado
4. **Rate limiting**: exceder limite do tenant Free (100 req/min) — verificar 429
5. **Feature flag**: acessar endpoint `advancedReports` como Free — verificar 403
6. **Quebra proposital**: query sem `WHERE tenant_id` — provar que retorna dados de todos

```typescript
describe('TaskHub — Isolamento Multi-Tenant', () => {
  let app: INestApplication;

  const asTenant = (slug: string) => {
    const token = jwt.sign({ sub: 'user1', tid: slug }, 'test-secret');
    return request(app.getHttpServer())
      .set('Authorization', `Bearer ${token}`)
      .set('X-Tenant-Id', slug);
  };

  describe('Vazamento de dados', () => {
    it('Tenant A não vê dados do Tenant B', async () => { /* ... */ });
    it('rejeita requisição sem tenant', async () => { /* ... */ });
    it('rejeita token com tenant inexistente', async () => { /* ... */ });
  });

  describe('Concorrência', () => {
    it('5 tenants simultâneos sem misturar dados', async () => { /* ... */ });
  });

  describe('Injeção de tenant_id', () => {
    it('ignora tenant_id enviado no body', async () => { /* ... */ });
  });

  describe('Rate limiting', () => {
    it('bloqueia Free após 100 req/min', async () => { /* ... */ });
    it('Enterprise não rate limita com mesma carga', async () => { /* ... */ });
  });

  describe('Feature flags', () => {
    it('Free não acessa advancedReports', async () => { /* ... */ });
    it('Enterprise acessa customDomain', async () => { /* ... */ });
  });
});
```

### 6. Pool Manager (src/common/pool-manager.ts)

Implemente um gerenciador de pools de conexão:

- Pool separado por tenant (lazy initialization)
- Limites por plano: Free=2, Pro=10, Enterprise=25
- Cleanup de pools ociosos (5 min sem uso)
- Método `getStats()` para monitoramento

## Critérios de Avaliação

| Critério | Peso | Descrição |
|----------|:----:|-----------|
| **Middleware de Tenant** | 15% | Extrai tenant de 3 fontes, valida existência/ativo, configura AsyncLocalStorage |
| **TenantRepository Genérico** | 15% | Força tenantId em todas as queries, injeta em creates, extensível |
| **Feature Flags** | 15% | Planos definidos, FeatureGuard/LimitGuard funcionais, endpoint /features |
| **Prisma + Migrations** | 15% | Schema correto, índices, scripts de seed e migration funcionais |
| **Testes de Isolamento** | 20% | Vazamento zero, concorrência, injeção, rate limit, feature flag, quebra proposital |
| **Pool Manager** | 10% | Pool por tenant, limites por plano, cleanup ocioso, stats |
| **Código TypeScript** | 10% | Strict mode, tipos corretos, sem `any`, organização dos arquivos |

## Entrega

O projeto deve ser entregue em um repositório GitHub com:

1. Código fonte completo (src/)
2. Prisma schema e migrations
3. Scripts de seed e migração
4. Testes automatizados
5. Docker Compose para ambiente de desenvolvimento
6. README com instruções de setup, criação de tenant e execução dos testes

**Bônus:** Implementar Row-Level Security (RLS) no PostgreSQL como camada extra de segurança.
