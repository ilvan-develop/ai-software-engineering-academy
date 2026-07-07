# Quiz — Módulo 09

## Pergunta 1

Qual a principal razão pela qual desenvolvedores confiam em código gerado por IA sem revisar?

- a) A IA nunca erra código
- b) A IA gera respostas com alta fluência e aparência de confiança
- c) O custo de revisar é maior que o custo do erro
- d) O time de QA é responsável por isso

**Resposta:** b
**Explicação:** A IA erra com confiança, não com hesitação. Código fluente parece correto, mas pode conter bugs sutis de lógica, segurança ou performance.

---

## Pergunta 2

Quais são os três elementos essenciais de um prompt estruturado?

- a) Saudação, pergunta, despedida
- b) Contexto, Intenção, Formato Esperado
- c) Exemplo, código, explicação
- d) Linguagem, framework, biblioteca

**Resposta:** b
**Explicação:** Contexto (onde/quem), Intenção (o que quer), Formato Esperado (como quer a resposta) — sem esses três, a IA produz respostas genéricas.

---

## Pergunta 3

Segundo o Claude Code Pro Pack Research, qual a taxa de erro ao usar 12 regras configuradas?

- a) ~40%
- b) ~11%
- c) ~3%
- d) ~0%

**Resposta:** c
**Explicação:** Sem regras o erro é ~40%. Com 4 regras cai para ~11%. Com 12 regras, atinge ~3% — uma melhoria de 13,3x.

---

## Pergunta 4

Qual categoria de bug NÃO está entre as classificações do survey arXiv 2512.05239?

- a) Bugs de lógica
- b) Bugs de segurança
- c) Bugs de sintaxe
- d) Bugs de compatibilidade

**Resposta:** c
**Explicação:** O survey classifica bugs em lógica, segurança, performance e compatibilidade. Bugs de sintaxe são raros porque os modelos são treinados para gerar código sintaticamente correto.

---

## Pergunta 5

Qual é o propósito do arquivo AGENTS.md (ou CLAUDE.md)?

- a) Documentar bugs conhecidos
- b) Servir como memória de longo prazo do agente com regras e padrões do projeto
- c) Listar dependências do projeto
- d) Configurar variáveis de ambiente

**Resposta:** b
**Explicação:** AGENTS.md/CLAUDE.md contém regras, stack, convenções e estrutura do projeto para que o agente não "chute" padrões a cada interação.

---

## Pergunta 6

O que significa "tratar IA como processo iterativo"?

- a) Gerar uma resposta e usá-la como final
- b) Refinar a resposta com feedback direcionado em múltiplas iterações
- c) Perguntar para várias IAs e escolher a melhor
- d) Usar a IA apenas para tarefas repetitivas

**Resposta:** b
**Explicação:** A primeira resposta raramente é a melhor. O profissional refina com feedback específico até atingir os critérios de qualidade.

---

## Pergunta 7

Qual tipo de bug está presente neste código?
```javascript
function hashPassword(password) {
  return hashlib.md5(password).hexdigest();
}
```text

- a) Lógica
- b) Segurança
- c) Performance
- d) Compatibilidade

**Resposta:** b
**Explicação:** MD5 é um algoritmo de hash inseguro para senhas, sendo instantaneamente quebrável com ataques de dicionário. O correto é usar bcrypt ou argon2.

---

## Pergunta 8

Segundo o GitHub Copilot Docs, quem é o responsável pelo código gerado por IA?

- a) O provedor da IA
- b) O time de QA
- c) O desenvolvedor
- d) O revisor de código

**Resposta:** c
**Explicação:** A documentação afirma: "Remember that you are in charge, and Copilot is a powerful tool at your service." O desenvolvedor é sempre o responsável.

---

## Pergunta 9

Qual destas NÃO é uma boa prática ao usar IA para programar?

- a) Sempre ler cada linha antes de implementar
- b) Pedir para a IA gerar testes junto com o código
- c) Usar a primeira resposta como solução final
- d) Configurar o projeto com regras para o agente

**Resposta:** c
**Explicação:** A primeira resposta é um rascunho, não produto final. A boa prática é iterar com feedback para refinar a solução.

---

## Pergunta 10

Qual a melhoria percentual na redução de iterações ao aplicar práticas recomendadas segundo o SFEIR Institute?

- a) ~15%
- b) ~25%
- c) ~35%
- d) ~50%

**Resposta:** c
**Explicação:** Desenvolvedores que aplicam 10 práticas recomendadas reduzem em ~35% as iterações necessárias (SFEIR Institute).
