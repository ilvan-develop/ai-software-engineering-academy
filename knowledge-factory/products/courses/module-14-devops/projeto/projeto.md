# Módulo 14 — DevOps: Docker, CI/CD e Deploy

**Da máquina do desenvolvedor à produção.**

---

## 1. Por que DevOps importa

DevOps é a ponte entre o **código funcionando na máquina do dev** e o **código funcionando em produção**.

### O problema clássico

```
"Funciona na minha máquina" → "Não funciona no servidor"

Causas:
  - Versões diferentes de dependências
  - Variáveis de ambiente não configuradas
  - Banco de dados diferente
  - Sistema operacional diferente
  - Permissões diferentes
```

### A solução DevOps

```
Containerização (Docker):
  → Mesmo ambiente em dev, staging e produção
  → Dependências isoladas
  → Reproducível em qualquer máquina

CI/CD:
  → Cada push é testado automaticamente
  → Deploy é um processo, não um evento
  → Rollback rápido se algo der errado
```

---

## 2. Docker — Containerização

### O que é um container

```
┌────────────────────────────────────────┐
│  CONTAINER                             │
│  ┌──────────────────────────────────┐  │
│  │  Aplicação (Node.js)             │  │
│  ├──────────────────────────────────┤  │
│  │  Dependências (npm packages)     │  │
│  ├──────────────────────────────────┤  │
│  │  Runtime (Node 20)               │  │
│  ├──────────────────────────────────┤  │
│  │  Sistema (Alpine Linux)          │  │
│  └──────────────────────────────────┘  │
└────────────────────────────────────────┘
```

### Dockerfile multi-stage (o padrão correto)

```dockerfile
# === ESTÁGIO 1: Instalação ===
FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --only=production

# === ESTÁGIO 2: Build ===
FROM node:20-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

# === ESTÁGIO 3: Runtime (imagem final LEVE) ===
FROM node:20-alpine AS runner
WORKDIR /app

# Segurança: não rodar como root
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 appuser

COPY --from=deps /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY package.json ./

USER appuser

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

ENV NODE_ENV=production
CMD ["node", "dist/main"]
```

### docker-compose.yml

```yaml
services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    env_file: .env
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    healthcheck:
      test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:3000/health"]
      interval: 30s
      timeout: 3s
      retries: 3

  db:
    image: postgres:16-alpine
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    env_file: .env
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 5

volumes:
  postgres_data:
  redis_data:
```

### .dockerignore

```
node_modules
.git
.env
dist
.gitignore
*.md
coverage
```

---

## 3. GitHub Actions — CI/CD

### Pipeline de CI (todo push)

```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck

  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: test
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'
      - run: npm ci
      - run: npm run test -- --coverage
      - uses: actions/upload-artifact@v4
        with:
          name: coverage
          path: coverage/

  build:
    runs-on: ubuntu-latest
    needs: [lint, test]
    steps:
      - uses: actions/checkout@v4
      - run: docker build -t app:${{ github.sha }} .
      - run: docker tag app:${{ github.sha }} app:latest
```

### Pipeline de CD (deploy em staging/produção)

```yaml
name: CD

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    needs: [lint, test, build]
    environment: production

    steps:
      - uses: actions/checkout@v4

      - name: Login no Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build e push da imagem
        run: |
          docker build -t app:${{ github.sha }} .
          docker tag app:${{ github.sha }} app:latest
          docker push app:${{ github.sha }}

      - name: Deploy via SSH
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.HOST }}
          username: ${{ secrets.USERNAME }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            cd /app
            docker compose pull
            docker compose up -d --force-recreate
            docker system prune -f
```

---

## 4. Variáveis de Ambiente

### .env.example (commitado)

```
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/db

# JWT
JWT_SECRET=change-me
JWT_REFRESH_SECRET=change-me

# Redis
REDIS_URL=redis://localhost:6379

# API
PORT=3000
NODE_ENV=development
```

### Validação na inicialização

```typescript
import { z } from 'zod';

const EnvSchema = z.object({
  NODE_ENV: z.enum(['development', 'staging', 'production']),
  PORT: z.string().transform(Number).pipe(z.number().positive()),
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
  JWT_REFRESH_SECRET: z.string().min(32),
  REDIS_URL: z.string().url(),
});

export type Env = z.infer<typeof EnvSchema>;

export function validateEnv(): Env {
  const result = EnvSchema.safeParse(process.env);
  if (!result.success) {
    console.error('❌ Variáveis de ambiente inválidas:', result.error.flatten());
    process.exit(1);
  }
  return result.data;
}

// main.ts
const env = validateEnv();
```

---

## 5. Estratégias de Deploy

### Blue-Green Deployment

```
Versão Azul (atual):
  ┌──────────┐
  │ app:v1   │ ← Load Balancer (tráfego ativo)
  └──────────┘

Versão Verde (nova):
  ┌──────────┐
  │ app:v2   │ (sem tráfego)
  └──────────┘

Passo 1: Deploy da versão verde
Passo 2: Testar versão verde
Passo 3: Troca LB para verde
Passo 4: Se erro, troca de volta (rollback imediato)
```

### Rolling Update

```
Passo 1: Sobe nova instância com v2
Passo 2: Remove uma instância v1
Passo 3: Repete até todas serem v2

Prós: Sem downtime
Contras: Duas versões convivem
```

### Canary Release

```
5% do tráfego → v2 (monitorar)
Se estável → 25% → 50% → 100%

Prós: Risco mínimo
Contras: Complexo de configurar
```

---

## 6. Docker Compose para múltiplos ambientes

### docker-compose.override.yml (dev)

```yaml
services:
  api:
    build:
      context: .
      dockerfile: Dockerfile.dev
    volumes:
      - .:/app  # Hot reload
      - /app/node_modules
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development

  db:
    ports:
      - "5432:5432"

  redis:
    ports:
      - "6379:6379"
```

### docker-compose.prod.yml (produção)

```yaml
services:
  api:
    restart: always
    deploy:
      replicas: 3
      resources:
        limits:
          memory: 512M
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  db:
    restart: always
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./backup:/backup
    deploy:
      resources:
        limits:
          memory: 1G
```

---

## 7. Health Checks e Graceful Shutdown

### Health check endpoint

```typescript
@Controller('health')
export class HealthController {
  constructor(
    private prisma: PrismaService,
    private redis: RedisService,
  ) {}

  @Get()
  async check(): Promise<HealthResponse> {
    const checks = await Promise.all([
      this.checkComponent('database', () => this.prisma.$queryRaw`SELECT 1`),
      this.checkComponent('redis', () => this.redis.ping()),
    ]);

    return {
      status: checks.every(c => c.status === 'healthy') ? 'healthy' : 'degraded',
      timestamp: new Date().toISOString(),
      checks,
    };
  }

  private async checkComponent(name: string, check: () => Promise<unknown>) {
    try {
      await check();
      return { name, status: 'healthy' as const };
    } catch (error) {
      return { name, status: 'unhealthy' as const, error: (error as Error).message };
    }
  }
}

@Get('/ready')
async ready(): Promise<{ status: string }> {
  // Readiness = todas as dependências prontas
  return this.check();
}

@Get('/live')
async live(): Promise<{ status: string }> {
  // Liveness = servidor está rodando
  return { status: 'alive' };
}
```

### Graceful Shutdown

```typescript
import { PrismaService } from './prisma.service';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  app.enableShutdownHooks();

  const prisma = app.get(PrismaService);
  await prisma.enableShutdownHooks(app);

  await app.listen(3000);

  console.log(`🚀 Servidor rodando em http://localhost:3000`);
}

// main.ts
process.on('SIGTERM', async () => {
  console.log('SIGTERM recebido, desligando...');
  await app.close();
  process.exit(0);
});

process.on('SIGINT', async () => {
  console.log('SIGINT recebido, desligando...');
  await app.close();
  process.exit(0);
});
```

---

## 8. Logs Estruturados

### Configuração de logs em JSON

```typescript
import { Logger } from '@nestjs/common';
import { utilities as nestWinstonModuleUtilities } from 'nest-winston';
import * as winston from 'winston';

// main.ts
app.useLogger(
  winston.createLogger({
    level: process.env.NODE_ENV === 'production' ? 'info' : 'debug',
    format: winston.format.combine(
      winston.format.timestamp(),
      winston.format.json(),  // Logs em JSON (melhor para ferramentas)
    ),
    transports: [
      new winston.transports.Console(),
      new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),
      new winston.transports.File({ filename: 'logs/combined.log' }),
    ],
  })
);
```

### Exemplo de log estruturado

```json
{
  "timestamp": "2026-06-01T10:30:00.000Z",
  "level": "error",
  "message": "Falha na autenticação",
  "context": "AuthService",
  "userId": "abc123",
  "ip": "192.168.1.1",
  "attempt": 3,
  "stack": "..."
}
```

---

## Resumo

1. **Docker multi-stage** — imagem final leve, segura, reproduzível
2. **docker-compose** — orquestração local com dependências (db, redis)
3. **CI/CD com GitHub Actions** — lint, testes, build, deploy automático
4. **Validação de env** — falhe cedo se variáveis ausentes
5. **Blue-Green / Rolling / Canary** — estratégias de deploy sem downtime
6. **Health checks** — /health, /ready, /live para orquestradores
7. **Graceful shutdown** — fechar conexões antes de morrer
8. **Logs estruturados** — JSON para ferramentas de observabilidade
