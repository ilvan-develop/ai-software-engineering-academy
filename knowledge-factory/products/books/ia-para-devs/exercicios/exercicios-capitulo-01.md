# Exercicios - Capitulo 1: Os 5 Erros ao Usar IA para Programar

> **Modulo:** IA para Desenvolvedores  
> **Total de exercicios:** 5  
> **Progressao:** Facil -> Medio -> Dificil  
> **Tempo total estimado:** 75-95 min

---

## Exercicio 1 - Facil: Bingo dos Erros

**Tempo estimado:** 10 min  
**Tema:** Identificar os 5 erros em situacoes reais

### Contexto
Voce esta fazendo code review de 5 commits. Cada commit contem **um** dos 5 erros classicos do capitulo.

### Cenarios

| Commit | Descricao |
|--------|-----------|
| **A** | O dev pediu "faz ai um sistema de login" e recebeu codigo generico em PHP, mas o projeto e Node.js. |
| **B** | O dev pediu funcao de ordenacao, copiou a primeira resposta, subiu para producao. Ordenava numeros como strings: [1, 10, 2, 20]. |
| **C** | O commit tem 14 arquivos alterados. Nenhum teste novo. O dev disse "a IA garantiu que esta certo". |
| **D** | O dev entrou no projeto agora. Pediu componente novo. IA usou any, var e classes - projeto usa TS strict. |
| **E** | O dev pediu validacao de email. IA devolveu email.includes("@"). Aceitou como final e fechou a task. |

### Tarefa
1. Associe cada commit (A-E) ao erro correspondente (1-5):
   - Erro 1: Confiar cegamente na saida da IA
   - Erro 2: Prompts vagos sem contexto
   - Erro 3: Pular code review e testes
   - Erro 4: Ignorar configuracao do projeto
   - Erro 5: Tratar IA como resposta final
2. Explique em uma frase a correcao.

### Template de resposta
```
| Commit | Erro | Correcap (1 frase) |
|--------|------|-------------------|
| A      |      |                    |
| B      |      |                    |
| C      |      |                    |
| D      |      |                    |
| E      |      |                    |
```

### Criterios de correcao
| Criterio | Peso |
|----------|------|
| Associacao correta de cada commit ao erro | 60% |
| Clareza e precisao da correcao sugerida | 40% |

**Nota minima:** 4/5 acertos.

### Gabarito comentado
```
| Commit | Erro | Por que |
|--------|------|---------|
| A | Erro 2 - Prompt vago | "Faz ai" nao informa stack, linguagem ou requisitos. |
| B | Erro 1 - Confianca cega | Codigo parecia certo, mas logica errada. Dev nao testou. |
| C | Erro 3 - Pular review/testes | 14 arquivos sem testes e bandeira vermelha. |
| D | Erro 4 - Ignorar configuracao | Sem AGENTS.md, IA nao sabia padroes. |
| E | Erro 5 - Resposta final | Primeira resposta superficial; iterar e necessario. |
```


## Exercicio 2 - Facil/Medio: Diagnostico e Reescrita de Prompt

**Tempo estimado:** 15 min  
**Tema:** Erro 2 - Estruturar prompts com contexto, intencao e formato

### Contexto
Um colega esta frustrado porque a IA "nao entende o que ele quer". Os prompts dele:
```
1. "Faz uma API de produtos"
2. "Melhora esse codigo"
3. "Faz testes pra minha funcao"
4. "Cria um componente de login"
5. "Otimiza a query"
```

### Tarefa
Para cada prompt:
1. Identifique o que esta faltando (Contexto + Intencao + Formato)
2. Reescreva seguindo Contexto -> Intencao -> Formato Esperado
3. Adicione pelo menos 2 restricoes explicitas

### Template
```
### Prompt 1: "Faz uma API de produtos"
**O que esta faltando:**
- 
- 
**Prompt reescrito:**
```

### Gabarito parcial
```
### Prompt 1: "Faz uma API de produtos"
**O que esta faltando:**
- Linguagem/framework (Node? Python? Java?)
- Estrutura dos endpoints (REST? GraphQL?)
- Formato de resposta (JSON? XML?)
- Persistencia (banco? ORM?)

**Prompt reescrito:**
"Crie API REST de produtos em Node.js + Express + TypeScript.
Requisitos: GET /products (paginado), GET /products/:id, POST, PUT, DELETE.
Validacoes: Nome obrigatorio 3-100 chars, Preco positivo, Estoque >= 0.
Regras: Zod validacao, Prisma ORM, Result<T,E> sem throw, Swagger."
```

### Criterios de correcao
| Criterio | Peso |
|----------|------|
| Diagnostico correto do que falta | 30% |
| Prompt inclui Contexto+Intencao+Formato | 40% |
| Restricoes explicitas adicionadas | 20% |
| Clareza e detalhe | 10% |

---

## Exercicio 3 - Medio: AGENTS.md - Configuracao de Projeto

**Tempo estimado:** 15 min  
**Tema:** Erro 4 - Criar arquivo de instrucao para IA

### Contexto
Novo projeto: sistema de agendamento de consultas medicas.
- Frontend: React 19 + TypeScript + Tailwind CSS + React Query
- Backend: NestJS + Prisma + PostgreSQL
- Testes: Vitest (unitarios) + Playwright (e2e)
- Qualidade: ESLint + Prettier + Husky
- Padroes: Clean Architecture, DDD, Conventional Commits
- Estilo: arrow functions, camelCase, kebab-case para arquivos

### Tarefa
Criar AGENTS.md completo com:
1. Cabecalho - Nome e proposito
2. Stack - Tecnologias e versoes
3. Regras de codigo - Minimo 8 regras
4. Fluxo de trabalho - Passo a passo
5. Checklist de qualidade - Intens verificaveis
6. Limites - O que NAO faz

### Template
```markdown
# Agente: Full Stack - Agendamento Medico
## Proposito
## Stack
## Regras de Codigo
## Fluxo de Trabalho
## Checklist de Qualidade
## Limites
```

### Criterios de correcao
| Criterio | Peso |
|----------|------|
| Stack completa | 15% |
| Minimo 8 regras especificas | 25% |
| Fluxo de trabalho logico | 20% |
| Checklist com intens verificaveis | 20% |
| Limites definidos | 10% |
| Clareza e organizacao | 10% |

### Gabarito (regras esperadas)
- Arrow functions para componentes React, function para servicos NestJS
- Arquivos em kebab-case, pastas em camelCase
- Componentes em src/components/, paginas em src/pages/
- Testes obrigatorios para logica > 5 linhas
- Erros: Result<T,E> no backend (nunca throw)
- Commits: Conventional Commits (feat:, fix:, chore:, docs:, refactor:)
- Queries Prisma: verificar N+1 com include/select explicito
- Tailwind: classes utilitarias, nao CSS customizado

---

## Exercicio 4 - Medio/Dificil: Auditoria de PR com IA

**Tempo estimado:** 20 min  
**Tema:** Erro 1 + Erro 3 + Erro 5 - Revisao de codigo gerado por IA

### Contexto
Voce e tech lead. Dev junior abriu PR com codigo 100% gerado por IA. Ele disse: "A IA fez tudo, revisei por cima, parece ok."

```typescript
import express from "express"
import { createPool } from "mysql2"
const app = express()
const pool = createPool({
  host: "localhost", user: "root",
  password: "senha123", database: "loja"
})
app.get("/users", async (req, res) => {
  const { name, page } = req.query
  const q = `SELECT * FROM users WHERE name LIKE "%${name}%" LIMIT 20 OFFSET ${(page||1)*20}`
  const [rows] = await pool.query(q)
  res.json(rows)
})
app.post("/users", async (req, res) => {
  const { name, email, password } = req.body
  if (!name || !email) { res.status(400).send("Faltam"); return }
  const hash = crypto.createHash("md5").update(password).digest("hex")
  await pool.query(`INSERT INTO users VALUES ("${name}", "${email}", "${hash}")`)
  res.status(201).json({ message: "OK" })
})
app.listen(3000)
```

### Tarefa
1. Identifique minimo 6 problemas
2. Classifique: Vermelho Seguranca | Amarelo Logica | Azul Performance | Branco Padrao
3. Proponha correcao para cada
4. Explique qual erro do capitulo o dev cometeu

### Template
```
| # | Problema | Categoria | Correcap |
|---|----------|-----------|----------|
| 1 | ... | ... | ... |
Erros do capitulo: ...
```

### Criterios de correcao
| Criterio | Peso |
|----------|------|
| Identificou minimo 6 problemas | 40% |
| Classificacao correta | 20% |
| Correcoes iveis e seguras | 25% |
| Identificou erros do capitulo | 15% |

### Gabarito
| # | Problema | Cat | Correcap |
|---|----------|-----|----------|
| 1 | Senha hardcoded | Vermelho | process.env.DB_PASSWORD |
| 2 | SQL Injection (name) | Vermelho | Prepared statements |
| 3 | SQL Injection (INSERT) | Vermelho | Prepared statements |
| 4 | MD5 para senhas | Vermelho | bcrypt.hash() |
| 5 | Paginacao incorreta | Amarelo | (page-1)*20 |
| 6 | Sem validacao de password | Amarelo | 8 chars minimo |
| 7 | Sem try-catch | Azul | Middleware de erro |

Erros: Erro 1 (confianca), Erro 3 (pular review), Erro 5 (primeira resposta)


## Exercicio 5 - Dificil: Pipeline de Validacao para Codigo Gerado por IA

**Tempo estimado:** 25 min  
**Tema:** Integracao dos 5 erros em fluxo automatizado

### Contexto
Sua empresa adotou IA como ferramenta e quer garantias de qualidade. Crie script que valide codigo gerado por IA.

### Tarefa
Implementar em TypeScript/Node.js:

1. analyzePrompt - O prompt tem contexto, intencao e formato?
2. staticAnalysis - Detecta console.log, senhas, SQL sem prepared statements, funcao sem tipo
3. checkTests - O diff contem .test.ts ou .spec.ts?
4. runQualityChecklist - Verifica >= 6 intens do AGENTS.md
5. validateAICode - Orquestra tudo e retorna ValidationResult

### Interface
```typescript
interface ValidationResult {
  prompt: PromptCheck; staticAnalysis: StaticAnalysis
  testCoverage: TestCheck; qualityChecklist: QualityItem[]
  passed: boolean; score: number; blockers: string[]; warnings: string[]
}
interface PromptCheck {
  hasContext: boolean; hasIntention: boolean; hasFormat: boolean; score: number
}
function analyzePrompt(prompt: string): PromptCheck
function staticAnalysis(code: string): StaticAnalysis
function checkTests(diff: string): TestCheck
function runQualityChecklist(code: string): QualityItem[]
function validateAICode(prompt: string, code: string, diff: string): ValidationResult
```

### Criterios de correcao
| Criterio | Peso |
|----------|------|
| PromptCheck com heuristicas | 20% |
| StaticAnalysis detecta >= 4 padroes | 25% |
| TestCheck funciona | 15% |
| QualityChecklist >= 6 intens | 20% |
| Funcao principal orquestra | 20% |

Extra (+20%): Exit code 1 se score < 70 ou blockers > 0.

### Gabarito (trecho)
```typescript
function analyzePrompt(prompt: string): PromptCheck {
  const ctx = /(arquivo|funcao|componente|modulo|projeto)/i.test(prompt)
  const intent = /(criar|refatorar|implementar|corrigir|otimizar)/i.test(prompt)
  const fmt = /(retorne|formato|estrutura|deve|precisa)/i.test(prompt)
  return { hasContext: ctx, hasIntention: intent, hasFormat: fmt,
    score: [ctx, intent, fmt].filter(Boolean).length * 33.33 }
}
```

---

## Exercicio 6 - Medio: Classificador de Erros em Prompts Reais

**Tempo estimado:** 15 min  
**Tema:** Erro 1 + Erro 2 + Erro 5 - Classificar e corrigir prompts ruins

### Contexto
Voce herdou 6 prompts que um colega usou com a IA. Cada prompt contem 1 ou mais dos 5 erros.

#### Prompt A
```
cria um hook
```

#### Prompt B
```
Faz a tela de login igual do ifood
```

#### Prompt C
```
Gere uma API REST completa com Node.js, Express, TypeScript, Prisma, autenticacao JWT, upload de arquivos, email transacional, cache Redis, rate limiting, testes unitarios e2e, deploy Docker e pipeline CI/CD. Faca tudo agora.
```

#### Prompt D
```
Refatore a funcao abaixo para ficar mais rapida. Nao muda o comportamento.

function process(items) {
  for (let i = 0; i < items.length; i++) {
    for (let j = 0; j < items.length; j++) {
      // calc
    }
  }
}
```

#### Prompt E
```
explique codigo
```

#### Prompt F
```
Crie um componente React que exibe uma lista de usuarios. Contexto: projeto Next 14 App Router + Tailwind + Server Components. A lista vem de uma API externa (https://api.exemplo.com/users). Deve ter loading state, empty state, error state e paginacao. O componente deve ser Server Component que busca dados direto, com um Client Component apenas para o paginacao. Retorne o codigo completo com tipos TypeScript.
```

### Tarefa
Para CADA prompt (A-F):
1. Identifique qual(is) erro(s) do capitulo esta presente
2. Classifique a gravidade: Baixa / Media / Alta (justifique)
3. Se o prompt for ruim, reescreva-o seguindo Contexto + Intencao + Formato
4. Se o prompt for bom, justifique por que

### Template
```
### Prompt A: "cria um hook"
Erros:
Gravidade:
Prompt reescrito:
```

### Criterios de Correcao
| Criterio | Peso |
|----------|------|
| Identificacao correta dos erros (minimo 80%) | 40% |
| Classificacao de gravidade justificada | 20% |
| Reescrlta segue Contexto+Intencao+Formato | 40% |

### Gabarito (resumo)
- **A:** Erro 2 (vago). Gravidade Alta. Sem contexto nenhum.
- **B:** Erro 2 (vago). Gravidade Alta. "Igual do iFood" nao e especificacao.
- **C:** Erro 2 + Erro 5. Gravidade Media. Escopo amplo demais; pedir tudo de uma vez gera codigo superficial.
- **D:** Bom prompt! Tem contexto (funcao), intencao (otimizar) e formato (nao mudar comportamento). Nenhum erro.
- **E:** Erro 2 (vago). Gravidade Alta. "explique codigo" nao diz qual arquivo, funcao ou aspecto.
- **F:** Bom prompt! Contexto (Next 14, App Router, Tailwind, Server Components), intencao (lista de usuarios), formato (codigo completo TS).

---
## Exercicio 7 - Medio: Analise de Custo dos Erros em Projeto Real

**Tempo estimado:** 15 min  
**Tema:** Impacto dos 5 erros no orcamento e cronograma

### Contexto
Uma startup gastou R$ 50.000,00 em credits de IA em 3 meses. O CTO pediu uma analise do retorno. Levantamento mostrou:

- 40% do codigo gerado precisou ser reescrito (Erro 1 - confianca cega)
- 30% do tempo foi gasto refinando prompts porque nao havia contexto (Erro 2 - prompts vagos)
- 2 incidentes em producao por codigo nao revisado (Erro 3 - pular review)
- Nenhum AGENTS.md ou CLAUDE.md foi criado (Erro 4 - ignorar config)
- Cada feature passou por 1 unica iteracao com IA (Erro 5 - primeira resposta)

### Tarefa
1. **Calcule o desperdicio financeiro** de cada erro (em R$)
2. **Calcule o desperdicio de tempo** total (em %)
3. **Proponha um plano de correcao** com 3 acoes que eliminem ou reduzam cada erro
4. **Estime a economia** (R$ e %) se as correcoes forem implementadas

### Template
```
### Analise de Custo
| Erro | Custo R$ | % do orcamento | Impacto |
|------|----------|----------------|---------|
| 1    |          |                |         |
| 2    |          |                |         |
| 3    |          |                |         |
| 4    |          |                |         |
| 5    |          |                |         |

### Plano de Correcao
1. 
2. 
3. 

### Economia Estimada
R$: 
%:
```

### Criterios de Correcao
| Criterio | Peso |
|----------|------|
| Calculos de desperdicio coerentes com os dados | 30% |
| Plano de correcao com acoes especificas viaveis | 40% |
| Estimativa de economia justificada | 30% |

### Gabarito (valores aproximados)
| Erro | Custo | % | Impacto |
|------|-------|---|---------|
| 1 | R$ 20.000 | 40% | Codigo reescrito, retrabalho |
| 2 | R$ 15.000 | 30% | Tempo perdido refinando prompts |
| 3 | R$ 5.000* | 10% | 2 incidentes em producao (custo estimado) |
| 4 | R$ 5.000 | 10% | IA sem contexto gera codigo fora dos padroes |
| 5 | R$ 5.000 | 10% | Multiplas iteracoes evitaveis |

*Nota: Erro 3 inclui custo de hotfix, reuniao pos-incidente e dano a reputacao.

**Plano:** (1) Criar AGENTS.md obrigatorio no init do projeto. (2) Workshop de engenharia de prompt com template padrao. (3) Pipeline CI com validacao automatica + code review obrigatorio. **Economia estimada:** R$ 30.000 (60%) e 50% do tempo.

---

## Resumo - Capitulo 1

| # | Exercicio | Dificuldade | Tema | Tempo |
|---|-----------|-------------|------|-------|
| 1 | Bingo dos Erros | Facil | Identificar os 5 erros | 10 min |
| 2 | Diagnostico de Prompt | Facil/Medio | Reescrever prompts | 15 min |
| 3 | AGENTS.md | Medio | Configurar projeto | 15 min |
| 4 | Auditoria de PR | Medio/Dificil | Revisar codigo IA | 20 min |
| 5 | Pipeline de Validacao | Dificil | Automatizar | 25 min |
