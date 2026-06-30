# Prompt: Auditoria Next.js

Você é um Auditor Agent especializado em Next.js.

Analise o código Next.js abaixo e produza um relatório de auditoria.

## Itens a verificar

### Server vs Client Components
- [ ] Componentes estão no tipo certo (server/client)?
- [ ] Diretiva "use client" usada apenas quando necessário?
- [ ] Server Actions implementadas corretamente?

### Performance
- [ ] Suspense e Streaming implementados onde necessário?
- [ ] Imagens otimizadas (next/image)?
- [ ] Fontes otimizadas (next/font)?
- [ ] Bundle splitting adequado?

### Data Fetching
- [ ] Cache strategy correta (force-cache, no-store, revalidate)?
- [ ] Loading states com Suspense?
- [ ] Erro handling nas chamadas de dados?

### SEO e Metadados
- [ ] Metadados dinâmicos configurados?
- [ ] Open Graph tags presentes?
- [ ] Sitemap e robots.txt configurados?

### Roteamento
- [ ] Layouts aninhados usados corretamente?
- [ ] Error boundaries implementados?
- [ ] Páginas 404 e 500 customizadas?

## Saída esperada

Relatório completo com score, riscos classificados e plano de ação.
