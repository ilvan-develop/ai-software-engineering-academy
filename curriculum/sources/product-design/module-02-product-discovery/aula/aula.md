# Módulo 02 — Product Discovery: Validando Ideias Antes de Construir

**Descubra o que construir antes de construir.**

---

## 1. O que é Product Discovery?

Product Discovery é o processo de **entender problemas reais de usuários reais antes de escrever uma linha de código**. O objetivo não é entregar features, mas sim **decidir o que vale a pena ser construído**.

### Discovery vs Delivery

```text
DISCOVERY                             DELIVERY
"Construímos a coisa certa?"          "Construímos a coisa certo?"
Alta incerteza, baixo custo           Baixa incerteza, alto custo
Perguntas, hipóteses, experimentos    Requisitos, planejamento, código
Falsificável, iterativo               Definido, incremental
"Devo construir isso?"                "Como construir isso?"
```javascript

![Discovery vs Delivery](/knowledge-factory/products/courses/product-design/module-02-product-discovery/assets/diagram-discovery-vs-delivery.svg)

### Por que Discovery é importante?

```text
Sem Discovery:
  "O cliente pediu uma tela de relatório"
  → 3 sprints de desenvolvimento
  → Ninguém usa
  → 3 sprints perdidos

Com Discovery:
  "O cliente pediu uma tela de relatório"
  → Entrevista: "Qual problema você quer resolver?"
  → Descoberta: ele quer exportar dados pra planilha
  → Solução: botão de exportar CSV em 1 dia
  → Valida: ele testa, funciona, usa todo dia
```markdown

### Armadilha comum

```text
Time: "Vamos construir um chat bot!"
Discovery: Nenhum

3 meses depois:
Ninguém usa o chat bot.

Por quê?
- Ninguém perguntou se o problema era real
- Ninguém validou se chat bot era a melhor solução
- Ninguém testou com usuários antes de construir
```markdown

![Mapa mental do Product Discovery](/knowledge-factory/products/courses/product-design/module-02-product-discovery/assets/diagram-discovery-mindmap.svg)

---

## 2. Processo de Discovery

O discovery não é linear — é um ciclo iterativo. O modelo mais comum tem 4 fases:

```text
OPORTUNIDADE → PESQUISA → IDEAÇÃO → PROTOTIPAÇÃO → VALIDAÇÃO
      │                                                 │
      └───────────────── (iterate) ────────────────────┘
```markdown

![Processo de Product Discovery](/knowledge-factory/products/courses/product-design/module-02-product-discovery/assets/diagram-discovery-flow.svg)

### 2.1 Oportunidades

Toda feature request, bug report, reclamação de cliente ou insight de analytics é uma **oportunidade**. O desafio é priorizá-las.

**Fontes de oportunidades:**
- Feedback de clientes (Zendesk, Intercom, surveys)
- Dados de uso (amplitude, mixpanel, GA4)
- Conversas com sales/suporte
- Análise concorrencial
- Visão do produto (OKRs, estratégia)
- Próprio time (dívida técnica, bugs recorrentes)

### 2.2 Pesquisa

Antes de pensar em solução, **entenda o problema**. Use técnicas qualitativas e quantitativas (ver seção 3).

### 2.3 Ideação

Gere múltiplas opções de solução, não apenas uma. Técnicas:
- **Crazy 8s** — 8 ideias em 8 minutos
- **Brainstorming** — quantidade > qualidade, sem julgamento
- **Design Sprint** — Google Ventures, 5 dias
- **How Might We** — reformular problema como pergunta

```text
Problema: "Usuários não completam o cadastro"
HMW: "Como poderíamos reduzir o atrito no cadastro?"
     → "Como poderíamos deixar o cadastro opcional?"
     → "Como poderíamos usar login social?"
     → "Como poderíamos pré-preencher dados?"
```markdown

### 2.4 Prototipação

Crie representações da solução com o mínimo esforço necessário para testar:

```text
Nível         Esforço    O que testa
───           ───────    ──────────
Sketch        Minutos    Fluxo macro
Wireframe     Horas      Layout, estrutura
Mockup        Dias       Visual, branding
Prototype     Dias       Interação, fluxo real
MVP           Semanas    Valor real no mercado
```markdown

### 2.5 Validação

Cada protótipo precisa ser testado com usuários reais. Se a hipótese não for validada, volte para ideação.

---

## 3. Técnicas de Pesquisa

### 3.1 Entrevistas com usuários

A ferramenta mais poderosa de discovery.

**Estrutura de uma entrevista:**

```text
1. Abertura (5min)
   "Obrigado por participar. Não estamos testando você.
    Queremos entender como você lida com [assunto].
    Pode ser sincero — críticas nos ajudam."

2. Contexto (10min)
   "Me conta como é seu dia a dia com [assunto]."
   "O que você mais usa hoje?"
   "O que te frustra?"

3. Profundidade (20min)
   "Me conta da última vez que você passou por [situação]."
   "O que você fez? O que aconteceu?"
   "Se pudesse mudar uma coisa, o que seria?"

4. Fechamento (5min)
   "Algo mais que gostaria de compartilhar?"
   "Posso voltar a te procurar se tiver mais perguntas?"
```text

**Regras de ouro:**
- Não faça perguntas indutoras ("Você não acha que X é melhor?")
- Não pergunte "você usaria?" (todo mundo diz sim)
- Pergunte sobre **comportamento passado**, não intenção futura
- Escute mais do que fala (ratio 80/20)

### 3.2 Surveys

Bom para validar achados qualitativos com escala.

```text
❌ "Você usaria uma funcionalidade de exportar relatórios?"
   (todo mundo diz sim — viés de cortesia)

✅ "Na última semana, quantas vezes você precisou exportar
    dados do sistema?"
   (comportamento real, mensurável)
```text

**Dicas de surveys:**
- Máximo 10 perguntas
- Escalas consistentes (Likert 1-5 ou 1-7)
- Sempre incluir pergunta aberta no final
- Ferramentas: Typeform, Google Forms, SurveyMonkey

### 3.3 Análise Concorrencial

```text
Concorrente A          Concorrente B            Concorrente C
──────────────────     ──────────────────       ──────────────────
Faz X bem              Faz Y bem                Faz Z bem
Não tem W              Tem W mas é confuso      Tem W excelente
Feedback: lento        Feedback: caro           Feedback: complexo

Oportunidade: X + W simples + preço acessível
```text

**O que analisar:**
- Proposta de valor
- Fluxos principais
- Pontos fortes e fracos
- Reviews (G2, Capterra, Play Store, App Store)
- Pricing e posicionamento

### 3.4 Analytics

Dados quantitativos não mentem — mas precisam de interpretação.

```text
Métricas de Discovery:

| Métrica                  | O que indica                             |
|--------------------------|------------------------------------------|
| Page views               | Interesse bruto                          |
| Bounce rate              | Não encontrou o que queria               |
| Drop-off por etapa       | Atrito no fluxo                          |
| Funil de conversão       | Onde os usuários desistem                |
| Retenção D1/D7/D30       | Valor entregue vs expectativa            |
| NPS / CSAT               | Satisfação geral                         |
| Search terms             | O que usuários procuram (e não acham)    |
| Feature usage            | O que realmente é usado                  |
```markdown

---

## 4. Frameworks de Discovery

### 4.1 JTBD — Jobs to be Done

JTBD parte da premissa: **usuários não compram produtos, eles contratam serviços para fazer um trabalho**.

```text
Exemplo:

Job: "Me manter informado sobre tecnologia"
──────────────────────────────────────────────

Opção A: Assinar newsletter        (R$ 0,  5min/dia)
Opção B: Seguir influencers         (R$ 0, 15min/dia)
Opção C: Assinar portal de tech    (R$ 30/mês, 30min/dia)
Opção D: Podcasts                  (R$ 0, 1h/dia no trânsito)

"Contratamos" a opção que melhor resolve o job
dado nosso contexto (tempo, dinheiro, momento)
```text

**Estrutura JTBD:**

```text
Quando [situação], eu quero [motivação] para [resultado esperado].

Exemplo:
"Quando estou começando um novo projeto, eu quero entender o
que outros times já tentaram antes, para não repetir erros."
```text

**Jobs principais vs jobs funcionais:**
- **Functional:** "Organizar tarefas do time"
- **Emocional:** "Me sentir no controle do projeto"
- **Social:** "Parecer competente para meu chefe"

### 4.2 Lean Canvas

Uma página que resume o modelo de negócio. Ideal para early stage.

```text
┌─────────────────┬────────────────┬─────────────────┬─────────────────┬─────────────────┐
│ PROBLEMA        │ SOLUÇÃO        │ PROPOSTA DE     │ VANTAGEM         │ SEGMENTO        │
│ Top 3 problemas │ Top 3 soluções │ VALOR           │ COMPETITIVA       │ DE CLIENTES     │
│                 │                │ Única           │ Não copiável      │                  │
│                 │                │ Mensagem clara  │ facilmente        │                  │
├─────────────────┼────────────────┼─────────────────┼─────────────────┼─────────────────┤
│ MÉTRICAS        │                │ CANAIS          │                   │                  │
│ CHAVE           │                │                 │                   │                  │
│ O que medir     │                │ Como chegar     │                   │                  │
│ para saber se   │                │ no cliente      │                   │                  │
│ está dando certo│                 │                 │                   │                  │
├─────────────────┴────────────────┴─────────────────┴─────────────────┴─────────────────┤
│ ESTRUTURA DE CUSTOS                                │ RECEITAS                         │
│ Fixos, variáveis, custo de aquisição               │ Como ganha dinheiro              │
└────────────────────────────────────────────────────┴─────────────────────────────────┘
```markdown

### 4.3 Value Proposition Canvas

Detalha o encaixe entre o cliente e o produto.

```text
VALUE PROPOSITION CANVAS

┌──────────────────────────────┬──────────────────────────────┐
│ PRODUTO                      │ CLIENTE                      │
│                              │                              │
│ ┌────────────────────────┐   │ ┌────────────────────────┐  │
│ │ Gain Creators          │   │ │ Gains                   │  │
│ │ O que entrega ganhos   │   │ │ Resultados desejados   │  │
│ │                        │   │ │                         │  │
│ ├────────────────────────┤   │ ├────────────────────────┤  │
│ │ Products & Services    │   │ │ Customer Jobs          │  │
│ │ O que oferecemos       │   │ │ O que ele quer fazer   │  │
│ │                        │   │ │                         │  │
│ ├────────────────────────┤   │ ├────────────────────────┤  │
│ │ Pain Relievers         │   │ │ Pains                   │  │
│ │ O que alivia dores     │   │ │ Frustrações, riscos    │  │
│ └────────────────────────┘   │ └────────────────────────┘  │
│                              │                              │
│         ENCAIXE: quando solutions > jobs + pains           │
└──────────────────────────────┴──────────────────────────────┘
```markdown

---

## 5. Mapeamento

### 5.1 Opportunity Solution Tree (Teresa Torres)

Árvore que conecta **oportunidades → soluções → experimentos**.

```text
RESULTADO ESPEREADO
(reduzir churn em 20%)
│
├── OPORTUNIDADE: Usuários não entendem o valor do produto
│   ├── SOLUÇÃO: Onboarding guiado
│   │   └── EXPERIMENTO: Teste A/B com novo onboarding vs atual
│   └── SOLUÇÃO: Vídeo de apresentação no primeiro login
│       └── EXPERIMENTO: Medir % que completa o vídeo
│
├── OPORTUNIDADE: Usuários não conseguem exportar dados
│   ├── SOLUÇÃO: Botão de exportar CSV
│   │   └── EXPERIMENTO: Protótipo clicável com 5 usuários
│   └── SOLUÇÃO: Integração com Google Sheets
│       └── EXPERIMENTO: Survey de interesse com clientes
│
└── OPORTUNIDADE: Produto é caro para PMEs
    ├── SOLUÇÃO: Plano "Starter" com funcionalidades limitadas
    └── EXPERIMENTO: Landing page com pricing e botão de compra
```text

**Como construir:**
1. Defina o **outcome** (resultado esperado, ex: "aumentar ativação em 30%")
2. Liste **oportunidades** (problemas/dores que impedem o outcome)
3. Para cada oportunidade, gere **soluções**
4. Para cada solução, defina um **experimento** para testar

### 5.2 User Story Mapping

Técnica de Jeff Patton que organiza o backlog em **atividades do usuário** de forma visual, ajudando o time a enxergar o produto como um fluxo.

```text
Jornada: "Gerenciar projetos"
────────────────────────────────────────────────────────────────────
              │  Semana 1     │  Semana 2    │  Semana 3      │
──────────────┼───────────────┼──────────────┼────────────────┤
Criar projeto │ Criar nome    │ Convidar     │                │
              │               │ membros      │                │
──────────────┼───────────────┼──────────────┼────────────────┤
Organizar     │ Criar         │ Adicionar    │ Arrastar       │
tarefas       │ colunas       │ cards        │ cards          │
──────────────┼───────────────┼──────────────┼────────────────┤
Acompanhar    │               │              │ Dashboard     │
progresso     │               │              │ de progresso   │
──────────────┴───────────────┴──────────────┴────────────────┘
  ↑ MVP (corta aqui)            ↑ Release 2          ↑ Release 3
```text

**Por que usar:**
- Mostra o produto como um **fluxo**, não uma lista
- Ajuda a identificar **gaps** no fluxo
- Facilita decisões de **MVP** (o corte vertical)
- Alinha time e stakeholders visualmente

---

## 6. Validação de Hipóteses

### Estrutura de hipótese

```text
HIPÓTESE:
Acreditamos que [solução] para [público]
resultará em [outcome].
Saberemos que estamos certos quando [métrica/meta].

Exemplo:
"Acreditamos que um onboarding guiado para novos usuários
resultará em 30% mais ativação no D7.
Saberemos que estamos certos quando a taxa de ativação
subir de 40% para 52% no teste A/B."
```markdown

### Tipos de experimento

```text
Experimento         | Esforço | Confiança | Quando usar
────────────────────|─────────|───────────|────────────────────────
Entrevista          | Baixo   | Média     | Entender problema
Landing page fake   | Baixo   | Alta      | Testar interesse real
Prototype test      | Médio   | Média     | Validar usabilidade
Teste A/B           | Médio   | Alta      | Comparar soluções
Concierge MVP       | Alto    | Alta      | Validar valor real
Wizard of Oz MVP    | Médio   | Alta      | Validar viabilidade
Single-feature MVP  | Médio   | Alta      | Testar feature isolada
Piecemeal MVP       | Baixo   | Média     | Validar sem construir
```markdown

### Exemplo: Landing page fake

```text
Ideia: "App que agenda reuniões automaticamente"

1. Criar landing page:
   "Agende reuniões sem trocar emails"

2. Botão: "Começar gratis →" (leva a página de "em breve")

3. Métricas:
   - Visitantes que chegam na página
   - % que clica no CTA      ← indicador de interesse real
   - % que deixa o email      ← lead qualificado

4. Resultado:
   Se < 5% clica → interesse baixo, repense a proposta
   Se > 15% clica → interesse real, continue
```markdown

### MVP não é produto mínimo

```text
MITO: MVP é a versão mais simples do produto final
REAL: MVP é o menor experimento que valida ou invalida uma hipótese

MVP serve para APRENDER, não para entregar valor.
Se você já sabe que funciona, não precisa de MVP.
```markdown

---

## 7. Product Discovery no Contexto Enterprise

Discovery em empresas grandes tem desafios específicos.

### Desafios Enterprise

```text
Desafio                    Impacto no Discovery
────────────────────────── ──────────────────────────────────
Muitos stakeholders        Múltiplas visões do que é "prioridade"
Processos burocráticos     Discovery lento, pouca iteração
Métrica de sucesso errada  Time mede output, não outcome
Times isolados             Descobertas não são compartilhadas
Gerenciamento de risco     Medo de errar → pouca experimentação
Orçamento anual fixo       Discovery não é orçado → não existe
```markdown

### Como fazer discovery em Enterprise

**1. Alinhe com OKRs**

```text
OKR da empresa: "Aumentar receita recorrente em 25%"

→ Opportunity: churn de 15% ao mês
→ Discovery: por que os clientes estão cancelando?
→ Outcome: reduzir churn pela metade
→ Backlog: funcionalidades que endereçam as causas
```text

**2. Discovery Sprints**

Reserve ciclos fixos para discovery (ex: 2 semanas a cada quarter).

```text
Sprint Discovery (2 semanas):
  Semana 1: Pesquisa (entrevistas, analytics, concorrência)
  Semana 2: Ideação, prototipação, testes com usuários
  Saída: Backlog priorizado para as próximas 6 semanas de delivery
```text

**3. Envolva stakeholders cedo**

```text
Stakeholder      | O que quer saber                   | Quando envolver
─────────────────|────────────────────────────────────|─────────────────
Diretor          | "Isso entrega o OKR?"              | Kickoff, review
Produto          | "Isso resolve o problema certo?"   | Discovery inteiro
Engenharia       | "Isso é viável tecnicamente?"      | Prototipação
Design           | "Isso é usável?"                    | Prototipação, teste
Comercial        | "O cliente pagaria por isso?"      | Pesquisa, validação
Sucesso do cl.   | "Isso reduz chamados?"             | Pesquisa
```text

**4. Discovery contínuo vs Discovery por projeto**

```text
Discovery Contínuo (recomendado):
  Discovery e Delivery rodam em paralelo
  Time sempre tem 20-30% do tempo para discovery
  Pipeline de oportunidades sempre abastecido

Discovery por Projeto (menos eficaz):
  Discovery só acontece no início do projeto
  Depois que o delivery começa, não se questiona mais
  Se descobrir algo errado no meio, é tarde demais
```markdown

### Cultura de Experimentação

Empresas maduras em discovery têm:

```text
Amazon:        "É mais fácil pedir desculpas do que permissão"
Netflix:       Testa tudo, aprende rápido, falha barato
Spotify:       Squads têm autonomia para discovery
Google:        Data beats opinions
Airbnb:        Design ops com discovery contínuo

Cultura que NÃO funciona:
  "Quem decide é o VP"
  "A gente sabe o que o cliente quer"
  "Se deu trabalho, vamos lançar mesmo assim"
```markdown

---

## 8. Saídas do Discovery

O discovery não termina sem artefatos. As saídas principais são:

### 8.1 Backlog Refinado

Um backlog que não é só lista de desejos — é priorizado por evidência.

```text
Antes do Discovery:
  - [ ] Tela de relatórios (pedido pelo stakeholder)
  - [ ] Exportar para PDF (ideia do PO)
  - [ ] Modo escuro (sugestão do dev)
  - [ ] Integração com Slack (pedido de 1 cliente)

Depois do Discovery:
  - [ ] Exportar CSV (validado: 78% dos usuários precisam)
  - [ ] Relatório de vendas (validado: resolve job #2)
  - [ ] Tema escuro (despriorizado: 12% pediram)
  - [ ] Integração Slack (despriorizado: 3 clientes, custo alto)
```markdown

### 8.2 Proto-personas

Persona provisória baseada em hipóteses, não em pesquisa extensa.

```text
Proto-persona: Analista de Dados
───────────────────────────────────────────────────────────────
Nome fictício:   Carla, 32 anos
Cargo:           Analista de BI Sênior
Contexto:        Trabalha em empresa de médio porte, time pequeno
Objetivo:        Extrair insights rápido para tomar decisões
Dores:           1. Dados espalhados (planilhas, BI, ERP)
                 2. Demora dias para gerar um relatório
                 3. Não confia na qualidade dos dados
Comportamento:   Usa Excel, Tableau, SQL (básico)
Job to be done:  "Quando preciso responder uma pergunta de negócio,
                  quero encontrar os dados certos em minutos, para
                  não perder credibilidade com o diretor."
```markdown

### 8.3 User Stories

Histórias baseadas em evidência, não em suposição.

```text
❌ Sem Discovery:
"Como usuário, quero uma tela de relatórios."

✅ Com Discovery:
"Como analista de BI, quero exportar dados em CSV
para poder analisar no Excel, porque meu time não
tem acesso direto ao banco."

Critérios de aceite:
- Botão de exportar na tela de search
- Formato CSV com encoding UTF-8
- Arquivo baixa em até 10s (para < 100k linhas)
- Colunas traduzidas para pt-BR
- Nome do arquivo: `export-{tipo}-{data}.csv`
```markdown

### 8.4 Opportunity Backlog

Um backlog de oportunidades (não de soluções).

```text
ID  | Oportunidade                              | Evidência              | Tamanho | Prioridade
────|───────────────────────────────────────────|────────────────────────|─────────|───────────
O01 | Usuários não encontram dados no sistema   | 45% dos chamados       | Grande  | P0
O02 | Demora para gerar relatórios              | Survey: 78% citaram    | Médio   | P0
O03 | Não confiabilidade dos dados              | NPS: 4.2 (crítico)     | Grande  | P1
O04 | Integração com ferramentas externas       | 3 clientes enterprise  | Médio   | P2
```markdown

---

## Resumo

1. **Product Discovery** é o processo de validar problemas e soluções antes de construir
2. **Discovery vs Delivery**: uma decide o que construir, a outra constrói
3. **Ciclo**: Oportunidade → Pesquisa → Ideação → Prototipação → Validação
4. **Pesquisa**: entrevistas, surveys, análise concorrencial, analytics
5. **Frameworks**: JTBD, Lean Canvas, Value Proposition Canvas
6. **Mapeamento**: Opportunity Solution Tree, User Story Mapping
7. **Hipóteses**: estruture, meça, aprenda (MVP = experimento, não produto)
8. **Enterprise**: alinhe com OKRs, envolva stakeholders, cultura de experimentação
9. **Saídas**: backlog refinado, proto-personas, user stories, opportunity backlog
