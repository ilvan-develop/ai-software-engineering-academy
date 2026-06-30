## Introducao

# Módulo 01 — Mentalidade Enterprise
**Como empresas de verdade desenvolvem software.**
---

---
## 1. O que é software Enterprise?

Software Enterprise é aquele construído para **organizações**, não para indivíduos.
### Características
| Característica | Exemplo de problema se ignorada |
|----------------|-------------------------------|
| **Multi-usuário** | Dois usuários editam o mesmo registro e um perde as alterações |
| **Multi-tenant** | Cliente A vê dados do Cliente B |
| **Segurança** | Dado sensível exposto por falta de autorização |
| **Auditabilidade** | Não é possível rastrear quem fez o quê |

---
## 2. Escalabilidade

Escalabilidade é a capacidade do sistema de **manter a performance** à medida que a demanda cresce.
### Tipos de escala
Escala Vertical (Scale Up):
Aumentar recursos da máquina
CPU: 4 cores → 16 cores
RAM: 8GB → 64GB
Limite: hardware máximo
Escala Horizontal (Scale Out):

---
## 3. Governança

Governança é o conjunto de **regras e processos** que garantem consistência e qualidade no desenvolvimento.
### Pilares da governança
┌──────────────────────────────────────────────┐
│                 GOVERNANÇA                    │
├──────────────────────────────────────────────┤
│  Código       │  Processo     │  Dados        │
│───────────────┼───────────────┼──────────────│
│ TypeScript    │ Git Flow      │ Migrações     │

---
## Regras de Governança

### Código
- TypeScript strict mode obrigatório
- Sem `any` — exceções revisadas em PR
- Lint e format automáticos (pre-commit hook)
### Processo
- Toda feature começa com ADR se mudar arquitetura
- PR aprovado por 1 reviewer + CI verde
- Commits semânticos: feat, fix, refactor, docs, test

---
## 4. Manutenibilidade

Manutenibilidade é a facilidade de **entender, modificar e estender** o sistema.
### O custo da falta de manutenibilidade
Código sem manutenibilidade:
┌────────────────────────────────────────────┐
│  Feature nova         │  2 semanas         │
│  Corrigir bug         │  3 dias            │
│  Onboarding dev novo   │  2 meses           │
│  Refatorar módulo     │  "melhor reescrever"│

---
## 5. Observabilidade

Observabilidade é a capacidade de **entender o estado interno do sistema** a partir de seus outputs externos.
### Os 3 pilares
LOGS                            MÉTRICAS                    TRACING
Eventos discretos               Dados agregados             Fluxo de requisições
"Usuário X fez Y"              "500 requisições/segundo"   "Requisição passou por A→B→C"
Exemplos:                       Exemplos:                   Exemplos:
- log.error("Falha no pgto")    - response_time_p95         - span do endpoint
- log.info("Usuário logou")     - error_rate                - span do banco

---
## 6. Segurança

Segurança em software Enterprise não é opcional — é **pré-requisito**.
### Mindset de segurança
Não: "Vamos adicionar segurança depois"
Sim: "Segurança é parte da definição de "pronto""
### Camadas de segurança
Camada 1: Código
→ Input validation, ORM (previne injection), prepared statements
Camada 2: Autenticação

---
## 7. Compliance

Compliance é a **conformidade com leis e regulamentações**.
### Principais regulamentações
| Regulamentação | Região | Foco |
|---------------|--------|------|
| LGPD | Brasil | Dados pessoais |
| GDPR | Europa | Dados pessoais |
| PCI DSS | Global | Dados de cartão |
| HIPAA | EUA | Dados de saúde |

---
## 8. Multi-tenant

Multi-tenant é a capacidade de **atender múltiplos clientes** (tenants) com uma única instância do sistema.
### Estratégias de isolamento
Database per Tenant:
Prós: isolamento máximo, backup individual
Contras: caro, complexo (migrations em N bancos)
Quando: dados sensíveis (saúde, finanças)
Custo: $$$$$
Schema per Tenant:

---
## 9. Alta disponibilidade

Alta disponibilidade (HA) é a capacidade do sistema de **permanecer acessível** mesmo com falhas.
### Métricas de disponibilidade
Disponibilidade     Downtime/ano       Exemplo
99% (1 nove)       3.65 dias           Sistemas internos
99.9% (2 noves)    8.76 horas          SaaS padrão
99.99% (3 noves)   52.56 minutos       Enterprise crítico
99.999% (4 noves)  5.26 minutos        Missão crítica
### Estratégias de HA

---
## Resumo

1. **Software Enterprise** é construído para organizações — multi-usuário, seguro, auditável
2. **Escalabilidade** — horizontal > vertical; banco não é broker
3. **Governança** — código + processo + dados com regras claras
4. **Manutenibilidade** — código limpo, testado, documentado, modular
5. **Observabilidade** — logs + métricas + tracing = entender o sistema
6. **Segurança** — em camadas, desde o código até a infra
7. **Compliance** — LGPD/GDPR não são opcionais
8. **Multi-tenant** — escolha a estratégia de isolamento certa

---
