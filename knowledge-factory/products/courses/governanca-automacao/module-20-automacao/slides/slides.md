---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 20 — Automação

## Módulo 20 - Automação

---
## 1. O que é Automação

- Automação é a substituição de processos manuais repetitivos por scripts, pipelines e ferramentas que executam essas t...
- | Motivo | Impacto |
- |--------|---------|
- | Reduzir erro humano | O maior causador de incidentes em produção ainda é o operador humano |
- | Velocidade | Máquinas executam em segundos o que levaria horas manualmente |

---
## 2. CI/CD — Pipelines de Integração e Deploy Contínuo

- CI/CD é a espinha dorsal da automação em engenharia de software.
- Todo push para branches compartilhadas dispara:
- 1. Checkout do código
- 2. Instalação de dependências
- 3. Linting

---
## 3. Automação de Testes

- A pipeline de CI deve executar testes em camadas, respeitando a **pirâmide de testes**.
- Executados primeiro — são rápidos e isolados.
- // Exemplo com vitest
- import { describe, it, expect } from 'vitest'
- import { calculateDiscount } from './pricing'

---
## 4. Automação de Infraestrutura — IaC

- Infrastructure as Code (IaC) é o gerenciamento de infraestrutura (servidores, bancos, redes) através de arquivos de c...
- terraform {
- required_providers {
- aws = {

---
## 5. Automação de Deploys

- Duas versões do ambiente (blue = atual, green = nova). O balanceador de carga muda o tráfego da blue para a green.
- USUÁRIOS → Load Balancer → Blue (v1.0) ✅
- → Green (v1.1) 🟢 (após validação)
- Switch: DNS/ALB aponta para Green
- Rollback: reverter DNS para Blue

---
## 6. Automação de Banco de Dados

- migrate:
- name: Rodar Migrations
- needs: build
- runs-on: ubuntu-latest

---
## 7. Automação de Segurança

- Análise estática de segurança diretamente no pipeline.
- security-sast:
- name: Análise Estática (SAST)
- runs-on: ubuntu-latest
- steps:

---
## 8. Automação de Code Review

- code-review:
- name: Revisão Automática
- runs-on: ubuntu-latest
- steps:
- uses: actions/checkout@v4

---
## 9. Automação de Releases

- release:
- name: Gerar Release
- needs: build
- runs-on: ubuntu-latest
- if: github.ref == 'refs/heads/main'

---
## [1.5.0](https://github.com/org/repo/compare/v1.4.0...v1.5.0) (2025-06-15)

- pagamento:** adiciona suporte a PIX ([abc1234](https://github.com/org/repo/commit/abc1234))
- relatorios:** nova rota de exportação CSV ([def5678](https://github.com/org/repo/commit/def5678))
- auth:** corrige timeout na renovação do token ([ghi9012](https://github.com/org/repo/commit/ghi9012))
- validacao:** CPF com formatação agora é aceito ([jkl3456](https://github.com/org/repo/commit/jkl3456))

---
## 10. Automação de Ambientes

- Ambientes temporários criados automaticamente para cada branch de feature.
- deploy-preview:
- name: Deploy Preview
- runs-on: ubuntu-latest
- if: github.event_name == 'pull_request'

---
## Exemplo: text

```text
Custo de automatizar = (tempo para criar + tempo para manter) × custo-hora
Benefício = (tempo economizado por execução × frequência × horizonte) - custo
```

---
## Exemplo: yaml

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
...
```

---
## Recap

- 1. O que é Automação
- 2. CI/CD — Pipelines de Integração e Deploy Contínuo
- 3. Automação de Testes
- 4. Automação de Infraestrutura — IaC
- 5. Automação de Deploys
- 6. Automação de Banco de Dados
- 7. Automação de Segurança
- 8. Automação de Code Review
- 9. Automação de Releases
- [1.5.0](https://github.com/org/repo/compare/v1.4.0...v1.5.0) (2025-06-15)
- 10. Automação de Ambientes

---
# Obrigado!

## Perguntas?
