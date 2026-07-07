# Projeto Final — Enterprise SaaS de Gestão de Projetos e Tarefas

## Objetivo

Construir uma plataforma SaaS multi-tenant completa de gestão de projetos e tarefas, similar a um Trello/Asana/ClickUp, porém com arquitetura Enterprise real, deploy em cloud, observabilidade, CI/CD e testes automatizados.

Este projeto avalia a integração de **todos os 20 módulos anteriores** do curso.

---

## Contexto

### Persona

Você é o CTO de uma startup que acabou de receber um seed funding de R$ 2 milhões. O investidor quer ver um MVP funcional em 8 semanas. Você tem liberdade técnica total e um time de 3 pessoas (incluindo você).

### Problema

"Pequenas e médias equipes de tecnologia gastam tempo demais alternando entre ferramentas desconectadas — Jira para issues, Trello para kanban, Google Sheets para horas, Slack para comunicação. Não há uma visão unificada do projeto e do time."

### Solução

Uma plataforma SaaS que unifica:
- Gestão de projetos (criação, priorização, categorização)
- Quadro Kanban com tempo real
- Atribuição e acompanhamento de tarefas
- Comunicação via comentários e menções
- Relatórios e dashboards de produtividade
- Notificações inteligentes (in-app, e-mail)

---

## Especificação Técnica

### 1. Backend (NestJS + Prisma + PostgreSQL + Redis)

#### 1.1 Módulo de Autenticação e Tenants

**Entidades:**
- `Tenant` (id, name, slug, plan, status, settings, createdAt, updatedAt)
- `User` (id, tenantId, name, email, password, role, avatar, isActive, createdAt, updatedAt)
- `Invite` (id, tenantId, email, role, token, expiresAt, status, createdAt)

**Endpoints:**
```text
POST   /api/auth/register          — Registrar tenant + owner
POST   /api/auth/login             — Login
POST   /api/auth/refresh           — Refresh token
POST   /api/auth/logout            — Logout
POST   /api/auth/forgot-password   — Solicitar recuperação
POST   /api/auth/reset-password    — Resetar senha
GET    /api/auth/me                — Perfil do usuário logado

POST   /api/tenants/:id/invite     — Convidar membro
POST   /api/tenants/accept-invite  — Aceitar convite
GET    /api/tenants/:id/members    — Listar membros
PATCH  /api/tenants/:id/members/:userId/role — Alterar papel
DELETE /api/tenants/:id/members/:userId       — Remover membro
```text

**Regras:**
- `tenant_id` presente em todas as tabelas do sistema
- RLS (Row Level Security) no PostgreSQL para garantir isolamento
- JWT com claims: `{ sub, tenantId, role, permissions }`

#### 1.2 Módulo de Projetos

**Entidades:**
- `Project` (id, tenantId, name, description, ownerId, status, priority, startDate, endDate, tags, archived, createdAt, updatedAt)
- `ProjectMember` (id, projectId, userId, role, joinedAt)
- `ProjectTemplate` (id, tenantId, name, description, columns, createdAt)

**Endpoints:**
```sql
GET    /api/projects               — Listar projetos (filtros: status, priority, tags)
POST   /api/projects               — Criar projeto
GET    /api/projects/:id           — Detalhe do projeto
PATCH  /api/projects/:id           — Editar projeto
DELETE /api/projects/:id           — Arquivar projeto (soft delete)
POST   /api/projects/:id/members   — Adicionar membro ao projeto
DELETE /api/projects/:id/members/:userId — Remover membro
POST   /api/projects/:id/template  — Salvar como template
POST   /api/projects/from-template/:templateId — Criar a partir de template
```sql

#### 1.3 Módulo de Tarefas

**Entidades:**
- `Task` (id, tenantId, projectId, columnId, title, description, assigneeId, priority, status, dueDate, estimatedHours, spentHours, position, parentId, archived, createdAt, updatedAt)
- `TaskComment` (id, taskId, userId, content, createdAt, updatedAt)
- `TaskChecklist` (id, taskId, title, completed, position)
- `TaskAttachment` (id, taskId, fileName, fileUrl, fileSize, mimeType, uploadedBy, createdAt)
- `TaskHistory` (id, taskId, userId, field, oldValue, newValue, createdAt)

**Endpoints:**
```sql
GET    /api/projects/:projectId/tasks          — Listar tarefas
POST   /api/projects/:projectId/tasks          — Criar tarefa
GET    /api/tasks/:id                          — Detalhe da tarefa
PATCH  /api/tasks/:id                          — Editar tarefa
DELETE /api/tasks/:id                          — Arquivar tarefa
PATCH  /api/tasks/:id/move                     — Mover (coluna + posição)
PATCH  /api/tasks/:id/assign                   — Atribuir responsável

POST   /api/tasks/:id/comments                 — Adicionar comentário
DELETE /api/tasks/:id/comments/:commentId      — Remover comentário

POST   /api/tasks/:id/checklist                — Adicionar item de checklist
PATCH  /api/tasks/:id/checklist/:itemId        — Marcar/desmarcar item

POST   /api/tasks/:id/attachments              — Anexar arquivo
DELETE /api/tasks/:id/attachments/:fileId      — Remover anexo

POST   /api/tasks/:id/time/start               — Iniciar time tracking
POST   /api/tasks/:id/time/stop                — Parar time tracking
GET    /api/tasks/:id/time                     — Tempo total gasto

GET    /api/tasks/:id/history                  — Histórico de alterações
```javascript

#### 1.4 Módulo de Notificações

**Entidades:**
- `Notification` (id, tenantId, userId, type, title, body, data, read, createdAt)
- `NotificationPreference` (id, userId, type, email, inApp, push)

**Endpoints:**
```text
GET    /api/notifications              — Listar notificações do usuário
PATCH  /api/notifications/:id/read     — Marcar como lida
POST   /api/notifications/read-all     — Marcar todas como lidas
GET    /api/notifications/preferences  — Preferências
PUT    /api/notifications/preferences  — Atualizar preferências
```text

**Tipos de notificação:**
- `task.assigned` — Tarefa atribuída a você
- `task.commented` — Comentário em tarefa sua
- `task.mention` — Você foi mencionado
- `task.due` — Tarefa próxima do vencimento
- `member.joined` — Novo membro no projeto
- `project.updated` — Projeto foi alterado

#### 1.5 Módulo de Relatórios

**Endpoints:**
```text
GET    /api/reports/dashboard          — Métricas do dashboard
GET    /api/reports/projects           — Relatório de projetos (PDF)
GET    /api/reports/hours              — Relatório de horas (PDF)
GET    /api/reports/hours/csv          — Relatório de horas (CSV)
GET    /api/reports/member/:userId     — Relatório por membro
```text

**Métricas do dashboard:**
```json
{
  "totalProjects": 42,
  "activeProjects": 18,
  "totalTasks": 1560,
  "tasksByStatus": { "todo": 320, "inProgress": 280, "review": 150, "done": 810 },
  "tasksCompletedThisMonth": 245,
  "tasksOverdue": 23,
  "avgCompletionTime": "3.5 days",
  "memberProductivity": [
    { "userId": "...", "name": "João", "completed": 45, "hoursLogged": 120 }
  ],
  "burndown": [
    { "date": "2026-06-01", "remaining": 120 },
    { "date": "2026-06-02", "remaining": 115 }
  ]
}
```markdown

#### 1.6 Módulo de Pagamentos

**Entidades:**
- `Subscription` (id, tenantId, stripeCustomerId, stripeSubscriptionId, plan, status, currentPeriodStart, currentPeriodEnd, trialEnd, canceledAt, createdAt)
- `Invoice` (id, tenantId, stripeInvoiceId, amount, currency, status, pdfUrl, paidAt, createdAt)

**Endpoints:**
```text
POST   /api/payments/create-checkout     — Criar sessão Stripe Checkout
GET    /api/payments/portal              — Portal de faturamento
GET    /api/payments/invoices            — Histórico de faturas
GET    /api/payments/current             — Plano atual

POST   /api/webhooks/stripe              — Webhook do Stripe (público)
```markdown

#### 1.7 Módulo de Administração

**Endpoints:**
```sql
GET    /api/admin/logs          — Logs de atividade do tenant
GET    /api/admin/audit         — Relatório de auditoria
GET    /api/admin/webhooks      — Listar webhooks configurados
POST   /api/admin/webhooks      — Criar webhook de saída
DELETE /api/admin/webhooks/:id  — Remover webhook
```markdown

---

### 2. Frontend (Next.js 14+ + Tailwind + shadcn/ui)

#### 2.1 Páginas

| Rota | Página | Componentes principais |
|------|--------|----------------------|
| `/login` | Login | LoginForm, OAuthButtons |
| `/register` | Registro | RegisterForm, TenantForm |
| `/dashboard` | Dashboard | ProjectStats, TaskChart, BurndownChart, RecentActivity |
| `/projects` | Lista de projetos | ProjectCard, ProjectFilters, CreateProjectDialog |
| `/projects/[id]` | Detalhe do projeto | ProjectHeader, MemberList, TaskList, KanbanBoard |
| `/projects/[id]/board` | Kanban board | KanbanBoard, TaskCard, Column |
| `/tasks/[id]` | Detalhe da tarefa | TaskDetail, CommentList, Checklist, TimeTracker, History |
| `/reports` | Relatórios | DashboardMetrics, ReportFilters, ExportButtons |
| `/settings` | Configurações do tenant | ProfileForm, MemberManagement, PlanInfo |
| `/settings/billing` | Faturamento | InvoiceList, PlanCard, UpgradeButton |
| `/admin` | Admin do tenant | ActivityLog, AuditReport, WebhookConfig |
| `/notifications` | Central de notificações | NotificationList, PreferencesForm |

#### 2.2 Layout

- Sidebar com navegação principal (Dashboard, Projects, Reports, Settings)
- Header com avatar, notificações (sininho com badge), busca global
- Breadcrumb para navegação hierárquica
- Modais para criação/edição de recursos

#### 2.3 Estados de UI

Toda página deve tratar:
- **Loading** — Skeleton components (shadcn/ui `Skeleton`)
- **Empty** — Ilustração + CTA (ex: "Nenhum projeto ainda. Crie o primeiro!")
- **Error** — Error boundary + botão "Tentar novamente"
- **Success** — Toast de confirmação (shadcn/ui `toast`)

---

### 3. Infraestrutura

#### 3.1 Docker

**Dockerfile.backend** (multi-stage):
```dockerfile
# Stage 1: Build
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Runtime
FROM node:20-alpine AS runner
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./
EXPOSE 3001
CMD ["node", "dist/main"]
```text

**Dockerfile.frontend** (multi-stage):
```dockerfile
# Stage 1: Build
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Runtime
FROM node:20-alpine AS runner
WORKDIR /app
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./
EXPOSE 3000
CMD ["npm", "start"]
```text

**docker-compose.yml:**
```yaml
version: '3.8'
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: saas
      POSTGRES_PASSWORD: saas_dev
      POSTGRES_DB: saas
    ports: ['5432:5432']
    volumes: ['pgdata:/var/lib/postgresql/data']

  redis:
    image: redis:7-alpine
    ports: ['6379:6379']

  backend:
    build:
      context: ./apps/backend
      dockerfile: Dockerfile
    ports: ['3001:3001']
    depends_on: [postgres, redis]
    environment:
      DATABASE_URL: postgresql://saas:saas_dev@postgres:5432/saas
      REDIS_URL: redis://redis:6379

  frontend:
    build:
      context: ./apps/frontend
      dockerfile: Dockerfile
    ports: ['3000:3000']
    depends_on: [backend]
    environment:
      NEXT_PUBLIC_API_URL: http://localhost:3001

volumes: { pgdata: }
```markdown

#### 3.2 CI/CD (GitHub Actions)

```yaml
name: CI/CD Pipeline

on:
  push: { branches: [main] }
  pull_request: { branches: [main] }

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  quality:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env: { POSTGRES_PASSWORD: test, POSTGRES_DB: test }
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
      redis:
        image: redis:7
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20 }

      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck
      - run: npm run test:ci
        env:
          DATABASE_URL: postgresql://postgres:test@localhost:5432/test
          REDIS_URL: redis://localhost:6379

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: coverage-report
          path: coverage/

  build-and-push:
    needs: [quality]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: docker build -t ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}-backend:latest ./apps/backend
      - run: docker tag ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}-backend:latest ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}-backend:${{ github.sha }}
      - run: docker push ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}-backend:${{ github.sha }}
      - run: docker push ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}-backend:latest

  deploy:
    needs: [build-and-push]
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      - run: echo "Deploy para produção..."
      # aws ecs update-service --cluster production --service backend --force-new-deployment
```markdown

---

### 4. Observabilidade

#### 4.1 Logs Estruturados (JSON)

```json
{
  "level": "info",
  "timestamp": "2026-06-26T10:30:00.000Z",
  "correlationId": "abc-123",
  "tenantId": "tenant_xyz",
  "userId": "user_456",
  "method": "POST",
  "path": "/api/projects",
  "statusCode": 201,
  "durationMs": 42,
  "message": "Project created successfully"
}
```markdown

#### 4.2 Métricas (Prometheus)

| Métrica | Tipo | Descrição |
|---------|------|-----------|
| `http_requests_total` | Counter | Total de requests por método, status, path |
| `http_request_duration_ms` | Histogram | Latência das requests (p50, p95, p99) |
| `db_query_duration_ms` | Histogram | Latência de queries no banco |
| `active_users` | Gauge | Usuários ativos no momento |
| `tasks_created_total` | Counter | Tarefas criadas (por tenant) |
| `notifications_sent_total` | Counter | Notificações enviadas |

#### 4.3 Tracing (OpenTelemetry)

```text
frontend (Browser) ──→ Next.js ──→ NestJS ──→ PostgreSQL / Redis
       ↑                   ↑           ↑              ↑
    trace-id          span-id      span-id        span-id
    (mesmo trace-id em toda a cadeia)
```markdown

#### 4.4 Dashboards (Grafana)

Três dashboards obrigatórios:

1. **Visão geral do sistema** — CPU, memória, requests/s, latência, erros, uptime
2. **Por tenant** — Mesmas métricas filtradas por tenant_id
3. **Negócio** — Tarefas criadas, concluídas, vencidas, usuários ativos por dia

---

### 5. Estrutura de Pastas (Monorepo)

```text
project-root/
├── apps/
│   ├── backend/
│   │   ├── prisma/
│   │   │   ├── schema.prisma
│   │   │   └── migrations/
│   │   ├── src/
│   │   │   ├── main.ts
│   │   │   ├── app.module.ts
│   │   │   ├── modules/
│   │   │   │   ├── auth/
│   │   │   │   ├── users/
│   │   │   │   ├── tenants/
│   │   │   │   ├── projects/
│   │   │   │   ├── tasks/
│   │   │   │   ├── notifications/
│   │   │   │   ├── reports/
│   │   │   │   ├── payments/
│   │   │   │   └── admin/
│   │   │   ├── common/
│   │   │   │   ├── guards/
│   │   │   │   ├── interceptors/
│   │   │   │   ├── pipes/
│   │   │   │   ├── filters/
│   │   │   │   └── decorators/
│   │   │   └── config/
│   │   ├── test/
│   │   │   ├── unit/
│   │   │   └── integration/
│   │   ├── Dockerfile
│   │   └── package.json
│   │
│   └── frontend/
│       ├── src/
│       │   ├── app/
│       │   │   ├── (auth)/
│       │   │   ├── (dashboard)/
│       │   │   └── layout.tsx
│       │   ├── components/
│       │   │   ├── ui/          (shadcn/ui)
│       │   │   ├── forms/
│       │   │   ├── layout/
│       │   │   └── shared/
│       │   ├── lib/
│       │   │   ├── api.ts
│       │   │   ├── auth.ts
│       │   │   └── utils.ts
│       │   └── hooks/
│       ├── public/
│       ├── Dockerfile
│       └── package.json
│
├── packages/
│   └── shared/
│       ├── schemas/     (Zod schemas compartilhados)
│       ├── types/       (TypeScript interfaces)
│       └── constants/   (papéis, planos, limites)
│
├── docker/
│   ├── docker-compose.yml
│   ├── Dockerfile.backend
│   └── Dockerfile.frontend
│
├── docs/
│   ├── adrs/
│   │   ├── ADR-001-modular-monolith.md
│   │   ├── ADR-002-multi-tenancy-strategy.md
│   │   ├── ADR-003-event-driven-communication.md
│   │   └── ADR-004-server-components.md
│   ├── architecture.md
│   ├── runbook.md
│   └── api.md
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── .env.example
├── .gitignore
├── README.md
└── package.json (raiz — scripts do monorepo)
```markdown

---

### 6. Prisma Schema

```prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

enum TenantPlan {
  FREE
  PRO
  ENTERPRISE
}

enum UserRole {
  OWNER
  ADMIN
  MANAGER
  DEVELOPER
  VIEWER
}

enum ProjectStatus {
  ACTIVE
  ARCHIVED
}

enum TaskPriority {
  LOW
  MEDIUM
  HIGH
  CRITICAL
}

model Tenant {
  id        String     @id @default(cuid())
  name      String
  slug      String     @unique
  plan      TenantPlan @default(FREE)
  status    String     @default("active")
  settings  Json       @default("{}")
  createdAt DateTime   @default(now())
  updatedAt DateTime   @updatedAt

  users           User[]
  projects        Project[]
  invites         Invite[]
  subscriptions   Subscription[]
  members         ProjectMember[]
}

model User {
  id             String   @id @default(cuid())
  tenantId       String
  name           String
  email          String
  password       String
  role           UserRole @default(DEVELOPER)
  avatar         String?
  isActive       Boolean  @default(true)
  createdAt      DateTime @default(now())
  updatedAt      DateTime @updatedAt

  tenant         Tenant   @relation(fields: [tenantId], references: [id])
  projects       Project[]
  assignedTasks  Task[]   @relation("TaskAssignee")
  comments       TaskComment[]
  notifications  Notification[]
  timeEntries    TimeEntry[]
  projectMembers ProjectMember[]

  @@unique([tenantId, email])
  @@index([tenantId])
}

model Invite {
  id        String   @id @default(cuid())
  tenantId  String
  email     String
  role      UserRole
  token     String   @unique
  expiresAt DateTime
  status    String   @default("pending")
  createdAt DateTime @default(now())

  tenant Tenant @relation(fields: [tenantId], references: [id])

  @@index([tenantId])
  @@index([token])
}

model Project {
  id          String        @id @default(cuid())
  tenantId    String
  name        String
  description String?
  ownerId     String
  status      ProjectStatus @default(ACTIVE)
  priority    TaskPriority  @default(MEDIUM)
  startDate   DateTime?
  endDate     DateTime?
  tags        String[]      @default([])
  archivedAt  DateTime?
  createdAt   DateTime      @default(now())
  updatedAt   DateTime      @updatedAt

  tenant      Tenant         @relation(fields: [tenantId], references: [id])
  owner       User           @relation(fields: [ownerId], references: [id])
  tasks       Task[]
  members     ProjectMember[]

  @@index([tenantId, status])
  @@index([tenantId, ownerId])
}

model ProjectMember {
  id        String   @id @default(cuid())
  projectId String
  userId    String
  role      String   @default("member")
  joinedAt  DateTime @default(now())

  project Project @relation(fields: [projectId], references: [id])
  user    User    @relation(fields: [userId], references: [id])

  @@unique([projectId, userId])
  @@index([projectId])
  @@index([userId])
}

model Task {
  id             String        @id @default(cuid())
  tenantId       String
  projectId      String
  columnId       String?
  title          String
  description    String?
  assigneeId     String?
  priority       TaskPriority  @default(MEDIUM)
  status         String        @default("todo")
  dueDate        DateTime?
  estimatedHours Float?
  spentHours     Float         @default(0)
  position       Int           @default(0)
  parentId       String?
  archivedAt     DateTime?
  createdAt      DateTime      @default(now())
  updatedAt      DateTime      @updatedAt

  project       Project          @relation(fields: [projectId], references: [id])
  assignee      User?            @relation("TaskAssignee", fields: [assigneeId], references: [id])
  comments      TaskComment[]
  checklists    TaskChecklist[]
  attachments   TaskAttachment[]
  histories     TaskHistory[]
  timeEntries   TimeEntry[]

  @@index([tenantId, projectId, status])
  @@index([tenantId, assigneeId])
  @@index([tenantId, dueDate])
}

model TaskComment {
  id        String   @id @default(cuid())
  taskId    String
  userId    String
  content   String
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  task Task @relation(fields: [taskId], references: [id])
  user User @relation(fields: [userId], references: [id])

  @@index([taskId])
}

model TaskChecklist {
  id        String  @id @default(cuid())
  taskId    String
  title     String
  completed Boolean @default(false)
  position  Int     @default(0)

  task Task @relation(fields: [taskId], references: [id])

  @@index([taskId])
}

model TaskAttachment {
  id         String   @id @default(cuid())
  taskId     String
  fileName   String
  fileUrl    String
  fileSize   Int
  mimeType   String
  uploadedBy String
  createdAt  DateTime @default(now())

  task Task @relation(fields: [taskId], references: [id])

  @@index([taskId])
}

model TaskHistory {
  id        String   @id @default(cuid())
  taskId    String
  userId    String
  field     String
  oldValue  String?
  newValue  String?
  createdAt DateTime @default(now())

  task Task @relation(fields: [taskId], references: [id])

  @@index([taskId])
}

model TimeEntry {
  id        String   @id @default(cuid())
  taskId    String
  userId    String
  startedAt DateTime
  endedAt   DateTime?
  duration  Int
  createdAt DateTime @default(now())

  task Task @relation(fields: [taskId], references: [id])
  user User @relation(fields: [userId], references: [id])

  @@index([taskId])
  @@index([userId])
}

model Notification {
  id        String   @id @default(cuid())
  tenantId  String
  userId    String
  type      String
  title     String
  body      String?
  data      Json?
  read      Boolean  @default(false)
  createdAt DateTime @default(now())

  user User @relation(fields: [userId], references: [id])

  @@index([userId, read])
  @@index([userId, createdAt])
}

model NotificationPreference {
  id     String  @id @default(cuid())
  userId String  @unique
  email  Boolean @default(true)
  inApp  Boolean @default(true)
  push   Boolean @default(false)
}

model Subscription {
  id                   String      @id @default(cuid())
  tenantId             String      @unique
  stripeCustomerId     String      @unique
  stripeSubscriptionId String      @unique
  plan                 TenantPlan  @default(FREE)
  status               String      @default("trialing")
  currentPeriodStart   DateTime
  currentPeriodEnd     DateTime
  trialEnd             DateTime?
  canceledAt           DateTime?
  createdAt            DateTime    @default(now())
  updatedAt            DateTime    @updatedAt

  tenant Tenant @relation(fields: [tenantId], references: [id])
}

model Invoice {
  id               String   @id @default(cuid())
  tenantId         String
  stripeInvoiceId  String   @unique
  amount           Int
  currency         String   @default("brl")
  status           String
  pdfUrl           String?
  paidAt           DateTime?
  createdAt        DateTime @default(now())

  tenant Tenant @relation(fields: [tenantId], references: [id])

  @@index([tenantId])
}
```markdown

---

### 7. Critérios de Aceite do Projeto

O projeto será considerado completo quando atender a todos os critérios abaixo:

#### Essenciais (MVP)

| # | Critério | Como verificar |
|---|----------|---------------|
| 1 | Usuário registra empresa e faz login | Fluxo de registro + login funcional |
| 2 | Usuário cria projeto | CRUD de projetos funcional |
| 3 | Usuário cria tarefas em um projeto | CRUD de tarefas funcional |
| 4 | Kanban board com drag & drop | Mover tarefa entre colunas |
| 5 | Comentários em tarefas | Adicionar e listar comentários |
| 6 | RBAC funcional | Developer não consegue criar projeto (403) |
| 7 | Isolamento multi-tenant | Tenant A não vê dados de Tenant B |
| 8 | Container Docker | `docker compose up` sobe toda aplicação |
| 9 | Pipeline CI/CD | GitHub Actions passa lint, test, build |
| 10 | Testes unitários (mín. 40) | `npm test` passa |

#### Importantes

| # | Critério | Como verificar |
|---|----------|---------------|
| 11 | Notificações in-app | Ao receber tarefa, notificação aparece |
| 12 | Dashboard com gráficos | Dashboard exibe tarefas por status |
| 13 | Upload de anexos em tarefas | Anexar arquivo e ver na tarefa |
| 14 | Logs estruturados (JSON) | Logs no console em formato JSON |
| 15 | Health checks | `/health` e `/ready` retornam OK |
| 16 | Cache Redis | Segunda chamada ao mesmo endpoint é mais rápida |
| 17 | Validação com Zod | Dados inválidos retornam 422 com detalhes |
| 18 | Exception Filter | Erros não tratados retornam 500 padronizado |
| 19 | Testes de integração (mín. 10) | Testes com banco real funcionam |
| 20 | README completo | Instruções de setup, env, deploy |

#### Diferenciais (pontuação extra)

| # | Critério |
|---|----------|
| 21 | Deploy em cloud (AWS/Azure/GCP) com URL pública |
| 22 | WebSocket em tempo real (Kanban multiplayer) |
| 23 | Integração Stripe com checkout funcional |
| 24 | Relatórios exportáveis (PDF/CSV) |
| 25 | Histórico de auditoria (tabela TaskHistory populada) |
| 26 | Testes E2E com Playwright (mín. 5 cenários) |
| 27 | Dashboard Grafana com métricas |
| 28 | Tracing com OpenTelemetry |
| 29 | Autenticação OAuth (Google/GitHub) |
| 30 | Integração com IA (sugestão de prioridade, chatbot) |

---

### 8. Template de README

O README deve seguir este formato mínimo:

```markdown
# [Nome do Projeto]

> SaaS de gestão de projetos e tarefas multi-tenant.

## Stack

- **Backend:** NestJS + Prisma + PostgreSQL + Redis
- **Frontend:** Next.js 14 + Tailwind + shadcn/ui
- **Infra:** Docker + [Cloud Provider]
- **CI/CD:** GitHub Actions

## Funcionalidades

- [x] Autenticação multi-tenant (JWT + OAuth)
- [x] CRUD de projetos com permissões
- [x] CRUD de tarefas com Kanban drag & drop
- [x] Comentários e menções em tempo real
- [x] Notificações in-app e e-mail
- [x] Dashboard com métricas e gráficos
- [x] Relatórios exportáveis (PDF/CSV)
- [x] Planos e pagamentos (Stripe)
- [x] RBAC com 5 papéis
- [ ] Integração com IA (próxima sprint)

## Quick Start

```bash
git clone <repo-url>
cd <repo-name>
cp .env.example .env
docker compose up
```markdown

Acesse http://localhost:3000

## Estrutura

```text
apps/
├── backend/   → NestJS API (porta 3001)
└── frontend/  → Next.js App (porta 3000)
packages/
└── shared/    → Tipos, schemas, constantes
docs/
└── adrs/      → Decisões arquiteturais
```markdown

## Testes

```bash
# Todos os testes
npm test

# Apenas unitários
npm run test:unit

# Apenas integração
npm run test:integration

# Cobertura
npm run test:coverage
```markdown

## Deploy

| Ambiente | URL | Status |
|----------|-----|--------|
| Production | https://app.meusistema.com | ✅ |
| Staging | https://staging.meusistema.com | ✅ |

## Documentação

- [Swagger / OpenAPI](link)
- [ADRs](docs/adrs/)
- [Runbook](docs/runbook.md)
- [Arquitetura](docs/architecture.md)

## Licença

MIT
```markdown

---

### 9. Sugestão de Cronograma (8 semanas)

| Semana | Foco | Entregas |
|--------|------|----------|
| 1 | Setup | Monorepo, Docker, CI/CD, Prisma schema, banco |
| 2 | Auth | Auth module, Tenant module, JWT, OAuth |
| 3 | Projetos | Project CRUD, ProjectMember, RBAC |
| 4 | Tarefas | Task CRUD, Kanban, drag & drop |
| 5 | Tempo real | WebSocket, Notificações, Comentários |
| 6 | Relatórios | Dashboard, gráficos, exportação PDF/CSV |
| 7 | Pagamentos | Stripe integration, planos, webhooks |
| 8 | Finalização | Testes, documentação, deploy, apresentação |

---

**Boa construção. Que este projeto seja o destaque do seu portfólio.**
