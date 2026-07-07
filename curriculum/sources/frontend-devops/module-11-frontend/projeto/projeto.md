# Projeto Módulo 11 — Dashboard Administrativo

## Objetivo

Criar um dashboard administrativo completo usando Next.js App Router, Server Components e Server Actions.

## Especificação

### Funcionalidades

1. **Dashboard** — cards com métricas (total users, orders, revenue)
2. **Lista de Usuários** — tabela com paginação, busca e filtros
3. **CRUD de Produtos** — formulário com Server Actions
4. **Gerenciamento de Pedidos** — lista com status e ações

### Requisitos técnicos

- Server Components para listagens
- Client Components apenas para interatividade (botões, formulários)
- Server Actions para mutations
- TanStack Query para cache de dados do cliente
- Zustand para estado global (carrinho)
- Loading states com Suspense
- Error boundaries
- Empty states
- Acessibilidade (ARIA labels, keyboard nav)
- Responsivo (mobile-first com Tailwind)

### Estrutura

```text
app/
├── layout.tsx
├── page.tsx                    (Dashboard)
├── loading.tsx
├── error.tsx
├── users/
│   ├── page.tsx                (Lista)
│   └── [id]/
│       └── page.tsx            (Detalhe)
├── products/
│   ├── page.tsx                (Lista)
│   ├── new/
│   │   └── page.tsx            (Criar)
│   └── [id]/
│       ├── page.tsx            (Editar)
│       └── delete/
│           └── page.tsx        (Confirmar deleção)
├── orders/
│   ├── page.tsx                (Lista)
│   └── [id]/
│       └── page.tsx            (Detalhe)
└── actions/
    ├── products.ts
    ├── users.ts
    └── orders.ts
```markdown

### Entregáveis

1. **Todas as páginas** com Server Components
2. **Server Actions** para criar, atualizar, deletar
3. **Loading states** com skeletons
4. **Error boundaries** customizados
5. **Empty states** para listas vazias
6. **Acessibilidade** em todos os componentes interativos
7. **Responsividade** (mobile + tablet + desktop)

## Critérios de avaliação

- [ ] Server Component por padrão (mínimo de `'use client'`)
- [ ] Server Actions para todas as mutations
- [ ] Loading, Error e Empty states em todas as listas
- [ ] Acessibilidade (aria-label, roles, keyboard)
- [ ] Responsivo (testar em 3 breakpoints)
- [ ] Formulários com validação client + server
- [ ] Código limpo e organizado
