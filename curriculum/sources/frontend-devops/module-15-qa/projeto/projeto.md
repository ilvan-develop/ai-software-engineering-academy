# Projeto Módulo 15 — Suíte de Testes para API de E-commerce

## Objetivo

Criar uma suíte completa de testes para a API de e-commerce do Módulo 10.

## Contexto

Você é o QA Engineer responsável por garantir a qualidade da API de e-commerce. A API tem:

- Produtos (CRUD)
- Categorias (CRUD)
- Carrinho (adicionar, remover, listar, checkout)
- Pedidos (criar, histórico, detalhe)
- Autenticação (login, refresh, logout)

## Entregáveis

### 1. Testes Unitários (Jest)

- **ProductService** — criar, buscar, validar SKU único, validar preço
- **CartService** — adicionar item (novo e existente), remover, calcular total, checkout
- **OrderService** — criar a partir do carrinho, validar limite de itens, validar carrinho vazio

### 2. Testes de Integração (Supertest)

- **POST /auth/login** — sucesso, credenciais inválidas, rate limit
- **POST /products** — criar, validação, SKU duplicado, autenticação
- **GET /products** — listar, paginação, cache
- **POST /cart/checkout** — carrinho com itens, carrinho vazio

### 3. Testes E2E (Playwright)

- **Login → Listar produtos → Adicionar ao carrinho → Checkout → Ver pedido**
- Tentar acessar rota protegida sem autenticação

### 4. Pipeline de Qualidade (GitHub Actions)

- Lint + typecheck
- Testes unitários com cobertura > 80%
- Testes de integração com banco PostgreSQL
- Relatório de cobertura como artefato

## Critérios de avaliação

- [ ] Testes unitários com mocks para todas as dependências
- [ ] Testes de integração com Supertest
- [ ] Testes E2E com Playwright
- [ ] Cobertura > 80% nos services
- [ ] Pipeline CI completo rodando os testes
- [ ] Testes independentes (podem rodar em qualquer ordem)
- [ ] Nenhum teste depende de outro
