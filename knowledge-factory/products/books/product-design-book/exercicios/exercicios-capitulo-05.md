# Exercícios — Capítulo 5: UI Design

> **Progressão:** Fácil → Médio → Difícil  
> **Total:** 4 exercícios

---

## Exercício 1 — Fácil: Identifique Violações CRAP

**Tema:** Princípios de design visual

Identifique qual(is) princípio(s) CRAP está(ão) sendo violados em cada caso:

| # | Cenário | Princípio Violado |
|---|---------|-------------------|
| 1 | Botão primário (#E8F0FE) e fundo da página (#FFFFFF) — quase invisível | ? |
| 2 | Cada card do dashboard tem um padding diferente (12px, 16px, 20px) | ? |
| 3 | Título alinhado à esquerda, corpo centralizado, botão à direita | ? |
| 4 | O rótulo "Email" está a 40px do campo de input | ? |

---

## Exercício 2 — Médio: Paleta de Cores Acessível

**Tema:** Contraste e acessibilidade WCAG

Dada a paleta abaixo, verifique quais combinações atendem WCAG AA (4.5:1 para texto normal):

```typescript
const palette = {
  primary: '#1A73E8',
  primaryLight: '#E8F0FE',
  textPrimary: '#202124',
  textSecondary: '#5F6368',
  bgWhite: '#FFFFFF',
  bgGray: '#F1F3F4',
  error: '#EA4335',
  success: '#34A853',
};
```

**Tarefa:** Para cada par (foreground, background), calcule se atende AA:
1. `textPrimary` em `bgWhite` (já sabemos que sim — 4.5:1 ✓)
2. `textSecondary` em `bgWhite`
3. `textPrimary` em `bgGray`
4. `primary` em `bgWhite` (como botão)
5. `error` em `bgWhite` (texto de erro)

Use a fórmula de contraste relativo da WCAG:
```
L = 0.2126 * R + 0.7152 * G + 0.0722 * B
ratio = (L1 + 0.05) / (L2 + 0.05)
```

---

## Exercício 3 — Médio: Implemente um Componente

**Tema:** Componente com todos os estados

Implemente um componente `Toggle` em React + TypeScript seguindo o design system:

```typescript
interface ToggleProps {
  checked: boolean;
  onChange: (checked: boolean) => void;
  disabled?: boolean;
  label?: string;
}
```

**Requisitos:**
- Estados: default, checked, disabled, disabled+checked, hover, focus
- Animação suave do thumb (150ms ease)
- Acessível: role="switch", aria-checked, focus visible
- Suporte a teclado (Enter/Space para toggle)
- Use tokens do design system (cores da paleta, spacing scale)

---

## Exercício 4 — Difícil: Dark Mode

**Tema:** Implementação de tema escuro

Converta o componente `Card` abaixo para suportar dark mode:

```typescript
const cardVariants = {
  default:  { bg: '#FFFFFF', border: '1px solid #E8EAED', boxShadow: 'none' },
  elevated: { bg: '#FFFFFF', border: 'none', boxShadow: '0 1px 3px rgba(0,0,0,0.1)' },
  outlined: { bg: '#FFFFFF', border: '1px solid #DADCE0', boxShadow: 'none' },
};
```

**Tarefas:**
1. Crie a versão dark de cada variante
2. Implemente usando ThemeContext (como visto no capítulo)
3. O card deve aceitar `noTheme` prop para casos especiais (ex: preview de email)
4. Adicione transição suave ao trocar de tema (200ms)
