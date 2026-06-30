# Módulo 13 — Multi-Tenant: Construindo SaaS Escalável

**Como isolar dados, identidade e recursos entre clientes em uma única aplicação.**

---

## 1. O que é Multi-Tenancy?

Multi-tenancy é um padrão arquitetural onde **uma única instância de software atende múltiplos clientes (tenants)**, mantendo os dados de cada um logicamente isolados e invisíveis entre si.

```
┌──────────────────────────────────────────────────────┐
│                    SISTEMA (1 instância)               │
│                                                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │ Tenant A │  │ Tenant B │  │ Tenant C │            │
│  │ (Acme)   │  │ (Zeta)   │  │ (Omega)  │            │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘            │
│       │              │              │                   │
│       └──────────────┴──────────────┘                   │
│                      │                                  │
│              ┌───────┴───────┐                          │
│              │  API + DB     │                          │
│              └───────────────┘                          │
└──────────────────────────────────────────────────────────┘
```

### 1.1 Conceito

Diferente de **single-tenancy** (uma instância por cliente), no multi-tenancy o código e a infraestrutura são compartilhados. Os dados são separados por regras de negócio e consultas, não por hardware.

| Característica | Single-Tenant | Multi-Tenant |
|---------------|:-------------:|:------------:|
| Instâncias | 1 por cliente | 1 para todos |
| Código | N versões | 1 versão |
| Banco | N bancos | 1 ou N (controlado) |
| Manutenção | N vezes | 1 vez |
| Isolamento | Físico | Lógico / Físico |

### 1.2 Por que usar?

| Motivo | Descrição |
|--------|-----------|
| **Custo** | Compartilhar infraestrutura reduz drasticamente custos operacionais |
| **Manutenção** | Uma única base de código para atualizar, corrigir e evoluir |
| **Escalabilidade** | Adicionar novos tenants sem provisionar novo ambiente |
| **Time-to-market** | Novo cliente entra em minutos, não semanas ou meses |
| **Atualizações** | Todos os clientes recebem atualização simultaneamente |

### 1.3 Exemplos reais (SaaS)

- **Slack** — cada workspace é um tenant; canais, mensagens e arquivos são isolados
- **Shopify** — cada loja é um tenant; produtos, pedidos e clientes nunca se misturam
- **Notion** — workspaces da equipe com páginas e permissões isoladas
- **GitHub** — organizações e repositórios como unidades de isolamento
- **Salesforce** — o pioneer do multi-tenancy enterprise; cada cliente (org) é um tenant

### 1.4 Quando NÃO usar?

- Clientes exigem compliance físico (dados não podem co-habitar servidor)
- Poucos clientes com volumes massivos de dados
- Clientes exigem versões diferentes do software
- O custo de implementar isolamento lógico supera o de rodar N instâncias

---

## 2. Abordagens de Isolamento

Existem três estratégias principais para isolar dados entre tenants.

### 2.1 Database per Tenant

Cada tenant tem **seu próprio banco de dados**. O roteador de conexão decide qual banco usar com base no tenant identificado.

```
┌──────────────────────────────────────────────┐
│                Connection Router               │
│                                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ DB Acme  │  │ DB Zeta  │  │ DB Omega │    │
│  │ tenant_1 │  │ tenant_2 │  │ tenant_3 │    │
│  └──────────┘  └──────────┘  └──────────┘    │
└──────────────────────────────────────────────┘
```

```typescript
// Router de conexão com lazy initialization
import { Pool } from 'pg';

const tenantDatabases: Record<string, string> = {
  acme: 'postgresql://user:pass@host:5432/acme_db',
  zeta: 'postgresql://user:pass@host:5432/zeta_db',
  omega: 'postgresql://user:pass@host:5432/omega_db',
};

class DatabaseRouter {
  private pools = new Map<string, Pool>();

  getPool(tenantId: string): Pool {
    if (!this.pools.has(tenantId)) {
      const url = tenantDatabases[tenantId];
      if (!url) throw new Error(`Database not found for tenant: ${tenantId}`);

      this.pools.set(
        tenantId,
        new Pool({
          connectionString: url,
          max: 10,
          idleTimeoutMillis: 30000,
        })
      );
    }
    return this.pools.get(tenantId)!;
  }
}
```

**Vantagens:**
- **Isolamento total** — um tenant nunca vê dados do outro, mesmo com SQL injection
- **Backup/restore independente** — pode restaurar um único tenant sem afetar outros
- **SLAs diferenciados** — cada banco pode estar em máquinas de性能 diferentes
- **Migração para instância dedicada** — basta apontar o DNS para o banco existente
- **Compliance** — atende requisitos LGPD/HIPAA que exigem separação física

**Desvantagens:**
- **Custo** — N bancos × licenciamento + infra; 1000 tenants = 1000 bancos
- **Conexões** — N tenants × pool size pode estourar limites do PostgreSQL
- **Migrations** — precisam rodar em N bancos; falha em um tenant bloqueia o deploy
- **Monitoramento** — N bancos para monitorar, N alarmes para configurar
- **Complexidade operacional** — gerenciar N conexões, N backups, N schemas

### 2.2 Schema per Tenant

Um banco de dados compartilhado, mas cada tenant tem seu **próprio schema** (namespace) dentro do banco.

```
┌──────────────────────────────────────────────┐
│              Banco Compartilhado               │
│                                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │schema_a  │  │schema_b  │  │schema_c  │    │
│  │  users   │  │  users   │  │  users   │    │
│  │  orders  │  │  orders  │  │  orders  │    │
│  │  products│  │  products│  │  products│    │
│  └──────────┘  └──────────┘  └──────────┘    │
└──────────────────────────────────────────────┘
```

```sql
-- Criar schema para novo tenant
CREATE SCHEMA IF NOT EXISTS tenant_acme;

-- Tabelas dentro do schema específico
CREATE TABLE tenant_acme.users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  role TEXT NOT NULL DEFAULT 'member',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE tenant_acme.orders (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  customer_id TEXT NOT NULL,
  total NUMERIC(10,2) NOT NULL,
  status TEXT NOT NULL DEFAULT 'pending',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Query com schema dinâmico
SELECT * FROM tenant_acme.users WHERE email = 'joao@acme.com';
```

```typescript
// Abstração para schema dinâmico
class SchemaTenantService {
  constructor(private tenantId: string) {}

  getSchemaName(): string {
    return `tenant_${this.tenantId}`;
  }

  async query<T = any>(sql: string, params?: any[]): Promise<T[]> {
    const schema = this.getSchemaName();
    // Substitui __SCHEMA__ pelo nome real do schema
    const finalSql = sql.replace(/__SCHEMA__/g, `"${schema}"`);
    const result = await pool.query(finalSql, params);
    return result.rows;
  }

  async createTenantSchema(): Promise<void> {
    const schema = this.getSchemaName();
    await pool.query(`CREATE SCHEMA IF NOT EXISTS "${schema}"`);

    // Rodar migrations para este schema
    for (const migration of MIGRATIONS) {
      const sql = migration.sql.replace(/__SCHEMA__/g, `"${schema}"`);
      await pool.query(sql);
    }
  }
}
```

**Vantagens:**
- **Banco único** — uma conexão, pool compartilhado, menos overhead
- **Backup centralizado** — um dump = todos os tenants
- **Custo menor** — uma licença de banco, uma máquina
- **Migrations mais simples** — roda uma vez, altera múltiplos schemas
- **Transações entre schemas** — possível (depende do banco)

**Desvantagens:**
- **Isolamento por schema** — não tão forte quanto DB separado
- **Ruídos between tenants** — queries pesadas de um tenant consomem recursos de todos
- **Recuperação de desastre** — restaurar um tenant específico requer restore do banco inteiro + cleanup
- **Limite de schemas** — PostgreSQL suporta milhares, mas MySQL não tem schemas nativos
- **Conexão única** — um bottleneck na aplicação se todos os tenants estiverem ativos

### 2.3 Shared Database (discriminador)

Um banco, um schema, e uma coluna `tenant_id` em cada tabela como discriminador. O isolamento é **puramente lógico**.

```typescript
// Modelo único com tenant_id
interface User {
  id: string;
  tenant_id: string;        // ← discriminador obrigatório
  name: string;
  email: string;
  role: 'admin' | 'member';
  created_at: Date;
}

interface Order {
  id: string;
  tenant_id: string;        // ← discriminador obrigatório
  customer_name: string;
  total: number;
  status: 'pending' | 'paid' | 'cancelled';
  created_at: Date;
}
```

```typescript
// Repositório que SEMPRE filtra por tenant
class UserRepository {
  constructor(private tenantId: string) {}

  async findAll(): Promise<User[]> {
    return pool.query<User>(
      'SELECT * FROM users WHERE tenant_id = $1 ORDER BY name',
      [this.tenantId]
    ).then(r => r.rows);
  }

  async findById(id: string): Promise<User | null> {
    const result = await pool.query<User>(
      'SELECT * FROM users WHERE id = $1 AND tenant_id = $2',
      [id, this.tenantId]
    );
    return result.rows[0] || null;
  }

  async create(data: Omit<User, 'id' | 'tenant_id' | 'created_at'>): Promise<User> {
    const result = await pool.query<User>(
      `INSERT INTO users (tenant_id, name, email, role)
       VALUES ($1, $2, $3, $4)
       RETURNING *`,
      [this.tenantId, data.name, data.email, data.role]
    );
    return result.rows[0];
  }
}
```

**Vantagens:**
- **Máximo compartilhamento** — um banco, uma conexão, custo mínimo
- **Operação simples** — add tenant = INSERT em tabela `tenants`
- **Performance previsível** — um pool, um plano de execução
- **Migrations tradicionais** — funcionam como em app single-tenant
- **Baixa latência** — sem roteamento de conexão

**Desvantagens:**
- **Menor isolamento** — um `SELECT` sem `WHERE tenant_id = ?` expõe dados de TODOS os tenants
- **SQL injection** — se um invasor consegue injetar SQL, consegue dados de todos
- **Índices inchados** — a tabela cresce com todos os tenants, índices ficam grandes
- **Backup/restore global** — não é possível restaurar um único tenant
- **Difícil diferenciar SLAs** — todos competem pelos mesmos recursos

### 2.4 Comparação Detalhada

| Critério | DB per Tenant | Schema per Tenant | Shared DB |
|----------|:------------:|:-----------------:|:---------:|
| **Isolamento** | ⭐⭐⭐ Físico | ⭐⭐ Lógico (schema) | ⭐ Lógico (linha) |
| **Segurança** | ⭐⭐⭐ | ⭐⭐ | ⭐ |
| **Performance** | ⭐⭐⭐ (dedicado) | ⭐⭐ (compartilhado) | ⭐⭐ (índices grandes) |
| **Custo** | ⭐ (caro) | ⭐⭐ (médio) | ⭐⭐⭐ (barato) |
| **Complexidade** | ⭐⭐ (média) | ⭐⭐⭐ (alta) | ⭐ (baixa) |
| **Migrations** | ⭐ (N execuções) | ⭐⭐ (N schemas) | ⭐⭐⭐ (1 execução) |
| **Backup/Restore** | ⭐⭐⭐ (individual) | ⭐⭐ (global) | ⭐ (só global) |
| **Escalabilidade** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| **Adicionar tenant** | ⭐ (criar DB) | ⭐⭐ (criar schema) | ⭐⭐⭐ (INSERT) |
| **Customização por tenant** | ⭐⭐⭐ | ⭐⭐ | ⭐ |

---

## 3. Análise Aprofundada por Dimensão

### 3.1 Segurança

**Database per Tenant:** Um vazamento de dados de um tenant não afeta os outros. Se um cliente exige compliance específico (LGPD, HIPAA, SOC2), pode-se isolar completamente em nível físico. Ataques de SQL injection ficam contidos no banco do tenant.

**Schema per Tenant:** Um invasor que ganha acesso ao banco pode potencialmente acessar múltiplos schemas. A segurança depende das permissões do usuário do banco (`GRANT USAGE ON SCHEMA`). Idealmente, o usuário da aplicação tem acesso apenas ao schema do tenant atual.

**Shared Database:** Um SQL injection ou bug no `WHERE` expõe **todos os dados de todos os tenants**. Requer:
- Testes de isolamento obrigatórios (ver seção 13)
- Code review com checklist específico
- Row-Level Security (RLS) do PostgreSQL como camada extra

```sql
-- Row-Level Security no PostgreSQL
CREATE TABLE users (
  id UUID PRIMARY KEY,
  tenant_id TEXT NOT NULL,
  name TEXT NOT NULL,
  email TEXT NOT NULL
);

-- Habilitar RLS
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- Política: usuário só vê linhas do seu tenant
CREATE POLICY tenant_isolation ON users
  USING (tenant_id = current_setting('app.tenant_id')::TEXT);

-- Na aplicação, antes de qualquer query:
await pool.query("SET app.tenant_id = 'acme'");
```

### 3.2 Performance

**Database per Tenant:** Cada tenant tem pool isolado. Um tenant com queries pesadas (JOINs complexos, full scans) **não degrada** os outros. Ideal para clientes Enterprise com workloads imprevisíveis.

**Schema per Tenant:** Pool compartilhado. Uma query `SELECT * FROM tenant_big.orders ORDER BY total DESC` pode consumir CPU e I/O, afetando os schemas `tenant_a` e `tenant_c`. Soluções:
- Statement timeout (`SET statement_timeout = '30s'`)
- `pg_terminate_backend` para queries runaway
- Resource queues (Citus, Yugabyte)

**Shared Database:** Todos competem pelo mesmo pool e índices. Queries de um tenant afetam todos. Necessário:
- Rate limiting por tenant
- `pg_stat_statements` para monitorar queries pesadas
- Índices parciais por tenant (se houver padrões distintos)

```sql
-- Índice parcial para tenant com padrão específico
CREATE INDEX idx_orders_acme_large
  ON orders (total DESC)
  WHERE tenant_id = 'acme' AND total > 10000;
```

### 3.3 Custo

| Cenário | DB per Tenant | Schema per Tenant | Shared DB |
|---------|:------------:|:-----------------:|:---------:|
| 10 tenants | 10× RDS db.t3.medium | 1× RDS db.r5.large | 1× RDS db.r5.large |
| Custo/mês | ~$150 | ~$50 | ~$50 |
| 100 tenants | 100× tiny | 1× db.r5.xlarge | 1× db.r5.xlarge |
| Custo/mês | ~$500 | ~$200 | ~$200 |
| 1000 tenants | Inviável | 1× db.r5.2xlarge + sharding | 1× db.r5.4xlarge |
| Custo/mês | — | ~$700 | ~$1400 |

**Database per Tenant** não escala financeiramente além de algumas dezenas de tenants, a menos que cada cliente pague um valor alto que justifique o custo.

### 3.4 Complexidade Operacional

| Operação | DB per Tenant | Schema per Tenant | Shared DB |
|----------|:------------:|:-----------------:|:---------:|
| Adicionar tenant | Criar DB + rodar migrations | Criar schema + rodar migrations | Inserir 1 linha |
| Backup | N backups (1 por DB) | 1 backup do banco | 1 backup do banco |
| Restore individual | Restaurar DB específico | Exportar schema, importar | Impossível |
| Restore total | N restores | 1 restore | 1 restore |
| Upgrade de schema | Roda em N bancos | 1 script para N schemas | 1 script |
| Rollback | Rollback em N bancos | 1 rollback para N schemas | 1 rollback |
| Migração de plano | Sobe de instância | Altera resource limits | Migra para schema/DB |

---

## 4. Identificação do Tenant

O sistema precisa identificar **qual tenant está fazendo a requisição** antes de qualquer lógica de negócio.

### 4.1 Estratégias de Identificação

| Estratégia | Exemplo | Segurança | Complexidade | Ideal para |
|-----------|---------|:---------:|:------------:|-----------|
| **Subdomínio** | `acme.minhasaas.com` | Média | Média | Apps web públicas |
| **Header HTTP** | `X-Tenant-Id: acme` | Média | Baixa | APIs server-to-server |
| **JWT Claim** | `{ "tid": "acme" }` | Alta | Média | Apps autenticadas |
| **Path Parameter** | `/api/acme/users` | Baixa | Baixa | Desenvolvimento/debug |
| **DNS + SSL** | SNI com cert por tenant | Alta | Alta | Enterprise |

### 4.2 Subdomínio

```typescript
// tenant.extractor.ts
function extractTenantFromHost(host: string): string | null {
  // host: "acme.minhasaas.com" → "acme"
  // host: "localhost:3000" → "localhost" (não é tenant)
  const parts = host.split('.');
  if (parts.length < 3) return null; // sem subdomínio
  return parts[0];
}

// Em produção, validar contra lista de tenants permitidos
async function validateTenantSubdomain(
  host: string,
  tenantService: TenantService
): Promise<Tenant | null> {
  const subdomain = extractTenantFromHost(host);
  if (!subdomain) return null;
  return tenantService.findBySubdomain(subdomain);
}
```

### 4.3 Header HTTP

```typescript
// Extração simples e direta
import { Request } from 'express';

const TENANT_HEADER = 'x-tenant-id';

function extractTenantFromHeader(req: Request): string | undefined {
  const tenantId = req.headers[TENANT_HEADER];
  if (Array.isArray(tenantId)) return tenantId[0];
  return tenantId;
}

// Com validação de formato (slug)
const TENANT_SLUG_REGEX = /^[a-z0-9-]{3,50}$/;

function validateTenantSlug(slug: string): boolean {
  return TENANT_SLUG_REGEX.test(slug);
}
```

### 4.4 JWT Claim

```typescript
// Interface do payload
interface TenantJwtPayload {
  sub: string;    // user ID
  tid: string;    // tenant ID
  rol: string;    // role dentro do tenant
  exp: number;    // expiração
}

// Extrair tenant do JWT
import * as jwt from 'jsonwebtoken';

function extractTenantFromJwt(authHeader?: string): string | null {
  if (!authHeader) return null;

  const token = authHeader.replace('Bearer ', '');
  try {
    const payload = jwt.verify(
      token,
      process.env.JWT_SECRET!
    ) as TenantJwtPayload;

    return payload.tid || null;
  } catch {
    return null; // token inválido
  }
}
```

### 4.5 Path Parameter

```typescript
// Útil para debug, mas não recomendado para produção
// Exemplo: GET /api/:tenant/users
@Get('/api/:tenant/users')
findUsers(@Param('tenant') tenantId: string) {
  return this.userService.findAll(tenantId);
}
```

### 4.6 Estratégia Combinada (Fallback)

```typescript
function resolveTenant(req: Request): string {
  // Prioridade: JWT → Header → Subdomínio → Path
  return (
    extractTenantFromJwt(req.headers.authorization) ??
    extractTenantFromHeader(req) ??
    extractTenantFromHost(req.hostname) ??
    extractTenantFromPath(req.path) ??
    (() => { throw new BadRequestException('Tenant não identificado'); })()
  );
}
```

---

## 5. Middleware de Tenant

### 5.1 Implementação com NestJS

```typescript
// tenant.middleware.ts
import { Injectable, NestMiddleware, UnauthorizedException } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';
import * as jwt from 'jsonwebtoken';

interface TenantInfo {
  id: string;
  name: string;
  plan: 'free' | 'pro' | 'enterprise';
  active: boolean;
}

@Injectable()
export class TenantMiddleware implements NestMiddleware {
  constructor() {
    // Em produção, carregar de um cache (Redis) ou banco
    this.loadTenants();
  }

  private tenants = new Map<string, TenantInfo>();

  private loadTenants() {
    this.tenants.set('acme', {
      id: 'acme', name: 'Acme Inc.', plan: 'enterprise', active: true,
    });
    this.tenants.set('zeta', {
      id: 'zeta', name: 'Zeta Ltda.', plan: 'pro', active: true,
    });
    this.tenants.set('omega', {
      id: 'omega', name: 'Omega S.A.', plan: 'free', active: true,
    });
  }

  use(req: Request, res: Response, next: NextFunction) {
    const tenantId = this.extractTenantId(req);
    const tenant = this.tenants.get(tenantId);

    if (!tenant) {
      throw new UnauthorizedException(`Tenant "${tenantId}" não encontrado`);
    }

    if (!tenant.active) {
      throw new UnauthorizedException(`Tenant "${tenantId}" está inativo`);
    }

    // Anexa ao request para uso nos controllers
    (req as any).tenant = tenant;
    (req as any).tenantId = tenant.id;

    next();
  }

  private extractTenantId(req: Request): string {
    const fromJwt = this.extractFromJwt(req.headers.authorization);
    if (fromJwt) return fromJwt;

    const fromHeader = req.headers['x-tenant-id'] as string;
    if (fromHeader) return fromHeader;

    const fromSubdomain = req.hostname.split('.')[0];
    if (fromSubdomain && fromSubdomain !== 'www' && fromSubdomain !== 'app') {
      return fromSubdomain;
    }

    throw new UnauthorizedException(
      'Identificação do tenant é obrigatória (JWT, X-Tenant-Id ou subdomínio)'
    );
  }

  private extractFromJwt(authorization?: string): string | null {
    if (!authorization) return null;
    try {
      const token = authorization.replace('Bearer ', '');
      const payload = jwt.verify(token, process.env.JWT_SECRET!) as any;
      return payload.tid || null;
    } catch {
      return null;
    }
  }
}
```

### 5.2 Aplicação Global ou por Rota

```typescript
// app.module.ts
import { Module, NestModule, MiddlewareConsumer } from '@nestjs/common';
import { TenantMiddleware } from './tenant/tenant.middleware';

@Module({
  imports: [TenantModule],
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer
      .apply(TenantMiddleware)
      .exclude(
        'auth/(.*)',   // login não precisa de tenant
        'health',       // health check
        'public/(.*)',  // páginas públicas
      )
      .forRoutes('*');
  }
}
```

### 5.3 TenantModule

```typescript
// tenant.module.ts
import { Global, Module } from '@nestjs/common';
import { TenantService } from './tenant.service';
import { TenantMiddleware } from './tenant.middleware';

@Global() // disponível em toda a aplicação
@Module({
  providers: [TenantService, TenantMiddleware],
  exports: [TenantService],
})
export class TenantModule {}
```

### 5.4 TenantService

```typescript
// tenant.service.ts
import { Injectable, Scope } from '@nestjs/common';

interface Tenant {
  id: string;
  name: string;
  plan: 'free' | 'pro' | 'enterprise';
}

@Injectable({ scope: Scope.REQUEST })
export class TenantService {
  private tenant!: Tenant;

  setTenant(tenant: Tenant) {
    this.tenant = tenant;
  }

  getTenant(): Tenant {
    if (!this.tenant) {
      throw new Error('Tenant não configurado para esta requisição');
    }
    return this.tenant;
  }

  getTenantId(): string {
    return this.getTenant().id;
  }

  getPlan(): string {
    return this.getTenant().plan;
  }

  isEnterprise(): boolean {
    return this.getPlan() === 'enterprise';
  }
}
```

### 5.5 @Tenant() Decorator

```typescript
// tenant.decorator.ts
import { createParamDecorator, ExecutionContext } from '@nestjs/common';

export const Tenant = createParamDecorator(
  (data: keyof Tenant | undefined, ctx: ExecutionContext) => {
    const request = ctx.switchToHttp().getRequest();
    const tenant = request.tenant;

    if (!tenant) {
      throw new Error('Tenant não encontrado no request. TenantMiddleware está configurado?');
    }

    return data ? tenant[data] : tenant;
  }
);

// Uso no controller
@Get('users')
findAll(@Tenant() tenant: Tenant) {
  return this.userService.findAll(tenant.id);
}

@Get('plan')
getPlan(@Tenant('plan') plan: string) {
  return { plan };
}
```

### 5.6 AsyncLocalStorage para Contexto

```typescript
// tenant-context.ts
import { AsyncLocalStorage } from 'async_hooks';

export interface TenantContext {
  tenantId: string;
  tenantName: string;
  plan: string;
}

export const tenantContext = new AsyncLocalStorage<TenantContext>();

// tenant-context.middleware.ts
import { Injectable, NestMiddleware } from '@nestjs/common';

@Injectable()
export class TenantContextMiddleware implements NestMiddleware {
  use(req: any, res: any, next: () => void) {
    const context: TenantContext = {
      tenantId: req.tenantId,
      tenantName: req.tenant?.name,
      plan: req.tenant?.plan,
    };

    tenantContext.run(context, () => next());
  }
}

// Uso em qualquer parte do código
import { tenantContext } from './tenant-context';

function getCurrentTenantId(): string {
  const ctx = tenantContext.getStore();
  if (!ctx) throw new Error('Fora de contexto de tenant');
  return ctx.tenantId;
}
```

---

## 6. Prisma Multi-Tenant

### 6.1 Schema per Tenant com Prisma

```prisma
// schema.prisma — modelo base
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

// Modelo compartilhado (global)
model Tenant {
  id        String   @id @default(uuid())
  slug      String   @unique
  name      String
  plan      String   @default("free")
  active    Boolean  @default(true)
  createdAt DateTime @default(now()) @map("created_at")
  @@map("tenants")
}

// Modelos por tenant (Prisma não suporta schema dinâmico nativamente)
// Solução: Client per tenant
model User {
  id        String   @id @default(uuid())
  name      String
  email     String   @unique
  role      String   @default("member")
  createdAt DateTime @default(now()) @map("created_at")
  @@map("users")
}

model Project {
  id        String   @id @default(uuid())
  name      String
  createdAt DateTime @default(now()) @map("created_at")
  @@map("projects")
}
```

```typescript
// prisma-multi-tenant.ts
import { PrismaClient } from '@prisma/client';

class PrismaTenantManager {
  private clients = new Map<string, PrismaClient>();

  getClient(schema: string): PrismaClient {
    if (!this.clients.has(schema)) {
      const url = new URL(process.env.DATABASE_URL!);
      url.searchParams.set('schema', schema);

      const client = new PrismaClient({
        datasources: {
          db: { url: url.toString() },
        },
      });

      this.clients.set(schema, client);
    }
    return this.clients.get(schema)!;
  }

  async closeAll(): Promise<void> {
    for (const [schema, client] of this.clients) {
      await client.$disconnect();
    }
  }
}

export const prismaTenantManager = new PrismaTenantManager();
```

### 6.2 Shared Database com Prisma

```prisma
// schema.prisma — shared database
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

model Order {
  id        String   @id @default(uuid())
  tenantId  String   @map("tenant_id")
  total     Decimal  @db.Decimal(10, 2)
  status    String   @default("pending")
  createdAt DateTime @default(now()) @map("created_at")

  @@index([tenantId, createdAt])
  @@map("orders")
}
```

```typescript
// tenant-aware.service.ts
import { Injectable } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';
import { TenantService } from './tenant.service';

@Injectable()
export class TenantAwareService {
  constructor(
    private prisma: PrismaService,
    private tenantService: TenantService,
  ) {}

  private get tenantId() {
    return this.tenantService.getTenantId();
  }

  async findUsers() {
    return this.prisma.user.findMany({
      where: { tenantId: this.tenantId },
    });
  }

  async createUser(data: { name: string; email: string; role?: string }) {
    return this.prisma.user.create({
      data: {
        ...data,
        tenantId: this.tenantId,
      },
    });
  }

  async findOrdersByDateRange(start: Date, end: Date) {
    return this.prisma.order.findMany({
      where: {
        tenantId: this.tenantId,
        createdAt: { gte: start, lte: end },
      },
      orderBy: { createdAt: 'desc' },
    });
  }
}
```

### 6.3 Prisma Middleware para Tenant

```typescript
// prisma-tenant.middleware.ts
import { PrismaClient } from '@prisma/client';
import { tenantContext } from './tenant-context';

export function createTenantMiddleware(prisma: PrismaClient): void {
  prisma.$use(async (params, next) => {
    const ctx = tenantContext.getStore();
    if (!ctx) return next(params);

    // Adiciona tenantId automaticamente em creates
    if (params.action === 'create' && params.args.data) {
      params.args.data.tenantId = ctx.tenantId;
    }

    // Adiciona filtro de tenant em finds
    if (
      ['findMany', 'findFirst', 'findUnique', 'update', 'delete'].includes(params.action)
    ) {
      const where = params.args.where ?? {};
      where.tenantId = ctx.tenantId;
      params.args.where = where;
    }

    return next(params);
  });
}

// Inicialização
const prisma = new PrismaClient();
createTenantMiddleware(prisma);
```

### 6.4 Prisma Extension (Prisma >= 5.0)

```typescript
// tenant.extension.ts
import { PrismaClient } from '@prisma/client';
import { tenantContext } from './tenant-context';

export const tenantExtension = Prisma.defineExtension((client) => {
  return client.$extends({
    query: {
      $allModels: {
        async $allOperations({ model, operation, args, query }) {
          const ctx = tenantContext.getStore();

          if (ctx && ['create', 'createMany'].includes(operation)) {
            args.data = { ...args.data, tenantId: ctx.tenantId };
          }

          if (ctx && ['findMany', 'findFirst', 'update', 'delete'].includes(operation)) {
            args.where = { ...args.where, tenantId: ctx.tenantId };
          }

          return query(args);
        },
      },
    },
  });
});

// Uso
const prisma = new PrismaClient().$extends(tenantExtension);
```

---

## 7. Migrations Multi-Tenant

### 7.1 Database per Tenant

```typescript
// migrate-all-tenants.ts
import { Pool } from 'pg';
import { readMigrationFiles } from './migration-runner';

async function migrateAllTenants(): Promise<void> {
  const tenants = [
    { id: 'acme', dbUrl: 'postgresql://.../acme' },
    { id: 'zeta', dbUrl: 'postgresql://.../zeta' },
    { id: 'omega', dbUrl: 'postgresql://.../omega' },
  ];

  const migrations = await readMigrationFiles();

  for (const tenant of tenants) {
    console.log(`[${tenant.id}] Iniciando migrations...`);
    const pool = new Pool({ connectionString: tenant.dbUrl });

    try {
      for (const migration of migrations) {
        await pool.query('BEGIN');
        try {
          await pool.query(migration.sql);
          await pool.query(
            `INSERT INTO _migrations (name, applied_at) VALUES ($1, NOW())`,
            [migration.name]
          );
          await pool.query('COMMIT');
          console.log(`[${tenant.id}] ✅ ${migration.name}`);
        } catch (err) {
          await pool.query('ROLLBACK');
          console.error(`[${tenant.id}] ❌ ${migration.name}:`, err);
          throw err; // abortar todos? ou continuar?
        }
      }
    } finally {
      await pool.end();
    }
  }
}
```

### 7.2 Schema per Tenant

```typescript
// schema-migration-runner.ts
const pool = new Pool({ connectionString: process.env.DATABASE_URL });

const MIGRATIONS = [
  {
    name: '001_create_users',
    sql: `
      CREATE TABLE IF NOT EXISTS __SCHEMA__.users (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'member',
        created_at TIMESTAMPTZ DEFAULT NOW()
      );
    `,
  },
  {
    name: '002_add_phone',
    sql: `
      ALTER TABLE __SCHEMA__.users
      ADD COLUMN IF NOT EXISTS phone TEXT;
    `,
  },
  {
    name: '003_create_projects',
    sql: `
      CREATE TABLE IF NOT EXISTS __SCHEMA__.projects (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        name TEXT NOT NULL,
        description TEXT,
        created_at TIMESTAMPTZ DEFAULT NOW()
      );
    `,
  },
];

async function migrateSchema(schema: string): Promise<void> {
  const client = await pool.connect();

  try {
    // Criar schema se não existe
    await client.query(`CREATE SCHEMA IF NOT EXISTS "${schema}"`);

    // Criar tabela de controle de migrations no schema
    await client.query(`
      CREATE TABLE IF NOT EXISTS "${schema}"._migrations (
        name TEXT PRIMARY KEY,
        applied_at TIMESTAMPTZ DEFAULT NOW()
      )
    `);

    for (const migration of MIGRATIONS) {
      // Verificar se já foi aplicada
      const exists = await client.query(
        `SELECT 1 FROM "${schema}"._migrations WHERE name = $1`,
        [migration.name]
      );

      if (exists.rows.length > 0) continue;

      // Aplicar migration
      const sql = migration.sql.replace(/__SCHEMA__/g, `"${schema}"`);
      await client.query('BEGIN');
      try {
        await client.query(sql);
        await client.query(
          `INSERT INTO "${schema}"._migrations (name) VALUES ($1)`,
          [migration.name]
        );
        await client.query('COMMIT');
        console.log(`[${schema}] ✅ ${migration.name}`);
      } catch (err) {
        await client.query('ROLLBACK');
        throw err;
      }
    }
  } finally {
    client.release();
  }
}

async function migrateAllSchemas(): Promise<void> {
  const tenants = await pool.query('SELECT slug FROM tenants WHERE active = true');
  for (const tenant of tenants.rows) {
    await migrateSchema(`tenant_${tenant.slug}`);
  }
}
```

### 7.3 Estratégias de Rollback

```typescript
// migrate-with-transaction.ts
async function migrateTenantWithTransaction(
  tenantId: string,
  migrationSql: string
): Promise<void> {
  const schema = `tenant_${tenantId}`;
  const client = await pool.connect();

  try {
    await client.query('BEGIN');

    // Isolar a transação no schema do tenant
    await client.query(`SET search_path TO "${schema}"`);

    await client.query(migrationSql);
    await client.query(`INSERT INTO _migrations (name) VALUES ($1)`, [
      '004_add_status',
    ]);

    await client.query('COMMIT');
    console.log(`[${tenantId}] Migration aplicada com sucesso`);
  } catch (error) {
    await client.query('ROLLBACK');
    console.error(`[${tenantId}] Migration falhou, rollback executado`);
    throw error;
  } finally {
    client.release();
  }
}
```

### 7.4 Shared Database

```typescript
// shared-migration.ts
// Migrations tradicionais — funcionam como app single-tenant

async function migrateShared(): Promise<void> {
  const client = await pool.connect();
  try {
    await client.query('BEGIN');

    // Adicionar coluna tenant_id se não existe
    await client.query(`
      ALTER TABLE users
      ADD COLUMN IF NOT EXISTS tenant_id TEXT NOT NULL DEFAULT 'default'
    `);

    // Índices compostos para performance
    await client.query(`
      CREATE INDEX IF NOT EXISTS idx_users_tenant_email
      ON users (tenant_id, email)
    `);

    await client.query(`
      CREATE INDEX IF NOT EXISTS idx_orders_tenant_created
      ON orders (tenant_id, created_at DESC)
    `);

    await client.query('COMMIT');
  } catch (error) {
    await client.query('ROLLBACK');
    throw error;
  } finally {
    client.release();
  }
}
```

---

## 8. Dados Compartilhados vs Por Tenant

### 8.1 Tabelas Globais (Compartilhadas)

Dados que **não pertencem a nenhum tenant específico** e são comuns a todos:

```typescript
// Globais — uma única instância para o sistema todo
interface Plan {
  id: string;
  name: string;              // "Free", "Pro", "Enterprise"
  maxUsers: number;
  maxStorage: number;        // MB
  monthlyPrice: number;
  features: string[];        // ["api_access", "custom_domain", "advanced_reports"]
}

interface FeatureFlag {
  id: string;
  key: string;               // "audit_log"
  description: string;
  enabledByDefault: boolean;
}

interface SystemConfig {
  key: string;               // "max_upload_size_mb"
  value: string;
  description: string;
}

interface AuditLog {
  id: string;
  tenantId: string;
  action: string;
  userId: string;
  metadata: JSON;
  createdAt: Date;
}
```

### 8.2 Tabelas Por Tenant (Isoladas)

Dados que **pertencem a um tenant específico** e devem ser isolados:

```typescript
// Isoladas por tenant
interface User {
  id: string;
  tenantId: string;          // FK implícita para o tenant
  name: string;
  email: string;
  role: 'admin' | 'member' | 'viewer';
  createdAt: Date;
}

interface Project {
  id: string;
  tenantId: string;
  name: string;
  description?: string;
  status: 'active' | 'archived';
  createdAt: Date;
}

interface Task {
  id: string;
  tenantId: string;
  projectId: string;
  title: string;
  assigneeId?: string;
  status: 'todo' | 'doing' | 'done';
  createdAt: Date;
}

interface Invoice {
  id: string;
  tenantId: string;
  number: string;
  amount: number;
  status: 'pending' | 'paid' | 'cancelled';
  dueDate: Date;
}
```

### 8.3 Regra Prática

```
┌─────────────────────────────────────────────────────┐
│              DADOS GLOBAIS (shared)                  │
│                                                      │
│  • Planos e preços          • Feature flags          │
│  • Configurações do sistema  • Templates              │
│  • Catálogo de integrações   • Regiões/Países        │
│  • Auditoria centralizada    • Webhooks system        │
├─────────────────────────────────────────────────────┤
│              DADOS POR TENANT (isolados)             │
│                                                      │
│  • Usuários e permissões     • Projetos e tarefas    │
│  • Faturas e pagamentos      • Produtos e catálogo   │
│  • Configurações do tenant   • Logs de atividade     │
│  • Arquivos e uploads        • Relatórios gerados    │
└─────────────────────────────────────────────────────┘
```

### 8.4 Implementação em Schema per Tenant

```sql
-- Schema global (público)
CREATE SCHEMA IF NOT EXISTS public;

CREATE TABLE public.plans (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  max_users INT NOT NULL,
  monthly_price NUMERIC(10,2) NOT NULL,
  features JSONB NOT NULL DEFAULT '[]'
);

CREATE TABLE public.tenants (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  slug TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  plan_id UUID REFERENCES public.plans(id),
  active BOOLEAN DEFAULT true,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Schema do tenant
CREATE SCHEMA IF NOT EXISTS tenant_acme;

CREATE TABLE tenant_acme.users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id UUID REFERENCES public.tenants(id),
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  role TEXT NOT NULL DEFAULT 'member',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Query que cruza dado global com dado do tenant
SELECT u.name, p.name as plan_name
FROM tenant_acme.users u
JOIN public.tenants t ON t.id = u.tenant_id
JOIN public.plans p ON p.id = t.plan_id
WHERE u.email = 'joao@acme.com';
```

---

## 9. Seed por Tenant

### 9.1 Seed Automático ao Criar Tenant

```typescript
// tenant-seed.ts
async function seedNewTenant(tenantSlug: string, plan: string): Promise<void> {
  const schema = `tenant_${tenantSlug}`;
  const client = await pool.connect();

  try {
    await client.query(`CREATE SCHEMA IF NOT EXISTS "${schema}"`);

    // 1. Migrations básicas
    await client.query(`
      CREATE TABLE IF NOT EXISTS "${schema}".users (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'member',
        created_at TIMESTAMPTZ DEFAULT NOW()
      )
    `);

    await client.query(`
      CREATE TABLE IF NOT EXISTS "${schema}".projects (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        name TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'active',
        created_at TIMESTAMPTZ DEFAULT NOW()
      )
    `);

    await client.query(`
      CREATE TABLE IF NOT EXISTS "${schema}".settings (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL
      )
    `);

    // 2. Seed data padrão
    await client.query(`
      INSERT INTO "${schema}".users (name, email, role)
      VALUES ('Admin', 'admin@${tenantSlug}.com', 'admin')
    `);

    await client.query(`
      INSERT INTO "${schema}".settings (key, value) VALUES
        ('locale', 'pt-BR'),
        ('timezone', 'America/Sao_Paulo'),
        ('notification_email', 'true'),
        ('max_upload_size_mb', '10'),
        ('default_language', 'pt')
    `);

    // 3. Dados condicionais por plano
    if (plan === 'enterprise') {
      await client.query(`
        INSERT INTO "${schema}".settings (key, value) VALUES
          ('custom_domain', ''),
          ('sso_enabled', 'true'),
          ('audit_log_retention_days', '365')
      `);
    }

    console.log(`[${tenantSlug}] Seed concluído`);
  } catch (error) {
    console.error(`[${tenantSlug}] Seed falhou:`, error);
    throw error;
  } finally {
    client.release();
  }
}

// Hook na criação do tenant
async function createTenant(data: { slug: string; name: string; plan: string }) {
  const result = await pool.query(
    `INSERT INTO tenants (slug, name, plan_id)
     VALUES ($1, $2, (SELECT id FROM plans WHERE name = $3))
     RETURNING *`,
    [data.slug, data.name, data.plan]
  );

  const tenant = result.rows[0];
  await seedNewTenant(tenant.slug, data.plan);

  return tenant;
}
```

### 9.2 Comandos CLI (NestJS Command)

```typescript
// tenant.command.ts
import { Command, CommandRunner } from 'nest-commander';
import { TenantService } from './tenant.service';

@Command({ name: 'tenant:create', description: 'Cria novo tenant com seed' })
export class TenantCommand extends CommandRunner {
  constructor(private tenantService: TenantService) {
    super();
  }

  async run(inputs: string[]): Promise<void> {
    const [slug, name, plan = 'free'] = inputs;

    if (!slug || !name) {
      console.error('Uso: tenant:create <slug> <name> [plan]');
      process.exit(1);
    }

    console.log(`Criando tenant: ${slug} (${name}) - Plano: ${plan}`);
    const tenant = await this.tenantService.createTenant({ slug, name, plan });
    console.log(`✅ Tenant ${tenant.slug} criado com sucesso!`);
  }
}
```

### 9.3 Idempotência

```typescript
// Seeds devem ser idempotentes (podem rodar múltiplas vezes)
async function seedSettingsIfNotExists(schema: string): Promise<void> {
  const defaultSettings = [
    { key: 'locale', value: 'pt-BR' },
    { key: 'timezone', value: 'America/Sao_Paulo' },
    { key: 'notification_email', value: 'true' },
  ];

  for (const setting of defaultSettings) {
    await pool.query(`
      INSERT INTO "${schema}".settings (key, value)
      VALUES ($1, $2)
      ON CONFLICT (key) DO NOTHING
    `, [setting.key, setting.value]);
  }
}
```

---

## 10. Backup e Restore

### 10.1 Database per Tenant

```bash
#!/bin/bash
# backup-all-tenants.sh — backup individual por tenant

TENANTS=("acme" "zeta" "omega")
DATE=$(date +%Y%m%d_%H%M)
BACKUP_DIR="./backups"

mkdir -p "$BACKUP_DIR"

for TENANT in "${TENANTS[@]}"; do
  echo "Iniciando backup do tenant: $TENANT"

  pg_dump "postgresql://user:pass@localhost:5432/${TENANT}_db" \
    --format=custom \
    --compress=9 \
    --file="${BACKUP_DIR}/${TENANT}_${DATE}.dump"

  if [ $? -eq 0 ]; then
    echo "✅ Backup de $TENANT concluído: ${BACKUP_DIR}/${TENANT}_${DATE}.dump"
  else
    echo "❌ Falha no backup de $TENANT"
  fi
done

# Restore individual
# pg_restore --dbname=postgresql://user:pass@localhost:5432/acme_db \
#   --clean --if-exists \
#   backups/acme_20240101.dump
```

### 10.2 Schema per Tenant — Backup Seletivo

```bash
#!/bin/bash
# backup-schema.sh — backup de schema específico

TENANT=$1
DATE=$(date +%Y%m%d)

if [ -z "$TENANT" ]; then
  echo "Uso: $0 <tenant_slug>"
  exit 1
fi

DB_URL="postgresql://user:pass@localhost:5432/shared_db"

# Backup do schema específico (PostgreSQL 15+)
pg_dump "$DB_URL" \
  --schema="tenant_${TENANT}" \
  --format=custom \
  --compress=9 \
  --file="backups/schema_${TENANT}_${DATE}.dump"

echo "✅ Schema tenant_${TENANT} salvo em backups/schema_${TENANT}_${DATE}.dump"

# Restore
# pg_restore "$DB_URL" \
#   --schema="tenant_${TENANT}" \
#   --clean \
#   backups/schema_zeta_20240101.dump
```

### 10.3 Estratégia por Plano

| Plano | Backup | RPO (Recovery Point Objective) | RTO (Recovery Time Objective) |
|-------|--------|:-----------------------------:|:-----------------------------:|
| **Free** | Diário compartilhado | 24h | 4h |
| **Pro** | Diário + WAL archiving (PITR) | 1h | 1h |
| **Enterprise** | Backup dedicado + PITR + réplica | 5min | 15min |

```typescript
// backup-scheduler.ts
interface BackupPolicy {
  type: 'shared' | 'dedicated' | 'pitr';
  frequency: string;        // cron expression
  retentionDays: number;
}

const planBackupPolicies: Record<string, BackupPolicy> = {
  free:    { type: 'shared',   frequency: '0 2 * * *', retentionDays: 7 },
  pro:     { type: 'pitr',     frequency: '0 */6 * * *', retentionDays: 30 },
  enterprise: { type: 'dedicated', frequency: '0 */1 * * *', retentionDays: 90 },
};

async function scheduleTenantBackup(tenant: { id: string; plan: string }): Promise<void> {
  const policy = planBackupPolicies[tenant.plan];

  switch (policy.type) {
    case 'shared':
      // Backup global já cobre
      console.log(`[${tenant.id}] Coberto pelo backup global`);
      break;

    case 'pitr':
      // WAL archiving + backups periódicos
      await enablePITR(tenant.id);
      break;

    case 'dedicated':
      // Backup individual do banco/schema
      await runFullBackup(tenant.id);
      break;
  }
}
```

---

## 11. Performance

### 11.1 Connection Pooling por Tenant

```typescript
// pool-manager.ts
import { Pool } from 'pg';

interface PoolConfig {
  max: number;
  idleTimeoutMillis: number;
  connectionTimeoutMillis: number;
}

const PLAN_POOL_LIMITS: Record<string, number> = {
  free: 2,
  pro: 10,
  enterprise: 25,
};

class PoolManager {
  private pools = new Map<string, { pool: Pool; lastUsed: number; config: PoolConfig }>();

  getPool(tenantId: string, plan: string = 'free'): Pool {
    const existing = this.pools.get(tenantId);
    if (existing) {
      existing.lastUsed = Date.now();
      return existing.pool;
    }

    const config: PoolConfig = {
      max: PLAN_POOL_LIMITS[plan] || 5,
      idleTimeoutMillis: 30000,
      connectionTimeoutMillis: 5000,
    };

    const pool = new Pool({
      connectionString: this.getTenantDbUrl(tenantId),
      ...config,
    });

    pool.on('error', (err) => {
      console.error(`Pool error for tenant ${tenantId}:`, err);
      this.pools.delete(tenantId);
    });

    this.pools.set(tenantId, { pool, lastUsed: Date.now(), config });
    return pool;
  }

  private getTenantDbUrl(tenantId: string): string {
    // Em schema per tenant: mesma URL
    // Em DB per tenant: URL diferente por tenant
    return process.env.DATABASE_URL!;
  }

  async closeIdlePools(maxIdleMs: number = 300000): Promise<void> {
    const now = Date.now();
    for (const [id, entry] of this.pools) {
      if (now - entry.lastUsed > maxIdleMs) {
        await entry.pool.end();
        this.pools.delete(id);
        console.log(`Pool do tenant ${id} fechado por inatividade`);
      }
    }
  }

  async closeAll(): Promise<void> {
    for (const [id, entry] of this.pools) {
      await entry.pool.end();
    }
    this.pools.clear();
  }

  getStats(): Record<string, { totalCount: number; idleCount: number; waitingCount: number }> {
    const stats: any = {};
    for (const [id, entry] of this.pools) {
      stats[id] = {
        totalCount: entry.pool.totalCount,
        idleCount: entry.pool.idleCount,
        waitingCount: entry.pool.waitingCount,
      };
    }
    return stats;
  }
}

export const poolManager = new PoolManager();
```

### 11.2 Query Optimization

```typescript
// query-optimizer.ts
class QueryOptimizer {
  constructor(private tenantId: string, private plan: string) {}

  async findOrders(start: Date, end: Date): Promise<Order[]> {
    const baseQuery = `
      SELECT * FROM orders
      WHERE tenant_id = $1
        AND created_at BETWEEN $2 AND $3
    `;

    // Enterprise: busca completa
    if (this.plan === 'enterprise') {
      return pool.query(baseQuery + ' ORDER BY created_at DESC', [
        this.tenantId, start, end,
      ]).then(r => r.rows);
    }

    // Free/Pro: paginado
    return pool.query(baseQuery + ' ORDER BY created_at DESC LIMIT 100', [
      this.tenantId, start, end,
    ]).then(r => r.rows);
  }
}
```

### 11.3 Rate Limiting por Tenant

```typescript
// tenant-rate-limiter.ts
import { Injectable } from '@nestjs/common';

interface RateLimitConfig {
  requestsPerMinute: number;
  concurrentRequests: number;
}

const PLAN_LIMITS: Record<string, RateLimitConfig> = {
  free:       { requestsPerMinute: 100,  concurrentRequests: 5 },
  pro:        { requestsPerMinute: 1000, concurrentRequests: 25 },
  enterprise: { requestsPerMinute: 10000, concurrentRequests: 100 },
};

@Injectable()
export class TenantRateLimiter {
  private requestCounts = new Map<string, { count: number; windowStart: number }>();
  private concurrentCounts = new Map<string, number>();

  async checkRateLimit(tenantId: string, plan: string): Promise<void> {
    const limits = PLAN_LIMITS[plan] || PLAN_LIMITS.free;
    const now = Date.now();
    const windowMs = 60_000; // 1 minuto

    // Rate limit
    const entry = this.requestCounts.get(tenantId) ?? { count: 0, windowStart: now };

    if (now - entry.windowStart > windowMs) {
      entry.count = 0;
      entry.windowStart = now;
    }

    entry.count++;
    this.requestCounts.set(tenantId, entry);

    if (entry.count > limits.requestsPerMinute) {
      throw new Error(`Rate limit excedido para tenant ${tenantId}. Limite: ${limits.requestsPerMinute}/min`);
    }

    // Concurrent requests
    const concurrent = this.concurrentCounts.get(tenantId) ?? 0;
    this.concurrentCounts.set(tenantId, concurrent + 1);

    if (concurrent + 1 > limits.concurrentRequests) {
      this.concurrentCounts.set(tenantId, concurrent);
      throw new Error(`Muitas requisições concorrentes para tenant ${tenantId}. Limite: ${limits.concurrentRequests}`);
    }
  }

  releaseConcurrent(tenantId: string): void {
    const current = this.concurrentCounts.get(tenantId) ?? 1;
    this.concurrentCounts.set(tenantId, Math.max(0, current - 1));
  }
}
```

### 11.4 Indexação para Shared Database

```sql
-- Índices essenciais para shared database

-- 1. Sempre incluir tenant_id como primeira coluna
CREATE INDEX idx_users_tenant_id ON users (tenant_id);
CREATE INDEX idx_users_tenant_email ON users (tenant_id, email);
CREATE INDEX idx_orders_tenant_created ON orders (tenant_id, created_at DESC);

-- 2. Índices parciais para tenants grandes
CREATE INDEX idx_orders_acme_pending ON orders (created_at)
  WHERE tenant_id = 'acme' AND status = 'pending';

-- 3. Índices funcionais para queries comuns
CREATE INDEX idx_users_tenant_lower_email ON users (tenant_id, LOWER(email));

-- 4. Evitar índices desnecessários em colunas de baixa cardinalidade
-- (tenant_id já é primeiro no índice composto)

-- Query que usa o índice:
EXPLAIN ANALYZE
SELECT * FROM users
WHERE tenant_id = 'acme' AND email = 'joao@acme.com';
-- -> Index Scan usando idx_users_tenant_email
```

---

## 12. Pricing Baseado em Tenancy

### 12.1 Modelo de Planos

A arquitetura de isolamento escolhida define diretamente o que pode ser oferecido em cada plano:

| Plano | Isolamento | Limites | Preço | Público |
|-------|-----------|---------|-------|---------|
| **Free** | Shared DB | 5 usuários, 10 projetos, 100 MB | Grátis | Teste / pequenas equipes |
| **Pro** | Schema per Tenant | 50 usuários, 100 projetos, 5 GB | $29/mês | PMEs |
| **Business** | Schema per Tenant (dedicado) | 200 usuários, 500 projetos, 50 GB | $99/mês | Médias empresas |
| **Enterprise** | DB per Tenant + Réplica | Ilimitado | $499/mês | Grandes clientes |

### 12.2 Feature Flags por Plano

```typescript
// feature-flags.ts
interface PlanFeatures {
  maxUsers: number;
  maxProjects: number;
  maxStorageMB: number;
  customDomain: boolean;
  apiAccess: boolean;
  advancedReports: boolean;
  auditLog: boolean;
  prioritySupport: boolean;
  ssoEnabled: boolean;
  whiteLabel: boolean;
}

const PLANS: Record<string, PlanFeatures> = {
  free: {
    maxUsers: 5,
    maxProjects: 10,
    maxStorageMB: 100,
    customDomain: false,
    apiAccess: false,
    advancedReports: false,
    auditLog: false,
    prioritySupport: false,
    ssoEnabled: false,
    whiteLabel: false,
  },
  pro: {
    maxUsers: 50,
    maxProjects: 100,
    maxStorageMB: 5_000,
    customDomain: false,
    apiAccess: true,
    advancedReports: true,
    auditLog: true,
    prioritySupport: false,
    ssoEnabled: false,
    whiteLabel: false,
  },
  enterprise: {
    maxUsers: Infinity,
    maxProjects: Infinity,
    maxStorageMB: Infinity,
    customDomain: true,
    apiAccess: true,
    advancedReports: true,
    auditLog: true,
    prioritySupport: true,
    ssoEnabled: true,
    whiteLabel: true,
  },
};
```

```typescript
// feature-flag.service.ts
import { Injectable } from '@nestjs/common';
import { TenantService } from './tenant.service';

@Injectable()
export class FeatureFlagService {
  constructor(private tenantService: TenantService) {}

  private get planFeatures(): PlanFeatures {
    const plan = this.tenantService.getPlan();
    return PLANS[plan] || PLANS.free;
  }

  isFeatureEnabled(feature: keyof PlanFeatures): boolean {
    const value = this.planFeatures[feature];
    return typeof value === 'boolean' ? value : false;
  }

  getLimit(resource: 'maxUsers' | 'maxProjects' | 'maxStorageMB'): number {
    const value = this.planFeatures[resource];
    return typeof value === 'number' ? value : Infinity;
  }

  async checkLimit(resource: 'maxUsers' | 'maxProjects' | 'maxStorageMB'): Promise<void> {
    const limit = this.getLimit(resource);
    if (limit === Infinity) return;

    const current = await this.getCurrentUsage(resource);
    if (current >= limit) {
      throw new Error(
        `Limite de ${resource} excedido (${current}/${limit}). Faça upgrade do plano.`
      );
    }
  }

  private async getCurrentUsage(resource: string): Promise<number> {
    const tenantId = this.tenantService.getTenantId();
    // Consultar banco para contagem atual
    switch (resource) {
      case 'maxUsers':
        return /* COUNT de users do tenant */ 3;
      case 'maxProjects':
        return /* COUNT de projects do tenant */ 7;
      case 'maxStorageMB':
        return /* SUM de tamanho de arquivos */ 50;
      default:
        return 0;
    }
  }

  getAllFeatures(): PlanFeatures {
    return { ...this.planFeatures };
  }
}
```

### 12.3 Guard do NestJS para Feature Flags

```typescript
// feature.guard.ts
import { Injectable, CanActivate, ExecutionContext } from '@nestjs/common';
import { FeatureFlagService } from './feature-flag.service';

@Injectable()
export class FeatureGuard implements CanActivate {
  constructor(
    private featureFlagService: FeatureFlagService,
    private featureName: keyof PlanFeatures,
  ) {}

  canActivate(context: ExecutionContext): boolean {
    return this.featureFlagService.isFeatureEnabled(this.featureName);
  }
}

// Uso no controller
@Get('reports/advanced')
@UseGuards(new FeatureGuard('advancedReports'))
getAdvancedReports() {
  // Só executa se o plano do tenant tiver advancedReports = true
  return this.reportService.generate();
}
```

---

## 13. Testes de Isolamento entre Tenants

### 13.1 Configuração de Teste

```typescript
// tenant-isolation.spec.ts
import { Test, TestingModule } from '@nestjs/testing';
import { INestApplication } from '@nestjs/common';
import * as request from 'supertest';
import { AppModule } from '../src/app.module';
import { TenantService } from '../src/tenant/tenant.service';

describe('Isolamento entre Tenants', () => {
  let app: INestApplication;

  beforeAll(async () => {
    const moduleFixture: TestingModule = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();

    app = moduleFixture.createNestApplication();
    await app.init();
  });

  afterAll(async () => {
    await app.close();
  });

  // Helper para atuar como um tenant específico
  const asTenant = (tenantId: string) => {
    const token = generateJwt({ sub: 'user1', tid: tenantId });
    return request(app.getHttpServer())
      .set('Authorization', `Bearer ${token}`)
      .set('X-Tenant-Id', tenantId);
  };

  function generateJwt(payload: any): string {
    const jwt = require('jsonwebtoken');
    return jwt.sign(payload, process.env.JWT_SECRET || 'test-secret');
  }
```

### 13.2 Teste 1: Vazamento Zero

```typescript
  describe('Vazamento de dados', () => {
    it('Tenant A não deve ver dados do Tenant B', async () => {
      // Arrange: criar dados como Tenant A
      await asTenant('acme')
        .post('/users')
        .send({ name: 'João Silva', email: 'joao@acme.com' })
        .expect(201);

      // Act: listar usuários como Tenant B
      const response = await asTenant('zeta')
        .get('/users')
        .expect(200);

      // Assert: Tenant B não vê os dados de A
      expect(response.body).toBeInstanceOf(Array);
      expect(response.body).toHaveLength(0);
      expect(response.body).not.toContainEqual(
        expect.objectContaining({ email: 'joao@acme.com' })
      );
    });

    it('deve rejeitar requisição sem tenant_id', async () => {
      const jwt = generateJwt({ sub: 'user1' }); // sem tid
      const response = await request(app.getHttpServer())
        .get('/users')
        .set('Authorization', `Bearer ${jwt}`)
        .expect(401);

      expect(response.body.message).toContain('Tenant');
    });

    it('deve rejeitar token com tenant inexistente', async () => {
      const response = await asTenant('tenant_inexistente')
        .get('/users')
        .expect(401);

      expect(response.body.message).toContain('não encontrado');
    });
  });
```

### 13.3 Teste 2: Concorrência

```typescript
  describe('Concorrência entre tenants', () => {
    it('deve processar dados de múltiplos tenants simultaneamente sem misturar', async () => {
      const tenants = ['acme', 'zeta', 'omega'];
      const createPromises = tenants.map((tid) =>
        asTenant(tid)
          .post('/users')
          .send({ name: `User from ${tid}`, email: `user@${tid}.com` })
          .expect(201)
      );

      await Promise.all(createPromises);

      // Verificar isolamento
      for (const tid of tenants) {
        const response = await asTenant(tid).get('/users').expect(200);
        const allEmails = response.body.map((u: any) => u.email);
        const otherTenants = tenants.filter((t) => t !== tid);

        // Não deve conter emails dos outros tenants
        for (const other of otherTenants) {
          expect(allEmails).not.toContain(`user@${other}.com`);
        }

        // Deve conter o próprio email
        expect(allEmails).toContain(`user@${tid}.com`);
      }
    });
  });
```

### 13.4 Teste 3: Injeção de Tenant ID

```typescript
  describe('Injeção de tenant_id', () => {
    it('deve ignorar tenant_id enviado no body e usar o do middleware', async () => {
      const response = await asTenant('acme')
        .post('/users')
        .send({
          name: 'Tentativa de invasão',
          email: 'hacker@zeta.com',
          tenant_id: 'zeta', // tentativa de criar como zeta
        })
        .expect(201);

      // Verificar que foi criado como acme, não zeta
      expect(response.body.tenant_id || response.body.tenantId).toBe('acme');

      // Tentar ler como zeta
      const zetaResponse = await asTenant('zeta')
        .get('/users')
        .expect(200);

      expect(zetaResponse.body).not.toContainEqual(
        expect.objectContaining({ email: 'hacker@zeta.com' })
      );
    });
  });
```

### 13.5 Teste 4: Rate Limit

```typescript
  describe('Rate limiting por plano', () => {
    it('deve bloquear tenant Free após exceder limite', async () => {
      // Tenant 'omega' é free (100 req/min no teste)
      const promises = Array.from({ length: 110 }, (_, i) =>
        asTenant('omega')
          .get('/users')
          .then((r) => r.status)
      );

      const statuses = await Promise.all(promises);
      const tooManyRequests = statuses.filter((s) => s === 429);

      expect(tooManyRequests.length).toBeGreaterThan(0);
    });

    it('Enterprise não deve ser rate limited com mesma carga', async () => {
      // Tenant 'acme' é enterprise (10000 req/min)
      const promises = Array.from({ length: 110 }, () =>
        asTenant('acme')
          .get('/users')
          .then((r) => r.status)
      );

      const statuses = await Promise.all(promises);
      const tooManyRequests = statuses.filter((s) => s === 429);

      expect(tooManyRequests).toHaveLength(0);
    });
  });
```

### 13.6 Teste 5: Migrations

```typescript
  describe('Migrations multi-tenant', () => {
    it('deve aplicar migration em todos os schemas de tenants ativos', async () => {
      const tenants = ['acme', 'zeta', 'omega'];

      for (const slug of tenants) {
        const result = await pool.query(`
          SELECT column_name
          FROM information_schema.columns
          WHERE table_schema = 'tenant_${slug}'
            AND table_name = 'users'
            AND column_name = 'phone'
        `);

        expect(result.rows.length).toBe(1);
        expect(result.rows[0].column_name).toBe('phone');
      }
    });
  });
```

### 13.7 Teste de Quebra Proposital

```typescript
  describe('Teste de quebra (fail-safe)', () => {
    it('deve falhar se removermos o WHERE tenant_id (prova de isolamento)', async () => {
      // Criar dados em tenants diferentes
      await asTenant('acme').post('/users').send({
        name: 'Dado sigiloso',
        email: 'secreto@acme.com',
      });

      await asTenant('zeta').post('/users').send({
        name: 'Outro dado',
        email: 'info@zeta.com',
      });

      // Query SEM filtro de tenant (simulando bug)
      const resultWithoutFilter = await pool.query('SELECT * FROM users');
      const allUsers = resultWithoutFilter.rows;

      // Se o isolamento está funcionando, essa query retorna dados de TODOS os tenants
      // Isso prova que sem o filtro, os dados vazam
      const tenantAcount = allUsers.filter((u: any) =>
        u.email.includes('acme')
      ).length;
      const tenantBcount = allUsers.filter((u: any) =>
        u.email.includes('zeta')
      ).length;

      expect(tenantAcount).toBeGreaterThan(0);
      expect(tenantBcount).toBeGreaterThan(0);

      // Com filtro, cada tenant vê apenas seus dados
      const resultWithFilter = await pool.query(
        'SELECT * FROM users WHERE tenant_id = $1',
        ['acme']
      );

      expect(resultWithFilter.rows).not.toContainEqual(
        expect.objectContaining({ email: 'info@zeta.com' })
      );
    });
  });
```

---

## Resumo

1. **Multi-tenancy** = uma instância de software atendendo múltiplos clientes com dados isolados
2. **Três abordagens**: Database per Tenant (máximo isolamento), Schema per Tenant (equilíbrio), Shared Database (mínimo custo)
3. **Identificação**: subdomínio, header HTTP, JWT claim ou path parameter — com fallback
4. **Middleware NestJS** extrai, valida e anexa o tenant ao request antes de qualquer controller
5. **AsyncLocalStorage** mantém o contexto do tenant durante toda a requisição, mesmo em async flows
6. **Prisma**: client por schema ou extensão com middleware para shared database
7. **Migrations**: precisam rodar em cada schema/banco; usar transações com rollback individual
8. **Dados globais** (planos, features) vs **dados por tenant** (usuários, pedidos, projetos)
9. **Seed automático** ao criar novo tenant — admin padrão, configurações, dados iniciais
10. **Backup** varia por plano: compartilhado (Free), PITR (Pro), dedicado (Enterprise)
11. **Performance**: connection pooling isolado, rate limiting por plano, índices com `tenant_id` como primeira coluna
12. **Pricing**: a arquitetura de isolamento define os limites técnicos de cada plano de negócio
13. **Testes**: vazamento zero, concorrência, injeção de tenant_id, rate limit, e teste de quebra proposital
