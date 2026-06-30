# Exercícios — Módulo 06

## Exercício 1: Aplicar CRAP em um Card

Dado o componente `UserCard` abaixo, ele viola todos os 4 princípios CRAP. Refatore-o.

```typescript
// ❌ Código com problemas CRAP
function UserCard({ name, role, email }: { name: string; role: string; email: string }) {
  return (
    <div style={{ border: '1px solid #ccc', padding: 10 }}>
      <h4 style={{ fontSize: 14, color: '#666', marginLeft: 8 }}>{name}</h4>
      <p style={{ fontSize: 16, color: '#333', marginRight: 20 }}>{role}</p>
      <span style={{ fontSize: 12, color: '#999', marginBottom: 4 }}>Contato:</span>
      <p style={{ fontSize: 14, color: '#1A73E8', marginTop: 16 }}>{email}</p>
    </div>
  );
}
```

Tarefas:
1. Identifique qual(is) princípio(s) CRAP cada problema viola
2. Refatore o componente aplicando os 4 princípios corretamente
3. Use a escala de espaçamento do módulo

---

## Exercício 2: Criar uma paleta de cores funcional

Implemente uma paleta de cores completa para um SaaS de **gestão de estoque industrial**.

Requisitos:
```typescript
interface IndustrialPalette {
  brand: {
    primary: string;
    primaryLight: string;
    primaryDark: string;
  };
  feedback: {
    success: string;
    warning: string;
    error: string;
    info: string;
  };
  neutral: Record<number, string>; // 50, 100, 200, 300, 400, 500, 600, 700, 800, 900
  text: {
    primary: string;
    secondary: string;
    disabled: string;
    inverse: string;
  };
  surface: {
    page: string;
    card: string;
    modal: string;
    sidebar: string;
  };
}
```

Tarefas:
1. Escolha uma cor primária que remeta ao segmento industrial (justifique)
2. Preencha todos os tokens
3. Verifique se o contraste entre `text.primary` e `surface.card` atende WCAG AA
4. Adapte a paleta para dark mode (cores invertidas ou ajustadas)

---

## Exercício 3: Implementar um DataTable component

Implemente um componente `DataTable` genérico em React/TypeScript com:

```typescript
interface Column<T> {
  key: keyof T;
  header: string;
  sortable?: boolean;
  width?: number;
  render?: (value: T[keyof T], row: T) => React.ReactNode;
}

interface DataTableProps<T> {
  columns: Column<T>[];
  data: T[];
  loading?: boolean;
  emptyMessage?: string;
  onSort?: (key: keyof T, direction: 'asc' | 'desc') => void;
  pageSize?: number;
}
```

Requisitos:
1. Estados: **default**, **loading** (skeleton de 3 linhas), **empty** (mensagem + ilustração textual), **error**
2. Suporte a ordenação por coluna (sortable)
3. Suporte a densidade: `comfortable` (48px), `standard` (40px), `compact` (32px)
4. Linhas com `hover` e `striped` alternado
5. Acessibilidade: `role="table"`, `aria-sort` no header, `aria-busy` no loading

---

## Exercício 4: Microinterações — Button Animado

Implemente um botão com microinterações completas:

```typescript
type ButtonVariant = 'primary' | 'secondary' | 'danger' | 'ghost';
type ButtonSize = 'sm' | 'md' | 'lg';

interface AnimatedButtonProps {
  variant: ButtonVariant;
  size: ButtonSize;
  loading?: boolean;
  disabled?: boolean;
  icon?: React.ReactNode;
  children: React.ReactNode;
  onClick: () => void;
}
```

Requisitos de microinteração:
1. `hover`: mudança suave de cor (150ms ease)
2. `active`: scale(0.97) + cor mais escura
3. `focus-visible`: ring de 3px com cor do outline
4. `disabled`: opacidade 0.5, cursor not-allowed, sem interação
5. `loading`: spinner animado substituindo o ícone, botão desabilitado
6. Transições com `transition` CSS para suavidade
7. Acessibilidade: `aria-disabled` quando loading, `aria-label` se só ícone

---

## Exercício 5: Dark Mode Toggle com ThemeProvider

Implemente um sistema de tema com dark mode completo.

```typescript
interface FullTheme {
  mode: 'light' | 'dark';
  colors: {
    background: { primary: string; secondary: string; elevated: string };
    text: { primary: string; secondary: string; disabled: string; inverse: string };
    border: { default: string; hover: string; focus: string };
    action: { primary: string; primaryHover: string; secondary: string; danger: string };
    feedback: { success: string; warning: string; error: string; info: string };
  };
  spacing: typeof spacing;
  typography: typeof typography;
}
```

Tarefas:
1. Defina `lightTheme` e `darkTheme` completos
2. Crie um `ThemeProvider` com contexto React
3. Crie um hook `useTheme()` que retorna o tema e `toggleTheme`
4. Crie um `ThemeToggle` componente que alterna entre os modos com ícone (sol/lua)
5. Persista a preferência no `localStorage`
6. Respeite `prefers-color-scheme` do SO como valor inicial
7. Transição suave (300ms) entre temas na `<body>`
