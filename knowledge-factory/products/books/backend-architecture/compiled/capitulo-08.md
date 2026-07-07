
# Multi-Tenant: Operações e Qualidade

# Módulo 13d — Multi-Tenant: Operações e Qualidade

**Backup, restore, performance, rate limiting, pricing baseado em tenancy e testes de isolamento.**

---

## 1. Backup e Restore

### 1.1 Database per Tenant

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
```text

### 1.2 Schema per Tenant — Backup Seletivo

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

### 1.3 Estratégia por Plano

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

## 2. Performance

### 2.1 Connection Pooling por Tenant

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

### 2.2 Query Optimization

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

### 2.3 Rate Limiting por Tenant

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

### 2.4 Indexação para Shared Database

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
```text

---

## 3. Pricing Baseado em Tenancy

### 3.1 Modelo de Planos

A arquitetura de isolamento escolhida define diretamente o que pode ser oferecido em cada plano:

| Plano | Isolamento | Limites | Preço | Público |
|-------|-----------|---------|-------|---------|
| **Free** | Shared DB | 5 usuários, 10 projetos, 100 MB | Grátis | Teste / pequenas equipes |
| **Pro** | Schema per Tenant | 50 usuários, 100 projetos, 5 GB | $29/mês | PMEs |
| **Business** | Schema per Tenant (dedicado) | 200 usuários, 500 projetos, 50 GB | $99/mês | Médias empresas |
| **Enterprise** | DB per Tenant + Réplica | Ilimitado | $499/mês | Grandes clientes |

### 3.2 Feature Flags por Plano

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

### 3.3 Guard do NestJS para Feature Flags

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

## 4. Testes de Isolamento entre Tenants

### 4.1 Configuração de Teste

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

### 4.2 Teste 1: Vazamento Zero

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

### 4.3 Teste 2: Concorrência

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

### 4.4 Teste 3: Injeção de Tenant ID

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

### 4.5 Teste 4: Rate Limit

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

### 4.6 Teste 5: Migrations

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

### 4.7 Teste de Quebra Proposital

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

