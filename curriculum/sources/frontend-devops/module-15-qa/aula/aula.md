# Módulo 15 — QA: Testes e Qualidade

**Código sem teste é legacy.**

---

## 1. Por que testar?

### O custo de não testar

```text
Sem testes:
  ┌────────────────────────────────────────────┐
  │  Bug em produção: 2 dias pra achar         │
  │  Correção: 1 hora                          │
  │  Regressão: 3 bugs novos (quebra outras    │
  │             funcionalidades)               │
  │  Confiança do time: baixa ("medo de mexer")│
  └────────────────────────────────────────────┘

Com testes:
  ┌────────────────────────────────────────────┐
  │  Bug em produção: 0 (teste pegou antes)    │
  │  Correção: 30 min (teste indica o local)   │
  │  Regressão: 0 (testes previnem)            │
  │  Confiança do time: alta ("posso refatorar")│
  └────────────────────────────────────────────┘
```markdown

### A pirâmide de testes

```text
          ╱╲
         ╱  ╲        E2E (Playwright)
        ╱    ╲       Testes de fluxo completo
       ╱────────╲
      ╱          ╲   Integration (Supertest)
     ╱            ╲  Testes de API + banco
    ╱────────────────╲
   ╱                  ╲ Unitários (Jest)
  ╱                    ╲ Testes de serviço/função
 ╱──────────────────────╲
  MUITOS (rápidos)         POUCOS (lentos)
```markdown

### Estratégia de cobertura

```text
Unitários:        70%+ cobertura (services, utils)
Integração:       20% (endpoints, fluxos críticos)
E2E:              10% (fluxos principais, felizes e infelizes)
```markdown

---

## 2. Testes Unitários com Jest

### Estrutura de um teste

```typescript
describe('UserService', () => {
  describe('create', () => {
    it('deve criar usuário com sucesso', async () => {
      // Arrange — preparar dados
      const dto: CreateUserDto = {
        name: 'João Silva',
        email: 'joao@email.com',
        password: 'Senha123',
      };

      // Act — executar
      const result = await service.create(dto);

      // Assert — verificar
      expect(result).toBeDefined();
      expect(result.name).toBe('João Silva');
      expect(result.email).toBe('joao@email.com');
    });

    it('deve lançar erro se email já existe', async () => {
      // Arrange
      repo.findByEmail.mockResolvedValue(existingUser);

      // Act + Assert
      await expect(
        service.create(mockDto)
      ).rejects.toThrow(ConflictException);
    });

    it('deve validar senha com bcrypt', async () => {
      const result = await service.create(mockDto);

      expect(bcrypt.hash).toHaveBeenCalledWith('Senha123', 12);
      expect(result.password).not.toBe('Senha123'); // hash != original
    });
  });
});
```text

### Mocks

```typescript
// Mock completo de um repository
const mockUserRepo = {
  findById: jest.fn(),
  findByEmail: jest.fn(),
  save: jest.fn(),
  findAll: jest.fn(),
  softDelete: jest.fn(),
};

// Mock com retorno específico
mockUserRepo.findById.mockResolvedValue({ id: '1', name: 'João' });
mockUserRepo.findById.mockRejectedValue(new Error('DB error'));
mockUserRepo.findById.mockResolvedValueOnce(user).mockResolvedValueOnce(null);

// Verificar chamadas
expect(mockUserRepo.save).toHaveBeenCalledTimes(1);
expect(mockUserRepo.save).toHaveBeenCalledWith(expect.objectContaining({
  name: 'João',
}));
```markdown

### Testando erros

```typescript
describe('quando o banco falha', () => {
  it('deve lançar erro genérico', async () => {
    repo.save.mockRejectedValue(new Error('Connection refused'));

    await expect(service.create(dto)).rejects.toThrow(
      'Erro interno do servidor'
    );
  });
});

describe('quando dados são inválidos', () => {
  it.each([
    { name: '', email: 'joao@email.com', password: '123' },
    { name: 'João', email: 'invalido', password: 'Senha123' },
    { name: 'João', email: 'joao@email.com', password: '123' },
  ])('deve rejeitar dados inválidos: %p', async (invalidDto) => {
    await expect(service.create(invalidDto)).rejects.toThrow(
      BadRequestException
    );
  });
});
```text

---

## 3. Testes de Integração com Supertest

```typescript
import * as request from 'supertest';
import { Test } from '@nestjs/testing';
import { INestApplication } from '@nestjs/common';

describe('UserController (integration)', () => {
  let app: INestApplication;

  beforeAll(async () => {
    const moduleRef = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();

    app = moduleRef.createNestApplication();
    await app.init();
  });

  afterAll(async () => {
    await app.close();
  });

  describe('POST /users', () => {
    it('deve criar usuário com dados válidos', async () => {
      const response = await request(app.getHttpServer())
        .post('/users')
        .send({
          name: 'João Silva',
          email: 'joao@email.com',
          password: 'Senha123',
        })
        .expect(201);

      expect(response.body).toHaveProperty('id');
      expect(response.body.name).toBe('João Silva');
    });

    it('deve retornar 400 com dados inválidos', async () => {
      await request(app.getHttpServer())
        .post('/users')
        .send({ name: '', email: 'invalido' })
        .expect(400);
    });

    it('deve retornar 409 se email já existe', async () => {
      // Primeiro cria
      await request(app.getHttpServer())
        .post('/users')
        .send(validDto)
        .expect(201);

      // Depois tenta criar de novo
      await request(app.getHttpServer())
        .post('/users')
        .send(validDto)
        .expect(409);
    });
  });

  describe('GET /users/:id', () => {
    it('deve retornar 404 para usuário inexistente', async () => {
      await request(app.getHttpServer())
        .get('/users/non-existent-id')
        .expect(404);
    });
  });
});
```markdown

---

## 4. Testes E2E com Playwright

### Configuração

```typescript
// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  retries: 1,
  workers: 3,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
});
```text

### Testes

```typescript
// e2e/login.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Fluxo de autenticação', () => {
  test('deve fazer login com sucesso', async ({ page }) => {
    await page.goto('/login');

    await page.fill('[name="email"]', 'admin@empresa.com');
    await page.fill('[name="password"]', 'Admin123');
    await page.click('button[type="submit"]');

    await expect(page).toHaveURL('/dashboard');
    await expect(page.locator('text=Bem-vindo, Admin')).toBeVisible();
  });

  test('deve mostrar erro com credenciais inválidas', async ({ page }) => {
    await page.goto('/login');

    await page.fill('[name="email"]', 'invalido@email.com');
    await page.fill('[name="password"]', 'senha-errada');
    await page.click('button[type="submit"]');

    await expect(page.locator('[role="alert"]')).toContainText(
      'Credenciais inválidas'
    );
  });

  test('deve redirecionar para login se não autenticado', async ({ page }) => {
    await page.goto('/dashboard');

    await expect(page).toHaveURL('/login');
  });
});

test.describe('CRUD de produtos', () => {
  test.beforeEach(async ({ page }) => {
    // Login antes de cada teste
    await page.goto('/login');
    await page.fill('[name="email"]', 'admin@empresa.com');
    await page.fill('[name="password"]', 'Admin123');
    await page.click('button[type="submit"]');
  });

  test('deve criar um novo produto', async ({ page }) => {
    await page.goto('/products/new');

    await page.fill('[name="name"]', 'Produto Teste');
    await page.fill('[name="price"]', '99.90');
    await page.fill('[name="description"]', 'Descrição do produto teste');

    await page.click('button[type="submit"]');

    // Verificar se foi redirecionado para lista
    await expect(page).toHaveURL('/products');
    await expect(page.locator('text=Produto Teste')).toBeVisible();
  });

  test('deve validar campos obrigatórios', async ({ page }) => {
    await page.goto('/products/new');
    await page.click('button[type="submit"]');

    // Verificar mensagens de erro
    await expect(page.locator('text=Nome é obrigatório')).toBeVisible();
    await expect(page.locator('text=Preço é obrigatório')).toBeVisible();
  });
});
```markdown

---

## 5. Cobertura de Código

### Configuração do Jest

```typescript
// jest.config.ts
export default {
  collectCoverageFrom: [
    'src/**/*.service.ts',
    'src/**/*.use-case.ts',
    'src/**/*.controller.ts',
    '!src/**/*.module.ts',
    '!src/main.ts',
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
};
```text

### O que cobrir

```text
✅ Services:     branches (if/else), funções, linhas
✅ Use Cases:    fluxos felizes e infelizes
✅ Controllers:  validação, autorização, respostas

❌ Módulos:      só declaram providers/imports
❌ Config:       valores estáticos
❌ DTOs:         schemas Zod (testados indiretamente)
```markdown

---

## 6. GitHub Actions com Testes

```yaml
name: CI

on: [push, pull_request]

jobs:
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

      - name: Lint
        run: npm run lint

      - name: Type check
        run: npm run typecheck

      - name: Unit tests
        run: npm run test -- --coverage

      - name: E2E tests
        run: npm run test:e2e

      - name: Upload coverage
        uses: actions/upload-artifact@v4
        with:
          name: coverage
          path: coverage/
```markdown

---

## 7. TDD — Test-Driven Development

### Ciclo TDD

```text
Red:   Escreva um teste que falha
Green: Faça o teste passar (código mínimo)
Refactor: Melhore o código mantendo os verdes
```markdown

### Exemplo prático

```typescript
// 1. RED — Escrever teste primeiro
describe('OrderService', () => {
  it('não deve criar pedido com valor abaixo do mínimo', () => {
    const items = [{ productId: '1', price: 5, quantity: 1 }]; // total: 5
    const MIN_ORDER_VALUE = 10;

    expect(() => service.create({ items })).toThrow(
      'Valor mínimo do pedido é R$ 10,00'
    );
  });
});

// 2. GREEN — Código mínimo para passar
class OrderService {
  create(input: CreateOrderInput): Order {
    const total = input.items.reduce((acc, i) => acc + i.price * i.quantity, 0);

    if (total < 10) {
      throw new Error('Valor mínimo do pedido é R$ 10,00');
    }

    return Order.create(input);
  }
}

// 3. REFACTOR — Melhorar sem quebrar testes
// Extrair constante, melhorar mensagem
