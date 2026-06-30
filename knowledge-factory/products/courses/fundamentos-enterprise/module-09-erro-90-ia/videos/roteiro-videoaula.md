# Roteiro de Videoaula — O erro que 90% das pessoas cometem usando IA para programar

**Duracao total estimada:** 35 minutos
**Formato:** Videoaula gravada / Streaming
**Publico-alvo:** Desenvolvedores intermediarios

---

## Visao Geral do Video

| Item | Detalhe |
|------|---------|
| Titulo | O erro que 90% das pessoas cometem usando IA para programar |
| Duracao | 35 min |
| Cenas | 14 |
| Formato | Expositivo com demonstracao pratica |
| Nivel | Intermediario |

---

## Roteiro por Cena

### Cena 1 — INTRO

**Duracao:** 1:30

**Narracao:**
> Ola! Nesta aula vamos explorar: O erro que 90% das pessoas cometem usando IA para programar. Ao final, voce vai entender os conceitos fundamentais e como aplica-los na pratica. Vamos la?

**Visuais:**
- Tela de abertura com titulo do modulo. Animacao suave com o nome do curso.

**Texto na tela:**
```
[TITULO] O erro que 90% das pessoas cometem usando IA para programar
```

**Notas de direcao:**
- Tom energico e convidativo. Apresentar o problema que sera resolvido.

---

### Cena 2 — OBJECTIVES

**Duracao:** 1:00

**Narracao:**
> Vamos cobrir 5 objetivos principais: Identificar os 5 erros mais comuns ao usar IA para programar; Diferenciar uso produtivo de uso prejudicial de assistentes de IA; Aplicar técnicas de prompt estruturado para obter respostas precisas; Estabelecer um fluxo de validação e revisão para código gerado por IA; Configurar arquivos de instrução do projeto (AGENTS.md / CLAUDE.md) para melhorar a consistência do agente.

**Visuais:**
- Lista animada dos objetivos, um por vez com checkmark.

**Texto na tela:**
```
✓ Identificar os 5 erros mais comuns ao usar IA para programar
✓ Diferenciar uso produtivo de uso prejudicial de assistentes de IA
✓ Aplicar técnicas de prompt estruturado para obter respostas precisas
✓ Estabelecer um fluxo de validação e revisão para código gerado por IA
✓ Configurar arquivos de instrução do projeto (AGENTS.md / CLAUDE.md) para melhorar a consistência do agente
```

**Notas de direcao:**
- Falar pausadamente. Cada objetivo e uma promessa para o aluno.

---

### Cena 3 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: Pré-requisitos. Experiência básica com programação em qualquer linguagem Familiaridade com uso de assistentes de IA (GitHub Copilot, Claude Code, ChatGPT, etc.) Noções fundamentais de Git e versionamento

**Visuais:**
- Slides com topicos-chave. ```javascript
// 🚫 Código gerado por IA — parece certo, mas está errado
function calculateDiscount(price, coupon) {
  if (coupon === 'SAVE10') {
    return price * 0.9;
  }
  return price; // ❌ Esqueceu de validar se price é número
}

calculateDiscount('cem reais', 'SAVE10'); // NaN em produção
```

**Texto na tela:**
```
[Pré-requisitos]
```

**Notas de direcao:**
- Secao 2 de 10. Usar exemplos praticos.

---

### Cena 4 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: Objetivos de aprendizagem. Ao final desta aula, o aluno será capaz de: 1. **Identificar** os 5 erros mais comuns ao usar IA para programar 2. **Diferenciar** uso produtivo de uso prejudicial de assistentes de IA 3. **Aplicar** técnicas de prompt estruturado para obter respostas precisas

**Visuais:**
- Slides com topicos-chave. ```javascript
// 🚫 Código gerado por IA — parece certo, mas está errado
function calculateDiscount(price, coupon) {
  if (coupon === 'SAVE10') {
    return price * 0.9;
  }
  return price; // ❌ Esqueceu de validar se price é número
}

calculateDiscount('cem reais', 'SAVE10'); // NaN em produção
```

**Texto na tela:**
```
[Objetivos de aprendizagem]
```

**Notas de direcao:**
- Secao 3 de 10. Usar exemplos praticos.

---

### Cena 5 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: Competências desenvolvidas. Hard skills:** Prompt engineering aplicado à programação Code review de código gerado por IA Configuração de assistentes de IA no projeto

**Visuais:**
- Slides com topicos-chave. ```javascript
// 🚫 Código gerado por IA — parece certo, mas está errado
function calculateDiscount(price, coupon) {
  if (coupon === 'SAVE10') {
    return price * 0.9;
  }
  return price; // ❌ Esqueceu de validar se price é número
}

calculateDiscount('cem reais', 'SAVE10'); // NaN em produção
```

**Texto na tela:**
```
[Competências desenvolvidas]
```

**Notas de direcao:**
- Secao 4 de 10. Usar exemplos praticos.

---

### Cena 6 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 1. Introdução: por que 90% cometem esse erro. Era uma terça-feira comum. O desenvolvedor precisava de uma função simples para validar emails. Pediu ao ChatGPT, copiou o código, fez deploy. Na sexta, o banco de dados estava cheio de registros com emails como "usuario@". Aquela função — que parecia perfeita — só verificava se existia um "@" na string. A IA acertou a sintaxe. Errou a lógica. O desenvolvedor não revisou. Produção quebrou. Esse cenário se repete milhares de vezes todos os dias. Assistentes de IA geram código em segundos — mas essa velocidade tem um custo oculto. Pesquisas da indústria revelam um padrão preocupante: | Dado | Fonte |

**Visuais:**
- Slides com topicos-chave. ```javascript
// 🚫 Código gerado por IA — parece certo, mas está errado
function calculateDiscount(price, coupon) {
  if (coupon === 'SAVE10') {
    return price * 0.9;
  }
  return price; // ❌ Esqueceu de validar se price é número
}

calculateDiscount('cem reais', 'SAVE10'); // NaN em produção
```

**Texto na tela:**
```
[1. Introdução: por que 90% cometem esse erro]
```

**Notas de direcao:**
- Secao 5 de 10. Usar exemplos praticos.

---

### Cena 7 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 2. Erro 1: Confiar cegamente na saída da IA. Aceitar o código gerado pela IA como correto sem qualquer questionamento, validação ou revisão. A IA gera respostas com **alta fluência e aparência de confiança**. O código parece correto, compila e muitas vezes até passa em testes simples — mas pode conter bugs sutis de lógica, segurança ou performance. > "A IA erra com confiança, não com hesitação." — TechTudo O problema é psicológico: nosso cérebro associa fluência a competência. Quando a IA escreve um parágrafo ou função que "soa bem", relaxamos a guarda. Só que a IA não sabe o que está fazendo — ela está apenas completando padrões estatísticos.

**Visuais:**
- Slides com topicos-chave. ```javascript
// 🚫 Código gerado por IA — parece certo, mas está errado
function calculateDiscount(price, coupon) {
  if (coupon === 'SAVE10') {
    return price * 0.9;
  }
  return price; // ❌ Esqueceu de validar se price é número
}

calculateDiscount('cem reais', 'SAVE10'); // NaN em produção
```

**Texto na tela:**
```
[2. Erro 1: Confiar cegamente na saída da IA]
```

**Notas de direcao:**
- Secao 6 de 10. Usar exemplos praticos.

---

### Cena 8 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 3. Erro 2: Prompts vagos sem contexto. Fazer pedidos genéricos e esperar respostas precisas e úteis. A IA opera com base em probabilidades: quanto menos contexto, mais genérica a resposta. É como perguntar "Me recomenda um filme?" para um amigo — você vai receber uma lista genérica. Agora pergunte "Me recomenda um filme de suspense coreano com menos de 2 horas" — a resposta muda completamente. O mesmo vale para código. > "Pedido fraco, resposta fraca em escala industrial." — TechTudo

**Visuais:**
- Slides com topicos-chave. ```javascript
// 🚫 Código gerado por IA — parece certo, mas está errado
function calculateDiscount(price, coupon) {
  if (coupon === 'SAVE10') {
    return price * 0.9;
  }
  return price; // ❌ Esqueceu de validar se price é número
}

calculateDiscount('cem reais', 'SAVE10'); // NaN em produção
```

**Texto na tela:**
```
[3. Erro 2: Prompts vagos sem contexto]
```

**Notas de direcao:**
- Secao 7 de 10. Usar exemplos praticos.

---

### Cena 9 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 4. Erro 3: Pular code review e testes. Ignorar as etapas de revisão de código e testes automatizados para código gerado por IA, tratando-o como isento de erros. A velocidade da IA cria a ilusão de que o código já passou por um "controle de qualidade implícito". O desenvolvedor assume que, se a IA gerou, está correto. > "Se você copia e cola sem ler, o erro deixa de ser da ferramenta. Passa a ser seu." — TechTudo Essa falsa sensação de segurança é traiçoeira. O código gerado por IA **não foi revisado por ninguém**. Ele é o equivalente a um primeiro rascunho escrito por alguém que nunca usou seu sistema.

**Visuais:**
- Slides com topicos-chave. ```javascript
// 🚫 Código gerado por IA — parece certo, mas está errado
function calculateDiscount(price, coupon) {
  if (coupon === 'SAVE10') {
    return price * 0.9;
  }
  return price; // ❌ Esqueceu de validar se price é número
}

calculateDiscount('cem reais', 'SAVE10'); // NaN em produção
```

**Texto na tela:**
```
[4. Erro 3: Pular code review e testes]
```

**Notas de direcao:**
- Secao 8 de 10. Usar exemplos praticos.

---

### Cena 10 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 5. Erro 4: Ignorar configuração do projeto (AGENTS.md / CLAUDE.md). Não configurar arquivos de instrução persistente para os agentes de IA, deixando-os operar sem contexto do projeto. Arquivos como `AGENTS.md` (OpenCode) e `CLAUDE.md` (Claude Code) funcionam como a memória de longo prazo do agente. Eles contêm regras, padrões e convenções do projeto. Sem eles, a IA opera com conhecimento genérico. Ela não sabe se o projeto usa React 18 ou Vue 3. Não sabe se prefere `const` ou `function`. Não sabe se os testes são com Vitest ou Jest. **Ela chuta.** > "5 minutos de configuração economizam horas de retrabalho." — OpenCode Community

**Visuais:**
- Slides com topicos-chave. ```javascript
// 🚫 Código gerado por IA — parece certo, mas está errado
function calculateDiscount(price, coupon) {
  if (coupon === 'SAVE10') {
    return price * 0.9;
  }
  return price; // ❌ Esqueceu de validar se price é número
}

calculateDiscount('cem reais', 'SAVE10'); // NaN em produção
```

**Texto na tela:**
```
[5. Erro 4: Ignorar configuração do projeto (AGENTS.md / CLAUDE.md)]
```

**Notas de direcao:**
- Secao 9 de 10. Usar exemplos praticos.

---

### Cena 11 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: Stack. React 18 + TypeScript + Tailwind CSS

**Visuais:**
- Slides com topicos-chave. ```javascript
// 🚫 Código gerado por IA — parece certo, mas está errado
function calculateDiscount(price, coupon) {
  if (coupon === 'SAVE10') {
    return price * 0.9;
  }
  return price; // ❌ Esqueceu de validar se price é número
}

calculateDiscount('cem reais', 'SAVE10'); // NaN em produção
```

**Texto na tela:**
```
[Stack]
```

**Notas de direcao:**
- Secao 10 de 10. Usar exemplos praticos.

---

### Cena 12 — CODE-DEMO

**Duracao:** 4:00

**Narracao:**
> Vamos ver na pratica como isso funciona. Observe este codigo em javascript:

**Visuais:**
- Tela dividida: editor de codigo a esquerda, terminal/output a direita.

**Texto na tela:**
```
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
```

**Notas de direcao:**
- Explicar linha por linha. Destacar pontos importantes com zoom ou realce.

---

### Cena 13 — SUMMARY

**Duracao:** 1:30

**Narracao:**
> Recapitulando: vimos Pré-requisitos, Objetivos de aprendizagem, Competências desenvolvidas, 1. Introdução: por que 90% cometem esse erro, 2. Erro 1: Confiar cegamente na saída da IA, 3. Erro 2: Prompts vagos sem contexto. Esses conceitos sao fundamentais para sua formacao.

**Visuais:**
- Lista resumida com icones. Transicao suave para encerramento.

**Texto na tela:**
```
✓ Pré-requisitos
✓ Objetivos de aprendizagem
✓ Competências desenvolvidas
✓ 1. Introdução: por que 90% cometem esse erro
✓ 2. Erro 1: Confiar cegamente na saída da IA
✓ 3. Erro 2: Prompts vagos sem contexto
```

**Notas de direcao:**
- Reforcar os aprendizados principais. Conectar com o proximo modulo.

---

### Cena 14 — OUTRO

**Duracao:** 0:30

**Narracao:**
> Na proxima aula, vamos aprofundar esses conceitos. Nao perca!

**Visuais:**
- Tela final com links, inscricao, e teaser da proxima aula.

**Texto na tela:**
```
Proximo modulo: [TITULO DO PROXIMO MODULO]
```

**Notas de direcao:**
- Chamada para acao: inscrever-se, comentar, compartilhar.

---

## Checklist de Producao

- [ ] Roteiro revisado
- [ ] Slides preparados
- [ ] Ambiente de codigo configurado
- [ ] Microfone testado
- [ ] Gravacao de tela configurada (1920x1080)
- [ ] Exemplos de codigo testados
- [ ] Legendas geradas
- [ ] Thumbnail criada
- [ ] Descricao e tags preenchidas
- [ ] Capitulos do video marcados

---

## Sugestoes de Thumbnail

- Texto: 'O erro que 90% das pessoas cometem usando IA para '
- Cor de fundo: azul escuro (#1a2332)
- Destaque: codigo ou diagrama ao fundo
- Rosto do apresentador no canto inferior direito

---

## SEO

**Titulo:** O erro que 90% das pessoas cometem usando IA para programar | Arquitetura Enterprise
**Descricao:** Aprenda o erro que 90% das pessoas cometem usando ia para programar. Nesta aula abordamos conceitos fundamentais com exemplos praticos em TypeScript.
**Tags:** arquitetura, software, enterprise, typescript, desenvolvimento
