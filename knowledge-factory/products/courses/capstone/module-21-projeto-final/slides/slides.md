---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 21 — Projeto Final: Enterprise SaaS de Gestão de Projetos e Tarefas

## Módulo 21 - Projeto Final: Enterprise SaaS de Gestão de Projetos e Tarefas

---
## 1. Visão Geral do Projeto

- O Projeto Final é a culminação de toda a jornada de 20 módulos. O aluno deve construir, de forma individual ou em squ...
- O objetivo não é apenas "fazer funcionar". É demonstrar domínio sobre:
- Arquitetura limpa e modular (Módulo 08)
- Design System e UI/UX profissional (Módulos 04–07)
- Backend robusto com NestJS + Prisma (Módulo 10)

---
## 2. Escopo Completo

- Cadastro de empresas (tenants) com plano gratuito e trial de 14 dias
- Cadastro de usuários com convite por e-mail (fluxo de onboarding)
- Login com e-mail/senha + OAuth2 (Google/GitHub)
- JWT com refresh token e rotação de tokens
- Recuperação de senha via e-mail transacional

---
## 3. Requisitos Funcionais

- | ID | Requisito | Prioridade |
- |----|-----------|------------|
- | RF01.1 | Usuário deve se registrar com e-mail + senha | Alta |
- | RF01.2 | Usuário pode registrar uma empresa (tenant) no ato do cadastro | Alta |
- | RF01.3 | Owner pode convidar membros por e-mail | Alta |

---
## 4. Requisitos Não-Funcionais

- | Requisito | Meta | Medição |
- |-----------|------|---------|
- | Latência p95 de API | < 200ms | Grafana + Prometheus |
- | Tempo de carregamento de página | < 2s (FCP), < 3s (LCP) | Lighthouse CI |
- | Throughput | 1000 req/s por instância | K6 |

---
## 5. Stack Tecnológica

- | Camada | Tecnologia | Justificativa |
- |--------|-----------|---------------|
- | Backend | NestJS + TypeScript | Framework Enterprise com DI, módulos, guards, interceptors |
- | API | REST + GraphQL (opcional) | REST padrão; GraphQL para dashboards complexos |
- | ORM | Prisma | Type-safe, migrations automáticas, ótima DX |

---
## 6. Arquitetura

- ┌─────────────────────────────────────────────────────────────────────┐
- │                        CLIENT (Browser)                             │
- │  ┌───────────────────────────────────────────────────────────────┐  │
- │  │               Next.js App (Vercel / ECS)                      │  │
- │  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌───────────────┐   │  │

---
## 7. Módulos do Sistema

- Responsabilidade:** Gerenciar usuários, empresas (tenants), convites, perfis.
- src/modules/users/
- ├── user.module.ts
- ├── user.controller.ts
- ├── user.service.ts

---
## 8. Critérios de Avaliação

- | Critério | Peso | Descrição |
- |----------|------|-----------|
- | Estrutura de pastas | 5 | Segue padrão modular, separação clara de responsabilidades |
- | Código limpo | 5 | Nomes significativos, funções pequenas, sem duplicação |

---
## 9. Entregáveis

- Um repositório GitHub (monorepo com `apps/backend`, `apps/frontend`, `packages/shared`)
- Ou dois repositórios separados (backend + frontend)
- Branch principal: `main` com proteção (PR obrigatório, CI obrigatório)
- Commits seguindo Conventional Commits

---
## Descrição

- [Proposta de valor em 2-3 frases]

---
## Stack

- Backend: NestJS + Prisma + PostgreSQL + Redis
- Frontend: Next.js 14 + Tailwind + shadcn/ui
- Infra: Docker + AWS/Azure/GCP

---
## Exemplo: text

```text
Empresas usam:     NestJS + Next.js + PostgreSQL + Redis + Docker + AWS
Não usam:          PHP puro, jQuery, MySQL sem ORM, servidor único

A stack escolhida prepara o aluno para:
  → 85% das vagas de SaaS Enterprise no Brasil
  → Escalabilidade real (horizontal, stateless)
  → Ecossistema com alta empregabilidade
```

---
## Exemplo: text

```text
┌─────────────────────────────────────────────────────────────────────┐
│                        CLIENT (Browser)                             │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │               Next.js App (Vercel / ECS)                      │  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌───────────────┐   │  │
│  │  │Pages/RSC │ │  API     │ │WebSocket │ │  React Query  │   │  │
│  │  │(Server)  │ │  Routes  │ │(Socket.io)│ │  (Cache)      │   │  │
│  │  └──────────┘ └──────────┘ └──────────┘ └───────────────┘   │  │
│  └───────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                              │ HTTP / WSS
                              ▼
...
```

---
## Recap

- 1. Visão Geral do Projeto
- 2. Escopo Completo
- 3. Requisitos Funcionais
- 4. Requisitos Não-Funcionais
- 5. Stack Tecnológica
- 6. Arquitetura
- 7. Módulos do Sistema
- 8. Critérios de Avaliação
- 9. Entregáveis
- Descrição
- Stack

---
# Obrigado!

## Perguntas?
