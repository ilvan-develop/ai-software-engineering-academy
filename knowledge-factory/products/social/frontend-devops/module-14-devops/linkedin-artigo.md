==================================================
LINKEDIN — Artigo
==================================================

Titulo: Módulo 14 - DevOps: Docker, CI/CD e Deploy: O Que Todo Arquiteto Deveria Saber


## 1. Por que DevOps importa

- DevOps é a ponte entre o **código funcionando na máquina do dev** e o **código funcionando em produção**.
- "Funciona na minha máquina" → "Não funciona no servidor"
- Versões diferentes de dependências

## 2. Docker — Containerização

- ┌────────────────────────────────────────┐
- │  CONTAINER                             │
- │  ┌──────────────────────────────────┐  │

## 3. GitHub Actions — CI/CD

- branches: [main, develop]
- runs-on: ubuntu-latest
- uses: actions/checkout@v4

## 4. Variáveis de Ambiente

- DATABASE_URL=postgresql://user:password@localhost:5432/db
- JWT_REFRESH_SECRET=change-me
- REDIS_URL=redis://localhost:6379

## 5. Estratégias de Deploy

- │ app:v1   │ ← Load Balancer (tráfego ativo)
- │ app:v2   │ (sem tráfego)
- Passo 1: Deploy da versão verde


---

🔥 Gostou? Compartilhe e marque alguem que precisa ler isso.

#ArquiteturaDeSoftware #EngenhariaDeSoftware #CarreiraDev
