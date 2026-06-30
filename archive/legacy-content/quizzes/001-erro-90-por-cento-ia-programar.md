# Quiz: O erro que 90% das pessoas cometem usando IA para programar

**Módulo:** 001-erro-90-por-cento-ia-programar
**Total de perguntas:** 10
**Distribuição:** 2 fáceis | 5 médias | 3 difíceis

---

## Pergunta 1

Segundo a pesquisa Claude Code Pro Pack, qual é a taxa de erro aproximada do código gerado por IA quando nenhuma regra de configuração é definida no projeto?

- [ ] A) ~3%
- [ ] B) ~11%
- [ ] C) ~40%
- [ ] D) ~63%

**Resposta correta:** C
**Explicação:** A pesquisa mostra que, sem regras configuradas, o código gerado por IA tem aproximadamente 40% de erro. Com 4 regras básicas, o erro cai para ~11% (melhoria de ~3,6x). Com 12 regras (Pro Pack), cai para ~3% (melhoria de ~13,3x). A alternativa A (~3%) é o resultado com 12 regras, não sem regras. A B (~11%) é o resultado com 4 regras básicas. A D (~63%) é o percentual de desenvolvedores que encontraram erros inesperados (Stack Overflow Survey), não a taxa de erro do código em si.
**Nível:** Fácil

---

## Pergunta 2

Qual dos itens abaixo **NÃO** é um dos 5 mandamentos do uso correto de IA para programar apresentados na aula?

- [ ] A) Valide toda saída da IA
- [ ] B) Estruture prompts com contexto
- [ ] C) Use sempre a IA mais cara do mercado
- [ ] D) Revise e teste como qualquer código

**Resposta correta:** C
**Explicação:** Os 5 mandamentos são: valide toda saída, estruture prompts com contexto, revise e teste como qualquer código, configure o projeto para a IA, e itere — não aceite a primeira resposta. "Usar a IA mais cara" não é um mandamento e não tem relação com as práticas ensinadas. O valor está na forma de uso, não no custo da ferramenta. As demais alternativas (A, B, D) são mandamentos reais da aula.
**Nível:** Fácil

---

## Pergunta 3

Um desenvolvedor pediu para a IA "criar uma função de login" e recebeu um código que funciona no caminho feliz, mas não trata senha incorreta, usuário inexistente nem taxa de limite. Qual erro ele cometeu?

- [ ] A) Erro 1 — Confiar cegamente na saída da IA
- [ ] B) Erro 2 — Prompt vago sem contexto
- [ ] C) Erro 4 — Ignorar configuração do projeto
- [ ] D) Erro 5 — Tratar IA como resposta final

**Resposta correta:** B
**Explicação:** O prompt "criar uma função de login" é extremamente genérico — não especifica linguagem, framework, definição de sucesso (JWT? Sessão? OAuth?) nem tratamento de erros. Isso caracteriza o Erro 2 (prompts vagos sem contexto). A alternativa A (confiar cegamente) poderia se aplicar se ele tivesse implementado sem revisar, mas o problema central é a falta de especificação inicial. A alternativa C (ignorar configuração) se refere à ausência de AGENTS.md/CLAUDE.md. A alternativa D (tratar como resposta final) se aplicaria se ele tivesse aceitado a primeira resposta sem iterar, mas novamente o erro raiz é o prompt vago.
**Nível:** Médio

---

## Pergunta 4

Um desenvolvedor gerou uma função de validação de email com IA. O código passou em todos os testes unitários que ele escreveu, mas em produção começou a aceitar emails como "usuario@" porque a regex era permissiva demais. Qual erro principal está sendo cometido?

- [ ] A) Erro 1 — Confiar cegamente na saída da IA
- [ ] B) Erro 3 — Pular code review e testes
- [ ] C) Erro 5 — Tratar IA como resposta final
- [ ] D) Erro 4 — Ignorar configuração do projeto

**Resposta correta:** A
**Explicação:** O desenvolvedor confiou cegamente que a função estava correta sem validar a lógica real. Ele escreveu testes, mas testou apenas o que a IA gerou (casos felizes), sem considerar casos extremos como "usuario@". A aula ensina que é preciso "ler cada linha antes de implementar" e "testar com casos extremos — string vazia, null, negativo, tipos inesperados". A alternativa B (pular code review) não se aplica porque ele escreveu testes. A alternativa C (tratar como resposta final) poderia ser um fator secundário, mas o erro principal foi não questionar a lógica gerada. A alternativa D (ignorar configuração) não se relaciona diretamente com o problema.
**Nível:** Médio

---

## Pergunta 5

Um dev copiou código de IA, não abriu um Pull Request para revisão de ninguém, não escreveu testes e deu commit direto na main. Qual o principal problema dessa conduta?

- [ ] A) Erro 2 — Prompt vago sem contexto
- [ ] B) Erro 3 — Pular code review e testes
- [ ] C) Erro 4 — Ignorar configuração do projeto
- [ ] D) Erro 5 — Tratar IA como resposta final

**Resposta correta:** B
**Explicação:** A situação descreve exatamente o Erro 3: ignorar as etapas de revisão de código e testes automatizados, tratando o código gerado por IA como isento de erros. A aula alerta: "pular code review em código gerado por IA não economiza tempo — ele terceiriza o risco para você". A alternativa A (prompt vago) não se aplica porque o problema não é como o prompt foi escrito. A alternativa C (ignorar configuração) seria relevante se faltasse AGENTS.md, mas o cenário não menciona isso. A alternativa D (tratar como resposta final) é secundária aqui — o erro central é pular a revisão e os testes.
**Nível:** Médio

---

## Pergunta 6

Um time de desenvolvimento percebeu que o código gerado pela IA muda de estilo a cada interação: às vezes usa `function`, às vezes arrow functions; horas em um arquivo, snake_case em outro; e ignora o padrão de testes do projeto. Qual erro está na raiz desse problema?

- [ ] A) Erro 1 — Confiar cegamente na saída da IA
- [ ] B) Erro 2 — Prompt vago sem contexto
- [ ] C) Erro 4 — Ignorar configuração do projeto
- [ ] D) Erro 5 — Tratar IA como resposta final

**Resposta correta:** C
**Explicação:** A descrição é um caso clássico de Erro 4 (ignorar configuração do projeto). Sem um arquivo como AGENTS.md ou CLAUDE.md, a IA não tem contexto sobre os padrões do projeto — ela "chuta" estilo, nomenclatura e ferramentas a cada resposta. A aula mostra que com 12 regras configuradas, o erro cai de ~40% para ~3%. A alternativa A (confiar cegamente) não explica a inconsistência de estilo. A alternativa B (prompt vago) poderia ser um fator, mas o problema sistêmico é a falta de configuração persistente. A alternativa D (tratar como resposta final) não aborda a raiz do problema.
**Nível:** Médio

---

## Pergunta 7

Um desenvolvedor pediu para a IA refatorar uma função, recebeu uma primeira versão que funciona e a implementou imediatamente em produção. Semanas depois, descobriu que a versão refatorada não lidava com o caso de lista vazia — algo que uma segunda iteração teria resolvido. Qual erro ele cometeu?

- [ ] A) Erro 1 — Confiar cegamente na saída da IA
- [ ] B) Erro 2 — Prompt vago sem contexto
- [ ] C) Erro 3 — Pular code review e testes
- [ ] D) Erro 5 — Tratar IA como resposta final

**Resposta correta:** D
**Explicação:** O desenvolvedor tratou a primeira resposta da IA como solução definitiva, sem refinamento ou iteração. A aula ensina que "a primeira resposta raramente é a melhor. Ela é o ponto de partida, não o produto final" e orienta a iterar com feedback direcionado. Embora a alternativa A (confiar cegamente) e C (pular code review) possam parecer plausíveis, o cerne do problema descrito é aceitar a primeira versão como final sem pedir refinamentos — isso é o Erro 5. A alternativa B (prompt vago) não se aplica, pois ele deu um pedido específico de refatoração.
**Nível:** Médio

---

## Pergunta 8

Analise o cenário: um desenvolvedor pediu à IA: "Faz aí uma query no banco". A IA gerou o código abaixo e o desenvolvedor implementou sem alterações:

```python
query = f"SELECT * FROM users WHERE name = '{user_input}'"
cursor.execute(query)
```

Considerando o fluxo ideal de uso de IA ([Prompt Estruturado] → [IA gera] → [Code Review] → [Testes] → [Refinamento] → [Commit]), **quantos erros dos 5 você identifica nessa conduta e qual é o mais grave?**

- [ ] A) 1 erro — o mais grave é o Erro 1 (confiar cegamente), pois o código tem SQL injection
- [ ] B) 2 erros — o mais grave é o Erro 3 (pular code review), pois não houve revisão nem testes
- [ ] C) 3 erros — o mais grave é o Erro 2 (prompt vago), pois sem contexto a IA gera código genérico e inseguro
- [ ] D) 4 erros — o mais grave é o Erro 5 (tratar como resposta final), pois ele aceitou a primeira versão

**Resposta correta:** C
**Explicação:** É possível identificar 3 erros: (1) Erro 2 — o prompt "Faz aí uma query no banco" é extremamente vago, sem contexto de linguagem, ORM, segurança ou tratamento de erros; (2) Erro 1 — confiar cegamente na saída, implementando código vulnerável a SQL injection sem questionar; (3) Erro 5 — tratar a primeira resposta como final, sem iterar. O erro mais grave é o Erro 2 porque é a causa raiz: um prompt vago produz uma resposta genérica que já nasce insegura. A alternativa A ignora que o prompt vago é a origem do problema. A alternativa B subestima a quantidade de erros. A alternativa D superestima (não há evidência clara de Erro 4 — faltar AGENTS.md — ou Erro 3, já que ele sequer chegou a testar/revisar porque o prompt já estava comprometido).
**Nível:** Difícil

---

## Pergunta 9

Um desenvolvedor incluiu no AGENTS.md do projeto: "Use React 18 com TypeScript". Mesmo assim, a IA continua gerando componentes com `any` em vez de tipos específicos, e usando `class components` em vez de funções. Qual a causa mais provável e qual a correção adequada?

- [ ] A) A IA está com bug; a solução é trocar de assistente de IA
- [ ] B) O AGENTS.md é muito curto; a solução é descrever "Regras" específicas: proibir `any`, exigir arrow functions, proibir class components
- [ ] C) O desenvolvedor está usando o assistente errado; a solução é migrar para outro agente que respeite AGENTS.md
- [ ] D) O erro é do prompt momentâneo; a solução é repetir as regras manualmente a cada interação

**Resposta correta:** B
**Explicação:** A aula mostra que a estrutura ideal de AGENTS.md inclui uma seção de "Regras" com diretivas específicas. Dizer apenas "use React 18 com TypeScript" é muito vago — a IA pode interpretar que TypeScript permite `any` (o que é verdade sintaticamente) e que class components ainda são válidos em React 18 (o que também é verdade, embora não recomendado). A correção é adicionar regras explícitas como "Proibir `any` — use tipos concretos ou `unknown`" e "Componentes devem ser arrow functions, nunca class components". A alternativa A culpa erroneamente a ferramenta. A alternativa C também culpa a ferramenta, quando o problema é a configuração insuficiente. A alternativa D ignora o propósito do AGENTS.md, que é justamente evitar repetir regras manualmente.
**Nível:** Difícil

---

## Pergunta 10

Um desenvolvedor recebeu este código gerado por IA para um sistema de e-commerce:

```javascript
function getProductPrice(productId) {
  const db = new SQLiteDatabase('products.db');
  const row = db.query(`SELECT price FROM products WHERE id = ${productId}`);
  return row.price;
}
```

Ele identificou SQL injection (Erro 1) e corrigiu usando prepared statements. Porém, o código ainda cria uma nova conexão com o banco a cada chamada, sem pool de conexões, e não trata o caso de `productId` inexistente. Considerando o fluxo ideal de uso de IA, qual etapa ele provavelmente pulou após a primeira correção?

- [ ] A) A etapa de Prompt Estruturado — ele deveria ter reescrito o prompt do zero
- [ ] B) A etapa de Refinamento — ele corrigiu apenas o primeiro problema visível, mas não iterou com feedback para tratar os demais problemas
- [ ] C) A etapa de Code Review — ele deveria pedir para outro desenvolvedor revisar
- [ ] D) A etapa de Testes — ele deveria rodar testes de integração antes de qualquer correção

**Resposta correta:** B
**Explicação:** O desenvolvedor corrigiu o SQL injection (correção correta), mas parou por aí — não refinou o código para resolver os outros problemas (conexão sem pool, falta de tratamento de `productId` inexistente). Isso caracteriza a omissão da etapa de Refinamento no fluxo ideal. A aula ensina que o processo é iterativo: "obtenha uma primeira versão → revise e identifique pontos de melhoria → refine com feedback direcionado → repita até atender aos critérios de qualidade". A alternativa A está errada porque reescrever o prompt do zero é menos eficiente que iterar com feedback. A alternativa C (code review) e D (testes) são importantes, mas o problema específico descrito é ter parado na primeira correção sem continuar refinando.
**Nível:** Difícil
