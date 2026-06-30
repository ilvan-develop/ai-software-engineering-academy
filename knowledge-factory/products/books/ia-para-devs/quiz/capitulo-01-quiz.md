# Quiz — Capítulo 1: Os 5 Erros ao Usar IA para Programar

**Instruções:** Responda às 5 perguntas de múltipla escolha. Apenas uma alternativa está correta.

---

## Pergunta 1 (Fácil)

O capítulo apresenta o erro de "confiar cegamente na saída da IA". Qual das alternativas melhor descreve esse erro?

- [ ] A) Usar IA apenas para tarefas que o desenvolvedor já domina completamente.
- [ ] B) Aceitar o código gerado pela IA como correto sem questionamento, validação ou revisão.
- [ ] C) Pedir para a IA gerar código em uma linguagem que o desenvolvedor não conhece.
- [ ] D) Utilizar a IA apenas para escrever testes automatizados e não para código de produção.

**Resposta correta:** B
**Explicação:** O erro 1 é definido no capítulo como "aceitar o código gerado pela IA como correto sem qualquer questionamento, validação ou revisão". A IA escreve código com alta fluência, mas pode conter bugs sutis de lógica, segurança ou performance. A alternativa A não é um erro (usar IA onde se tem domínio é prudente), C é um uso legítimo desde que haja revisão, e D descreve um uso restritivo que não é tratado como erro no capítulo.
**Nível:** Fácil

---

## Pergunta 2 (Fácil)

Segundo os dados apresentados no capítulo, qual é a taxa de erro do código gerado por IA quando **não há regras configuradas** no projeto?

- [ ] A) ~3%
- [ ] B) ~11%
- [ ] C) ~40%
- [ ] D) ~63%

**Resposta correta:** C
**Explicação:** O capítulo cita a pesquisa Claude Code Pro Pack (DEV.to): sem regras configuradas, o código gerado por IA tem ~40% de erro. Com 12 regras, esse número cai para ~3% — uma melhoria de ~13x. A alternativa A (~3%) é o resultado com 12 regras, B (~11%) com 4 regras, e D (~63%) é o percentual de desenvolvedores que encontraram erros inesperados (Stack Overflow Survey), não a taxa de erro do código.
**Nível:** Fácil

---

## Pergunta 3 (Médio)

O capítulo propõe que prompts eficazes devem conter três elementos essenciais. Quais são eles?

- [ ] A) Saudação, pergunta e agradecimento
- [ ] B) Contexto, intenção e formato esperado
- [ ] C) Título, descrição e exemplos
- [ ] D) Linguagem, framework e biblioteca

**Resposta correta:** B
**Explicação:** A estrutura de prompt eficaz apresentada no capítulo é: **Contexto** (qual é o cenário/arquivo/função), **Intenção** (o que você quer alcançar) e **Formato esperado** (como deve ser a resposta). A alternativa A descreve uma cortesia social que não melhora a precisão técnica. C e D são elementos que podem fazer parte do contexto, mas não cobrem a estrutura completa. A estrutura Contexto + Intenção + Formato é o que transforma um "pedido vago" em uma instrução executável.
**Nível:** Médio

---

## Pergunta 4 (Médio)

Qual é a função principal dos arquivos `AGENTS.md` (OpenCode) e `CLAUDE.md` (Claude Code) em um projeto de software?

- [ ] A) Documentar o código fonte para outros desenvolvedores humanos.
- [ ] B) Servir como memória de longo prazo do agente de IA, contendo regras, padrões e convenções do projeto.
- [ ] C) Armazenar as credenciais e chaves de API utilizadas pelo projeto.
- [ ] D) Registrar o histórico de prompts utilizados durante o desenvolvimento.

**Resposta correta:** B
**Explicação:** O capítulo explica que arquivos AGENTS.md e CLAUDE.md "funcionam como a memória de longo prazo do agente", contendo regras como stack tecnológica, padrões de código e convenções. Sem eles, a IA "chuta" — não sabe se o projeto usa React ou Vue, const ou function, Vitest ou Jest. A alternativa A é função de README.md, C é inseguro (secrets nunca devem ser versionados), e D não é função desses arquivos.
**Nível:** Médio

---

## Pergunta 5 (Difícil)

Considere o cenário: um desenvolvedor pede para a IA gerar uma função de login, analisa o código linha por linha, aprova a lógica, mas **não escreve testes automatizados, não configura regras para o agente e usa a primeira resposta da IA como solução final**. Ele faz commit e deploy. Quantos dos 5 erros ele está cometendo simultaneamente e quais são?

- [ ] A) 1 erro: confiar cegamente na saída da IA.
- [ ] B) 2 erros: pular code review e testes; ignorar configuração do projeto.
- [ ] C) 3 erros: pular code review e testes; ignorar configuração do projeto; tratar IA como resposta final.
- [ ] D) 5 erros: todos os erros do capítulo estão presentes.

**Resposta correta:** C
**Explicação:** O desenvolvedor comete 3 erros simultâneos: **Erro 3** (pular code review e testes — não escreveu testes automatizados), **Erro 4** (ignorar configuração do projeto — não criou AGENTS.md/CLAUDE.md) e **Erro 5** (tratar IA como resposta final — usou a primeira resposta sem refinar). Ele NÃO comete o Erro 1 (confiar cegamente) porque analisou o código linha por linha. Também NÃO comete o Erro 2 (prompts vagos) porque o enunciado não menciona se o prompt foi vago ou estruturado — não há evidência desse erro. Portanto, a alternativa C está correta, enquanto A, B e D subestimam ou superestimam os erros.
**Nível:** Difícil

---

---

## Pergunta 6 (Médio)

Um desenvolvedor configurou um AGENTS.md com 12 regras para seu projeto TypeScript. Segundo os dados apresentados no capítulo, qual a redução esperada na taxa de erro do código gerado pela IA em comparação com um projeto sem regras?

- [ ] A) De ~40% para ~20% (redução de 2x)
- [ ] B) De ~40% para ~3% (redução de ~13x)
- [ ] C) De ~63% para ~11% (redução de ~6x)
- [ ] D) De ~20% para ~5% (redução de 4x)

**Resposta correta:** B
**Explicação:** O capítulo apresenta os dados da pesquisa Claude Code Pro Pack: sem regras, a taxa de erro é de ~40%; com 12 regras no AGENTS.md/CLAUDE.md, cai para ~3% — uma melhoria de aproximadamente 13x. A alternativa A (~20%) não corresponde a nenhum dado apresentado. C (~63%) confunde com o percentual de desenvolvedores que encontraram erros inesperados (Stack Overflow Survey). D subestima tanto a taxa inicial quanto a final.
**Nível:** Médio

---

## Pergunta 7 (Médio)

No capítulo, o autor descreve a "Síndrome do Estudante" ao usar IA para programar. Qual das alternativas abaixo melhor caracteriza essa síndrome?

- [ ] A) O desenvolvedor estuda exaustivamente a documentação da IA antes de usá-la.
- [ ] B) O desenvolvedor pede para a IA gerar um esboço e depois refina o prompt até o código ficar correto — mas nunca estuda os erros para não repeti-los.
- [ ] C) O desenvolvedor usa IA apenas para aprender novas linguagens, não para produzir código.
- [ ] D) O desenvolvedor cria múltiplos AGENTS.md para cada tarefa diferente.

**Resposta correta:** B
**Explicação:** A "Síndrome do Estudante" é descrita no capítulo como o comportamento de usar IA iterativamente para corrigir erros sem nunca aprender por que eles ocorreram. O desenvolvedor sabe refinar prompts, mas não desenvolve o senso crítico para identificar padrões de erro. A alternativa A não é uma síndrome negativa. C descreve um uso legítimo e seguro da IA. D descreve uma prática excessiva mas não corresponde à síndrome descrita.
**Nível:** Médio

---

## Gabarito

| Pergunta | Resposta | Nível |
|----------|----------|-------|
| 1 | B | Fácil |
| 2 | C | Fácil |
| 3 | B | Médio |
| 4 | B | Médio |
| 5 | C | Difícil |
| 6 | B | Médio |
| 7 | B | Médio |
