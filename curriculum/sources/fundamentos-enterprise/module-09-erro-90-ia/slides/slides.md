# Módulo 09 — Slides

---

## Slide 1: Título

**O Erro de 90% ao Usar IA para Programar**
Como usar IA sem comprometer seu código

---

## Slide 2: O Problema

```
63% dos devs encontraram erros inesperados ao usar IA
68% têm dificuldade em integrar IA nos workflows

Sem regras:   ~40% de erro no código gerado
Com 12 regras: ~3% de erro → 13,3x melhor
```

A IA não erra por hesitação — erra com confiança

---

## Slide 3: Os 5 Erros

| # | Erro | Impacto |
|---|------|---------|
| 1 | Confiar cegamente na IA | Bugs em produção |
| 2 | Prompts vagos sem contexto | Respostas genéricas |
| 3 | Pular code review e testes | Dívida técnica e segurança |
| 4 | Ignorar AGENTS.md/CLAUDE.md | Comportamento inconsistente |
| 5 | Tratar IA como resposta final | Resultados superficiais |

---

## Slide 4: Erro 1 — Confiar Cegamente

```
// Código gerado por IA — parece certo, está errado
function calculateDiscount(price, coupon) {
  if (coupon === 'SAVE10') return price * 0.9;
  return price; // ❌ price pode ser string!
}

calculateDiscount('cem reais', 'SAVE10'); // NaN
```

**Solução:** Leia cada linha. Teste casos extremos. Valide dependências.

---

## Slide 5: Erro 2 — Prompts Vagos

```
❌ "Melhore esse código"
   - Qual linguagem? Critério? Contexto?

✅ "Refatore handleSubmit em src/forms.ts
   para usar async/await com try-catch,
   mantendo comportamento e padrão do projeto"
   - Arquivo, ação, restrições, formato
```

**Regra de ouro:** Contexto + Intenção + Formato Esperado

---

## Slide 6: Erro 3 — Pular Code Review

```
"Se você copia e cola sem ler,
o erro deixa de ser da ferramenta.
Passa a ser seu."

— TechTudo
```

**Solução:**
1. Code review obrigatório (como revisaria de um colega)
2. Peça testes junto com o código
3. CI pipeline para todo código, inclusive IA

---

## Slide 7: Erro 4 — Ignorar Configuração

```
Sem AGENTS.md/CLAUDE.md → IA chuta padrões

AGENTS.md mínimo:
  Stack: React 18 + TS + Tailwind
  Regras: arrow functions, const, Vitest
  Estrutura: components/, pages/, lib/
```

**5 minutos de setup economizam horas de retrabalho**

---

## Slide 8: Erro 5 — Tratar como Resposta Final

```
🚫 Primeira resposta:
  validateEmail(email) { return email.includes('@'); }

✅ Versão refinada:
  validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  }
```

**IA é processo iterativo, não resposta final**

---

## Slide 9: Fluxo Ideal

```
[Prompt] → [IA rascunha] → [Review] → [Testes] → [Refinamento] → [Commit]
    ↑                                                          │
    └────────────────── Iteração (feedback) ──────────────────┘
```

---

## Slide 10: Os 5 Mandamentos

| # | Mandamento | Por quê |
|---|------------|---------|
| 1 | **Valide** toda saída | IA erra com confiança |
| 2 | **Estruture** prompts | Pedido fraco → resposta fraca |
| 3 | **Revise e teste** | Seu nome está no commit |
| 4 | **Configure** o projeto | 5 min economizam horas |
| 5 | **Itere** | Refinamento separa o mediano do excelente |

---

## Slide 11: Analogia Final

```
Usar IA é como ter um estagiário brilhante, mas inexperiente:
  ✅ Rápido, escreve bem
  ❗ Precisa de supervisão, contexto, revisão
  ❌ Confiar cegamente é negligência
  ❌ Ignorar é desperdício

O profissional sábio sabe quando delegar,
quando revisar e como orientar.
```

---

## Slide 12: Para refletir

> "A primeira resposta raramente é a melhor. Ela é o ponto de partida, não o produto final."

> "O responsável é você. A ferramenta é só a ferramenta." — GitHub Copilot Docs

> "Give Claude a check it can run. It's the difference between a session you watch and one you walk away from." — Claude Code Docs
