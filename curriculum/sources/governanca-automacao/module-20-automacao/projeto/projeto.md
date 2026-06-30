# Projeto Final — Módulo 20: Automação

**Peso na nota final:** 40%  
**Duração estimada:** 16-20 horas  
**Formato:** Entrega em repositório GitHub (link), com pipeline funcional e documentação

---

## Cenário

Você é Tech Lead de um squad em uma fintech brasileira chamada **PagBrasil**. O produto é uma API de pagamentos que processa ~10 mil transações por dia. Atualmente:

- Deploys são feitos manualmente via SSH
- Não existem testes automatizados no CI
- O banco de dados (PostgreSQL) é migrado manualmente
- Não há ambientes de staging ou preview
- Releases são feitas manualmente sem versionamento semântico
- Segurança não é verificada antes do deploy
- Monitoramento reativo — time descobre incidentes por reclamação de cliente

**Sua missão:** Projetar e implementar um sistema completo de automação para o time.

---

## Entregáveis

### 1. Pipeline CI/CD (peso: 30%)

Crie um arquivo `.github/workflows/ci-cd.yml` completo com:

**CI (toda branch):**
- Lint (ESLint + Prettier)
- Testes unitários (Vitest)
- Testes de integração (com PostgreSQL)
- Build (TypeScript → dist/)
- SAST (SonarCloud + ESLint security)
- Dependency Scan (Snyk ou npm audit)
- Criação de preview environment (supondo deploy em container)

**CD (branch main + tags):**
- Build da imagem Docker com cache
- Push para ECR ou Docker Hub
- Deploy canary no ECS (CodeDeploy)
- Smoke tests pós-deploy
- Rollback automático em caso de falha
- Atualização de feature flag (configurar flag pós-deploy)

**Requisitos:**
- Usar GitHub Actions
- Cache de dependências e Docker layers
- Matrix strategy para Node.js 18, 20, 22
- Concurrency group para evitar deploys simultâneos
- Secrets: `DOCKER_USER`, `DOCKER_PASS`, `SNYK_TOKEN`, `SONAR_TOKEN`, `SLACK_WEBHOOK`
- Variáveis de ambiente: `NODE_VERSION=20`, `APP_NAME=pagbrasil-api`

### 2. Infraestrutura como Código (peso: 25%)

Crie um diretório `infra/` com IaC usando **Terraform** ou **Pulumi** (TypeScript).

**Recursos a criar:**
- VPC com subnets públicas e privadas
- ECS Cluster Fargate
- Task Definition com container da aplicação
- ALB (Application Load Balancer)
- Security Groups
- RDS PostgreSQL (instância small, multi-AZ)
- CodeDeploy Application + Deployment Group (blue/green)

**Requisitos:**
- Backend remoto (S3 ou Pulumi Cloud)
- Tags: `project: pagbrasil`, `managed-by: terraform` (ou pulumi)
- Outputs: `alb_dns`, `rds_endpoint`, `cluster_name`
- Uso de variáveis/modules para separar dev/prod
- Arquivo `variables.tf` (ou `Pulumi.yaml` separado por stack)

**Diferenciais (bônus de 5% na nota):**
- Módulo reutilizável para o serviço ECS
- Configuração de auto-scaling (mín. 2, máx. 10)
- Configuração de WAF no ALB

### 3. Script de Automação de Migrations (peso: 15%)

Crie um script (`scripts/migrate.ts` ou `scripts/migrate.sh`) que:

1. Faça backup automático do banco antes da migration
2. Execute as migrations (Prisma Migrate ou Sequelize)
3. Execute o seed apenas em ambientes não-prod
4. Em caso de falha, execute rollback automático
5. Envie notificação pro Slack com resultado

**Requisitos:**
- Usar variáveis de ambiente (`DATABASE_URL`, `NODE_ENV`, `SLACK_WEBHOOK`)
- Logs com timestamp e nível (INFO, WARN, ERROR)
- Código TypeScript com tipos
- Tratamento de erros com `try/catch` e `process.exit` adequado

### 4. Release Automatizada (peso: 15%)

Crie um workflow `.github/workflows/release.yml` que:

1. Execute quando um PR for mergeado na `main` ou via `workflow_dispatch`
2. Use `semantic-release` para:
   - Analisar commits (Conventional Commits)
   - Versionar (major/minor/patch)
   - Gerar changelog
   - Criar tag e release no GitHub
   - Publicar no npm (pode ser pacote privado)
3. Após a release, disparar o deploy em produção
4. Notificar o Slack com o resumo da release

**Configuração necessária:**
- `package.json` com `private: false`, `version: 0.0.0-development`
- `.releaserc.json` (ou `release.config.js`)
- Plugin `@semantic-release/changelog`
- Plugin `@semantic-release/git`
- Plugin `@semantic-release/npm`
- Plugin `@semantic-release/github`

### 5. Documentação (peso: 15%)

Crie um arquivo `README.md` na raiz do repositório contendo:

1. **Visão geral:** descrição do projeto e do sistema de automação
2. **Arquitetura:** diagrama da pipeline (texto ou ASCII) mostrando o fluxo completo
3. **Como contribuir:** padrão de branches, Conventional Commits, passo a passo
4. **Pipeline:** explicação de cada job (o que faz, quanto tempo leva, o que verificar)
5. **Deploy:** estratégia (canary), rollback, como verificar saúde
6. **Ambientes:** staging, production, preview ephemeral
7. **Monitoramento:** alertas configurados, runbooks, self-healing
8. **Segurança:** SAST, SCA, DAST — o que é verificado e como
9. **Troubleshooting:** problemas comuns em pipeline e como resolver
10. **Métricas:** tempo médio de pipeline, deploy frequency, MTTR, change failure rate

---

## Exemplo de Estrutura do Repositório

```
pagbrasil-api/
├── .github/
│   ├── workflows/
│   │   ├── ci-cd.yml
│   │   └── release.yml
│   ├── actions/
│   │   └── setup-node/action.yml
│   └── dependabot.yml
├── infra/
│   ├── main.tf           ou  Pulumi.yaml + index.ts
│   ├── variables.tf
│   ├── outputs.tf
│   ├── modules/
│   │   └── ecs-service/
│   │       ├── main.tf
│   │       ├── variables.tf
│   │       └── outputs.tf
│   └── environments/
│       ├── dev/
│       │   ├── terraform.tfvars  ou  Pulumi.dev.yaml
│       └── prod/
│           ├── terraform.tfvars  ou  Pulumi.prod.yaml
├── scripts/
│   ├── migrate.ts
│   ├── seed.ts
│   └── self-healing.ts
├── src/
│   └── ... (código da aplicação)
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── .releaserc.json
├── .eslintrc.json
├── .prettierrc
├── tsconfig.json
├── package.json
└── README.md
```

---

## Critérios de Avaliação

| Critério | Peso | Descrição |
|----------|------|-----------|
| Pipeline funcional | 25% | CI/CD completa, todos os jobs executam |
| Qualidade da IaC | 20% | Código modular, seguro, boas práticas |
| Scripts de automação | 15% | Migrations, self-healing funcionais |
| Release automatizada | 15% | Versionamento, changelog e publicação |
| Documentação | 15% | README completo e claro |
| Boas práticas | 10% | Cache, secrets, segurança, modularização |

**Bônus (até +10%):**
- Self-healing script que monitora e recupera serviços automaticamente
- Dashboard de pipeline com métricas (GitHub Actions metrics)
- Testes para o próprio pipeline (act para testar localmente)
- Feature flags funcionais integradas ao pipeline

---

## Sugestão de Plano de Trabalho

| Dia | Atividade | Horas |
|-----|-----------|-------|
| 1 | Setup do repositório, CI básico (lint + test + build) | 4 |
| 2 | Adicionar segurança, dependency scan, preview environment | 4 |
| 3 | IaC com Terraform/Pulumi (VPC, ECS, RDS, ALB) | 5 |
| 4 | Scripts de migration e self-healing | 3 |
| 5 | Release automatizada, README, revisão final | 4 |

---

## Entrega

1. Suba o repositório no GitHub (público ou privado com convite)
2. Certifique-se de que a pipeline está rodando (push na `main`)
3. Envie o link do repositório
4. Opcional: grave um vídeo de 5-10 minutos demonstrando a pipeline rodando e explicando a arquitetura (ganha até +5% na nota)

---

## Referências

- [GitHub Actions Docs](https://docs.github.com/actions)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Pulumi AWS](https://www.pulumi.com/docs/reference/pkg/aws/)
- [Semantic Release](https://semantic-release.gitbook.io/)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [ECS CodeDeploy Blue/Green](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps-ecs.html)
