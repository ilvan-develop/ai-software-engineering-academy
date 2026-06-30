# Módulo 15 — Slides

---

## Slide 1: Título

**QA: Testes e Qualidade**
Código sem teste é legacy

---

## Slide 2: O custo de não testar

```
Sem testes:               Com testes:
Bug em prod: 2 dias       Bug: 0 (teste pegou)
Correção: 1 hora          Correção: 30 min
Regressão: 3 bugs         Regressão: 0
Confiança: baixa          Confiança: alta
```

**Teste não é custo. É investimento.**

---

## Slide 3: Pirâmide de testes

```
      ╱╲
     ╱  ╲     E2E (Playwright) — poucos, lentos
    ╱────────╲
   ╱          ╲   Integration (Supertest)
  ╱────────────────╲
 ╱                  ╲  Unitários (Jest) — muitos, rápidos
╱──────────────────────╲
```

70% unitários, 20% integração, 10% E2E

---

## Slide 4: Jest — Estrutura

```typescript
describe('UserService', () => {
  describe('create', () => {
    it('deve criar com sucesso', async () => {
      // Arrange
      // Act
      // Assert
      expect(result.name).toBe('João');
    });

    it('deve lançar erro se email existe', async () => {
      repo.findByEmail.mockResolvedValue(user);
      await expect(service.create(dto)).rejects.toThrow();
    });
  });
});
```

---

## Slide 5: Mocks

```typescript
// Mock completo
const repo = {
  findById: jest.fn(),
  save: jest.fn(),
};

// Retornos
repo.findById.mockResolvedValue(user);
repo.save.mockRejectedValue(new Error('DB error'));

// Verificações
expect(repo.save).toHaveBeenCalledTimes(1);
expect(repo.save).toHaveBeenCalledWith(
  expect.objectContaining({ name: 'João' })
);
```

---

## Slide 6: Supertest — Testes de API

```typescript
request(app.getHttpServer())
  .post('/users')
  .send(validDto)
  .expect(201)
  .expect(res => {
    expect(res.body).toHaveProperty('id');
  });
```

Testa controller + validação + service + banco

---

## Slide 7: Playwright — E2E

```typescript
test('deve criar produto', async ({ page }) => {
  await page.goto('/login');
  await page.fill('[name="email"]', 'admin@email.com');
  await page.click('button[type="submit"]');

  await page.goto('/products/new');
  await page.fill('[name="name"]', 'Produto X');
  await page.click('button[type="submit"]');

  await expect(page.locator('text=Produto X')).toBeVisible();
});
```

---

## Slide 8: Cobertura

```typescript
coverageThreshold: {
  global: {
    branches: 80,
    functions: 80,
    lines: 80,
    statements: 80,
  },
}
```

**Mínimo 80%** — pipeline quebra se abaixo

---

## Slide 9: CI com Testes

```
Todo push:
  npm run lint
  npm run typecheck
  npm run test          (unitários + cobertura)
  npm run test:e2e      (integração)
  npm run test:playwright (E2E)
```

Se algum falhar: ❌ pipeline vermelho = não merge

---

## Slide 10: TDD — Red/Green/Refactor

```
1. RED:     Escrever teste que falha
2. GREEN:   Código mínimo para passar
3. REFACTOR: Melhorar código mantendo testes verdes

Benefício: código nasce testado
```

---

## Slide 11: Anti-padrões

- **Teste que testa implementação** — teste comportamento, não método
- **Mock de tudo** — só mock o que é externo (banco, API)
- **Teste frágil** — quebra com qualquer mudança de layout
- **Cobertura alta mas testes ruins** — qualidade > quantidade
- **Sem testes de integração** — unitários não pegam bugs de contrato
- **Testes lentos** — > 5 min fazem dev não rodar

---

## Slide 12: Para refletir

> "Código sem teste é legacy no dia em que é escrito."

> "Testes não são sobre evitar bugs. São sobre **ter confiança para mudar**."
