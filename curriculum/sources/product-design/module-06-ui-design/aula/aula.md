# Módulo 06 — UI Design

**Transformar wireframes em interfaces funcionais, acessíveis e visualmente consistentes.**

---

## 1. O que é UI Design

UI (User Interface) Design é a disciplina responsável pela **aparência e comportamento visual** de um produto digital. Enquanto UX define a estrutura e a experiência, UI traduz essa estrutura em pixels — cores, tipografia, espaçamento, componentes e animações.

### UI ≠ UX

```text
UI (User Interface)              UX (User Experience)
─────────────────────             ─────────────────────
Aparência visual                 Experiência completa
Cores, tipografia, ícones        Pesquisa, jornada, AI
Layout e componentes             Fluxo e arquitetura
Microinterações                  Emoção e usabilidade
"Como vê?"                       "Como se sente?"
```markdown

UI é a **camada de superfície** dos 5 Planos de Garrett. É o que o usuário vê e com o que interage diretamente.

### A relação UI + UX

```text
UX sem UI: ideia sem forma, impossível de usar
UI sem UX: bonito mas inútil, frustrante
UI + UX: útil, usável e desejável
```markdown

O papel do dev é implementar a UI com **fidelidade ao design**, respeitando decisões de UX embutidas nos componentes.

---

## 2. Princípios de Design Visual — CRAP

CRAP é um acrônimo para os 4 princípios fundamentais do design visual.

### Contraste

Elementos diferentes devem **parecer diferentes**. Use contraste para destacar o que é importante.

```typescript
// ❌ Botão primário vs secundário quase iguais
const bad = { primary: '#4A90D9', secondary: '#5BA0E9' };

// ✅ Contraste claro entre ações
const good = { primary: '#1A73E8', secondary: '#E8F0FE' };
```text

- Contraste de **cor**: fundo vs texto, botão primário vs secundário
- Contraste de **tamanho**: título vs corpo
- Contraste de **peso**: bold vs regular
- Contraste de **forma**: botão preenchido vs outline

### Repetição

Repita estilos visuais para criar consistência.

```text
Mesma cor de link        → usuário reconhece que é clicável
Mesmo padding nos cards  → ritmo visual previsível
Mesmo border-radius      → identidade visual consistente
```markdown

### Alinhamento

Nada deve ser colocado arbitrariamente. Cada elemento tem conexão visual com outro.

```typescript
// ❌ Alinhamento solto
const misaligned = {
  title: { marginLeft: 16 },
  body: { marginLeft: 20 },
  action: { marginLeft: 12 },
};

// ✅ Alinhamento consistente
const aligned = {
  title: { marginLeft: 16 },
  body: { marginLeft: 16 },
  action: { marginLeft: 16 },
};
```markdown

### Proximidade

Itens relacionados devem ficar **próximos** visualmente. Itens não relacionados, separados.

```text
❌ Agrupamento confuso:
  [Nome] [Email] [Telefone]
  [Senha] [Confirmar Senha]

✅ Agrupamento lógico por proximidade:
  [Nome] [Email]          ← Dados pessoais
  [Telefone]              ← Contato
  [Senha] [Confirmar]     ← Segurança
```markdown

---

## 3. Cor

### Teoria das Cores

Cores comunicam significado e emoção. No contexto enterprise, a escolha deve ser funcional, não apenas estética.

| Cor | Significado comum | Uso em UI enterprise |
|-----|------------------|---------------------|
| Azul | Confiança, segurança | Primary action, links |
| Verde | Sucesso, conclusão | Confirmação, status OK |
| Vermelho | Erro, perigo | Erro, ação destrutiva |
| Amarelo | Atenção, aviso | Warning, alerta |
| Cinza | Neutro, secundário | Background, disabled |

### Paletas de cor no Design System

```typescript
interface ColorPalette {
  primary: string;
  primaryHover: string;
  primaryLight: string;
  secondary: string;
  success: string;
  warning: string;
  error: string;
  info: string;
  neutral: {
    50: string;   // background mais claro
    100: string;
    200: string;
    300: string;
    400: string;
    500: string;  // cor neutra base
    600: string;
    700: string;
    800: string;
    900: string;  // texto mais escuro
  };
}

const enterprisePalette: ColorPalette = {
  primary: '#1A73E8',
  primaryHover: '#1557B0',
  primaryLight: '#E8F0FE',
  secondary: '#5F6368',
  success: '#34A853',
  warning: '#FBBC04',
  error: '#EA4335',
  info: '#4285F4',
  neutral: {
    50: '#F8F9FA',
    100: '#F1F3F4',
    200: '#E8EAED',
    300: '#DADCE0',
    400: '#BDC1C6',
    500: '#9AA0A6',
    600: '#80868B',
    700: '#5F6368',
    800: '#3C4043',
    900: '#202124',
  },
};
```text

### Acessibilidade e Contraste

WCAG 2.2 define ratios mínimos de contraste:

| Tipo | Ratio mínimo (AA) | Ratio mínimo (AAA) |
|------|------------------|-------------------|
| Texto normal (< 18px) | 4.5:1 | 7:1 |
| Texto grande (>= 18px bold ou 24px) | 3:1 | 4.5:1 |
| Componentes ativos (ícones, inputs) | 3:1 | — |

```typescript
// Utilitário de contraste
function isAccessible(foreground: string, background: string, level: 'AA' | 'AAA' = 'AA'): boolean {
  const ratio = getContrastRatio(foreground, background); // implementação do módulo 04
  const threshold = level === 'AA' ? 4.5 : 7;
  return ratio >= threshold;
}

// Uso na validação do tema
const theme = {
  textPrimary: '#202124',
  bgPrimary: '#FFFFFF',
};

console.log(isAccessible(theme.textPrimary, theme.bgPrimary)); // true
```markdown

### Cor e Branding

No contexto enterprise, a paleta primária reflete a marca, mas a paleta **funcional** (success, error, warning, info) deve seguir padrões culturais. Nunca use verde para erros ou vermelho para sucesso.

```typescript
interface BrandTokens {
  colors: ColorPalette;
  usage: {
    primaryAction: string;
    dangerAction: string;
    link: string;
    border: string;
    surface: {
      page: string;
      card: string;
      modal: string;
      sidebar: string;
    };
    text: {
      primary: string;
      secondary: string;
      disabled: string;
      inverse: string;
    };
  };
}
```text

---

## 4. Tipografia

### Hierarquia Tipográfica

A hierarquia guia o olho do usuário: o que é mais importante deve ser visualmente mais proeminente.

```typescript
interface TypographyScale {
  display: { size: number; lineHeight: number; weight: number };
  heading1: { size: number; lineHeight: number; weight: number };
  heading2: { size: number; lineHeight: number; weight: number };
  heading3: { size: number; lineHeight: number; weight: number };
  body: { size: number; lineHeight: number; weight: number };
  bodySmall: { size: number; lineHeight: number; weight: number };
  caption: { size: number; lineHeight: number; weight: number };
}

const enterpriseTypography: TypographyScale = {
  display:    { size: 32, lineHeight: 40, weight: 700 },
  heading1:   { size: 24, lineHeight: 32, weight: 700 },
  heading2:   { size: 20, lineHeight: 28, weight: 600 },
  heading3:   { size: 16, lineHeight: 24, weight: 600 },
  body:       { size: 14, lineHeight: 20, weight: 400 },
  bodySmall:  { size: 12, lineHeight: 16, weight: 400 },
  caption:    { size: 11, lineHeight: 16, weight: 400 },
};
```markdown

### Escalas Modulares

Use uma escala modular (ex: 1.25 ou 1.333) para garantir proporções harmônicas.

```text
Escala 1.25 (Major Second):
11 → 14 → 16 → 20 → 24 → 32 → 40

Escala 1.333 (Major Third):
12 → 16 → 20 → 24 → 32 → 40 → 48
```markdown

### Legibilidade

- **Largura de linha**: 45–75 caracteres por linha (ideal ~66)
- **Line-height**: 1.4–1.6 para body text
- **Font-weight**: 400 para body, 600+ para headings
- **Font-family**: system-ui ou fonte carregada via CDN

```typescript
// Stack de fontes para enterprise
const fontStack = {
  sans: `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`,
  mono: `'JetBrains Mono', 'Fira Code', 'Cascadia Code', Consolas, monospace`,
};

// Uso no CSS-in-JS
const bodyStyle = {
  fontFamily: fontStack.sans,
  fontSize: 14,
  lineHeight: 1.5,
  maxWidth: '66ch', // controle de largura
};
```text

---

## 5. Espaçamento e Grid

### Box Model e Spacing Consistente

Use uma escala de espaçamento, não valores arbitrários.

```typescript
const spacing = {
  xxs:  2,   // 2px  — divider finíssimo
  xs:   4,   // 4px  — ícone pequeno, gap mínimo
  sm:   8,   // 8px  — padding interno de inputs
  md:   12,  // 12px — gap entre label e input
  lg:   16,  // 16px — padding de cards, seções
  xl:   24,  // 24px — margem entre seções
  xxl:  32,  // 32px — padding de página
  xxxl: 48,  // 48px — seções grandes no layout
};
```text

```typescript
// ❌ Espaçamento arbitrário
const badCard = { padding: 17, gap: 11 };

// ✅ Espaçamento da escala
const goodCard = { padding: spacing.lg, gap: spacing.md };
```text

### Grid Systems

| Grid | Colunas | Gutters | Uso |
|------|---------|---------|-----|
| Mobile | 4 | 16px | Telas < 768px |
| Tablet | 8 | 24px | 768px–1024px |
| Desktop | 12 | 24px | > 1024px |

```typescript
interface GridConfig {
  columns: number;
  gutter: number;
  margin: number;
  maxWidth: number;
}

const grid: Record<string, GridConfig> = {
  mobile:  { columns: 4,  gutter: 16, margin: 16, maxWidth: 480 },
  tablet:  { columns: 8,  gutter: 24, margin: 24, maxWidth: 960 },
  desktop: { columns: 12, gutter: 24, margin: 0,  maxWidth: 1200 },
};

// Utility: cálculo de coluna
function colWidth(columns: number, totalColumns: number, gutter: number): string {
  const fraction = columns / totalColumns;
  return `calc(${fraction * 100}% - ${gutter}px)`;
}
```markdown

### Layout Patterns

```text
Dashboard:
┌──────────────┬──────────┬──────────┐
│   Sidebar    │   Main   │  Panel   │
│   240px      │   1fr    │  320px   │
└──────────────┴──────────┴──────────┘

Single Column (formulários):
┌────────────────────────────────────────┐
│              Content (max 720px)       │
└────────────────────────────────────────┘

Split Screen:
┌────────────────────┬───────────────────┐
│    List (1fr)      │   Detail (1fr)    │
└────────────────────┴───────────────────┘
```markdown

---

## 6. Componentes de UI

### Botões

```typescript
type ButtonVariant = 'primary' | 'secondary' | 'outline' | 'ghost' | 'danger';
type ButtonSize = 'sm' | 'md' | 'lg';

interface ButtonProps {
  variant: ButtonVariant;
  size: ButtonSize;
  disabled?: boolean;
  loading?: boolean;
  icon?: React.ReactNode;
  children: React.ReactNode;
}

// Mapa de cores por variante
const buttonStyles: Record<ButtonVariant, { bg: string; color: string; border: string }> = {
  primary:   { bg: '#1A73E8', color: '#FFFFFF', border: 'transparent' },
  secondary: { bg: '#E8F0FE', color: '#1A73E8', border: 'transparent' },
  outline:   { bg: 'transparent', color: '#1A73E8', border: '#1A73E8' },
  ghost:     { bg: 'transparent', color: '#5F6368', border: 'transparent' },
  danger:    { bg: '#EA4335', color: '#FFFFFF', border: 'transparent' },
};
```text

### Inputs e Formulários

```typescript
interface InputProps {
  label: string;
  placeholder?: string;
  error?: string;
  hint?: string;
  disabled?: boolean;
  required?: boolean;
  leftIcon?: React.ReactNode;
}

// Estados do input
const inputStates = {
  default: { border: '#DADCE0', bg: '#FFFFFF' },
  hover:   { border: '#9AA0A6', bg: '#FFFFFF' },
  focus:   { border: '#1A73E8', bg: '#FFFFFF', boxShadow: '0 0 0 3px #E8F0FE' },
  error:   { border: '#EA4335', bg: '#FFFFFF' },
  disabled: { border: '#E8EAED', bg: '#F1F3F4', color: '#9AA0A6' },
};
```markdown

### Cards

```typescript
interface CardProps {
  padding?: keyof typeof spacing;
  variant?: 'default' | 'elevated' | 'outlined';
  onClick?: () => void;
}

const cardVariants = {
  default:  { bg: '#FFFFFF', border: '1px solid #E8EAED', boxShadow: 'none' },
  elevated: { bg: '#FFFFFF', border: 'none', boxShadow: '0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06)' },
  outlined: { bg: '#FFFFFF', border: '1px solid #DADCE0', boxShadow: 'none' },
};
```text

### Modais

```typescript
interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  size: 'sm' | 'md' | 'lg';
  children: React.ReactNode;
  footer?: React.ReactNode;
}

const modalSizes = {
  sm: { width: 400 },
  md: { width: 560 },
  lg: { width: 720 },
};

// Overlay deve fechar o modal
const overlayStyles = {
  position: 'fixed',
  inset: 0,
  bg: 'rgba(0, 0, 0, 0.5)',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
  zIndex: 1000,
};
```markdown

### Tabelas

```typescript
interface Column<T> {
  key: keyof T;
  header: string;
  width?: number;
  align?: 'left' | 'center' | 'right';
  render?: (value: T[keyof T], row: T) => React.ReactNode;
  sortable?: boolean;
}

interface TableProps<T> {
  columns: Column<T>[];
  data: T[];
  loading?: boolean;
  emptyMessage?: string;
  onRowClick?: (row: T) => void;
}
```text

### Dropdowns e Selects

```typescript
interface Option {
  value: string;
  label: string;
  disabled?: boolean;
  group?: string;
}

interface SelectProps {
  options: Option[];
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  searchable?: boolean;
  clearable?: boolean;
}
```markdown

---

## 7. Design Patterns

### Navegação

| Tipo | Quando usar | Exemplo |
|------|------------|---------|
| Sidebar | Muitas seções, hierarquia profunda | Dashboards |
| Top nav | Poucas seções, conteúdo horizontal | Sites institucionais |
| Tabs | Seções relacionadas, mesma página | Detalhes de registro |
| Breadcrumb | Hierarquia profunda, orientação | E-commerce, docs |
| Stepper | Fluxo sequencial | Wizard, checkout |

```typescript
interface BreadcrumbItem {
  label: string;
  href?: string;
  isCurrent?: boolean;
}

function Breadcrumb({ items }: { items: BreadcrumbItem[] }) {
  return (
    <nav aria-label="Breadcrumb">
      {items.map((item, i) => (
        <span key={i}>
          {i > 0 && <ChevronRightIcon />}
          {item.isCurrent
            ? <span aria-current="page">{item.label}</span>
            : <a href={item.href}>{item.label}</a>
          }
        </span>
      ))}
    </nav>
  );
}
```text

### Formulários

Patterns que melhoram a experiência de formulários:

```typescript
// ✅ Label visível e associado
<label htmlFor="email">Email</label>
<input id="email" type="email" aria-describedby="email-hint" />
<span id="email-hint">Usaremos seu email para login</span>

// ✅ Validação inline
function validateField(value: string): string | null {
  if (!value) return 'Campo obrigatório';
  if (value.length < 3) return 'Mínimo de 3 caracteres';
  return null;
}

// ✅ Máscara de formatação
function formatPhone(value: string): string {
  const digits = value.replace(/\D/g, '').slice(0, 11);
  if (digits.length <= 2) return `(${digits}`;
  if (digits.length <= 7) return `(${digits.slice(0, 2)}) ${digits.slice(2)}`;
  return `(${digits.slice(0, 2)}) ${digits.slice(2, 7)}-${digits.slice(7)}`;
}
```markdown

### Feedback

| Situação | Componente | Exemplo |
|----------|-----------|---------|
| Sucesso | Toast/snackbar | "Projeto salvo" |
| Erro | Alert + inline error | "Email inválido" |
| Carregando | Skeleton / Spinner | Skeleton de 3 linhas |
| Vazio | Empty state | "Nenhum projeto ainda" |
| Confirmação | Modal/dialog | "Tem certeza?" |

### Onboarding

```typescript
interface OnboardingStep {
  target: string;        // seletor do elemento alvo
  title: string;
  content: string;
  position: 'top' | 'bottom' | 'left' | 'right';
}

const onboarding: OnboardingStep[] = [
  {
    target: '#create-project-btn',
    title: 'Criar projeto',
    content: 'Clique aqui para criar seu primeiro projeto',
    position: 'bottom',
  },
  {
    target: '#sidebar',
    title: 'Navegação',
    content: 'Use o menu lateral para acessar todas as seções',
    position: 'right',
  },
];
```text

### Empty States

Nunca mostre uma tela em branco. Todo empty state deve ter:

1. **Ilustração** ou ícone representativo
2. **Título** claro do que falta
3. **Descrição** do que fazer
4. **CTA** para a ação principal

```typescript
const emptyState = {
  title: 'Nenhum projeto encontrado',
  description: 'Crie seu primeiro projeto para começar a organizar suas tarefas.',
  action: { label: 'Criar projeto', href: '/projects/new' },
};
```markdown

---

## 8. Microinterações

Microinterações são **pequenos momentos de feedback** que comunicam o resultado de uma ação.

### Estados Visuais

```css
/* Botão — todos os estados */
.button {
  background: #1A73E8;
  transition: background 0.15s ease, box-shadow 0.15s ease;
  cursor: pointer;
}

.button:hover {
  background: #1557B0; /* escurece 10-15% */
}

.button:active {
  background: #0D47A1; /* escurece mais */
  transform: scale(0.98);
}

.button:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px #E8F0FE;
}

.button:disabled {
  background: #E8EAED;
  color: #9AA0A6;
  cursor: not-allowed;
  transform: none;
}
```text

### Animações

```typescript
interface AnimationTokens {
  duration: {
    instant:  '50ms';
    fast:     '150ms';
    normal:   '200ms';
    slow:     '300ms';
  };
  easing: {
    default:  'ease';
    enter:    'cubic-bezier(0.0, 0.0, 0.2, 1)';
    exit:     'cubic-bezier(0.4, 0.0, 1, 1)';
    spring:   'cubic-bezier(0.34, 1.56, 0.64, 1)';
  };
}

// Modal enter/exit
const modalAnimation = {
  enter: {
    opacity: [0, 1],
    transform: ['translateY(8px)', 'translateY(0)'],
    duration: 200,
    easing: 'cubic-bezier(0.0, 0.0, 0.2, 1)',
  },
  exit: {
    opacity: [1, 0],
    transform: ['translateY(0)', 'translateY(4px)'],
    duration: 150,
    easing: 'cubic-bezier(0.4, 0.0, 1, 1)',
  },
};
```markdown

### Microinterações Essenciais

```text
Elemento        | Interação       | Feedback
─────────────────────────────────────────────────
Botão           | Click           | Scale 0.98 + cor
Toggle          | Toggle          | Animação do thumb + bg
Input           | Focus           | Borda azul + box-shadow
Dropdown        | Open            | Fade in + slide
Toast           | Appear          | Slide in da direita
Skeleton        | Load            | Pulse shimmer
Link            | Hover           | Underline aparece
Checkbox        | Toggle          | Check animado
```markdown

---

## 9. Dark Mode

### Estratégia de Implementação

Dark mode não é apenas inverter cores — é um **tema alternativo** com paleta própria.

```typescript
type ThemeMode = 'light' | 'dark';

interface Theme {
  mode: ThemeMode;
  colors: {
    background: {
      primary: string;
      secondary: string;
      elevated: string;
      modal: string;
    };
    text: {
      primary: string;
      secondary: string;
      disabled: string;
      inverse: string;
    };
    border: {
      default: string;
      hover: string;
      focus: string;
    };
    action: {
      primary: string;
      primaryHover: string;
      secondary: string;
    };
  };
}

const lightTheme: Theme = {
  mode: 'light',
  colors: {
    background: {
      primary: '#FFFFFF',
      secondary: '#F8F9FA',
      elevated: '#FFFFFF',
      modal: '#FFFFFF',
    },
    text: {
      primary: '#202124',
      secondary: '#5F6368',
      disabled: '#9AA0A6',
      inverse: '#FFFFFF',
    },
    border: {
      default: '#DADCE0',
      hover: '#9AA0A6',
      focus: '#1A73E8',
    },
    action: {
      primary: '#1A73E8',
      primaryHover: '#1557B0',
      secondary: '#E8F0FE',
    },
  },
};

const darkTheme: Theme = {
  mode: 'dark',
  colors: {
    background: {
      primary: '#1F1F1F',
      secondary: '#2C2C2C',
      elevated: '#333333',
      modal: '#2C2C2C',
    },
    text: {
      primary: '#E8EAED',
      secondary: '#9AA0A6',
      disabled: '#5F6368',
      inverse: '#202124',
    },
    border: {
      default: '#3C4043',
      hover: '#5F6368',
      focus: '#8AB4F8',
    },
    action: {
      primary: '#8AB4F8',
      primaryHover: '#A8C7FA',
      secondary: '#3C4043',
    },
  },
};
```text

### Contraste no Dark Mode

O contraste absoluto não muda, mas a **percepção** sim. Ajustes necessários:

- Evite pretos puros (`#000000`) — use `#1F1F1F`
- Prefira branco suave (`#E8EAED`) em vez de branco puro (`#FFFFFF`)
- Sombras viram luz (elevation vira tom mais claro que o fundo)
- Cores vibrantes (primary) devem ser dessaturadas para evitar fadiga

```text
Light mode:          Dark mode:
┌────────────┐      ┌────────────┐
│ #FFFFFF    │      │ #1F1F1F    │
│  bg        │      │  bg        │
├────────────┤      ├────────────┤
│ #202124    │      │ #E8EAED    │
│  text      │      │  text      │
├────────────┤      ├────────────┤
│ #1A73E8    │      │ #8AB4F8    │
│  primary   │      │  primary   │
└────────────┘      └────────────┘
```markdown

### Implementação com Context

```typescript
const ThemeContext = React.createContext<{
  theme: Theme;
  toggleTheme: () => void;
}>({
  theme: lightTheme,
  toggleTheme: () => {},
});

function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [mode, setMode] = useState<ThemeMode>('light');

  const toggleTheme = () => {
    setMode(prev => prev === 'light' ? 'dark' : 'light');
  };

  const theme = mode === 'light' ? lightTheme : darkTheme;

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      <div data-theme={mode} style={{ background: theme.colors.background.primary }}>
        {children}
      </div>
    </ThemeContext.Provider>
  );
}
```markdown

---

## 10. UI para Devs

### Inspeção no Figma

Ao inspecionar um layout no Figma, extraia:

```text
Elemento     | O que inspecionar
──────────────────────────────────────
Botão        | width, height, padding, border-radius, font-size, bg
Input        | padding, border, border-radius, font-size, label position
Card         | padding, border-radius, box-shadow, gap entre filhos
Text         | font-family, font-size, line-height, letter-spacing, color
Spacing      | margin, gap, top/left/bottom/right values
```markdown

### Medidas e Densidade

```typescript
// Prefira valores da escala de espaçamento
const badImplementation = {
  padding: '13px 22px', // arbitrário
};

const faithfulImplementation = {
  padding: 12, // da escala: spacing.sm
  gap: 8,      // da escala: spacing.xs
};
```text

### Implementação Fiel

Checklist para implementar um componente com fidelidade:

```typescript
interface UIInspectionChecklist {
  layout: {
    dimensions: boolean;      // width, height, min/max
    padding: boolean;         // internal spacing
    margin: boolean;          // external spacing
    alignment: boolean;       // flex, grid, absolute
  };
  typography: {
    fontFamily: boolean;
    fontSize: boolean;
    fontWeight: boolean;
    lineHeight: boolean;
    letterSpacing: boolean;
    textAlign: boolean;
  };
  visuals: {
    backgroundColor: boolean;
    border: boolean;          // width, style, color, radius
    boxShadow: boolean;
    opacity: boolean;
  };
  states: {
    hover: boolean;
    active: boolean;
    focus: boolean;
    disabled: boolean;
    error: boolean;
  };
  responsive: {
    mobile: boolean;
    tablet: boolean;
    desktop: boolean;
  };
  accessibility: {
    contrast: boolean;        // WCAG AA
    focusVisible: boolean;
    ariaLabels: boolean;
    keyboardNav: boolean;
  };
}

function checkFidelity(inspection: UIInspectionChecklist): number {
  const items = Object.values(inspection).flatMap(category =>
    Object.values(category)
  );
  const total = items.length;
  const passed = items.filter(Boolean).length;
  return Math.round((passed / total) * 100);
}
```markdown

### Densidade de Informação

Produtos enterprise geralmente precisam de mais densidade que produtos B2C.

```typescript
