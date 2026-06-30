# Roteiro de Videoaula — Módulo 11 — Frontend: Interfaces Enterprise com Next.js

**Duracao total estimada:** 34 minutos
**Formato:** Videoaula gravada / Streaming
**Publico-alvo:** Desenvolvedores intermediarios

---

## Visao Geral do Video

| Item | Detalhe |
|------|---------|
| Titulo | Módulo 11 — Frontend: Interfaces Enterprise com Next.js |
| Duracao | 34 min |
| Cenas | 13 |
| Formato | Expositivo com demonstracao pratica |
| Nivel | Intermediario |

---

## Roteiro por Cena

### Cena 1 — INTRO

**Duracao:** 1:30

**Narracao:**
> Ola! Nesta aula vamos explorar: Módulo 11 — Frontend: Interfaces Enterprise com Next.js. Ao final, voce vai entender os conceitos fundamentais e como aplica-los na pratica. Vamos la?

**Visuais:**
- Tela de abertura com titulo do modulo. Animacao suave com o nome do curso.

**Texto na tela:**
```
[TITULO] Módulo 11 — Frontend: Interfaces Enterprise com Next.js
```

**Notas de direcao:**
- Tom energico e convidativo. Apresentar o problema que sera resolvido.

---

### Cena 2 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 1. Next.js App Router — A Nova Forma de Pensar. O App Router do Next.js 13+ mudou fundamentalmente como construímos aplicações React. Server Component (padrão): ┌────────────────────────────────────┐ │  Renderiza no servidor             │

**Visuais:**
- Slides com topicos-chave. ```text
Perceptível:      Todo conteúdo deve ser percebível (alternativas para mídia)
Operável:         Toda interface deve ser operável (teclado, voz)
Compreensível:    Conteúdo e interface devem ser compreensíveis
Robusto:          Conteúdo deve funcionar em diferentes tecnologias
```

**Texto na tela:**
```
[1. Next.js App Router — A Nova Forma de Pensar]
```

**Notas de direcao:**
- Secao 2 de 10. Usar exemplos praticos.

---

### Cena 3 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 2. Data Fetching — Buscando Dados. // app/page.tsx — Server Component async function DashboardPage() { // Fetch direto no servidor (sem useEffect!) const stats = await getDashboardStats();

**Visuais:**
- Slides com topicos-chave. ```text
Perceptível:      Todo conteúdo deve ser percebível (alternativas para mídia)
Operável:         Toda interface deve ser operável (teclado, voz)
Compreensível:    Conteúdo e interface devem ser compreensíveis
Robusto:          Conteúdo deve funcionar em diferentes tecnologias
```

**Texto na tela:**
```
[2. Data Fetching — Buscando Dados]
```

**Notas de direcao:**
- Secao 3 de 10. Usar exemplos praticos.

---

### Cena 4 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 3. Loading, Error e Empty States. // app/products/page.tsx import { Suspense } from 'react'; import { ProductsList } from './products-list'; import { ProductsSkeleton } from './products-skeleton';

**Visuais:**
- Slides com topicos-chave. ```text
Perceptível:      Todo conteúdo deve ser percebível (alternativas para mídia)
Operável:         Toda interface deve ser operável (teclado, voz)
Compreensível:    Conteúdo e interface devem ser compreensíveis
Robusto:          Conteúdo deve funcionar em diferentes tecnologias
```

**Texto na tela:**
```
[3. Loading, Error e Empty States]
```

**Notas de direcao:**
- Secao 4 de 10. Usar exemplos praticos.

---

### Cena 5 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 4. Formulários com Server Actions. // app/products/actions.ts 'use server'; import { z } from 'zod'; import { revalidatePath } from 'next/cache';

**Visuais:**
- Slides com topicos-chave. ```text
Perceptível:      Todo conteúdo deve ser percebível (alternativas para mídia)
Operável:         Toda interface deve ser operável (teclado, voz)
Compreensível:    Conteúdo e interface devem ser compreensíveis
Robusto:          Conteúdo deve funcionar em diferentes tecnologias
```

**Texto na tela:**
```
[4. Formulários com Server Actions]
```

**Notas de direcao:**
- Secao 5 de 10. Usar exemplos praticos.

---

### Cena 6 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 5. Gerenciamento de Estado. 'use client'; function Filters() { const [search, setSearch] = useState(''); const [category, setCategory] = useState('all');

**Visuais:**
- Slides com topicos-chave. ```text
Perceptível:      Todo conteúdo deve ser percebível (alternativas para mídia)
Operável:         Toda interface deve ser operável (teclado, voz)
Compreensível:    Conteúdo e interface devem ser compreensíveis
Robusto:          Conteúdo deve funcionar em diferentes tecnologias
```

**Texto na tela:**
```
[5. Gerenciamento de Estado]
```

**Notas de direcao:**
- Secao 6 de 10. Usar exemplos praticos.

---

### Cena 7 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 6. TanStack Query — Cache de Servidor. 'use client'; import { useQuery } from '@tanstack/react-query'; // hooks/use-products.ts export function useProducts(filters: ProductFilters) {

**Visuais:**
- Slides com topicos-chave. ```text
Perceptível:      Todo conteúdo deve ser percebível (alternativas para mídia)
Operável:         Toda interface deve ser operável (teclado, voz)
Compreensível:    Conteúdo e interface devem ser compreensíveis
Robusto:          Conteúdo deve funcionar em diferentes tecnologias
```

**Texto na tela:**
```
[6. TanStack Query — Cache de Servidor]
```

**Notas de direcao:**
- Secao 7 de 10. Usar exemplos praticos.

---

### Cena 8 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 7. Acessibilidade (WCAG 2.1). Perceptível:      Todo conteúdo deve ser percebível (alternativas para mídia) Operável:         Toda interface deve ser operável (teclado, voz) Compreensível:    Conteúdo e interface devem ser compreensíveis Robusto:          Conteúdo deve funcionar em diferentes tecnologias

**Visuais:**
- Slides com topicos-chave. ```text
Perceptível:      Todo conteúdo deve ser percebível (alternativas para mídia)
Operável:         Toda interface deve ser operável (teclado, voz)
Compreensível:    Conteúdo e interface devem ser compreensíveis
Robusto:          Conteúdo deve funcionar em diferentes tecnologias
```

**Texto na tela:**
```
[7. Acessibilidade (WCAG 2.1)]
```

**Notas de direcao:**
- Secao 8 de 10. Usar exemplos praticos.

---

### Cena 9 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 8. Responsividade com Tailwind. // Sempre comece com mobile, depois adicione breakpoints <div className=" grid grid-cols-1           /* mobile: 1 coluna */

**Visuais:**
- Slides com topicos-chave. ```text
Perceptível:      Todo conteúdo deve ser percebível (alternativas para mídia)
Operável:         Toda interface deve ser operável (teclado, voz)
Compreensível:    Conteúdo e interface devem ser compreensíveis
Robusto:          Conteúdo deve funcionar em diferentes tecnologias
```

**Texto na tela:**
```
[8. Responsividade com Tailwind]
```

**Notas de direcao:**
- Secao 9 de 10. Usar exemplos praticos.

---

### Cena 10 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 9. Otimização de Performance. import Image from 'next/image'; // ✅ next/image otimiza automaticamente <Image src="/product.jpg"

**Visuais:**
- Slides com topicos-chave. ```text
Perceptível:      Todo conteúdo deve ser percebível (alternativas para mídia)
Operável:         Toda interface deve ser operável (teclado, voz)
Compreensível:    Conteúdo e interface devem ser compreensíveis
Robusto:          Conteúdo deve funcionar em diferentes tecnologias
```

**Texto na tela:**
```
[9. Otimização de Performance]
```

**Notas de direcao:**
- Secao 10 de 10. Usar exemplos praticos.

---

### Cena 11 — CODE-DEMO

**Duracao:** 4:00

**Narracao:**
> Vamos ver na pratica como isso funciona. Observe este codigo em text:

**Visuais:**
- Tela dividida: editor de codigo a esquerda, terminal/output a direita.

**Texto na tela:**
```
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
```
```

**Notas de direcao:**
- Explicar linha por linha. Destacar pontos importantes com zoom ou realce.

---

### Cena 12 — SUMMARY

**Duracao:** 1:30

**Narracao:**
> Recapitulando: vimos 1. Next.js App Router — A Nova Forma de Pensar, 2. Data Fetching — Buscando Dados, 3. Loading, Error e Empty States, 4. Formulários com Server Actions, 5. Gerenciamento de Estado, 6. TanStack Query — Cache de Servidor. Esses conceitos sao fundamentais para sua formacao.

**Visuais:**
- Lista resumida com icones. Transicao suave para encerramento.

**Texto na tela:**
```
✓ 1. Next.js App Router — A Nova Forma de Pensar
✓ 2. Data Fetching — Buscando Dados
✓ 3. Loading, Error e Empty States
✓ 4. Formulários com Server Actions
✓ 5. Gerenciamento de Estado
✓ 6. TanStack Query — Cache de Servidor
```

**Notas de direcao:**
- Reforcar os aprendizados principais. Conectar com o proximo modulo.

---

### Cena 13 — OUTRO

**Duracao:** 0:30

**Narracao:**
> Na proxima aula, vamos aprofundar esses conceitos. Nao perca!

**Visuais:**
- Tela final com links, inscricao, e teaser da proxima aula.

**Texto na tela:**
```
Proximo modulo: [TITULO DO PROXIMO MODULO]
```

**Notas de direcao:**
- Chamada para acao: inscrever-se, comentar, compartilhar.

---

## Checklist de Producao

- [ ] Roteiro revisado
- [ ] Slides preparados
- [ ] Ambiente de codigo configurado
- [ ] Microfone testado
- [ ] Gravacao de tela configurada (1920x1080)
- [ ] Exemplos de codigo testados
- [ ] Legendas geradas
- [ ] Thumbnail criada
- [ ] Descricao e tags preenchidas
- [ ] Capitulos do video marcados

---

## Sugestoes de Thumbnail

- Texto: 'Módulo 11 '
- Cor de fundo: azul escuro (#1a2332)
- Destaque: codigo ou diagrama ao fundo
- Rosto do apresentador no canto inferior direito

---

## SEO

**Titulo:** Módulo 11 — Frontend: Interfaces Enterprise com Next.js | Arquitetura Enterprise
**Descricao:** Aprenda módulo 11 — frontend: interfaces enterprise com next.js. Nesta aula abordamos conceitos fundamentais com exemplos praticos em TypeScript.
**Tags:** arquitetura, software, enterprise, typescript, desenvolvimento
