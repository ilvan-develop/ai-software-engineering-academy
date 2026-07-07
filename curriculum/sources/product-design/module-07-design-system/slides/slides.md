# Módulo 07 — Slides

---

## Slide 1: Título

**Design System: Consistência em Escala**
Como construir, manter e escalar sistemas de design no Enterprise

---

## Slide 2: O que é Design System?

```text
Style Guide:             Component Library:         Design System:
"Guia de estilos"        "Biblioteca de             "Ecossistema vivo"
                         componentes"
─────────────            ─────────────               ─────────────
Cores, tipografia,       Botões, inputs,             Tudo acima +
grid                     tabelas, cards              processos,
                                                     governance,
─ Estático               ─ Dinâmico                  tooling,
─ PDF/doc                ─ npm package               documentação
```markdown

> "Um Design System não é um projeto. É um produto que serve outros produtos."

---

## Slide 3: Atomic Design (Brad Frost)

```text
Átomos ─→ Moléculas ─→ Organismos ─→ Templates ─→ Páginas
  │            │             │             │            │
Botão       Input +       Formulário    Layout da     Página de
Ícone       Label +       + Header +    página de     cadastro
Label       Error =       Footer        cadastro      (com dados)
Tag         Campo de      = Página      (vazia)
Cor
```markdown

5 níveis de complexidade → do mais simples ao mais completo

---

## Slide 4: Design Tokens

Variáveis visuais que abstraem decisões de design:

```text
Cores           Tipografia          Spacing          Efeitos
──────────      ──────────          ────────         ────────
Primary 500     display-xl          spacing-4        shadow-md
Semantic error  body                spacing-8        radius-lg
Neutral 900     caption             spacing-16       radius-full
```text

```typescript
const colors = {
  brand: { primary: { 500: '#3b82f6', 600: '#2563eb' } },
  semantic: { success: '#10b981', error: '#ef4444' },
  neutral: { 100: '#f3f4f6', 900: '#111827' },
} as const;
```markdown

---

## Slide 5: Componentes — Botão

```typescript
interface ButtonProps {
  variant: 'primary' | 'secondary' | 'outline' | 'ghost' | 'danger';
  size: 'sm' | 'md' | 'lg';
  loading?: boolean;
  disabled?: boolean;
  fullWidth?: boolean;
  leftIcon?: React.ReactNode;
  rightIcon?: React.ReactNode;
}
```sql

| Variant | Visual | Uso |
|---------|--------|-----|
| primary | Azul sólido | Ação principal |
| secondary | Cinza claro | Ação secundária |
| outline | Borda | Alternativa leve |
| ghost | Transparente | Contexto denso |
| danger | Vermelho | Ação destrutiva |

---

## Slide 6: Componentes — Input, Select, Modal, Table

```yaml
Input:                              Select:
┌─────────────────────────────────┐ ┌─────────────────────────────────┐
│ Email                           │ │  Cargo                          │
│ ┌───────────────────────────┐   │ │ ┌───────────────────────────┐   │
│ │ user@email.com            │   │ │ │ Selecione...          ▼   │   │
│ └───────────────────────────┘   │ │ └───────────────────────────┘   │
└─────────────────────────────────┘ └─────────────────────────────────┘

Modal:                              Table:
┌─────────────────────────────┐   ┌─────────┬─────────┬─────────┐
│ ✕ Editar usuário            │   │  Nome   │ Cargo   │  Status  │
│ ────────────────────        │   ├─────────┼─────────┼─────────┤
│ Nome: [                   ] │   │  Ana    │ Dev     │ Ativo   │
│ Email: [                  ] │   │  João   │ Design  │ Ativo   │
│ ────────────────────        │   └─────────┴─────────┴─────────┘
│ [Cancelar] [Salvar]         │
└─────────────────────────────┘
```markdown

Cada componente: padronizado, acessível, documentado, testado

---

## Slide 7: Documentação com Storybook

```typescript
// Button.stories.ts
export default {
  title: 'Components/Button',
  component: Button,
  argTypes: {
    variant: { control: 'select', options: ['primary', 'secondary'] },
    size: { control: 'select', options: ['sm', 'md', 'lg'] },
  },
  tags: ['autodocs'],
};

export const Primary = {
  args: { variant: 'primary', children: 'Salvar' },
};
```text

Storybook oferece:
- 📖 Documentação automática (autodocs)
- 🎮 Playground interativo (controles)
- ♿ Auditoria de acessibilidade (a11y addon)
- 📐 Visual regression testing (Chromatic)
- 🎨 Embed do Figma (designs addon)

---

## Slide 8: Versionamento — SemVer

```text
MAJOR (1.x.x → 2.0.0):
  Breaking changes
  Button: `appearance="primary"` → `variant="primary"`
  Token: `--blue-500` → `--primary-500`

MINOR (x.1.x → x.2.0):
  Novas funcionalidades
  Novo componente Tooltip
  Nova prop `size` no Modal

PATCH (x.x.1 → x.x.2):
  Correções
  Contraste do Button danger
  Fechamento do Modal via Escape
```text

❌ Breaking sem aviso → projetos quebram
✅ Depreciação gradual + migration guide + codemod

---

## Slide 9: Consumo em Projetos

```javascript
npm package (@empresa/design-system)
         │
         ├── Tree-shaking (import { Button })
         ├── CSS Custom Properties (theming)
         ├── ThemeProvider (contexto)
         └── Types (TypeScript)
```text

```json
{
  "exports": {
    ".": "./dist/index.mjs",
    "./styles.css": "./dist/styles.css",
    "./tokens": "./dist/tokens/index.js"
  }
}
```text

```typescript
// Consumo
import { Button, Modal, Input } from '@empresa/design-system';
import '@empresa/design-system/styles.css';
```markdown

---

## Slide 10: Manutenção e Governance

```text
DS Squad:
┌────────────────────────────────────┐
│  Core Team (dedicado)              │
│  ├── Design Lead                   │
│  ├── Engineering Lead              │
│  └── Developer                     │
├────────────────────────────────────┤
│  Contributors (cada squad)         │
│  ├── Designers dos produtos        │
│  ├── Devs frontend                 │
│  └── QA / Acessibilidade           │
└────────────────────────────────────┘
```text

Processo de contribuição:
1. RFC → 2. Review DS Squad → 3. Implementação → 4. Code Review (design + a11y) → 5. Release

---

## Slide 11: ROI no Enterprise

| Métrica | Antes do DS | Depois do DS |
|---------|-------------|--------------|
| Tela simples | 3 dias | 1 dia |
| Tela complexa | 5 dias | 2.5 dias |
| Onboarding dev | 2 meses | 2 semanas |
| Bugs de UI/mês | 15 | 3 |
| Consistência | "cada um faz do seu jeito" | "padrão único" |

**ROI estimado (5 squads):**
- Economia: ~R$ 20K/tela × 20 telas/mês = R$ 400K/mês
- Custo DS Squad: R$ 85K/mês
- **Retorno líquido: ~R$ 3.8M/ano**

---

## Slide 12: Implementação Prática

```bash
mkdir my-design-system && cd my-design-system
pnpm init
pnpm add react react-dom
pnpm add -D typescript vite storybook
pnpm dlx storybook@latest init --builder=vite
```text

```javascript
my-design-system/
├── tokens/          → colors, typography, spacing
├── src/components/  → Button, Input, Modal, Table, Select
├── src/index.ts     → barrel export
├── .storybook/      → main.ts, preview.ts
└── vite.config.ts   → build lib
```markdown

Próximo passo: criar o primeiro componente com tokens!

---

## Slide 13: Para refletir

> "Design Systems não são sobre pixels. São sobre **pessoas, processos e consistência** em escala."

- Design System é **produto**, não projeto
- **Tokens primeiro**, componentes depois
- **Documentação é obrigatória**, não opcional
- **Versionamento salva vidas** (e deploys)
- **ROI aparece quando o sistema escala** para 3+ produtos
