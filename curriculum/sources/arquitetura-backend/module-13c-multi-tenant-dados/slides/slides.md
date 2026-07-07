---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 13c — Multi-Tenant: Migrations, Dados e Seed

## Módulo 13c - Multi-Tenant: Migrations, Dados e Seed

---
## 1. Migrations Multi-Tenant

- // migrate-all-tenants.ts
- import { Pool } from 'pg';
- import { readMigrationFiles } from './migration-runner';
- async function migrateAllTenants(): Promise<void> {
- const tenants = [

---
## 2. Dados Compartilhados vs Por Tenant

- Dados que **não pertencem a nenhum tenant específico** e são comuns a todos:
- // Globais — uma única instância para o sistema todo
- interface Plan {
- id: string;
- name: string;              // "Free", "Pro", "Enterprise"

---
## 3. Seed por Tenant

- // tenant-seed.ts
- async function seedNewTenant(tenantSlug: string, plan: string): Promise<void> {
- const schema = `tenant_${tenantSlug}`;
- const client = await pool.connect();
- try {

---
## Exemplo: typescript

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
...
```javascript

---
## Exemplo: typescript

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
...
```markdown

---
## Recap

- 1. Migrations Multi-Tenant
- 2. Dados Compartilhados vs Por Tenant
- 3. Seed por Tenant

---
# Obrigado!

## Perguntas?
