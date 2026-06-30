# Prompt: Dockerizar Aplicação

Você é um DevOps Expert Agent.

Crie a configuração Docker para a aplicação abaixo.

## Aplicação

- **Tipo:** Next.js + NestJS + Prisma + PostgreSQL
- **Portas:** app:3000, api:4000
- **Banco:** PostgreSQL 16
- **Cache:** Redis 7

## Saída esperada

### Dockerfile (multi-stage)

```dockerfile
# Estágio 1: Instalar dependências
FROM node:20-alpine AS deps
# ...

# Estágio 2: Build
FROM node:20-alpine AS builder
# ...

# Estágio 3: Runtime (leve)
FROM node:20-alpine AS runner
# ...
```

### docker-compose.yml

```yaml
services:
  app:
    build:
      context: ./apps/web
    ports:
      - "3000:3000"
    env_file: .env
    depends_on:
      api:
        condition: service_healthy
  api: ...
  db: ...
  redis: ...
```

Regras:
- Multi-stage build
- Não rodar como root
- Health checks para dependências
- Caching de camadas Docker otimizado
