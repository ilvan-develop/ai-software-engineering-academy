# Módulo 11 — Slides

---

## Slide 1: Título

**Frontend Enterprise com Next.js**
Server Components, performance e acessibilidade

---

## Slide 2: Server vs Client Components

```
Server Component (padrão):
  ✅ Renderiza no servidor
  ✅ Acessa banco/API direto
  ✅ Menos JS no cliente
  ❌ Sem useState/useEffect

Client Component ("use client"):
  ❌ Mais JS no cliente
  ✅ Interatividade
  ✅ useState, useEffect, eventos

Regra: Server por padrão, Client só quando precisar
```

---

## Slide 3: Data Fetching

```typescript
// ✅ Server Component — fetch direto
async function ProductsPage() {
  const products = await prisma.product.findMany();
  return <ProductList products={products} />;
}
```

- Sem `useEffect`
- Sem estado de loading
- Cache automático
- Revalidação por tempo ou sob demanda

---

## Slide 4: Os 3 estados de todo componente

```
1. Loading (Suspense)
   ┌──────────────────────┐
   │  [Skeleton loading]  │
   └──────────────────────┘

2. Error (error.tsx)
   ┌──────────────────────┐
   │  Algo deu errado     │
   │  [Tentar novamente]  │
   └──────────────────────┘

3. Empty
   ┌──────────────────────┐
   │  Nenhum resultado    │
   │  [Adicionar]         │
   └──────────────────────┘
```

---

## Slide 5: Server Actions

```typescript
'use server';
export async function createProduct(formData: FormData) {
  const data = Object.fromEntries(formData);
  const result = ProductSchema.safeParse(data);
  if (!result.success) return { error: ... };

  await prisma.product.create({ data: result.data });
  revalidatePath('/products');
}
```

Sem API Route, sem fetch, tipagem automática

---

## Slide 6: Estado Global com Zustand

```typescript
const useCartStore = create<CartStore>((set, get) => ({
  items: [],
  addItem: (item) => set(state => ({
    items: [...state.items, item]
  })),
  total: () => get().items.reduce(...),
}));
```

Simples, tipado, sem boilerplate

---

## Slide 7: Acessibilidade — WCAG 2.1

```
Perceptível:  aria-label em ícones
Operável:     navegação por teclado
Compreensível: labels em formulários
Robusto:      role="alert" em mensagens
```

```typescript
<button aria-label="Fechar">
  <XIcon />
</button>
<label htmlFor="email">Email</label>
```

---

## Slide 8: Responsividade Mobile-first

```
grid grid-cols-1        Mobile: 1 coluna
  sm:grid-cols-2        Tablet: 2 colunas
  lg:grid-cols-3        Desktop: 3 colunas
  xl:grid-cols-4        Wide: 4 colunas
```

Sidebar vira drawer:
- Mobile: fixed + -translate-x-full
- Desktop: static + translate-x-0

---

## Slide 9: Performance

```
Imagens:    next/image (WebP, lazy, blur placeholder)
Fontes:     next/font (swap, auto-otimizada)
Código:     dynamic import (só carrega quando precisa)
Cache:      staleTime no TanStack Query
```

---

## Slide 10: Estrutura do projeto

```
app/
├── layout.tsx          (Root Layout)
├── page.tsx            (Home)
├── loading.tsx         (Loading global)
├── error.tsx           (Error global)
├── products/
│   ├── page.tsx        (Lista)
│   ├── loading.tsx     (Skeleton)
│   ├── [id]/
│   │   └── page.tsx    (Detalhe)
│   └── new/
│       └── page.tsx    (Formulário)
└── actions/
    └── products.ts     (Server Actions)
```

---

## Slide 11: Anti-padrões

- **Tudo Client Component** — perde benefícios de SSR
- **useEffect para fetch** — prefira Server Component
- **Ignorar acessibilidade** — botão sem aria-label
- **Sem loading state** — tela branca enquanto carrega
- **Imagens sem otimização** — next/image é obrigatório
- **CSS global** — Tailwind + CSS Modules

---

## Slide 12: Para refletir

> "Um bom frontend não é bonito. É **rápido, acessível e confiável**."

> "Server Components não são uma feature. São uma **mudança de paradigma** — menos JavaScript, mais HTML."
