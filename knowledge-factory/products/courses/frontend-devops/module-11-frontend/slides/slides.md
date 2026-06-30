---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 11 — Frontend: Interfaces Enterprise com Next.js

## Módulo 11 - Frontend: Interfaces Enterprise com Next.js

---
## 1. Next.js App Router — A Nova Forma de Pensar

- O App Router do Next.js 13+ mudou fundamentalmente como construímos aplicações React.
- Server Component (padrão):
- ┌────────────────────────────────────┐
- │  Renderiza no servidor             │
- │  Envia HTML para o cliente         │

---
## 2. Data Fetching — Buscando Dados

- // app/page.tsx — Server Component
- async function DashboardPage() {
- // Fetch direto no servidor (sem useEffect!)
- const stats = await getDashboardStats();
- const recentOrders = await getRecentOrders();

---
## 3. Loading, Error e Empty States

- // app/products/page.tsx
- import { Suspense } from 'react';
- import { ProductsList } from './products-list';
- import { ProductsSkeleton } from './products-skeleton';
- export default function ProductsPage() {

---
## 4. Formulários com Server Actions

- // app/products/actions.ts
- 'use server';
- import { z } from 'zod';
- import { revalidatePath } from 'next/cache';
- const ProductSchema = z.object({
- name: z.string().min(3),

---
## 5. Gerenciamento de Estado

- 'use client';
- function Filters() {
- const [search, setSearch] = useState('');
- const [category, setCategory] = useState('all');
- const [sort, setSort] = useState<'asc' | 'desc'>('asc');

---
## 6. TanStack Query — Cache de Servidor

- 'use client';
- import { useQuery } from '@tanstack/react-query';
- // hooks/use-products.ts
- export function useProducts(filters: ProductFilters) {
- return useQuery({
- queryKey: ['products', filters],

---
## 7. Acessibilidade (WCAG 2.1)

- Perceptível:      Todo conteúdo deve ser percebível (alternativas para mídia)
- Operável:         Toda interface deve ser operável (teclado, voz)
- Compreensível:    Conteúdo e interface devem ser compreensíveis
- Robusto:          Conteúdo deve funcionar em diferentes tecnologias

---
## 8. Responsividade com Tailwind

- // Sempre comece com mobile, depois adicione breakpoints
- <div className="
- grid
- grid-cols-1           /* mobile: 1 coluna */
- sm:grid-cols-2        /* sm: 2 colunas */

---
## 9. Otimização de Performance

- import Image from 'next/image';
- // ✅ next/image otimiza automaticamente
- <Image
- src="/product.jpg"
- alt="Produto"

---
## Exemplo: text

```text
Server Component (padrão):
  ┌────────────────────────────────────┐
  │  Renderiza no servidor             │
  │  Envia HTML para o cliente         │
  │  Pode acessar banco, API, FS       │
  │  Menos JavaScript no cliente       │
  │  NÃO tem estado, effects, eventos  │
  └────────────────────────────────────┘

Client Component ("use client"):
  ┌────────────────────────────────────┐
  │  Renderiza no cliente              │
...
```

---
## Exemplo: typescript

```typescript
// ✅ Server Component (padrão)
async function ProductList() {
  const products = await prisma.product.findMany();
  return (
    <div>
      {products.map(p => <ProductCard key={p.id} product={p} />)}
    </div>
  );
}

// ✅ Client Component (só quando precisar de interação)
'use client';
...
```

---
## Recap

- 1. Next.js App Router — A Nova Forma de Pensar
- 2. Data Fetching — Buscando Dados
- 3. Loading, Error e Empty States
- 4. Formulários com Server Actions
- 5. Gerenciamento de Estado
- 6. TanStack Query — Cache de Servidor
- 7. Acessibilidade (WCAG 2.1)
- 8. Responsividade com Tailwind
- 9. Otimização de Performance

---
# Obrigado!

## Perguntas?
