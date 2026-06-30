---
title: "Módulo 20 — Automação"
theme: "default"
transition: "slide"
---

# Automação

**Módulo 20** · Transição para cargos seniores/tech lead

---

## Slide 1 — O que é Automação?

> "Automatize tudo que for executado mais de 2 vezes."

- Substituição de processos manuais por scripts e pipelines
- Reduce erro humano, aumenta velocidade e reprodutibilidade
- **Custo vs Benefício:** tempo investido vs frequência de execução

| Benefício | Impacto |
|-----------|---------|
| Redução de erros | ~70% menos incidentes |
| Velocidade | Deploys em minutos, não horas |
| Auditoria | Logs e artefatos automáticos |

---

## Slide 2 — CI/CD: O Coração da Automação

**Continuous Integration:** todo push → build + testes + lint

**Continuous Delivery:** artefato pronto, deploy manual

**Continuous Deployment:** deploy automático após CI passar

```
Push → Lint → Testes → Build → SAST → Deploy → Health Check
```

GitHub Actions e GitLab CI são as plataformas mais usadas no mercado brasileiro.

---

## Slide 3 — Pipeline CI na Prática (GitHub Actions)

```yaml
jobs:
  lint:       # ESLint + Prettier
  test:       # Unit + Integration (com banco real em service)
  build:      # Compilação + artefato
  security:   # SAST + dependency scan
```

```yaml
- uses: actions/checkout@v4
- run: pnpm install --frozen-lockfile
- run: pnpm test:unit
- run: pnpm test:integration
  env:
    DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

---

## Slide 4 — Automação de Testes (Pirâmide)

```
        ⬆ E2E (Playwright, Cypress)
      ⬆⬆ Integração (Supertest, MSW)
    ⬆⬆⬆ Unitários (Vitest, Jest)
  ⬆⬆⬆⬆ Static (ESLint, TypeScript)
```

- **Unitários:** rápidos, isolados, sem side effects
- **Integração:** banco real ou em memória, testa contratos
- **E2E:** fluxo completo, simulando o usuário

Regra: 70% unitários, 20% integração, 10% e2e

---

## Slide 5 — Infraestrutura como Código (IaC)

Gerenciar infraestrutura com arquivos versionados.

| Ferramenta | Abordagem | Exemplo de uso |
|------------|-----------|----------------|
| Terraform | HCL declarativo | Multi-cloud |
| Pulumi | TypeScript/Python | Times que já usam a linguagem |
| CloudFormation | YAML/JSON | AWS nativo |

```
git push → terraform plan → review → terraform apply
```

---

## Slide 6 — Estratégias de Deploy

| Estratégia | Descrição | Rollback |
|------------|-----------|----------|
| **Blue-Green** | Duas versões completas, swap de DNS | Imediato (reverter DNS) |
| **Canary** | % pequena de tráfego na nova versão | Gradual (reduzir %) |
| **Rolling Update** | Substitui instâncias 1 a 1 | Reverter versão |
| **Feature Flag** | Ativa/desativa funcionalidade | Desligar flag |

**Recomendação:** Canary + Feature Flags para produção.

---

## Slide 7 — Automação de Banco de Dados

- **Migrations:** versionadas, executadas no CI
- **Seed:** dados iniciais para ambiente de teste
- **Rollback automático:** backup antes da migration

```yaml
- name: Backup
  run: pg_dump $DATABASE_URL > /tmp/backup.sql
- name: Migrate
  run: pnpm db:migrate
- name: Rollback (se falhar)
  if: failure()
  run: psql $DATABASE_URL < /tmp/backup.sql
```

---

## Slide 8 — Automação de Segurança

**SAST** (estático): código parado, analisa padrões inseguros
**DAST** (dinâmico): aplicação rodando, simula ataques
**SCA** (dependências): bibliotecas com CVEs conhecidas

Ferramentas no pipeline:
- SonarQube/SonarCloud — qualidade e segurança
- Snyk / Dependabot — varredura de dependências
- Trivy — containers
- CodeQL — análise semântica do GitHub

---

## Slide 9 — Code Review Automatizado

Bots e linters que revisam código antes do review humano.

| Ferramenta | Função |
|------------|--------|
| Dependabot | PRs automáticos de atualização de dep |
| CodeQL | Análise de segurança |
| ESLint + Prettier | Padronização de código |
| GitHub Status Checks | Gate para merge |

> Automatize o óbvio para que humanos foquem no que importa: arquitetura e lógica de negócio.

---

## Slide 10 — Releases Automatizadas

**Semantic Release** + **Conventional Commits**:

```
feat: → minor (1.2.0 → 1.3.0)
fix:  → patch (1.2.0 → 1.2.1)
BREAKING CHANGE: → major (1.2.0 → 2.0.0)
```

Gera automaticamente:
- Changelog
- Tag no GitHub
- Publicação no npm
- Nota de release

---

## Slide 11 — Ambientes Efêmeros (Preview Deployments)

Ambiente criado automaticamente para cada PR.

```
Branch feature/login → Deploy → https://pr-42.app.io
Branch main          → Deploy → https://staging.app.io
Tag v1.0.0           → Deploy → https://app.io (prod)
```

**Duração:** enquanto o PR estiver aberto  
**Destruição automática:** ao fechar o PR  

Ferramentas: Vercel, Render, Railway, ECS + RDS efêmero

---

## Slide 12 — Monitoramento e Self-Healing

**Alertas automáticos:** Datadog, Grafana, New Relic

**Self-healing:** scripts que detectam falha e corrigem sem intervenção humana

```typescript
if (running < desired) {
  await ecs.send(new UpdateServiceCommand({
    forceNewDeployment: true,
  }))
}
```

**Runbooks automáticos:** workflows que executam receitas de recuperação com um clique.

---

## Slide 13 — Pipeline as Code: Boas Práticas

1. **Modularize:** crie actions compostas reutilizáveis
2. **Cache:** dependências, build, Docker layers
3. **Fail fast:** jobs rápidos primeiro (lint antes de e2e)
4. **Idempotência:** mesma pipeline, mesmo resultado
5. **Segurança:** secrets nunca em plain text
6. **Observabilidade:** métricas de pipeline (tempo, falha, MTTR)

```yaml
# Job reutilizável
- uses: ./.github/actions/setup-node
- run: pnpm test
```

---

## Slide 14 — Exemplo de Pipeline Completa

```
[Push] → [Lint & Format] → [Testes Unitários]
                                  ↓
                           [Testes Integração]
                                  ↓
                              [Build]
                                  ↓
                    ┌─────────────┴─────────────┐
                    ↓                           ↓
            [SAST Security]           [Deploy Preview]
                    ↓
           [Dependency Scan]
                    ↓
           [Deploy Staging]
                    ↓
           [Testes E2E]
                    ↓
           [Deploy Production]
                    ↓
           [Health Check]
                    ↓
           [Monitoramento]
```

---

## Slide 15 — Conclusão

Automação não é um projeto, é uma **cultura**.

- Toda tarefa manual é uma dívida técnica
- Pipeline quebrada = esteira de produção parada
- Invista em automação como investiria em testes

**Meta:** deploy em produção com 1 clique (ou automático), com confiança e segurança.

> "Se você está fazendo algo pela segunda vez, automatize."

---

## Referências Rápidas

- GitHub Actions docs
- GitLab CI docs
- Terraform by HashiCorp
- semantic-release
- Conventional Commits
- Playwright / Vitest
