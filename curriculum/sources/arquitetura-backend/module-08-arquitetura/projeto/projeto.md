# Projeto Módulo 08 — Arquitetura de um Sistema Enterprise

## Objetivo

Projetar a arquitetura completa de um sistema Enterprise, documentando decisões arquiteturais com ADRs.

## Contexto

Você é o Enterprise Architect de uma startup que vai construir um **SaaS de Gestão Financeira Enterprise**.

Requisitos:
- Controle de contas a pagar e receber
- Conciliação bancária automática
- Geração de relatórios financeiros (DRE, Fluxo de Caixa)
- Múltiplas empresas por usuário (multi-tenant)
- Integração com APIs bancárias
- Até 10.000 transações/dia por tenant
- Equipe: 8 devs (3 backend, 3 frontend, 1 QA, 1 DevOps)

## Entregáveis

### 1. Decisão Arquitetural

Escolha entre Modular Monolith e Microservices. Justifique com ADR.

### 2. Diagrama de Camadas

Desenhe (em ASCII/descrição) a arquitetura em camadas seguindo Clean Architecture:
- Entities
- Use Cases
- Adapters
- Frameworks

### 3. Bounded Contexts

Identifique os Bounded Contexts do sistema e suas responsabilidades.

### 4. Estrutura de Pastas

Proponha a estrutura de pastas do projeto backend (NestJS) seguindo Clean Architecture + DDD.

### 5. ADRs

Crie 3 ADRs documentando decisões arquiteturais:

1. **Escolha da arquitetura** (Clean Arch vs. outra)
2. **Estratégia multi-tenant** (RLS vs. schema vs. database)
3. **Comunicação entre contextos** (event-driven vs. direct call)

### 6. Anti-padrões

Identifique 3 anti-padrões comuns que este sistema deve evitar e como preveni-los.

## Formato

```markdown
# Proposta de Arquitetura: Gestão Financeira Enterprise

## Decisão: Modular Monolith
[ADR completo]

## Diagrama de Camadas
...

## Bounded Contexts
| Contexto | Responsabilidade |
|----------|-----------------|
| ...      | ...             |

## Estrutura de Pastas
```text
src/
├── domain/
...
```markdown

## ADRs
### ADR-001: ...
...
```text
