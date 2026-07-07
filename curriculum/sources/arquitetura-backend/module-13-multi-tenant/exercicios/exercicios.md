# Exercícios — Módulo 13: Multi-Tenant

## Exercício 1: Middleware de Tenant

Implemente um middleware NestJS que extraia o tenant de três fontes com a seguinte precedência:

1. JWT (claim `tid`)
2. Header `X-Tenant-Id`
3. Subdomínio (ex: `acme.app.com` → `acme`)

Valide também que:
- O tenant existe no cadastro (consulte uma lista em memória)
- O tenant está ativo
- O plano do tenant permite a requisição (rate limit básico — máx 100 req/min para Free)

```typescript
// Estrutura esperada
interface TenantConfig {
  id: string;
  name: string;
  plan: 'free' | 'pro' | 'enterprise';
  active: boolean;
}

@Injectable()
export class TenantMiddleware implements NestMiddleware {
  private tenants = new Map<string, TenantConfig>();

  constructor() {
    // Inicializar com dados mock
    this.tenants.set('acme', { id: 'acme', name: 'Acme Inc.', plan: 'enterprise', active: true });
    this.tenants.set('zeta', { id: 'zeta', name: 'Zeta Ltda.', plan: 'pro', active: true });
    this.tenants.set('omega', { id: 'omega', name: 'Omega S.A.', plan: 'free', active: true });
    this.tenants.set('disabled', { id: 'disabled', name: 'Disabled Co.', plan: 'free', active: false });
  }

  use(req: Request, res: Response, next: NextFunction) {
    // Sua implementação aqui
    // 1. Extrair tenant ID (JWT → Header → Subdomínio)
    // 2. Validar se existe
    // 3. Validar se ativo
    // 4. Rate limit check
    // 5. Anexar ao request e chamar next()
  }
}
```markdown

**Bônus:** Use `AsyncLocalStorage` para manter o contexto do tenant e crie um decorator `@Tenant()` para injetar o tenant nos controllers.

---

## Exercício 2: Repositório Multi-Tenant Genérico

Crie uma classe genérica `TenantRepository<T>` que:

1. Receba o `tenantId` no construtor
2. Force `WHERE tenant_id = $1` em TODAS as queries
3. Injete automaticamente `tenant_id` nos inserts
4. Seja extensível para `User`, `Order`, `Project`

```typescript
interface BaseEntity {
  id: string;
  tenant_id: string;
  created_at: Date;
}

class TenantRepository<T extends BaseEntity> {
  constructor(
    protected tableName: string,
    protected tenantId: string,
    protected pool: Pool,
  ) {}

  async findAll(): Promise<T[]> {
    // Implementar com WHERE tenant_id
  }

  async findById(id: string): Promise<T | null> {
    // Implementar com WHERE tenant_id AND id
  }

  async create(data: Omit<T, 'id' | 'tenant_id' | 'created_at'>): Promise<T> {
    // Implementar adicionando tenant_id automaticamente
  }

  async update(id: string, data: Partial<Omit<T, 'id' | 'tenant_id'>>): Promise<T> {
    // Implementar com WHERE tenant_id AND id
  }

  async delete(id: string): Promise<void> {
    // Implementar com WHERE tenant_id AND id
  }

  async count(where?: string, params?: any[]): Promise<number> {
    // Implementar com COUNT + tenant_id
  }
}
```text

Crie também uma factory:

```typescript
class RepositoryFactory {
  static create<T extends BaseEntity>(
    tableName: string,
    pool: Pool,
  ): (tenantId: string) => TenantRepository<T> {
    return (tenantId: string) => new TenantRepository<T>(tableName, tenantId, pool);
  }
}

// Uso
const userRepo = RepositoryFactory.create<User>('users', pool);
const acmeUsers = userRepo('acme'); // TenantRepository<User> com tenantId = acme
```markdown

---

## Exercício 3: Feature Flags por Plano + Guard

Implemente um sistema de feature flags baseado no plano do tenant e um Guard do NestJS.

```typescript
interface PlanFeatures {
  maxUsers: number;
  maxProjects: number;
  maxStorageMB: number;
  customDomain: boolean;
  apiAccess: boolean;
  advancedReports: boolean;
  auditLog: boolean;
}

const PLANS: Record<string, PlanFeatures> = {
  free: {
    maxUsers: 5, maxProjects: 10, maxStorageMB: 100,
    customDomain: false, apiAccess: false,
    advancedReports: false, auditLog: false,
  },
  pro: {
    maxUsers: 50, maxProjects: 100, maxStorageMB: 5_000,
    customDomain: false, apiAccess: true,
    advancedReports: true, auditLog: true,
  },
  enterprise: {
    maxUsers: Infinity, maxProjects: Infinity, maxStorageMB: Infinity,
    customDomain: true, apiAccess: true,
    advancedReports: true, auditLog: true,
  },
};
```yaml

Implemente:

1. **`FeatureFlagService`** — métodos `isFeatureEnabled(feature)`, `getLimit(resource)`, `checkLimit(resource)` 
2. **`FeatureGuard`** — `@UseGuards(FeatureGuard('apiAccess'))` que bloqueia requisições se a feature não estiver habilitada
3. **`LimitGuard`** — `@UseGuards(LimitGuard('maxUsers'))` que verifica se o tenant não excedeu o limite

```typescript
// Exemplo de uso
@Controller('reports')
export class ReportsController {
  @Get('advanced')
  @UseGuards(FeatureGuard('advancedReports'))
  getAdvancedReports() {
    // Só executa se o plano tiver advancedReports = true
  }
}

@Controller('users')
export class UsersController {
  @Post()
  @UseGuards(LimitGuard('maxUsers'))
  createUser(@Body() data: CreateUserDto) {
    // Só cria se não excedeu limite de usuários do plano
  }
}
```markdown

**Dica:** Guards precisam acessar o `TenantService` para saber o plano.

---

## Exercício 4: Pool Manager com Limites por Plano

Implemente um gerenciador de pools de conexão que:

1. Mantenha um pool separado para cada tenant (lazy initialization)
2. Configure limites diferentes conforme o plano:
   - Free: max 2 conexões, timeout 10s
   - Pro: max 10 conexões, timeout 30s
   - Enterprise: max 25 conexões, timeout 60s
3. Feche pools ociosos (sem uso por 5 minutos)
4. Exponha método `getStats()` para monitoramento

```typescript
import { Pool } from 'pg';

interface PoolEntry {
  pool: Pool;
  lastUsed: number;
  plan: string;
  createdAt: Date;
}

class PoolManager {
  private pools = new Map<string, PoolEntry>();

  private readonly PLAN_CONFIG = {
    free:       { max: 2,   idleTimeoutMillis: 10_000,  connectionTimeoutMillis: 5_000 },
    pro:        { max: 10,  idleTimeoutMillis: 30_000,  connectionTimeoutMillis: 10_000 },
    enterprise: { max: 25,  idleTimeoutMillis: 60_000,  connectionTimeoutMillis: 15_000 },
  };

  getPool(tenantId: string, plan: string = 'free'): Pool {
    // Implementar:
    // 1. Se já existe, atualizar lastUsed e retornar
    // 2. Se não existe, criar com config do plano e armazenar
  }

  async closeIdlePools(maxIdleMs: number = 300_000): Promise<void> {
    // Implementar: fechar pools que não foram usados nos últimos maxIdleMs
  }

  async closeAll(): Promise<void> {
    // Implementar: fechar todos os pools
  }

  getStats(): Record<string, {
    totalCount: number;
    idleCount: number;
    waitingCount: number;
    plan: string;
    uptime: number; // minutos desde criação
  }> {
    // Implementar: retornar estatísticas de cada pool
  }
}
```markdown

**Bônus:** Adicione um `setInterval` que roda `closeIdlePools` a cada minuto.

---

## Exercício 5: Testes de Isolamento

Escreva testes automatizados com NestJS Testing + Supertest que provem:

```typescript
describe('Isolamento entre Tenants', () => {
  let app: INestApplication;

  beforeAll(async () => {
    const moduleFixture = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();
    app = moduleFixture.createNestApplication();
    await app.init();
  });

  // Teste 1: Vazamento zero
  it('deve garantir que Tenant A NÃO veja dados do Tenant B', async () => {
    // 1. Criar 3 usuários como Tenant A
    // 2. Listar usuários como Tenant B
    // 3. Verificar que lista está vazia
  });

  // Teste 2: Concorrência segura
  it('deve processar 5 tenants simultâneos sem misturar dados', async () => {
    // 1. 5 tenants criam dados concorrentemente (Promise.all)
    // 2. Cada tenant lista seus dados
    // 3. Verificar que cada um vê APENAS seus próprios dados
  });

  // Teste 3: Injeção de tenant_id
  it('deve rejeitar tentativa de criar dado com tenant_id diferente', async () => {
    // 1. Autenticar como Tenant A
    // 2. Enviar requisição com tenant_id: 'zeta' no body
    // 3. Verificar que o dado foi criado como Tenant A (não Zeta)
    // 4. Verificar que Tenant B não vê este dado
  });

  // Teste 4: Rate limit
  it('deve bloquear tenant Free que excede rate limit', async () => {
    // 1. Disparar 110 requisições como tenant Free
    // 2. Verificar que pelo menos 1 retorna 429 Too Many Requests
    // 3. Repetir com tenant Enterprise — não deve rate limitar
  });

  // Teste 5: Feature flag blocking
  it('deve bloquear acesso a endpoint de plano superior', async () => {
    // 1. Autenticar como tenant Free
    // 2. Tentar acessar @UseGuards(FeatureGuard('customDomain'))
    // 3. Verificar 403 Forbidden
    // 4. Repetir como Enterprise — deve funcionar
  });
});
```text

**Dica:** Use `beforeEach` para limpar dados entre os testes e garantir isolamento também nos testes.

**Bônus:** Implemente um teste que **quebra propositalmente** o filtro de tenant e verifica que o teste falha (prova de que o isolamento funciona):
```typescript
it('prova de isolamento — query sem WHERE tenant_id retorna dados de todos', async () => {
  // Query direta no banco SEM filtro
  const result = await pool.query('SELECT * FROM users');
  // Deve conter dados de múltiplos tenants
  const tenants = new Set(result.rows.map((r: any) => r.tenant_id));
  expect(tenants.size).toBeGreaterThan(1);
});
```text
