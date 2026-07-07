# Exercícios — Módulo 14

## Exercício 1: Dockerfile

Crie um Dockerfile multi-stage para uma aplicação Next.js com as seguintes características:
- Build com `npm run build`
- Runtime com Node 20 alpine
- Porta 3000
- Health check no `/api/health`
- Usuário não-root
- Imagem final < 200MB

---

## Exercício 2: docker-compose

Crie um docker-compose.yml para um sistema com:
- **api** — NestJS (build local, porta 3000)
- **frontend** — Next.js (build local, porta 3001)
- **db** — PostgreSQL 16
- **redis** — Redis 7
- **adminer** — gerenciamento do banco (porta 8080)

Inclua:
- Health checks em todos os serviços
- Volumes persistentes para db e redis
- Variáveis de ambiente via .env
- Dependências corretas (api depende de db e redis)

---

## Exercício 3: Pipeline CI/CD

Crie um workflow do GitHub Actions para:

**CI:**
- Rodar em todo push e PR para main
- Lint + typecheck
- Testes com banco PostgreSQL (usar service container)
- Build da imagem Docker

**CD:**
- Rodar apenas em push para main
- Login no Docker Hub
- Build e push da imagem
- Deploy via SSH com docker compose

---

## Exercício 4: Health checks

Implemente um endpoint `/health` que verifica:

1. **Banco de dados** — query `SELECT 1`
2. **Redis** — comando `PING`
3. **Disc space** — verificar se disco tem > 10% livre
4. **Memory** — verificar se memória disponível > 100MB

Retorne:

```json
{
  "status": "healthy",
  "timestamp": "2026-01-01T00:00:00Z",
  "checks": [
    { "name": "database", "status": "healthy", "latency": "2ms" },
    { "name": "redis", "status": "healthy", "latency": "1ms" },
    { "name": "disk", "status": "healthy", "available": "45%" },
    { "name": "memory", "status": "healthy", "available": "512MB" }
  ]
}
```markdown

---

## Exercício 5: Plano de deploy

Crie um plano de deploy para um sistema de **processamento de pagamentos** que:
- Precisa de 99.99% de disponibilidade
- Processa 10.000 transações/dia
- Tem dados sensíveis (PCI DSS)
- Tem 3 ambientes: dev, staging, production

O plano deve incluir:
1. Estratégia de deploy (Blue-Green, Rolling, Canary?)
2. Rollback plan
3. Health checks específicos
4. Monitoramento pós-deploy
5. Procedimento em caso de falha
6. Quem aprova cada deploy
