# Projeto Módulo 06 — Design System de uma Plataforma de Recursos Humanos

## Objetivo

Criar a especificação e implementação de um **Design System** para um SaaS de RH enterprise chamado **PeopleFlow**, que gerencia recrutamento, onboarding, avaliações e folha de pagamento.

## Contexto

A **PeopleFlow** é uma startup que cresceu rápido e hoje tem um produto funcional mas visualmente inconsistente. Cada tela foi feita por um time diferente, com cores, tipografia e componentes próprios. O resultado:

- 3 tons de azul diferentes em botões "Salvar"
- Inputs com padding variando de 6px a 14px
- Mensagens de erro em vermelho, laranja ou vinho
- Nenhum estado de loading ou empty state
- Dark mode inexistente

Sua missão é **criar e implementar o Design System** da PeopleFlow, padronizando a UI e documentando todos os tokens, componentes e padrões.

## Entregáveis

### 1. Tokens de Design (weight: 20%)

Defina os tokens de design da PeopleFlow:

```typescript
interface DesignTokens {
  colors: {
    brand: { primary: string; primaryLight: string; primaryDark: string };
    feedback: { success: string; warning: string; error: string; info: string };
    neutral: Record<number, string>; // 50–900
    text: { primary: string; secondary: string; disabled: string; inverse: string };
    surface: { page: string; card: string; modal: string; sidebar: string };
  };
  typography: {
    fontFamily: { sans: string; mono: string };
    scale: Record<string, { size: number; lineHeight: number; weight: number }>;
  };
  spacing: Record<string, number>;
  breakpoints: Record<string, number>;
  animation: {
    duration: Record<string, string>;
    easing: Record<string, string>;
  };
}
```yaml

Tarefas:
1. Escolha uma cor primária para a marca (justifique com base no segmento RH)
2. Defina paleta completa (brand, feedback, neutral, text, surface)
3. Defina escala tipográfica (uso modular scale 1.25)
4. Defina escala de espaçamento (4px base)
5. Defina breakpoints (mobile, tablet, desktop)
6. Defina tokens de animação (duration + easing)

### 2. Componentes Core (weight: 30%)

Implemente em React/TypeScript os seguintes componentes com **todos os estados**:

#### Button
- Variantes: `primary`, `secondary`, `outline`, `ghost`, `danger`
- Tamanhos: `sm`, `md`, `lg`
- Estados: default, hover, active, focus-visible, disabled, loading
- Suporte a ícone esquerdo/direito

#### Input
- Tipos: text, email, password, number, date
- Estados: default, hover, focus, error, disabled
- Suporte a label, placeholder, hint, error message
- Suporte a leftIcon e rightIcon (ex: eye para password)

#### Modal
- Tamanhos: `sm` (400px), `md` (560px), `lg` (720px)
- Overlay com fade, focus trap, fechar com Escape
- Header (ícone + título + close), body, footer
- Animação de entrada/saída

#### DataTable
- Colunas com sort e width configurável
- Densidades: `comfortable` (48px), `standard` (40px), `compact` (32px)
- Estados: loading (skeleton), empty (empty state), error
- Striped rows, hover highlight
- Paginação (pageSize configurável)

#### Select
- Com busca (searchable), opções agrupadas, clearable
- Estados: default, hover, focus, error, disabled
- Keyboard navigation (setas, enter, escape)

### 3. Dark Mode (weight: 15%)

Implemente dark mode completo:

1. Defina `darkTheme` com paleta invertida/ajustada
2. Crie `ThemeProvider` com Context API
3. Crie hook `useTheme()` com `toggleTheme`
4. Persistência em `localStorage`
5. Respeitar `prefers-color-scheme` do SO
6. Transição suave (300ms) entre temas
7. Todos os componentes core devem funcionar em dark mode

### 4. Página de Amostra (weight: 25%)

Implemente uma página funcional que demonstre o sistema. Escolha UMA das telas abaixo:

#### Opção A — Dashboard de Recrutamento
```text
┌──────────────────────────────────────────────┐
│  Header (logo + search + avatar + theme btn) │
├──────────┬───────────────────────────────────┤
│ Sidebar  │  Main Content                      │
│          │  ┌──────┬──────┬──────┬──────┐     │
│ Dashboard│  │ Total │ Novos│ Em    │ Con- │     │
│ Vagas    │  │ vagas │ hoje │ and.  │ trat.│     │
│ Candidatos│  └──────┴──────┴──────┴──────┘     │
│ Relatórios│  ┌─────────────────────────────┐   │
│ Config   │  │ Tabela de vagas ativas       │   │
│          │  │ (DataTable com sort+page)    │   │
│          │  └─────────────────────────────┘   │
└──────────┴───────────────────────────────────┘
```markdown

#### Opção B — Formulário de Cadastro de Funcionário
```text
┌─────────────────────────────────┐
│  Header + Breadcrumb            │
├─────────────────────────────────┤
│  Novo Funcionário               │
│  ┌───────────────────────────┐  │
│  │ Dados Pessoais            │  │
│  │ [Nome] [Email] [Telefone] │  │
│  │ [CPF] [Data Nasc]         │  │
│  ├───────────────────────────┤  │
│  │ Endereço                  │  │
│  │ [CEP] [Rua] [Número]     │  │
│  │ [Bairro] [Cidade] [UF]   │  │
│  ├───────────────────────────┤  │
│  │ Cargo e Salário           │  │
│  │ [Select cargo] [Salário]  │  │
│  │ [Data início] [Tipo]      │  │
│  └───────────────────────────┘  │
│  [Salvar] [Cancelar]           │
└─────────────────────────────────┘
```markdown

#### Opção C — Kanban de Processo Seletivo
```text
┌──────────────────────────────────────────────┐
│  Header + Filtros + Botão "Nova vaga"        │
├──────────┬──────────┬──────────┬─────────────┤
│ Triagem  │ Entrev.  │ Técnica  │ Contratação │
│ ┌──────┐ │ ┌──────┐ │ ┌──────┐ │ ┌──────┐    │
│ │Maria │ │ │ João │ │ │ Ana  │ │ │Carlos│    │
│ │Dev   │ │ │Dev   │ │ │Dev   │ │ │Dev   │    │
│ └──────┘ │ └──────┘ │ └──────┘ │ └──────┘    │
│ ┌──────┐ │ ┌──────┐ │ ┌──────┐ │             │
│ │Pedro │ │ │Lucas │ │ │Sofia │ │             │
│ │Dev   │ │ │Dev   │ │ │Dev   │ │             │
│ └──────┘ │ └──────┘ │ └──────┘ │             │
└──────────┴──────────┴──────────┴─────────────┘
```sql

Requisitos da página:
- Use **todos os 5 componentes core** (Button, Input, Modal, DataTable, Select)
- Implemente dark mode funcional
- Inclua pelo menos 1 modal (ex: "Confirmar exclusão" ou "Nova vaga")
- Inclua pelo menos 1 empty state (se não houver dados)
- Inclua pelo menos 1 loading state
- Responsivo (mobile + tablet + desktop)

### 5. Documentação (weight: 10%)

Crie um arquivo `README.md` com:

```markdown
# PeopleFlow — Design System

## Tokens
- [Link para tokens completos]
- Paleta de cores (com exemplos visuais hex)
- Escala tipográfica
- Escala de espaçamento

## Componentes
- Button: variantes, tamanhos, estados, exemplo de uso
- Input: tipos, estados, exemplo de uso
- Modal: tamanhos, comportamento, exemplo de uso
- DataTable: colunas, densidades, exemplo de uso
- Select: busca, grupos, exemplo de uso

## Dark Mode
- Como o tema é aplicado
- Exemplo de uso do ThemeProvider

## Como usar
```typescript
import { Button, Input, Modal, DataTable, Select } from '@peopleflow/ui';
import { ThemeProvider, useTheme } from '@peopleflow/ui/theme';
```markdown

## Contribuição
- Convenções de código
- Como adicionar novo componente
- Como testar
```markdown

## Critérios de avaliação

- [ ] Tokens de design completos e consistentes (cor, tipografia, espaçamento, animação)
- [ ] Paleta funcional (success, warning, error, info) correta e acessível
- [ ] Componentes implementam **todos os estados** (default, hover, active, focus, disabled, loading, empty, error)
- [ ] Dark mode funcional com persistência e transição suave
- [ ] Dark mode respeita `prefers-color-scheme`
- [ ] Componentes são acessíveis (aria, focus trap, keyboard nav, contraste)
- [ ] Página de amostra usa todos os 5 componentes core
- [ ] Página de amostra responsiva (mobile + tablet + desktop)
- [ ] Microinterações (animações, transições) presentes e suaves
- [ ] Documentação clara com exemplos de uso
