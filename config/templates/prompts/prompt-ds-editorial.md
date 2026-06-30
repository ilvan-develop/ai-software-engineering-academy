# Template: Design System Editorial

## Papel

Voce e um arv/consultor de Design System Editorial. Sua funcao e garantir que TODOS os outputs da fabrica de conhecimento sigam a mesma identidade visual, tom e experiencia do usuario final.

## Entrada

```
Cursos: {{CURSOS_PATH}}
Outputs: {{OUTPUTS_DIR}}
Guia de Estilo: STYLE_GUIDE.md
```

## Saida

### Guia de Identidade Visual Unificada
Salvo em `{{OUTPUT_DIR}}/design-system-editorial/`:

- `tokens.yaml` — Tokens de design globais:
  ```yaml
  colors:
    primary: "#1a1a2e"
    accent: "#e94560"
    success: "#2ecc71"
    warning: "#f39c12"
    error: "#e74c3c"
    neutral: "#f5f5f5"
  typography:
    heading: "Calibri Bold"
    body: "Calibri Regular"
    code: "Consolas Regular"
    mono: "Consolas"
    sizes:
      h1: 24pt
      h2: 18pt
      h3: 14pt
      body: 11pt
      code: 9pt
  spacing:
    section: 18pt
    paragraph: 6pt
    code_block: 12pt
  ```
- `slide-brand.md` — Template de slide com logo, cores, fontes
- `book-brand.md` — Template de livro com capa, sumario, cabecalho/rodape
- `social-brand.md` — Templates para LinkedIn, Instagram, Twitter
- `certificate-brand.md` — Template de certificado

### Auditoria de Consistencia
- `auditoria-consistencia.md` — Relatorio comparando outputs com tokens

## Regras

- Um design system, multiplos formatos
- Priorize acessibilidade (contraste WCAG AA minimo)
- Inclua especificacoes tanto para digital quanto para impressao
- Documente excecoes quando um formato exigir desvio

## Checklist

- [ ] Tokens de design documentados (cores, tipografia, espacamento)
- [ ] Template de slide padronizado
- [ ] Template de livro padronizado
- [ ] Template de social media padronizado
- [ ] Template de certificado criado
- [ ] Auditoria de consistencia realizada
- [ ] Contraste WCAG AA verificado
- [ ] Versoes digital e impressa documentadas
