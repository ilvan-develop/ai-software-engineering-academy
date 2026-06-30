# Prompt: Descrever Tela com Design System

Descreva a implementação visual da tela abaixo usando tokens do Design System.

## Wireframe

[descrição do wireframe ou referência]

## Design System Tokens

```typescript
// Cores
colors: {
  primary: '#...',
  secondary: '#...',
  accent: '#...',
  muted: '#...',
  destructive: '#...',
  background: '#...',
  foreground: '#...',
}

// Tipografia
typography: {
  fontFamily: 'Inter, sans-serif',
  h1: { size: '2rem', weight: 700, lineHeight: 1.2 },
  h2: { size: '1.5rem', weight: 600, lineHeight: 1.3 },
  body: { size: '1rem', weight: 400, lineHeight: 1.5 },
  small: { size: '0.875rem', weight: 400 },
}

// Spacing
spacing: { 1: '4px', 2: '8px', 3: '12px', 4: '16px', ... }

// Radius
radius: { sm: '4px', md: '8px', lg: '12px', full: '9999px' }
```

## Saída esperada

Para cada seção/componente da tela, especifique:

1. **Componente** — qual componente shadcn/ui usar (Button, Card, Table, Dialog, etc.)
2. **Tokens** — cores, tipografia, spacing
3. **Estados** — hover, focus, active, disabled
4. **Responsividade** — como se adapta (grid, stack, hidden)
5. **Dark mode** — cores específicas para dark

Regras:
- Mobile-first
- Usar Tailwind classes (não CSS custom)
- Dark mode via `dark:` prefix
