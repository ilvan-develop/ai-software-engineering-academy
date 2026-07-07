# Exercícios — Módulo 07

## Exercício 1: Classifique os elementos no Atomic Design

Para cada elemento abaixo, classifique em qual nível do Atomic Design ele se encaixa (Átomo, Molécula, Organismo, Template ou Página).

| # | Elemento | Nível |
|---|----------|-------|
| 1 | Um botão "Salvar" | |
| 2 | Um formulário de login com email, senha e botão | |
| 3 | Um campo de input de texto | |
| 4 | A página de perfil do usuário com dados reais | |
| 5 | Um card de produto (imagem, título, preço, botão) | |
| 6 | Um token de cor `--color-primary-500` | |
| 7 | A estrutura de uma tela de dashboard (sidebar + header + content area vazia) | |
| 8 | Um ícone de lixeira | |

---

## Exercício 2: Crie design tokens para um novo tema

Uma empresa de saúde precisa de um Design System com **cores que transmitam confiança e cuidado**. O tema atual usa azul (`#3b82f6`). Para o novo produto, o cliente pediu uma paleta em **verde-teal**.

Complete os tokens abaixo:

```typescript
// tokens/colors.ts
export const colors = {
  brand: {
    primary: {
      50: '#______',   // tom mais claro (use teal como referência)
      100: '#______',
      200: '#______',
      300: '#______',
      400: '#______',
      500: '#______',  // ← cor primária (teal: #14b8a6)
      600: '#______',
      700: '#______',
      800: '#______',
      900: '#______',
      950: '#______',  // tom mais escuro
    },
  },
  semantic: {
    success: '#______',  // verde
    warning: '#______',  // âmbar
    error:   '#______',  // vermelho
    info:    '#______',  // azul info
  },
};
```javascript

**Perguntas:**
1. Qual a importância de ter 10 shades (50-950) para uma cor primária?
2. Como você garantiria que o `primary-500` tem contraste WCAG AA sobre fundo branco?

---

## Exercício 3: Implemente o componente Avatar

O squad de produto precisa de um componente **Avatar** no DS. Ele deve:

- Exibir a foto do usuário (se disponível) ou as iniciais (fallback)
- Ter tamanhos: `sm` (32px), `md` (40px), `lg` (56px)
- Aceitar uma prop `status` que exibe um indicador online/offline
- Ser acessível (aria-label)

Implemente o componente com TypeScript:

```typescript
// components/Avatar/Avatar.tsx

type AvatarSize = 'sm' | 'md' | 'lg';
type StatusType = 'online' | 'offline' | 'away' | 'busy';

interface AvatarProps {
  src?: string;
  name: string;         // usado para gerar iniciais
  size?: AvatarSize;
  status?: StatusType;
  className?: string;
}

// Implemente o componente abaixo
export function Avatar({ src, name, size = 'md', status, className }: AvatarProps) {
  // 1. Extraia as iniciais do nome (ex: "João Silva" → "JS")
  // 2. Defina os tamanhos baseados no token spacing
  // 3. Se src existir, renderize <img>, senão renderize as iniciais
  // 4. Se status existir, exiba um indicador no canto inferior direito
  // 5. Adicione aria-label com o nome do usuário
}
```markdown

---

## Exercício 4: Migration Guide — v1 para v2

Seu Design System está migrando da v1 para v2 com as seguintes mudanças:

1. **Button**: `appearance` → `variant` (mesmos valores: `'primary'`, `'secondary'`, `'danger'`)
2. **Input**: `placeholder` como label foi removido — agora usa `label` obrigatório
3. **Modal**: `onClose` agora é obrigatório (antes era opcional)
4. **Tokens**: `--color-blue-*` → `--color-primary-*`
5. **Spacing**: `spacing-5` (20px) foi removido — usar `spacing-4` (16px) ou `spacing-6` (24px)

Escreva um migration guide seguindo o formato:

```markdown
# Migration Guide: v1 → v2

## Button: `appearance` → `variant`

**Antes:**
```tsx
<Button appearance="primary" />
```text

**Depois:**
```tsx
<Button variant="primary" />
```text

**Codemod:**
```bash
npx @acme/ds-codemod button-appearance-to-variant
```text

<!-- Continue para os outros 4 itens... -->
```markdown

---

## Exercício 5: Configure um DS do zero

Siga o passo a passo da Seção 10 da aula para configurar um Design System básico.

**Passos:**

1. Crie um projeto com `pnpm init`
2. Instale React, TypeScript, Vite e Storybook
3. Crie a estrutura de diretórios:
   - `tokens/colors.ts` — defina 3 tokens (primary 500, spacing-4, radius-md)
   - `src/components/Button/Button.tsx` — implemente um botão com variant primary/secondary
   - `src/components/Button/Button.stories.ts` — 2 stories (Primary, Secondary)
   - `src/index.ts` — barrel export
   - `src/styles.css` — CSS custom properties
4. Configure o `vite.config.ts` para build de library
5. Configure o `.storybook/main.ts` e `preview.ts`

**Não precisa rodar os comandos** — apenas escreva os arquivos de configuração e componentes.

**Entregue:**
- `package.json` (apenas o campo de scripts e dependencies relevantes)
- `vite.config.ts`
- `tokens/colors.ts`
- `Button.tsx`
- `Button.stories.ts`
- `index.ts`
- `styles.css`
- `.storybook/main.ts`
- `.storybook/preview.ts`
