# O erro que 90% cometem ao usar IA para programar

**5 erros — e como corrigir cada um**

[imagem: um desenvolvedor encarando duas telas — uma com código gerado por IA, outra com um alerta de bug — expressão de surpresa]

*Muito provavelmente você já cometeu todos os 5 erros que vamos ver hoje. A diferença? Depois deste slide, você vai saber exatamente como evitar cada um. Vamos nessa.*

---

## O problema em números

| Dado | 
|------|
| **63%** dos devs encontraram erros inesperados ao usar IA |
| **68%** têm dificuldade em integrar IA nos workflows |
| **Sem regras**, código gerado por IA tem **~40% de erro** |
| **Com 12 regras**, o erro cai para **~3%** — melhoria de **~13x** |

Fontes: Stack Overflow Survey · Claude Code Pro Pack Research

[imagem: gráfico de barras comparando 40% vs 3% de taxa de erro, com destaque no improvement de 13x]

*A IA não é o problema. O problema é como usamos ela. Esses números são o resumo de milhares de desenvolvedores ao redor do mundo repetindo os mesmos erros. Vamos ao primeiro.*

---

## Erro #1: Confiar cegamente na saída da IA

Aceitar o código gerado sem questionamento, validação ou revisão.

**Por que acontece:** a IA gera respostas com alta fluência — o código *parece* certo, compila, passa em testes simples... mas pode conter bugs sutis de lógica, segurança ou performance.

> "A IA erra com confiança, não com hesitação."

| Tipo de bug | Exemplo |
|-------------|---------|
| **Lógica** | Validar email só com `includes('@')` |
| **Segurança** | SQL injection, senha em MD5 |
| **Performance** | Loop aninhado desnecessário |
| **Compatibilidade** | Biblioteca que não existe mais |

[imagem: cérebro humano com uma seta escrita "fluência = competência" — e um alerta "FALSO" cruzando a seta]

*Nosso cérebro associa fluência a competência. Quando a IA escreve algo que "soa bem", relaxamos a guarda. Só que ela não sabe o que está fazendo — está apenas completando padrões estatísticos. Cada linha merece seu olhar crítico.*

---

## Erro #2: Prompts vagos sem contexto

Fazer pedidos genéricos e esperar respostas precisas.

**Prompt vago** ❌ — "Melhore esse código"
*A IA não sabe: linguagem, critério de "melhor", contexto do projeto*

**Prompt estruturado** ✅ — *Arquivo + ação + restrições*

| Elemento | Pergunta guia |
|----------|---------------|
| **Contexto** | Qual é o cenário? |
| **Intenção** | O que você quer alcançar? |
| **Formato** | Como deve ser a resposta? |

[imagem: balões de diálogo — um com "Me recomenda um filme" (genérico) vs "Me recomenda um suspense coreano com <2h" (específico)]

*Pedido fraco, resposta fraca em escala industrial. Antes de escrever um prompt, pergunte: "Se eu desse isso para um colega dev, ele saberia exatamente o que fazer?" Se a resposta for não, adicione contexto.*

---

## Erro #3: Pular code review e testes

Ignorar revisão e testes automatizados para código gerado por IA.

**Por que acontece:** a velocidade da IA cria a ilusão de que o código passou por um controle de qualidade implícito.

> "Se você copia e cola sem ler, o erro deixa de ser da ferramenta. Passa a ser seu."

**Como corrigir:**
1. Code review obrigatório — "Eu aceitaria isso num PR?"
2. Testes automatizados como verificação
3. CI pipeline — mesmo check para todo código

[imagem: um PR aberto com código gerado por IA, sem reviews, com um grande "MERGE" em vermelho — e ao lado o mesmo PR com 3 aprovações e checks verdes]

*Pular code review em código de IA não economiza tempo. Ele terceiriza o risco para você. O bug vai aparecer, a pergunta vai ser "quem autorizou?", e a resposta será seu nome no commit.*

---

## Erro #4: Ignorar configuração do projeto (AGENTS.md)

Não configurar arquivos de instrução para os agentes de IA.

Sem `AGENTS.md` ou `CLAUDE.md`, a IA opera com **conhecimento genérico**. Ela não sabe se o projeto usa React 18 ou Vue 3, `const` ou `function`, Vitest ou Jest. **Ela chuta.**

> "5 minutos de configuração economizam horas de retrabalho."

**Estrutura mínima:**
- Stack (React 18 + TS + Tailwind)
- Regras (arrow functions, `const`, kebab-case)
- Padrões (Result<T,E>, sem throw)

[imagem: duas colunas — lado esquerdo IA perdida sem instruções, lado direito IA organizada com um checklist do projeto]

*Seu projeto atual tem um arquivo de instruções para a IA? Se não, esse pode ser o erro que você está cometendo sem perceber. Invista 5 minutos agora. É o maior ROI por minuto no uso de IA para programar.*

---

## Erro #5: Tratar IA como resposta final

Usar a primeira resposta da IA como solução definitiva, sem refinamento.

> "A primeira resposta raramente é a melhor. Ela é o ponto de partida, não o produto final."

**Processo iterativo:**
1. Obtenha a primeira versão (rascunho)
2. Revise e identifique melhorias
3. Refine com feedback direcionado
4. Repita até passar nos critérios

**Dado:** feedback estruturado reduz em **~35% as iterações** (SFEIR Institute)

[imagem: refinamento de uma escultura — bloco bruto → forma aproximada → detalhes finos → obra finalizada, com a IA nos estágios iniciais]

*Não reescreva o prompt do zero. Itera com feedback: "Mude para camelCase", "Extraia para um hook", "Adicione tratamento para lista vazia". A IA aprende com o direcionamento.*

---

## Os 5 erros lado a lado

| # | Erro | Consequência | Correção |
|---|------|-------------|----------|
| 1 | Confiar cegamente | Bugs em produção | Leia + teste cada linha |
| 2 | Prompt vago | Respostas genéricas | Contexto + intenção + formato |
| 3 | Pular code review | Dívida técnica + bugs | Revise + automatize testes |
| 4 | Ignorar AGENTS.md | Comportamento inconsistente | 5 min de setup na raiz |
| 5 | IA como resposta final | Resultados superficiais | Itere com feedback |

[imagem: tabela visual colorida com 5 linhas, cada erro em uma cor diferente, ícones de alerta ao lado]

*Essa tabela é seu resumo de bolso. Decore esses 5 padrões. Quando você se pegar fazendo qualquer um deles, já sabe: é hora de pausar e corrigir a rota.*

---

## Os 5 mandamentos do uso correto de IA

| # | Mandamento |
|---|------------|
| 1 | **Valide** toda saída da IA |
| 2 | **Estruture** prompts com contexto |
| 3 | **Revise e teste** como qualquer código |
| 4 | **Configure** o projeto para a IA |
| 5 | **Itere**, não aceite a primeira resposta |

**Impacto comprovado:** ~35% menos iterações · ~97% de acerto com 12 regras

[imagem: duas tábuas de pedra estilo "Os Dez Mandamentos", mas com 5 mandamentos de boas práticas com IA]

*Não é teoria. São dados. Desenvolvedores que aplicam esses 5 mandamentos reduzem drasticamente erros e retrabalho. É um antes e depois na forma de programar com IA.*

---

## O impacto da configuração

| Configuração | Taxa de erro | Melhoria |
|-------------|:------------:|:--------:|
| Sem regras | ~40% | — |
| Com 4 regras básicas | ~11% | ~3,6x |
| Com 12 regras | ~3% | ~13,3x |

Fonte: Claude Code Pro Pack Research (DEV.to)

[imagem: gráfico de linha descendente — 40% → 11% → 3% — com um ícone de escudo crescendo a cada degrau]

*40% de erro sem configuração. 3% com 12 regras. São 13x menos erros só por escrever um arquivo de instruções. Se você fizer uma única coisa hoje depois desta palestra, que seja criar o AGENTS.md do seu projeto.*

---

## Fluxo ideal de uso de IA

```
[Prompt Estruturado] → [IA gera rascunho] → [Code Review] → [Testes] → [Refinamento] → [Commit]
        ↑                                                                                    |
        └────────────────── Iteração (feedback) ────────────────────────────────────────────┘
```

**A analogia:** IA é como um estagiário brilhante, mas inexperiente. Trabalha rápido, escreve bem, mas precisa de supervisão, contexto e revisão constantes.

[imagem: diagrama de fluxo visual com ícones — teclado (prompt) → robô (IA) → lupa (review) → checklist (testes) → seta em loop (refinamento) → check verde (commit)]

*Confiar cegamente no estagiário é negligência. Ignorá-lo é desperdício. O profissional sábio sabe quando delegar, quando revisar e como orientar. Esse fluxo é o mapa para isso.*

---

## Recado final

**IA não substitui o desenvolvedor — eleva quem sabe usar.**

O mercado não vai premiar quem sabe pedir para IA fazer tudo. Vai premiar quem sabe **validar, estruturar, revisar e refinar** o que a IA produz.

**Seu diferencial não é apertar o botão. É saber o que fazer depois que ele aperta.**

---

**Próximos passos:**
1. Crie o `AGENTS.md` do seu projeto atual — hoje
2. Na próxima vez que usar IA, leia cada linha gerada
3. Estruture 1 prompt por dia com Contexto + Intenção + Formato
4. Configure CI com testes automatizados
5. Compartilhe esses 5 erros com seu time

[imagem: um desenvolvedor de pé em um palco, plateia ao fundo, segurando um laptop com código — legenda "O profissional do futuro não é substituído pela IA. É potencializado por ela."]

*A ferramenta mais poderosa que você tem não é a IA. É o seu julgamento. Use a IA para acelerar, não para abdicar. O código tem seu nome. A responsabilidade também. Obrigado.*
