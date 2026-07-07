# Módulo 14 — Slides

---

## Slide 1: Título

**DevOps: Docker, CI/CD e Deploy**
Da máquina do desenvolvedor à produção

---

## Slide 2: O problema clássico

```yaml
"Funciona na minha máquina" → "Não funciona no servidor"

Causas:
- Versões diferentes de dependências
- Variáveis de ambiente ausentes
- Banco diferente
- SO diferente
```markdown

Docker resolve: **mesmo ambiente em todo lugar**

---

## Slide 3: Docker multi-stage

```yaml
deps:      npm ci → node_modules
builder:   npm ci + npm run build → dist
runner:    node_modules + dist (imagem LEVE)
```yaml

Final: só o necessário para rodar
Segurança: usuário não-root
Health check: integrado

---

## Slide 4: Pipeline CI/CD

```javascript
CI (todo push):
  lint → typecheck → test (com banco real) → build

CD (push na main):
  lint → test → build → docker push → deploy SSH
```markdown

Pipeline falhou? Não vai para produção

---

## Slide 5: Validação de env

```typescript
const EnvSchema = z.object({
  JWT_SECRET: z.string().min(32),
  DATABASE_URL: z.string().url(),
  // ...
});

// Falha na inicialização se algo faltar
if (!result.success) process.exit(1);
```markdown

Falhe cedo, não no meio da execução

---

## Slide 6: Estratégias de deploy

```yaml
Blue-Green:
  v1 (ativo) ──► v2 (novo) ──► switch ──► v1 (standby)

Rolling:
  v1 ──► v2 ──► v1 ──► v2 ──► v1 ──► v2 (sem downtime)

Canary:
  5% → 25% → 50% → 100% (risco mínimo)
```markdown

---

## Slide 7: Health checks

```text
/health    → todas as dependências
/ready     → pronto para receber tráfego
/live      → servidor está rodando
```markdown

Usado pelo Docker e orquestradores

---

## Slide 8: Graceful Shutdown

```text
SIGTERM recebido:
  1. Parar de aceitar novas conexões
  2. Finalizar requisições em andamento
  3. Fechar conexões (DB, Redis)
  4. Sair

Sem graceful shutdown: conexões são cortadas no meio
```markdown

---

## Slide 9: Logs estruturados

```javascript
❌ console.log('Usuário logou')

✅ {
    "timestamp": "2026-06-01T10:30:00Z",
    "level": "info",
    "message": "Usuário autenticado",
    "userId": "abc123",
    "ip": "192.168.1.1"
  }
```markdown

JSON é searchável por ferramentas (Datadog, ELK, Grafana)

---

## Slide 10: Estrutura do projeto

```text
/
├── Dockerfile
├── Dockerfile.dev
├── docker-compose.yml
├── docker-compose.override.yml (dev)
├── docker-compose.prod.yml
├── .dockerignore
├── .env.example
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
└── src/
```markdown

---

## Slide 11: Anti-padrões DevOps

- **Imagem gigante** — sem multi-stage (> 1GB)
- **Rodar como root** — risco de segurança
- **Sem health check** — orquestrador não sabe se está vivo
- **Deploy manual** — "sobe lá no servidor e roda"
- **Rollback?** — "espero que nunca precise"
- **Log em texto** — "vou ler no terminal mesmo"

---

## Slide 12: Para refletir

> "Seu deploy não é manual. Seu deploy é um pipeline que você **confia**."

> "Docker não é sobre 'funciona na minha máquina'. É sobre 'funciona em **qualquer** máquina'."
