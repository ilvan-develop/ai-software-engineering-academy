# Projeto Módulo 07 — Design System Interno

## Objetivo

Criar um **Design System mínimo** para uma empresa fictícia, contendo tokens, componentes, documentação e estratégia de consumo. O projeto simula o desafio real de construir um DS do zero para atender múltiplos produtos.

## Contexto

A **FintechPay** é uma empresa de pagamentos que cresceu de 1 para 4 produtos em 2 anos:

1. **FintechPay App** — app mobile de pagamentos (React Native)
2. **FintechPay Dashboard** — painel web para lojistas (React + TypeScript)
3. **FintechPay Admin** — sistema interno de administração (React + TypeScript)
4. **FintechPay Onboarding** — portal de cadastro de novos clientes (Next.js)

Atualmente, cada produto tem seu próprio design e componentes. O CTO identificou que:
- 30% do tempo dos devs é gasto recriando os mesmos componentes
- Existem 4 implementações diferentes de botão, cada uma com props diferentes
- O onboarding de novos devs leva 3 semanas
- A marca está inconsistente entre os produtos

Sua missão: **criar a base do Design System da FintechPay**.

## Entregáveis

### 1. Tokens de Design

Defina os tokens seguindo o padrão de cores, tipografia, spacing, border-radius e shadows.

```typescript
// tokens/colors.ts — Defina a paleta da FintechPay (cor primária: roxo/violeta)
export const colors = {
  brand: {
    primary: {
      50: '...',
      100: '...',
      // ... até 950
    },
    secondary: {
      // ...
    },
  },
  semantic: {
    success: '...',
    warning: '...',
    error: '...',
    info: '...',
  },
  neutral: {
    white: '#ffffff',
    50: '...',
    // ... até 950
    black: '#000000',
  },
};

// tokens/typography.ts — Defina a type scale (ao menos 6 níveis)
// tokens/spacing.ts — Defina a escala de spacing (base 8px, ao menos 10 valores)
// tokens/effects.ts — Defina shadows e border-radius
```

### 2. Componentes

Implemente **3 componentes** completos com TypeScript:

#### 2.1. Button
- Variantes: `primary`, `secondary`, `outline`, `ghost`, `danger`
- Tamanhos: `sm`, `md`, `lg`
- Estados: default, hover, focus, disabled, loading
- Props: `leftIcon`, `rightIcon`, `fullWidth`, `loading`, `disabled`

#### 2.2. Input
- Com label, error, hint
- Prefixo/sufixo (ícone ou texto)
- Estados: default, focus, disabled, error

#### 2.3. Modal (ou Dialog)
- Overlay com backdrop
- Fechamento por esc + clique fora
- Tamanhos: `sm`, `md`, `lg`
- Footer com actions
- Acessível (role="dialog", aria-modal, focus trap)

### 3. Documentação (Storybook)

Para cada componente, crie **stories** do Storybook:

```typescript
// Button.stories.ts
// - Pelo menos 6 stories cobrindo variantes e estados
// - Autodocs habilitado
// - Controls para props principais

// Input.stories.ts
// - Pelo menos 4 stories (default, com erro, com prefixo, disabled)

// Modal.stories.ts
// - Pelo menos 3 stories (sm, md, lg, com footer)
```

### 4. Estratégia de Consumo

Crie um plano de como o DS será consumido pelos 4 produtos:

```
package.json — exports, sideEffects, build config
src/index.ts — barrel export
src/styles.css — CSS custom properties

Responda:
1. Como cada produto vai instalar o DS? (npm package, git submodule, monorepo?)
2. Como lidar com theming (cada produto pode ter variações de cor)?
3. Como garantir tree-shaking?
4. Como versionar (SemVer)?
5. Como documentar breaking changes?
```

### 5. Estratégia de Adoção

Crie um plano de migração para os 4 produtos adotarem o DS:

| Produto | Prioridade | Esforço | Riscos | Estratégia |
|---------|------------|---------|--------|------------|
| FintechPay App | ? | ? | ? | ? |
| FintechPay Dashboard | ? | ? | ? | ? |
| FintechPay Admin | ? | ? | ? | ? |
| FintechPay Onboarding | ? | ? | ? | ? |

Inclua:
- Ordem de adoção sugerida e justificativa
- Plano de migração gradual (estilo: parallel run, feature flag, big bang?)
- Métricas para medir sucesso da adoção

## Critérios de avaliação

- [ ] Tokens completos (cores, tipografia, spacing, effects) com TypeScript `as const`
- [ ] Button com todas as variantes, estados e props
- [ ] Input com label, error, hint, prefix/suffix
- [ ] Modal acessível com backdrop, esc, sizes
- [ ] Stories do Storybook para cada componente (mínimo 13 no total)
- [ ] Estratégia de consumo viável (package.json, exports, tree-shaking, theming)
- [ ] Plano de adoção realista com riscos e métricas
- [ ] Planilha de esforço/impacto para os 4 produtos
