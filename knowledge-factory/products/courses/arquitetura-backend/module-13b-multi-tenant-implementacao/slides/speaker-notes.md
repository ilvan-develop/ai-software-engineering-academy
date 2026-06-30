## Introducao

# Módulo 13b — Multi-Tenant: Implementação com NestJS e Prisma
**Middleware de tenant, identificação, serviços NestJS e integração com Prisma para isolamento de dados.**

---
## 1. Identificação do Tenant

O sistema precisa identificar **qual tenant está fazendo a requisição** antes de qualquer lógica de negócio.
### 1.1 Estratégias de Identificação
| Estratégia | Exemplo | Segurança | Complexidade | Ideal para |
|-----------|---------|:---------:|:------------:|-----------|
| **Subdomínio** | `acme.minhasaas.com` | Média | Média | Apps web públicas |
| **Header HTTP** | `X-Tenant-Id: acme` | Média | Baixa | APIs server-to-server |
| **JWT Claim** | `{ "tid": "acme" }` | Alta | Média | Apps autenticadas |
| **Path Parameter** | `/api/acme/users` | Baixa | Baixa | Desenvolvimento/debug |

---
## 2. Middleware de Tenant

### 2.1 Implementação com NestJS
// tenant.middleware.ts
import { Injectable, NestMiddleware, UnauthorizedException } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';
import * as jwt from 'jsonwebtoken';
interface TenantInfo {
id: string;
name: string;

---
## 3. Prisma Multi-Tenant

### 3.1 Schema per Tenant com Prisma
// schema.prisma — modelo base
generator client {
provider = "prisma-client-js"
}
datasource db {
provider = "postgresql"
url      = env("DATABASE_URL")

---
