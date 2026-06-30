## Introducao

# Módulo 11 — Frontend: Interfaces Enterprise com Next.js
**Server Components, performance e acessibilidade.**
---

---
## 1. Next.js App Router — A Nova Forma de Pensar

O App Router do Next.js 13+ mudou fundamentalmente como construímos aplicações React.
### Server Components vs Client Components
Server Component (padrão):
┌────────────────────────────────────┐
│  Renderiza no servidor             │
│  Envia HTML para o cliente         │
│  Pode acessar banco, API, FS       │
│  Menos JavaScript no cliente       │

---
## 2. Data Fetching — Buscando Dados

### Server-side fetching (recomendado)
// app/page.tsx — Server Component
async function DashboardPage() {
// Fetch direto no servidor (sem useEffect!)
const stats = await getDashboardStats();
const recentOrders = await getRecentOrders();
return (
<div>

---
## 3. Loading, Error e Empty States

### Loading com Suspense
// app/products/page.tsx
import { Suspense } from 'react';
import { ProductsList } from './products-list';
import { ProductsSkeleton } from './products-skeleton';
export default function ProductsPage() {
return (
<div>

---
## 4. Formulários com Server Actions

// app/products/actions.ts
'use server';
import { z } from 'zod';
import { revalidatePath } from 'next/cache';
const ProductSchema = z.object({
name: z.string().min(3),
price: z.number().positive(),
description: z.string().min(10),

---
## 5. Gerenciamento de Estado

### Estado local (useState)
'use client';
function Filters() {
const [search, setSearch] = useState('');
const [category, setCategory] = useState('all');
const [sort, setSort] = useState<'asc' | 'desc'>('asc');
return (
<div>

---
## 6. TanStack Query — Cache de Servidor

'use client';
import { useQuery } from '@tanstack/react-query';
// hooks/use-products.ts
export function useProducts(filters: ProductFilters) {
return useQuery({
queryKey: ['products', filters],
queryFn: () => fetchProducts(filters),
staleTime: 1000 * 60, // 1 minuto

---
## 7. Acessibilidade (WCAG 2.1)

### Princípios
Perceptível:      Todo conteúdo deve ser percebível (alternativas para mídia)
Operável:         Toda interface deve ser operável (teclado, voz)
Compreensível:    Conteúdo e interface devem ser compreensíveis
Robusto:          Conteúdo deve funcionar em diferentes tecnologias
### Práticas essenciais
// ARIA labels em elementos interativos
<button aria-label="Fechar modal">

---
## 8. Responsividade com Tailwind

### Mobile-first
// Sempre comece com mobile, depois adicione breakpoints
<div className="
grid
grid-cols-1           /* mobile: 1 coluna */
sm:grid-cols-2        /* sm: 2 colunas */
lg:grid-cols-3        /* lg: 3 colunas */
xl:grid-cols-4        /* xl: 4 colunas */

---
## 9. Otimização de Performance

### Imagens
import Image from 'next/image';
// ✅ next/image otimiza automaticamente
<Image
src="/product.jpg"
alt="Produto"
width={400}
height={300}

---
