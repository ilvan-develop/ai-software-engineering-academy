# Módulo 21 — Exercícios Preparatórios

Antes de iniciar o Projeto Final, resolva estes 5 exercícios para aquecer e revisar os conceitos mais críticos dos módulos anteriores.

---

## Exercício 1: Setup da Stack Completa

Configure o ambiente de desenvolvimento local com toda a stack do projeto final.

### Requisitos

1. Crie um monorepo com a seguinte estrutura:
   ```
   apps/
     backend/     (NestJS + Prisma)
     frontend/    (Next.js 14+)
   packages/
     shared/      (tipos, schemas Zod, constantes)
   docker/
     docker-compose.yml
     Dockerfile.backend
     Dockerfile.frontend
   ```

2. O `docker-compose.yml` deve subir:
   - PostgreSQL 16
   - Redis 7
   - Backend (NestJS em modo dev)
   - Frontend (Next.js em modo dev)

3. Configure variáveis de ambiente via `.env.example` e `.env`:
   ```env
   DATABASE_URL=postgresql://user:pass@localhost:5432/saas
   REDIS_URL=redis://localhost:6379
   JWT_SECRET=
   JWT_REFRESH_SECRET=
   STRIPE_SECRET_KEY=
   STRIPE_WEBHOOK_SECRET=
   GOOGLE_CLIENT_ID=
   GOOGLE_CLIENT_SECRET=
   ```

4. O backend deve expor `GET /health` e `GET /ready` com verificação de banco e Redis.

5. O frontend deve exibir uma página inicial que consome `GET /health` do backend.

### Entrega

O repositório deve estar funcional com `docker compose up` e ambos os serviços rodando.

---

## Exercício 2: Módulo de Autenticação Multi-tenant

Implemente o módulo de autenticação completo com suporte multi-tenant.

### Especificação

1. **Registro de tenant + owner:**
   ```
   POST /api/auth/register
   Body: { companyName, adminName, adminEmail, adminPassword }
   
   Response: { accessToken, refreshToken, tenant, user }
   ```

2. **Login com e-mail + senha:**
   ```
   POST /api/auth/login
   Body: { email, password }
   
   Response: { accessToken, refreshToken, tenant, user }
   ```

3. **Refresh token:**
   ```
   POST /api/auth/refresh
   Body: { refreshToken }
   
   Response: { accessToken, refreshToken }
   ```

4. **Logout (invalidar refresh token):**
   ```
   POST /api/auth/logout
   Headers: Authorization: Bearer <accessToken>
   Body: { refreshToken }
   ```

5. **Convidar membro:**
   ```
   POST /api/tenants/:tenantId/invite
   Body: { email, role (Admin | Manager | Developer | Viewer) }
   
   Efeito: enviar e-mail com link de aceite
   ```

6. **Aceitar convite:**
   ```
   POST /api/auth/accept-invite
   Body: { token (do link do e-mail), name, password }
   ```

### Regras de negócio

- E-mail deve ser único dentro do mesmo tenant
- Owner não pode ser removido
- Apenas Owner e Admin podem convidar membros
- Token JWT expira em 15 minutos
- Refresh token expira em 7 dias e só pode ser usado uma vez (rotação)
- Bloquear login após 5 tentativas falhas por 15 minutos

### Testes

Escreva testes unitários para:
- `AuthService.register()` — deve criar tenant + owner + retornar tokens
- `AuthService.login()` — deve validar credenciais e retornar tokens
- `AuthService.refreshToken()` — deve rotacionar o token
- `TenantService.inviteMember()` — deve criar convite e enviar e-mail (mock)

---

## Exercício 3: RBAC com Guards e Permissões Granulares

Implemente o sistema de RBAC com papéis hierárquicos e permissões por recurso.

### Estrutura de papéis

```
Owner    → tudo (inclusive faturamento e exclusão do tenant)
Admin    → gerenciar membros, configurar workspace, criar projetos
Manager  → criar/editar projetos, alocar tarefas, relatórios
Developer→ executar tarefas, comentar, anexar arquivos
Viewer   → somente leitura
```

### Permissões por recurso

Defina permissões no formato `{recurso}:{acao}`:

| Permissão | Owner | Admin | Manager | Developer | Viewer |
|-----------|-------|-------|---------|-----------|--------|
| `project:create` | ✅ | ✅ | ✅ | ❌ | ❌ |
| `project:edit` | ✅ | ✅ | ✅ | ❌ | ❌ |
| `project:delete` | ✅ | ✅ | ❌ | ❌ | ❌ |
| `project:view` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `task:create` | ✅ | ✅ | ✅ | ✅ | ❌ |
| `task:assign` | ✅ | ✅ | ✅ | ❌ | ❌ |
| `task:complete` | ✅ | ✅ | ✅ | ✅ | ❌ |
| `member:invite` | ✅ | ✅ | ❌ | ❌ | ❌ |
| `member:remove` | ✅ | ✅ | ❌ | ❌ | ❌ |
| `billing:view` | ✅ | ❌ | ❌ | ❌ | ❌ |
| `settings:edit` | ✅ | ✅ | ❌ | ❌ | ❌ |

### Implementação

1. Crie um `RolesGuard` que verifica o papel do usuário
2. Crie um `PermissionsGuard` que verifica permissões específicas
3. Use decorators customizados:
   ```typescript
   @Roles('Admin', 'Manager')
   @Permissions('project:create')
   @Post()
   createProject(@Body() dto: CreateProjectDto) { }
   ```

### Testes

- Testar que Developer não pode criar projeto (deve retornar 403)
- Testar que Viewer não pode editar tarefa
- Testar que Owner pode remover membro
- Testar que Manager pode gerar relatório

---

## Exercício 4: Kanban com WebSocket em Tempo Real

Implemente o quadro Kanban com drag & drop e atualização em tempo real via WebSocket.

### Funcionalidades

1. **Colunas personalizáveis:**
   ```
   GET /api/projects/:projectId/board
   Response: { columns: [{ id, name, tasks: [...] }] }
   ```

2. **Mover tarefa entre colunas:**
   ```
   PATCH /api/tasks/:taskId/move
   Body: { columnId, position }
   
   WebSocket: emitir 'task:moved' para todos no projeto
   ```

3. **WebSocket Gateway:**
   ```typescript
   @WebSocketGateway({ namespace: '/tasks' })
   export class TaskGateway {
     @SubscribeMessage('task:move')
     handleMove(client, payload: MoveTaskDto) {
       // Validar permissão
       // Atualizar no banco
       // Emitir para sala do projeto
       this.server.to(`project:${payload.projectId}`).emit('task:moved', payload);
     }
   }
   ```

4. **Frontend com drag & drop:**
   - Use `@dnd-kit/core` para drag & drop
   - Otimistic update: mover visualmente antes da confirmação do servidor
   - Rollback se a API rejeitar

5. **Indicador de "alguém está editando":**
   ```
   WebSocket: 'task:editing' → { taskId, userId, userName }
   Exibir: "João está editando esta tarefa"
   ```

### Regras

- Apenas membros do projeto podem ver o board
- Apenas roles com permissão `task:edit` podem mover tarefas
- Histórico de movimentação registrado (auditoria)

---

## Exercício 5: Pipeline CI/CD e Deploy em Cloud

Configure a pipeline de CI/CD e faça o deploy do sistema em uma cloud (AWS, Azure ou GCP).

### CI/CD (GitHub Actions)

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck

  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env: { POSTGRES_PASSWORD: test }
      redis:
        image: redis:7
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run test:ci

  build:
    needs: [lint, test]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: docker build -t app:${{ github.sha }} .
      - run: docker tag app:${{ github.sha }} ${{ secrets.REGISTRY }}/app:${{ github.sha }}
      - run: docker push ${{ secrets.REGISTRY }}/app:${{ github.sha }}

  deploy:
    needs: [build]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploy para produção (manual trigger)"
```

### Deploy (AWS - exemplo)

1. **Backend:** ECS Fargate (ou EKS)
   - Task definition com 2 containers: app + nginx reverse proxy
   - Auto-scaling: 2–10 instâncias baseado em CPU
   - ALB (Application Load Balancer) com SSL

2. **Banco:** RDS PostgreSQL
   - Multi-AZ
   - Backup automático diário
   - PgBouncer para connection pooling

3. **Cache:** ElastiCache Redis
   - Cluster mode desligado (1 shard, 2 réplicas)

4. **Arquivos:** S3
   - Bucket público para avatares e anexos
   - Presigned URLs para upload seguro

5. **Frontend:** Vercel ou CloudFront + S3
   - Build estático ou SSR na Vercel
   - CDN global

6. **Observabilidade:**
   - CloudWatch Logs para logs
   - CloudWatch Metrics para métricas
   - X-Ray para tracing
   - Grafana (opcional, via sidecar)

### Entregáveis

- Pipeline rodando no GitHub Actions com sucesso
- URL pública do sistema funcional
- README com instruções de deploy
- Script de infraestrutura (Terraform ou CDK — opcional, mas pontua extra)

---

## Bônus: Integração com Pagamentos (Stripe)

Implemente a integração com Stripe para planos e assinaturas.

### Funcionalidades

1. **Checkout:**
   ```
   POST /api/payments/create-checkout
   Body: { priceId (do Stripe Dashboard), tenantId }
   
   Response: { url (redirect para Stripe Checkout) }
   ```

2. **Webhook:**
   ```typescript
   @Post('webhooks/stripe')
   @Public()
   async handleWebhook(@Req() req, @Headers('stripe-signature') sig: string) {
     const event = stripe.webhooks.constructEvent(req.rawBody, sig, webhookSecret);
     
     switch (event.type) {
       case 'checkout.session.completed':
         await this.paymentService.activateSubscription(event.data.object);
         break;
       case 'customer.subscription.updated':
         await this.paymentService.updateSubscription(event.data.object);
         break;
       case 'customer.subscription.deleted':
         await this.paymentService.cancelSubscription(event.data.object);
         break;
     }
   }
   ```

3. **Planos:**
   | Plano | Preço | Projetos | Membros | Storage |
   |-------|-------|----------|---------|---------|
   | Free | Grátis | 3 | 5 | 100MB |
   | Pro | R$ 29/mês | Ilimitado | 50 | 10GB |
   | Enterprise | R$ 99/mês | Ilimitado | Ilimitado | 100GB |

4. **Rate limits por plano:**
   ```typescript
   // middleware/rate-limiter.ts
   const limits = {
     free: { rpm: 100, projects: 3, members: 5 },
     pro: { rpm: 1000, projects: Infinity, members: 50 },
     enterprise: { rpm: 5000, projects: Infinity, members: Infinity },
   };
   ```

### Testes

- Mock do Stripe API nos testes
- Testar webhook com payload assinado
- Testar que Free não pode criar mais de 3 projetos
