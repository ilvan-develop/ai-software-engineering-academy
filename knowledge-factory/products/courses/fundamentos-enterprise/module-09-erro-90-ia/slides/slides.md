---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# O erro que 90% das pessoas cometem usando IA para programar

## O erro que 90% das pessoas cometem usando IA para programar

---
## Objetivos

- Identificar os 5 erros mais comuns ao usar IA para programar
- Diferenciar uso produtivo de uso prejudicial de assistentes de IA
- Aplicar técnicas de prompt estruturado para obter respostas precisas
- Estabelecer um fluxo de validação e revisão para código gerado por IA
- Configurar arquivos de instrução do projeto (AGENTS.md / CLAUDE.md) para melhorar a consistência do agente

---
## Pré-requisitos

- Experiência básica com programação em qualquer linguagem
- Familiaridade com uso de assistentes de IA (GitHub Copilot, Claude Code, ChatGPT, etc.)
- Noções fundamentais de Git e versionamento

---
## Objetivos de aprendizagem

- Ao final desta aula, o aluno será capaz de:
- 1. **Identificar** os 5 erros mais comuns ao usar IA para programar
- 2. **Diferenciar** uso produtivo de uso prejudicial de assistentes de IA
- 3. **Aplicar** técnicas de prompt estruturado para obter respostas precisas
- 4. **Estabelecer** um fluxo de validação e revisão para código gerado por IA
- 5. **Configurar** arquivos de instrução do projeto (AGENTS.md / CLAUDE.md) para melhorar a consistência do agente

---
## Competências desenvolvidas

- Hard skills:**
- Prompt engineering aplicado à programação
- Code review de código gerado por IA
- Configuração de assistentes de IA no projeto
- Automação de testes como ferramenta de verificação
- Soft skills:**

---
## 1. Introdução: por que 90% cometem esse erro

- Era uma terça-feira comum. O desenvolvedor precisava de uma função simples para validar emails. Pediu ao ChatGPT, cop...
- A IA acertou a sintaxe. Errou a lógica. O desenvolvedor não revisou. Produção quebrou.
- Esse cenário se repete milhares de vezes todos os dias. Assistentes de IA geram código em segundos — mas essa velocid...
- | Dado | Fonte |
- |------|-------|
- | **63%** dos desenvolvedores encontraram erros inesperados ao usar IA | Stack Overflow Survey |

---
## 2. Erro 1: Confiar cegamente na saída da IA

- Aceitar o código gerado pela IA como correto sem qualquer questionamento, validação ou revisão.
- A IA gera respostas com **alta fluência e aparência de confiança**. O código parece correto, compila e muitas vezes a...
- > "A IA erra com confiança, não com hesitação." — TechTudo
- O problema é psicológico: nosso cérebro associa fluência a competência. Quando a IA escreve um parágrafo ou função qu...

---
## 3. Erro 2: Prompts vagos sem contexto

- Fazer pedidos genéricos e esperar respostas precisas e úteis.
- A IA opera com base em probabilidades: quanto menos contexto, mais genérica a resposta. É como perguntar "Me recomend...
- O mesmo vale para código.
- > "Pedido fraco, resposta fraca em escala industrial." — TechTudo

---
## 4. Erro 3: Pular code review e testes

- Ignorar as etapas de revisão de código e testes automatizados para código gerado por IA, tratando-o como isento de er...
- A velocidade da IA cria a ilusão de que o código já passou por um "controle de qualidade implícito". O desenvolvedor ...
- > "Se você copia e cola sem ler, o erro deixa de ser da ferramenta. Passa a ser seu." — TechTudo
- Essa falsa sensação de segurança é traiçoeira. O código gerado por IA **não foi revisado por ninguém**. Ele é o equiv...

---
## 5. Erro 4: Ignorar configuração do projeto (AGENTS.md / CLAUDE.md)

- Não configurar arquivos de instrução persistente para os agentes de IA, deixando-os operar sem contexto do projeto.
- Arquivos como `AGENTS.md` (OpenCode) e `CLAUDE.md` (Claude Code) funcionam como a memória de longo prazo do agente. E...
- Sem eles, a IA opera com conhecimento genérico. Ela não sabe se o projeto usa React 18 ou Vue 3. Não sabe se prefere ...
- > "5 minutos de configuração economizam horas de retrabalho." — OpenCode Community

---
## Stack

- React 18 + TypeScript + Tailwind CSS

---
## Regras

- Use arrow functions para componentes
- Prefira `const` sobre `let`
- Testes com Vitest, não Jest
- Erros devem usar `Result<T, E>` (never throw)
- Nomes de arquivo em kebab-case
- Componentes em `src/components/`, páginas em `src/pages/`

---
## 6. Erro 5: Tratar IA como resposta final

- Usar a primeira resposta da IA como solução definitiva, sem refinamento ou iteração.
- A IA entrega respostas completas e aparentemente prontas. O desenvolvedor assume que a primeira tentativa é a melhor ...
- > "A primeira resposta raramente é a melhor. Ela é o ponto de partida, não o produto final." — TechTudo

---
## Exemplo: javascript

```javascript
// 🚫 Código gerado por IA — parece certo, mas está errado
function calculateDiscount(price, coupon) {
  if (coupon === 'SAVE10') {
    return price * 0.9;
  }
  return price; // ❌ Esqueceu de validar se price é número
}

calculateDiscount('cem reais', 'SAVE10'); // NaN em produção
```

---
## Exemplo: markdown

```markdown
# Agente: Front-end

## Stack
React 18 + TypeScript + Tailwind CSS

## Regras
- Use arrow functions para componentes
- Prefira `const` sobre `let`
- Testes com Vitest, não Jest
- Erros devem usar `Result<T, E>` (never throw)
- Nomes de arquivo em kebab-case
- Componentes em `src/components/`, páginas em `src/pages/`
```

---
## Recap

- Pré-requisitos
- Objetivos de aprendizagem
- Competências desenvolvidas
- 1. Introdução: por que 90% cometem esse erro
- 2. Erro 1: Confiar cegamente na saída da IA
- 3. Erro 2: Prompts vagos sem contexto
- 4. Erro 3: Pular code review e testes
- 5. Erro 4: Ignorar configuração do projeto (AGENTS.md / CLAUDE.md)
- Stack
- Regras
- 6. Erro 5: Tratar IA como resposta final

---
# Obrigado!

## Perguntas?
