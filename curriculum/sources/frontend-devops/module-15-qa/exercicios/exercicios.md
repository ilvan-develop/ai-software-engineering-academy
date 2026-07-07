# Exercícios — Módulo 15

## Exercício 1: Escrevendo testes unitários

Escreva testes unitários para o serviço abaixo usando Jest.

```typescript
class ProductService {
  constructor(
    private repo: ProductRepository,
    private cache: CacheService,
  ) {}

  async create(dto: CreateProductDto): Promise<Product> {
    const existing = await this.repo.findBySku(dto.sku);
    if (existing) throw new ConflictException('SKU já existe');

    if (dto.price <= 0) throw new BadRequestException('Preço deve ser > 0');

    const product = Product.create(dto);
    await this.repo.save(product);
    await this.cache.invalidate('products:*');

    return product;
  }

  async findById(id: string): Promise<Product> {
    const cached = await this.cache.get(`product:${id}`);
    if (cached) return JSON.parse(cached);

    const product = await this.repo.findById(id);
    if (!product) throw new NotFoundException('Produto não encontrado');

    await this.cache.set(`product:${id}`, JSON.stringify(product), 300);
    return product;
  }
}
```yaml

Cubra:
- Criação com sucesso
- SKU duplicado → 409
- Preço inválido → 400
- Busca com cache hit
- Busca sem cache (cache miss)
- Produto não encontrado → 404

---

## Exercício 2: Testes de integração

Escreva testes de integração com Supertest para os endpoints abaixo:

```typescript
@Controller('products')
export class ProductController {
  @Post()
  async create(@Body() dto: CreateProductDto) { /* ... */ }

  @Get(':id')
  async findOne(@Param('id') id: string) { /* ... */ }

  @Get()
  async findAll(@Query('page') page: number) { /* ... */ }

  @Delete(':id')
  async remove(@Param('id') id: string) { /* ... */ }
}
```yaml

Cubra:
- POST /products com dados válidos → 201
- POST /products sem nome → 400
- GET /products/:id → 200
- GET /products/:id inexistente → 404
- GET /products?page=1 → 200 com paginação
- DELETE /products/:id → 204
- DELETE /products/:id inexistente → 404

---

## Exercício 3: Testes E2E com Playwright

Escreva testes E2E para o fluxo de **compra**:

1. Login com usuário existente
2. Navegar para listagem de produtos
3. Adicionar produto ao carrinho
4. Ver carrinho (verificar item e total)
5. Finalizar compra (checkout)
6. Ver confirmação do pedido

Inclua:
- Teste de fluxo feliz
- Teste de carrinho vazio
- Teste de login inválido

---

## Exercício 4: TDD na prática

Implemente a funcionalidade abaixo seguindo TDD (Red → Green → Refactor):

**Regra:** Um pedido não pode ter mais de 10 itens. Se ultrapassar, deve lançar erro.

```typescript
class OrderService {
  addItem(orderId: string, item: OrderItem): void {
    // Implementar seguindo TDD
  }
}
```yaml

Passos:
1. RED: Escreva o teste que espera o erro
2. GREEN: Implemente a validação
3. REFACTOR: Melhore o código

---

## Exercício 5: Pipeline de qualidade

Configure um pipeline de qualidade que inclua:

1. **Lint** — ESLint com regras strict
2. **Type check** — TypeScript strict mode
3. **Testes unitários** — com cobertura > 80%
4. **Testes de integração** — com banco real
5. **Testes E2E** — Playwright
6. **Auditoria de segurança** — npm audit
7. **Build** — verificar que compila

Crie o arquivo `.github/workflows/quality.yml` completo.

Inclua:
- Estratégia de cache para npm
- Service container para PostgreSQL
- Upload de relatório de cobertura
- Notificação em caso de falha
