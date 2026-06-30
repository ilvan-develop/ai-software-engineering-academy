# Agentes para o Módulo 06

## Agentes envolvidos

| Agente | Função |
|--------|--------|
| Curriculum Architect | Estruturar conteúdo de UI Design |
| UI Designer Agent | Referência em princípios de design, tipografia, cor |
| Frontend Developer Agent | Exemplos de código React/TypeScript, implementação de componentes |
| Accessibility Specialist Agent | WCAG, contraste, aria, navegação por teclado |
| Design System Agent | Tokens de cor, tipografia, espaçamento, dark mode |

## Instruções específicas

### UI Designer Agent

- Fornecer exemplos reais de aplicação dos princípios CRAP
- Explicar teoria das cores com foco em contexto enterprise
- Demonstrar escalas modulares de tipografia e espaçamento
- Incluir referências visuais de microinterações e animações

### Frontend Developer Agent

- Exemplos de código React/TypeScript para cada componente de UI
- Implementação de estados (hover, active, focus, disabled, loading, empty, error)
- Dark mode com ThemeProvider e Context API
- Utilitários de contraste, grid, e densidade

### Accessibility Specialist Agent

- Verificar contraste mínimo WCAG AA nos exemplos (4.5:1 texto, 3:1 componentes)
- Garantir que componentes tenham `aria-*` attributes, `role`, `tabIndex`
- Validar navegação por teclado (focus trap em modais, tab order)
- Incluir `prefers-color-scheme` e `prefers-reduced-motion`

### Design System Agent

- Definir tokens de cor (paleta funcional + neutra)
- Definir escala de tipografia (display, h1-h3, body, caption)
- Definir escala de espaçamento (2, 4, 8, 12, 16, 24, 32, 48)
- Definir tokens de animação (duration, easing)
- Garantir consistência entre temas light e dark
