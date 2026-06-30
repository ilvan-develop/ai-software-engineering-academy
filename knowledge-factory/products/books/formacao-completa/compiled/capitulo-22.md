
# Construindo um SaaS Enterprise

# Módulo 21 — Projeto Final: Enterprise SaaS de Gestão de Projetos e Tarefas

**O ápice da jornada. Construir um sistema completo, do zero, com tudo que um SaaS Enterprise exige.**

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
- Multi-tenancy real (Módulo 13)
- DevOps, CI/CD e containerização (Módulo 14)
- Qualidade e testes automatizados (Módulo 15)
- Observabilidade completa (Módulo 16)
- Integração com agentes de IA (Módulo 18)
- Auditoria e compliance (Módulo 19)
- Automação de processos (Módulo 20)

### 1.2 O que será construído

| Aspecto | Descrição |
|---------|-----------|
| Produto | Plataforma SaaS multi-tenant de gestão de projetos e tarefas |
| Público-alvo | Equipes de desenvolvimento, marketing, RH e operações |
| Diferencial | Arquitetura Enterprise, observabilidade, multi-tenancy real, IA integrada |
| Stack | NestJS + Next.js + PostgreSQL + Redis + Docker + Cloud |

### 1.3 Habilidades avaliadas

| Habilidade | Módulo relacionado |
|------------|-------------------|
| Mentalidade Enterprise | M01 |
| Product Discovery & Design Thinking | M02, M03 |
| UX, UI, Design System | M04, M05, M06, M07 |
| Arquitetura, Modelagem, SOLID | M08, M09 |
| Backend NestJS | M10 |
| Frontend Next.js | M11 |
| Segurança e Autenticação | M12 |
| Multi-tenancy | M13 |
| DevOps e Deploy | M14 |
| Testes e Qualidade | M15 |
| Observabilidade | M16 |
| Governança e Code Review | M17 |
| Agentes de IA | M18 |
| Auditoria e Compliance | M19 |
| Automação | M20 |

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

Fluxo de onboarding do tenant em diagrama de sequência:

![Onboarding de Tenant - Auth e Convite](/knowledge-factory/products/courses/capstone/module-21-projeto-final/assets/diagram-sequence-auth-onboarding.svg)

### 2.2 CRUD com Permissões Baseadas em Papéis (RBAC)

Hierarquia de papéis:
- **Owner** (dono do tenant) — acesso total, faturamento, configurações
- **Admin** — gerenciar projetos, membros, configurar workspace
- **Manager** — criar/editar projetos, alocar tarefas, gerar relatórios
- **Developer** — executar tarefas, comentar, anexar arquivos
- **Viewer** — acesso somente leitura a boards e relatórios

Permissões granulares por recurso (projeto, tarefa, relatório, configuração).

### 2.3 Gestão de Projetos e Tarefas

**Projetos:**
- CRUD completo (nome, descrição, datas, prioridade, status)
- Categorização por tags e departamentos
- Atribuição de equipe ao projeto
- Template de projeto (criar a partir de modelo)

**Tarefas:**
- CRUD completo com título, descrição, checklist, anexos
- Quadro Kanban (drag & drop entre colunas: To Do, In Progress, Review, Done)
- Sistema de comentários com menção a usuários
- Atividade em tempo real via WebSocket (alguém está editando)
- Histórico de alterações com auditoria
- Dependências entre tarefas (bloqueia/desbloqueia)
- Etiquetas personalizáveis com cores
- Estimativa de horas e time tracking

### 2.4 Notificações

- Notificações in-app (sininho no header)
- Notificações push (via WebSocket)
- Notificações por e-mail (tarefa atribuída, menção, vencimento)
- Preferências de notificação por usuário
- Template de e-mail transacional customizável

### 2.5 Relatórios e Dashboards

**Dashboard do workspace:**
- Gráfico de tarefas por status (pizza/barras)
- Burndown chart (sprint atual)
- Tarefas vencidas vs. concluídas no mês
- Produtividade por membro

**Relatórios exportáveis:**
- Relatório de projetos (PDF/CSV)
- Relatório de horas por membro
- Relatório de performance da equipe
- Histórico de conclusão por período

### 2.6 Integração com Pagamentos

- Planos: Free (até 3 projetos), Pro (ilimitado), Enterprise (custom)
- Gateway de pagamento: Stripe ou Paddle
- Webhooks para confirmação de pagamento, cancelamento, trial ending
- Portal de faturamento para o usuário (histórico, notas fiscais)
- Rate limiting por plano (API calls, storage, members)

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
| RF01.6 | Token JWT expira em 15 min, refresh token em 7 dias | Alta |
| RF01.7 | Usuário pode recuperar senha via e-mail | Média |
| RF01.8 | Admin pode desativar/ativar membros do tenant | Alta |
| RF01.9 | Sistema deve bloquear login após 5 tentativas falhas (rate limit) | Alta |

### RF02 — Gestão de Projetos

| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF02.1 | Usuário com permissão pode criar projeto | Alta |
| RF02.2 | Projeto tem: nome, descrição, dono, datas, prioridade, status | Alta |
| RF02.3 | Usuário pode editar e arquivar projeto | Alta |
| RF02.4 | Usuário pode filtrar projetos por status, prioridade, tags | Média |
| RF02.5 | Manager pode criar template a partir de projeto existente | Baixa |
| RF02.6 | Projeto arquivado não aparece nas listagens padrão | Alta |

### RF03 — Gestão de Tarefas

| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF03.1 | Usuário pode criar tarefa em um projeto | Alta |
| RF03.2 | Tarefa tem: título, descrição, responsável, data, prioridade, etiquetas | Alta |
| RF03.3 | Tarefa pode ter checklist com itens marcáveis | Média |
| RF03.4 | Tarefa pode ter comentários com menção (@usuário) | Alta |
| RF03.5 | Tarefa pode ser movida entre colunas Kanban (drag & drop) | Alta |
| RF03.6 | Histórico de alterações visível na tarefa | Alta |
| RF03.7 | Tarefa pode ter dependência de outra tarefa | Média |
| RF03.8 | Usuário pode anexar arquivos (imagens, PDFs) até 10MB | Média |
| RF03.9 | Sistema notifica quando tarefa é atribuída a alguém | Alta |
| RF03.10 | Tarefa pode ter time tracking (iniciar/pausar/parar) | Média |

### RF04 — Kanban Board

| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF04.1 | Board exibe colunas por status (To Do, In Progress, Review, Done) | Alta |
| RF04.2 | Usuário pode arrastar tarefa entre colunas | Alta |
| RF04.3 | Colunas podem ser personalizadas por projeto | Média |
| RF04.4 | Board atualiza em tempo real via WebSocket | Média |
| RF04.5 | Filtros por responsável, prioridade, etiqueta no board | Média |

### RF05 — Notificações

| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF05.1 | Notificação in-app ao ser mencionado em comentário | Alta |
| RF05.2 | Notificação in-app ao ser atribuído a tarefa | Alta |
| RF05.3 | Notificação por e-mail configurável | Média |
| RF05.4 | Central de notificações com marcador de lido/não lido | Alta |
| RF05.5 | Usuário pode configurar quais notificações receber | Média |

### RF06 — Relatórios

| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF06.1 | Dashboard com gráficos de tarefas por status | Alta |
| RF06.2 | Burndown chart por período | Média |
| RF06.3 | Relatório de horas por membro | Média |
| RF06.4 | Exportar relatório em PDF | Média |
| RF06.5 | Exportar relatório em CSV | Baixa |

### RF07 — Pagamentos e Planos

| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF07.1 | Usuário pode assinar plano Pro via Stripe | Alta |
| RF07.2 | Webhook Stripe processa eventos (payment_intent.succeeded, etc.) | Alta |
| RF07.3 | Limites do plano são aplicados (projetos, membros, storage) | Alta |
| RF07.4 | Usuário pode ver histórico de faturas | Média |
| RF07.5 | Trial de 14 dias com aviso de expiração | Média |
| RF07.6 | Downgrade/upgrade de plano com proration | Média |

### RF08 — Administração

| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF08.1 | Owner pode ver logs de atividade do tenant | Alta |
| RF08.2 | Owner pode gerenciar membros (convidar, remover, alterar papel) | Alta |
| RF08.3 | Owner pode configurar webhooks de saída (integração externa) | Baixa |
| RF08.4 | Owner pode baixar relatório de auditoria | Média |

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

### RNF02 — Segurança

| Requisito | Implementação |
|-----------|--------------|
| Autenticação | JWT + refresh token + OAuth2 |
| Autorização | RBAC com guard por endpoint |
| Rate limiting | 100 req/min por IP, 1000 req/min por usuário autenticado |
| CORS | Whitelist de origens configurável |
| Headers de segurança | Helmet.js (CSP, X-Frame-Options, HSTS) |
| Validação de entrada | Zod em toda API |
| Proteção contra XSS | Sanitização HTML em comentários |
| Proteção contra CSRF | CSRF token ou SameSite=Strict |
| Hash de senha | bcrypt (cost 12) |
| Secrets management | AWS Secrets Manager / Azure Key Vault |

### RNF03 — Escalabilidade

| Requisito | Estratégia |
|-----------|-----------|
| Horizontal scaling | Backend stateless com sessão em Redis |
| Database scaling | Read replicas + connection pooling (PgBouncer) |
| Cache | Redis para queries frequentes e sessões |
| Filas | Redis Bull para jobs assíncronos (e-mails, relatórios) |
| CDN | Assets estáticos no CloudFront / Cloudflare |
| Auto-scaling | Baseado em CPU/memória (HPA no Kubernetes) |

### RNF04 — Observabilidade

| Componente | Ferramenta | O que monitorar |
|------------|-----------|-----------------|
| Métricas | Prometheus + Grafana | CPU, memória, requests, latência, erros, throughput |
| Logs | OpenTelemetry + Loki | Logs estruturados (JSON), correlation ID |
| Tracing | OpenTelemetry + Jaeger | Trace de requisição completa (front → back → banco) |
| Uptime | Uptime Kuma / StatusCake | Health checks a cada 30s |
| Alertas | Grafana Alerting | Latência > 1s, erro > 1%, downtime |
| Dashboards | Grafana | Visão geral do sistema por tenant |

### RNF05 — Disponibilidade

| Requisito | Meta |
|-----------|------|
| Uptime SLA | 99.9% (8h downtime/ano) |
| RPO (Recovery Point Objective) | 5 minutos |
| RTO (Recovery Time Objective) | 30 minutos |
| Backup automático | Diário com retenção de 30 dias |
| Disaster Recovery | Multi-AZ na cloud |

### RNF06 — Manutenibilidade

| Requisito | Prática |
|-----------|---------|
| Cobertura de testes | > 80% unitários, > 60% integração |
| Documentação | README, API Reference (Swagger), ADRs, Runbook |
| Padrão de código | ESLint + Prettier + Husky + Commitlint |
| Versionamento | SemVer + Conventional Commits |
| CI/CD | GitHub Actions (lint → test → build → deploy) |

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
| Banco | PostgreSQL 16 | MVCC, JSONB, índices parciais, excelente para SaaS |
| Cache / Filas | Redis + Bull | Cache de queries, filas de job, sessões |
| Frontend | Next.js 14+ (App Router) | SSR, Server Components, Streaming, RSC |
| UI | Tailwind + shadcn/ui | Componentes acessíveis, customizáveis, design system |
| Estado | React Query + Zustand | Server state + client state |
| Testes | Vitest + Playwright + Supertest | Unitário, E2E, integração |
| Container | Docker + Docker Compose | Ambiente local idêntico ao produção |
| Orquestração | Kubernetes (ou Docker Swarm) | Para produção |
| Cloud | AWS (ECS/EKS, RDS, ElastiCache, S3) | Ou Azure/GCP — escolha do aluno |
| CI/CD | GitHub Actions | Pipeline completo |
| Observabilidade | OpenTelemetry + Grafana + Loki + Tempo | Stack open-source |

### 5.2 Por que essa stack?

```
Empresas usam:     NestJS + Next.js + PostgreSQL + Redis + Docker + AWS
Não usam:          PHP puro, jQuery, MySQL sem ORM, servidor único

A stack escolhida prepara o aluno para:
  → 85% das vagas de SaaS Enterprise no Brasil
  → Escalabilidade real (horizontal, stateless)
  → Ecossistema com alta empregabilidade
```

---

## 6. Arquitetura

### 6.1 Diagrama em ASCII

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
┌─────────────────────────────────────────────────────────────────────┐
│                    API GATEWAY (CloudFront / ALB)                    │
│         Rate Limiting │ Auth │ CORS │ Request Validation            │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    BACKEND — NestJS (ECS Fargate / EKS)             │
│                                                                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  │ Auth     │ │ Projects │ │ Tasks    │ │Notific.  │ │ Payments │ │
│  │ Module   │ │ Module   │ │ Module   │ │ Module   │ │ Module   │ │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘ │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────────┐  │
│  │ Reports  │ │ Admin    │ │ Webhooks │ │ Common: Guards,       │  │
│  │ Module   │ │ Module   │ │ Module   │ │ Pipes, Filters,       │  │
│  └──────────┘ └──────────┘ └──────────┘ │ Interceptors, DI      │  │
│                                          └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
         │           │               │               │
         ▼           ▼               ▼               ▼
┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────────────┐
│ PostgreSQL │ │   Redis    │ │     S3     │ │    Bull Queue      │
│ (RDS)      │ │(ElastiCache)│ │  (Arquivos)│ │  (Jobs assíncronos)│
│            │ │            │ │            │ │  ┌──────────────┐  │
│ - Dados    │ │ - Cache    │ │ - Anexos   │ │  │ Envio e-mail │  │
│ - Tenant   │ │ - Sessão   │ │ - Avatares │ │  │ Geração PDF  │  │
│ - Auditoria│ │ - Rate     │ │ - Exports  │ │  │ Limpeza      │  │
│            │ │  Limit     │ │            │ │  └──────────────┘  │
└────────────┘ └────────────┘ └────────────┘ └────────────────────┘

                         OBSERVABILIDADE
┌─────────────────────────────────────────────────────────────────────┐
│  Prometheus ← Métricas  │  Loki ← Logs  │  Tempo/Jaeger ← Traces  │
│  Grafana (Dashboard)    │  Alertmanager │  Uptime Kuma             │
└─────────────────────────────────────────────────────────────────────┘
```

### 6.2 Decisões Arquiteturais (ADRs)

#### ADR-001: Modular Monolith com estratégia de extração para microservices

**Contexto:** Precisamos decidir entre Modular Monolith e Microservices.

**Decisão:** Começar com Modular Monolith, com bounded contexts bem definidos.

**Justificativa:**
- Time pequeno (1–3 devs) — microservices trariam sobrecarga de comunicação e deploy
- Domínio bem conhecido (gestão de projetos) — não justifica complexidade inicial
- Bounded contexts bem definidos permitem extração futura para microservices sem reescrita

**Consequências:**
- Positivas: deploy único, comunicação in-process, debug simples, CI/CD simples
- Negativas: acoplamento indireto se módulos não forem disciplinados, escalonamento monolítico
- Mitigação: módulos estritamente isolados com interfaces públicas e events entre contextos

#### ADR-002: Multi-tenancy via discriminator column (tenant_id)

**Contexto:** Precisamos isolar dados de diferentes empresas.

**Decisão:** Usar coluna `tenant_id` em todas as tabelas (discriminator column) + RLS no PostgreSQL.

**Justificativa:**
- Menos complexo que schema por tenant (sem migrations N×)
- Mais isolado que database por tenant (sem conexões N×)
- RLS garante que nenhuma query vaze dados entre tenants
- Backup e restore mais simples (único banco)

**Consequências:**
- Positivas: backup único, migrations únicas, custo menor
- Negativas: contenção em tabelas grandes, necessidade de índices cuidadosos
- Mitigação: índices compostos (tenant_id + id), partition by tenant em tabelas grandes

#### ADR-003: Event-driven para comunicação entre módulos

**Contexto:** Módulos precisam se comunicar sem acoplamento direto (ex: ao criar tarefa, notificar usuário).

**Decisão:** Usar Event Emitter in-process (para o monólito) com interface que permita migrar para message broker.

**Justificativa:**
- Módulos não se importam com quem consome seus eventos
- Fácil adicionar novos consumers sem modificar producers
- Se um dia migrar para microservices, os eventos já estão definidos

**Consequências:**
- Positivas: baixo acoplamento, extensível, testável
- Negativas: complexidade adicional (eventos precisam ser versionados)
- Mitigação: eventos versionados (v1, v2), schemas de evento validados com Zod

#### ADR-004: Next.js App Router com Server Components

**Contexto:** Precisamos de SSR para SEO e performance, mas também de interatividade rica.

**Decisão:** Next.js 14+ App Router com Server Components por padrão, Client Components onde necessário.

**Justificativa:**
- Server Components diminuem JS enviado ao cliente
- Streaming melhora percepção de performance
- App Router oferece layout aninhado, loading states, error boundaries nativos

**Consequências:**
- Positivas: performance, SEO, DX moderna
- Negativas: curva de aprendizado (server vs client mental model)
- Mitigação: documentar decisão de componente server vs client no design system

### 6.3 Trade-offs Explicados

| Decisão | Trade-off |
|---------|-----------|
| Monólito vs Microservices | Simplicidade inicial vs escalabilidade futura |
| RLS vs Schema vs DB | Custo vs isolamento vs complexidade |
| Event-driven in-process | Baixa latência vs dependência de runtime |
| Server Components | Performance vs interatividade |
| Prisma vs TypeORM | Type-safe vs maturidade de recursos |
| Zod vs class-validator | Bundle menor vs ecossistema NestJS nativo |

---

## 7. Módulos do Sistema

### 7.1 User & Tenant Module

**Responsabilidade:** Gerenciar usuários, empresas (tenants), convites, perfis.

```text
src/modules/users/
├── user.module.ts
├── user.controller.ts
├── user.service.ts
├── user.repository.ts
├── dto/
│   ├── create-user.dto.ts
│   ├── update-user.dto.ts
│   └── invite-user.dto.ts
├── entities/
│   └── user.entity.ts
├── events/
│   ├── user-created.event.ts
│   └── user-invited.event.ts
└── specs/
    ├── user.service.spec.ts
    └── user.controller.spec.ts

src/modules/tenants/
├── tenant.module.ts
├── tenant.controller.ts
├── tenant.service.ts
├── tenant.repository.ts
├── dto/
│   ├── create-tenant.dto.ts
│   └── update-tenant.dto.ts
├── entities/
│   └── tenant.entity.ts
└── specs/
    └── tenant.service.spec.ts
```

### 7.2 Auth Module

**Responsabilidade:** Login, registro, OAuth, MFA, refresh token, session.

```text
src/modules/auth/
├── auth.module.ts
├── auth.controller.ts
├── auth.service.ts
├── strategies/
│   ├── jwt.strategy.ts
│   ├── jwt-refresh.strategy.ts
│   └── google.strategy.ts
├── guards/
│   ├── jwt-auth.guard.ts
│   ├── roles.guard.ts
│   └── tenant.guard.ts
├── dto/
│   ├── login.dto.ts
│   ├── register.dto.ts
│   ├── refresh.dto.ts
│   └── forgot-password.dto.ts
└── specs/
    └── auth.service.spec.ts
```

### 7.3 Projects Module

**Responsabilidade:** CRUD de projetos, membros do projeto, templates.

```text
src/modules/projects/
├── project.module.ts
├── project.controller.ts
├── project.service.ts
├── project.repository.ts
├── dto/
│   ├── create-project.dto.ts
│   ├── update-project.dto.ts
│   └── add-member.dto.ts
├── entities/
│   └── project.entity.ts
├── events/
│   ├── project-created.event.ts
│   └── member-added.event.ts
└── specs/
    └── project.service.spec.ts
```

### 7.4 Tasks Module

**Responsabilidade:** CRUD de tarefas, Kanban, comentários, checklists, time tracking, dependências.

```text
src/modules/tasks/
├── task.module.ts
├── task.controller.ts
├── task.service.ts
├── task.repository.ts
├── dto/
│   ├── create-task.dto.ts
│   ├── update-task.dto.ts
│   ├── move-task.dto.ts
│   └── add-comment.dto.ts
├── entities/
│   ├── task.entity.ts
│   └── task-history.entity.ts
├── gateway/
│   └── task.gateway.ts         (WebSocket)
├── events/
│   ├── task-created.event.ts
│   ├── task-assigned.event.ts
│   └── task-completed.event.ts
└── specs/
    ├── task.service.spec.ts
    └── task.gateway.spec.ts
```

### 7.5 Notifications Module

**Responsabilidade:** Notificações in-app, push, e-mail, preferências.

```text
src/modules/notifications/
├── notification.module.ts
├── notification.controller.ts
├── notification.service.ts
├── notification.repository.ts
├── dto/
│   └── update-preferences.dto.ts
├── entities/
│   └── notification.entity.ts
├── processors/
│   ├── email.processor.ts       (Bull)
│   └── push.processor.ts
├── templates/
│   ├── task-assigned.hbs
│   └── mention.hbs
└── specs/
    └── notification.service.spec.ts
```

### 7.6 Reports Module

**Responsabilidade:** Dashboard, gráficos, exportação PDF/CSV.

```text
src/modules/reports/
├── report.module.ts
├── report.controller.ts
├── report.service.ts
├── dto/
│   └── generate-report.dto.ts
├── generators/
│   ├── pdf.generator.ts
│   └── csv.generator.ts
└── specs/
    └── report.service.spec.ts
```

### 7.7 Payments Module

**Responsabilidade:** Planos, assinaturas, gateway Stripe, webhooks, faturas.

```text
src/modules/payments/
├── payment.module.ts
├── payment.controller.ts
├── payment.service.ts
├── entities/
│   ├── subscription.entity.ts
│   └── invoice.entity.ts
├── webhooks/
│   └── stripe.webhook.ts
├── dto/
│   └── create-checkout.dto.ts
└── specs/
    └── payment.service.spec.ts
```

### 7.8 Admin Module

**Responsabilidade:** Logs de atividade, auditoria, configurações do tenant, webhooks de saída.

```text
src/modules/admin/
├── admin.module.ts
├── admin.controller.ts
├── admin.service.ts
├── dto/
│   └── create-webhook.dto.ts
└── specs/
    └── admin.service.spec.ts
```

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
| Validação de entrada | 5 | Zod em toda API, mensagens de erro claras |
| Segurança | 5 | RBAC, rate limit, headers, validação, hash |
| Multi-tenancy | 5 | Isolamento verificado, sem vazamento de dados |
| Performance | 5 | Cache, paginação, índices, N+1 eliminado |

#### Testes (20% da nota)

| Critério | Peso |
|----------|------|
| Testes unitários (mín. 40 testes) | 5 |
| Testes de integração (mín. 10 testes) | 5 |
| Testes E2E (mín. 5 cenários) | 5 |
| Cobertura > 80% unitários, > 60% integração | 5 |

#### Documentação (15% da nota)

| Critério | Peso |
|----------|------|
| README completo (instalação, configuração, deploy) | 5 |
| ADRs documentando decisões arquiteturais | 3 |
| Swagger/OpenAPI da API | 3 |
| Runbook de operação (como monitorar, como debugar) | 2 |
| Instruções de setup local (docker-compose) | 2 |

#### Deploy e CI/CD (15% da nota)

| Critério | Peso |
|----------|------|
| Dockerfile e docker-compose | 3 |
| Pipeline CI/CD funcional (GitHub Actions) | 4 |
| Deploy em cloud funcional | 4 |
| Health checks e monitoramento ativo | 2 |
| Variáveis de ambiente externalizadas | 2 |

#### Apresentação (10% da nota)

| Critério | Peso |
|----------|------|
| Pitch de 5 min (problema, solução, diferenciais) | 3 |
| Demo ao vivo (funcionalidades principais) | 4 |
| Lições aprendidas e próximos passos | 2 |
| Respostas a perguntas técnicas | 1 |

### 8.2 Nota de Corte

- **Mínimo para aprovação:** 70% (nota geral)
- **Mínimo por categoria:** 50% em cada uma das 5 categorias
- **Reprovação automática:** código sem multi-tenancy, senha em texto puro, ou dados vazando entre tenants

---

## 9. Entregáveis

### 9.1 Repositório

- Um repositório GitHub (monorepo com `apps/backend`, `apps/frontend`, `packages/shared`)
- Ou dois repositórios separados (backend + frontend)
- Branch principal: `main` com proteção (PR obrigatório, CI obrigatório)
- Commits seguindo Conventional Commits

### 9.2 README

```markdown
# Nome do Projeto

## Descrição
[Proposta de valor em 2-3 frases]

## Stack
- Backend: NestJS + Prisma + PostgreSQL + Redis
- Frontend: Next.js 14 + Tailwind + shadcn/ui
- Infra: Docker + AWS/Azure/GCP

## Funcionalidades
- [x] Autenticação multi-tenant
- [x] Gestão de projetos e tarefas
- [x] Kanban com drag & drop
- [x] Notificações em tempo real
- [x] Relatórios e dashboards
- [x] Pagamentos integrados

## Quick Start
```bash
git clone ...
cp .env.example .env
docker compose up
```text

## Estrutura
[Diagrama de pastas]

## Documentação
- [Swagger](link)
- [ADRs](docs/adrs/)
- [Runbook](docs/runbook.md)

## Deploy
[Link para produção]
```

### 9.3 Documentação

- `docs/adrs/` — Decisões arquiteturais (mín. 4 ADRs)
- `docs/runbook.md` — Como operar o sistema em produção
- `docs/api.md` ou Swagger — Documentação da API
- `docs/architecture.md` — Diagrama e explicação da arquitetura

### 9.4 Testes

- Unitários: `apps/backend/src/**/*.spec.ts` (mín. 40)
- Integração: testes com banco real ou testcontainers (mín. 10)
- E2E: Playwright cobrindo fluxos críticos (mín. 5)
- Relatório de cobertura anexado ao README

### 9.5 CI/CD

Pipeline de GitHub Actions:
```
push / PR → main:
  1. Lint (ESLint + Prettier)
  2. Type check (tsc --noEmit)
  3. Testes unitários + integração
  4. Build (Docker image)
  5. Push para container registry
  6. Deploy para staging (automatizado)
  7. Smoke tests
  8. Deploy para produção (manual)
```

### 9.6 Dashboard de Monitoramento

- Grafana com métricas do backend (requests, latência, erros)
- Logs centralizados no Loki (ou CloudWatch)
- Tracing no Jaeger (ou X-Ray)
- Alerta configurado para latência > 1s

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
| 3:00–3:30 | **Testes:** Cobertura, estratégia, CI/CD |
| 3:30–4:00 | **Deploy:** Infraestrutura na cloud, monitoramento |
| 4:00–4:30 | **Lições aprendidas:** O que faria diferente, maiores desafios |
| 4:30–5:00 | **Próximos passos:** Features futuras, como contribuir |

### 10.2 Demo ao Vivo

Fluxo obrigatório de demonstração:
1. Acessar a aplicação e registrar um novo tenant
2. Convidar um membro (simular)
3. Criar um projeto com template
4. Criar tarefas e mover no Kanban
5. Atribuir tarefa e ver notificação
6. Comentar em uma tarefa com menção
7. Visualizar dashboard com gráficos
8. Mostrar monitoramento (Grafana)

### 10.3 Lições Aprendidas

O aluno deve refletir sobre:
- O que foi mais desafiador e por quê
- Qual decisão técnica mudaria se fosse começar de novo
- Como o aprendizado dos 20 módulos se aplicou na prática
- O que aprendeu além do conteúdo das aulas

### 10.4 Próximos Passos (Pós-Curso)

Sugestões de evolução contínua:
- Transformar o monólito em microservices (extrair Payments, Notifications)
- Adicionar inteligência artificial (sugestão de prioridade, estimativa automática)
- Criar integrações com Slack, Discord, Jira, GitHub
- Publicar como SaaS real (cobrar clientes de verdade)
- Abrir o core como open source

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

### M03 — Design Thinking
- [ ] Sei aplicar as 5 etapas do Design Thinking
- [ ] Crio protótipos de baixa fidelidade

### M04 — UX Research
- [ ] Sei fazer testes de usabilidade
- [ ] Crio personas e mapas de jornada

### M05 — Wireframes
- [ ] Crio wireframes de média fidelidade no Figma
- [ ] Documento fluxos de navegação

### M06 — UI Design
- [ ] Aplico princípios de gestalt, tipografia, cor, espaçamento
- [ ] Crio protótipos de alta fidelidade

### M07 — Design System
- [ ] Crio e documento componentes no Storybook
- [ ] Mantenho consistência visual com tokens

### M08 — Arquitetura
- [ ] Aplico SOLID, Clean Architecture, DDD
- [ ] Documento decisões com ADRs

### M09 — Modelagem de Dados
- [ ] Modelo bancos normalizados até 3FN
- [ ] Crio índices, constraints, relacionamentos

### M10 — Backend NestJS
- [ ] Construo módulos, controllers, services, repositories
- [ ] Implemento guards, interceptors, pipes, filters
- [ ] Escrevo testes unitários e de integração

### M11 — Frontend Next.js
- [ ] Desenvolvo com App Router, Server/Client Components
- [ ] Gerencia estado com React Query + Zustand

### M12 — Segurança
- [ ] Implemento JWT, OAuth, RBAC, rate limiting
- [ ] Sei mitigar OWASP Top 10

### M13 — Multi-tenancy
- [ ] Implemento isolamento de dados entre tenants
- [ ] Aplico RLS ou discriminator column

### M14 — DevOps
- [ ] Dockerizo aplicações
- [ ] Configuro CI/CD com GitHub Actions
- [ ] Faço deploy em cloud

### M15 — Testes e QA
- [ ] Escrevo testes unitários, integração, E2E
- [ ] Uso mocks, fixtures, testcontainers

### M16 — Observabilidade
- [ ] Implemento logging estruturado, métricas, tracing
- [ ] Crio dashboards no Grafana

### M17 — Governança
- [ ] Uso ADRs para documentar decisões arquiteturais
- [ ] Implemento code review com checklists e approval gates

### M18 — Agentes de IA
- [ ] Integro APIs de LLM (OpenAI, Anthropic)
- [ ] Crio agentes para automação de tarefas

### M19 — Auditoria
- [ ] Implemento trilha de auditoria
- [ ] Atendo requisitos de compliance (LGPD)

### M20 — Automação
- [ ] Automatizo processos com filas e jobs
- [ ] Crio e2e tests com Playwright

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
- Extrair Notifications para microsserviço com Serverless (Lambda)
- Adicionar IA: sugerir responsável baseado em carga de trabalho
- Criar integração bidirecional com Slack e Discord
- Implementar importação de projetos do Trello/Asana/Jira
- Adicionar busca full-text com Elasticsearch ou Meilisearch

**Longo prazo (6-12 meses):**
- Transformar em plataforma de marketplace de integrações
- Adicionar white-label (tenant pode personalizar domínio, logo, cores)
- Criar mobile app (React Native)
- Suporte offline-first com PWA e sincronização background

### 12.2 Contribuir para Open Source

O projeto pode evoluir para um open source real:
- Publicar em organização GitHub
- Adicionar CONTRIBUTING.md, CODE_OF_CONDUCT.md
- Criar issue templates (bug, feature, RFC)
- Configurar GitHub Discussions para comunidade
- Fazer release no GitHub com changelog automático

### 12.3 Portfólio

Para usar o projeto como portfólio:
- README com capturas de tela, GIFs, link para demo ao vivo
- Artigo no Medium/Dev.to explicando a arquitetura e decisões
- Vídeo de 10 min no YouTube mostrando o sistema funcionando
- LinkedIn: adicionar projeto na seção "Projetos" com descrição técnica
- GitHub: fixar o repositório no perfil, manter atividade constante

### 12.4 Monetização

- Publicar como SaaS real (cobrar R$ 29–R$ 99/mês por empresa)
- Oferecer versão self-hosted para empresas com compliance restrito
- Vender consultoria de implementação e customização
- Criar curso sobre "Como construir um SaaS Enterprise do zero"

---

## Resumo

O Projeto Final é a oportunidade de demonstrar tudo que foi aprendido nos 20 módulos. Mais do que um sistema funcional, o que se avalia é a **qualidade das decisões técnicas**, a **organização do código**, a **cobertura de testes**, a **documentação clara**, e a **capacidade de apresentar e defender** as escolhas feitas.

Lembre-se: um sistema Enterprise de verdade não é aquele que funciona no seu computador. É aquele que continua funcionando sob carga, com múltiplos tenants, com falhas de rede, com dados inconsistentes — e que pode ser operado, monitorado e evoluído por um time.

Boa construção.

