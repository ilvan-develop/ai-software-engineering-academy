==================================================
LINKEDIN — Artigo
==================================================

Titulo: Módulo 13c - Multi-Tenant: Migrations, Dados e Seed: O Que Todo Arquiteto Deveria Saber


## 1. Migrations Multi-Tenant

- // migrate-all-tenants.ts
- import { Pool } from 'pg';
- import { readMigrationFiles } from './migration-runner';

## 2. Dados Compartilhados vs Por Tenant

- Dados que **não pertencem a nenhum tenant específico** e são comuns a todos:
- // Globais — uma única instância para o sistema todo
- name: string;              // "Free", "Pro", "Enterprise"

## 3. Seed por Tenant

- async function seedNewTenant(tenantSlug: string, plan: string): Promise<void> {
- const schema = `tenant_${tenantSlug}`;
- const client = await pool.connect();


---

🔥 Gostou? Compartilhe e marque alguem que precisa ler isso.

#ArquiteturaDeSoftware #EngenhariaDeSoftware #CarreiraDev
