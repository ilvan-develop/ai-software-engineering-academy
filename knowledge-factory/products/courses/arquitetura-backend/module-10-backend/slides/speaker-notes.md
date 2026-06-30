## Introducao

# Módulo 10 — Backend: APIs Enterprise com NestJS
**Construindo backends robustos, testáveis e seguros.**
---

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

---
## 2. Estrutura de módulos

### Organização por domínio
src/
├── modules/
│   ├── users/
│   │   ├── user.module.ts
│   │   ├── user.controller.ts
│   │   ├── user.service.ts
│   │   ├── user.repository.ts

---
## 3. Controllers, Services, Repositories

### Camadas
Controller (Rota)
↓ chamada
Service (Lógica de negócio)
↓ chamada
Repository (Persistência)
↓
Database (Prisma)

---
## 4. DTOs e Validação com Zod

### DTOs (Data Transfer Objects)
import { z } from 'zod';
export const CreateUserSchema = z.object({
name: z.string().min(3).max(100),
email: z.string().email(),
password: z.string().min(8).regex(
/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/,
'Senha deve conter maiúscula, minúscula e número'

---
## 5. Tratamento de Erros

### Exception Filters
@Catch()
export class GlobalExceptionFilter implements ExceptionFilter {
catch(exception: unknown, host: ArgumentsHost) {
const ctx = host.switchToHttp();
const response = ctx.getResponse<Response>();
if (exception instanceof DomainError) {
return response.status(400).json({

---
## 6. Interceptors e Guards

### Interceptors (transformação de resposta)
@Injectable()
export class TransformInterceptor<T> implements NestInterceptor<T, ApiResponse<T>> {
intercept(context: ExecutionContext, next: CallHandler): Observable<ApiResponse<T>> {
return next.handle().pipe(
map(data => ({
success: true,
data,

---
## 7. Paginação, Filtros e Ordenação

### Paginação cursor-based (recomendada para scale)
interface CursorPaginationInput {
cursor?: string;  // ID do último item
limit: number;    // Itens por página
}
interface CursorPaginatedResult<T> {
items: T[];
nextCursor: string | null;

---
## 8. Cache com Redis

### Cache de respostas
@Injectable()
export class CacheService {
constructor(private readonly redis: Redis) {}
async getOrSet<T>(key: string, ttl: number, fetcher: () => Promise<T>): Promise<T> {
const cached = await this.redis.get(key);
if (cached) return JSON.parse(cached);
const data = await fetcher();

---
## 9. Health Checks

@Controller('health')
export class HealthController {
constructor(
private prisma: PrismaService,
private redis: RedisService,
) {}
@Get()
async check() {

---
## 10. Testes

// Teste de service
describe('UserService', () => {
let service: UserService;
let repo: jest.Mocked<UserRepository>;
let emailService: jest.Mocked<EmailService>;
beforeEach(async () => {
repo = { findById: jest.fn(), save: jest.fn() } as any;
emailService = { sendWelcome: jest.fn() } as any;

---
