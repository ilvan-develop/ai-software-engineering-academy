---
marp: true
theme: uncover
class:
  - lead
  - invert
---

<!-- _class: lead invert -->
<!-- _backgroundColor: "#1A1A2E" -->
<!-- _color: "#FFFFFF" -->

# **IA para Desenvolvedores**

**CapÃ­tulo 1 â€” Os 5 Erros ao Usar IA para Programar**

---

AI Software Engineering Academy â€” 2026

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Agenda

- Por que **90%** dos devs cometem esses erros
- Erro 1 â€” Confiar cegamente na saÃ­da da IA
- Erro 2 â€” Prompts vagos sem contexto
- Erro 3 â€” Pular code review e testes
- Erro 4 â€” Ignorar configuraÃ§Ã£o do projeto
- Erro 5 â€” Tratar IA como resposta final
- Os 5 mandamentos + fluxo ideal

*Nota do apresentador: Contextualize que este capÃ­tulo nÃ£o Ã© sobre "IA Ã© ruim", mas sobre "como usar IA profissionalmente".*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## O Problema: Por que 90% cometem esses erros?

A IA gera cÃ³digo em segundos â€” mas velocidade tem um custo oculto.

| Dado | Fonte |
|------|-------|
| **63%** dos devs encontraram erros inesperados | Stack Overflow Survey |
| **68%** tÃªm dificuldade em integrar IA no workflow | Stack Overflow Survey |
| **~40%** de erro sem regras configuradas | Claude Code Pro Pack |
| **~3%** com 12 regras â€” melhoria de **~13x** | Claude Code Pro Pack |

[imagem: grÃ¡fico de barras 40% vs 3%]

> O problema nÃ£o Ã© a IA. O problema Ã© **como usamos a IA**.

*Nota do apresentador: Enfatize os nÃºmeros â€” 63% e 68% sÃ£o da pesquisa oficial do Stack Overflow.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Erro 1 â€” Confiar cegamente na saÃ­da da IA

**DefiniÃ§Ã£o:** Aceitar cÃ³digo gerado por IA como correto sem questionamento.

```javascript
function calculateDiscount(price, coupon) {
  if (coupon === "SAVE10") {
    return price * 0.9;
  }
  return price; // Esqueceu de validar se price Ã© nÃºmero
}
calculateDiscount("cem reais", "SAVE10"); // NaN em produÃ§Ã£o
```

**Os 4 tipos de bug que a IA insere:**

| Tipo | Exemplo |
|------|---------|
| **LÃ³gica** | Valida email sÃ³ com includes("@") |
| **SeguranÃ§a** | SQL injection, senha em MD5 |
| **Performance** | N+1 queries, loop aninhado |
| **Compatibilidade** | Import de biblioteca que nÃ£o existe |

*Nota do apresentador: PeÃ§a para a audiÃªncia encontrar o bug. A IA acerta a sintaxe mas erra a lÃ³gica.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Como corrigir o Erro 1

**Passo a passo para todo cÃ³digo gerado por IA:**

1. Leia cada linha antes de implementar
2. Teste com casos extremos â€” vazio, null, negativo
3. Valide dependÃªncias sugeridas â€” IA pode inventar bibliotecas
4. Use type checking â€” TypeScript, mypy, Zod

> Trate a saÃ­da da IA como **rascunho inicial**, nÃ£o produto acabado.

*Nota do apresentador: A diferenÃ§a entre profissional e amador Ã© que o profissional verifica antes de entregar.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Erro 2 â€” Prompts vagos sem contexto

**DefiniÃ§Ã£o:** Pedidos genÃ©ricos que geram respostas genÃ©ricas.

| Vago | Estruturado |
|---------|---------------|
| "Melhore esse cÃ³digo" | "Refatore handleSubmit em src/forms.ts para async/await com try-catch" |
| IA nÃ£o sabe linguagem, critÃ©rio, contexto | IA sabe arquivo, aÃ§Ã£o, formato, restriÃ§Ãµes |

**CorreÃ§Ã£o â€” Template CIF:**

| Elemento | Exemplo |
|----------|---------|
| **C**ontexto | "No arquivo login.ts, funÃ§Ã£o authenticateUser..." |
| **I**ntenÃ§Ã£o | "...validar token JWT antes de consultar o banco" |
| **F**ormato | "...retorne Result<T,E>, sem throw, com testes em Vitest" |

*Nota do apresentador: Pergunte-se: "Um colega dev saberia o que fazer com esta instruÃ§Ã£o?"*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Erro 3 â€” Pular code review e testes

**DefiniÃ§Ã£o:** Ignorar revisÃ£o e testes para cÃ³digo gerado por IA.

```
Realidade: IA -> Copia e cola -> Commit -> Producao
Correto:   IA -> Review -> Testes -> Refinar -> Commit
```

**CorreÃ§Ã£o:**

1. **Code Review obrigatÃ³rio** â€” "Eu aceitaria isso num PR?"
2. **Testes como verificaÃ§Ã£o** â€” peÃ§a para a IA gerar testes tambÃ©m
3. **CI Pipeline** â€” todo cÃ³digo passa pelos mesmos checks

> Pular code review nÃ£o economiza tempo â€” terceiriza o risco para vocÃª.

*Nota do apresentador: A IA nÃ£o assume responsabilidade. Seu nome estÃ¡ no commit.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Erro 4 â€” Ignorar AGENTS.md / CLAUDE.md

**DefiniÃ§Ã£o:** NÃ£o configurar instruÃ§Ãµes persistentes para agentes de IA.

Sem instruÃ§Ãµes, a IA **chuta**: nÃ£o sabe React ou Vue, const ou function, Vitest ou Jest.

| ConfiguraÃ§Ã£o | Taxa de erro | Melhoria |
|-------------|:-----------:|:--------:|
| Sem regras | ~40% | â€” |
| Com 4 regras | ~11% | ~3,6x |
| Com 12 regras | ~3% | **~13,3x** |

**CorreÃ§Ã£o:** 5 minutos na raiz do projeto:

```markdown
# AGENTS.md
## Stack: React 18 + TypeScript + Tailwind
## Regras: arrow functions, const, Vitest, kebab-case
```

*Nota do apresentador: AGENTS.md Ã© a "memÃ³ria de longo prazo" do agente. Invista 5 min agora.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Erro 5 â€” Tratar IA como resposta final

**DefiniÃ§Ã£o:** Usar a primeira resposta da IA como soluÃ§Ã£o definitiva.

```javascript
// Primeira resposta
function validateEmail(email) {
  return email.includes("@");
  // Aceita "@", "a@"
}

// ApÃ³s refinamento com feedback
function validateEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
  // Rejeita "@", aceita "user@domain.com"
}
```

**CorreÃ§Ã£o â€” Processo Iterativo:**
1. Obtenha o rascunho
2. Revise
3. Feedback direcionado
4. Repita

*Nota do apresentador: SFEIR â€” ~35% menos iteraÃ§Ãµes com feedback estruturado. Seja especÃ­fico.*

---

<!-- _backgroundColor: "#1A1A2E" -->
<!-- _color: "#FFFFFF" -->

## Os 5 Mandamentos do Uso Correto de IA

| # | Mandamento | Por quÃª |
|---|------------|:------:|
| 1 | **Valide** toda saÃ­da | IA erra com confianÃ§a |
| 2 | **Estruture** prompts | Pedido fraco -> resposta fraca |
| 3 | **Revise e teste** | Seu nome estÃ¡ no commit |
| 4 | **Configure** o projeto | 5 min economizam horas |
| 5 | **Itere** sempre | Refinamento separa o mediano do excelente |

```
Fluxo ideal:
[Prompt] -> [IA gera] -> [Review] -> [Testes] -> [Refinar] -> [Commit]
    ^                                                             |
    +------------------- Iteracao --------------------------------+
```

*Nota do apresentador: Recapitule os 5 mandamentos. Fluxo ideal = ciclo, nÃ£o linha reta.*

---

<!-- _backgroundColor: "#1A1A2E" -->
<!-- _color: "#FFFFFF" -->

## Recados Finais

**Analogia:** IA Ã© um **estagiÃ¡rio brilhante, mas inexperiente**. RÃ¡pido, precisa de supervisÃ£o.

**Para levar:**
- IA Ã© ferramenta, nÃ£o substituta
- 5 min de configuraÃ§Ã£o = 13x menos erros
- Seu nome estÃ¡ no commit
- Itere, refine, valide â€” sempre

---

Leituras: github.com/copilot/docs | code.claude.com/docs | opencode.ai

Proximo: Agentes de IA na Pratica

*Nota do apresentador: "Da prÃ³xima vez que usar IA, lembre-se: a diferenÃ§a entre profissional e amador Ã© quem revisa."*
