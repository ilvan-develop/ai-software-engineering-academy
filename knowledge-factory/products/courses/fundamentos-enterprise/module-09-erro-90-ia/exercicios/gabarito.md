# Gabarito — Módulo 09 — O Erro de 90% ao Usar IA para Programar

---

## Exercício 1 — Critérios de Correção

**a)** Erro 2 (Prompts vagos sem contexto) — o prompt não especificava stack, então a IA chutou MongoDB.

**b)** Erro 1 (Confiar cegamente) + Erro 3 (Pular code review) — código não foi revisado nem testado.

**c)** Erro 2 (Prompts vagos) — faltou contexto sobre a stack (React + Chakra UI).

**d)** Erro 4 (Ignorar AGENTS.md) — sem configuração persistente, o agente não mantém consistência.

**e)** Erro 1 (Confiar cegamente) + Erro 5 (Primeira resposta como final) — `localStorage` é inseguro para JWT; o ideal seria httpOnly cookie.

---

## Exercício 2 — Exemplos de Resposta

**a)** "Crie uma função `validateEmail(email: string): boolean` em `src/utils/validation.ts` que use regex para validar formato de email. Retorne `true` se o formato for válido, `false` caso contrário. Inclua casos de teste para emails válidos e inválidos."

**b)** "Refatore a função `processOrder` em `src/services/orders.ts`: substitua `for` aninhado por `map`/`filter`, extraia a lógica de cálculo de desconto para uma função separada, e adicione tipagem TypeScript. Mantenha a mesma saída."

**c)** "Crie um teste unitário para a função `calculateTotal` em `src/utils/pricing.ts` usando Vitest. Cubra: valor normal, frete grátis (> R$ 100), cupom inválido, e lista vazia de itens. Use `describe` e `it` com nomes descritivos."

**d)** "Explique a query SQL abaixo linha por linha: o que cada cláusula faz, qual a ordem de execução no banco, e se há oportunidades de otimização de performance."

---

## Exercício 3 — Gabarito

| # | Problema | Erro relacionado | Gravidade |
|---|----------|------------------|-----------|
| 1 | **SQL injection**: string interpolation direta na query com `'${username}'` | Erro 3 (pular review) | Crítico |
| 2 | **Token fixo**: `token: '123456'` é hardcoded e idêntico para todos | Erro 1 (confiar cegamente) | Crítico |
| 3 | **Senha em texto puro**: comparando password diretamente no banco | Erro 1 (confiar) + Erro 5 (primeira resposta) | Crítico |
| 4 | **Sem validação de entrada**: `req.body` pode ter tipos inesperados | Erro 3 (pular review) | Alto |
| 5 | **Sem hash de senha**: bcrypt/argon2 deveriam ser usados | Erro 1 (confiar cegamente) | Alto |
| 6 | **Sem tratamento de erro em `db.query`**: `err` não é tratado | Erro 3 (pular review) | Médio |
| 7 | **Sem HTTPS nem headers de segurança**: falta helmet | Erro 5 (primeira resposta) | Médio |

---

## Exercício 4 — Exemplo de AGENTS.md

```markdown
# Agente: Projeto Next.js Enterprise

## Stack
- Next.js 14 (App Router) + TypeScript
- Prisma ORM + PostgreSQL
- Vitest (testes unitários) + Playwright (E2E)
- CSS Modules

## Estrutura
- `src/components/` — Componentes reutilizáveis
- `src/app/` — Páginas e layouts (App Router)
- `src/lib/` — Funções utilitárias e helpers
- `prisma/schema.prisma` — Schema do banco

## Regras de Código
1. Use arrow functions para componentes e funções
2. Prefira `const` sobre `let`; nunca use `var`
3. Nomes de arquivo em kebab-case
4. Componentes em PascalCase, funções em camelCase
5. CSS Modules: arquivo `*.module.css` no mesmo diretório

## Testes
6. Todo arquivo em `src/lib/` deve ter `*.test.ts` correspondente
7. Use `describe`/`it` com nomes descritivos em português
8. Mock Prisma com `vitest-mock-extended`

## Commits
9. Prefixo: feat/fix/refactor/test/docs
10. Mensagem em português, presente simples
11. Máximo 72 caracteres na primeira linha
```
