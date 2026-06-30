# Quiz — Módulo 09 — O Erro de 90% ao Usar IA para Programar

**Total de perguntas:** 10

**Distribuição:** 2 Fáceis, 5 Médias, 3 Difíceis

**Tempo estimado:** 20 minutos

---

## Pergunta 1 — Fácil

Qual a principal razão pela qual desenvolvedores confiam em código gerado por IA sem revisar?

- a) A IA nunca erra código
- b) A IA gera respostas com alta fluência e aparência de confiança
- c) Revisar é mais caro que o erro
- d) O time de QA é responsável

**Resposta correta:** b

**Explicação:** A IA erra com confiança, não com hesitação. Código fluente parece correto, mas pode conter bugs sutis.

---

## Pergunta 2 — Fácil

Quais são os três elementos essenciais de um prompt estruturado?

- a) Saudação, pergunta, despedida
- b) Contexto, Intenção, Formato Esperado
- c) Exemplo, código, explicação
- d) Linguagem, framework, biblioteca

**Resposta correta:** b

**Explicação:** Sem esses três elementos, a IA produz respostas genéricas que não resolvem o problema real.

---

## Pergunta 3 — Média

Segundo pesquisas, qual a taxa de erro ao usar IA para programar com 12 regras configuradas no AGENTS.md?

- a) ~40%
- b) ~11%
- c) ~3%
- d) ~0%

**Resposta correta:** c

**Explicação:** Sem regras: ~40% de erro. Com 4 regras: ~11%. Com 12 regras: ~3% — melhoria de 13,3x.

---

## Pergunta 4 — Média

Qual tipo de bug NÃO está entre as categorias do survey arXiv 2512.05239?

- a) Bugs de lógica
- b) Bugs de segurança
- c) Bugs de sintaxe
- d) Bugs de compatibilidade

**Resposta correta:** c

**Explicação:** O survey classifica bugs em lógica, segurança, performance e compatibilidade. Bugs de sintaxe são raros em código gerado por IA.

---

## Pergunta 5 — Média

Qual é o propósito do arquivo AGENTS.md?

- a) Documentar bugs conhecidos do projeto
- b) Servir como memória persistente do agente com regras e padrões
- c) Listar dependências do projeto
- d) Configurar variáveis de ambiente

**Resposta correta:** b

**Explicação:** AGENTS.md contém stack, regras, estrutura e convenções para o agente não "chutar" padrões.

---

## Pergunta 6 — Média

O que significa "tratar IA como processo iterativo"?

- a) Usar a primeira resposta da IA como solução final
- b) Refinar a resposta com feedback direcionado em múltiplas iterações
- c) Perguntar para várias IAs e escolher a melhor
- d) Usar a IA apenas para tarefas repetitivas

**Resposta correta:** b

**Explicação:** A primeira resposta raramente é a melhor. O profissional refina com feedback específico até atingir qualidade.

---

## Pergunta 7 — Média

Qual tipo de bug está presente neste código?
```javascript
function hashPassword(password) {
  return crypto.createHash('md5').update(password).digest('hex');
}
```

- a) Lógica
- b) Segurança
- c) Performance
- d) Compatibilidade

**Resposta correta:** b

**Explicação:** MD5 é inseguro para senhas. O correto é usar bcrypt ou argon2 com salt.

---

## Pergunta 8 — Média

Segundo a documentação do GitHub Copilot, quem é o responsável pelo código gerado?

- a) O provedor da IA
- b) O time de QA
- c) O desenvolvedor
- d) O revisor de código

**Resposta correta:** c

**Explicação:** "Remember that you are in charge, and Copilot is a powerful tool at your service."

---

## Pergunta 9 — Difícil

Qual destas NÃO é uma boa prática ao usar IA para programar?

- a) Ler cada linha antes de implementar
- b) Pedir testes junto com o código
- c) Usar a primeira resposta como solução final
- d) Configurar regras no AGENTS.md

**Resposta correta:** c

**Explicação:** A primeira resposta é rascunho inicial. A boa prática é iterar com feedback direcionado.

---

## Pergunta 10 — Difícil

Qual a melhoria percentual na redução de iterações ao aplicar práticas recomendadas (SFEIR Institute)?

- a) ~15%
- b) ~25%
- c) ~35%
- d) ~50%

**Resposta correta:** c

**Explicação:** Desenvolvedores que aplicam 10 práticas recomendadas reduzem em ~35% as iterações necessárias.
