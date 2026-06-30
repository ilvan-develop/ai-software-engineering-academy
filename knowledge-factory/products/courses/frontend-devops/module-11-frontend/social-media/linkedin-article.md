# Módulo 11 - Frontend: Interfaces Enterprise com Next.js

---

## 1. Next.js App Router — A Nova Forma de Pensar

O App Router do Next.js 13+ mudou fundamentalmente como construímos aplicações React.
### Server Components vs Client Components
Server Component (padrão):
┌────────────────────────────────────┐

## 2. Data Fetching — Buscando Dados

### Server-side fetching (recomendado)
// app/page.tsx — Server Component
async function DashboardPage() {
// Fetch direto no servidor (sem useEffect!)

## 3. Loading, Error e Empty States

### Loading com Suspense
// app/products/page.tsx
import { Suspense } from 'react';
import { ProductsList } from './products-list';

## 4. Formulários com Server Actions

// app/products/actions.ts
'use server';
import { z } from 'zod';
import { revalidatePath } from 'next/cache';

## 5. Gerenciamento de Estado

### Estado local (useState)
'use client';
function Filters() {
const [search, setSearch] = useState('');

## 6. TanStack Query — Cache de Servidor

'use client';
import { useQuery } from '@tanstack/react-query';
// hooks/use-products.ts
export function useProducts(filters: ProductFilters) {

---
*Este artigo faz parte da formacao Arquitetura de Software Enterprise com IA*