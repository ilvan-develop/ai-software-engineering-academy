==================================================
TWITTER/X — Thread
==================================================

🧵 Módulo 14 - DevOps: Docker, CI/CD e Deploy

Uma thread para voce dominar esse conceito.

1. Por que DevOps importa:
→ DevOps é a ponte entre o **código funcionando na máquina do dev** e o **código funcionando em produç
→ "Funciona na minha máquina" → "Não funciona no servidor"


2. Docker — Containerização:
→ ┌────────────────────────────────────────┐
→ │  CONTAINER                             │


3. GitHub Actions — CI/CD:
→ branches: [main, develop]
→ runs-on: ubuntu-latest


4. Variáveis de Ambiente:
→ DATABASE_URL=postgresql://user:password@localhost:5432/db
→ JWT_REFRESH_SECRET=change-me


5. Estratégias de Deploy:
→ │ app:v1   │ ← Load Balancer (tráfego ativo)
→ │ app:v2   │ (sem tráfego)


6. Docker Compose para múltiplos ambientes:
→ dockerfile: Dockerfile.dev
→ postgres_data:/var/lib/postgresql/data


Curtiu? Salve e compartilhe! 🚀

#DevTips #Arquitetura
