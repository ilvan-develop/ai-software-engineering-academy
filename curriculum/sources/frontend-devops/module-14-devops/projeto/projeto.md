# Projeto Módulo 14 — DevOps Pipeline Completo

## Objetivo

Configurar o pipeline DevOps completo para um sistema Enterprise.

## Contexto

Você é o DevOps Engineer de um SaaS de **gestão de projetos** com:
- Frontend: Next.js (porta 3000)
- Backend: NestJS (porta 4000)
- Banco: PostgreSQL 16
- Cache: Redis 7
- 3 ambientes: dev, staging, production

## Entregáveis

### 1. Dockerfiles

Crie Dockerfiles para:

- **Dockerfile** — produção (multi-stage, < 200MB, não-root)
- **Dockerfile.dev** — desenvolvimento (hot reload)

### 2. Docker Compose

- **docker-compose.yml** — base com todos os serviços
- **docker-compose.override.yml** — dev (hot reload, portas expostas)
- **docker-compose.prod.yml** — produção (replicas, recursos, restart)

### 3. CI/CD (GitHub Actions)

**ci.yml:**
- Rodar em push e PR para main
- Lint + typecheck (frontend + backend)
- Testes com PostgreSQL
- Build das imagens Docker

**cd.yml:**
- Rodar em push para main (após CI passar)
- Login no Docker Hub
- Build e push das imagens
- Deploy via SSH com docker compose
- Health check pós-deploy
- Rollback automático se health check falhar

### 4. Health Checks

Implemente endpoints de health check no backend:
- `/health` — verificar banco + redis
- `/ready` — readiness probe
- `/live` — liveness probe

### 5. Configuração

- `.env.example` com todas as variáveis documentadas
- `.dockerignore` otimizado
- Script de validação de env na inicialização
- Graceful shutdown configurado

## Critérios de avaliação

- [ ] Dockerfile multi-stage funcional
- [ ] Imagem final < 200MB
- [ ] Usuário não-root
- [ ] Health checks em todos os serviços
- [ ] Pipeline CI/CD completo (lint → test → build → deploy)
- [ ] Validação de env na inicialização
- [ ] Graceful shutdown
- [ ] .env.example com todas as variáveis
- [ ] Rollback automático se falhar
