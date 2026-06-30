# Módulo 10 — Exercícios

## Exercício 1: Estrutura de módulo

Crie a estrutura completa do módulo `products` seguindo o padrão apresentado:

- Controller (CRUD)
- Service (com validação)
- Repository (Prisma)
- DTOs (CreateProductDto, UpdateProductDto, ProductResponse)
- Entity (Product)

**Regras de negócio:**
- SKU deve ser único
- Preço deve ser > 0
- Nome deve ter entre 3 e 100 caracteres
- Soft delete

---

## Exercício 2: Validação com Zod

Implemente a validação para o endpoint de criação de pedido:

```typescript
interface CreateOrderInput {
  customerId: string;        // UUID válido
  items: Array<{
    productId: string;       // UUID válido
    quantity: number;        // >= 1
    unitPrice: number;       // > 0
  }>;
  discount?: number;         // 0-100 (percentual)
  notes?: string;            // max 500 caracteres
}
```

Crie o schema Zod e o pipe de validação.

---

## Exercício 3: Exception Filter

Implemente um Exception Filter que trata os seguintes erros:

1. `DomainError` → 400 com código do erro
2. `Prisma.PrismaClientKnownRequestError` → traduzir para erros HTTP (P2002 = 409, P2025 = 404)
3. `ValidationError` (Zod) → 422 com campos inválidos
4. Qualquer outro → 500 (logar e não expor stack)

---

## Exercício 4: Paginação

Implemente um endpoint `GET /products` com paginação cursor-based.

```typescript
@Get()
async findAll(
  @Query('cursor') cursor?: string,
  @Query('limit', ParseIntPipe) limit: number = 10,
) {
  // Implementar
}
```

Inclua:
- Filtro por categoria (query param `category`)
- Ordenação por preço (query param `sort`: 'asc' | 'desc')
- Cache de 1 minuto

---

## Exercício 5: Refatoração

O código abaixo tem múltiplos problemas. Refatore seguindo os padrões do módulo.

```typescript
@Controller('/api')
export class ApiController {
  constructor(private prisma: PrismaService) {}

  @Post('/save-user')
  async saveUser(@Body() body: any) {
    const user = await this.prisma.user.findUnique({ where: { email: body.email } });
    if (user) return { error: 'exists' };

    const created = await this.prisma.user.create({
      data: { name: body.name, email: body.email, password: body.password }
    });

    return { id: created.id, name: created.name, email: created.email };
  }

  @Get('/get-users')
  async getUsers() {
    const users = await this.prisma.user.findMany();
    return { users };
  }

  @Delete('/remove-user/:id')
  async removeUser(@Param('id') id: string) {
    await this.prisma.user.delete({ where: { id } });
    return { success: true };
  }
}
```

Problemas a corrigir:
- Nomes de rotas inconsistentes
- `any` no body
- Senha em texto puro
- Sem validação
- Sem tratamento de erro
- Delete físico (não soft delete)
- Resposta inconsistente
