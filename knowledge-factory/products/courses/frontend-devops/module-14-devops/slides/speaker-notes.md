## Introducao

# Módulo 14 — DevOps: Docker, CI/CD e Deploy
**Da máquina do desenvolvedor à produção.**
---

---
## 1. Por que DevOps importa

DevOps é a ponte entre o **código funcionando na máquina do dev** e o **código funcionando em produção**.
### O problema clássico
"Funciona na minha máquina" → "Não funciona no servidor"
Causas:
- Versões diferentes de dependências
- Variáveis de ambiente não configuradas
- Banco de dados diferente
- Sistema operacional diferente

---
## 2. Docker — Containerização

### O que é um container
┌────────────────────────────────────────┐
│  CONTAINER                             │
│  ┌──────────────────────────────────┐  │
│  │  Aplicação (Node.js)             │  │
│  ├──────────────────────────────────┤  │
│  │  Dependências (npm packages)     │  │
│  ├──────────────────────────────────┤  │

---
## 3. GitHub Actions — CI/CD

### Pipeline de CI (todo push)
name: CI
on:
push:
branches: [main, develop]
pull_request:
branches: [main]
jobs:

---
## 4. Variáveis de Ambiente

### .env.example (commitado)
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/db
# JWT
JWT_SECRET=change-me
JWT_REFRESH_SECRET=change-me
# Redis
REDIS_URL=redis://localhost:6379

---
## 5. Estratégias de Deploy

### Blue-Green Deployment
Versão Azul (atual):
┌──────────┐
│ app:v1   │ ← Load Balancer (tráfego ativo)
└──────────┘
Versão Verde (nova):
┌──────────┐
│ app:v2   │ (sem tráfego)

---
## 6. Docker Compose para múltiplos ambientes

### docker-compose.override.yml (dev)
services:
api:
build:
context: .
dockerfile: Dockerfile.dev
volumes:
- .:/app  # Hot reload

---
## 7. Health Checks e Graceful Shutdown

### Health check endpoint
@Controller('health')
export class HealthController {
constructor(
private prisma: PrismaService,
private redis: RedisService,
) {}
@Get()

---
## 8. Logs Estruturados

### Configuração de logs em JSON
import { Logger } from '@nestjs/common';
import { utilities as nestWinstonModuleUtilities } from 'nest-winston';
import * as winston from 'winston';
// main.ts
app.useLogger(
winston.createLogger({
level: process.env.NODE_ENV === 'production' ? 'info' : 'debug',

---
