# Módulo 13 — Multi-Tenant: Conceitos e Estratégias de Isolamento

**Conceitos fundamentais, três abordagens de isolamento de dados e análise comparativa por dimensão.**

---

## 1. O que é Multi-Tenancy?

Multi-tenancy é um padrão arquitetural onde **uma única instância de software atende múltiplos clientes (tenants)**, mantendo os dados de cada um logicamente isolados e invisíveis entre si.

```text
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

```text
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
```text

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

```sql
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
```text

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
```text

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
```text

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
