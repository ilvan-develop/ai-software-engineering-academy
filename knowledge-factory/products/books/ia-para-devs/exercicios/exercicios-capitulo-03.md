# Exercicios - Capitulo 3: Automacao do Ciclo de Desenvolvimento com IA

> **Modulo:** IA para Desenvolvedores  
> **Total de exercicios:** 5  
> **Progressao:** Facil -> Medio -> Dificil  
> **Tempo total estimado:** 90-130 min

---

## Exercicio 1 - Facil: Leitura e Interpretacao de Pipeline CI/CD

**Tempo estimado:** 15 min  
**Tema:** Entender o fluxo de uma pipeline CI/CD

### Contexto

Analise o pipeline GitHub Actions abaixo e responda as perguntas.

```yaml
name: CI Pipeline
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
env:
  NODE_VERSION: 20.x
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
      - run: npm ci
      - run: npm run lint
  test:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm test
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm run build
  deploy:
    needs: build
    if: github.ref == "refs/heads/main"
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying..."
```

### Perguntas

1. Quantos jobs existem no pipeline?
2. Em que ordem eles executam? (qual a dependencia entre eles?)
3. Em quais branches o pipeline dispara?
4. O job de deploy executa em que situacao?
5. O que acontece se o job de lint falhar?
6. Qual problema de performance existe na pipeline? (dica: npm ci vs cache)
7. Se um PR para main e aberto, quais jobs rodam?
8. O que falta para esta pipeline ser considerada CD (Continuous Deployment) em vez de CI apenas?

### Template

```
1.
2.
3.
...
```

### Criterios de correcao

| Criterio | Peso |
|----------|------|
| Respondeu corretamente todas as 8 perguntas | 80% |
| Justificativas claras | 20% |

### Gabarito

1. 4 jobs: lint, test, build, deploy
2. lint -> test -> build -> deploy (cada um com needs do anterior)
3. main e develop (push); main (pull_request)
4. So quando o push e para main (github.ref == refs/heads/main)
5. Os jobs test, build e deploy nao rodam (needs: lint bloqueia)
6. Nao usa cache de dependencias - npm ci toda vez, desnecessario
7. lint e test (build e deploy so rodam em push, nao PR)
8. Deploy automatizado sem aprovacao manual (atualmente e so um echo, sem acao real)

---
## Exercicio 2 - Facil/Medio: Criar Pipeline GitHub Actions do Zero

**Tempo estimado:** 20 min  
**Tema:** Escrever workflow YAML para CI/CD

### Contexto

Voce precisa criar um pipeline de CI/CD para um projeto TypeScript com as seguintes caracteristicas:
- Gerenciador de pacotes: pnpm
- Node.js 20.x
- Testes: Vitest (unitarios) + Playwright (e2e)
- Build: tsc + vite
- Deploy: Vercel (via vercel-action)
- Branches: main (producao), develop (staging)

### Tarefa

Crie o arquivo `.github/workflows/ci.yml` completo com:

1. **Job de lint** - ESLint + Prettier check
2. **Job de testes unitarios** - Vitest, dependente de lint
3. **Job de build** - Compilacao TypeScript, dependente de testes
4. **Job de testes e2e** - Playwright, dependente de build
5. **Job de deploy staging** - Dispara em push para develop (manual gate)
6. **Job de deploy producao** - Dispara em push para main (automatico se todos anteriores passarem)

Requisitos:
- Usar actions/checkout@v4, pnpm/action-setup@v3, actions/setup-node@v4
- Cache de dependencias com pnpm
- Variaveis de ambiente para NODE_VERSION e PNPM_VERSION
- Job de e2e precisa de build pronto (needs + download artifact)

### Template

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]

env:
  NODE_VERSION: "20.x"
  PNPM_VERSION: "9"

jobs:
  # ... completar
```

### Criterios de correcao

| Criterio | Peso |
|----------|------|
| Estrutura YAML valida | 15% |
| Jobs em ordem correta com dependencies (needs) | 25% |
| Cache de dependencias configurado | 15% |
| Deploy staging com manual gate (environment) | 15% |
| Deploy producao automatico so em main | 15% |
| Uso de artifacts entre jobs (build -> e2e) | 15% |

### Gabarito (resumo)

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v3
        with: { version: "${{ env.PNPM_VERSION }}" }
      - uses: actions/setup-node@v4
        with: { node-version: "${{ env.NODE_VERSION }}", cache: "pnpm" }
      - run: pnpm install --frozen-lockfile
      - run: pnpm lint && pnpm format:check

  test:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      # setup igual ao lint
      - run: pnpm test:unit

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      # setup
      - run: pnpm build
      - uses: actions/upload-artifact@v4
        with: { name: build, path: dist/ }

  e2e:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # setup
      - uses: actions/download-artifact@v4
        with: { name: build, path: dist/ }
      - run: pnpm dlx playwright install --with-deps
      - run: pnpm test:e2e

  deploy-staging:
    needs: e2e
    if: github.ref == "refs/heads/develop"
    environment: { name: staging }
    runs-on: ubuntu-latest
    steps:
      - uses: amondnet/vercel-action@v25
        with: { vercel-token: "${{ secrets.VERCEL_TOKEN }}", vercel-org-id: "...", vercel-project-id: "...", vercel-args: "--prod" }

  deploy-production:
    needs: e2e
    if: github.ref == "refs/heads/main"
    environment: { name: production }
    runs-on: ubuntu-latest
    steps:
      # deploy igual, sem --prod?
      - uses: amondnet/vercel-action@v25
```

---

## Exercicio 3 - Medio: Pipeline Multi-Estagio com Seguranca e IaC

**Tempo estimado:** 25 min  
**Tema:** Integrar seguranca e infraestrutura como codigo na pipeline

### Contexto

Voce precisa expandir a pipeline do exercicio anterior para incluir:
- **Analise de seguranca estatica (SAST)** com SonarQube e Trivy
- **Varredura de dependencias** com npm audit
- **Infrastructure as Code** com Terraform (plan + apply)
- **Validacao de migrations** do Prisma

### Tarefa

Adicione os seguintes jobs a pipeline do exercicio 2:

1. **security-sast** - Job que roda apos build:
   - ESLint com plugins de seguranca
   - Trivy scan na imagem do container
   - npm audit com severity-threshold=high

2. **iac-plan** - Job que roda em paralelo com security:
   - Terraform init, fmt -check, validate, plan
   - Upload do plano como artifact

3. **migration-check** - Job que valida as migrations do Prisma:
   - pnpm db:migrate --dry-run
   - Verifica se nao ha colunas dropadas sem warning

4. **iac-apply** - Job que so roda em main, dependente de iac-plan e security-sast:
   - Terraform apply com o plano gerado

### Regras de negocio da pipeline

- Se security-sast encontrar vulnerabilidade CRITICAL, o build deve falhar
- iac-plan e security-sast rodam em paralelo (depois do build)
- deploy-production so roda se security-sast, iac-apply e e2e passarem
- migration-check roda antes do deploy

### Template

```yaml
security-sast:
  needs: build
  # ... completar

iac-plan:
  needs: build
  # ... completar

migration-check:
  needs: build
  # ... completar

iac-apply:
  needs: [iac-plan, security-sast]
  if: github.ref == "refs/heads/main"
  # ... completar
```

### Criterios de correcao

| Criterio | Peso |
|----------|------|
| SAST configurado com ferramentas corretas | 20% |
| IaC plan e apply configurados corretamente | 25% |
| Migration check implementado | 15% |
| Regras de paralelismo e dependencia corretas | 25% |
| Bloqueio por vulnerabilidade critica implementado | 15% |

### Gabarito (trechos)

```yaml
security-sast:
  needs: build
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - run: pnpm install --frozen-lockfile
    - run: pnpm dlx eslint . --ext .ts --rulesdir eslint-security-rules
    - name: Trivy Scan
      uses: aquasecurity/trivy-action@master
      with:
        image-ref: meuregistro/app:${{ github.sha }}
        format: sarif
        output: trivy-results.sarif
        exit-code: 1  # Falha se encontrar CRITICAL
    - run: pnpm audit --audit-level=high

iac-plan:
  needs: build
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: hashicorp/setup-terraform@v3
      with: { terraform_version: "1.8.0" }
    - run: terraform init
    - run: terraform fmt -check
    - run: terraform validate
    - run: terraform plan -out=tfplan
    - uses: actions/upload-artifact@v4
      with: { name: tfplan, path: tfplan }
```

---

## Exercicio 4 - Medio/Dificil: Estrategia de Deploy com Rollback e Feature Flags

**Tempo estimado:** 20 min  
**Tema:** Blue-green, canary, rolling update e feature flags

### Contexto

Sua app tem 10 replicas em producao. Voce precisa deployar v2.0.0 que:
- Adiciona novo fluxo de checkout
- Altera schema do banco (nova tabela)
- Pode impactar performance

### Tarefa
Responda JUSTIFICANDO cada escolha:

1. **Qual estrategia de deploy?** (Blue-green, Canary ou Rolling?)
   - Considere zero downtime, rollback rapido, seguranca

2. **Rollout gradual?**
   - Passos e porcentagens

3. **Rollback?**
   - Manual ou automatico? Gatilhos?

4. **Feature flags?**
   - Qual flag? Como ativar/desativar?

5. **Migracao de banco?**
   - Forward-compatible? Ordem?

### Template

```
1. Estrategia:
   Justificativa:
2. Rollout:
3. Rollback:
4. Feature flags:
5. Migracao:
```

### Criterios de correcao

| Criterio | Peso |
|----------|------|
| Justificativa coerente | 20% |
| Rollout gradual ivel | 20% |
| Rollback claro | 20% |
| Feature flags adequadas | 20% |
| Migracao segura | 20% |

### Gabarito

1. **Canary** - Menos arriscado que blue-green, mais seguro que rolling. Comecar com 10%, monitorar.
2. 10% (5 min) -> 25% (10 min) -> 50% (10 min) -> 100%. Abortar se P95 latency >20% ou error rate >1%.
3. Argo Rollouts auto-rollback se metricas degradarem. Manual: reverter tag image.
4. Flag "checkout-v2-enabled". Ativar para internos, depois 10%, 50%, 100%. Desativar sem redeploy.
5. (1) Criar nova tabela. (2) Flag ativa novo fluxo. (3) Backfill dados. (4) Remover codigo antigo. Nunca dropar coluna sem garantia.

---

## Exercicio 5 - Dificil: Runbook Automatico e Self-Healing

**Tempo estimado:** 30 min  
**Tema:** Automacao de recuperacao e auto-cura de infra

### Contexto

Voce e responsavel pela resiliencia de um sistema critico. Incidentes recorrentes:

1. **Pool de conexoes** - App perde conexao com PostgreSQL (pool esgota)
2. **Disco cheio** - Pods em ECS sem espaco (logs nao rotacionados)
3. **Memory leak** - App consome memoria progressivamente, precisa de restart
4. **TLS expirado** - Certificado SSL expira sem renovacao

### Tarefa

Para cada incidente, crie:

1. **Script de self-healing** (TypeScript) que detecta e corrige
2. **Runbook automatico** (GitHub Actions workflow)
3. **Detecao/Monitor** - Como identificar antes do usuario?

### Template

```
### Incidente: [nome]
**Deteccao:**
**Script:**
**Runbook (YAML):**
**Metricas de sucesso:**
```

### Criterios de correcao

| Criterio | Peso |
|----------|------|
| Deteccao ivel para cada incidente | 20% |
| Scripts de self-healing implementaveis | 30% |
| Runbooks bem estruturados (YAML) | 30% |
| Metricas de sucesso mensuraveis | 20% |

### Gabarito (Incidente 1 - Pool de Conexoes)

**Deteccao:** Datadog: postgresql.connections.active > max_connections * 0.9

**Script (TypeScript):**
```typescript
import { Pool } from "pg"
const pool = new Pool({ connectionString: process.env.DATABASE_URL })
async function healPool() {
  const r = await pool.query(`SELECT count(*) as active FROM pg_stat_activity WHERE state = "active"`)
  if (parseInt(r.rows[0].active) > 80) {
    await pool.query(`SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE state = "idle" AND state_change < now() - interval "5 minutes" AND pid <> pg_backend_pid()`)
    console.log("Conexoes idle terminadas")
  }
}
```

**Runbook (GitHub Actions):**
```yaml
name: Runbook - Pool Recovery
on:
  workflow_dispatch:
  schedule: [{ cron: "*/5 * * * *" }]
jobs:
  heal:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: node scripts/heal-pool.js
        env: { DATABASE_URL: ${{ secrets.DATABASE_URL }} }
```

**Metricas:** Error rate de conexao <5%. MTTR <2min.

---

## Exercicio 6 - Medio: Debug de Pipeline com Erros Sutis

**Tempo estimado:** 20 min  
**Tema:** Identificar e corrigir problemas em um pipeline YAML

### Contexto
Um dev junior criou a pipeline abaixo, mas ela apresenta varios problemas. Nem todos sao erros de sintaxe — alguns sao logicos ou de boas praticas.

```yaml
name: Deploy
on:
  push:
    branches: [main, develop, feature/*]
jobs:
  test:
    runs-on: ubuntu-lastest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 18
      - run: npm install
      - run: npm run test -- --coverage
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run lint
  build:
    needs: [test, lint]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run build
      - uses: actions/upload-artifact@v4
        with:
          name: build
          path: .
  deploy-staging:
    needs: build
    if: github.ref == "refs/heads/develop"
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Deploying to staging"
  deploy-production:
    needs: [build, test]
    if: github.ref == "refs/heads/main"
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Deploying to production"
```

### Tarefa
1. Identifique minimo **7 problemas** (entre erros e anti-padroes)
2. Classifique cada um como: **Sintaxe** / **Logica** / **Seguranca** / **Performance** / **Boas Praticas**
3. Corrija cada problema no YAML
4. Depois de corrigir, responda: se um push for feito em `feature/login`, quais jobs rodam?

### Template
```
### Problemas Encontrados
| # | Problema | Categoria | Correcap |
|---|----------|-----------|----------|
| 1 |          |           |          |

### Pipeline Corrigida (completa)

### Pergunta: Push em feature/login
R:
```

### Criterios de Correcao
| Criterio | Peso |
|----------|------|
| Identificou minimo 7 problemas | 40% |
| Classificacao correta | 20% |
| Correcoes viaveis e corretas | 30% |
| Resposta sobre push em feature/login correta | 10% |

### Gabarito
| # | Problema | Cat | Correcap |
|---|----------|-----|----------|
| 1 | `ubuntu-lastest` (typo) | Sintaxe | `ubuntu-latest` |
| 2 | `node-version: 18` fixa, sem env var | Boas Praticas | `env.NODE_VERSION: "20.x"` |
| 3 | `npm install` (nao `npm ci`) | Boas Praticas | `npm ci` (reprodutivel) |
| 4 | lint NAO tem `needs` de setup-node | Logica | Adicionar actions/setup-node com npm ci |
| 5 | `path: .` no upload-artifact (muito grande) | Performance | `path: dist/` (so o necessario) |
| 6 | `deploy-production` depende de `test` (nao `lint`) | Logica | `needs: [lint, test, build]` |
| 7 | feature/* branches disparam a pipeline | Seguranca | Remover feature/*; branches de feature devem passar por PR |
| 8 | Sem cache de dependencias | Performance | `cache: npm` no setup-node |
| 9 | `--coverage` no test sem upload do coverage | Boas Praticas | Upload coverage artifact ou remover flag |
| 10 | Sem ambiente (environment) no deploy | Seguranca | Adicionar `environment: { name: staging/production }` com aprovacao |

**Push em feature/login:** Nenhum job roda — o trigger `push` so cobre `main` e `develop`, nao `feature/*`. Para rodar em feature branches, deveria usar `pull_request` em vez de `push`.

### Pipeline Corrigida
```yaml
name: Deploy
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
env:
  NODE_VERSION: "20.x"
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "${{ env.NODE_VERSION }}", cache: "npm" }
      - run: npm ci
      - run: npm run lint
  test:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "${{ env.NODE_VERSION }}", cache: "npm" }
      - run: npm ci
      - run: npm test
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "${{ env.NODE_VERSION }}", cache: "npm" }
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-artifact@v4
        with: { name: build, path: dist/ }
  deploy-staging:
    needs: build
    if: github.ref == "refs/heads/develop"
    environment: { name: staging }
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying to staging"
  deploy-production:
    needs: build
    if: github.ref == "refs/heads/main"
    environment: { name: production }
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying to production"
```

---
## Exercicio 7 - Medio: Estrategia de Rollback e Observabilidade

**Tempo estimado:** 20 min  
**Tema:** Projetar mecanismos de rollback e monitoramento pos-deploy

### Contexto
Um deploy em producao comecou a apresentar erro 500 em 15% das requisicoes 3 minutos apos o deploy. O time levou 45 minutos para identificar e reverter:

- O deploy foi manual (kubectl apply -f deployment.yaml)
- Nao havia health check automatizado
- O rollback foi manual: `kubectl rollout undo deployment/api`
- Nao havia alerta configurado — usuario reportou no Discord
- Nao havia versao anterior identificada

### Tarefa
Projete um sistema de deployment resiliente que evite esse cenario:

1. **Pipeline com rollback automatico** - Crie um job de health check pos-deploy que:
   - Aguarda 2 minutos apos o deploy
   - Verifica 3 endpoints (health, ready, metrics)
   - Se P95 > 500ms OU error rate > 2%: dispara rollback automatico
   - Envia notificacao no Slack com o resumo

2. **Estrategia de versionamento** - Defina:
   - Formato de tag das imagens Docker
   - Como identificar a versao anterior rapidamente
   - Politica de retencao (quantas versoes manter)

3. **Observabilidade** - Defina:
   - 3 metricas essenciais para monitorar pos-deploy
   - 3 logs essenciais que todo endpoint deve emitir
   - 1 dashboard que todo time deveria ter

4. **Runbook de incidente** - Crie um checklist de 6 passos para quando o rollback automatico falhar

### Template
```
### 1. Health Check + Rollback Automatico
```yaml
# GitHub Actions step ou Kubernetes probe
```

### 2. Versionamento
Formato de tag:
Versao anterior:
Retencao:

### 3. Observabilidade
Metricas:
Logs:
Dashboard:

### 4. Runbook de Incidente (quando auto-rollback falha)
1.
2.
3.
4.
5.
6.
```

### Criterios de Correcao
| Criterio | Peso |
|----------|------|
| Health check com metricas e gatilhos claros | 30% |
| Estrategia de versionamento pratica | 20% |
| Observabilidade cobre metricas, logs e dashboard | 25% |
| Runbook com passos iveis e ordenados | 25% |

### Gabarito (resumo)

**1. Health Check:**
```yaml
deploy:
  steps:
    - run: kubectl set image deployment/api api=registry/app:${{ github.sha }}
    - name: Health Check
      run: |
        sleep 120
        for i in 1 2 3 4 5; do
          p95=$(curl -s http://app/metrics | grep p95_latency | awk "{print $2}")
          errors=$(curl -s http://app/metrics | grep error_rate | awk "{print $2}")
          if (( $(echo "$p95 > 500" | bc -l) )) || (( $(echo "$errors > 2" | bc -l) )); then
            kubectl rollout undo deployment/api
            curl -X POST -H "Content-type: application/json" \
              --data "{"text": "ROLLBACK: P95=${p95}ms, Errors=${errors}% para ${{ github.sha }}"}" \
              ${{ secrets.SLACK_WEBHOOK }}
            exit 1
          fi
          sleep 30
        done
```

**2. Versionamento:** `registry/app:git-${{ github.sha }}-${{ github.run_number }}`. Versao anterior: ultima tag no registry. Reter ultimas 5 versoes.

**3. Observabilidade:**
- Metricas: P95 latency, error rate %, requests/min
- Logs: request_id + duration + status_code + error_message (estruturados JSON)
- Dashboard: Deploy timeline + error rate + latency + rollback events

**4. Runbook:**
1. Identificar a versao afetada (git log + deploy history)
2. Notificar equipe no canal de incidentes (#on-call)
3. Reverter para versao estavel anterior (kubectl rollout undo ou docker tag anterior)
4. Verificar health check manualmente (curl + dashboard)
5. Coletar logs do periodo do incidente (kubectl logs --since=10m)
6. Criar ADR documentando causa raiz e prevencao

---

## Resumo - Capitulo 3

| # | Exercicio | Dificuldade | Tema | Tempo |
|---|-----------|-------------|------|-------|
| 1 | Leitura de Pipeline CI/CD | Facil | Interpretar YAML existente | 15 min |
| 2 | Criar Pipeline do Zero | Facil/Medio | GitHub Actions completo | 20 min |
| 3 | Pipeline Multi-Estagio | Medio | SAST + IaC + Migrations | 25 min |
| 4 | Estrategia de Deploy | Medio/Dificil | Canary + Flags + Rollback | 20 min |
| 5 | Runbook + Self-Healing | Dificil | Automacao de resiliencia | 30 min |