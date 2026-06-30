# Módulo 20 - Automação

---

## 1. O que é Automação

Automação é a substituição de processos manuais repetitivos por scripts, pipelines e ferramentas que executam essas tarefas de forma confiável, auditável e escalável.
### Por que automatizar?
| Motivo | Impacto |
|--------|---------|

## 2. CI/CD — Pipelines de Integração e Deploy Contínuo

CI/CD é a espinha dorsal da automação em engenharia de software.
### Continuous Integration (CI)
Todo push para branches compartilhadas dispara:
1. Checkout do código

## 3. Automação de Testes

A pipeline de CI deve executar testes em camadas, respeitando a **pirâmide de testes**.
### Testes Unitários
Executados primeiro — são rápidos e isolados.
// Exemplo com vitest

## 4. Automação de Infraestrutura — IaC

Infrastructure as Code (IaC) é o gerenciamento de infraestrutura (servidores, bancos, redes) através de arquivos de configuração versionados.
### Terraform (HashiCorp)
# main.tf
terraform {

## 5. Automação de Deploys

### Blue-Green Deployment
Duas versões do ambiente (blue = atual, green = nova). O balanceador de carga muda o tráfego da blue para a green.
USUÁRIOS → Load Balancer → Blue (v1.0) ✅
→ Green (v1.1) 🟢 (após validação)

## 6. Automação de Banco de Dados

### Migrations Automáticas no CI
# Job de migration
migrate:
name: Rodar Migrations

---
*Este artigo faz parte da formacao Arquitetura de Software Enterprise com IA*