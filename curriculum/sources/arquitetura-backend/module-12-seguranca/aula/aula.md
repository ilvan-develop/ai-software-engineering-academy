# Módulo 12 — Segurança

**Protegendo sistemas Enterprise contra ameaças reais.**

---

## 1. Por que segurança é o requisito mais importante

Segurança não é uma feature — é um **pré-requisito**. Um sistema inseguro é um passivo, não um ativo.

### O custo de uma falha de segurança

```text
Falha de segurança típica:
  ┌──────────────────────────────────────────────┐
  │  Dados vazados                               │
  │  Multas regulatórias (LGPD: até 2% do fat.) │
  │  Perda de confiança dos clientes             │
  │  Custos de remediação (R$ 200k-2M médio)     │
  │  Tempo de inatividade                        │
  └──────────────────────────────────────────────┘

Custo de prevenir:
  ┌──────────────────────────────────────────────┐
  │  Treinamento do time: R$ 5k                  │
  │  Ferramentas de segurança: R$ 1k/mês         │
  │  Revisão de código: parte do processo        │
  └──────────────────────────────────────────────┘
```markdown

### Mindset de segurança

```text
❌ "Segurança é problema do DevOps"
❌ "Depois a gente adiciona segurança"
❌ "Ninguém vai atacar nosso sistema"

✅ "Segurança é responsabilidade de todos"
✅ "Segurança é parte da definição de 'pronto'"
✅ "Se tem valor, vai ser atacado"
```markdown

---

## 2. OWASP Top 10 (2021)

As 10 vulnerabilidades mais críticas em aplicações web.

### 1. Broken Access Control

> Usuário acessa recursos que não deveria.

```typescript
// ❌ Ruim: Não verifica se o recurso pertence ao usuário
@Get('/orders/:id')
async getOrder(@Param('id') id: string) {
  return this.orderRepo.findById(id);  // qualquer um vê qualquer pedido!
}

// ✅ Bom: Verifica propriedade
@Get('/orders/:id')
async getOrder(@Param('id') id: string, @Req() req) {
  const order = await this.orderRepo.findById(id);
  if (order.userId !== req.user.id) {
    throw new ForbiddenException();
  }
  return order;
}
```text

### 2. Cryptographic Failures

> Dados sensíveis expostos ou mal protegidos.

```typescript
// ❌ Ruim: Senha em texto puro
const user = await prisma.user.create({
  data: { password: req.body.password }  // 💥
});

// ✅ Bom: Hash com bcrypt
const hashedPassword = await bcrypt.hash(req.body.password, 12);
const user = await prisma.user.create({
  data: { password: hashedPassword }
});
```markdown

### 3. Injection

> SQL, NoSQL, OS command injection.

```typescript
// ❌ Ruim: Query concatenada (SQL injection!)
const users = await prisma.$queryRawUnsafe(
  `SELECT * FROM users WHERE email = '${email}'`
);

// ✅ Bom: Query parametrizada (Prisma previne injection)
const user = await prisma.user.findUnique({
  where: { email }
});
```text

### 4. Insecure Design

> Falhas no design que permitem ataques.

```typescript
// ❌ Ruim: Rate limit não implementado
@Post('/login')
async login(@Body() dto: LoginDto) {
  // Tentativas ilimitadas — brute force!
}

// ✅ Bom: Rate limit com throttling
@Throttle(5, 60) // 5 tentativas por minuto
@Post('/login')
async login(@Body() dto: LoginDto) {
  // ...
}
```markdown

### 5. Security Misconfiguration

> Configurações padrão inseguras.

```typescript
// ❌ Ruim: CORS aberto
app.enableCors();  // permite qualquer origem!

// ✅ Bom: CORS restrito
app.enableCors({
  origin: ['https://app.meusistema.com'],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
});
```text

### 6-10: Vulnerable Components, Auth Failures, Data Integrity, Logging, SSRF

| # | Vulnerabilidade | Prevenção |
|---|----------------|-----------|
| 6 | Vulnerable Components | npm audit, Dependabot, manter deps atualizadas |
| 7 | Identification/Auth Failures | JWT com expiração, MFA, session segura |
| 8 | Data Integrity Failures | Assinatura de dados, validação, CSP |
| 9 | Security Logging/Monitoring | Logs estruturados, alertas de segurança |
| 10 | SSRF | Validar URLs, restringir rede interna |

---

## 3. Autenticação com JWT

### Fluxo completo

```text
1. Usuário envia email + senha
2. Servidor valida credenciais
3. Servidor gera ACCESS TOKEN (15min) + REFRESH TOKEN (7d)
4. Cliente armazena e envia access token em requisições
5. Servidor valida token em cada requisição (AuthGuard)
6. Quando access token expira, cliente usa refresh token para obter novo
```markdown

### Implementação

```typescript
// auth.service.ts
@Injectable()
export class AuthService {
  constructor(
    private userRepo: UserRepository,
    private jwtService: JwtService,
  ) {}

  async login(dto: LoginDto): Promise<AuthTokens> {
    const user = await this.userRepo.findByEmail(dto.email);
    if (!user) throw new UnauthorizedException('Credenciais inválidas');

    const passwordValid = await bcrypt.compare(dto.password, user.password);
    if (!passwordValid) throw new UnauthorizedException('Credenciais inválidas');

    return this.generateTokens(user);
  }

  private async generateTokens(user: User): Promise<AuthTokens> {
    const payload = { sub: user.id, email: user.email, role: user.role };

    const accessToken = await this.jwtService.signAsync(payload, {
      expiresIn: '15m',
    });

    const refreshToken = await this.jwtService.signAsync(payload, {
      expiresIn: '7d',
      secret: process.env.JWT_REFRESH_SECRET,
    });

    // Armazenar refresh token (para revogação)
    await this.tokenRepo.save(user.id, refreshToken);

    return { accessToken, refreshToken };
  }

  async refresh(refreshToken: string): Promise<AuthTokens> {
    try {
      const payload = await this.jwtService.verifyAsync(refreshToken, {
        secret: process.env.JWT_REFRESH_SECRET,
      });

      // Verificar se token ainda é válido (não foi revogado)
      const stored = await this.tokenRepo.find(payload.sub, refreshToken);
      if (!stored) throw new UnauthorizedException('Token revogado');

      // Revogar token antigo (rotação)
      await this.tokenRepo.delete(payload.sub, refreshToken);

      const user = await this.userRepo.findById(payload.sub);
      return this.generateTokens(user);
    } catch {
      throw new UnauthorizedException('Refresh token inválido');
    }
  }

  async logout(userId: string): Promise<void> {
    await this.tokenRepo.deleteAll(userId);
  }
}

// jwt-auth.guard.ts
@Injectable()
export class JwtAuthGuard extends AuthGuard('jwt') {}

// jwt.strategy.ts
@Injectable()
export class JwtStrategy extends PassportStrategy(Strategy) {
  constructor() {
    super({
      jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
      secretOrKey: process.env.JWT_SECRET,
    });
  }

  async validate(payload: JwtPayload): Promise<User> {
    return { id: payload.sub, email: payload.email, role: payload.role };
  }
}
```markdown

---

## 4. Autorização com CASL (RBAC)

### Definição de abilities

```typescript
// abilities.ts
export type Action = 'manage' | 'create' | 'read' | 'update' | 'delete';
export type Subject = 'User' | 'Order' | 'Product' | 'Report' | 'all';

export function defineAbilitiesFor(user: User): PureAbility {
  return AbilityBuilder.define((can, cannot) => {
    // Admin pode fazer tudo
    if (user.role === 'admin') {
      can('manage', 'all');
      return;
    }

    // Usuário comum
    can('read', 'User', { id: user.id });       // só próprio perfil
    can('read', 'Order', { userId: user.id });  // só seus pedidos
    can('create', 'Order');                      // criar pedidos
    can('update', 'Order', { userId: user.id, status: 'pending' });

    // Gerente pode ver relatórios
    if (user.role === 'manager') {
      can('read', 'Report');
      can('read', 'User', { tenantId: user.tenantId });
    }

    // Ninguém pode deletar
    cannot('delete', 'all');
  });
}
```text

### Uso no controller

```typescript
@Post('/orders')
async create(@Body() dto: CreateOrderDto, @Req() req) {
  const ability = defineAbilitiesFor(req.user);
  ForbiddenError.from(ability).throwUnlessCan('create', 'Order');
  return this.orderService.create(dto, req.user.id);
}

@Delete('/orders/:id')
async delete(@Param('id') id: string, @Req() req) {
  const ability = defineAbilitiesFor(req.user);
  ForbiddenError.from(ability).throwUnlessCan('delete', 'Order');
  // Nunca chega aqui — admin também não pode deletar
}
```markdown

---

## 5. Rate Limiting

Protege contra brute force, DDoS e abuso.

### Implementação com @nestjs/throttler

```typescript
// app.module.ts
@Module({
  imports: [
    ThrottlerModule.forRoot([{
      ttl: 60000,      // 1 minuto
      limit: 60,        // 60 requisições por minuto (global)
    }]),
  ],
})

// Uso em endpoints específicos
@Throttle(5, 60)  // 5 tentativas por minuto
@Post('/login')
async login(@Body() dto: LoginDto) {
  // ...
}

@Throttle(3, 60)  // 3 tentativas por minuto
@Post('/password-reset')
async requestPasswordReset(@Body() dto: ResetDto) {
  // ...
}
```text

### Estratégias adicionais

```text
Rate Limiting por:
  IP:           limitar por endereço IP
  Usuário:      limitar por user ID
  Rota:         limites diferentes por endpoint
  Global:       limite total de requisições

Respostas:
  429 Too Many Requests
  Header: Retry-After: X segundos
```markdown

---

## 6. Headers de Segurança (Helmet + CSP)

### Helmet (NestJS)

```typescript
import helmet from 'helmet';

app.use(helmet());

// Configura automaticamente:
// Content-Security-Policy
// X-Content-Type-Options: nosniff
// X-Frame-Options: DENY
// X-XSS-Protection: 0
// Strict-Transport-Security
// Referrer-Policy
```markdown

### CSP (Content Security Policy)

```typescript
app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", "https://cdn.example.com"],
    styleSrc: ["'self'", "'unsafe-inline'"],
    imgSrc: ["'self'", "https://images.example.com", "data:"],
    connectSrc: ["'self'", "https://api.example.com"],
    fontSrc: ["'self'", "https://fonts.googleapis.com"],
    objectSrc: ["'none'"],
    upgradeInsecureRequests: [],
  },
}));
```text

---

## 7. Proteções Específicas

### SQL Injection

```typescript
// ❌ Nunca fazer
const users = await prisma.$queryRawUnsafe(`SELECT * FROM users WHERE email = '${email}'`);

// ✅ Prisma previne com query builders
const user = await prisma.user.findUnique({ where: { email } });

// ✅ Se precisar de raw query, usar parametrização
const users = await prisma.$queryRaw`SELECT * FROM users WHERE email = ${email}`;
```markdown

### XSS (Cross-Site Scripting)

```typescript
// ❌ Renderizar HTML sem sanitizar
<div dangerouslySetInnerHTML={{ __html: userComment }} />

// ✅ Sanitizar antes de renderizar
import DOMPurify from 'isomorphic-dompurify';
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userComment) }} />

// ✅ No backend, escapar output
const sanitized = escapeHtml(userComment);
```text

### CSRF (Cross-Site Request Forgery)

```typescript
// NestJS com CSRF protection
import * as csurf from 'csurf';

app.use(csurf({ cookie: true }));

// Enviar token CSRF em formulários/headers
// <meta name="csrf-token" content="{{csrfToken}}">
// Header: X-CSRF-Token
```markdown

---

## 8. Secrets Management

### O que NÃO fazer

```typescript
// ❌ Hardcoded no código
const API_KEY = 'sk-1234567890abcdef';
const DB_PASSWORD = 'minha-senha-super-secreta';

// ❌ No .env comitado
.env
DB_PASSWORD=minha-senha

// ❌ No código fonte
config.service.apiKey = 'sk-1234567890abcdef';
```text

### O que fazer

```bash
# ✅ .env.example (commitado, sem valores reais)
DATABASE_URL=postgresql://user:password@localhost:5432/db
JWT_SECRET=change-me
API_KEY=change-me

# ✅ .env (NÃO commitado, .gitignore)
DATABASE_URL=postgresql://user:senha-real@produção:5432/db
JWT_SECRET=minha-chave-jwt-segura
API_KEY=sk-real-key

# ✅ Validação na inicialização
# main.ts
const requiredEnvVars = ['DATABASE_URL', 'JWT_SECRET', 'API_KEY'];
for (const varName of requiredEnvVars) {
  if (!process.env[varName]) {
    throw new Error(`Variável de ambiente ${varName} não configurada`);
  }
}
```markdown

---

## 9. Auditoria de Segurança

### O que auditar

```typescript
// Log de ações sensíveis
@Injectable()
export class AuditService {
  async log(action: AuditAction): Promise<void> {
    await prisma.auditLog.create({
      data: {
        userId: action.userId,
        action: action.type,
        resource: action.resource,
        resourceId: action.resourceId,
        details: action.details,
        ip: action.ip,
        userAgent: action.userAgent,
        timestamp: new Date(),
      },
    });
  }
}

// Uso
@Post('/transfer')
async transfer(@Body() dto: TransferDto, @Req() req) {
  const result = await this.transferService.execute(dto);
  await this.auditService.log({
    userId: req.user.id,
    type: 'TRANSFER',
    resource: 'Account',
    resourceId: dto.fromAccountId,
    details: { to: dto.toAccountId, amount: dto.amount },
    ip: req.ip,
    userAgent: req.headers['user-agent'],
  });
  return result;
}
```text

### Checklist de segurança para code review

```text
Segurança em code review:
  [ ] Todos os inputs são validados?
  [ ] Autenticação em todas as rotas protegidas?
  [ ] Autorização verifica propriedade do recurso?
  [ ] Senhas com hash (bcrypt, não MD5/SHA1)?
  [ ] Sem segredos no código?
  [ ] Rate limiting nos endpoints críticos?
  [ ] CORS configurado (não * em produção)?
  [ ] SQL injection prevenido (ORM)?
  [ ] Headers de segurança configurados?
  [ ] Logs não expõem dados sensíveis?
