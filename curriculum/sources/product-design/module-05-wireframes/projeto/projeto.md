# Projeto Módulo 05 — Wireframes para o SaaS FinControl

## Objetivo

Criar wireframes completos (baixa, média e alta fidelidade) para um SaaS B2B de **gestão financeira empresarial**, aplicando as técnicas, princípios de layout, documentação e handoff aprendidos no módulo.

## Contexto

A **FinControl** é uma startup que desenvolveu um SaaS de gestão financeira para pequenas e médias empresas. O produto atual foi construído sem wireframes — o time foi direto para o código. Resultado:

1. Telas inconsistentes (cada dev fez do seu jeito)
2. Fluxos confusos (usuários abandonam o cadastro)
3. Navegação não intuitiva (suporte recebe 50 chamados/dia sobre "onde clicar")
4. Sem documentação de layout (dificuldade de onboarding de novos devs)

A FinControl contratou você para **criar a base de wireframes** que vai guiar o redesign do produto.

## Entregáveis

### 1. Crazy 8s — Tela de Dashboard (weight: 15%)

Aplique a técnica Crazy 8s para a **tela principal de dashboard** do FinControl.

O dashboard deve mostrar:
- Saldo atual (cards de resumo: receitas, despesas, saldo)
- Gráfico de evolução financeira (últimos 6 meses)
- Últimas transações (tabela com 5 linhas)
- Alertas financeiros (contas a vencer, limite estourado)

Entregue:
- 8 variações descritas (pode ser textual ou imagem dos esboços)
- Variação vencedora com justificativa
- Wireframe da vencedora em formato de especificação TypeScript

```typescript
interface Crazy8ProjectResult {
  problem: string;
  variations: {
    id: number;
    layoutDescription: string;
    keyDifference: string;
    pros: string[];
    cons: string[];
  }[];
  chosenVariation: number;
  justification: string;
  refinedWireframe: WireframeSpec;
}
```

### 2. Grey Box — Tela de Cadastro de Transação (weight: 20%)

Crie um wireframe **grey box** para a tela de **cadastro/edição de transação financeira**.

Campos necessários:
- Tipo (entrada/saída) — seletor
- Valor — input monetário
- Data — date picker
- Categoria — dropdown (alimentação, transporte, salário, etc)
- Descrição — textarea
- Forma de pagamento — radio group (crédito, débito, pix, boleto)
- Anexar comprovante — upload de arquivo
- Botões: Salvar, Cancelar

Requisitos:
- Layout responsivo (desktop: formulário em 2 colunas; mobile: 1 coluna)
- Hierarquia visual clara (CTA "Salvar" em destaque)
- Estados: default, loading (salvando), error (validação), success (confirmação)

```typescript
interface GreyBoxProjectResult {
  screen: 'CadastroTransacao';
  layout: 'single-column' | 'multi-column';
  sections: GreyBoxSection[];
  responsiveBreakpoints: {
    mobile: string;  // descrição do layout mobile
    desktop: string; // descrição do layout desktop
  };
  states: {
    default: WireframeElement[];
    loading: WireframeElement[];
    error: WireframeElement[];
    success: WireframeElement[];
  };
}
```

### 3. Wireflow — Fluxo Completo de Lançamento Financeiro (weight: 25%)

Modele o **wireflow completo** de um lançamento financeiro, desde o acesso ao sistema até a confirmação:

1. Login
2. Dashboard (visão geral)
3. Navega para "Nova Transação"
4. Preenche formulário
5. **Caminho A (sucesso)**: transação salva → volta ao dashboard com toast de sucesso
6. **Caminho B (erro validação)**: campos inválidos → mensagens de erro inline no formulário
7. **Caminho C (erro servidor)**: falha na API → modal de erro com opção de retentar
8. Dashboard atualizado

Requisitos:
- Mínimo de 8 telas/estados representados
- Todos os caminhos de erro mapeados (pelo menos 2)
- Transições nomeadas com gatilhos (click, submit, success, error)

```typescript
interface WireflowProjectResult {
  title: string;
  screens: WireframeSpec[];
  transitions: Transition[];
  errorPaths: {
    path: string;
    trigger: string;
    screenIds: string[];
  }[];
  totalScreens: number;
  coverage: {
    happyPath: string[];
    errorPaths: string[];
  };
}
```

### 4. Anatomia da Tela — Especificação Enterprise (weight: 20%)

Documente a **tela de Dashboard** no formato enterprise, com metadados completos.

Inclua:
- ID, versão, autor, datas
- User story e epic vinculados
- Elementos mapeados com bounding boxes
- Estados de cada componente (tabela: loading, empty, error; cards: default, loading)
- Interações (cliques, hover, transições)
- Aprovações

```typescript
const dashboardDoc: WireframeDocumentation = {
  id: 'WF-DASH-001',
  title: 'Dashboard Financeiro',
  module: 'Finanças',
  version: '1.0',
  author: 'Seu Nome',
  createdAt: new Date().toISOString(),
  updatedAt: new Date().toISOString(),
  userStoryId: 'US-FIN-042',
  epicId: 'EPIC-FIN-07',
  elements: [
    // Mínimo de 8 elementos
  ],
  states: [
    // Mínimo de 3 componentes com estados mapeados
  ],
  interactions: [
    // Mínimo de 3 interações
  ],
  notes: 'Observações sobre comportamento, responsividade e dependências',
  approvals: [
    { role: 'PO', name: '', date: '', status: 'pending' },
    { role: 'DesignLead', name: '', date: '', status: 'pending' },
  ],
};
```

### 5. Especificação de Handoff (weight: 20%)

Prepare a especificação de handoff para o componente de **Tabela de Transações** do dashboard.

```typescript
interface HandoffProjectResult {
  componentName: string;
  dsReference: string;
  states: {
    default: { rows: number; columns: string[] };
    loading: { skeletonRows: number };
    empty: { message: string; ctaLabel: string };
    error: { message: string; retryAction: string };
  };
  responsiveBreakpoints: {
    mobile: { hiddenColumns: string[]; layout: string };
    tablet: { hiddenColumns: string[]; layout: string };
    desktop: { hiddenColumns: string[]; layout: string };
  };
  apiContract: {
    endpoint: string;
    method: string;
    requestFields: { name: string; type: string; required: boolean }[];
    responseFields: { name: string; type: string }[];
    pagination: { pageSize: number; cursorBased: boolean };
    errorCodes: { code: string; description: string; action: string }[];
  };
  measurements: {
    rowHeight: number;
    headerHeight: number;
    cellPadding: number;
    fontSize: number;
    borderWidth: number;
  };
  notes: string;
}
```

Preencha todos os campos com valores realistas e observações relevantes para o desenvolvedor (ex: "ordenar por data decrescente", "coluna valor com formatação monetária", "em mobile transformar tabela em cards").

## Critérios de avaliação

- [ ] Crazy 8s: 8 variações distintas e justificativa clara da escolha
- [ ] Grey Box: hierarquia visual correta, responsividade considerada
- [ ] Wireflow: todos os caminhos (incluindo erros) mapeados com transições
- [ ] Documentação: metadados completos, elementos, estados e interações
- [ ] Handoff: spec completa com estados, breakpoints, contrato de API e medidas
- [ ] Código TypeScript: tipos corretos, sem erros de sintaxe
- [ ] Consistência: nomenclatura uniforme entre todos os entregáveis
- [ ] Realismo: dimensões, grids e espaçamentos fazem sentido
