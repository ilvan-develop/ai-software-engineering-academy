# Módulo 13 - Multi-Tenant: Construindo SaaS Escalável

---

## 1. O que é Multi-Tenancy?

Multi-tenancy é um padrão arquitetural onde **uma única instância de software atende múltiplos clientes (tenants)**, mantendo os dados de cada um logicamente isolados e invisíveis entre si.
┌──────────────────────────────────────────────────────┐
│                    SISTEMA (1 instância)               │
│                                                        │

## 2. Abordagens de Isolamento

Existem três estratégias principais para isolar dados entre tenants.
### 2.1 Database per Tenant
Cada tenant tem **seu próprio banco de dados**. O roteador de conexão decide qual banco usar com base no tenant identificado.
┌──────────────────────────────────────────────┐

## 3. Análise Aprofundada por Dimensão

### 3.1 Segurança
**Database per Tenant:** Um vazamento de dados de um tenant não afeta os outros. Se um cliente exige compliance específico (LGPD, HIPAA, SOC2), pode-se isolar completamente em nível físico. Ataques de SQL injection ficam contidos no banco do tenant.
**Schema per Tenant:** Um invasor que ganha acesso ao banco pode potencialmente acessar múltiplos schemas. A segurança depende das permissões do usuário do banco (`GRANT USAGE ON SCHEMA`). Idealmente, o usuário da aplicação tem acesso apenas ao schema do tenant atual.
**Shared Database:** Um SQL injection ou bug no `WHERE` expõe **todos os dados de todos os tenants**. Requer:

## 4. Identificação do Tenant

O sistema precisa identificar **qual tenant está fazendo a requisição** antes de qualquer lógica de negócio.
### 4.1 Estratégias de Identificação
| Estratégia | Exemplo | Segurança | Complexidade | Ideal para |
|-----------|---------|:---------:|:------------:|-----------|

## 5. Middleware de Tenant

### 5.1 Implementação com NestJS
// tenant.middleware.ts
import { Injectable, NestMiddleware, UnauthorizedException } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';

## 6. Prisma Multi-Tenant

### 6.1 Schema per Tenant com Prisma
// schema.prisma — modelo base
generator client {
provider = "prisma-client-js"

---
*Este artigo faz parte da formacao Arquitetura de Software Enterprise com IA*