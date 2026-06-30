# Prompt: Criar Testes de API

Você é um QA Expert Agent.

Crie testes de API para o endpoint abaixo usando Jest + Supertest.

## Endpoint

- **Método:** [GET/POST/PUT/DELETE]
- **Rota:** /api/v1/[resource]
- **Autenticação:** [requer/não requer]
- **Permissões:** [roles necessárias]

## Cenários a cobrir

### Happy path
- [ ] Requisição válida retorna 200/201
- [ ] Body de resposta no formato esperado

### Error path
- [ ] Sem autenticação → 401
- [ ] Sem permissão → 403
- [ ] Dados inválidos → 400/422
- [ ] Recurso não encontrado → 404
- [ ] Conflito → 409

### Edge cases
- [ ] Paginação (se aplicável)
- [ ] Filtros (se aplicável)
- [ ] Dados maliciosos (injection)

## Estrutura

```typescript
describe('[Recurso] - [Operação]', () => {
  describe('Happy path', () => {
    it('deve retornar 201 ao criar recurso válido', async () => {
      // Arrange, Act, Assert
    });
  });

  describe('Error path', () => {
    it('deve retornar 401 sem token', async () => {
      // ...
    });
  });
});
```
