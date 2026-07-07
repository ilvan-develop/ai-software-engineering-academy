# Módulo 07 — Design System: Consistência em Escala

**Um Design System não é um projeto. É um produto que serve outros produtos.**

---

## 1. O que é Design System

Design System é um **conjunto integrado de padrões, componentes, diretrizes e ferramentas** que orientam a criação de interfaces digitais de forma consistente e escalável.

### Design System vs Style Guide vs Component Library

```text
Style Guide:                    Component Library:              Design System:
"Guia de estilos"               "Biblioteca de componentes"    "Sistema integrado"
─────────────────────           ─────────────────────           ────────────────────
Cores, tipografia,              Botões, inputs, modais,         Tudo acima +
grid, regras de uso             tabelas, cards                  processos, governance,
                                                                documentação,
─ Estático                      ─ Dinâmico                      tooling, princípios
─ PDF/doc                       ─ npm package                   ─ Ecossistema vivo
─ "O que usar"                  ─ "O que implementar"           ─ "Como pensar"

Exemplo:                        Exemplo:                        Exemplo:
Manual de marca                 Material UI                     Shopify Polaris
```markdown

### Propósito

```typescript
interface DesignSystemPurpose {
  consistencia:  'Mesma aparência e comportamento em todo o ecossistema';
  eficiencia:    'Devs e designers produzem mais rápido, sem recriar o óbvio';
  escalabilidade:'Novos produtos/heranças adotam o sistema sem retrabalho';
  qualidade:     'Componentes testados, acessíveis, documentados';
  colaboracao:   'Linguagem comum entre devs, designers, PMs, QA';
}
```text

> "Design Systems are how we scale design decisions across an organization." — Nathan Curtis

---

## 2. Atomic Design

Criado por **Brad Frost**, o Atomic Design é uma metodologia que divide interfaces em **níveis hierárquicos** de complexidade.

### Os 5 níveis

```text
Átomos ─→ Moléculas ─→ Organismos ─→ Templates ─→ Páginas
  │            │             │             │            │
  │          Combina       Junta         Define       Aplica
  │          átomos        moléculas     layout       conteúdo
  ▼            ▼             ▼             ▼            ▼
Botão      Input +       Formulário    Página de     Página de
Ícone      Label +       + Header +    cadastro      cadastro
Label      Error =       Sidebar +     (vazia,       (com dados
Tag        Campo de      Footer =      estrutura)    reais)
Cor        texto         Página
Tipografia
Espaçamento
```markdown

#### Átomos

```typescript
// Átomo: Label
interface LabelProps {
  text: string;
  variant: 'default' | 'required' | 'optional';
  size: 'sm' | 'md';
}

function Label({ text, variant, size }: LabelProps) {
  const variants = {
    default: 'text-gray-700',
    required: 'text-red-600 after:content-["*"] after:ml-0.5',
    optional: 'text-gray-400',
  };
  return (
    <span className={`${variants[variant]} text-${size === 'sm' ? 'xs' : 'sm'} font-medium`}>
      {text}
    </span>
  );
}
```markdown

#### Moléculas

```typescript
// Molécula: Campo de texto (Label + Input + ErrorMessage)
interface TextFieldProps {
  label: string;
  name: string;
  value: string;
  onChange: (value: string) => void;
  error?: string;
  required?: boolean;
}

function TextField({ label, name, value, onChange, error, required }: TextFieldProps) {
  return (
    <div className="flex flex-col gap-1.5">
      <Label text={label} variant={required ? 'required' : 'default'} size="md" />
      <Input
        name={name}
        value={value}
        onChange={onChange}
        hasError={!!error}
      />
      {error && <ErrorMessage text={error} />}
    </div>
  );
}
```text

#### Organismos

```typescript
// Organismo: Formulário de cadastro
interface SignupFormProps {
  onSubmit: (data: SignupData) => Promise<void>;
}

function SignupForm({ onSubmit }: SignupFormProps) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  return (
    <form onSubmit={(e) => { e.preventDefault(); onSubmit({ email, password }); }}
      className="flex flex-col gap-4 max-w-md">
      <TextField label="Email" name="email" value={email} onChange={setEmail} required />
      <TextField label="Senha" name="password" value={password} onChange={setPassword} required />
      <Button type="submit" variant="primary" fullWidth>Cadastrar</Button>
    </form>
  );
}
```markdown

#### Templates e Páginas

```typescript
// Template: estrutura da página (sem dados reais)
function AuthTemplate({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="w-full max-w-md p-8 bg-white rounded-xl shadow-sm">
        <Logo />
        {children}
      </div>
    </div>
  );
}

// Página: template + dados reais
function SignupPage() {
  return (
    <AuthTemplate>
      <h1 className="text-2xl font-bold mb-6">Crie sua conta</h1>
      <SignupForm onSubmit={handleSignup} />
    </AuthTemplate>
  );
}
```text

### Por que Atomic Design no Enterprise?

```text
Sem Atomic Design:                         Com Atomic Design:
"Onde está o botão primary?"               "Button: variant=primary"
"Este input tem o mesmo estilo             "Input segue o Field token"
  que aquele?"                               (sempre consistente)
"Este formulário quebrou porque            "Mudei o Input, todos os
  mudei o Input em 10 lugares"               formulários atualizam"
```markdown

---

## 3. Design Tokens

Design Tokens são as **variáveis visuais** do sistema. Eles abstraem decisões de design em valores únicos e reutilizáveis.

### Definição em TypeScript

```typescript
// tokens/colors.ts
export const colors = {
  brand: {
    primary:    { 50: '#eff6ff', 100: '#dbeafe', 200: '#bfdbfe',
                  300: '#93c5fd', 400: '#60a5fa', 500: '#3b82f6',
                  600: '#2563eb', 700: '#1d4ed8', 800: '#1e40af',
                  900: '#1e3a8a', 950: '#172554' },
    secondary:  { 50: '#faf5ff', 100: '#f3e8ff', 500: '#8b5cf6',
                  600: '#7c3aed', 700: '#6d28d9' },
  },
  semantic: {
    success: '#10b981',
    warning: '#f59e0b',
    error:   '#ef4444',
    info:    '#3b82f6',
  },
  neutral: {
    white:  '#ffffff',
    50:     '#f9fafb',
    100:    '#f3f4f6',
    200:    '#e5e7eb',
    300:    '#d1d5db',
    400:    '#9ca3af',
    500:    '#6b7280',
    600:    '#4b5563',
    700:    '#374151',
    800:    '#1f2937',
    900:    '#111827',
    black:  '#000000',
  },
} as const;

export type ColorToken = keyof typeof colors.semantic;
```markdown

### Tipografia

```typescript
// tokens/typography.ts
export const typography = {
  fontFamily: {
    sans: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
    mono: "'JetBrains Mono', 'Fira Code', monospace",
  },
  scale: {
    'display-xl': { fontSize: '4.5rem', lineHeight: '5rem', fontWeight: 700, letterSpacing: '-0.02em' },
    'display-lg':  { fontSize: '3.75rem', lineHeight: '4.25rem', fontWeight: 700, letterSpacing: '-0.02em' },
    'display':     { fontSize: '3rem', lineHeight: '3.5rem', fontWeight: 700, letterSpacing: '-0.01em' },
    'heading-xl':  { fontSize: '2.25rem', lineHeight: '2.75rem', fontWeight: 600, letterSpacing: '-0.01em' },
    'heading-lg':  { fontSize: '1.875rem', lineHeight: '2.375rem', fontWeight: 600 },
    'heading':     { fontSize: '1.5rem', lineHeight: '2rem', fontWeight: 600 },
    'heading-sm':  { fontSize: '1.25rem', lineHeight: '1.75rem', fontWeight: 600 },
    'body-lg':     { fontSize: '1.125rem', lineHeight: '1.75rem', fontWeight: 400 },
    'body':        { fontSize: '1rem', lineHeight: '1.5rem', fontWeight: 400 },
    'body-sm':     { fontSize: '0.875rem', lineHeight: '1.25rem', fontWeight: 400 },
    'caption':     { fontSize: '0.75rem', lineHeight: '1rem', fontWeight: 400 },
    'overline':    { fontSize: '0.75rem', lineHeight: '1rem', fontWeight: 500, textTransform: 'uppercase', letterSpacing: '0.08em' },
  },
} as const;
```text

### Spacing

```typescript
// tokens/spacing.ts
export const spacing = {
  0:   '0px',
  0.5: '2px',
  1:   '4px',
  2:   '8px',
  3:   '12px',
  4:   '16px',
  5:   '20px',
  6:   '24px',
  8:   '32px',
  10:  '40px',
  12:  '48px',
  16:  '64px',
  20:  '80px',
  24:  '96px',
} as const;

export type SpacingToken = keyof typeof spacing;
```markdown

### Shadows, Border Radius e Breakpoints

```typescript
// tokens/effects.ts
export const shadows = {
  none:   'none',
  sm:     '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
  md:     '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1)',
  lg:     '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1)',
  xl:     '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1)',
} as const;

export const borderRadius = {
  none:   '0px',
  sm:     '4px',
  md:     '8px',
  lg:     '12px',
  xl:     '16px',
  full:   '9999px',
} as const;

// tokens/breakpoints.ts
export const breakpoints = {
  sm: 640,
  md: 768,
  lg: 1024,
  xl: 1280,
  '2xl': 1536,
} as const;

// Uso: breakpoints como media queries
export const mediaQueries = {
  sm:  `@media (min-width: ${breakpoints.sm}px)`,
  md:  `@media (min-width: ${breakpoints.md}px)`,
  lg:  `@media (min-width: ${breakpoints.lg}px)`,
  xl:  `@media (min-width: ${breakpoints.xl}px)`,
  '2xl': `@media (min-width: ${breakpoints['2xl']}px)`,
} as const;
```text

### CSS Custom Properties a partir dos Tokens

```typescript
// tokens/toCSS.ts
import { colors } from './colors';
import { spacing } from './spacing';
import { shadows, borderRadius } from './effects';

export function generateCSSVariables(): string {
  let css = ':root {\n';

  // Colors
  for (const [brand, shades] of Object.entries(colors.brand)) {
    for (const [shade, value] of Object.entries(shades)) {
      css += `  --color-${brand}-${shade}: ${value};\n`;
    }
  }

  // Spacing
  for (const [key, value] of Object.entries(spacing)) {
    css += `  --spacing-${key}: ${value};\n`;
  }

  // Shadows
  for (const [key, value] of Object.entries(shadows)) {
    css += `  --shadow-${key}: ${value};\n`;
  }

  // Border radius
  for (const [key, value] of Object.entries(borderRadius)) {
    css += `  --radius-${key}: ${value};\n`;
  }

  css += '}\n';
  return css;
}

// Saída gerada:
// :root {
//   --color-primary-50: #eff6ff;
//   --spacing-4: 16px;
//   --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
//   --radius-md: 8px;
// }
```markdown

---

## 4. Componentes

Componentes são a **implementação concreta** dos tokens. Cada componente deve ser:
- **Padronizado** — props consistentes entre componentes
- **Documentado** — spec, variantes, exemplos
- **Acessível** — ARIA, teclado, contraste
- **Testado** — unitário, visual, acessibilidade

### Botão

```typescript
// components/Button/Button.tsx
import { ButtonHTMLAttributes, forwardRef } from 'react';

type ButtonVariant = 'primary' | 'secondary' | 'outline' | 'ghost' | 'danger';
type ButtonSize = 'sm' | 'md' | 'lg';

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
  size?: ButtonSize;
  loading?: boolean;
  fullWidth?: boolean;
  leftIcon?: React.ReactNode;
  rightIcon?: React.ReactNode;
}

const variantStyles: Record<ButtonVariant, string> = {
  primary:   'bg-[var(--color-primary-600)] text-white hover:bg-[var(--color-primary-700)] focus:ring-[var(--color-primary-500)]',
  secondary: 'bg-gray-100 text-gray-900 hover:bg-gray-200 focus:ring-gray-500',
  outline:   'border border-gray-300 text-gray-700 hover:bg-gray-50 focus:ring-[var(--color-primary-500)]',
  ghost:     'text-gray-600 hover:bg-gray-100 focus:ring-gray-500',
  danger:    'bg-[var(--color-semantic-error)] text-white hover:bg-red-700 focus:ring-red-500',
};

const sizeStyles: Record<ButtonSize, string> = {
  sm: 'px-3 py-1.5 text-sm gap-1.5',
  md: 'px-4 py-2 text-sm gap-2',
  lg: 'px-6 py-3 text-base gap-2',
};

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ variant = 'primary', size = 'md', loading, fullWidth, leftIcon, rightIcon, children, disabled, className, ...props }, ref) => {
    return (
      <button
        ref={ref}
        disabled={disabled || loading}
        className={`
          inline-flex items-center justify-center font-medium rounded-[var(--radius-md)]
          transition-all duration-150
          focus:outline-none focus:ring-2 focus:ring-offset-2
          disabled:opacity-50 disabled:cursor-not-allowed
          ${variantStyles[variant]}
          ${sizeStyles[size]}
          ${fullWidth ? 'w-full' : ''}
          ${className ?? ''}
        `.trim()}
        {...props}
      >
        {loading ? <Spinner /> : leftIcon}
        {children}
        {rightIcon}
      </button>
    );
  }
);
```text

### Input

```typescript
// components/Input/Input.tsx
import { InputHTMLAttributes, forwardRef } from 'react';

interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  label: string;
  error?: string;
  hint?: string;
  leftElement?: React.ReactNode;
  rightElement?: React.ReactNode;
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ label, error, hint, leftElement, rightElement, id, className, ...props }, ref) => {
    const inputId = id ?? `input-${label.toLowerCase().replace(/\s+/g, '-')}`;

    return (
      <div className="flex flex-col gap-1.5">
        <label htmlFor={inputId} className="text-sm font-medium text-gray-700">
          {label}
          {props.required && <span className="text-red-500 ml-0.5">*</span>}
        </label>
        <div
          className={`
            flex items-center border rounded-[var(--radius-md)] transition-all
            ${error
              ? 'border-red-500 focus-within:ring-red-500'
              : 'border-gray-300 focus-within:ring-[var(--color-primary-500)]'
            }
            ${props.disabled ? 'bg-gray-50 cursor-not-allowed' : 'bg-white'}
            focus-within:ring-2
          `.trim()}
        >
          {leftElement && <span className="pl-3 text-gray-400">{leftElement}</span>}
          <input
            ref={ref}
            id={inputId}
            className={`
              w-full px-3 py-2 text-sm bg-transparent outline-none
              ${props.disabled ? 'text-gray-400' : 'text-gray-900'}
              placeholder:text-gray-400
            `.trim()}
            aria-invalid={!!error}
            aria-describedby={error ? `${inputId}-error` : hint ? `${inputId}-hint` : undefined}
            {...props}
          />
          {rightElement && <span className="pr-3 text-gray-400">{rightElement}</span>}
        </div>
        {error && <span id={`${inputId}-error`} className="text-xs text-red-500">{error}</span>}
        {hint && !error && <span id={`${inputId}-hint`} className="text-xs text-gray-500">{hint}</span>}
      </div>
    );
  }
);
```markdown

### Modal

```typescript
// components/Modal/Modal.tsx
import { useEffect, useRef } from 'react';

interface ModalProps {
  open: boolean;
  onClose: () => void;
  title: string;
  size?: 'sm' | 'md' | 'lg' | 'xl';
  children: React.ReactNode;
  footer?: React.ReactNode;
}

const sizeStyles = {
  sm: 'max-w-sm',
  md: 'max-w-lg',
  lg: 'max-w-2xl',
  xl: 'max-w-4xl',
};

export function Modal({ open, onClose, title, size = 'md', children, footer }: ModalProps) {
  const overlayRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!open) return;
    const handleEsc = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    document.addEventListener('keydown', handleEsc);
    document.body.style.overflow = 'hidden';
    return () => {
      document.removeEventListener('keydown', handleEsc);
      document.body.style.overflow = '';
    };
  }, [open, onClose]);

  if (!open) return null;

  return (
    <div
      ref={overlayRef}
      className="fixed inset-0 z-50 flex items-center justify-center p-4"
      onClick={(e) => { if (e.target === overlayRef.current) onClose(); }}
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
    >
      <div className="fixed inset-0 bg-black/50 backdrop-blur-sm" aria-hidden="true" />
      <div className={`relative bg-white rounded-xl shadow-xl w-full ${sizeStyles[size]} p-6 animate-in fade-in zoom-in duration-200`}>
        <div className="flex items-center justify-between mb-4">
          <h2 id="modal-title" className="text-lg font-semibold text-gray-900">{title}</h2>
          <button onClick={onClose} className="p-1 text-gray-400 hover:text-gray-600 rounded-lg hover:bg-gray-100 transition-colors" aria-label="Fechar">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M15 5L5 15M5 5l10 10" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/></svg>
          </button>
        </div>
        <div className="mb-6 text-sm text-gray-600">{children}</div>
        {footer && (
          <div className="flex items-center justify-end gap-3 pt-4 border-t border-gray-100">
            {footer}
          </div>
        )}
      </div>
    </div>
  );
}
```text

### Tabela

```typescript
// components/Table/Table.tsx
interface Column<T> {
  key: string;
  header: string;
  render: (item: T) => React.ReactNode;
  sortable?: boolean;
  width?: string;
  align?: 'left' | 'center' | 'right';
}

interface TableProps<T> {
  columns: Column<T>[];
  data: T[];
  loading?: boolean;
  emptyMessage?: string;
  onRowClick?: (item: T) => void;
  sortable?: boolean;
}

export function Table<T extends Record<string, unknown>>({
  columns, data, loading, emptyMessage = 'Nenhum registro encontrado',
  onRowClick, sortable,
}: TableProps<T>) {
  const [sortKey, setSortKey] = useState<string | null>(null);
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('asc');

  const sorted = useMemo(() => {
    if (!sortKey) return data;
    return [...data].sort((a, b) => {
      const aVal = a[sortKey];
      const bVal = b[sortKey];
      if (aVal < bVal) return sortDir === 'asc' ? -1 : 1;
      if (aVal > bVal) return sortDir === 'asc' ? 1 : -1;
      return 0;
    });
  }, [data, sortKey, sortDir]);

  const handleSort = (key: string) => {
    if (sortKey === key) {
      setSortDir(d => d === 'asc' ? 'desc' : 'asc');
    } else {
      setSortKey(key);
      setSortDir('asc');
    }
  };

  return (
    <div className="overflow-x-auto border border-gray-200 rounded-[var(--radius-lg)]">
      <table className="w-full text-sm">
        <thead>
          <tr className="bg-gray-50 border-b border-gray-200">
            {columns.map(col => (
              <th
                key={col.key}
                className={`px-4 py-3 font-medium text-gray-600 text-${col.align || 'left'} ${col.width ?? ''}`}
              >
                {col.sortable && sortable !== false ? (
                  <button className="flex items-center gap-1 hover:text-gray-900" onClick={() => handleSort(col.key)}>
                    {col.header}
                    {sortKey === col.key && (
                      <span className="text-xs">{sortDir === 'asc' ? '▲' : '▼'}</span>
                    )}
                  </button>
                ) : col.header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {loading ? (
            Array.from({ length: 3 }).map((_, i) => (
              <tr key={i} className="animate-pulse">
                {columns.map(col => (
                  <td key={col.key} className="px-4 py-3">
                    <div className="h-4 bg-gray-200 rounded w-3/4" />
                  </td>
                ))}
              </tr>
            ))
          ) : sorted.length === 0 ? (
            <tr>
              <td colSpan={columns.length} className="px-4 py-8 text-center text-gray-500">
                {emptyMessage}
              </td>
            </tr>
          ) : (
            sorted.map((item, i) => (
              <tr
                key={i}
                className={`border-b border-gray-100 last:border-0 hover:bg-gray-50 transition-colors ${onRowClick ? 'cursor-pointer' : ''}`}
                onClick={() => onRowClick?.(item)}
              >
                {columns.map(col => (
                  <td key={col.key} className={`px-4 py-3 text-${col.align || 'left'}`}>
                    {col.render(item)}
                  </td>
                ))}
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}
```sql

### Select

```typescript
// components/Select/Select.tsx
interface SelectOption {
  label: string;
  value: string;
  disabled?: boolean;
}

interface SelectProps {
  label: string;
  options: SelectOption[];
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  error?: string;
  required?: boolean;
  disabled?: boolean;
}

export function Select({ label, options, value, onChange, placeholder, error, required, disabled }: SelectProps) {
  const selectId = `select-${label.toLowerCase().replace(/\s+/g, '-')}`;

  return (
    <div className="flex flex-col gap-1.5">
      <label htmlFor={selectId} className="text-sm font-medium text-gray-700">
        {label}
        {required && <span className="text-red-500 ml-0.5">*</span>}
      </label>
      <select
        id={selectId}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        disabled={disabled}
        className={`
          w-full px-3 py-2 text-sm bg-white border rounded-[var(--radius-md)] transition-all
          ${error ? 'border-red-500' : 'border-gray-300'}
          ${disabled ? 'bg-gray-50 text-gray-400 cursor-not-allowed' : 'text-gray-900'}
          focus:outline-none focus:ring-2 ${error ? 'focus:ring-red-500' : 'focus:ring-[var(--color-primary-500)]'}
        `.trim()}
        required={required}
        aria-invalid={!!error}
      >
        {placeholder && <option value="" disabled>{placeholder}</option>}
        {options.map(opt => (
          <option key={opt.value} value={opt.value} disabled={opt.disabled}>
            {opt.label}
          </option>
        ))}
      </select>
      {error && <span className="text-xs text-red-500">{error}</span>}
    </div>
  );
}
```text

---

## 5. Documentação

Documentação é o que **transforma uma biblioteca de componentes em um Design System**.

### Storybook

Storybook é a ferramenta mais popular para documentar, testar e explorar componentes visualmente.

```typescript
// components/Button/Button.stories.ts
import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta: Meta<typeof Button> = {
  title: 'Components/Button',
  component: Button,
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'secondary', 'outline', 'ghost', 'danger'],
    },
    size: { control: 'select', options: ['sm', 'md', 'lg'] },
    loading: { control: 'boolean' },
    disabled: { control: 'boolean' },
    fullWidth: { control: 'boolean' },
    children: { control: 'text' },
  },
  tags: ['autodocs'],
};

export default meta;
type Story = StoryObj<typeof Button>;

export const Primary: Story = {
  args: {
    variant: 'primary',
    children: 'Salvar',
    size: 'md',
  },
};

export const Secondary: Story = {
  args: {
    variant: 'secondary',
    children: 'Cancelar',
  },
};

export const Danger: Story = {
  args: {
    variant: 'danger',
    children: 'Excluir',
  },
};

export const Loading: Story = {
  args: {
    variant: 'primary',
    children: 'Salvando...',
    loading: true,
  },
};

export const Disabled: Story = {
  args: {
    variant: 'primary',
    children: 'Salvar',
    disabled: true,
  },
};

export const WithIcons: Story = {
  args: {
    variant: 'primary',
    children: 'Próximo',
    rightIcon: <span>→</span>,
  },
};

export const FullWidth: Story = {
  args: {
    variant: 'primary',
    children: 'Criar conta',
    fullWidth: true,
  },
};
```markdown

### Specs e Guidelines

Cada componente deve ter uma **especificação técnica** (spec) e **diretrizes de uso** (guidelines).

```markdown
<!-- Button/Button.spec.md -->

## Button — Especificação Técnica

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| variant | `'primary' \| 'secondary' \| 'outline' \| 'ghost' \| 'danger'` | `'primary'` | Estilo visual do botão |
| size | `'sm' \| 'md' \| 'lg'` | `'md'` | Tamanho do botão |
| loading | `boolean` | `false` | Exibe spinner e desabilita |
| disabled | `boolean` | `false` | Desabilita interação |
| fullWidth | `boolean` | `false` | Ocupa 100% do container |
| leftIcon | `ReactNode` | — | Ícone à esquerda |
| rightIcon | `ReactNode` | — | Ícone à direita |

### Estados

| State | Visual | Acessibilidade |
|-------|--------|---------------|
| Default | Cor sólida | Focus visible |
| Hover | 1 shade mais escuro | Cursor: pointer |
| Focus | Ring 2px + offset 2px | Outline visível |
| Active | 2 shades mais escuro | — |
| Disabled | Opacity 50% | aria-disabled |
| Loading | Spinner no lugar do ícone | aria-busy="true" |

### Comportamento

- **Teclado**: Enter/Space aciona o click
- **Loading**: Botão não responde a cliques
- **Full width**: Útil em mobile, raro em desktop
```text

### Playground Interativo

```typescript
// No Storybook, o próprio docs gera um playground automático:
// controls interativos para testar todas as props.
// 
// Exemplo de addons:
// - @storybook/addon-controls: manipular props
// - @storybook/addon-a11y: auditoria de acessibilidade
// - @storybook/addon-interactions: testar interações
// - storybook-addon-designs: embed do Figma
```markdown

---

## 6. Versionamento

Design Systems evoluem. Versionamento garante que **mudanças sejam previsíveis e seguras**.

### SemVer (Semantic Versioning)

```text
MAJOR.MINOR.PATCH

MAJOR (1.x.x → 2.0.0):
  Breaking changes — componente renomeado, prop removida, token alterado
  Ex: Button: `variant="primary"` → `variant="filled"`

MINOR (x.1.x → x.2.0):
  Novas funcionalidades — novo componente, nova variante, nova prop
  Ex: Novo componente `Tooltip`, prop `size` no Modal

PATCH (x.x.1 → x.x.2):
  Correções — bug fix, acessibilidade, performance
  Ex: Corrigir contraste do Button danger, ARIA label no Modal
```markdown

### Breaking Changes

```typescript
// ❌ BREAKING: renomear prop sem deprecação
interface ButtonProps {
  appearance?: 'primary' | 'secondary'; // antes era 'variant'
}

// ✅ CORRETO: deprecação gradual
interface ButtonProps {
  /** @deprecated Use `variant` instead */
  appearance?: 'primary' | 'secondary';
  variant?: 'primary' | 'secondary' | 'outline';
}

// Log de deprecação em runtime
if (appearance && !variant) {
  console.warn('[DS] Button: `appearance` is deprecated. Use `variant` instead.');
  variant = appearance;
}
```text

### Migration Guides

```markdown
# Migration Guide: v1 → v2

## Breaking Changes

### Button: `appearance` → `variant`

**Antes:**
```tsx
<Button appearance="primary" />
```tsx

**Depois:**
```text
<Button variant="primary" />
```bash

**Codemod:**
```text
npx @acme/ds-codemod button-appearance-to-variant
```text

### Modal: sizes renomeados

| v1 | v2 |
|----|----|
| `size="small"` | `size="sm"` |
| `size="medium"` | `size="md"` |
| `size="large"` | `size="lg"` |
```markdown

### Changelog

```markdown
# Changelog

## [2.1.0] — 2026-06-15

### Added
- Novo componente: `Tooltip`
- Button: nova prop `leftIcon` e `rightIcon`
- Modal: nova variante `size="xl"`

### Changed
- Input: cor de foco agora usa token primary ao invés de blue-500 fixo
- Table: sortable agora é opcional (default: true)

### Fixed
- Modal: fechamento com Escape não funcionava em alguns browsers
- Select: placeholder não aparecia quando value era vazio
- Button: contraste do variant danger estava abaixo de WCAG AA

## [2.0.0] — 2026-05-20

### Breaking
- Button: `appearance` → `variant`
- Modal: `size="small"|"medium"|"large"` → `size="sm"|"md"|"lg"`
- Tokens: `--color-blue-*` → `--color-primary-*`
```bash

---

## 7. Consumo em Projetos

### Publicação como npm Package

```json
// package.json (do Design System)
{
  "name": "@empresa/design-system",
  "version": "2.1.0",
  "main": "dist/cjs/index.js",
  "module": "dist/esm/index.js",
  "types": "dist/types/index.d.ts",
  "exports": {
    ".": {
      "import": "./dist/esm/index.js",
      "require": "./dist/cjs/index.js",
      "types": "./dist/types/index.d.ts"
    },
    "./styles.css": "./dist/styles.css",
    "./tokens": "./dist/tokens/index.js"
  },
  "sideEffects": false,
  "files": ["dist", "README.md", "LICENSE"]
}
```text

### Tree-shaking

Para que o **tree-shaking** funcione, os componentes devem ser exportados individualmente:

```typescript
// index.ts — barrel export
export { Button } from './components/Button/Button';
export { Input } from './components/Input/Input';
export { Modal } from './components/Modal/Modal';
export { Table } from './components/Table/Table';
export { Select } from './components/Select/Select';

// Tokens
export { colors } from './tokens/colors';
export { typography } from './tokens/typography';
export { spacing } from './tokens/spacing';
export { shadows, borderRadius } from './tokens/effects';
```text

```typescript
// Consumo com tree-shaking
import { Button } from '@empresa/design-system';
// ✅ Apenas Button entra no bundle (desde que sideEffects: false)
```text

### Theming

```typescript
// components/ThemeProvider.tsx
import { createContext, useContext } from 'react';

interface Theme {
  colors: {
    primary: typeof import('../tokens/colors').colors.brand.primary;
    semantic: typeof import('../tokens/colors').colors.semantic;
  };
  spacing: typeof import('../tokens/spacing').spacing;
  borderRadius: typeof import('../tokens/effects').borderRadius;
}

const defaultTheme: Theme = {
  colors: {
    primary: { 500: '#3b82f6', 600: '#2563eb', /* ... */ },
    semantic: { success: '#10b981', error: '#ef4444', /* ... */ },
  },
  spacing: { 4: '16px', /* ... */ },
  borderRadius: { md: '8px', /* ... */ },
};

const ThemeContext = createContext<Theme>(defaultTheme);

export function ThemeProvider({ theme, children }: { theme?: Partial<Theme>; children: React.ReactNode }) {
  const merged = { ...defaultTheme, ...theme };
  return (
    <ThemeContext.Provider value={merged}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme(): Theme {
  return useContext(ThemeContext);
}
```markdown

### Customização (Override via CSS Custom Properties)

```css
/* Projeto: overrides.css */
:root {
  --color-primary-600: #7c3aed;  /* roxo ao invés de azul */
  --color-primary-700: #6d28d9;
  --radius-md: 4px;
  --font-family-sans: 'Roboto', sans-serif;
}
```text

```typescript
// Uso
import '@empresa/design-system/styles.css';
import './overrides.css';
```markdown

---

## 8. Manutenção

### Governance

```text
Equipe de Design System (DS Squad):

┌─────────────────────────────────────────────────────┐
│                     DS SQUAD                         │
├───────────────────┬─────────────────────────────────┤
│  Core Team        │  Contributors                    │
│  (dedicado)       │  (de cada squad)                 │
├───────────────────┼─────────────────────────────────┤
│  Design Lead      │  Designers de cada produto       │
│  Engineering Lead │  Devs de frontend dos squads     │
│  Developer        │  QA engineers                    │
│  Design Ops       │  Accessibility specialists       │
└───────────────────┴─────────────────────────────────┘

Rituais:
- Weekly sync (DS Squad)
- Monthly showcase (novos componentes)
- Quarterly review (ROI, métricas)
- Voting on RFCs (propostas de mudança)
```markdown

### Contribuição

```markdown
# CONTRIBUTING.md (extrato)

## Como contribuir com um novo componente

1. **RFC**: Abra uma RFC no repositório do DS
   - Problema que resolve
   - Alternativas consideradas
   - Mockup / protótipo
2. **Review**: DS Squad revisa a RFC em até 1 semana
3. **Implementação**:
   - Componente + stories + specs + testes
   - Tokens se necessário
   - Documentação em PT-BR e EN
4. **Code Review**:
   - 2 approvals da DS Squad
   - a11y review obrigatório
5. **Release**: DS Squad faz o release

### Critérios de aceite

- [ ] Componente segue os princípios do DS
- [ ] Suporta todos os estados (default, hover, focus, disabled, error, loading)
- [ ] Acessível (ARIA, teclado, contraste WCAG AA)
- [ ] Testado (unitário + visual + a11y)
- [ ] Documentado (Storybook + spec.md)
- [ ] Exemplo de uso real em projeto consumidor
```text

### Code Review de Design

```typescript
// Checklist de review de design no PR

interface DesignReviewChecklist {
  tokens: [
    'Usa tokens de cor (não hex fixo)',
    'Usa tokens de spacing (não px fixo)',
    'Usa type scale (não font-size arbitrário)',
    'Usa shadow tokens (não box-shadow manual)',
  ];
  acessibilidade: [
    'Contraste WCAG AA (4.5:1 texto normal)',
    'Focus visible em todos os elementos interativos',
    'ARIA labels em elementos sem texto',
    'Suporte a navegação por teclado',
    'Testado com leitor de tela (NVDA/VoiceOver)',
  ];
  responsividade: [
    'Funciona em mobile (320px) até desktop (1920px)',
    'Touch targets >= 44px',
    'Texto não cortado em nenhum breakpoint',
  ];
  performance: [
    'Nenhum re-render desnecessário',
    'Imagens com lazy loading se aplicável',
    'Bundle size < 5KB (gzip) para componente simples',
  ];
}
```markdown

### Changelog Automatizado

```typescript
// .github/release.yml
changelog:
  categories:
    - title: '🚨 Breaking Changes'
      labels: ['breaking']
    - title: '✨ Novos Componentes'
      labels: ['new-component']
    - title: '🚀 Novas Funcionalidades'
      labels: ['enhancement']
    - title: '🐛 Bug Fixes'
      labels: ['bug']
    - title: '♿ Acessibilidade'
      labels: ['a11y']
    - title: '📖 Documentação'
      labels: ['documentation']
    - title: '🔧 Manutenção'
      labels: ['chore', 'dependencies']
```text

---

## 9. Design System no Enterprise

### Escalabilidade

```text
Sem DS:                          Com DS:
┌───┐ ┌───┐ ┌───┐               ┌──────────────────────┐
│P1  │ │P2  │ │P3  │              │      Design System   │
│    │ │    │ │    │              │                      │
│azul│ │azul│ │roxo│              │ primary: azul        │
│8px │ │12px│ │8px │              │ spacing: 8px base    │
│sm  │ │md  │ │sm  │              │ radius: 8px          │
└───┘ └───┘ └───┘               └──────────────────────┘
                                      │     │     │
                                  ┌───┐ ┌───┐ ┌───┐
                                  │P1 │ │P2 │ │P3 │
                                  │   │ │   │ │   │
                                  │ok │ │ok │ │ok │
                                  └───┘ └───┘ └───┘
```markdown

### Consistência

```typescript
// Antes do DS: cada squad tinha seu próprio "jeito"
const SquadA = () => <button className="btn-save">Salvar</button>;
const SquadB = () => <button className="submit-button">Salvar</button>;
const SquadC = () => <div class="action-btn" onclick={save}>Salvar</div>;

// Depois do DS: todos usam o mesmo componente
const SquadA = () => <Button variant="primary">Salvar</Button>;
const SquadB = () => <Button variant="primary">Salvar</Button>;
const SquadC = () => <Button variant="primary">Salvar</Button>;
```markdown

### Eficiência e ROI

```text
Métricas de ROI de Design System:

┌─────────────────────────────────────────────────────┐
│  Antes do DS          │  Depois do DS               │
├───────────────────────┼─────────────────────────────┤
│  Tela simples: 3 dias │  Tela simples: 1 dia         │
│  Tela complexa: 5d   │  Tela complexa: 2.5d         │
│  Onboarding: 2 meses │  Onboarding: 2 semanas        │
│  Design review: 3h   │  Design review: 30min         │
│  Bugs de UI: 15/mês  │  Bugs de UI: 3/mês            │
└─────────────────────────────────────────────────────┘

Cálculo de ROI:
  5 squads × 4 devs × 1 tela/semana × R$ 10.000/dia
  → Cada tela custa R$ 30.000 (3 dias)
  → Com DS: R$ 10.000 (1 dia)
  → Economia: R$ 20.000/tela × 20 telas/mês × 12 meses
  → ROI: R$ 4.8M/ano

  Custo do DS Squad: 4 pessoas × R$ 250K = R$ 1M/ano
  Net: R$ 3.8M/ano    (fonte: dados hipotéticos para ilustração)
```markdown

---

## 10. Implementação Prática

Vamos configurar um Design System básico com **React + TypeScript + Storybook + tokens**.

### Setup inicial

```bash
# 1. Criar monorepo
mkdir my-design-system && cd my-design-system
pnpm init

# 2. Instalar dependências
pnpm add react react-dom
pnpm add -D typescript @types/react @types/react-dom
pnpm add -D vite @vitejs/plugin-react
pnpm add -D storybook @storybook/react @storybook/react-vite @storybook/addon-essentials

# 3. Iniciar Storybook
pnpm dlx storybook@latest init --builder=vite

# 4. Instalar tokens via CSS
pnpm add -D @tokens-studio/sd-transforms style-dictionary
```text

### Estrutura de diretórios

```text
my-design-system/
├── tokens/
│   ├── colors.ts
│   ├── typography.ts
│   ├── spacing.ts
│   └── effects.ts
├── src/
│   ├── components/
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.stories.ts
│   │   │   └── Button.spec.md
│   │   ├── Input/
│   │   ├── Modal/
│   │   ├── Table/
│   │   └── Select/
│   ├── index.ts
│   └── styles.css
├── .storybook/
│   ├── main.ts
│   └── preview.ts
├── package.json
└── tsconfig.json
```markdown

### Configuração do Vite para build

```typescript
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { resolve } from 'path';

export default defineConfig({
  plugins: [react()],
  build: {
    lib: {
      entry: resolve(__dirname, 'src/index.ts'),
      name: 'MyDesignSystem',
      formats: ['es', 'cjs'],
      fileName: (format) => `index.${format === 'es' ? 'mjs' : 'cjs'}`,
    },
    rollupOptions: {
      external: ['react', 'react-dom'],
      output: {
        globals: {
          react: 'React',
          'react-dom': 'ReactDOM',
        },
      },
    },
  },
});
```markdown

### Storybook config

```typescript
// .storybook/main.ts
import type { StorybookConfig } from '@storybook/react-vite';

const config: StorybookConfig = {
  stories: ['../src/**/*.stories.@(ts|tsx)'],
  addons: [
    '@storybook/addon-essentials',
    '@storybook/addon-a11y',
    '@storybook/addon-interactions',
  ],
  framework: {
    name: '@storybook/react-vite',
    options: {},
  },
  docs: {
    autodocs: 'tag',
    defaultName: 'Documentação',
  },
};

export default config;
```typescript

```typescript
// .storybook/preview.ts
import type { Preview } from '@storybook/react';
import '../src/styles.css';

const preview: Preview = {
  parameters: {
    controls: { expanded: true },
    a11y: {
      config: {
        rules: [{ id: 'color-contrast', enabled: true }],
      },
    },
  },
  globalTypes: {
    theme: {
      name: 'Theme',
      defaultValue: 'light',
      toolbar: {
        icon: 'circlehollow',
        items: ['light', 'dark'],
      },
    },
  },
};

export default preview;
```markdown

### Estilos base

```css
```
/* src/styles.css */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

*, *::before, *::after {
  box-sizing: border-box;
}

:root {
  --font-family-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --color-primary-50: #eff6ff;
  --color-primary-100: #dbeafe;
  --color-primary-200: #bfdbfe;
  --color-primary-300: #93c5fd;
  --color-primary-400: #60a5fa;
  --color-primary-500: #3b82f6;
  --color-primary-600: #2563eb;
  --color-primary-700: #1d4ed8;
  --color-primary-800: #1e40af;
  --color-primary-900: #1e3a8a;
  --color-primary-950: #172554;
  --color-semantic-success: #10b981;
  --color-semantic-warning: #f59e0b;
  --color-semantic-error: #ef4444;
  --color-semantic-info: #3b82f6;
  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-3: 12px;
  --spacing-4: 16px;
  --spacing-6: 24px;
  --spacing-8: 32px;
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
}

body {
  font-family: var(--font-family-sans);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
