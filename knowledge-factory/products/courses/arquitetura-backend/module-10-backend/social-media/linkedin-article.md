# Módulo 10 - Backend: APIs Enterprise com NestJS

---

## 1. Por que NestJS?

NestJS é o framework Node.js mais adequado para sistemas Enterprise.
### Comparação
| Característica | Express | Fastify | NestJS |
|---------------|---------|---------|--------|

## 2. Estrutura de módulos

### Organização por domínio
src/
├── modules/
│   ├── users/

## 3. Controllers, Services, Repositories

### Camadas
Controller (Rota)
↓ chamada
Service (Lógica de negócio)

## 4. DTOs e Validação com Zod

### DTOs (Data Transfer Objects)
import { z } from 'zod';
export const CreateUserSchema = z.object({
name: z.string().min(3).max(100),

## 5. Tratamento de Erros

### Exception Filters
@Catch()
export class GlobalExceptionFilter implements ExceptionFilter {
catch(exception: unknown, host: ArgumentsHost) {

## 6. Interceptors e Guards

### Interceptors (transformação de resposta)
@Injectable()
export class TransformInterceptor<T> implements NestInterceptor<T, ApiResponse<T>> {
intercept(context: ExecutionContext, next: CallHandler): Observable<ApiResponse<T>> {

---
*Este artigo faz parte da formacao Arquitetura de Software Enterprise com IA*