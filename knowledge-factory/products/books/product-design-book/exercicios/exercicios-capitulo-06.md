# Exercícios — Capítulo 6: Design System

> **Progressão:** Fácil → Médio → Difícil  
> **Total:** 4 exercícios

---

## Exercício 1 — Fácil: Atomic Design

**Tema:** Identificar níveis do Atomic Design

Classifique cada item no nível correspondente do Atomic Design:

| Item | Nível (Átomo/Molécula/Organismo/Template/Página) |
|------|--------------------------------------------------|
| Botão | ? |
| Formulário de login com header e footer | ? |
| Campo de texto com label + input + erro | ? |
| Página de perfil com dados do usuário | ? |
| Layout de página com sidebar + header + main | ? |
| Ícone de check | ? |
| Cor primária (#1A73E8) | ? |

---

## Exercício 2 — Médio: Sistema de Design Tokens

**Tema:** Tokens de design consistentes

Crie um sistema de design tokens para um novo produto. Use TypeScript com `as const`:

**Requisitos:**
- Paleta de cores: 10 níveis de cinza (50–950), 5 cores semânticas (success, warning, error, info, brand)
- Tipografia: escala de 8 tamanhos (display-xl até caption)
- Spacing: escala de 0 a 24 (seguindo base 4px)
- Border radius: none, sm, md, lg, full
- Shadows: sm, md, lg, xl
- Breakpoints: sm (640), md (768), lg (1024), xl (1280), 2xl (1536)

**Bônus:** Gere CSS Custom Properties a partir dos tokens.

---

## Exercício 3 — Médio: Storybook Stories

**Tema:** Documentação de componentes

Crie stories do Storybook para o componente `Select`:

```typescript
interface SelectProps {
  label: string;
  options: { value: string; label: string }[];
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  error?: string;
  disabled?: boolean;
  required?: boolean;
}
```

**Stories necessários:**
1. Default — com placeholder
2. Com valor selecionado
3. Com erro — mensagem de erro visível
4. Disabled — campo desabilitado
5. Required — com asterisco no label
6. Muitas opções — 20+ opções para testar scroll

---

## Exercício 4 — Difícil: Plano de Governança de DS

**Tema:** Governança e evolução do Design System

Você é o DS Lead em uma empresa com 5 squads de produto. O Design System tem 30 componentes, mas:

- Squads não estão usando — preferem criar componentes próprios
- Não há processo de contribuição
- Breaking changes são comunicados por Slack
- Não há métricas de adoção

**Tarefa:** Crie um plano de governança que resolva estes problemas:

1. **Processo de contribuição** — RFC template, critérios de aceite, review cycle
2. **Versionamento** — política SemVer, changelog, migration guides
3. **Comunidade** — DS guild, office hours, showcases mensais
4. **Métricas** — como medir adoção, ROI, satisfação dos squads
5. **Roadmap** — próximos 6 meses em 3 fases (curto/médio/longo prazo)
6. **Comunicação de breaking changes** — deprecação gradual, codemods, período de migração
