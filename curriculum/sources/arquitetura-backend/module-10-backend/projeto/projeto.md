# Projeto Módulo 10 — API de E-commerce

## Objetivo

Implementar uma API REST completa para um e-commerce usando NestJS + Prisma + PostgreSQL.

## Especificação

### Funcionalidades

1. **Produtos** — CRUD com cache e paginação cursor-based
2. **Categorias** — CRUD básico
3. **Carrinho** — adicionar/remover itens, calcular total
4. **Pedidos** — criar a partir do carrinho, consultar histórico
5. **Autenticação** — JWT com refresh token
6. **Autorização** — admin gerencia produtos, usuário faz pedidos

### Entregáveis

### 1. Estrutura de pastas

```
src/
├── modules/
│   ├── products/
│   ├── categories/
│   ├── cart/
│   ├── orders/
│   └── auth/
├── common/
└── main.ts
```

### 2. Schema Prisma

Modele as entidades: User, Product, Category, Cart, CartItem, Order, OrderItem

### 3. Módulo de Produtos (completo)

- Controller com CRUD + paginação cursor-based + cache Redis
- Service com validação e regras de negócio
- Repository com Prisma
- DTOs com Zod

### 4. Módulo de Carrinho

- Adicionar item (se já existe, incrementar quantidade)
- Remover item
- Listar itens com subtotal
- Calcular total
- ``Checkout`` → converte em pedido

### 5. Módulo de Pedidos

- Criar pedido a partir do carrinho (limpar carrinho após)
- Histórico de pedidos do usuário
- Detalhe do pedido com itens

### 6. Testes

- Testes unitários do service de Products
- Testes do service de Cart (criar, adicionar, checkout)

## Critérios de avaliação

- [ ] Estrutura de pastas segue Clean Architecture
- [ ] Validação com Zod em todos os endpoints
- [ ] Tratamento de erros com Exception Filter
- [ ] Paginação cursor-based em Products
- [ ] Autenticação JWT em rotas protegidas
- [ ] Cache Redis em Products
- [ ] Testes unitários dos services
- [ ] Soft delete em Products
