# Módulo 10 — Slides

---

## Slide 1: Título

**Backend Enterprise com NestJS**
APIs robustas, testáveis e seguras

---

## Slide 2: Por que NestJS?

| Característica | Express | NestJS |
|---------------|---------|--------|
| Arquitetura | Livre | Modular + DI |
| TypeScript | Opcional | Nativo (decorators) |
| Segurança | Manual | Guards + Interceptors |
| Swagger | Manual | Nativo |
| Testabilidade | Média | Alta |

---

## Slide 3: Estrutura de módulos

```text
src/
├── modules/
│   ├── users/        (controller, service, repository, dto)
│   ├── orders/
│   └── payments/
├── common/           (guards, pipes, filters)
├── config/
└── main.ts
```markdown

Cada módulo é autocontido e testável

---

## Slide 4: Camadas

```text
Controller (rota) → DTO (validação)
    ↓
Service (lógica de negócio)
    ↓
Repository (persistência)
    ↓
Prisma (banco)
```markdown

Cada camada tem responsabilidade única

---

## Slide 5: Validação com Zod

```typescript
const CreateUserSchema = z.object({
  name: z.string().min(3),
  email: z.string().email(),
  password: z.string().min(8)
    .regex(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/),
});

// Valida + transforma
email: z.string().email().transform(v => v.toLowerCase())
```markdown

---

## Slide 6: Exception Filters

```text
Erro de Domínio:    400 + código (EMAIL_ALREADY_EXISTS)
Erro HTTP:          status + mensagem
Erro não mapeado:   500 + log (não expõe stack)
```text

```typescript
@Catch()
export class GlobalExceptionFilter {
  catch(exception, host) {
    if (exception instanceof DomainError) { /* 400 + código */ }
    if (exception instanceof HttpException) { /* status + msg */ }
    // 500 genérico
  }
}
```markdown

---

## Slide 7: Paginação

| Offset (ruim para scale) | Cursor (bom para scale) |
|--------------------------|------------------------|
| SELECT ... OFFSET 1000   | WHERE id > 'abc' |
| Lento em grandes datasets | Rápido, consistente |
| Dados duplicados se inseridos | Sem duplicação |

---

## Slide 8: Cache com Redis

```typescript
async getOrSet<T>(key, ttl, fetcher) {
  const cached = await redis.get(key);
  if (cached) return JSON.parse(cached);

  const data = await fetcher();
  await redis.set(key, JSON.stringify(data), 'EX', ttl);
  return data;
}
```markdown

Cache + Invalidação por padrão

---

## Slide 9: Health Checks

```css
GET /health

{
  status: 'healthy', // ou 'degraded'
  checks: [
    { name: 'database', status: 'healthy' },
    { name: 'redis', status: 'healthy' },
  ]
}
```markdown

---

## Slide 10: Testes com DI

```typescript
const repo = { findById: jest.fn(), save: jest.fn() };
const service = new UserService(repo, emailService);

// Testar service sem banco real
await service.create(dto);
expect(repo.save).toHaveBeenCalled();
```markdown

DI torna testes isolados e rápidos

---

## Slide 11: Anti-padrões

- **Controller gordo** — lógica de negócio no controller
- **Service anêmico** — service só repassa para repository
- **DTO genérico** — mesma classe para request/response/entity
- **Tratamento de erro genérico** — try/catch vazio
- **Query N+1** — buscar itens em loop

---

## Slide 12: Para refletir

> "Um bom backend não é aquele que funciona. É aquele que **continua funcionando** sob carga, com dados inconsistentes, com falhas de rede."

> "Controllers são finos. Services são profundos. Repositories são abstratos."
