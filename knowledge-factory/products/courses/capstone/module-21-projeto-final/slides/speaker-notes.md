## Introducao

# Módulo 21 — Projeto Final: Enterprise SaaS de Gestão de Projetos e Tarefas
**O ápice da jornada. Construir um sistema completo, do zero, com tudo que um SaaS Enterprise exige.**
---

---
## 1. Visão Geral do Projeto

### 1.1 Objetivo
O Projeto Final é a culminação de toda a jornada de 20 módulos. O aluno deve construir, de forma individual ou em squad de até 3 pessoas, uma plataforma **SaaS de Gestão de Projetos e Tarefas** completa — similar a um Trello/Asana/ClickUp simplificado, porém com arquitetura Enterprise real.
O objetivo não é apenas "fazer funcionar". É demonstrar domínio sobre:
- Arquitetura limpa e modular (Módulo 08)
- Design System e UI/UX profissional (Módulos 04–07)
- Backend robusto com NestJS + Prisma (Módulo 10)
- Frontend com Next.js e componentes reutilizáveis (Módulo 11)
- Segurança, autenticação e RBAC (Módulo 12)

---
## 2. Escopo Completo

### 2.1 Autenticação Multi-tenant
- Cadastro de empresas (tenants) com plano gratuito e trial de 14 dias
- Cadastro de usuários com convite por e-mail (fluxo de onboarding)
- Login com e-mail/senha + OAuth2 (Google/GitHub)
- JWT com refresh token e rotação de tokens
- Recuperação de senha via e-mail transacional
- MFA (Autenticação de dois fatores) — opcional, mas pontua extra
- Session management com Redis

---
## 3. Requisitos Funcionais

### RF01 — Autenticação e Onboarding
| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF01.1 | Usuário deve se registrar com e-mail + senha | Alta |
| RF01.2 | Usuário pode registrar uma empresa (tenant) no ato do cadastro | Alta |
| RF01.3 | Owner pode convidar membros por e-mail | Alta |
| RF01.4 | Convidado recebe e-mail com link para aceitar convite | Alta |
| RF01.5 | Usuário pode fazer login com Google/GitHub OAuth | Média |

---
## 4. Requisitos Não-Funcionais

### RNF01 — Performance
| Requisito | Meta | Medição |
|-----------|------|---------|
| Latência p95 de API | < 200ms | Grafana + Prometheus |
| Tempo de carregamento de página | < 2s (FCP), < 3s (LCP) | Lighthouse CI |
| Throughput | 1000 req/s por instância | K6 |
| Tempo de query no banco | < 100ms p95 | Prisma logging + PG Stats |
| Tamanho de resposta JSON | < 500KB (com paginação) | Monitoramento |

---
## 5. Stack Tecnológica

### 5.1 Decisão de Stack
| Camada | Tecnologia | Justificativa |
|--------|-----------|---------------|
| Backend | NestJS + TypeScript | Framework Enterprise com DI, módulos, guards, interceptors |
| API | REST + GraphQL (opcional) | REST padrão; GraphQL para dashboards complexos |
| ORM | Prisma | Type-safe, migrations automáticas, ótima DX |
| Validação | Zod | Schemas compartilháveis, inferência de tipos |
| Autenticação | Passport + JWT + OAuth2 | Ecossistema maduro |

---
## 6. Arquitetura

### 6.1 Diagrama em ASCII
┌─────────────────────────────────────────────────────────────────────┐
│                        CLIENT (Browser)                             │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │               Next.js App (Vercel / ECS)                      │  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌───────────────┐   │  │
│  │  │Pages/RSC │ │  API     │ │WebSocket │ │  React Query  │   │  │
│  │  │(Server)  │ │  Routes  │ │(Socket.io)│ │  (Cache)      │   │  │

---
## 7. Módulos do Sistema

### 7.1 User & Tenant Module
**Responsabilidade:** Gerenciar usuários, empresas (tenants), convites, perfis.
src/modules/users/
├── user.module.ts
├── user.controller.ts
├── user.service.ts
├── user.repository.ts
├── dto/

---
## 8. Critérios de Avaliação

### 8.1 Checklist por Categoria
#### Código (40% da nota)
| Critério | Peso | Descrição |
|----------|------|-----------|
| Estrutura de pastas | 5 | Segue padrão modular, separação clara de responsabilidades |
| Código limpo | 5 | Nomes significativos, funções pequenas, sem duplicação |
| TypeScript estrito | 5 | strict mode, sem `any`, tipos bem definidos |
| Tratamento de erros | 5 | Exception filters, erros de domínio, respostas padronizadas |

---
## 9. Entregáveis

### 9.1 Repositório
- Um repositório GitHub (monorepo com `apps/backend`, `apps/frontend`, `packages/shared`)
- Ou dois repositórios separados (backend + frontend)
- Branch principal: `main` com proteção (PR obrigatório, CI obrigatório)
- Commits seguindo Conventional Commits
### 9.2 README
# Nome do Projeto

---
## Descrição

[Proposta de valor em 2-3 frases]

---
## Stack

- Backend: NestJS + Prisma + PostgreSQL + Redis
- Frontend: Next.js 14 + Tailwind + shadcn/ui
- Infra: Docker + AWS/Azure/GCP

---
## Funcionalidades

- [x] Autenticação multi-tenant
- [x] Gestão de projetos e tarefas
- [x] Kanban com drag & drop
- [x] Notificações em tempo real
- [x] Relatórios e dashboards
- [x] Pagamentos integrados

---
## Quick Start

git clone ...
cp .env.example .env
docker compose up

---
## Estrutura

[Diagrama de pastas]

---
## Documentação

- [Swagger](link)
- [ADRs](docs/adrs/)
- [Runbook](docs/runbook.md)

---
## Deploy

[Link para produção]
### 9.3 Documentação
- `docs/adrs/` — Decisões arquiteturais (mín. 4 ADRs)
- `docs/runbook.md` — Como operar o sistema em produção
- `docs/api.md` ou Swagger — Documentação da API
- `docs/architecture.md` — Diagrama e explicação da arquitetura
### 9.4 Testes
- Unitários: `apps/backend/src/**/*.spec.ts` (mín. 40)

---
## 10. Apresentação Final

### 10.1 Estrutura do Pitch (5 minutos)
| Minuto | Conteúdo |
|--------|----------|
| 0:00–0:30 | **Problema:** "Gerenciar projetos em equipe é caótico sem a ferramenta certa" |
| 0:30–1:00 | **Solução:** "Criamos uma plataforma SaaS multi-tenant que unifica gestão de projetos" |
| 1:00–2:00 | **Demo:** Mostrar login, criar projeto, adicionar tarefas, Kanban, notificações |
| 2:00–2:30 | **Diferenciais técnicos:** Multi-tenancy, RBAC, tempo real, observabilidade |
| 2:30–3:00 | **Arquitetura:** Modular Monolith, evento-driven, vertical scaling |

---
## 11. Checklist de Habilidades

Antes de entregar o projeto final, verifique se você domina:
### M01 — Mentalidade Enterprise
- [ ] Entendo a diferença entre produto e projeto
- [ ] Sei calcular ROI de uma funcionalidade
- [ ] Conheço os papéis de um time Engineering
### M02 — Product Discovery
- [ ] Sei conduzir entrevistas com stakeholders
- [ ] Sei priorizar backlog com valor de negócio

---
## 12. Próximos Passos — Como Continuar Evoluindo

### 12.1 Evoluções Técnicas
**Curto prazo (1-3 meses):**
- Substituir Event Emitter in-process por message broker (RabbitMQ / Kafka)
- Extrair Payments Module para microsserviço independente
- Adicionar GraphQL para consultas complexas do dashboard
- Implementar cache de página com ISR (Incremental Static Regeneration)
- Adicionar testes de carga com K6 (1000 usuários simultâneos)
**Médio prazo (3-6 meses):**

---
## Resumo

O Projeto Final é a oportunidade de demonstrar tudo que foi aprendido nos 20 módulos. Mais do que um sistema funcional, o que se avalia é a **qualidade das decisões técnicas**, a **organização do código**, a **cobertura de testes**, a **documentação clara**, e a **capacidade de apresentar e defender** as escolhas feitas.
Lembre-se: um sistema Enterprise de verdade não é aquele que funciona no seu computador. É aquele que continua funcionando sob carga, com múltiplos tenants, com falhas de rede, com dados inconsistentes — e que pode ser operado, monitorado e evoluído por um time.
Boa construção.

---
