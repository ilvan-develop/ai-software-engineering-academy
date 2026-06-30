# Módulo 04 — UX: Experiência do Usuário

**Design centrado no usuário não é opcional — é o que separa produtos que vendem de produtos que acumulam poeira.**

---

## 1. O que é UX?

UX (User Experience) é a **percepção geral que uma pessoa tem ao interagir com um produto, sistema ou serviço**. Não se trata apenas de telas bonitas — envolve emoções, eficiência, acessibilidade e satisfação.

### UX vs UI

```text
UX                                        UI
Experiência completa                      Superfície visual
"Como o usuário se sente?"               "Como o produto se parece?"
Pesquisa, arquitetura, fluxo             Cores, tipografia, ícones
Funcionalidade e usabilidade             Estética e identidade
Ciência + Design                         Design + Arte
```

> UI sem UX é como um carro bonito sem motor. UX sem UI é como um motor potente sem carroceria.

### Os 5 Planos de Jesse James Garrett

O modelo mais clássico para estruturar UX, de baixo (abstrato) para cima (concreto):

```text
┌─────────────────────────────────────────────┐
│ 5. SUPERFÍCIE      Visual Design            │  ← UI, cores, ícones
├─────────────────────────────────────────────┤
│ 4. ESQUELETO       Interface / Navegação    │  ← Layout, botões, inputs
├─────────────────────────────────────────────┤
│ 3. ESTRUTURA       Interação / Info Arch    │  ← Fluxos, jornadas
├─────────────────────────────────────────────┤
│ 2. ESCOPO          Funcionalidades          │  ← Features, conteúdo
├─────────────────────────────────────────────┤
│ 1. ESTRATÉGIA      Necessidades do negócio  │  ← Objetivos, dores
└─────────────────────────────────────────────┘
```

| Plano | Pergunta central | Entregável típico |
|-------|------------------|-------------------|
| Estratégia | "Por que estamos fazendo isso?" | Visão do produto, OKRs |
| Escopo | "O que vamos construir?" | Backlog, requisitos |
| Estrutura | "Como as coisas se relacionam?" | Fluxogramas, IA |
| Esqueleto | "Onde cada coisa aparece?" | Wireframes, protótipos |
| Superfície | "Qual a aparência final?" | Design system, UI |

**Para devs:** entender os 5 planos significa saber que um bug de frontend pode estar no plano da estrutura (fluxo errado) e não no da superfície (CSS feio).

---

## 2. Pesquisa com Usuários

Pesquisa não é opcional — é o que impede você de construir a feature errada.

### Entrevistas

```text
❌ "Você usaria um botão de exportar CSV?"
✅ "Me conta como você faz para gerar relatórios hoje."
```

**Estrutura de uma entrevista:**

```text
1. Abertura (5min) — "Não estamos testando você, queremos aprender"
2. Contexto (10min) — "Me conta seu dia a dia com..."
3. Tarefa (15min) — "Você pode tentar fazer X enquanto pensa em voz alta?"
4. Exploração (10min) — "Por que você fez isso? O que esperava que acontecesse?"
5. Fechamento (5min) — "Algo mais que não perguntei?"
```

**Bons hábitos:**
- Pergunte sobre **comportamento passado** (não intenção futura)
- Fale 20% do tempo, ouça 80%
- Não faça perguntas indutoras ("Você não achou confuso?")
- Grave com permissão

### Testes de Usabilidade

Peça para o usuário **realizar uma tarefa** enquanto observa:

```typescript
// Exemplo de roteiro de teste
const tasks = [
  {
    id: 'cadastro',
    instrucao: 'Você é um novo usuário. Crie uma conta.',
    sucesso: 'consegue finalizar o cadastro em < 3 min',
  },
  {
    id: 'pedido',
    instrucao: 'Faça um pedido do produto X.',
    sucesso: 'conclui a compra sem ajuda',
  },
  {
    id: 'suporte',
    instrucao: 'Você precisa cancelar seu pedido. Onde procuraria?',
    sucesso: 'encontra a opção em < 2 cliques',
  },
];
```text

**Métricas de usabilidade:**
| Métrica | O que mede |
|---------|-----------|
| Success Rate | % de usuários que completam a tarefa |
| Time on Task | Tempo médio para completar |
| Error Rate | Quantidade de erros cometidos |
| SUS Score | Percepção subjetiva de usabilidade |
| NPS | Probabilidade de recomendação |

### Card Sorting

Técnica para **entender como usuários organizam informações**:

- **Aberto:** usuários criam suas próprias categorias
- **Fechado:** usuários classificam itens em categorias pré-definidas
- **Híbrido:** pode sugerir novas categorias

> Use card sorting quando for definir a navegação do seu produto. O resultado pode destruir (ou validar) a arquitetura que seu time inventou.

---

## 3. Arquitetura da Informação (IA)

Arquitetura da Informação é a **organização estrutural do conteúdo** — como as informações são categorizadas, rotuladas e navegadas.

### Os 4 componentes da IA

```text
1. ORGANIZAÇÃO      — Como o conteúdo é agrupado
   ├── Hierárquica  (ex: categorias e subcategorias)
   ├── Sequencial   (ex: wizard de cadastro)
   └── Matricial    (ex: tags, filtros)

2. NAVEGAÇÃO        — Como o usuário se movimenta
   ├── Global       (menu principal)
   ├── Local        (links internos de uma seção)
   ├── Contextual   (links no corpo do texto)
   └── Facetada     (filtros dinâmicos)

3. LABELING         — Nomes e rótulos
   ├── "Minha Conta" vs "Perfil"
   ├── "Gestão de Usuários" vs "Team"
   └── Consistência é mais importante que criatividade

4. BUSCA            — Sistema de busca interna
   ├── Autocomplete
   ├── Filtros
   └── Resultados relevantes
```

### Princípios de IA

| Princípio | Descrição |
|-----------|-----------|
| Revelância | Mostre o suficiente para o usuário saber o que existe |
| Exemplos | Mostre exemplos do que está por trás de um link |
| Portas de entrada | Permita chegar ao mesmo conteúdo por caminhos diferentes |
| Classificação múltipla | Ofereça diferentes formas de organizar (data, relevância, alfabética) |
| Navegação focada | Evite misturar navegação principal com conteúdo |

**Para devs:** AO definir rotas de API e URLs, pense na IA:
```typescript
// ❌ IA fraca, URLs confusas
/products/list?type=all
/user/info

// ✅ IA clara, URLs previsíveis
/produtos
/produtos/:id
/minha-conta/dados
/minha-conta/pedidos
```

---

## 4. Jornada do Usuário

A jornada mapeia **cada passo que o usuário dá** ao interagir com o produto, incluindo emoções, canais e pontos de dor.

### User Journey Map

```text
FASE          AÇÕES                   EMOÇÃO     OPORTUNIDADE
─────────     ─────────────────────   ─────────   ─────────────────
DESCOBERTA    "Pesquisei 'SaaS CRM'"  😕 Confuso  SEO melhor
              "Li review no Google"   🤔 Curioso  Comparativo claro
              "Acessei landing page"  😐 Neutro   CTAs mais claros

AVALIAÇÃO     "Preenchi formulário"   😤 Irritado Formulário menor
              "Agendei demo"          🙂 Ok       Auto-agendamento
              "Testei 14 dias"        😊 Animado  Onboarding guiado

ATIVAÇÃO      "Convidei time"         😰 Ansioso  Convite em massa
              "Configurei dados"      😩 Frust.   Importação fácil
              "Primeiro relatório"    😃 Feliz    Template pronto

RETENÇÃO      "Uso semanal"           😊 Satisf.  Notificações
              "Preciso de ajuda"      😠 Irrit.   Chat + FAQ
              "Renovei contrato"      😍 Leal     Programa de fidelidade
```

### Service Blueprint

Vai além do User Journey Map: **inclui a visão do backstage** (o que o sistema e o time fazem).

```text
CLIENTE         Ações visíveis ao usuário
                    ↓
FRONTSTAGE      Interações com o sistema (UI, API calls)
                    ↓
BACKSTAGE       Ações internas invisíveis ao usuário
                    ↓
PROCESSOS       Sistemas, jobs, integrações
```

**Exemplo (simplificado de uma compra):**

| Fase | Cliente | Frontstage | Backstage | Processos |
|------|---------|------------|-----------|-----------|
| Carrinho | Adiciona item | UI atualiza | Calcula frete | API de frete |
| Pagamento | Preenche dados | Formulário | Valida antifraude | Gateway |
| Confirmação | Recebe email | Tela de sucesso | Gera nota fiscal | ERP |
| Entrega | Rastreia | Tracking page | Logística | Transportadora |

**Para devs:** Service Blueprint mostra que seu código é apenas uma camada. Falhas na integração com ERP, no job de email ou no gateway de pagamento são **falhas de UX** também.

---

## 5. Personas

Personas são **personagens fictícios baseados em dados reais** que representam segmentos de usuários.

### Proto-personas vs Data-driven

```text
Proto-persona                        Data-driven persona
Baseada em hipóteses do time         Baseada em dados reais
Rápida (1 workshop)                  Leva semanas
"Eu acho que o usuário..."           "Os dados mostram que..."
Valida: "Erramos, vamos pesquisar"   Valida: "Confirmamos nossas hipóteses"
```

### Estrutura de uma persona

```yaml
nome:   Dr. Carlos
idade:  42
cargo:  Diretor de TI em empresa de médio porte
stack:  Legado (Java 8, Oracle, mainframe)

Objetivos:
  - Modernizar infra sem parar produção
  - Justificar ROI para o CFO
  - Reduzir em 30% os incidentes críticos

Dores:
  - "Toda mudança é um risco"
  - "Não consigo atrair devs bons por causa do legado"
  - "Pressão da diretoria para inovar"

Frustrações:
  - Ferramentas "modernas" não integram com o legacy
  - Fornecedores não entendem o contexto enterprise
  - Falta tempo para aprender novas stacks

Comportamento digital:
  - Pesquisa no Google antes de comprar
  - Lê relatórios do Gartner e Forrester
  - Participa de webinar, não de evento presencial
```text

### Anti-personas

Usuários que **não são seu público-alvo**. Importante para não desperdiçar esforço.

```text
Anti-persona: "Usuário Free"
- Usa só o plano gratuito
- Abre 3 tickets de suporte por mês
- Dá nota 2 no NPS porque "falta recurso premium"
- Gera custo operacional sem retorno financeiro

O que NÃO fazer: não projetar para ele.
```

### Para devs: personas no código

```typescript
// Mapeamento de personas para feature flags
type Persona = 'admin' | 'dev_individual' | 'gestor_enterprise' | 'suporte';

interface FeatureFlag {
  persona: Persona[];
  rollout: number; // % de usuários
}

const flags: Record<string, FeatureFlag> = {
  'export-csv': {
    persona: ['gestor_enterprise', 'admin'],
    rollout: 100,
  },
  'ai-suggestions': {
    persona: ['dev_individual', 'gestor_enterprise'],
    rollout: 10, // Lançamento gradual
  },
};
```

---

## 6. Acessibilidade (a11y)

Acessibilidade não é um plus — é **requisito legal e moral**. No Brasil, a **Lei Brasileira de Inclusão (LBI)** exige que sites e apps sejam acessíveis.

### WCAG (Web Content Accessibility Guidelines)

As diretrizes se organizam em 4 princípios:

```text
P
├── Perceptível     — O conteúdo deve ser percebível
│   ├── Alternativas textuais para imagens
│   ├── Legendas para vídeos
│   └── Contraste suficiente
│
O
├── Operável        — A interface deve ser operável
│   ├── Navegação por teclado
│   ├── Tempo suficiente para ler
│   └── Não causar convulsões (flash)
│
U
├── Compreensível   — A interface deve ser compreensível
│   ├── Idioma identificado
│   ├── Comportamento previsível
│   └── Tratamento de erros claro
│
R
├── Robusto         — Deve funcionar com tecnologias assistivas
│   ├── HTML semântico
│   ├── ARIA labels
│   └── Funciona com screen readers
```

### Níveis de conformidade

| Nível | Descrição | Exemplo |
|-------|-----------|---------|
| A | Mínimo obrigatório | Alt text em imagens |
| AA | Recomendado (padrão legal) | Contraste 4.5:1 |
| AAA | Avançado | Linguagem de sinais em vídeos |

### Contraste

```text
✅ Bom contraste (AA):
   #333333 sobre #FFFFFF   — texto normal
   #000000 sobre #FFFFFF   — texto grande
   #FFFFFF sobre #0055CC   — botões

❌ Contraste insuficiente:
   #CCCCCC sobre #FFFFFF   — texto cinza claro
   #999999 sobre #EEEEEE   — links desativados
   #FFCC00 sobre #FFFFFF   — alertas amarelos
```

### Navegação por teclado

```typescript
// ❌ Botão que não recebe foco
<div onClick={handleClick}>Salvar</div>

// ✅ Botão nativo com foco
<button onClick={handleClick}>Salvar</button>

// ✅ Se precisar de div, adicione ARIA
<div
  role="button"
  tabIndex={0}
  onClick={handleClick}
  onKeyDown={(e) => e.key === 'Enter' && handleClick()}
>
  Salvar
</div>
```text

### Screen Readers

```html
<!-- ❌ Imagem decorativa sem alt -->
<img src="lupa.png" />

<!-- ✅ Imagem funcional com alt descritivo -->
<img src="lupa.png" alt="Pesquisar" />

<!-- ❌ Ícone sem contexto -->
<button><i class="icon-cog"></i></button>

<!-- ✅ Ícone com aria-label -->
<button aria-label="Configurações"><i class="icon-cog"></i></button>

<!-- ❌ Tabela sem escopo -->
<td>Nome</td>

<!-- ✅ Tabela com scopo -->
<th scope="col">Nome</th>
```

### Para devs: checklist de acessibilidade no código

```typescript
interface A11yChecklist {
  semanticHtml: boolean;    // Usa tags nativas (<nav>, <main>, <button>)
  keyboardNav: boolean;     // Tudo operável por teclado
  focusVisible: boolean;    // Focus ring visível
  ariaLabels: boolean;      // Labels para ações não textuais
  colorContrast: boolean;   // 4.5:1 mínimo (AA)
  reducedMotion: boolean;   // Respeita prefers-reduced-motion
  zoomTested: boolean;      // Funciona com zoom até 200%
}

const checkA11y: A11yChecklist = {
  semanticHtml: false, // ❌ div onclick no lugar de button
  keyboardNav: false,  // ❌ dropdown não abre com Enter
  // ...
};
```text

---

## 7. UX Writing

UX Writing é a **criação de textos para interfaces** que guiam o usuário de forma clara e humana.

### Microtexto

```typescript
// ❌ Texto focado no sistema
"Erro 0x87E50007: Falha na autenticação do certificado"

// ✅ Texto focado no usuário
"Seu login expirou. Faça login novamente para continuar."

// ❌ Técnico e genérico
"Requisição inválida"

// ✅ Claro e acionável
"Preencha todos os campos obrigatórios antes de continuar."
```

### Tom de voz

| Situação | Tom | Exemplo |
|----------|-----|---------|
| Sucesso | Positivo | "Conta criada com sucesso! 🎉" |
| Erro | Empático | "Algo deu errado. Não se preocupe, seus dados estão seguros." |
| Alerta | Direto | "Sua sessão vai expirar em 5 minutos." |
| Confirmação | Neutro | "Tem certeza que deseja excluir este projeto?" |

### Mensagens de erro

```text
❌ "Falha ao processar requisição"
❌ "Ocorreu um erro inesperado"
❌ "Campos inválidos"

✅ "E-mail ou senha incorretos. Tente novamente."
✅ "O servidor não respondeu. Seu rascunho foi salvo automaticamente."
✅ "O campo 'CNPJ' precisa ter 14 dígitos."
```

### Para devs: UX Writing no frontend

```typescript
// ❌ Mensagens de erro hardcoded e genéricas
const errorMessagesOld = {
  400: 'Bad Request',
  401: 'Unauthorized',
  500: 'Internal Server Error',
};

// ✅ Mensagens humanas centralizadas
const errorMessages = {
  400: 'Verifique os dados enviados e tente novamente.',
  401: 'Sua sessão expirou. Faça login novamente.',
  403: 'Você não tem permissão para essa ação.',
  404: 'O recurso solicitado não foi encontrado.',
  409: 'Já existe um registro com esses dados.',
  422: 'Corrija os campos destacados e tente novamente.',
  429: 'Muitas requisições. Aguarde alguns segundos.',
  500: 'Erro interno. Nossa equipe foi notificada.',
  502: 'Serviço temporariamente indisponível. Tente novamente.',
  503: 'Manutenção programada. Volte em instantes.',
};
```text

### Princípios de UX Writing

```text
CLARO          → "Salvar" (não "Persistir alterações no repositório")
CONCISO        → "E-mail inválido" (não "O endereço de e-mail digitado não é válido")
ÚTIL           → "Digite seu e-mail corporativo" (orienta, não só rotula)
CONSISTENTE    → Sempre "Excluir", não "Excluir"/"Remover"/"Deletar" aleatoriamente
HUMANO         → "Algo deu errado, mas já estamos cuidando disso"
```

---

## 8. Heurísticas de Nielsen

As 10 heurísticas são **critérios de usabilidade** que funcionam como checklist para avaliar qualquer interface.

### As 10 Heurísticas

```text
1. VISIBILIDADE DO STATUS DO SISTEMA
   "O sistema deve sempre informar o que está acontecendo."
   ❌ Clica em "Salvar" e nada acontece por 10s
   ✅ Spinner + "Salvando..." + "Salvo!" com timestamp

2. CORRESPONDÊNCIA COM O MUNDO REAL
   "Use linguagem do usuário, não do sistema."
   ❌ "Diretório raiz do repositório"
   ✅ "Pasta principal do projeto"

3. CONTROLE E LIBERDADE DO USUÁRIO
   "O usuário deve poder desfazer ações."
   ❌ Excluiu sem confirmação, sem undo
   ✅ "Excluir → Confirmar → Desfazer (5s)"

4. CONSISTÊNCIA E PADRÕES
   "Mesma palavra = mesma ação em todo o sistema."
   ❌ "Excluir" em um lugar, "Apagar" em outro
   ✅ Sempre "Excluir" + ícone de lixeira

5. PREVENÇÃO DE ERROS
   "Melhor que uma boa mensagem de erro é nenhum erro."
   ❌ Data digitada livremente e depois valida
   ✅ Datepicker que já impede data inválida

6. RECONHECIMENTO EM VEZ DE RECORDAÇÃO
   "Mostre opções, não force o usuário a lembrar."
   ❌ Campo "Categoria" em branco
   ✅ Dropdown com as categorias existentes

7. FLEXIBILIDADE E EFICIÊNCIA DE USO
   "Atenda novatos e experts."
   ❌ Mesmo fluxo para todos
   ✅ Atalhos de teclado para experts, wizard para novatos

8. DESIGN ESTÉTICO E MINIMALISTA
   "Cada informação extra compete com a informação relevante."
   ❌ Dashboard com 20 gráficos
   ✅ Top 5 métricas que importam

9. AJUDE USUÁRIOS A RECONHECER, DIAGNOSTICAR E RECUPERAR DE ERROS
   "Mensagens de erro claras e acionáveis."
   ❌ "Erro 500"
   ✅ "Serviço indisponível. Tente novamente em alguns minutos."

10. AJUDA E DOCUMENTAÇÃO
    "Se o usuário precisa de ajuda, ela deve estar disponível."
    ❌ Documentação escondida
    ✅ "?" contextual + FAQ + chat
```

### Como avaliar com as heurísticas

```typescript
type HeuristicSeverity = 0 | 1 | 2 | 3 | 4;

interface HeuristicEvaluation {
  heuristic: string;
  severity: HeuristicSeverity;
  finding: string;
  suggestion: string;
}

// Severidade:
// 0 = não é problema
// 1 = problema cosmético
// 2 = problema menor
// 3 = problema grave (deve ser corrigido)
// 4 = catástrofe (uso impossível)

const evaluation: HeuristicEvaluation[] = [
  {
    heuristic: '1. Visibilidade do status',
    severity: 3,
    finding: 'Botão "Exportar" não mostra progresso',
    suggestion: 'Adicionar barra de progresso + notificação ao finalizar',
  },
  {
    heuristic: '9. Mensagens de erro',
    severity: 4,
    finding: 'Erro 500 sem mensagem ao usuário',
    suggestion: 'Mensagem amigável + log no backend',
  },
];
```

---

## 9. UX para Devs

### Mentalidade centrada no usuário

```text
ANTES                             DEPOIS
"O usuário vai aprender"          "Como tornar isso intuitivo?"
"Está no requisito"              "O usuário realmente precisa disso?"
"Funciona no meu ambiente"       "Funciona para o usuário real?"
"O design está errado"           "Qual problema estamos resolvendo?"
```

### Como colaborar com designers

| Situação | Faça | Não faça |
|----------|------|----------|
| Recebeu um design | Pergunte "qual o fluxo do usuário?" | Comece a codificar sem entender |
| Conflito de implementação | Mostre dados (tempo, performance) | Fale "não dá pra fazer" sem alternativas |
| Review de design | Aponte violações de acessibilidade | Critique cor ou fonte |
| Entrega de funcionalidade | Valide com teste rápido de usabilidade | Considere pronto só porque compilou |
| Refinamento | Leve dados de analytics/feedback | Apenas "o PO pediu" |

### Checklist para devs

```markdown
## Antes de codificar
- [ ] Entendi o problema do usuário (não só a solução)
- [ ] Verifiquei se existem dados/entrevistas que embasam a demanda
- [ ] Questionei: "essa é a melhor forma de resolver?"

## Durante o código
- [ ] Componentes são acessíveis (teclado, screen reader)
- [ ] Mensagens de erro são humanas e acionáveis
- [ ] Estados vazios, loading e erro estão tratados
- [ ] Contraste mínimo 4.5:1
- [ ] Microinterações informam o status do sistema

## Antes do deploy
- [ ] Testei com teclado apenas (sem mouse)
- [ ] Testei com zoom de 200%
- [ ] Textos estão consistentes (mesmo label para mesma ação)
- [ ] Performance: < 3s para carregar (mobile)
```text

### Exemplo prático: refatorando uma feature com mentalidade UX

```typescript
// ❌ Antes: feature-centrica
function TelaRelatorios() {
  const [relatorios] = useQuery(GET_RELATORIOS);
  return <Table data={relatorios} />;
  // Usuário: "e agora? o que eu faço com isso?"
}

// ✅ Depois: centrada no usuário
function TelaRelatorios() {
  const [relatorios, { loading, error }] = useQuery(GET_RELATORIOS);
  const [search, setSearch] = useState('');
  const filtered = relatorios.filter(r => r.name.includes(search));

  if (loading) return <Skeleton lines={5} aria-label="Carregando relatórios" />;
  if (error) return <ErrorAlert message="Não foi possível carregar. Tente novamente." />;
  if (filtered.length === 0) return <EmptyState message="Nenhum relatório encontrado. Crie o primeiro." />;

  return (
    <Page>
      <SearchInput
        value={search}
        onChange={setSearch}
        placeholder="Buscar relatório por nome..."
        aria-label="Buscar relatórios"
      />
      <Table
        data={filtered}
        emptyMessage="Nenhum resultado para essa busca"
      />
    </Page>
  );
}
```

### Perguntas que todo dev deveria fazer

```text
1. "Qual o objetivo do usuário nesta tela?"
2. "O que acontece se der erro?"
3. "Como um usuário novato se sentiria aqui?"
4. "Isso funciona sem JavaScript?"
5. "O usuário consegue desfazer essa ação?"
6. "Onde o usuário vai procurar essa funcionalidade?"
7. "Em quanto tempo isso carrega no 3G?"
```

---

## Resumo

| Tópico | Principal aprendizado |
|--------|-----------------------|
| UX vs UI | UX é a experiência completa; UI é a superfície visual |
| 5 Planos | Estratégia → Escopo → Estrutura → Esqueleto → Superfície |
| Pesquisa | Entreviste para entender, não para validar |
| IA | Organize conteúdo como o usuário espera |
| Jornada | Mapeie emoções, não só cliques |
| Personas | Baseie em dados, não em achismo |
| Acessibilidade | WCAG AA é o mínimo legal |
| UX Writing | Mensagens claras, concisas e humanas |
| Heurísticas | 10 critérios para avaliar qualquer interface |
| Dev + UX | Pergunte "por quê" antes de codificar |
