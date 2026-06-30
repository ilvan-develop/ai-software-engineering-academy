---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 14 — DevOps: Docker, CI/CD e Deploy

## Módulo 14 - DevOps: Docker, CI/CD e Deploy

---
## 1. Por que DevOps importa

- DevOps é a ponte entre o **código funcionando na máquina do dev** e o **código funcionando em produção**.
- "Funciona na minha máquina" → "Não funciona no servidor"
- Causas:
- Versões diferentes de dependências
- Variáveis de ambiente não configuradas

---
## 2. Docker — Containerização

- ┌────────────────────────────────────────┐
- │  CONTAINER                             │
- │  ┌──────────────────────────────────┐  │
- │  │  Aplicação (Node.js)             │  │
- │  ├──────────────────────────────────┤  │

---
## 3. GitHub Actions — CI/CD

- name: CI
- on:
- push:
- branches: [main, develop]
- pull_request:

---
## 4. Variáveis de Ambiente

- DATABASE_URL=postgresql://user:password@localhost:5432/db
- JWT_SECRET=change-me
- JWT_REFRESH_SECRET=change-me

---
## 5. Estratégias de Deploy

- Versão Azul (atual):
- ┌──────────┐
- │ app:v1   │ ← Load Balancer (tráfego ativo)
- └──────────┘
- Versão Verde (nova):

---
## 6. Docker Compose para múltiplos ambientes

- services:
- api:
- build:
- context: .
- dockerfile: Dockerfile.dev

---
## 7. Health Checks e Graceful Shutdown

- @Controller('health')
- export class HealthController {
- constructor(
- private prisma: PrismaService,
- private redis: RedisService,

---
## 8. Logs Estruturados

- import { Logger } from '@nestjs/common';
- import { utilities as nestWinstonModuleUtilities } from 'nest-winston';
- import * as winston from 'winston';
- // main.ts
- app.useLogger(

---
## Exemplo: text

```text
"Funciona na minha máquina" → "Não funciona no servidor"

Causas:
  - Versões diferentes de dependências
  - Variáveis de ambiente não configuradas
  - Banco de dados diferente
  - Sistema operacional diferente
  - Permissões diferentes
```

---
## Exemplo: text

```text
Containerização (Docker):
  → Mesmo ambiente em dev, staging e produção
  → Dependências isoladas
  → Reproducível em qualquer máquina

CI/CD:
  → Cada push é testado automaticamente
  → Deploy é um processo, não um evento
  → Rollback rápido se algo der errado
```

---
## Recap

- 1. Por que DevOps importa
- 2. Docker — Containerização
- 3. GitHub Actions — CI/CD
- 4. Variáveis de Ambiente
- 5. Estratégias de Deploy
- 6. Docker Compose para múltiplos ambientes
- 7. Health Checks e Graceful Shutdown
- 8. Logs Estruturados

---
# Obrigado!

## Perguntas?
