# Exercícios — Capítulo 3: Desenvolvimento Backend

> **Progressão:** Fácil → Médio → Difícil  
> **Total:** 4 exercícios

---

## Exercício 1 — Fácil: Crie um Módulo NestJS

**Tema:** Módulos, Controllers e Providers no NestJS

Crie um módulo NestJS completo para a entidade `Product` com:
- `ProductModule` — módulo principal
- `ProductController` — rotas CRUD básicas (GET /products, GET /products/:id, POST /products)
- `ProductService` — lógica de negócio
- Utilize injeção de dependência corretamente

---

## Exercício 2 — Médio: Guard de Autenticação

**Tema:** Guards e Pipes no NestJS

Implemente um guard `JwtAuthGuard` que:
- Extrai o token JWT do header `Authorization: Bearer <token>`
- Valida o token usando uma secret key
- Injeta o payload decodificado no `request.user`
- Retorna 401 se o token for inválido ou ausente

```typescript
// Estrutura esperada
@Injectable()
export class JwtAuthGuard implements CanActivate {
  canActivate(context: ExecutionContext): boolean | Promise<boolean> {
    // implementação
  }
}
```

---

## Exercício 3 — Médio: Pipe de Validação Customizado

**Tema:** Pipes de transformação e validação

Crie um pipe `ParseCpfPipe` que:
- Recebe uma string de CPF (com ou sem máscara)
- Valida usando a lógica de dígitos verificadores
- Retorna o CPF apenas com números
- Lança `BadRequestException` se inválido

Use no controller:
```typescript
@Get(':cpf')
findByCpf(@Param('cpf', ParseCpfPipe) cpf: string) { /* ... */ }
```

---

## Exercício 4 — Difícil: Interceptor de Logging e Tracing

**Tema:** Interceptors e observabilidade

Implemente um interceptor que:
1. Gera um `traceId` único para cada requisição (UUID v4)
2. Loga no início: `[traceId] METHOD /path - INÍCIO`
3. Loga no final: `[traceId] METHOD /path - STATUS DURATIONms`
4. Injeta o `traceId` no header de resposta (`X-Trace-Id`)
5. Usa `cls-rtracer` ou `AsyncLocalStorage` para disponibilizar o traceId em qualquer camada

```typescript
@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    // implementação
  }
}
```
