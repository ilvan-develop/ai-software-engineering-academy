## Introducao

# Módulo 13c — Multi-Tenant: Migrations, Dados e Seed
**Migrations multi-tenant, estratégias de dados compartilhados vs isolados e seed automático por tenant.**

---
## 1. Migrations Multi-Tenant

### 1.1 Database per Tenant
// migrate-all-tenants.ts
import { Pool } from 'pg';
import { readMigrationFiles } from './migration-runner';
async function migrateAllTenants(): Promise<void> {
const tenants = [
{ id: 'acme', dbUrl: 'postgresql://.../acme' },
{ id: 'zeta', dbUrl: 'postgresql://.../zeta' },

---
## 2. Dados Compartilhados vs Por Tenant

### 2.1 Tabelas Globais (Compartilhadas)
Dados que **não pertencem a nenhum tenant específico** e são comuns a todos:
// Globais — uma única instância para o sistema todo
interface Plan {
id: string;
name: string;              // "Free", "Pro", "Enterprise"
maxUsers: number;
maxStorage: number;        // MB

---
## 3. Seed por Tenant

### 3.1 Seed Automático ao Criar Tenant
// tenant-seed.ts
async function seedNewTenant(tenantSlug: string, plan: string): Promise<void> {
const schema = `tenant_${tenantSlug}`;
const client = await pool.connect();
try {
await client.query(`CREATE SCHEMA IF NOT EXISTS "${schema}"`);
// 1. Migrations básicas

---
