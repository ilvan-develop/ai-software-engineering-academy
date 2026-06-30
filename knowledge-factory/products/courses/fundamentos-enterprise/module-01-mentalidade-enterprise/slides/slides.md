---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 01 — Mentalidade Enterprise

## Módulo 01 - Mentalidade Enterprise

---
## 1. O que é software Enterprise?

- Software Enterprise é aquele construído para **organizações**, não para indivíduos.
- | Característica | Exemplo de problema se ignorada |
- |----------------|-------------------------------|
- | **Multi-usuário** | Dois usuários editam o mesmo registro e um perde as alterações |
- | **Multi-tenant** | Cliente A vê dados do Cliente B |

---
## 2. Escalabilidade

- Escalabilidade é a capacidade do sistema de **manter a performance** à medida que a demanda cresce.
- Escala Vertical (Scale Up):
- Aumentar recursos da máquina
- CPU: 4 cores → 16 cores
- RAM: 8GB → 64GB

---
## 3. Governança

- Governança é o conjunto de **regras e processos** que garantem consistência e qualidade no desenvolvimento.
- ┌──────────────────────────────────────────────┐
- │                 GOVERNANÇA                    │
- ├──────────────────────────────────────────────┤
- │  Código       │  Processo     │  Dados        │

---
## Regras de Governança

- TypeScript strict mode obrigatório
- Sem `any` — exceções revisadas em PR
- Lint e format automáticos (pre-commit hook)
- Toda feature começa com ADR se mudar arquitetura

---
## 4. Manutenibilidade

- Manutenibilidade é a facilidade de **entender, modificar e estender** o sistema.
- Código sem manutenibilidade:
- ┌────────────────────────────────────────────┐
- │  Feature nova         │  2 semanas         │
- │  Corrigir bug         │  3 dias            │

---
## 5. Observabilidade

- Observabilidade é a capacidade de **entender o estado interno do sistema** a partir de seus outputs externos.
- LOGS                            MÉTRICAS                    TRACING
- Eventos discretos               Dados agregados             Fluxo de requisições
- "Usuário X fez Y"              "500 requisições/segundo"   "Requisição passou por A→B→C"
- Exemplos:                       Exemplos:                   Exemplos:

---
## 6. Segurança

- Segurança em software Enterprise não é opcional — é **pré-requisito**.
- Não: "Vamos adicionar segurança depois"
- Sim: "Segurança é parte da definição de "pronto""
- Camada 1: Código

---
## 7. Compliance

- Compliance é a **conformidade com leis e regulamentações**.
- | Regulamentação | Região | Foco |
- |---------------|--------|------|
- | LGPD | Brasil | Dados pessoais |
- | GDPR | Europa | Dados pessoais |

---
## 8. Multi-tenant

- Multi-tenant é a capacidade de **atender múltiplos clientes** (tenants) com uma única instância do sistema.
- Database per Tenant:
- Prós: isolamento máximo, backup individual
- Contras: caro, complexo (migrations em N bancos)
- Quando: dados sensíveis (saúde, finanças)

---
## 9. Alta disponibilidade

- Alta disponibilidade (HA) é a capacidade do sistema de **permanecer acessível** mesmo com falhas.
- Disponibilidade     Downtime/ano       Exemplo
- 99% (1 nove)       3.65 dias           Sistemas internos
- 99.9% (2 noves)    8.76 horas          SaaS padrão
- 99.99% (3 noves)   52.56 minutos       Enterprise crítico

---
## Resumo

- 1. **Software Enterprise** é construído para organizações — multi-usuário, seguro, auditável
- 2. **Escalabilidade** — horizontal > vertical; banco não é broker
- 3. **Governança** — código + processo + dados com regras claras
- 4. **Manutenibilidade** — código limpo, testado, documentado, modular
- 5. **Observabilidade** — logs + métricas + tracing = entender o sistema
- 6. **Segurança** — em camadas, desde o código até a infra

---
## Exemplo: text

```text
Software de Consumo:                Software Enterprise:
- Um usuário                        - Centenas/milhares de usuários
- Dados isolados                    - Dados compartilhados com permissões
- "Funcionou no meu PC"             - Funciona em múltiplos ambientes
- Atualização quando quiser         - Atualização com rollback e migração
- Suporte via chat                  - SLA definido contratualmente
- Compliance: nenhum                - Compliance: LGPD, SOC2, ISO 27001
```

---
## Exemplo: text

```text
Escala Vertical (Scale Up):
  Aumentar recursos da máquina
  CPU: 4 cores → 16 cores
  RAM: 8GB → 64GB
  Limite: hardware máximo

Escala Horizontal (Scale Out):
  Adicionar mais máquinas
  1 servidor → 10 servidores
  Balanceador de carga na frente
  Limite: gerenciamento de estado
```

---
## Recap

- 1. O que é software Enterprise?
- 2. Escalabilidade
- 3. Governança
- Regras de Governança
- 4. Manutenibilidade
- 5. Observabilidade
- 6. Segurança
- 7. Compliance
- 8. Multi-tenant
- 9. Alta disponibilidade
- Resumo

---
# Obrigado!

## Perguntas?
