## Introducao

# Módulo 20 — Automação
**Duração estimada:** 5 dias (~40h)
**Público-alvo:** Desenvolvedores brasileiros em transição para cargos seniores/tech lead
**Pré-requisitos:** Conhecimento básico de Git, terminal Linux, conceitos de deploy
---

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

---
## 3. Automação de Testes

A pipeline de CI deve executar testes em camadas, respeitando a **pirâmide de testes**.
### Testes Unitários
Executados primeiro — são rápidos e isolados.
// Exemplo com vitest
import { describe, it, expect } from 'vitest'
import { calculateDiscount } from './pricing'
describe('calculateDiscount', () => {
it('aplica 10% para compras acima de R$ 100', () => {

---
## 4. Automação de Infraestrutura — IaC

Infrastructure as Code (IaC) é o gerenciamento de infraestrutura (servidores, bancos, redes) através de arquivos de configuração versionados.
### Terraform (HashiCorp)
# main.tf
terraform {
required_providers {
aws = {
source  = "hashicorp/aws"
version = "~> 5.0"

---
## 5. Automação de Deploys

### Blue-Green Deployment
Duas versões do ambiente (blue = atual, green = nova). O balanceador de carga muda o tráfego da blue para a green.
USUÁRIOS → Load Balancer → Blue (v1.0) ✅
→ Green (v1.1) 🟢 (após validação)
Switch: DNS/ALB aponta para Green
Rollback: reverter DNS para Blue
### Canary Deployment
Uma porcentagem pequena do tráfego vai para a nova versão. Aos poucos, aumenta-se até 100%.

---
## 6. Automação de Banco de Dados

### Migrations Automáticas no CI
# Job de migration
migrate:
name: Rodar Migrations
needs: build
runs-on: ubuntu-latest
environment: ${{ github.ref == 'refs/heads/main' && 'production' || 'staging' }}
steps:

---
## 7. Automação de Segurança

### SAST (Static Application Security Testing)
Análise estática de segurança diretamente no pipeline.
security-sast:
name: Análise Estática (SAST)
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4
- uses: pnpm/action-setup@v3

---
## 8. Automação de Code Review

### Bots no Pipeline
code-review:
name: Revisão Automática
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4
with:
fetch-depth: 0

---
## 9. Automação de Releases

### Semantic Versioning Automático
release:
name: Gerar Release
needs: build
runs-on: ubuntu-latest
if: github.ref == 'refs/heads/main'
permissions:
contents: write

---
## [1.5.0](https://github.com/org/repo/compare/v1.4.0...v1.5.0) (2025-06-15)

### Features
* **pagamento:** adiciona suporte a PIX ([abc1234](https://github.com/org/repo/commit/abc1234))
* **relatorios:** nova rota de exportação CSV ([def5678](https://github.com/org/repo/commit/def5678))
### Bug Fixes
* **auth:** corrige timeout na renovação do token ([ghi9012](https://github.com/org/repo/commit/ghi9012))
* **validacao:** CPF com formatação agora é aceito ([jkl3456](https://github.com/org/repo/commit/jkl3456))
---

---
## 10. Automação de Ambientes

### Ephemeral Environments
Ambientes temporários criados automaticamente para cada branch de feature.
deploy-preview:
name: Deploy Preview
runs-on: ubuntu-latest
if: github.event_name == 'pull_request'
environment:
name: preview-${{ github.event.number }}

---
## 11. Automação de Monitoramento

### Alertas Automáticos
monitoring-setup:
name: Configurar Alertas
runs-on: ubuntu-latest
steps:
- name: Configurar Datadog Monitors
uses: datadog/synthetics-ci-github-action@v1
with:

---
## 12. Pipeline as Code — Boas Práticas

### Modularização e Reuso
# .github/actions/setup-node/action.yml
name: "Setup Node.js"
description: "Configura Node.js, pnpm e cache"
inputs:
node-version:
required: false
default: "20.x"

---
