## Introducao

# O erro que 90% das pessoas cometem usando IA para programar
**Nível:** Conceitos / Engenharia
**Tempo estimado:** 20 minutos
**Público-alvo:** Desenvolvedores iniciantes e intermediários que utilizam assistentes de IA no dia a dia
---

---
## Pré-requisitos

- Experiência básica com programação em qualquer linguagem
- Familiaridade com uso de assistentes de IA (GitHub Copilot, Claude Code, ChatGPT, etc.)
- Noções fundamentais de Git e versionamento

---
## Objetivos de aprendizagem

Ao final desta aula, o aluno será capaz de:
1. **Identificar** os 5 erros mais comuns ao usar IA para programar
2. **Diferenciar** uso produtivo de uso prejudicial de assistentes de IA
3. **Aplicar** técnicas de prompt estruturado para obter respostas precisas
4. **Estabelecer** um fluxo de validação e revisão para código gerado por IA
5. **Configurar** arquivos de instrução do projeto (AGENTS.md / CLAUDE.md) para melhorar a consistência do agente

---
## Competências desenvolvidas

**Hard skills:**
- Prompt engineering aplicado à programação
- Code review de código gerado por IA
- Configuração de assistentes de IA no projeto
- Automação de testes como ferramenta de verificação
**Soft skills:**
- Pensamento crítico e validação de fontes
- Comunicação clara e estruturada

---
## 1. Introdução: por que 90% cometem esse erro

Era uma terça-feira comum. O desenvolvedor precisava de uma função simples para validar emails. Pediu ao ChatGPT, copiou o código, fez deploy. Na sexta, o banco de dados estava cheio de registros com emails como "usuario@". Aquela função — que parecia perfeita — só verificava se existia um "@" na string.
A IA acertou a sintaxe. Errou a lógica. O desenvolvedor não revisou. Produção quebrou.
Esse cenário se repete milhares de vezes todos os dias. Assistentes de IA geram código em segundos — mas essa velocidade tem um custo oculto. Pesquisas da indústria revelam um padrão preocupante:
| Dado | Fonte |
|------|-------|
| **63%** dos desenvolvedores encontraram erros inesperados ao usar IA | Stack Overflow Survey |
| **68%** têm dificuldade em integrar IA efetivamente nos workflows | Stack Overflow Survey |
| Sem regras configuradas, código gerado por IA tem **~40% de erro** | Claude Code Pro Pack |

---
## 2. Erro 1: Confiar cegamente na saída da IA

### Definição
Aceitar o código gerado pela IA como correto sem qualquer questionamento, validação ou revisão.
### Por que acontece
A IA gera respostas com **alta fluência e aparência de confiança**. O código parece correto, compila e muitas vezes até passa em testes simples — mas pode conter bugs sutis de lógica, segurança ou performance.
> "A IA erra com confiança, não com hesitação." — TechTudo
O problema é psicológico: nosso cérebro associa fluência a competência. Quando a IA escreve um parágrafo ou função que "soa bem", relaxamos a guarda. Só que a IA não sabe o que está fazendo — ela está apenas completando padrões estatísticos.
O survey arXiv 2512.05239 classifica os bugs encontrados em código gerado por IA em quatro categorias:
| Tipo de Bug | O que significa | Exemplo |

---
## 3. Erro 2: Prompts vagos sem contexto

### Definição
Fazer pedidos genéricos e esperar respostas precisas e úteis.
### Por que acontece
A IA opera com base em probabilidades: quanto menos contexto, mais genérica a resposta. É como perguntar "Me recomenda um filme?" para um amigo — você vai receber uma lista genérica. Agora pergunte "Me recomenda um filme de suspense coreano com menos de 2 horas" — a resposta muda completamente.
O mesmo vale para código.
> "Pedido fraco, resposta fraca em escala industrial." — TechTudo
### Consequência
Respostas genéricas que não resolvem o problema real. O desenvolvedor perde tempo iterando sobre sugestões irrelevantes, se frustra com a ferramenta e culpa a IA — quando o problema era o prompt.

---
## 4. Erro 3: Pular code review e testes

### Definição
Ignorar as etapas de revisão de código e testes automatizados para código gerado por IA, tratando-o como isento de erros.
### Por que acontece
A velocidade da IA cria a ilusão de que o código já passou por um "controle de qualidade implícito". O desenvolvedor assume que, se a IA gerou, está correto.
> "Se você copia e cola sem ler, o erro deixa de ser da ferramenta. Passa a ser seu." — TechTudo
Essa falsa sensação de segurança é traiçoeira. O código gerado por IA **não foi revisado por ninguém**. Ele é o equivalente a um primeiro rascunho escrito por alguém que nunca usou seu sistema.
A documentação do Claude Code é categórica:
> "Give Claude a check it can run: tests, a build, a screenshot to compare. It's the difference between a session you watch and one you walk away from."

---
## 5. Erro 4: Ignorar configuração do projeto (AGENTS.md / CLAUDE.md)

### Definição
Não configurar arquivos de instrução persistente para os agentes de IA, deixando-os operar sem contexto do projeto.
### Por que acontece
Arquivos como `AGENTS.md` (OpenCode) e `CLAUDE.md` (Claude Code) funcionam como a memória de longo prazo do agente. Eles contêm regras, padrões e convenções do projeto.
Sem eles, a IA opera com conhecimento genérico. Ela não sabe se o projeto usa React 18 ou Vue 3. Não sabe se prefere `const` ou `function`. Não sabe se os testes são com Vitest ou Jest. **Ela chuta.**
> "5 minutos de configuração economizam horas de retrabalho." — OpenCode Community
### Consequência
Comportamento inconsistente do agente — o código gerado muda de estilo a cada interação, ignora padrões do projeto e força retrabalho manual.

---
## Stack

React 18 + TypeScript + Tailwind CSS

---
## Regras

- Use arrow functions para componentes
- Prefira `const` sobre `let`
- Testes com Vitest, não Jest
- Erros devem usar `Result<T, E>` (never throw)
- Nomes de arquivo em kebab-case
- Componentes em `src/components/`, páginas em `src/pages/`
> [!TIP]
> Invista 5 minutos agora para criar o `AGENTS.md`. É o investimento com maior retorno por minuto no uso de IA para programar. A cada novo projeto, comece por ele.

---
## 6. Erro 5: Tratar IA como resposta final

### Definição
Usar a primeira resposta da IA como solução definitiva, sem refinamento ou iteração.
### Por que acontece
A IA entrega respostas completas e aparentemente prontas. O desenvolvedor assume que a primeira tentativa é a melhor e encerra o ciclo ali. É o mesmo impulso de mandar um email sem reler — a gratificação imediata de "pronto" supera a disciplina de refinar.
> "A primeira resposta raramente é a melhor. Ela é o ponto de partida, não o produto final." — TechTudo
### Consequência
Resultados superficiais. O código funciona no caminho feliz, mas quebra nos casos extremos. O desenvolvedor perde a oportunidade de refinar, corrigir e adaptar a solução ao contexto real. Pior: nunca sabe o que perdeu.
### Exemplo concreto

---
## 7. Conclusão: como usar IA corretamente

Usar IA para programar não é sobre aceitar código — é sobre **colaboração inteligente**. A IA é uma ferramenta poderosa, mas sem direção, validação e contexto, ela produz resultados medíocres.
### Os 5 mandamentos do uso correto de IA
| # | Mandamento | Por quê |
|---|------------|---------|
| 1 | **Valide** toda saída da IA | IA erra com confiança, não com hesitação |
| 2 | **Estruture** prompts com contexto | Pedido fraco → resposta fraca |
| 3 | **Revise e teste** como qualquer código | Seu nome está no commit |
| 4 | **Configure** o projeto para a IA | 5 minutos economizam horas |

---
## Recursos didáticos sugeridos

**Exemplo prático para sala de aula:**
// Prompt vago: "Valide esse email"
function validateEmail(email) {
return email.includes('@'); // ❌ Superficial, não valida domínio nem formato
}
// Prompt estruturado: "Valide email com regex básica de formato, retorne booleano"
function validateEmail(email) {
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

---
## Exercício prático

**Título:** Diagnosticando um prompt ruim
**Duração:** 5 minutos
**Instruções:**
1. Leia o prompt abaixo:
> "Faz aí uma função de login pra mim"
2. Liste **3 problemas** com este prompt (erro 2 — prompt vago)
3. Reescreva o prompt seguindo a estrutura **Contexto + Intenção + Formato Esperado**
4. Se possível, execute o prompt reescrito em um assistente de IA e compare a qualidade da resposta

---
## Desafio final

**Título:** Auditoria de código gerado por IA
**Duração:** 10 minutos
**Cenário:** Você recebeu um Pull Request com código 100% gerado por IA. O desenvolvedor apenas copiou e colou sem revisar.
**Tarefa:** Analise o trecho abaixo, identifique **todos os erros** e proponha correções:
import os
import hashlib
def hash_password(password):
# Gerar hash simples

---
## Leituras complementares

- GitHub Copilot Best Practices — https://docs.github.com/en/copilot/get-started/best-practices
- Claude Code Best Practices — https://code.claude.com/docs/en/best-practices
- OpenCode Official Docs — https://opencode.ai/
- "A Survey of Bugs in AI-Generated Code" (arXiv 2512.05239) — https://arxiv.org/abs/2512.05239
- 5 erros ao usar IA que sabotam suas respostas (TechTudo) — https://www.techtudo.com.br/listas/2026/04/5-erros-ao-usar-ia-que-sabotam-suas-respostas-e-como-evita-los-edsoftwares.ghtml
- CLAUDE.md Rules: How to Cut AI Coding Mistakes from ~40% to ~3% (DEV.to) — https://dev.to/rams901/claudemd-rules-how-to-cut-ai-coding-mistakes-from-40-to-3-in-2026-2j7o
- 10 Most Common Mistakes Using AI Coding Tools (Ryz Labs) — https://www.ryzlabs.com/

---
