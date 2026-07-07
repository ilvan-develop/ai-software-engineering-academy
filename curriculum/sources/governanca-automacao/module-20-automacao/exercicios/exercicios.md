# Exercícios — Módulo 20: Automação

**Objetivo:** Praticar a criação de pipelines, scripts de automação e infraestrutura como código.

---

## Exercício 1 — Pipeline CI de um Projeto Node.js

**Contexto:** Você é tech lead de um squad que mantém uma API REST em Node.js com Express e Prisma. O time cresceu e os deploys manuais estão causando incidentes.

**Tarefa:** Crie um arquivo `.github/workflows/ci.yml` completo com os seguintes jobs:

1. **lint:** ESLint + Prettier check
2. **test-unit:** Testes unitários com Vitest
3. **test-int:** Testes de integração com banco PostgreSQL via service container
4. **build:** Compilação TypeScript e upload do artefato `dist/`
5. **security:** Scan com SonarCloud e `pnpm audit`

**Requisitos:**
- Usar Node.js 20.x
- Usar pnpm com frozen-lockfile
- Cache de dependências
- Jobs devem rodar em paralelo quando possível
- `test-int` deve esperar `lint` e `test-unit` terminarem
- `build` deve esperar `test-int`
- `security` deve rodar em paralelo com `build`

**Dica:** Use a estrutura de `needs` e `services` do GitHub Actions.

---

## Exercício 2 — Script de Self-Healing

**Contexto:** Sua aplicação roda em ECS Fargate com 3 tarefas. Eventualmente, tasks travam (stuck) e precisam ser substituídas.

**Tarefa:** Escreva um script em TypeScript (Node.js) que:

1. Liste os serviços de um cluster ECS
2. Para cada serviço, verifique se o número de tasks running é igual ao desired
3. Se for diferente, force um novo deploy (`forceNewDeployment: true`)
4. Se houver tasks stopped, descreva-as e logue o motivo (exit code, reason)
5. Envie uma notificação para um webhook do Slack com o resumo

**Requisitos:**
- Usar AWS SDK v3 (`@aws-sdk/client-ecs`)
- Usar variáveis de ambiente para cluster, região e webhook
- Tratar erros com try/catch
- Logs estruturados com `console.log` incluindo timestamp

**Exemplo de saída esperada:**

```json
[2025-06-15T10:30:00Z] 🔍 Verificando cluster: production
[2025-06-15T10:30:01Z] ✅ app-service: 3/3 tasks running
[2025-06-15T10:30:02Z] 🔧 worker-service: 1/2 tasks running — forçando deploy...
[2025-06-15T10:30:03Z] ✅ worker-service: deploy forçado enviado
[2025-06-15T10:30:04Z] ⚠️ worker-service: task stopped — exit code 137 (OOMKilled)
[2025-06-15T10:30:05Z] 📤 Notificação enviada ao Slack
```markdown

---

## Exercício 3 — IaC com Pulumi: Ambiente Efêmero

**Contexto:** Sua empresa quer adotar ephemeral environments. Cada branch de feature deve ganhar um ambiente próprio com ECS Fargate + RDS PostgreSQL.

**Tarefa:** Escreva um programa Pulumi em TypeScript que:

1. Crie um cluster ECS
2. Crie uma task definition com um container da aplicação (porta 3000)
3. Crie um security group que permite tráfego HTTP na porta 3000
4. Crie um load balancer (ALB) apontando para o serviço
5. Exporte a URL do load balancer como stack output
6. Use tags para identificar o ambiente (`environment: ephemeral`, `branch: ${branch}`)

**Requisitos:**
- Usar `@pulumi/aws`
- Usar `pulumi.Config` para parâmetros (subnets, VPC, imagem da app)
- Aceitar uma config `branch` para nomear recursos (ex: `app-service-branch-name`)
- O container deve ter variáveis de ambiente `DATABASE_URL` e `NODE_ENV`

**Estrutura esperada:**

```typescript
import * as aws from '@pulumi/aws'
import * as pulumi from '@pulumi/pulumi'

const config = new pulumi.Config()
const branch = config.require('branch')
const stack = pulumi.getStack()

// ... seu código aqui

export const url = loadBalancer.dnsName
```markdown

---

## Exercício 4 — Pipeline de Deploy Canary com Feature Flag

**Contexto:** Você precisa implementar um pipeline de CD que faça deploy canary com feature flags. A funcionalidade nova (checkout v2) deve ser liberada gradualmente.

**Tarefa:** Crie um workflow GitHub Actions que:

1. Faça build da imagem Docker
2. Faça push para o ECR
3. Faça deploy canary no ECS (10% de tráfego)
4. Execute testes de smoke na versão canary (chamar `GET /health` da nova versão)
5. Se os smokes passarem, aumente para 50% por 5 minutos
6. Se tudo ok, vá para 100%
7. Em qualquer falha, faça rollback automático para a versão anterior
8. Atualize a feature flag `checkout-v2-enabled` no Configu/LaunchDarkly para false

**Requisitos:**
- Usar `deploy` strategy com CodeDeploy (blue/green ou canary)
- Usar `environment` do GitHub Actions com protection rules
- Adicionar concurrency group para evitar deploys simultâneos
- Notificar o Slack em caso de sucesso ou falha

**Dica:** Pesquise sobre `aws deploy create-deployment` e `CodeDeploy` como deployment controller no ECS.

---

## Exercício 5 — Pipeline de Release Automatizada com Semantic Release

**Contexto:** Seu repositório segue Conventional Commits e você quer automatizar todo o processo de release.

**Tarefa:** Crie um workflow de release que:

1. Execute apenas quando um PR for mergeado na `main`
2. Use `cycjimmy/semantic-release-action` com os plugins:
   - `@semantic-release/changelog`
   - `@semantic-release/git`
   - `@semantic-release/npm`
   - `@semantic-release/github`
3. Publique o pacote no npm (escopo `@my-company`)
4. Crie uma release no GitHub com o changelog
5. Faça deploy automático em produção após a release
6. Adicione um passo manual de aprovação antes do deploy em produção
7. Notifique o time no Slack com a versão publicada e link da release

**Requisitos:**
- Configurar `package.json` com `private: false` e `publishConfig`
- Usar `NPM_TOKEN` e `GITHUB_TOKEN` como secrets
- O deploy em produção deve usar o ambiente `production` com `environment` do GitHub Actions
- Adicionar um step de validação: verificar se a branch está atualizada com `main` antes de publicar

---

## Critérios de Avaliação

| Critério | Peso | Descrição |
|----------|------|-----------|
| Funcionalidade | 40% | O código/script executa o que foi pedido |
| Boas práticas | 25% | Segurança, modularização, tratamento de erros |
| Clareza | 20% | Código legível, nomes descritivos, estrutura organizada |
| Documentação | 15% | Comentários relevantes, README ou explainer do exercício |
