# Módulo 21 — Slides

---

## Slide 1: Título

**Projeto Final — SaaS de Gestão de Projetos**
Construir um sistema Enterprise completo, do zero

> "O que pode ser medido pode ser gerenciado."

---

## Slide 2: O que vamos construir?

Plataforma SaaS multi-tenant de gestão de projetos e tarefas

| Funcionalidade | Descrição |
|----------------|-----------|
| Autenticação | Multi-tenant + OAuth + JWT |
| Projetos | CRUD + templates + membros |
| Tarefas | Kanban + checklists + comentários + time tracking |
| Notificações | In-app, push, e-mail |
| Relatórios | Dashboards + PDF/CSV |
| Pagamentos | Stripe + planos + trial |

---

## Slide 3: Stack Tecnológica

```yaml
Frontend:     Next.js 14 + Tailwind + shadcn/ui + React Query
Backend:      NestJS + Prisma + Zod
Banco:        PostgreSQL 16 + Redis
Infra:        Docker + AWS (ECS/RDS/ElastiCache)
CI/CD:        GitHub Actions
Obs:          OpenTelemetry + Grafana + Loki + Tempo
```markdown

---

## Slide 4: Arquitetura — Visão Geral

```text
Cliente (Browser)
    │
    ▼
API Gateway (CloudFront / ALB)
    │
    ▼
NestJS Modular Monolith
┌───┬───┬───┬───┬───┬───┬───┬───┐
│AUTH│PRJ│TASK│NOTI│PAY│REP│ADM│WEB│
└───┴───┴───┴───┴───┴───┴───┴───┘
    │       │           │
    ▼       ▼           ▼
PostgreSQL  Redis       S3
(RDS)    (ElastiCache) (Arquivos)
```markdown

---

## Slide 5: Decisões Arquiteturais (ADRs)

| ADR | Decisão | Motivo |
|-----|---------|--------|
| ADR-001 | Modular Monolith | Time pequeno, deploy simples |
| ADR-002 | Discriminator column (tenant_id) | Custo vs isolamento |
| ADR-003 | Event-driven in-process | Baixo acoplamento |
| ADR-004 | Server Components | Performance |

> Toda decisão tem trade-off documentado

---

## Slide 6: Autenticação Multi-tenant

```text
Register → Cria Tenant + Owner
             ↓
Convite por e-mail → Aceita → Membro do Tenant
             ↓
Login → JWT (15min) + Refresh (7d)
             ↓
OAuth → Google / GitHub
```yaml

RBAC: Owner > Admin > Manager > Developer > Viewer

---

## Slide 7: Kanban Board em Tempo Real

```text
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│ To Do    │ │ In Prog  │ │ Review   │ │ Done     │
│          │ │          │ │          │ │          │
│ [Tarefa]│→│ [Tarefa]│→│ [Tarefa]│→│ [Tarefa] │
│ [Tarefa]│ │ [Tarefa]│ │          │ │ [Tarefa] │
│          │ │          │ │          │ │          │
└──────────┘ └──────────┘ └──────────┘ └──────────┘
```yaml

WebSocket: movimento reflete em todos os clients

---

## Slide 8: Notificações e Tempo Real

```text
Evento (task.assigned)
    │
    ▼
Event Emitter (in-process)
    │
    ├── Notificação in-app (WebSocket)
    ├── E-mail transacional (Bull Queue)
    └── Push notification (futuro)
```markdown

Usuário configura preferências por tipo

---

## Slide 9: Relatórios e Dashboards

```text
Dashboard (tempo real):
  - Tarefas por status (gráfico de pizza)
  - Burndown chart (sprint)
  - Produtividade por membro
  - Tarefas vencidas vs concluídas

Relatórios (exportáveis):
  - PDF: Relatório de projetos
  - CSV: Horas por membro
```markdown

Dados agregados por tenant (sem vazamento)

---

## Slide 10: Pagamentos com Stripe

```text
Free (3 projetos, 5 membros)
    → Upgrade
Pro (ilimitado, 50 membros)
    → Enterprise (custom)

Fluxo:
  Stripe Checkout → Webhook → Ativar subscription
  Trial 14 dias → E-mail de expiração
  Downgrade/Upgrade com proration
```markdown

Rate limits por plano (API, storage, members)

---

## Slide 11: DevOps e CI/CD

```yaml
Pipeline GitHub Actions:
  Push → Lint → Type Check → Test → Build → Deploy

Docker:
  - Dockerfile (multi-stage)
  - docker-compose (dev)
  - ECS Fargate (prod)

Monitoramento:
  - Health checks (/health, /ready)
  - Prometheus + Grafana
  - Loki (logs) + Tempo (traces)
```markdown

---

## Slide 12: Testes e Qualidade

| Tipo | Mínimo | Ferramenta |
|------|--------|-----------|
| Unitários | 40 | Vitest |
| Integração | 10 | Supertest + Testcontainers |
| E2E | 5 cenários | Playwright |
| Cobertura | 80% unit, 60% integ | c8/istanbul |

> Código sem teste é legado no dia 1

---

## Slide 13: Critérios de Avaliação

```text
Código        (40%) — estrutura, TS, segurança, multi-tenant
Testes        (20%) — unit, integração, E2E, cobertura
Documentação  (15%) — README, ADRs, Swagger, runbook
Deploy        (15%) — Docker, CI/CD, cloud, monitoramento
Apresentação  (10%) — pitch, demo, lições aprendidas

Corte: 70% geral, 50% por categoria
Reprovação automática: vazamento de dados entre tenants
```markdown

---

## Slide 14: Apresentação Final

```text
Pitch de 5 minutos:
  0:30 — Problema
  0:30 — Solução
  1:00 — Demo (ao vivo)
  0:30 — Diferenciais técnicos
  0:30 — Arquitetura
  0:30 — Testes e qualidade
  0:30 — Deploy e monitoramento
  0:30 — Lições aprendidas
  0:30 — Próximos passos
```markdown

Demo obrigatória: registro → projeto → tarefas → Kanban → notificações

---

## Slide 15: Para refletir

> "Não é sobre ter a stack mais nova. É sobre entregar valor com excelência técnica."

> "Um sistema Enterprise não é o que funciona no seu PC. É o que sobrevive em produção."

> "O portfólio não é o código. É a história que você conta sobre as decisões que tomou."
