# Agentes para o Módulo 21 — Projeto Final

## Agentes envolvidos

| Agente | Função |
|--------|--------|
| Curriculum Architect | Definir escopo, critérios de avaliação, entregáveis |
| Enterprise Architect Agent | Validar decisões arquiteturais (ADRs), trade-offs |
| Backend Engineer Agent | Implementar módulos NestJS, Prisma, Redis, WebSocket |
| Frontend Engineer Agent | Implementar Next.js, Tailwind, shadcn/ui, React Query |
| DevOps Engineer Agent | Docker, CI/CD, deploy cloud, observabilidade |
| QA Engineer Agent | Testes unitários, integração, E2E, cobertura |
| Security Analyst Agent | Revisar autenticação, RBAC, rate limiting, OWASP |
| Product Manager Agent | Definir backlog, priorizar features, validar MVP |
| AI/ML Engineer Agent | Integrar agentes de IA (sugestão, automação) |

## Instruções específicas

### Enterprise Architect Agent

Ao revisar:
- Verificar se ADRs documentam contexto, decisão, justificativa e consequências
- Validar trade-offs: monólito vs microservices, RLS vs schema, evento vs chamada direta
- Garantir que a arquitetura suporta extração futura para microservices
- Revisar diagrama de arquitetura (componentes, fluxos, boundaries)

### Backend Engineer Agent

Ao implementar:
- Seguir modular structure com módulos autocontidos
- Guards: `JwtAuthGuard`, `RolesGuard`, `PermissionsGuard`, `TenantGuard`
- Interceptors: logging, transformação, cache
- Filters: `GlobalExceptionFilter` com erros de domínio
- WebSocket Gateway com autenticação e rooms por tenant/projeto
- Bull queues para jobs assíncronos (e-mail, relatórios, limpeza)
- Validação com Zod em todos os DTOs
- Testes unitários e de integração para cada service
- Índices compostos (tenant_id + id) para performance multi-tenant

### Frontend Engineer Agent

Ao implementar:
- Next.js App Router com Server Components por padrão
- Client Components apenas onde necessário (interatividade, drag & drop)
- React Query para server state com cache e invalidação
- Zustand para client state (UI state, preferências)
- shadcn/ui components consistentes com design system
- Drag & drop com `@dnd-kit/core` no Kanban board
- WebSocket client com Socket.io para tempo real
- Otimistic updates no Kanban (mover tarefa antes da confirmação)
- Páginas: Login, Register, Dashboard, Project, Board, Task Detail, Reports, Settings, Admin

### DevOps Engineer Agent

Ao configurar:
- Dockerfile multi-stage (dev, build, produção)
- docker-compose com PostgreSQL, Redis, backend, frontend
- GitHub Actions: lint → typecheck → test → build → deploy
- ECS Fargate task definitions (ou EKS manifests)
- RDS PostgreSQL Multi-AZ com PgBouncer
- ElastiCache Redis com replicação
- S3 para arquivos com presigned URLs
- CloudFront CDN para assets estáticos
- Variáveis de ambiente via Secrets Manager

### QA Engineer Agent

Ao validar:
- Mín. 40 testes unitários (services, guards, filters)
- Mín. 10 testes de integração (controllers + banco real)
- Mín. 5 testes E2E (Playwright): registro, criar projeto, Kanban, notificação, relatório
- Cobertura > 80% unitários, > 60% integração
- Testes específicos de isolamento multi-tenant (tenant A não vê dados de tenant B)
- Testes de RBAC (cada papel testado contra endpoints proibidos)
- Testes de rate limiting (exceder limite deve retornar 429)

### Security Analyst Agent

Ao revisar:
- JWT com claims: userId, tenantId, role, permissions
- Refresh token com rotação (um uso só)
- Nenhuma query sem filtro de tenant_id
- Rate limiting por IP (100/min) e por usuário autenticado (1000/min)
- CORS whitelist configurável
- Helmet headers (CSP, X-Frame-Options, HSTS)
- Sanitização de HTML em comentários (XSS)
- bcrypt cost 12 para senhas
- Secrets no Secrets Manager, nunca no código
- Logs sem dados sensíveis (PII, senhas, tokens)

### Product Manager Agent

Ao definir backlog:
- MVP: autenticação + projetos + tarefas + Kanban básico
- V2: notificações + relatórios + time tracking
- V3: pagamentos + integrações + IA
- Priorizar features por valor de negócio vs esforço técnico
- Definir critérios de aceite para cada user story
- Validar se o produto resolve o problema proposto

### AI/ML Engineer Agent

Ao integrar IA:
- Sugestão automática de prioridade baseada em descrição da tarefa
- Estimativa de horas baseada em tarefas similares concluídas
- Atribuição inteligente (responsável com menor carga)
- Chatbot para tirar dúvidas sobre o sistema
- Geração automática de resumo de projeto

## Fluxo de trabalho recomendado

```text
Sprint 1 (Setup):
  DevOps → Docker, CI/CD, infra cloud
  Backend → Auth + Tenant modules
  Frontend → Login, Register, setup pages

Sprint 2 (Core):
  Backend → Projects + Tasks modules
  Frontend → Project CRUD, Task CRUD, Kanban board
  QA → Testes de CRUD e RBAC

Sprint 3 (Real-time & Notifications):
  Backend → WebSocket, Notifications module
  Frontend → Tempo real no board, central de notificações
  QA → Testes de WebSocket e concorrência

Sprint 4 (Reports & Payments):
  Backend → Reports + Payments modules
  Frontend → Dashboards, gráficos, página de planos
  QA → Testes de relatórios e webhooks

Sprint 5 (Polish & Deploy):
  Todos → Revisão de segurança, performance, observabilidade
  DevOps → Deploy produção, monitoramento ativo
  Documentação → README, ADRs, Swagger, runbook
  Preparação → Pitch, demo, slides
```text
