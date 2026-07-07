# Módulo 06 — Slides

---

## Slide 1: Título

**UI Design**
Transformar wireframes em interfaces funcionais, acessíveis e consistentes.

---

## Slide 2: UI ≠ UX

```text
UI (Interface)                   UX (Experiência)
─────────────────────            ─────────────────────
Cores, tipografia               Pesquisa, jornada
Layout, componentes             Arquitetura, fluxo
"Como vê?"                      "Como se sente?"
```markdown

UI é a **superfície** dos 5 Planos de Garrett.

---

## Slide 3: CRAP — Princípios Visuais

```text
C  Contraste     — elementos diferentes parecem diferentes
R  Repetição     — estilos consistentes criam identidade
A  Alinhamento   — cada elemento conectado visualmente
P  Proximidade   — itens relacionados ficam juntos
```markdown

---

## Slide 4: Cor

| Função | Uso |
|--------|-----|
| Primary | Ação principal |
| Success | Confirmação |
| Warning | Alerta |
| Error | Erro / ação destrutiva |
| Neutral | Background, borda |

**Contraste WCAG AA**: texto 4.5:1, ícones 3:1

---

## Slide 5: Tipografia

```yaml
display:   32px / 700
heading1:  24px / 700
heading2:  20px / 600
heading3:  16px / 600
body:      14px / 400
caption:   11px / 400
```markdown

Escala modular (1.25 ou 1.333) para proporções harmônicas.

---

## Slide 6: Espaçamento e Grid

```yaml
Escala de espaçamento:
2 → 4 → 8 → 12 → 16 → 24 → 32 → 48

Grid por breakpoint:
Mobile:   4 colunas   gutter 16px
Tablet:   8 colunas   gutter 24px
Desktop: 12 colunas   gutter 24px
```markdown

---

## Slide 7: Componentes de UI

```yaml
Botões:   primary, secondary, outline, ghost, danger
Inputs:   label, placeholder, error, hint, disabled
Cards:    default, elevated, outlined
Modais:   sm (400) / md (560) / lg (720)
Tabelas:  colunas definidas, sortable, loading, empty
```markdown

Cada componente = props + variantes + estados.

---

## Slide 8: Estados dos Componentes

```text
Elemento   |  default  |  hover  |  active  |  focus  |  disabled
───────────────────────────────────────────────────────────────
Botão      |  #1A73E8  | #1557B0 | #0D47A1  |  ring   |  #E8EAED
Input      |  #DADCE0  | #9AA0A6 | —        | #1A73E8 |  #E8EAED
```markdown

---

## Slide 9: Design Patterns

```yaml
Navegação:   sidebar, top nav, tabs, breadcrumb, stepper
Formulários: label visível, validação inline, máscara
Feedback:    toast, alert, skeleton, spinner, modal
Onboarding:  guided tour, tooltip, empty state com CTA
Empty state: ilustração + título + descrição + ação
```markdown

---

## Slide 10: Microinterações

```yaml
Botão:      click → scale(0.98) + cor
Toggle:     thumb slide + bg animado
Modal:      fade in + translateY
Toast:      slide in da direita
Skeleton:   pulse shimmer
Link:       hover → underline aparece

Duração: 150ms–300ms | Easing: ease-in-out
```markdown

---

## Slide 11: Dark Mode — Paleta

```typescript
const light = { background: '#FFFFFF', text: '#202124' };
const dark  = { background: '#1F1F1F', text: '#E8EAED' };
```text

| Propriedade | Light | Dark |
|------------|-------|------|
| Bg primário | `#FFFFFF` | `#1F1F1F` |
| Bg card | `#FFFFFF` | `#333333` |
| Texto primário | `#202124` | `#E8EAED` |
| Primary | `#1A73E8` | `#8AB4F8` |
| Borda | `#DADCE0` | `#3C4043` |

---

## Slide 12: UI para Devs — Checklist

```json
[ ] Dimensões correspondem ao Figma
[ ] Padding/margin usam a escala de espaçamento
[ ] Tipografia: font-family, size, weight, line-height
[ ] Cores: hex exato do design system
[ ] Estados: hover, active, focus, disabled
[ ] Responsivo: mobile, tablet, desktop
[ ] Acessibilidade: contraste 4.5:1, focus visible
[ ] Dark mode implementado com ThemeProvider
```markdown

---

## Slide 13: Densidade Enterprise

```yaml
B2C:        padding 16px, font 14px, row 48px
Enterprise: padding 12px, font 13px, row 40px
Dense:      padding 8px,  font 12px, row 32px
```markdown

Produtos enterprise priorizam informação sobre espaço em branco.

---

## Slide 14: Ferramentas

| Ferramenta | Para que serve |
|-----------|----------------|
| Figma Inspect | Medir e extrair CSS |
| Pixel Perfect | Overlay design × código |
| Storybook | Catálogo de componentes |
| Chromatic | Review visual |
| Lighthouse | Acessibilidade + perf |

---

## Slide 15: Para refletir

> "UI é a ponte entre a intenção do design e a percepção do usuário."

> "Fidelidade não é copiar pixel a pixel — é entender o sistema de design e aplicá-lo com consistência."

> "Dark mode não é só inverter cores — é um tema com paleta própria."
