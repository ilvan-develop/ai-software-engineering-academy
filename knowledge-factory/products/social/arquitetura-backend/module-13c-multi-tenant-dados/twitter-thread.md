==================================================
TWITTER/X — Thread
==================================================

🧵 Módulo 13c - Multi-Tenant: Migrations, Dados e Seed

Uma thread para voce dominar esse conceito.

1. Migrations Multi-Tenant:
→ // migrate-all-tenants.ts
→ import { Pool } from 'pg';


2. Dados Compartilhados vs Por Tenant:
→ Dados que **não pertencem a nenhum tenant específico** e são comuns a todos:
→ // Globais — uma única instância para o sistema todo


3. Seed por Tenant:
→ async function seedNewTenant(tenantSlug: string, plan: string): Promise<void> {
→ const schema = `tenant_${tenantSlug}`;


Curtiu? Salve e compartilhe! 🚀

#DevTips #Arquitetura
