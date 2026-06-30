# Exercícios — Módulo 05

## Exercício 1: Crazy 8s — Tela de Cadastro

Aplique a técnica Crazy 8s para a tela de **cadastro de usuário** de um SaaS B2B.

```typescript
interface Crazy8Result {
  problem: string;
  variations: Variation[];
  chosenIndex: number;
  refinedWireframe: WireframeSpec;
}

interface Variation {
  id: number;
  description: string;
  keyDifference: string;
}
```

Instruções:
1. Desenhe 8 variações diferentes da tela de cadastro (no papel ou Excalidraw)
2. Para cada variação, anote o que é diferente (posição do formulário, campos exibidos, layout)
3. Escolha a melhor variação e refina em um wireframe único
4. Justifique sua escolha

Entregue as 8 descrições + o wireframe refinado documentado em TypeScript.

---

## Exercício 2: Grey Box — Dashboard Financeiro

Crie um wireframe **grey box** para um dashboard financeiro com:

- Header com navegação (logo, menu, perfil do usuário)
- Sidebar com atalhos (5 itens)
- Área principal com:
  - Card de saldo (destacado)
  - Gráfico de receitas vs despesas (placeholder)
  - Tabela de últimas transações (5 linhas)
- Footer minimalista

```typescript
interface GreyBoxWireframe {
  layout: 'sidebar-content';
  sections: GreyBoxSection[];
}

interface GreyBoxSection {
  name: string;
  shade: 'light' | 'medium' | 'dark';
  width: string;  // ex: '100%', '250px', '1fr'
  height: string;
  elements: string[];  // descrição dos elementos
}
```

Preencha a estrutura acima com as dimensões e descrições de cada seção. Use proporções realistas (ex: sidebar 250px, card de saldo em destaque).

---

## Exercício 3: Wireflow — Fluxo de Recuperação de Senha

Modele o **wireflow** completo do fluxo de recuperação de senha:

1. Tela de login → clica em "Esqueci a senha"
2. Tela de solicitação (informar email)
3. **Sucesso**: email enviado → tela de confirmação
4. **Erro**: email não encontrado → toast de erro na mesma tela
5. Link do email → tela de redefinição (nova senha + confirmação)
6. **Sucesso**: senha alterada → redireciona ao login
7. **Erro**: token expirado → tela de erro com link para reenviar

```typescript
interface WireflowExercise {
  screens: WireframeSpec[];
  transitions: Transition[];
  errorPaths: number;  // quantos caminhos de erro foram mapeados
}
```

Mapeie todas as telas e transições, incluindo **todos os caminhos de erro** (pelo menos 3). Represente como array de `Transition`.

---

## Exercício 4: Documentação de Wireframe Enterprise

Você é o tech lead de um projeto enterprise. Recebeu o wireframe abaixo do designer:

> Tela: "Dashboard do Gestor"
> Versão: v1 (rascunho)
> Observações do designer: "Tem um gráfico aqui e uma tabela ali"

Documente este wireframe corretamente preenchendo a estrutura abaixo:

```typescript
// Complete esta documentação
const wireframeDoc: WireframeDocumentation = {
  id: 'WF-???',
  title: '???',
  module: '???',
  version: '???',
  author: '???',
  createdAt: '???',
  updatedAt: '???',
  userStoryId: '???',
  epicId: '???',
  elements: [
    // Defina pelo menos 6 elementos com tipo e bounding box
  ],
  states: [
    // Defina estados loading e empty para a tabela
  ],
  interactions: [
    // Defina ao menos 2 interações (ex: clicar em card abre detalhes)
  ],
  notes: '???',
  approvals: [
    // Crie uma aprovação com status 'pending'
  ],
};
```

Use nomes e IDs realistas. Justifique cada campo que você preencheu.

---

## Exercício 5: Especificação de Handoff

Prepare a **especificação de handoff** para um componente de **Tabela de Transações** que aparece no wireframe de um sistema financeiro.

O componente deve:
- Exibir colunas: Data, Descrição, Categoria, Valor, Status
- Ter estados: **default** (com dados), **loading** (skeleton), **empty** (sem transações), **error** (falha ao carregar)
- Ser responsivo: em mobile, as colunas Data e Categoria ficam ocultas
- Seguir o design system com nome de componente `DataTable`

```typescript
interface HandoffSpec {
  componentName: string;
  dsReference: string;
  states: Record<string, WireframeElement>; // default, loading, empty, error
  responsiveBreakpoints: {
    mobile: { hiddenColumns: string[] };
    tablet: { hiddenColumns: string[] };
    desktop: { hiddenColumns: string[] };
  };
  apiContract: {
    endpoint: string;
    method: 'GET' | 'POST';
    requestFields: string[];
    responseFields: string[];
    errorCodes: string[];
  };
  measurements: {
    rowHeight: number;
    headerHeight: number;
    cellPadding: number;
    fontSize: number;
  };
  notes: string; // observações para o desenvolvedor
}
```

Preencha todos os campos com valores realistas. Nas notes, inclua observações sobre ordenação, paginação e estado vazio.
