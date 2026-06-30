# Prompt: Criar Componente React

Você é um Frontend Expert Agent.

Crie um componente React no padrão do projeto.

## Especificação

- **Nome:** [nome do componente]
- **Tipo:** [Server Component / Client Component]
- **Props:** ...
- **Estados:** [loading, empty, error, success]
- **Acessibilidade:** requer ARIA labels?
- **Responsividade:** breakpoints necessários?

## Estrutura do componente

```tsx
interface [Componente]Props {
  // props tipadas
}

export function [Componente]({ ... }: [Componente]Props) {
  return (
    // JSX com Tailwind + acessibilidade
  )
}
```

## Requisitos

1. Usar Tailwind CSS classes
2. Incluir estados de loading, empty e error
3. ARIA labels em elementos interativos
4. Responsivo (mobile-first)
5. Teste unitário com Testing Library
6. Histórias Storybook (se aplicável)
