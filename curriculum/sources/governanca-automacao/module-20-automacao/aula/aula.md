# Módulo 20 — Automação

**Duração estimada:** 5 dias (~40h)  
**Público-alvo:** Desenvolvedores brasileiros em transição para cargos seniores/tech lead  
**Pré-requisitos:** Conhecimento básico de Git, terminal Linux, conceitos de deploy

---

## 1. O que é Automação

Automação é a substituição de processos manuais repetitivos por scripts, pipelines e ferramentas que executam essas tarefas de forma confiável, auditável e escalável.

### Por que automatizar?

| Motivo | Impacto |
|--------|---------|
| Reduzir erro humano | O maior causador de incidentes em produção ainda é o operador humano |
| Velocidade | Máquinas executam em segundos o que levaria horas manualmente |
| Reprodutibilidade | O mesmo pipeline executa exatamente da mesma forma todas as vezes |
| Auditoria | Logs e artefatos gerados automaticamente servem como evidência |
| Escala | O que funciona para 1 deploy falha para 100 deploys manuais |

### Onde automatizar

- Build e compilação
- Testes (unitários, integração, e2e)
- Linting e formatação de código
- Verificação de segurança
- Deploy em ambientes
- Migrações de banco de dados
- Geração de changelog e release
- Monitoramento e alertas
- Criação e destruição de ambientes

### Custo vs Benefício

A regra prática: **automatize tudo que for executado mais de 2 vezes.**

```text
Custo de automatizar = (tempo para criar + tempo para manter) × custo-hora
Benefício = (tempo economizado por execução × frequência × horizonte) - custo
```markdown

Se o benefício for positivo em 6 meses, vale a pena automatizar.

---

## 2. CI/CD — Pipelines de Integração e Deploy Contínuo

CI/CD é a espinha dorsal da automação em engenharia de software.

### Continuous Integration (CI)

Todo push para branches compartilhadas dispara:
1. Checkout do código
2. Instalação de dependências
3. Linting
4. Testes unitários
5. Testes de integração
6. Build
7. Análise de segurança

### Continuous Delivery / Continuous Deployment (CD)

- **Continuous Delivery:** O artefato é gerado e publicado em um repositório, mas o deploy em produção é manual (aprovado por um humano).
- **Continuous Deployment:** O deploy em produção é automático após a pipeline CI passar.

### GitHub Actions — Exemplo Real

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  NODE_VERSION: 20.x
  PNPM_VERSION: 9

jobs:
  lint:
    name: Lint e Formatação
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v3
        with:
          version: ${{ env.PNPM_VERSION }}
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: pnpm
      - run: pnpm install --frozen-lockfile
      - run: pnpm lint
      - run: pnpm format:check

  test:
    name: Testes
    needs: lint
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_DB: app_test
          POSTGRES_USER: app
          POSTGRES_PASSWORD: secret
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v3
        with:
          version: ${{ env.PNPM_VERSION }}
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: pnpm
      - run: pnpm install --frozen-lockfile
      - run: pnpm test:unit
      - run: pnpm test:integration
        env:
          DATABASE_URL: postgres://app:secret@localhost:5432/app_test

  build:
    name: Build
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v3
        with:
          version: ${{ env.PNPM_VERSION }}
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: pnpm
      - run: pnpm install --frozen-lockfile
      - run: pnpm build
      - uses: actions/upload-artifact@v4
        with:
          name: build-output
          path: dist/
```text

### GitLab CI — Exemplo Real

```yaml
# .gitlab-ci.yml
stages:
  - lint
  - test
  - build
  - deploy

variables:
  NODE_VERSION: "20"
  PNPM_VERSION: "9"

cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .pnpm-store/

lint:
  stage: lint
  image: node:${NODE_VERSION}
  script:
    - npm install -g pnpm@${PNPM_VERSION}
    - pnpm install --frozen-lockfile
    - pnpm lint
    - pnpm format:check

test:
  stage: test
  image: node:${NODE_VERSION}
  services:
    - postgres:16-alpine
  variables:
    DATABASE_URL: postgres://app:secret@postgres:5432/app_test
    POSTGRES_DB: app_test
    POSTGRES_USER: app
    POSTGRES_PASSWORD: secret
  script:
    - npm install -g pnpm@${PNPM_VERSION}
    - pnpm install --frozen-lockfile
    - pnpm test:unit
    - pnpm test:integration

build:
  stage: build
  image: node:${NODE_VERSION}
  script:
    - npm install -g pnpm@${PNPM_VERSION}
    - pnpm install --frozen-lockfile
    - pnpm build
  artifacts:
    paths:
      - dist/
    expire_in: 30 days

deploy:
  stage: deploy
  image: alpine:latest
  script:
    - apk add --no-cache curl
    - curl -X POST "${DEPLOY_HOOK_URL}"
  only:
    - main
  when: manual
  environment: production
```markdown

---

## 3. Automação de Testes

A pipeline de CI deve executar testes em camadas, respeitando a **pirâmide de testes**.

### Testes Unitários

Executados primeiro — são rápidos e isolados.

```typescript
// Exemplo com vitest
import { describe, it, expect } from 'vitest'
import { calculateDiscount } from './pricing'

describe('calculateDiscount', () => {
  it('aplica 10% para compras acima de R$ 100', () => {
    expect(calculateDiscount(150)).toBe(135)
  })

  it('não aplica desconto para compras abaixo de R$ 100', () => {
    expect(calculateDiscount(50)).toBe(50)
  })

  it('lança erro para valores negativos', () => {
    expect(() => calculateDiscount(-10)).toThrow('Valor inválido')
  })
})
```text

### Testes de Integração

Testam a interação entre módulos, geralmente com banco de dados real ou em memória.

```typescript
import { describe, it, expect, beforeAll, afterAll } from 'vitest'
import { createApp } from './app'
import { prisma } from './lib/prisma'

const app = createApp()

describe('POST /users', () => {
  beforeAll(async () => {
    await prisma.$executeRawUnsafe('TRUNCATE TABLE users CASCADE')
  })

  afterAll(async () => {
    await prisma.$disconnect()
  })

  it('cria um usuário com dados válidos', async () => {
    const response = await app.inject({
      method: 'POST',
      url: '/users',
      payload: { name: 'João', email: 'joao@email.com' },
    })

    expect(response.statusCode).toBe(201)
    expect(response.json()).toHaveProperty('id')
  })
})
```markdown

### Testes E2E

Testam o sistema como um todo, simulando o usuário real.

```yaml
# job no CI para E2E
e2e:
  name: Testes End-to-End
  needs: build
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: pnpm/action-setup@v3
      with:
        version: ${{ env.PNPM_VERSION }}
    - uses: actions/setup-node@v4
      with:
        node-version: ${{ env.NODE_VERSION }}
        cache: pnpm
    - run: pnpm install --frozen-lockfile
    - run: pnpm build
    - run: pnpm dlx playwright install --with-deps
    - run: pnpm test:e2e
      env:
        BASE_URL: http://localhost:3000
```text

```typescript
// E2E com Playwright
import { test, expect } from '@playwright/test'

test('usuário consegue finalizar compra', async ({ page }) => {
  await page.goto('/produtos')
  await page.click('text=Adicionar ao carrinho')
  await page.click('text=Finalizar compra')
  await page.fill('[name=email]', 'joao@email.com')
  await page.click('text=Confirmar')

  await expect(page.locator('text=Pedido confirmado')).toBeVisible()
})
```markdown

---

## 4. Automação de Infraestrutura — IaC

Infrastructure as Code (IaC) é o gerenciamento de infraestrutura (servidores, bancos, redes) através de arquivos de configuração versionados.

### Terraform (HashiCorp)

```hcl
# main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket = "meu-terraform-state"
    key    = "prod/terraform.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_ecs_service" "app" {
  name            = "app-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = 2
  launch_type     = "FARGATE"

  network_configuration {
    subnets         = var.private_subnet_ids
    security_groups = [aws_security_group.app.id]
  }

  deployment_controller {
    type = "CODE_DEPLOY"  # blue/green
  }
}
```text

### Pulumi

IaC com linguagens de programação reais (TypeScript, Python, Go, C#).

```typescript
import * as aws from '@pulumi/aws'
import * as pulumi from '@pulumi/pulumi'

const config = new pulumi.Config()
const stack = pulumi.getStack()

const cluster = new aws.ecs.Cluster('app-cluster')

const taskDefinition = new aws.ecs.TaskDefinition('app-task', {
  family: 'app',
  cpu: '256',
  memory: '512',
  networkMode: 'awsvpc',
  executionRoleArn: config.require('executionRoleArn'),
  containerDefinitions: JSON.stringify([
    {
      name: 'app',
      image: `meuregistro/app:${stack}`,
      portMappings: [{ containerPort: 3000 }],
    },
  ]),
})

new aws.ecs.Service('app-service', {
  cluster: cluster.arn,
  taskDefinition: taskDefinition.arn,
  desiredCount: 2,
  launchType: 'FARGATE',
  networkConfiguration: {
    subnets: config.requireObject<string[]>('privateSubnets'),
    securityGroups: [config.require('securityGroupId')],
  },
})
```markdown

### CloudFormation (AWS)

Template declarativo em YAML/JSON para recursos AWS.

```yaml
# template.yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "Stack da aplicação"

Parameters:
  Env:
    Type: String
    Default: production

Resources:
  ECSCluster:
    Type: AWS::ECS::Cluster
    Properties:
      ClusterName: !Sub "app-cluster-${Env}"

  AppService:
    Type: AWS::ECS::Service
    Properties:
      ServiceName: !Sub "app-service-${Env}"
      Cluster: !Ref ECSCluster
      LaunchType: FARGATE
      DesiredCount: 2
      TaskDefinition: !Ref AppTaskDefinition
      NetworkConfiguration:
        AwsvpcConfiguration:
          Subnets:
            - !Ref PrivateSubnet1
            - !Ref PrivateSubnet2
```text

### Pipeline para IaC

```yaml
iac-plan:
  name: Terraform Plan
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: hashicorp/setup-terraform@v3
      with:
        terraform_version: 1.8.0
    - run: terraform init
    - run: terraform fmt -check
    - run: terraform validate
    - run: terraform plan -out=tfplan
    - uses: actions/upload-artifact@v4
      with:
        name: tfplan
        path: tfplan

iac-apply:
  name: Terraform Apply
  needs: iac-plan
  runs-on: ubuntu-latest
  if: github.ref == 'refs/heads/main'
  environment: production
  steps:
    - uses: actions/checkout@v4
    - uses: hashicorp/setup-terraform@v3
    - run: terraform init
    - uses: actions/download-artifact@v4
      with:
        name: tfplan
    - run: terraform apply tfplan
```markdown

---

## 5. Automação de Deploys

### Blue-Green Deployment

Duas versões do ambiente (blue = atual, green = nova). O balanceador de carga muda o tráfego da blue para a green.

```text
USUÁRIOS → Load Balancer → Blue (v1.0) ✅
                         → Green (v1.1) 🟢 (após validação)

Switch: DNS/ALB aponta para Green
Rollback: reverter DNS para Blue
```markdown

### Canary Deployment

Uma porcentagem pequena do tráfego vai para a nova versão. Aos poucos, aumenta-se até 100%.

```yaml
# Apropriado para Kubernetes com Argo Rollouts
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: app-rollout
spec:
  replicas: 10
  revisionHistoryLimit: 2
  selector:
    matchLabels:
      app: meu-app
  template:
    metadata:
      labels:
        app: meu-app
    spec:
      containers:
        - name: app
          image: meuregistro/app:1.1.0
  strategy:
    canary:
      steps:
        - setWeight: 10
        - pause: { duration: 5m }
        - setWeight: 50
        - pause: { duration: 5m }
        - setWeight: 100
```text

### Rolling Update

Substitui instâncias gradualmente, sem tempo de inatividade.

```yaml
# docker-compose.yml com rolling update no Swarm
version: "3.8"
services:
  app:
    image: meuregistro/app:${VERSION}
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
        order: start-first
      rollback_config:
        parallelism: 1
        order: stop-first
```markdown

### Feature Flags

Permitem ativar/desativar funcionalidades em produção sem fazer deploy.

```typescript
import { createClient } from '@configu/sdk'

const configu = createClient({ apiKey: process.env.CONFIGU_KEY })

async function handler(req, res) {
  const novoCheckout = await configu.getFlag('checkout-v2-enabled')

  if (novoCheckout && req.user.id in novoCheckout.targeting) {
    return handleCheckoutV2(req, res)
  }

  return handleCheckoutV1(req, res)
}
```text

**Ferramentas:** LaunchDarkly, Configu, GrowthBook, Unleash, Flagsmith.

---

## 6. Automação de Banco de Dados

### Migrations Automáticas no CI

```yaml
# Job de migration
migrate:
  name: Rodar Migrations
  needs: build
  runs-on: ubuntu-latest
  environment: ${{ github.ref == 'refs/heads/main' && 'production' || 'staging' }}
  steps:
    - uses: actions/checkout@v4
    - uses: pnpm/action-setup@v3
    - uses: actions/setup-node@v4
    - run: pnpm install --frozen-lockfile
    - run: pnpm build
    - uses: actions/download-artifact@v4
      with:
        name: build-output
        path: dist
    - run: pnpm db:migrate
      env:
        DATABASE_URL: ${{ secrets.DATABASE_URL }}
```markdown

### Exemplo com Prisma Migrate

```typescript
// scripts/migrate.ts
import { execSync } from 'node:child_process'

const env = process.env.NODE_ENV || 'development'

function run() {
  console.log(`▶ Rodando migrations em ${env}...`)

  // Validar se a migration é segura (não dropa colunas sem verificação)
  execSync('pnpm prisma migrate deploy', {
    stdio: 'inherit',
    env: { ...process.env, DATABASE_URL: process.env.DATABASE_URL },
  })

  console.log('✅ Migrations executadas com sucesso')
}

run()
```text

### Seed Automático em CI

```typescript
// scripts/seed.ts
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

async function seed() {
  console.log('🌱 Iniciando seed...')

  await prisma.tenant.create({
    data: {
      name: 'Default',
      slug: 'default',
      users: {
        create: {
          email: 'admin@empresa.com',
          role: 'ADMIN',
        },
      },
    },
  })

  console.log('✅ Seed concluído')
}

seed()
  .catch((e) => {
    console.error(e)
    process.exit(1)
  })
  .finally(() => prisma.$disconnect())
```yaml

### Rollback Automático

Estratégia: antes de rodar a migration, fazer backup; se a migration falhar, restaurar.

```yaml
# Rollback automático
- name: Backup antes da migration
  run: pg_dump $DATABASE_URL > /tmp/pre_migration_backup.sql
  env:
    DATABASE_URL: ${{ secrets.DATABASE_URL }}

- name: Rodar migration
  id: migrate
  run: pnpm db:migrate
  continue-on-error: true
  env:
    DATABASE_URL: ${{ secrets.DATABASE_URL }}

- name: Rollback em caso de falha
  if: steps.migrate.outcome != 'success'
  run: |
    echo "🔄 Migration falhou — restaurando backup..."
    psql $DATABASE_URL < /tmp/pre_migration_backup.sql
    echo "✅ Backup restaurado"
  env:
    DATABASE_URL: ${{ secrets.DATABASE_URL }}
```text

---

## 7. Automação de Segurança

### SAST (Static Application Security Testing)

Análise estática de segurança diretamente no pipeline.

```yaml
security-sast:
  name: Análise Estática (SAST)
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: pnpm/action-setup@v3
    - uses: actions/setup-node@v4
    - run: pnpm install --frozen-lockfile

    # ESLint com plugins de segurança
    - name: ESLint Security
      run: pnpm dlx eslint . --ext .ts --rulesdir eslint-security-rules

    # SonarQube
    - name: SonarQube Scan
      uses: sonarsource/sonarcloud-github-action@master
      env:
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
      with:
        args: >
          -Dsonar.organization=minha-org
          -Dsonar.projectKey=meu-projeto
          -Dsonar.javascript.lcov.reportPaths=coverage/lcov.info

    # Trivy para vulnerabilidades em container
    - name: Trivy Scan
      uses: aquasecurity/trivy-action@master
      with:
        image-ref: meuregistro/app:${{ github.sha }}
        format: sarif
        output: trivy-results.sarif
```markdown

### DAST (Dynamic Application Security Testing)

Testa a aplicação rodando, simulando ataques reais.

```yaml
security-dast:
  name: Teste Dinâmico (DAST)
  needs: deploy-staging
  runs-on: ubuntu-latest
  steps:
    - name: OWASP ZAP Scan
      uses: zaproxy/action-full-scan@v0.10
      with:
        target: https://staging.meusistema.com.br
        rules_file_name: .zap/rules.tsv
        cmd_options: "-a -j"
```text

### Dependency Scanning

```yaml
dependency-scan:
  name: Varredura de Dependências
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: pnpm/action-setup@v3
    - uses: actions/setup-node@v4
    - run: pnpm install --frozen-lockfile

    # Snyk
    - name: Snyk Scan
      uses: snyk/actions/node@master
      env:
        SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
      with:
        args: --severity-threshold=medium

    # Dependabot alerts (nativo do GitHub)
    # npm audit
    - name: npm audit
      run: pnpm audit --audit-level=high
```markdown

---

## 8. Automação de Code Review

### Bots no Pipeline

```yaml
code-review:
  name: Revisão Automática
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0

    # Linters automáticos
    - uses: pnpm/action-setup@v3
    - uses: actions/setup-node@v4
    - run: pnpm install --frozen-lockfile
    - run: pnpm lint
    - run: pnpm format:check

    # Status checks
    - name: Verificar tamanho do PR
      uses: actions/github-script@v7
      with:
        script: |
          const { data: pr } = await github.rest.pulls.get({
            ...context.repo,
            pull_number: context.issue.number,
          })
          const changedFiles = pr.changed_files
          const additions = pr.additions

          if (changedFiles > 20) {
            core.warning(`⚠️ PR grande: ${changedFiles} arquivos alterados`)
          }
          if (additions > 500) {
            core.warning(`⚠️ Muitas linhas adicionadas: ${additions}`)
          }

    # CodeQL
    - name: Initialize CodeQL
      uses: github/codeql-action/init@v3
      with:
        languages: javascript-typescript

    - name: CodeQL Analysis
      uses: github/codeql-action/analyze@v3
      with:
        category: /language:javascript

    # Dependabot (configurado no .github/dependabot.yml)
```text

### Dependabot Configuration

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
    open-pull-requests-limit: 10
    labels:
      - "dependencies"
      - "automated"
    reviewers:
      - "time-squad"
    commit-message:
      prefix: "chore"
      include: "scope"
```markdown

---

## 9. Automação de Releases

### Semantic Versioning Automático

```yaml
release:
  name: Gerar Release
  needs: build
  runs-on: ubuntu-latest
  if: github.ref == 'refs/heads/main'
  permissions:
    contents: write
    packages: write
  steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0

    # Análise de commits para versionamento semântico
    - name: Semantic Release
      uses: cycjimmy/semantic-release-action@v4
      id: semantic
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
      with:
        extra_plugins: |
          @semantic-release/changelog
          @semantic-release/git
          @semantic-release/npm

    - name: Publicar no npm
      if: steps.semantic.outputs.new_release_published == 'true'
      run: |
        echo "📦 Publicando versão ${{ steps.semantic.outputs.new_release_version }}"
        npm publish
      env:
        NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```text

### Conventional Commits

O `semantic-release` depende do padrão **Conventional Commits**:

```text
feat: adiciona calculadora de impostos
feat(api): nova rota de relatórios
fix: corrige validação de CPF
fix(auth): timeout na renovação do token
chore: atualiza dependências
docs: atualiza README
refactor: extrai lógica de pagamento para serviço
perf: otimiza consulta de histórico
test: adiciona testes para o módulo de notas fiscais
```markdown

### Changelog Gerado Automaticamente

O `semantic-release` com plugin `@semantic-release/changelog` gera:

```markdown
# Changelog

## [1.5.0](https://github.com/org/repo/compare/v1.4.0...v1.5.0) (2025-06-15)

### Features
* **pagamento:** adiciona suporte a PIX ([abc1234](https://github.com/org/repo/commit/abc1234))
* **relatorios:** nova rota de exportação CSV ([def5678](https://github.com/org/repo/commit/def5678))

### Bug Fixes
* **auth:** corrige timeout na renovação do token ([ghi9012](https://github.com/org/repo/commit/ghi9012))
* **validacao:** CPF com formatação agora é aceito ([jkl3456](https://github.com/org/repo/commit/jkl3456))
```markdown

---

## 10. Automação de Ambientes

### Ephemeral Environments

Ambientes temporários criados automaticamente para cada branch de feature.

```yaml
deploy-preview:
  name: Deploy Preview
  runs-on: ubuntu-latest
  if: github.event_name == 'pull_request'
  environment:
    name: preview-${{ github.event.number }}
    url: https://pr-${{ github.event.number }}.meusistema.com.br
  steps:
    - uses: actions/checkout@v4
    - uses: pnpm/action-setup@v3
    - uses: actions/setup-node@v4
    - run: pnpm install --frozen-lockfile
    - run: pnpm build

    # Criar banco efêmero
    - name: Criar database preview
      run: |
        aws rds create-db-instance \
          --db-instance-identifier app-preview-${{ github.event.number }} \
          --db-instance-class db.t3.micro \
          --engine postgres \
          --master-username preview \
          --master-user-password ${{ secrets.PREVIEW_DB_PASSWORD }}

    - name: Rodar migrations
      run: pnpm db:migrate
      env:
        DATABASE_URL: postgres://preview:${{ secrets.PREVIEW_DB_PASSWORD }}@preview-db/app-preview-${{ github.event.number }}

    - name: Fazer deploy no ECS
      run: |
        aws ecs update-service \
          --cluster preview \
          --service app-preview-${{ github.event.number }} \
          --force-new-deployment

destroy-preview:
  name: Destruir Preview
  runs-on: ubuntu-latest
  if: github.event_name == 'pull_request' && github.event.action == 'closed'
  steps:
    - name: Remover database preview
      run: |
        aws rds delete-db-instance \
          --db-instance-identifier app-preview-${{ github.event.number }} \
          --skip-final-snapshot

    - name: Remover serviço ECS
      run: |
        aws ecs delete-service \
          --cluster preview \
          --service app-preview-${{ github.event.number }} \
          --force
```text

### Preview Deployments (Vercel / Render)

```yaml
vercel-preview:
  name: Vercel Preview
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: amondnet/vercel-action@v25
      with:
        vercel-token: ${{ secrets.VERCEL_TOKEN }}
        vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
        vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
        github-token: ${{ secrets.GITHUB_TOKEN }}
        github-comment: true
```markdown

---

## 11. Automação de Monitoramento

### Alertas Automáticos

```yaml
monitoring-setup:
  name: Configurar Alertas
  runs-on: ubuntu-latest
  steps:
    - name: Configurar Datadog Monitors
      uses: datadog/synthetics-ci-github-action@v1
      with:
        api_key: ${{ secrets.DD_API_KEY }}
        app_key: ${{ secrets.DD_APP_KEY }}
        public_ids: ${{ vars.DATADOG_SYNTHETIC_TESTS }}

    - name: Configurar alerta de latência P99
      run: |
        curl -X POST "https://api.datadoghq.com/api/v1/monitor" \
          -H "Content-Type: application/json" \
          -H "DD-API-KEY: ${{ secrets.DD_API_KEY }}" \
          -H "DD-APPLICATION-KEY: ${{ secrets.DD_APP_KEY }}" \
          -d '{
            "name": "Latência P99 > 500ms",
            "type": "query alert",
            "query": "avg(last_5m):p99(trace.http.request.duration{service:app}) > 500",
            "message": "Latência alta detectada! @time-squad",
            "tags": ["service:app", "severity:critical"]
          }'
```text

### Self-Healing

```typescript
// scripts/self-healing.ts
import { ECSClient, DescribeServicesCommand, UpdateServiceCommand } from '@aws-sdk/client-ecs'

const ecs = new ECSClient({ region: 'us-east-1' })

async function healService(cluster: string, service: string) {
  const { services } = await ecs.send(
    new DescribeServicesCommand({ cluster, services: [service] })
  )

  const svc = services![0]
  const running = svc.runningCount ?? 0
  const desired = svc.desiredCount ?? 0

  if (running < desired) {
    console.log(`🔧 Service ${service} com ${running}/${desired} — forcando novo deploy...`)

    await ecs.send(
      new UpdateServiceCommand({
        cluster,
        service,
        forceNewDeployment: true,
      })
    )

    console.log('✅ Deploy forcado enviado')
  } else {
    console.log(`✅ Service ${service} saudavel (${running}/${desired})`)
  }
}

healService('production', 'app-service').catch(console.error)
```markdown

### Runbooks Automáticos

```yaml
# runbook: recuperacao-banco.yml
name: Runbook - Recuperar Database
on:
  workflow_dispatch:
    inputs:
      database_name:
        description: 'Nome do banco'
        required: true
      restore_point:
        description: 'PITR timestamp (YYYY-MM-DD HH:MM:SS)'
        required: false

jobs:
  restore:
    runs-on: ubuntu-latest
    steps:
      - name: Validar parâmetros
        run: |
          if [ -z "${{ inputs.database_name }}" ]; then
            echo "❌ database_name é obrigatório"
            exit 1
          fi

      - name: Parar aplicação
        run: |
          aws ecs update-service \
            --cluster production \
            --service app-service \
            --desired-count 0

      - name: Restaurar snapshot
        run: |
          if [ -n "${{ inputs.restore_point }}" ]; then
            aws rds restore-db-instance-to-point-in-time \
              --source-db-instance-identifier ${{ inputs.database_name }} \
              --target-db-instance-identifier ${{ inputs.database_name }}-restored \
              --restore-time "${{ inputs.restore_point }}"
          else
            SNAPSHOT=$(aws rds describe-db-snapshots \
              --db-instance-identifier ${{ inputs.database_name }} \
              --query "DBSnapshots[-1].DBSnapshotIdentifier" \
              --output text)
            aws rds restore-db-instance-from-db-snapshot \
              --db-instance-identifier ${{ inputs.database_name }}-restored \
              --db-snapshot-identifier $SNAPSHOT
          fi

      - name: Trocar DNS para DB restaurado
        run: |
          aws rds modify-db-instance \
            --db-instance-identifier ${{ inputs.database_name }} \
            --new-db-instance-identifier ${{ inputs.database_name }}-old
          aws rds modify-db-instance \
            --db-instance-identifier ${{ inputs.database_name }}-restored \
            --new-db-instance-identifier ${{ inputs.database_name }}

      - name: Subir aplicação
        run: |
          aws ecs update-service \
            --cluster production \
            --service app-service \
            --desired-count 3

      - name: Notificar
        run: |
          curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
            -H "Content-Type: application/json" \
            -d '{"text": "✅ Database ${{ inputs.database_name }} recuperada com sucesso"}'
```text

---

## 12. Pipeline as Code — Boas Práticas

### Modularização e Reuso

```yaml
# .github/actions/setup-node/action.yml
name: "Setup Node.js"
description: "Configura Node.js, pnpm e cache"
inputs:
  node-version:
    required: false
    default: "20.x"
  pnpm-version:
    required: false
    default: "9"

runs:
  using: "composite"
  steps:
    - uses: actions/checkout@v4
    - uses: pnpm/action-setup@v3
      with:
        version: ${{ inputs.pnpm-version }}
    - uses: actions/setup-node@v4
      with:
        node-version: ${{ inputs.node-version }}
        cache: pnpm
    - run: pnpm install --frozen-lockfile
      shell: bash
```text

Uso da action reutilizável:

```yaml
# .github/workflows/ci.yml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: ./.github/actions/setup-node
      - run: pnpm lint

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: ./.github/actions/setup-node
      - run: pnpm test
```text

### Reuso de Jobs com Matrix

```yaml
test-matrix:
  name: Testes (${{ matrix.node-version }})
  runs-on: ubuntu-latest
  strategy:
    matrix:
      node-version: [18.x, 20.x, 22.x]
    fail-fast: false
  steps:
    - uses: ./.github/actions/setup-node
      with:
        node-version: ${{ matrix.node-version }}
    - run: pnpm test:ci
```markdown

### Pipeline de Deploy com Environments e Gates

```yaml
```
deploy-production:
  name: Deploy em Produção
  needs: [lint, test, build, security-sast]
  runs-on: ubuntu-latest
  if: github.ref == 'refs/heads/main'
  environment:
    name: production
    url: https://meusistema.com.br
  concurrency:
    group: production-deploy
    cancel-in-progress: false
  steps:
    - uses: actions/checkout@v4
    - uses: ./.github/actions/setup-node
    - uses: actions/download-artifact@v4
      with:
        name: build-output
        path: dist

    - name: Login no Docker Registry
      uses: docker/login-action@v3
      with:
        username: ${{ secrets.DOCKER_USER }}
        password: ${{ secrets.DOCKER_PASS }}

    - name: Build e Push da Imagem
      run: |
        docker build -t meuregistro/app:${{ github.sha }} .
        docker push meuregistro/app:${{ github.sha }}

    - name: Deploy no ECS
      run: |
        aws ecs update-service \
          --cluster production \
          --service app-service \
          --force-new-deployment

    - name: Verificar Saúde
      run: |
        for i in {1..30}; do
          STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://meusistema.com.br/health)
          if [ "$STATUS" = "200" ]; then
            echo "✅ Deploy saudável"
            exit 0
          fi
          sleep 10
        done
        echo "❌ Health check falhou após deploy"
        exit 1

    - name: Rollback automático
      if: failure()
      run: |
        echo "🔄 Iniciando rollback..."
        aws ecs update-service \
          --cluster production \
          --service app-service \
          --force-new-deployment
