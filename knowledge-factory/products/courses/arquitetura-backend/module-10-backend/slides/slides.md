---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 10 — Backend: APIs Enterprise com NestJS

## Módulo 10 - Backend: APIs Enterprise com NestJS

---
## 1. Por que NestJS?

- NestJS é o framework Node.js mais adequado para sistemas Enterprise.
- | Característica | Express | Fastify | NestJS |
- |---------------|---------|---------|--------|
- | Arquitetura | Livre | Livre | Modular (módulos, controllers, providers) |
- | DI (Injeção de Dependência) | Manual | Manual | Nativo + suporte a decorators |

---
## 2. Estrutura de módulos

- src/
- ├── modules/
- │   ├── users/
- │   │   ├── user.module.ts
- │   │   ├── user.controller.ts

---
## 3. Controllers, Services, Repositories

- Controller (Rota)
- ↓ chamada
- Service (Lógica de negócio)
- ↓ chamada
- Repository (Persistência)

---
## 4. DTOs e Validação com Zod

- import { z } from 'zod';
- export const CreateUserSchema = z.object({
- name: z.string().min(3).max(100),
- email: z.string().email(),
- password: z.string().min(8).regex(

---
## 5. Tratamento de Erros

- @Catch()
- export class GlobalExceptionFilter implements ExceptionFilter {
- catch(exception: unknown, host: ArgumentsHost) {
- const ctx = host.switchToHttp();
- const response = ctx.getResponse<Response>();

---
## 6. Interceptors e Guards

- @Injectable()
- export class TransformInterceptor<T> implements NestInterceptor<T, ApiResponse<T>> {
- intercept(context: ExecutionContext, next: CallHandler): Observable<ApiResponse<T>> {
- return next.handle().pipe(
- map(data => ({

---
## 7. Paginação, Filtros e Ordenação

- interface CursorPaginationInput {
- cursor?: string;  // ID do último item
- limit: number;    // Itens por página
- }
- interface CursorPaginatedResult<T> {

---
## 8. Cache com Redis

- @Injectable()
- export class CacheService {
- constructor(private readonly redis: Redis) {}
- async getOrSet<T>(key: string, ttl: number, fetcher: () => Promise<T>): Promise<T> {
- const cached = await this.redis.get(key);

---
## 9. Health Checks

- @Controller('health')
- export class HealthController {
- constructor(
- private prisma: PrismaService,
- private redis: RedisService,
- ) {}

---
## 10. Testes

- // Teste de service
- describe('UserService', () => {
- let service: UserService;
- let repo: jest.Mocked<UserRepository>;
- let emailService: jest.Mocked<EmailService>;
- beforeEach(async () => {

---
## Exemplo: typescript

```typescript
@Module({
  imports: [PrismaModule, HttpModule],
  controllers: [UserController],
  providers: [UserService, UserRepository, JwtStrategy],
  exports: [UserService],
})
export class UserModule {}
```

---
## Exemplo: text

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
...
```

---
## Recap

- 1. Por que NestJS?
- 2. Estrutura de módulos
- 3. Controllers, Services, Repositories
- 4. DTOs e Validação com Zod
- 5. Tratamento de Erros
- 6. Interceptors e Guards
- 7. Paginação, Filtros e Ordenação
- 8. Cache com Redis
- 9. Health Checks
- 10. Testes

---
# Obrigado!

## Perguntas?
