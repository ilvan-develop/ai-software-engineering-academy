---
marp: true
theme: uncover
class:
  - lead
  - invert
---

<!-- _class: lead invert -->
<!-- _backgroundColor: "#1A1A2E" -->
<!-- _color: "#FFFFFF" -->

# **IA para Desenvolvedores**

**CapÃ­tulo 3 â€” AutomaÃ§Ã£o do Ciclo de Desenvolvimento com IA**

---

AI Software Engineering Academy â€” 2026

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Agenda

- O que Ã© automaÃ§Ã£o e por que automatizar
- CI/CD â€” Pipeline de IntegraÃ§Ã£o e Deploy ContÃ­nuo
- AutomaÃ§Ã£o de Testes (pirÃ¢mide de testes)
- IaC â€” Infraestrutura como CÃ³digo
- EstratÃ©gias de Deploy (Blue-Green, Canary, Rolling)
- AutomaÃ§Ã£o: Banco, SeguranÃ§a e Code Review
- Releases, Ambientes EfÃªmeros e Monitoramento
- Pipeline as Code â€” Boas PrÃ¡ticas

*Nota do apresentador: MÃ³dulo denso em cÃ³digo. Foque nos conceitos, use exemplos como referÃªncia.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## O que Ã© AutomaÃ§Ã£o?

**DefiniÃ§Ã£o:** Substituir processos manuais repetitivos por scripts e pipelines confiÃ¡veis.

| Motivo | Impacto |
|--------|---------|
| Reduz erro humano | Maior causa de incidentes |
| Velocidade | Segundos vs horas |
| Reprodutibilidade | Mesmo resultado sempre |
| Auditoria | Logs como evidÃªncia |
| Escala | 1 deploy manual falha em 100 |

**Regra prÃ¡tica:** Automatize tudo que for executado **mais de 2 vezes**.

```
Custo = (tempo_criar + tempo_manter) * custo_hora
Beneficio = (tempo_por_exec * frequencia * horizonte) - custo
Se beneficio > 0 em 6 meses, automatize.
```

*Nota do apresentador: A regra das 2 execuÃ§Ãµes Ã© um bom filtro prÃ¡tico.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## CI/CD â€” Espinha Dorsal da AutomaÃ§Ã£o

**Continuous Integration (CI):** Todo push dispara:
1. Checkout + dependÃªncias
2. Linting + formataÃ§Ã£o
3. Testes unitÃ¡rios + integraÃ§Ã£o
4. Build
5. AnÃ¡lise de seguranÃ§a

**Continuous Delivery vs Deployment:**

| EstratÃ©gia | Deploy produÃ§Ã£o |
|------------|----------------|
| **CDelivery** | Artefato pronto, deploy manual (gate humano) |
| **CDeployment** | Deploy automÃ¡tico apÃ³s CI passar |

[imagem: diagrama do pipeline CI/CD: push -> CI -> CD -> deploy]

*Nota do apresentador: CD com deploy automÃ¡tico Ã© o padrÃ£o em times maduros. Gates sÃ£o para compliance.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Pipeline CI na PrÃ¡tica â€” GitHub Actions

```yaml
name: CI Pipeline
on:
  push: {branches: [main, develop]}
  pull_request: {branches: [main]}

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pnpm install --frozen-lockfile
      - run: pnpm lint
      - run: pnpm format:check

  test:
    needs: lint
    services:
      postgres: {image: postgres:16-alpine}
    steps:
      - run: pnpm test:unit
      - run: pnpm test:integration

  build:
    needs: test
    steps:
      - run: pnpm build
```

**Fail Fast:** lint (rapido) -> test (medio) -> build (lento)

*Nota do apresentador: Destaque o encadeamento (needs). Fail fast = feedback em segundos.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## AutomaÃ§Ã£o de Testes â€” PirÃ¢mide

```
            /\
           /  \         E2E (poucos, lentos,
          /    \        simulam usuario real)
         /______\
        /        \      Integracao (medios,
       /          \     testam interacao entre modulos)
      /____________\
     /              \   Unitarios (muitos, rapidos,
    /                \  testam uma unidade isolada)
   /__________________\
```

| Camada | Ferramentas | Velocidade | Cobertura |
|--------|------------|:--------:|:---------:|
| UnitÃ¡rios | Vitest, Jest | ms | Alta |
| IntegraÃ§Ã£o | Supertest, Prisma | s | MÃ©dia |
| E2E | Playwright, Cypress | min | CrÃ­tico |

*Nota do apresentador: Base larga = feedback rÃ¡pido. Topo estreito = sÃ³ o crÃ­tico. Inverta a pirÃ¢mide e seu pipeline vai demorar horas.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## IaC â€” Infraestrutura como CÃ³digo

Infraestrutura versionada, revisada e reproduzÃ­vel.

| Ferramenta | Abordagem | Diferencial |
|------------|-----------|-------------|
| **Terraform** | Declarativa (HCL) | Multi-cloud, estado remoto |
| **Pulumi** | Linguagens reais | TypeScript com tipos |
| **CloudFormation** | YAML/JSON | Nativo AWS |

```hcl
resource "aws_ecs_service" "app" {
  name           = "app-service"
  cluster        = aws_ecs_cluster.main.id
  desired_count  = 2
  launch_type    = "FARGATE"
}
```

> IaC transforma infra em cÃ³digo reviewÃ¡vel. Nunca mais "alguÃ©m entrou no servidor e mudou algo".

*Nota do apresentador: Prefira Pulumi se o time jÃ¡ usa TypeScript. Terraform se precisar de multi-cloud.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## EstratÃ©gias de Deploy

[imagem: diagramas visuais das 3 estratÃ©gias]

**Blue-Green:** Duas versÃµes. Balancer muda trÃ¡fego. Rollback = reverter DNS.

```
Usuarios -> LB -> Blue (v1.0)
               -> Green (v1.1) <- apos validacao
```

**Canary:** % pequena do trÃ¡fego para nova versÃ£o. Aumenta gradualmente (10% -> 50% -> 100%).

**Rolling Update:** Substitui instÃ¢ncias uma a uma. Zero downtime.

| EstratÃ©gia | Rollback | Complexidade |
|------------|:-------:|:----------:|
| Blue-Green | Imediato | MÃ©dia |
| Canary | Gradual | Alta |
| Rolling | Gradual | Baixa |

*Nota do apresentador: Blue-Green Ã© padrÃ£o ouro para sistemas crÃ­ticos. Canary para times maduros.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## AutomaÃ§Ã£o de Banco e SeguranÃ§a

**Banco â€” Migrations no Pipeline:**

```yaml
- name: Backup antes da migration
  run: pg_dump $DATABASE_URL > /tmp/backup.sql
- name: Rodar migration
  id: migrate
  run: pnpm db:migrate
  continue-on-error: true
- name: Rollback em caso de falha
  if: steps.migrate.outcome != 'success'
  run: psql $DATABASE_URL < /tmp/backup.sql
```

**SeguranÃ§a â€” 3 camadas no pipeline:**

| Camada | Ferramentas | O que detecta |
|--------|-------------|---------------|
| **SAST** | SonarQube, CodeQL, ESLint | Vulnerabilidades no cÃ³digo fonte |
| **Dependency** | Snyk, Dependabot, npm audit | Bibliotecas com CVEs |
| **DAST** | OWASP ZAP | Ataques simulados em staging |

*Nota do apresentador: SAST roda em segundos, DAST em minutos. Organize por velocidade.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## AutomaÃ§Ã£o de Code Review e Releases

**Code Review automÃ¡tico com bots:**

```yaml
code-review:
  steps:
    - run: pnpm lint && pnpm format:check
    - name: Verificar tamanho do PR
      uses: actions/github-script@v7
      with:
        script: |
          if (changedFiles > 20) core.warning("PR grande")
          if (additions > 500) core.warning("Muitas linhas")
    - name: CodeQL Analysis
      uses: github/codeql-action/analyze@v3
```

**Releases com Semantic Versioning:**

```
feat: adiciona PIX          -> MINOR (1.x.0)
fix: corrige validaÃ§Ã£o CPF  -> PATCH (x.1.0)
BREAKING CHANGE: refatora   -> MAJOR (x.0.1)
```

Ferramenta: **semantic-release** â€” gera versÃ£o + changelog automaticamente.

*Nota do apresentador: Conventional Commits Ã© prÃ©-requisito. Sem ele, nÃ£o hÃ¡ versionamento automÃ¡tico.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Ambientes EfÃªmeros e Monitoramento

**Preview Deployments:** Ambiente temporÃ¡rio para cada branch.

```
Branch feature/x -> CI detecta PR -> Cria banco + servico
  -> URL: https://pr-42.meusistema.com.br
  -> PR mergeado -> Destroy (remove tudo)
```

Ferramentas: Vercel (front-end), ECS efÃªmero, Railway, Render.

**Self-Healing:** Script que recupera automaticamente:

```typescript
// Se running < desired, forca novo deploy
if (running < desired) {
  await ecs.updateService({forceNewDeployment: true});
}
```

**Runbook
