# Módulo 11 — Exercícios

## Exercício 1: Server vs Client Component

Classifique cada componente abaixo como Server Component ou Client Component e justifique.

| Componente | Tipo | Justificativa |
|------------|------|---------------|
| Página de listagem de produtos (fetch do banco) | | |
| Botão "Adicionar ao carrinho" | | |
| Modal de confirmação | | |
| Footer com links estáticos | | |
| Formulário de cadastro com validação | | |
| Header com informações do usuário logado | | |
| Gráfico de vendas interativo | | |
| Tabela de dados com sort | | |

---

## Exercício 2: Implementando os 3 estados

Implemente um componente `UserList` que:

1. Busca dados do servidor
2. Mostra **loading** (skeleton de 3 linhas)
3. Mostra **error** (com botão de retry)
4. Mostra **empty state** (mensagem + CTA para criar)
5. Mostra a lista quando há dados

Use Server Components, Suspense e Error Boundary.

---

## Exercício 3: Server Action

Crie uma Server Action para criar um **produto** com:

```typescript
interface ProductInput {
  name: string;        // min 3, max 100
  price: number;       // > 0
  categoryId: string;  // UUID válido
  description: string; // min 10, max 1000
}
```

Inclua:
- Validação com Zod
- Tratamento de erro (campos inválidos)
- Revalidação do cache após criar
- Retorno de sucesso/erro tipado

---

## Exercício 4: Carrinho com Zustand

Implemente um carrinho de compras com Zustand:

```typescript
interface CartItem {
  id: string;
  name: string;
  price: number;
  quantity: number;
  image: string;
}
```

Funcionalidades:
- Adicionar item (se já existe, incrementar)
- Remover item
- Atualizar quantidade
- Calcular subtotal por item
- Calcular total geral
- Limpar carrinho
- Contagem de itens (badge no header)

---

## Exercício 5: Refatoração com Server Components

O código abaixo usa padrões antigos. Refatore usando Server Components e Server Actions.

```typescript
'use client';
import { useState, useEffect } from 'react';

export default function ProductsPage() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/products')
      .then(res => res.json())
      .then(data => { setProducts(data); setLoading(false); })
      .catch(err => { setError(err); setLoading(false); });
  }, []);

  if (loading) return <div>Carregando...</div>;
  if (error) return <div>Erro: {error.message}</div>;
  if (products.length === 0) return <div>Nenhum produto</div>;

  return (
    <div>
      <h1>Produtos</h1>
      <div className="grid">
        {products.map(p => (
          <div key={p.id}>
            <h2>{p.name}</h2>
            <p>R$ {p.price}</p>
            <button onClick={() => addToCart(p)}>Comprar</button>
          </div>
        ))}
      </div>
    </div>
  );
}
```

Refatore para:
- Server Component para listagem
- Client Component apenas para o botão de compra
- Suspense para loading
- Server Action para addToCart
