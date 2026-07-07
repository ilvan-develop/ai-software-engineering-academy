# Módulo 10 — Backend: APIs Enterprise com NestJS

**Construindo backends robustos, testáveis e seguros.**

---

## 1. Por que NestJS?

NestJS é o framework Node.js mais adequado para sistemas Enterprise.

### Comparação

| Característica | Express | Fastify | NestJS |
|---------------|---------|---------|--------|
| Arquitetura | Livre | Livre | Modular (módulos, controllers, providers) |
| DI (Injeção de Dependência) | Manual | Manual | Nativo + suporte a decorators |
| TypeScript | Opcional | Opcional | Nativo (decorators, metadados) |
| Guards/Interceptors | Manual | Manual | Nativo (auth, validação, transformação) |
| OpenAPI/Swagger | Manual | Manual | Nativo (@nestjs/swagger) |
| Testabilidade | Média | Média | Alta (DI + módulos testáveis) |
| Ecossistema Enterprise | Baixo | Baixo | Alto (Guard, Interceptor, Pipe, Filter) |

### Módulo NestJS típico

```typescript
@Module({
  imports: [PrismaModule, HttpModule],
  controllers: [UserController],
  providers: [UserService, UserRepository, JwtStrategy],
  exports: [UserService],
})
export class UserModule {}
```text

![Arquitetura de Referencia Backend](/knowledge-factory/products/courses/arquitetura-backend/module-10-backend/assets/diagram-arquitetura-backend.svg)

---

## 2. Estrutura de módulos

### Organização por domínio

```text
src/
├── modules/
│   ├── users/
│   │   ├── user.module.ts
│   │   ├── user.controller.ts
│   │   ├── user.service.ts
│   │   ├── user.repository.ts
│   │   ├── dto/
│   │   │   ├── create-user.dto.ts
│   │   │   └── update-user.dto.ts
│   │   └── entities/
│   │       └── user.entity.ts
│   ├── orders/
│   │   └── ...
│   └── payments/
│       └── ...
├── common/
│   ├── guards/
│   ├── interceptors/
│   ├── pipes/
│   └── filters/
├── config/
│   └── app.config.ts
└── main.ts
```markdown

### Por que essa estrutura?

```text
Separação por domínio:
  → Tudo relacionado a "users" está junto
  → Fácil de navegar e manter
  → Cada módulo é autocontido
  
Módulo raiz (AppModule):
  → Importa os módulos de domínio
  → Tempo de inicialização mais rápido
  → Testes mais isolados
```markdown

---

## 3. Controllers, Services, Repositories

### Camadas

```text
Controller (Rota)
  ↓ chamada
Service (Lógica de negócio)
  ↓ chamada
Repository (Persistência)
  ↓
Database (Prisma)
```markdown

### Controller

```typescript
@Controller('users')
@UseGuards(JwtAuthGuard)
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Post()
  @ApiOperation({ summary: 'Criar usuário' })
  @ApiResponse({ status: 201, type: UserResponse })
  async create(@Body() dto: CreateUserDto) {
    return this.userService.create(dto);
  }

  @Get(':id')
  async findOne(@Param('id', ParseUUIDPipe) id: string) {
    return this.userService.findById(id);
  }

  @Get()
  async findAll(
    @Query('page', ParseIntPipe) page: number = 1,
    @Query('limit', ParseIntPipe) limit: number = 10,
  ) {
    return this.userService.findAll({ page, limit });
  }

  @Patch(':id')
  async update(
    @Param('id', ParseUUIDPipe) id: string,
    @Body() dto: UpdateUserDto,
  ) {
    return this.userService.update(id, dto);
  }

  @Delete(':id')
  @HttpCode(HttpStatus.NO_CONTENT)
  async remove(@Param('id', ParseUUIDPipe) id: string) {
    await this.userService.softDelete(id);
  }
}
```markdown

### Service

```typescript
@Injectable()
export class UserService {
  constructor(
    private readonly userRepo: UserRepository,
    private readonly emailService: EmailService,
  ) {}

  async create(dto: CreateUserDto): Promise<UserResponse> {
    const email = new Email(dto.email);

    const exists = await this.userRepo.findByEmail(email.toString());
    if (exists) throw new ConflictException('Email já cadastrado');

    const hashedPassword = await bcrypt.hash(dto.password, 12);
    const user = User.create({
      name: dto.name,
      email: email,
      password: hashedPassword,
    });

    await this.userRepo.save(user);
    await this.emailService.sendWelcome(user.email.toString());

    return UserResponse.from(user);
  }

  async findById(id: string): Promise<UserResponse> {
    const user = await this.userRepo.findById(id);
    if (!user) throw new NotFoundException('Usuário não encontrado');
    return UserResponse.from(user);
  }

  async findAll(pagination: PaginationInput): Promise<PaginatedResult<UserResponse>> {
    return this.userRepo.findAll(pagination);
  }
}
```text

### Repository

```typescript
@Injectable()
export class UserRepository {
  constructor(private readonly prisma: PrismaService) {}

  async findById(id: string): Promise<User | null> {
    const raw = await this.prisma.user.findUnique({ where: { id } });
    return raw ? this.toDomain(raw) : null;
  }

  async findByEmail(email: string): Promise<User | null> {
    const raw = await this.prisma.user.findUnique({ where: { email } });
    return raw ? this.toDomain(raw) : null;
  }

  async findAll(pagination: PaginationInput): Promise<PaginatedResult<User>> {
    const [items, total] = await Promise.all([
      this.prisma.user.findMany({
        skip: (pagination.page - 1) * pagination.limit,
        take: pagination.limit,
        orderBy: { createdAt: 'desc' },
      }),
      this.prisma.user.count(),
    ]);

    return {
      items: items.map(this.toDomain),
      total,
      page: pagination.page,
      limit: pagination.limit,
    };
  }

  async save(user: User): Promise<void> {
    await this.prisma.user.create({ data: this.toPersistence(user) });
  }

  async update(id: string, user: User): Promise<void> {
    await this.prisma.user.update({
      where: { id },
      data: this.toPersistence(user),
    });
  }

  async softDelete(id: string): Promise<void> {
    await this.prisma.user.update({
      where: { id },
      data: { deletedAt: new Date() },
    });
  }

  private toDomain(raw: PrismaUser): User {
    return User.restore(
      raw.id,
      raw.name,
      Email.restore(raw.email),
      raw.password,
      raw.role as UserRole,
    );
  }

  private toPersistence(user: User): PrismaUserCreateInput {
    return {
      id: user.id,
      name: user.name,
      email: user.email.toString(),
      password: user.password,
      role: user.role,
    };
  }
}
```markdown

---

## 4. DTOs e Validação com Zod

### DTOs (Data Transfer Objects)

```typescript
import { z } from 'zod';

export const CreateUserSchema = z.object({
  name: z.string().min(3).max(100),
  email: z.string().email(),
  password: z.string().min(8).regex(
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/,
    'Senha deve conter maiúscula, minúscula e número'
  ),
  role: z.enum(['admin', 'manager', 'user']).default('user'),
});

export type CreateUserDto = z.infer<typeof CreateUserSchema>;

export class CreateUserPipe implements PipeTransform {
  transform(value: unknown) {
    const result = CreateUserSchema.safeParse(value);
    if (!result.success) {
      throw new BadRequestException({
        message: 'Dados inválidos',
        errors: result.error.flatten().fieldErrors,
      });
    }
    return result.data;
  }
}
```text

### Uso no controller

```typescript
@Post()
async create(@Body(new CreateUserPipe()) dto: CreateUserDto) {
  return this.userService.create(dto);
}
```markdown

### Validação vs Sanitização

```typescript
// Validação: rejeitar dados inválidos
password: z.string().min(8)

// Sanitização: transformar dados
email: z.string().email().transform(v => v.toLowerCase()),
name: z.string().trim().min(3),
```text

---

## 5. Tratamento de Erros

### Exception Filters

```typescript
@Catch()
export class GlobalExceptionFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost) {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse<Response>();

    if (exception instanceof DomainError) {
      return response.status(400).json({
        statusCode: 400,
        error: exception.code,
        message: exception.message,
      });
    }

    if (exception instanceof HttpException) {
      return response.status(exception.getStatus()).json({
        statusCode: exception.getStatus(),
        error: exception.name,
        message: exception.message,
      });
    }

    // Erro não mapeado — log e retorno genérico
    console.error('Erro não tratado:', exception);
    return response.status(500).json({
      statusCode: 500,
      error: 'Internal Server Error',
      message: 'Erro interno do servidor',
    });
  }
}
```markdown

### Domain Errors

```typescript
export abstract class DomainError extends Error {
  abstract readonly code: string;
}

export class EmailAlreadyExistsError extends DomainError {
  readonly code = 'EMAIL_ALREADY_EXISTS';
  constructor() { super('Email já cadastrado'); }
}

export class InsufficientBalanceError extends DomainError {
  readonly code = 'INSUFFICIENT_BALANCE';
  constructor() { super('Saldo insuficiente'); }
}

export class InvalidEmailError extends DomainError {
  readonly code = 'INVALID_EMAIL';
  constructor() { super('Formato de email inválido'); }
}
```text

---

## 6. Interceptors e Guards

### Interceptors (transformação de resposta)

```typescript
@Injectable()
export class TransformInterceptor<T> implements NestInterceptor<T, ApiResponse<T>> {
  intercept(context: ExecutionContext, next: CallHandler): Observable<ApiResponse<T>> {
    return next.handle().pipe(
      map(data => ({
        success: true,
        data,
        timestamp: new Date().toISOString(),
      })),
    );
  }
}

// Uso global
app.useGlobalInterceptors(new TransformInterceptor());
```markdown

### Guards (proteção de rotas)

```typescript
@Injectable()
export class RolesGuard implements CanActivate {
  constructor(private readonly requiredRoles: string[]) {}

  canActivate(context: ExecutionContext): boolean {
    const request = context.switchToHttp().getRequest();
    const user = request.user;

    if (!user) return false;
    return this.requiredRoles.includes(user.role);
  }
}

// Uso no controller
@Delete(':id')
@UseGuards(new RolesGuard(['admin']))
async remove(@Param('id') id: string) {
  return this.userService.softDelete(id);
}
```text

---

## 7. Paginação, Filtros e Ordenação

### Paginação cursor-based (recomendada para scale)

```typescript
interface CursorPaginationInput {
  cursor?: string;  // ID do último item
  limit: number;    // Itens por página
}

interface CursorPaginatedResult<T> {
  items: T[];
  nextCursor: string | null;
  hasMore: boolean;
}

// Implementação
async findAll(input: CursorPaginationInput): Promise<CursorPaginatedResult<User>> {
  const items = await this.prisma.user.findMany({
    take: input.limit + 1,  // Pega um a mais para saber se tem próxima
    cursor: input.cursor ? { id: input.cursor } : undefined,
    orderBy: { createdAt: 'desc' },
  });

  const hasMore = items.length > input.limit;
  if (hasMore) items.pop();

  return {
    items: items.map(this.toDomain),
    nextCursor: hasMore ? items[items.length - 1].id : null,
    hasMore,
  };
}
```markdown

---

## 8. Cache com Redis

### Cache de respostas

```typescript
@Injectable()
export class CacheService {
  constructor(private readonly redis: Redis) {}

  async getOrSet<T>(key: string, ttl: number, fetcher: () => Promise<T>): Promise<T> {
    const cached = await this.redis.get(key);
    if (cached) return JSON.parse(cached);

    const data = await fetcher();
    await this.redis.set(key, JSON.stringify(data), 'EX', ttl);
    return data;
  }

  async invalidate(pattern: string): Promise<void> {
    const keys = await this.redis.keys(pattern);
    if (keys.length > 0) await this.redis.del(keys);
  }
}

// Uso
async findById(id: string): Promise<UserResponse> {
  return this.cacheService.getOrSet(
    `user:${id}`,
    300, // 5 minutos
    () => this.fetchUser(id),
  );
}
```text

---

## 9. Health Checks

```typescript
@Controller('health')
export class HealthController {
  constructor(
    private prisma: PrismaService,
    private redis: RedisService,
  ) {}

  @Get()
  async check() {
    const checks = await Promise.all([
      this.checkDatabase(),
      this.checkRedis(),
    ]);

    const allHealthy = checks.every(c => c.status === 'healthy');

    return {
      status: allHealthy ? 'healthy' : 'degraded',
      timestamp: new Date().toISOString(),
      checks,
    };
  }

  private async checkDatabase() {
    try {
      await this.prisma.$queryRaw`SELECT 1`;
      return { name: 'database', status: 'healthy' };
    } catch {
      return { name: 'database', status: 'unhealthy' };
    }
  }

  private async checkRedis() {
    try {
      await this.redis.ping();
      return { name: 'redis', status: 'healthy' };
    } catch {
      return { name: 'redis', status: 'unhealthy' };
    }
  }
}
```markdown

---

## 10. Testes

```typescript
// Teste de service
describe('UserService', () => {
  let service: UserService;
  let repo: jest.Mocked<UserRepository>;
  let emailService: jest.Mocked<EmailService>;

  beforeEach(async () => {
    repo = { findById: jest.fn(), save: jest.fn() } as any;
    emailService = { sendWelcome: jest.fn() } as any;
    service = new UserService(repo, emailService);
  });

  describe('create', () => {
    it('deve criar usuário com sucesso', async () => {
      const dto = { name: 'João', email: 'joao@email.com', password: 'Senha123' };
      repo.findByEmail.mockResolvedValue(null);

      const result = await service.create(dto);

      expect(repo.save).toHaveBeenCalled();
      expect(emailService.sendWelcome).toHaveBeenCalled();
      expect(result).toBeDefined();
    });

    it('deve lançar erro se email já existe', async () => {
      repo.findByEmail.mockResolvedValue(createUser());

      await expect(service.create(mockDto)).rejects.toThrow(ConflictException);
    });
  });
});
