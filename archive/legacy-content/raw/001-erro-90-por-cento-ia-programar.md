# Raw Input: O erro que 90% das pessoas cometem usando IA para programar

## Fonte: Documentação Oficial GitHub Copilot
https://docs.github.com/en/copilot/get-started/best-practices

### Strengths and Weaknesses
- Copilot é excelente para: escrever testes e código repetitivo, debugar e corrigir sintaxe, explicar e comentar código, gerar expressões regulares
- Copilot NÃO foi projetado para: substituir sua expertise e habilidades
- Mensagem-chave: "Remember that you are in charge, and Copilot is a powerful tool at your service."

### Best Practices
- Escolha a ferramenta certa: inline suggestions vs Copilot Chat
- Crie prompts bem estruturados: divida tarefas complexas, seja específico, forneça exemplos
- **Sempre valide o código gerado**: entenda antes de implementar, revise cuidadosamente, use testes automatizados
- Guie o Copilot: forneça contexto, reescreva prompts se necessário, forneça feedback

---

## Fonte: Documentação Oficial Claude Code
https://code.claude.com/docs/en/best-practices

### Princípio Central: Context Window Management
- A janela de contexto é o recurso mais importante a gerenciar
- Performance degrada conforme o contexto enche
- Claude pode "esquecer" instruções anteriores quando o contexto está cheio

### Give Claude a Way to Verify Its Work
> "Give Claude a check it can run: tests, a build, a screenshot to compare. It's the difference between a session you watch and one you walk away from."

- Sem uma verificação executável, "parece pronto" é o único sinal disponível
- Você se torna o loop de verificação: cada erro espera você perceber
- Com uma verificação, Claude faz o trabalho, executa o check, lê o resultado, itera até passar

### Top Best Practices
1. Configure CLAUDE.md - memória persistente do projeto
2. Estruture prompts com contexto, intenção e formato esperado
3. Ative plan mode antes de tarefas complexas (+3 arquivos)
4. Divida tarefas grandes em subtasks atômicas (5-10 min)
5. Use slash commands para operações recorrentes
6. Use integração Git para commits, revisões e PRs automatizados
7. Itere através de feedback em vez de reescrever prompts do zero
8. Documente workflows como arquivos reutilizáveis

---

## Fonte: OpenCode Official Docs
https://opencode.ai/

### Key Concepts
- Subagents: especializados para tarefas específicas
- Permissions: allow/ask/deny para controle granular
- AGENTS.md: instruções persistentes do projeto
- LSP integration: entendimento em nível de compilador

### Common Mistakes (from community guides)
1. **Vague prompts**: "Make it better" vs. "Refactor handleSubmit to use async/await with try-catch"
2. **Skipping Plan mode**: sempre analise antes de modificar
3. **Neglecting AGENTS.md**: 5 minutos economizam horas depois
4. **Ignoring sessions**: use /sessions para manter contexto entre pausas
5. **Global MCP servers**: habilite por agente para evitar context bloat

---

## Fonte: Pesquisa Acadêmica - arXiv 2512.05239
"A Survey of Bugs in AI-Generated Code" (Dec 2025)

### Descobertas Principais
- Código gerado por IA contém bugs e problemas de qualidade
- Modelos são treinados em código público que já contém bugs
- Isso causa desafios de confiança e manutenção no processo de desenvolvimento

### Classificação de Bugs em Código Gerado por IA
O paper categoriza os tipos de bugs encontrados:
- Bugs de lógica: código sintaticamente correto mas semanticamente errado
- Bugs de segurança: vulnerabilidades introduzidas
- Bugs de performance: código ineficiente
- Bugs de compatibilidade: dependências incorretas ou desatualizadas

### Estratégias de Mitigação
- Revisão sistemática do código gerado
- Testes automatizados obrigatórios
- Validação de dependências sugeridas
- Compreensão do código antes da implementação

---

## Fonte: TechTudo (Especialistas consultados)
https://www.techtudo.com.br/listas/2026/04/5-erros-ao-usar-ia-que-sabotam-suas-respostas-e-como-evita-los-edsoftwares.ghtml

### Erro 1: Fazer pedidos vagos (e esperar respostas precisas)
- "IA opera com base em probabilidades: quanto menos contexto, mais genérica a resposta"
- "Pedido fraco, resposta fraca em escala industrial"
- Solução: detalhe o cenário, objetivo e formato esperado

### Erro 2: Não revisar o que a IA gera
- "A IA erra com confiança, não com hesitação"
- "Se você copia e cola sem ler, o erro deixa de ser da ferramenta. Passa a ser seu."
- Solução: trate a resposta como rascunho inicial, não produto acabado

### Erro 3: Tentar resolver tudo em um único comando
- "A IA tenta abraçar tudo e não vai aprofundar nada"
- Solução: etapas. Um pedido por vez. "Primeiro o resumo. Depois a análise. Depois o texto."

### Erro 4: Usar IA como resposta final — e não como processo
- "A primeira resposta raramente é a melhor. Ela é o ponto de partida, não o produto final."
- Solução: refine, corrija e redirecione ao longo da conversa

### Erro 5: Usar IA para tarefas inadequadas (ou críticas demais)
- "Usar IA para diagnósticos médicos, decisões críticas ou áreas sensíveis"
- "A IA tende a fornecer interpretações genéricas, sem considerar particularidades"
- Solução: tarefas operacionais com IA, decisões estratégicas com validação humana

---

## Fonte: Indústria - Pesquisas e Benchmarks

### Stack Overflow Survey
- 63% dos desenvolvedores encontraram erros inesperados ao usar assistentes de codificação IA
- 68% dos desenvolvedores têm dificuldade em integrar IA efetivamente nos workflows

### Claude Code Pro Pack Research (DEV.to)
- Sem regras (CLAUDE.md): ~40% de erro em código gerado
- Com 4 regras básicas: ~11% de erro
- Com 12 regras (pro pack): ~3% de erro — melhoria de ~10x

### SFEIR Institute
- Desenvolvedores que aplicam 10 práticas recomendadas reduzem em 35% as iterações necessárias
- Principais áreas: configuração, comunicação e workflow

### 10 Most Common Mistakes (Ryz Labs, consolidated)
1. Over-reliance on AI suggestions
2. Ignoring contextual awareness
3. Skipping code reviews
4. Not customizing AI settings
5. Neglecting dependency validation
6. Forgetting version control management
7. Underestimating testing needs
8. Overlooking performance implications
9. Misunderstanding licensing and code ownership
10. Not engaging with community feedback

---

## Síntese: Os 5 Erros que 90% Cometem

| # | Erro | Fontes | Impacto |
|---|------|--------|---------|
| 1 | Confiar cegamente na saída da IA | GitHub, Claude, arXiv, TechTudo | Bugs em produção, vulnerabilidades |
| 2 | Prompts vagos sem contexto | GitHub, TechTudo, OpenCode | Respostas genéricas inúteis |
| 3 | Pular code review e testes | GitHub, Claude, Ryz Labs, arXiv | Dívida técnica, segurança |
| 4 | Ignorar configuração do projeto (AGENTS.md/CLAUDE.md) | OpenCode, Claude, DEV.to | Comportamento inconsistente do agente |
| 5 | Tratar IA como resposta final, não processo iterativo | Claude, TechTudo, SFEIR | Resultados superficiais |
