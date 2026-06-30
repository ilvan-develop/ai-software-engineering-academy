
# Wireframes e Prototipação

# Módulo 05 — Wireframes

**Esboçar telas antes de codar. Validar antes de investir.**

---

## 1. O que são Wireframes

Wireframe é o **esqueleto visual** de uma tela. É a representação estrutural da interface, focando em **layout, hierarquia, conteúdo e funcionalidade** — sem nenhum polimento visual (cores, fontes, imagens).

### Propósito

```text
Wireframe serve para:
┌──────────────────────────────────────────────┐
│  Validar fluxo e navegação antes do design   │
│  Alinhar time sobre a estrutura da tela      │
│  Identificar inconsistências cedo            │
│  Servir de contrato entre produto e dev      │
│  Acelerar o ciclo de iteração                │
└──────────────────────────────────────────────┘
```

### Níveis de Fidelidade

| Fidelidade | Aparência | Quando usar | Prós | Contras |
|------------|-----------|-------------|------|---------|
| **Baixa** | Esboço à mão, traços simples | Brainstorming, ideação, sprints | Rápido, barato, encoraja iteração | Pouco realista, difícil compartilhar remotamente |
| **Média** | Grey box, tons de cinza, formas definidas | Validação de fluxo, testes remotos | Clara distinção de hierarquia, boa para testar | Ainda não testa apelo visual |
| **Alta** | Quase real, com grid definido, tipografia aproximada | Handoff, aprovação de stakeholders | Mínima ambiguidade, base para protótipo | Leva mais tempo, pode ser confundida com design final |

```typescript
// Representação de níveis de fidelidade
type Fidelity = 'low' | 'medium' | 'high';

interface WireframeSpec {
  fidelity: Fidelity;
  elements: WireframeElement[];
  interactions?: Interaction[];
}

interface WireframeElement {
  type: 'header' | 'hero' | 'card' | 'form' | 'button' | 'footer';
  boundingBox: { x: number; y: number; w: number; h: number };
  placeholder: string; // "imagem do produto", "título"
}
```text

---

## 2. Wireframe vs Mockup vs Protótipo

É comum confundir os três. A diferença está no **nível de detalhe** e no **propósito**.

```text
                  DETALHE VISUAL
                  ──────────────▶
  Wireframe ───▶  Mockup ───▶  Protótipo
  Estrutura        Visual        Interação
  ────────         ──────        ─────────
  Caixas           Cores         Clica
  Hierarquia       Fontes        Navega
  Fluxo            Ícones        Anima
  Sem estilo       Imagens       Testa
```

### Comparação

| Aspecto | Wireframe | Mockup | Protótipo |
|---------|-----------|--------|-----------|
| **O que é** | Esqueleto estrutural | Representação estática final | Simulação interativa |
| **Fidelidade** | Baixa/média | Alta | Alta |
| **Interativo?** | Não | Não | Sim |
| **Cores?** | Não (tons de cinza) | Sim (design final) | Sim |
| **Tempo de criação** | Minutos | Horas | Dias |
| **Objetivo** | Alinhar estrutura | Aprovar visual | Testar usabilidade |
| **Quem usa** | Produto + Dev + Design | Stakeholders | Time + Usuários |

### Quando usar cada um

```typescript
interface DesignStage {
  phase: string;
  artifact: 'wireframe' | 'mockup' | 'prototype';
  goal: string;
  participants: string[];
  estimatedTime: string;
}

const stages: DesignStage[] = [
  {
    phase: 'Descoberta',
    artifact: 'wireframe',
    goal: 'Validar fluxo e estrutura com o time',
    participants: ['PO', 'Designer', 'Dev'],
    estimatedTime: '30 min — 2h',
  },
  {
    phase: 'Definição',
    artifact: 'mockup',
    goal: 'Aprovar estilo visual com stakeholder',
    participants: ['Designer', 'PO', 'Cliente'],
    estimatedTime: '1 — 3 dias',
  },
  {
    phase: 'Validação',
    artifact: 'prototype',
    goal: 'Testar usabilidade com usuários reais',
    participants: ['Designer', 'Dev', 'Usuários'],
    estimatedTime: '2 — 5 dias',
  },
];
```

---

## 3. Princípios de Layout

Wireframe eficiente segue princípios de design visual, mesmo sem cores.

### Grid

O grid é a **espinha dorsal** do layout. Ele garante alinhamento, consistência e ritmo.

```typescript
interface Grid {
  columns: number;       // ex: 12
  gutter: number;        // ex: 16px (espaço entre colunas)
  margin: number;        // ex: 24px (margem lateral)
  breakpoints: Record<string, number>;
}

const desktopGrid: Grid = {
  columns: 12,
  gutter: 16,
  margin: 24,
  breakpoints: { sm: 640, md: 768, lg: 1024, xl: 1280 },
};

// Utilitário para calcular largura de coluna
function colWidth(cols: number, grid: Grid): number {
  const contentWidth = 1200 - grid.margin * 2;
  const totalGutter = (grid.columns - 1) * grid.gutter;
  const colSize = (contentWidth - totalGutter) / grid.columns;
  return colSize * cols + (cols - 1) * grid.gutter;
}
```

```text
Wireframe com grid de 12 colunas:
┌──────────────────────────────────────────────────┐
│   Header (12 col)                                │
├──────┬──────────┬──────────┬──────────┬──────────┤
│ 3col │    3col  │   3col   │   3col   │          │
├──────┴──────────┴──────────┴──────────┴──────────┤
│   Content (8 col)        │   Sidebar (4 col)     │
├──────────────────────────┴───────────────────────┤
│   Footer (12 col)                                │
└──────────────────────────────────────────────────┘
```

### Hierarquia Visual

Organize os elementos por **importância**. O olho do usuário deve saber para onde olhar primeiro.

```text
Hierarquia no wireframe:
─────────────────────────
1. Hero / Título principal   (maior box, posição central)
2. Chamada para ação (CTA)   (destacado, contraste de forma)
3. Seções de conteúdo         (blocos médios, organizados)
4. Navegação secundária       (menor, no topo ou sidebar)
5. Footer                     (menor destaque, no final)
```

### Espaçamento

```typescript
// Sistema de espaçamento (8px grid)
const space = {
  xxs: 4,   // 4px  — ícones, badges
  xs: 8,    // 8px  — padding interno compacto
  sm: 16,   // 16px — entre elementos relacionados
  md: 24,   // 24px — entre seções
  lg: 32,   // 32px — entre blocos maiores
  xl: 48,   // 48px — entre seções principais
  xxl: 64,  // 64px — margens de página
};

// Regra: elementos relacionados ficam mais próximos (8-16px)
// Seções diferentes ficam mais distantes (32-48px)
```

### Proporção

Use proporções familiares para criar harmonia visual:

```text
╔══════════════════════════════════════╗
║  16:9  — Hero/Banner (widescreen)   ║
║  4:3   — Cards de conteúdo          ║
║  1:1   — Avatares, thumbnails       ║
║  3:2   — Imagens de destaque        ║
║  2:1   — Painéis e dashboards       ║
╚══════════════════════════════════════╝
```

---

## 4. Ferramentas

### Comparação

| Ferramenta | Tipo | Fidelidade | Curva | Colaboração | Preço |
|------------|------|-----------|-------|-------------|-------|
| **Papel e caneta** | Físico | Baixa | Zero | Presencial | Grátis |
| **Excalidraw** | Web | Baixa | 5 min | Tempo real (link) | Grátis |
| **Balsamiq** | Desktop/Web | Baixa-média | 30 min | Compartilhamento | Pago (~$12/mês) |
| **Figma** | Web | Média-alta | 2h | Tempo real + comentários | Grátis (inicio) |
| **Whimsical** | Web | Baixa-média | 15 min | Link compartilhável | Grátis (limitado) |
| **Miro** | Web | Baixa | 10 min | Quadro infinito + templates | Grátis (limitado) |

### Quando usar qual

```
📝 Papel e caneta
  → Brainstorming individual ou em dupla
  → Sprint de design (Google Design Sprint)

✏️ Excalidraw / Whimsical
  → Esboço remoto rápido
  → Wireframes de baixa fidelidade colaborativos

🎨 Balsamiq
  → Wireframes de média fidelidade
  → Prototipação rápida sem distração visual

🖌️ Figma
  → Wireframes de média/alta fidelidade
  → Componentes reutilizáveis
  → Handoff para devs
  → Protótipos interativos
```

### Excalidraw — Exemplo rápido

```typescript
// Representação de um wireframe no Excalidraw
interface ExcalidrawElement {
  type: 'rectangle' | 'text' | 'arrow' | 'diamond';
  x: number;
  y: number;
  width: number;
  height: number;
  backgroundColor: 'transparent' | '#ffffff' | '#cccccc';
  strokeStyle: 'solid' | 'dashed' | 'dotted';
}

const loginWireframe: ExcalidrawElement[] = [
  { type: 'rectangle', x: 0, y: 0, width: 400, height: 60, backgroundColor: '#cccccc', strokeStyle: 'solid' },
  { type: 'text', x: 10, y: 20, width: 200, height: 20, backgroundColor: 'transparent', strokeStyle: 'solid' },
  // ...mais elementos
];
```text

> 💡 **Dica Enterprise**: Figma é o padrão da indústria. Invista em aprender componentes, auto-layout e variants. Balsamiq é ótimo para documentação regulatória (foco em estrutura, não em visual).

---

## 5. Técnicas de Wireframing

### Esboço Rápido (Crazy 8s)

Técnica de **divergência criativa**: dobre uma folha em 8 partes, desenhe 8 variações diferentes de uma mesma tela em **8 minutos** (1 minuto cada).

```text
Como fazer:
1. Defina o problema: "Tela de dashboard pós-login"
2. Configure timer de 8 minutos
3. Desenhe 8 versões diferentes (sem repetir)
4. Ao final, vote na melhor ideia
5. Refine a vencedora em um wireframe único
```

### Grey Box

Técnica de wireframing que usa **apenas caixas cinzas** para representar os elementos. Foco total na estrutura, sem distrações.

```text
Exemplo de Grey Box:
┌─────────────────────────────────────────────────┐
│  [LOGO]          [Nav1] [Nav2] [Nav3]  [Login]  │  ← header (cinza escuro)
├─────────────────────────────────────────────────┤
│                                                   │
│   ┌─────────────────────────────────────┐         │
│   │  ████████████████████████████████  │         │  ← hero (cinza médio)
│   │  ████████████████████████████████  │         │
│   └─────────────────────────────────────┘         │
│                                                   │
│   ┌──────┐  ┌──────┐  ┌──────┐                   │
│   │      │  │      │  │      │                    │  ← cards (cinza claro)
│   │      │  │      │  │      │                    │
│   └──────┘  └──────┘  └──────┘                   │
│                                                   │
├─────────────────────────────────────────────────┤
│  [Links]         [Contato]         © 2025       │  ← footer (cinza escuro)
└─────────────────────────────────────────────────┘
```

### Wireflow

Combinação de **wireframe + fluxograma**. Cada tela é conectada por setas que mostram a navegação.

```text
Wireflow de cadastro:
┌──────────┐   clicou   ┌──────────┐   sucesso   ┌──────────┐
│ Tela     │ ────────▶ │ Tela     │ ──────────▶ │ Dashboard │
│ Login    │           │ Cadastro │              │           │
└──────────┘           └──────────┘              └──────────┘
    │                       │
    │ erro                  │ cancelou
    ▼                       ▼
┌──────────┐           ┌──────────┐
│ Toast:   │           │ Tela     │
│ "Email"  │           │ Login    │
└──────────┘           └──────────┘
```

```typescript
interface Wireflow {
  screens: WireframeSpec[];
  transitions: Transition[];
}

interface Transition {
  from: string;          // id da tela de origem
  to: string;            // id da tela de destino
  trigger: 'click' | 'submit' | 'error' | 'success' | 'timeout';
  element?: string;      // elemento que dispara (ex: "btn-login")
  condition?: string;    // condição (ex: "campos válidos")
}
```

### Sketching (Desenho à mão)

Desenhar à mão força o **foco na estrutura** e elimina a tentação de polir visualmente. Além disso:

```
Vantagens do sketching:
├── Velocidade: 10x mais rápido que digital
├── Baixo comprometimento: fácil descartar e recomeçar
├── Qualquer um participa: não precisa saber ferramenta
└── Memorável: estudos mostram que esboços manuais
    geram mais feedback honesto que protótipos polidos
```

---

## 6. Anatomia de uma Tela

Toda tela segue uma estrutura comum. Conhecer a anatomia ajuda a criar wireframes consistentes.

```text
Anatomia padrão de uma página:
┌──────────────────────────────────────────────────────┐
│  HEADER                                               │
│  ┌──────┐  ┌──────────────────────┐  ┌────┐ ┌────┐  │
│  │ LOGO │  │ Nav: Prod | Preços   │  │ Bus│ │User│  │
│  └──────┘  └──────────────────────┘  └────┘ └────┘  │
├──────────────────────────────────────────────────────┤
│                                                       │
│  HERO                                                 │
│  ┌────────────────────────────────────────────────┐  │
│  │  Título principal (H1)                         │  │
│  │  Subtítulo de apoio (até 2 linhas)             │  │
│  │  [CTA Primário]  [CTA Secundário]              │  │
│  │  ┌──────────────────────────────────────────┐  │  │
│  │  │         Imagem / Ilustração              │  │  │
│  │  └──────────────────────────────────────────┘  │  │
│  └────────────────────────────────────────────────┘  │
│                                                       │
│  CONTEÚDO                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐           │
│  │ Card 1   │  │ Card 2   │  │ Card 3   │           │
│  │ Título   │  │ Título   │  │ Título   │           │
│  │ Descrição│  │ Descrição│  │ Descrição│           │
│  └──────────┘  └──────────┘  └──────────┘           │
│                                                       │
│  ┌────────────────────────────────────────────────┐  │
│  │  Formulário:                                   │  │
│  │  [Nome ______________]                         │  │
│  │  [Email _____________]                         │  │
│  │  [Enviar]                                      │  │
│  └────────────────────────────────────────────────┘  │
│                                                       │
├──────────────────────────────────────────────────────┤
│  FOOTER                                               │
│  ┌──────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │ Links│  │ Redes sociais│  │ © 2025 Company   │  │
│  └──────┘  └──────────────┘  └──────────────────┘  │
└──────────────────────────────────────────────────────┘
```

### Detalhamento dos elementos

| Elemento | Função | Wireframe |
|----------|--------|-----------|
| **Header** | Identidade + navegação global | Box superior com logo à esquerda, nav ao centro/direita |
| **Hero** | Primeira impressão, valor principal | Box grande com título, subtítulo e CTA |
| **Conteúdo** | Informação principal | Grid de cards, listas, formulários |
| **CTA** | Ação desejada (primário/secundário) | Botão destacado (maior, posição estratégica) |
| **Navegação** | Explorar o produto | Menu horizontal, sidebar, breadcrumb |
| **Footer** | Links secundários, legais | Box inferior com informações complementares |

```typescript
// Definição programática de uma tela
interface ScreenAnatomy {
  header: {
    logo: string;
    navItems: NavItem[];
    ctaButton?: { label: string; action: string };
  };
  hero: {
    headline: string;
    subheadline?: string;
    primaryCta: { label: string; action: string };
    secondaryCta?: { label: string; action: string };
    mediaType: 'image' | 'video' | 'illustration';
  };
  content: ContentSection[];
  footer: {
    links: { label: string; url: string }[];
    legal: string;
  };
}

interface NavItem {
  label: string;
  active: boolean;
  children?: NavItem[];
}
```text

### Padrões de layout comuns

```text
┌─────────────────┐  ┌──────────┬──────────────┐  ┌──────────┬─────────┐
│   Single        │  │   Sidebar               │  │   Dashboard          │
│   Column        │  │   + Content             │  │   Cards              │
│                 │  │                          │  │                      │
│   Landing       │  │   [Menu] │  Conteúdo     │  │  ┌───┐ ┌───┐ ┌───┐ │
│   page          │  │   [Sub]  │  principal    │  │  │   │ │   │ │   │ │
│                 │  │   [Sub]  │  da página    │  │  └───┘ └───┘ └───┘ │
│   Foco total    │  │          │               │  │  ┌───┐ ┌───┐ ┌───┐ │
│   no conteúdo   │  │          │               │  │  │   │ │   │ │   │ │
│                 │  │          │               │  │  └───┘ └───┘ └───┘ │
└─────────────────┘  └──────────┴──────────────┘  └─────────────────────┘
```

---

## 7. Interação — Estados e Transições

Wireframes de média/alta fidelidade devem representar **estados da interface**.

### Estados de Componentes

Cada componente pode estar em um dos seguintes estados:

```typescript
type ComponentState = 'loading' | 'empty' | 'error' | 'success' | 'disabled' | 'default' | 'hover' | 'active';

interface StatefulComponent {
  name: string;
  states: Record<ComponentState, WireframeElement>;
}
```

### Como representar cada estado no wireframe

| Estado | Representação visual | O que mostra |
|--------|---------------------|--------------|
| **Default** | Elemento normal, tons de cinza | Estado neutro |
| **Loading** | Skeleton boxes (retângulos com animação sugerida) | Dados estão carregando |
| **Empty** | Box vazio com texto "Nenhum item encontrado" + CTA | Não há dados |
| **Error** | Box com borda tracejada/vermelha + mensagem | Algo deu errado |
| **Success** | Confirmação visual (checkmark, toast) | Ação concluída |
| **Disabled** | Elemento opaco, sem contraste | Ação indisponível |

### Skeleton Loading

```typescript
// Componente de skeleton para wireframe
interface SkeletonBox {
  width: number | string;  // '100%' | '300px'
  height: number | string;
  borderRadius: number;
  lines?: number;          // para texto simulado
}
```

```text
Wireframe de estado loading (skeleton):
┌──────────────────────────────────────┐
│  ┌────────────────────────────────┐  │
│  │  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │  │  ← skeleton hero
│  │  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │  │
│  └────────────────────────────────┘  │
│                                       │
│  ┌──────────┐  ┌──────────┐          │
│  │ ▓▓▓▓▓▓▓  │  │ ▓▓▓▓▓▓▓  │          │  ← skeleton cards
│  │ ▓▓▓▓▓    │  │ ▓▓▓▓▓    │          │
│  └──────────┘  └──────────┘          │
└──────────────────────────────────────┘
```

### Estado Empty

```text
Wireframe de estado vazio (empty):
┌──────────────────────────────────────┐
│                                       │
│          ┌──────────────┐            │
│          │   📦 (ícone) │            │
│          └──────────────┘            │
│                                       │
│    Nenhum projeto encontrado         │
│                                       │
│    Crie seu primeiro projeto para     │
│    começar a organizar suas tarefas.  │
│                                       │
│    [Criar Projeto]                    │
│                                       │
└──────────────────────────────────────┘
```

### Transições

Wireframes podem (e devem) indicar transições entre telas:

```typescript
interface Transition {
  type: 'push' | 'modal' | 'toast' | 'slide' | 'fade';
  duration: number;  // ms
  trigger: string;   // ação do usuário
}
```

```text
Representação de transição no wireframe:
┌────────────┐      push(300ms)      ┌────────────┐
│  Tela A    │ ────────────────────▶ │  Tela B    │
│            │                      │            │
│  [Login]───┤                      │ Dashboard  │
└────────────┘                      └────────────┘
        │
        │ error(modal)
        ▼
┌────────────┐
│ ┌────────┐ │
│ │ Erro:  │ │
│ │ "Email"│ │
│ │ [OK]   │ │
│ └────────┘ │
└────────────┘
```

---

## 8. Validação de Wireframes

Wireframe não é o destino — é um **meio para validar**.

### Clickable Wireframes

Transforme wireframes estáticos em protótipos clicáveis para testar fluxo:

```typescript
interface ClickableWireframe {
  screens: WireframeSpec[];
  hotspots: Hotspot[];
}

interface Hotspot {
  screenId: string;
  area: { x: number; y: number; w: number; h: number };
  action: 'navigate' | 'showModal' | 'showToast';
  target: string; // id da tela ou ação
}
```text

Ferramentas para criar clickable wireframes:
- **Figma** — Prototyping mode (conecta frames com setas)
- **Balsamiq** — Link entre telas
- **Excalidraw** — Setas + links
- **Miro** — Conecta boards com setas

### Teste de wireframe com usuários

```text
Roteiro de teste de wireframe:
──────────────────────────────

1. Contexto
   "Aqui está um esboço de uma tela. Não está finalizado.
    Queremos entender se o fluxo faz sentido."

2. Tarefa
   "Mostre como você faria para criar um novo projeto."

3. Observe
   - Onde o usuário clica primeiro?
   - Ele hesita em algum lugar?
   - Ele encontra o CTA?

4. Pergunte
   - "O que você acha que esse elemento faz?"
   - "O que você esperaria ao clicar aqui?"
   - "Faltou alguma informação?"
```

### Iteração

O ciclo ideal:
```typescript
Esboçar → Validar → Aprender → Refinar → (repetir)
```

```typescript
interface IterationCycle {
  version: number;
  changes: string[];
  validatedBy: string[];
  feedbackThemes: string[];
  nextSteps: string[];
}

const cycle: IterationCycle = {
  version: 3,
  changes: [
    'Moveu CTA para o centro da tela',
    'Adicionou breadcrumb na navegação',
    'Reduziu formulário de 8 para 4 campos',
  ],
  validatedBy: ['PO', '2 usuários'],
  feedbackThemes: [
    'CTA não era visível',
    'Formulário muito longo',
    'Falta indicador de volta',
  ],
  nextSteps: ['Testar versão 4 com 5 usuários'],
};
```

---

## 9. Wireframes em Enterprise

Em contexto enterprise, wireframes vão além do esboço — eles se tornam **documentos de especificação**.

### Documentação

Cada wireframe deve incluir metadados:

```typescript
interface WireframeDocumentation {
  // Metadados
  id: string;                    // "WF-001"
  title: string;                 // "Tela de Login"
  module: string;                // "Autenticação"
  version: string;               // "1.3"
  author: string;                // "Maria Silva"
  createdAt: string;             // ISO date
  updatedAt: string;             // ISO date

  // Rastreabilidade
  userStoryId: string;           // "US-042"
  epicId: string;                // "EPIC-07"

  // Conteúdo
  elements: WireframeElement[];
  states: StatefulComponent[];
  interactions: Interaction[];
  notes: string;                 // Observações para dev

  // Aprovações
  approvals: Approval[];
}

interface Approval {
  role: 'PO' | 'DesignLead' | 'TechLead';
  name: string;
  date: string;
  status: 'pending' | 'approved' | 'changes_requested';
  comments?: string;
}
```text

### Handoff para Devs

O handoff é o momento em que o wireframe vira código. Para que seja eficiente:

```
Checklist de handoff (wireframe → dev):
──────────────────────────────────────────
[ ] Grid definido (colunas, gutters, margens)
[ ] Medidas exatas dos elementos (largura, altura)
[ ] Espaçamentos documentados (padding, margin)
[ ] Estados mapeados (loading, empty, error, success)
[ ] Comportamento em breakpoints (responsivo)
[ ] Fluxo de navegação diagramado (wireflow)
[ ] Anotações em elementos não óbvios
[ ] Nomes de componentes consistentes com o design system
```

```typescript
// Especificação de handoff
interface HandoffSpec {
  screen: WireframeDocumentation;
  responsiveBreakpoints: {
    mobile: WireframeSpec;
    tablet: WireframeSpec;
    desktop: WireframeSpec;
  };
  componentReferences: {
    [componentName: string]: string; // "Button" → "ds-button"
  };
  apiContracts: {
    endpoint: string;
    method: string;
    requestFields: string[];
    responseFields: string[];
  }[];
}
```

### Versionamento

Wireframes em enterprise precisam de versionamento igual a código.

```text
Estratégia de versionamento:
─────────────────────────────

Figma:
  - Branching: crie branches para variações
  - Version history: Figma salva automaticamente
  - Nomeie versões: "v1.0 - Aprovado PO", "v1.1 - Revisão dev"

Arquivos:
  wireframe-tela-login-v1.0.fig
  wireframe-tela-login-v1.1.fig
  wireframe-tela-login-v2.0.fig

Convenção: {componente}-{tela}-v{major}.{minor}.{tipo}

Boas práticas:
  ├── Congele versões aprovadas (não mexa)
  ├── Versão major = mudança estrutural
  ├── Versão minor = ajuste de layout
  └── Mantenha changelog por versão
```

### Exemplo de Changelog de Wireframe

```typescript
interface WireframeChangelog {
  version: string;
  date: string;
  author: string;
  changes: string[];
  reason: string;
}

const changelog: WireframeChangelog[] = [
  {
    version: '1.0',
    date: '2025-06-01',
    author: 'Maria Silva',
    changes: ['Criação inicial do wireframe'],
    reason: 'Primeira versão para alinhamento com PO',
  },
  {
    version: '1.1',
    date: '2025-06-03',
    author: 'Maria Silva',
    changes: [
      'Adicionado campo de busca no header',
      'Reduzido hero de 800px para 600px',
    ],
    reason: 'Feedback do PO: buscar é prioridade',
  },
  {
    version: '2.0',
    date: '2025-06-10',
    author: 'Carlos Lima',
    changes: [
      'Reestruturado layout para sidebar + content',
      'Adicionada seção de relatórios',
      'Removido carrossel do hero',
    ],
    reason: 'Mudança de escopo: nova feature de relatórios',
  },
];

