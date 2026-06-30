---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 13 — Multi-Tenant: Conceitos e Estratégias de Isolamento

## Módulo 13 - Multi-Tenant: Conceitos e Estratégias de Isolamento

---
## 1. O que é Multi-Tenancy?

- Multi-tenancy é um padrão arquitetural onde **uma única instância de software atende múltiplos clientes (tenants)**, ...
- ┌──────────────────────────────────────────────────────┐
- │                    SISTEMA (1 instância)               │
- │                                                        │
- │  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
- │  │ Tenant A │  │ Tenant B │  │ Tenant C │            │

---
## 2. Abordagens de Isolamento

- Existem três estratégias principais para isolar dados entre tenants.
- Cada tenant tem **seu próprio banco de dados**. O roteador de conexão decide qual banco usar com base no tenant ident...
- ┌──────────────────────────────────────────────┐
- │                Connection Router               │
- │                                                │

---
## 3. Análise Aprofundada por Dimensão

- Database per Tenant:** Um vazamento de dados de um tenant não afeta os outros. Se um cliente exige compliance específ...
- Schema per Tenant:** Um invasor que ganha acesso ao banco pode potencialmente acessar múltiplos schemas. A segurança ...
- Shared Database:** Um SQL injection ou bug no `WHERE` expõe **todos os dados de todos os tenants**. Requer:
- Testes de isolamento obrigatórios (ver seção 13)
- Code review com checklist específico

---
## Exemplo: text

```text
┌──────────────────────────────────────────────────────┐
│                    SISTEMA (1 instância)               │
│                                                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │ Tenant A │  │ Tenant B │  │ Tenant C │            │
│  │ (Acme)   │  │ (Zeta)   │  │ (Omega)  │            │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘            │
│       │              │              │                   │
│       └──────────────┴──────────────┘                   │
│                      │                                  │
│              ┌───────┴───────┐                          │
│              │  API + DB     │                          │
│              └───────────────┘                          │
└──────────────────────────────────────────────────────────┘
```

---
## Exemplo: text

```text
┌──────────────────────────────────────────────┐
│                Connection Router               │
│                                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ DB Acme  │  │ DB Zeta  │  │ DB Omega │    │
│  │ tenant_1 │  │ tenant_2 │  │ tenant_3 │    │
│  └──────────┘  └──────────┘  └──────────┘    │
└──────────────────────────────────────────────┘
```

---
## Recap

- 1. O que é Multi-Tenancy?
- 2. Abordagens de Isolamento
- 3. Análise Aprofundada por Dimensão

---
# Obrigado!

## Perguntas?
