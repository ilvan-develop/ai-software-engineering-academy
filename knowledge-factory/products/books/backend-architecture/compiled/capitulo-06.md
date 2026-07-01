
# Multi-Tenant: Implementação com NestJS e Prisma

# Módulo 13b — Multi-Tenant: Implementação com NestJS e Prisma

**Middleware de tenant, identificação, serviços NestJS e integração com Prisma para isolamento de dados.**

## 1. Identificação do Tenant

O sistema precisa identificar **qual tenant está fazendo a requisição** antes de qualquer lógica de negócio.

### 1.1 Estratégias de Identificação

| Estratégia | Exemplo | Segurança | Complexidade | Ideal para |
|-----------|---------|:---------:|:------------:|-----------|
| **Subdomínio** | `acme.minhasaas.com` | Média | Média | Apps web públicas |
| **Header HTTP** | `X-Tenant-Id: acme` | Média | Baixa | APIs server-to-server |
| **JWT Claim** | `{ "tid": "acme" }` | Alta | Média | Apps autenticadas |
| **Path Parameter** | `/api/acme/users` | Baixa | Baixa | Desenvolvimento/debug |
| **DNS + SSL** | SNI com cert por tenant | Alta | Alta | Enterprise |

### 1.2 Subdomínio

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

### 1.3 Header HTTP

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
```text

### 1.4 JWT Claim

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

### 1.5 Path Parameter

```typescript
// Útil para debug, mas não recomendado para produção
// Exemplo: GET /api/:tenant/users
@Get('/api/:tenant/users')
findUsers(@Param('tenant') tenantId: string) {
  return this.userService.findAll(tenantId);
}
```text

### 1.6 Estratégia Combinada (Fallback)

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

## 2. Middleware de Tenant

### 2.1 Implementação com NestJS

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
```text

### 2.2 Aplicação Global ou por Rota

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

### 2.3 TenantModule

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
```text

### 2.4 TenantService

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

### 2.5 @Tenant() Decorator

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
```text

### 2.6 AsyncLocalStorage para Contexto

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

## 3. Prisma Multi-Tenant

### 3.1 Schema per Tenant com Prisma

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
```typescript

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

### 3.2 Shared Database com Prisma

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
```typescript

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

### 3.3 Prisma Middleware para Tenant

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
```text

### 3.4 Prisma Extension (Prisma >= 5.0)

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

