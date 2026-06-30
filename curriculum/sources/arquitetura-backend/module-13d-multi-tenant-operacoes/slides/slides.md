---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 13d — Multi-Tenant: Operações e Qualidade

## Módulo 13d - Multi-Tenant: Operações e Qualidade

---
## 1. Backup e Restore

- TENANTS=("acme" "zeta" "omega")
- DATE=$(date +%Y%m%d_%H%M)
- BACKUP_DIR="./backups"

---
## 2. Performance

- // pool-manager.ts
- import { Pool } from 'pg';
- interface PoolConfig {
- max: number;
- idleTimeoutMillis: number;

---
## 3. Pricing Baseado em Tenancy

- A arquitetura de isolamento escolhida define diretamente o que pode ser oferecido em cada plano:
- | Plano | Isolamento | Limites | Preço | Público |
- |-------|-----------|---------|-------|---------|
- | **Free** | Shared DB | 5 usuários, 10 projetos, 100 MB | Grátis | Teste / pequenas equipes |
- | **Pro** | Schema per Tenant | 50 usuários, 100 projetos, 5 GB | $29/mês | PMEs |

---
## 4. Testes de Isolamento entre Tenants

- // tenant-isolation.spec.ts
- import { Test, TestingModule } from '@nestjs/testing';
- import { INestApplication } from '@nestjs/common';
- import * as request from 'supertest';
- import { AppModule } from '../src/app.module';

---
## Exemplo: bash

```bash
#!/bin/bash
# backup-all-tenants.sh — backup individual por tenant

TENANTS=("acme" "zeta" "omega")
DATE=$(date +%Y%m%d_%H%M)
BACKUP_DIR="./backups"

mkdir -p "$BACKUP_DIR"

for TENANT in "${TENANTS[@]}"; do
  echo "Iniciando backup do tenant: $TENANT"

...
```

---
## Exemplo: bash

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
...
```

---
## Recap

- 1. Backup e Restore
- 2. Performance
- 3. Pricing Baseado em Tenancy
- 4. Testes de Isolamento entre Tenants

---
# Obrigado!

## Perguntas?
