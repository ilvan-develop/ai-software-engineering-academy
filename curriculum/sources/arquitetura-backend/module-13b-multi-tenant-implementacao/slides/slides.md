---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 13b — Multi-Tenant: Implementação com NestJS e Prisma

## Módulo 13b - Multi-Tenant: Implementação com NestJS e Prisma

---
## 1. Identificação do Tenant

- O sistema precisa identificar **qual tenant está fazendo a requisição** antes de qualquer lógica de negócio.
- | Estratégia | Exemplo | Segurança | Complexidade | Ideal para |
- |-----------|---------|:---------:|:------------:|-----------|
- | **Subdomínio** | `acme.minhasaas.com` | Média | Média | Apps web públicas |
- | **Header HTTP** | `X-Tenant-Id: acme` | Média | Baixa | APIs server-to-server |

---
## 2. Middleware de Tenant

- // tenant.middleware.ts
- import { Injectable, NestMiddleware, UnauthorizedException } from '@nestjs/common';
- import { Request, Response, NextFunction } from 'express';
- import * as jwt from 'jsonwebtoken';
- interface TenantInfo {

---
## 3. Prisma Multi-Tenant

- // schema.prisma — modelo base
- generator client {
- provider = "prisma-client-js"
- }
- datasource db {

---
## Exemplo: typescript

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
...
```

---
## Exemplo: typescript

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
...
```

---
## Recap

- 1. Identificação do Tenant
- 2. Middleware de Tenant
- 3. Prisma Multi-Tenant

---
# Obrigado!

## Perguntas?
