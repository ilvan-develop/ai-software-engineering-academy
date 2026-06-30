# Exercícios Complementares — O erro que 90% cometem usando IA para programar

**Módulo de referência:** `content/modules/001-erro-90-por-cento-ia-programar.md`
**Nível:** Conceitos / Engenharia
**Público-alvo:** Desenvolvedores iniciantes e intermediários

---

## Sumário

1. [Exercícios Práticos](#1-exercícios-práticos)
   - [Fácil: Identifique o erro](#11-exercício-fácil-identifique-o-erro)
   - [Médio: Refatore o prompt e o código](#12-exercício-médio-refatore-o-prompt-e-o-código)
   - [Difícil: Auditoria de PR com IA](#13-exercício-difícil-auditoria-de-pr-com-ia)
2. [Mini-Projeto: Guia de Adoção de IA para o Time](#2-mini-projeto-guia-de-adoção-de-ia-para-o-time)
3. [Laboratório Guiado: Configure AGENTS.md do Zero](#3-laboratório-guiado-configure-agentsmd-do-zero)

---

## 1. Exercícios Práticos

---

### 1.1 Exercício Fácil — Identifique o Erro

**Tempo estimado:** 8 minutos

#### Contexto

Você é desenvolvedor júnior em uma startup de fintech. Seu tech lead pediu para você revisar um trecho de código que ele suspeita ter sido gerado por IA sem revisão adequada. O código está em um arquivo chamado `src/transaction.ts`:

```typescript
function formatTransactionAmount(value: number): string {
  return `R$ ${value.toFixed(2)}`;
}
```

#### Instruções

1. Identifique qual(is) dos 5 erros do módulo está(ão) presente(s) neste cenário
2. Execute a função com os seguintes valores e anote o resultado de cada um:
   - `formatTransactionAmount(150.50)`
   - `formatTransactionAmount(0)`
   - `formatTransactionAmount(-50.00)`
   - `formatTransactionAmount(null)`
   - `formatTransactionAmount("cem")`
3. Escreva uma versão corrigida e robusta da função
4. Explique em uma frase qual erro do módulo foi cometido

#### Critérios de sucesso

- [ ] Identificou corretamente o **Erro 1 (confiar cegamente)** e ao menos um outro erro entre os 5
- [ ] Percebeu que `null`, `undefined` e strings quebram a função
- [ ] Versão corrigida inclui validação de tipo e valor
- [ ] Explicação clara do erro cometido

#### Gabarito comentado

**Erros identificados:**

| Erro | Justificativa |
|------|---------------|
| **Erro 1 — Confiar cegamente** | A função parece correta, mas não trata casos extremos |
| **Erro 3 — Pular code review e testes** | O tech lead suspeita que não houve revisão |
| **Erro 5 — Tratar como resposta final** | Provavelmente a primeira resposta da IA foi aceita sem iteração |

**Resultados das execuções:**

```typescript
formatTransactionAmount(150.50)    // "R$ 150.50" ✅
formatTransactionAmount(0)         // "R$ 0.00" ✅
formatTransactionAmount(-50.00)    // "R$ -50.00" ⚠️  Aceita negativo (pode ser regra de negócio)
formatTransactionAmount(null)      // ❌ TypeError: Cannot read property 'toFixed' of null
formatTransactionAmount("cem")     // ❌ TypeError: "cem".toFixed is not a function
```

**Versão corrigida:**

```typescript
function formatTransactionAmount(value: unknown): string {
  if (typeof value !== 'number' || !Number.isFinite(value)) {
    throw new TypeError('formatTransactionAmount: value must be a finite number');
  }
  if (value < 0) {
    throw new RangeError('formatTransactionAmount: value cannot be negative');
  }
  return `R$ ${value.toFixed(2)}`;
}
```

**Frase-resposta:** O erro foi confiar cegamente na saída da IA (Erro 1) sem testar casos extremos como `null`, tipos inesperados e valores negativos, tratando o rascunho como produto acabado (Erro 5).

---

### 1.2 Exercício Médio — Refatore o Prompt e o Código

**Tempo estimado:** 15 minutos

#### Contexto

Você está revisando o PR de um colega que usou IA para implementar uma rota de API. Ele usou o prompt:

> "Faz uma rota pra buscar usuário por ID"

A IA gerou o código abaixo. O PR está marcado como "Aguardando revisão".

```javascript
// routes/users.js
const express = require('express');
const router = express.Router();

router.get('/user/:id', (req, res) => {
  const id = req.params.id;
  const user = database.query(`SELECT * FROM users WHERE id = ${id}`);
  res.json(user);
});

module.exports = router;
```

#### Instruções

1. **Identifique os erros** no código gerado (mínimo 3)
2. **Classifique os erros** segundo a tabela do módulo (Lógica, Segurança, Performance, Compatibilidade)
3. **Reescreva o prompt** seguindo a estrutura **Contexto + Intenção + Formato Esperado**
4. **Reescreva o código corrigido** usando Express com async/await, validação de entrada, prepared statements e tratamento de erros
5. **Adicione testes** para pelo menos 2 cenários (sucesso e erro)

#### Critérios de sucesso

- [ ] Identificou SQL injection (Segurança), falta de validação de ID (Lógica), callback sem async/await (Performance)
- [ ] Prompt reescrito inclui: stack (Node + Express + PostgreSQL), regra de negócio (ID numérico, 404 se não existir), formato (JSON com status code)
- [ ] Código corrigido usa prepared statements e try-catch
- [ ] Testes cobrem usuário encontrado e usuário não encontrado

#### Gabarito comentado

**Erros identificados:**

| Tipo | Problema | Gravidade |
|------|----------|-----------|
| **Segurança** | SQL injection com template string `${id}` | Crítico |
| **Lógica** | Nenhuma validação do parâmetro `id` | Alto |
| **Lógica** | Nenhum tratamento para usuário inexistente (sempre retorna 200) | Alto |
| **Performance** | Função callback síncrona em operação de I/O | Médio |
| **Compatibilidade** | `database.query` — não especifica biblioteca, pode nem existir | Médio |

**Prompt reescrito:**

> Crie uma rota GET `/users/:id` em Node.js com Express e PostgreSQL usando `pg` (node-postgres). O parâmetro `id` deve ser um número inteiro positivo. Valide o ID e, se inválido, retorne 400. Use prepared statements para consultar o banco. Se o usuário não for encontrado, retorne 404 com `{ error: "User not found" }`. Se encontrado, retorne 200 com os dados do usuário (excluindo a senha). Use `async/await` com `try-catch`. Formato da resposta: JSON.

**Código corrigido:**

```javascript
// routes/users.js
const express = require('express');
const router = express.Router();
const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

router.get('/users/:id', async (req, res) => {
  try {
    const id = parseInt(req.params.id, 10);

    if (!Number.isInteger(id) || id <= 0) {
      return res.status(400).json({ error: 'ID must be a positive integer' });
    }

    const result = await pool.query(
      'SELECT id, name, email, created_at FROM users WHERE id = $1',
      [id]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'User not found' });
    }

    return res.status(200).json(result.rows[0]);
  } catch (error) {
    console.error('Error fetching user:', error);
    return res.status(500).json({ error: 'Internal server error' });
  }
});

module.exports = router;
```

**Testes (Vitest):**

```javascript
import { describe, it, expect, vi } from 'vitest';
import request from 'supertest';
import express from 'express';

// Mock do pool
vi.mock('../db', () => ({
  pool: {
    query: vi.fn(),
  },
}));

const app = express();
app.use('/api', router);

describe('GET /api/users/:id', () => {
  it('retorna 200 com os dados do usuário quando encontrado', async () => {
    const mockUser = { id: 1, name: 'João', email: 'joao@email.com' };
    pool.query.mockResolvedValue({ rows: [mockUser] });

    const res = await request(app).get('/api/users/1');
    expect(res.status).toBe(200);
    expect(res.body).toEqual(mockUser);
  });

  it('retorna 404 quando usuário não existe', async () => {
    pool.query.mockResolvedValue({ rows: [] });

    const res = await request(app).get('/api/users/999');
    expect(res.status).toBe(404);
    expect(res.body).toHaveProperty('error');
  });

  it('retorna 400 para ID inválido', async () => {
    const res = await request(app).get('/api/users/abc');
    expect(res.status).toBe(400);
    expect(res.body).toHaveProperty('error');
  });
});
```

---

### 1.3 Exercício Difícil — Auditoria de PR com IA

**Tempo estimado:** 25 minutos

#### Contexto

Um desenvolvedor gerou o código abaixo usando IA com o prompt: "Cria um serviço de cache em Node". Ele abriu um PR e marcou você como revisor. O código **passou em todos os testes automatizados** da pipeline, mas você desconfia de problemas estruturais.

```typescript
// src/cache/memory-cache.ts
interface CacheEntry {
  value: unknown;
  expiry: number;
}

export class MemoryCache {
  private store: Map<string, CacheEntry>;
  private defaultTTL: number;

  constructor(defaultTTLMs: number = 60000) {
    this.store = new Map();
    this.defaultTTL = defaultTTLMs;
  }

  set(key: string, value: unknown, ttlMs?: number): void {
    const ttl = ttlMs ?? this.defaultTTL;
    this.store.set(key, {
      value,
      expiry: Date.now() + ttl,
    });
  }

  get(key: string): unknown | null {
    const entry = this.store.get(key);
    if (!entry) return null;
    if (Date.now() > entry.expiry) {
      this.store.delete(key);
      return null;
    }
    return entry.value;
  }

  delete(key: string): void {
    this.store.delete(key);
  }

  clear(): void {
    this.store.clear();
  }

  stats(): { size: number; keys: string[] } {
    return { size: this.store.size, keys: Array.from(this.store.keys()) };
  }
}
```

```typescript
// src/services/product-service.ts
import { MemoryCache } from '../cache/memory-cache';

const cache = new MemoryCache();

export async function getProduct(id: string) {
  const cached = cache.get(`product:${id}`);
  if (cached) return cached;

  const product = await fetchFromDatabase(id);
  cache.set(`product:${id}`, product);
  return product;
}

async function fetchFromDatabase(id: string): Promise<unknown> {
  const result = await db.query('SELECT * FROM products WHERE id = $1', [id]);
  return result.rows[0] ?? null;
}
```

#### Instruções

Você deve conduzir uma auditoria completa. Para cada problema encontrado:

1. **Classifique o erro** segundo os 5 erros do módulo e o tipo (Lógica/Segurança/Performance/Compatibilidade)
2. **Explique o impacto** em produção
3. **Proponha a correção** com código

Áreas para investigar:
- **Concorrência:** O que acontece se 100 requisições simultâneas pedirem o mesmo produto que não está no cache?
- **Vazamento de memória:** O cache tem limite de tamanho? O que acontece com chaves expiradas?
- **Tratamento de erro:** O que ocorre se `fetchFromDatabase` lançar uma exceção?
- **Atomicidade:** `get` e `set` não são atômicos — há uma condição de corrida?
- **Serialização:** O cache armazena referências de objeto. Isso pode causar mutações inesperadas?
- **Testes:** Como você testaria cada cenário acima?

#### Critérios de sucesso

- [ ] Identificou **mínimo 5 problemas** distintos
- [ ] Cada problema classificado por: erro do módulo + tipo (Lógica/Segurança/Performance/Compatibilidade)
- [ ] Código corrigido com: operação atômica, limite de cache, tratamento de erro, proteção contra raça
- [ ] Sugeriu estratégia de teste para cada cenário crítico
- [ ] Incluiu menção ao **Erro 4 (Ignorar AGENTS.md)** — se o projeto tivesse regras configuradas, parte dos problemas poderia ser evitada

#### Gabarito comentado

| # | Problema | Erro do módulo | Tipo | Impacto |
|---|----------|----------------|------|---------|
| 1 | **Cache stampede** — N requisições simultâneas batem no banco | Erro 5 (tratar como resposta final) | Performance | Queda do banco sob pico de acesso |
| 2 | **Sem limite de tamanho** — cache cresce infinitamente | Erro 1 (confiar cegamente) | Performance | Queda de memória do processo |
| 3 | **Sem tratamento de erro** — exceção no fetch quebra a requisição | Erro 3 (pular code review) | Lógica | Usuário recebe 500 interno |
| 4 | **Condição de corrida** — get/set não atômicos entre requisições | Erro 1 (confiar cegamente) | Lógica | Múltiplas chamadas ao banco para mesma chave |
| 5 | **Referência mutável** — objeto no cache pode ser alterado externamente | Erro 1 (confiar cegamente) | Lógica | Cache corrompido silenciosamente |

**Código corrigido (versão robusta):**

```typescript
// src/cache/memory-cache.ts
interface CacheEntry<T> {
  value: T;
  expiry: number;
}

export class MemoryCache<T = unknown> {
  private store: Map<string, CacheEntry<T>>;
  private defaultTTL: number;
  private maxSize: number;
  private pending: Map<string, Promise<T>>;

  constructor(defaultTTLMs = 60000, maxSize = 1000) {
    this.store = new Map();
    this.defaultTTL = defaultTTLMs;
    this.maxSize = maxSize;
    this.pending = new Map();
  }

  private evictIfNeeded(): void {
    if (this.store.size >= this.maxSize) {
      const oldest = this.store.keys().next().value;
      if (oldest) this.store.delete(oldest);
    }
  }

  async getOrSet(
    key: string,
    fetcher: () => Promise<T>,
    ttlMs?: number
  ): Promise<T> {
    // Proteção contra cache stampede
    const existing = this.get(key);
    if (existing !== null) return existing;

    // Se já há uma busca em andamento, aguarda ela
    const pending = this.pending.get(key);
    if (pending) return pending;

    const promise = fetcher()
      .then((value) => {
        this.set(key, value, ttlMs);
        this.pending.delete(key);
        return value;
      })
      .catch((error) => {
        this.pending.delete(key);
        throw error;
      });

    this.pending.set(key, promise);
    return promise;
  }

  set(key: string, value: T, ttlMs?: number): void {
    const ttl = ttlMs ?? this.defaultTTL;
    this.evictIfNeeded();
    // Armazena clone para evitar mutação externa
    this.store.set(key, {
      value: JSON.parse(JSON.stringify(value)),
      expiry: Date.now() + ttl,
    });
  }

  get(key: string): T | null {
    const entry = this.store.get(key);
    if (!entry) return null;
    if (Date.now() > entry.expiry) {
      this.store.delete(key);
      return null;
    }
    return JSON.parse(JSON.stringify(entry.value)) as T;
  }

  delete(key: string): void {
    this.store.delete(key);
    this.pending.delete(key);
  }

  clear(): void {
    this.store.clear();
    this.pending.clear();
  }

  stats(): { size: number; keys: string[] } {
    return { size: this.store.size, keys: Array.from(this.store.keys()) };
  }
}
```

**Estratégia de testes:**

```typescript
import { describe, it, expect, vi } from 'vitest';

describe('MemoryCache', () => {
  it('getOrSet previne cache stampede', async () => {
    const cache = new MemoryCache<number>(60000, 100);
    const fetcher = vi.fn().mockResolvedValue(42);

    const results = await Promise.all(
      Array(10).fill(null).map(() => cache.getOrSet('key', fetcher))
    );

    expect(fetcher).toHaveBeenCalledTimes(1); // Apenas 1 chamada ao banco
    expect(results).toEqual(Array(10).fill(42));
  });

  it('trata erro do fetcher sem poluir o cache', async () => {
    const cache = new MemoryCache<number>();
    const fetcher = vi.fn().mockRejectedValue(new Error('DB down'));

    await expect(cache.getOrSet('key', fetcher)).rejects.toThrow('DB down');
    expect(cache.get('key')).toBeNull();
  });

  it('evita vazamento de memória', async () => {
    const cache = new MemoryCache<number>(1000, 3);
    await cache.getOrSet('a', () => Promise.resolve(1));
    await cache.getOrSet('b', () => Promise.resolve(2));
    await cache.getOrSet('c', () => Promise.resolve(3));
    await cache.getOrSet('d', () => Promise.resolve(4)); // Deve expulsar 'a'

    expect(cache.stats().size).toBe(3);
    expect(cache.get('a')).toBeNull();
  });

  it('protege contra mutação externa', () => {
    const cache = new MemoryCache<{ count: number }>();
    const obj = { count: 1 };
    cache.set('key', obj);
    obj.count = 999; // Mutação externa

    const cached = cache.get('key');
    expect(cached?.count).toBe(1); // Deve manter o valor original
  });
});
```

**Nota sobre o Erro 4:** Se o projeto tivesse um `AGENTS.md` com regras como "Implementar proteção contra cache stampede" e "Adicionar limite máximo de entradas no cache", a IA teria gerado um código muito mais robusto na primeira tentativa.

---

## 2. Mini-Projeto: Guia de Adoção de IA para o Time

**Nível:** Avançado
**Tempo estimado:** 2–3 horas
**Formato:** Repositório com documentação + código de exemplo

### Cenário

Você é o desenvolvedor sênior de um time de 6 pessoas. Seu CTO leu o módulo "O erro que 90% cometem usando IA para programar" e pediu para você estruturar a adoção de IA no time. Atualmente:

- Cada desenvolvedor usa IA do seu jeito (ChatGPT, Copilot, Claude)
- Não há revisão obrigatória de código gerado por IA
- Não há arquivo de instruções (AGENTS.md) no repositório
- Já ocorreram 2 incidentes em produção causados por código de IA não revisado
- O time quer usar IA, mas não tem um processo definido

### Requisitos

#### 1. Guia de Uso de IA (arquivo `GUIDE.md`)

Deve conter:

- **Política de uso:** quando é apropriado usar IA vs. quando evitar
- **Classificação de tarefas** por risco:
  - **Baixo risco:** boilerplate, testes, documentação, refatoração simples → pode usar IA livremente com revisão leve
  - **Médio risco:** lógica de negócio, consultas ao banco, integrações → IA com revisão obrigatória de outro dev
  - **Alto risco:** autenticação, pagamento, dados sensíveis, infraestrutura → IA apenas para rascunho inicial; implementação manual com revisão em par
- **Fluxo obrigatório** para código gerado por IA (diagrama ou lista passo a passo)
- **Exemplos de prompts aprovados** por categoria (3 exemplos no mínimo)
- **Checklist de revisão** (mínimo 10 itens)
- **Seção de "O que fazer em caso de incidente"** — como rastrear se código de IA causou um bug

#### 2. Arquivo AGENTS.md para o Projeto

Crie um `AGENTS.md` de exemplo com **mínimo 12 regras** que cubra:

- Stack tecnológica (Node + TypeScript + React + PostgreSQL)
- Convenções de código (nomenclatura, imports, componentes)
- Padrões de teste (framework, cobertura mínima)
- Tratamento de erros (Result type vs exceptions)
- Segurança (SQL injection, validação de input, sanitização)
- Performance (cache, lazy loading, bundle size)

#### 3. Fluxo de Revisão em Código

Implemente um script ou workflow (pode ser GitHub Actions, script Node, ou makefile) que:

- Execute antes de todo commit contendo arquivos `.ts`, `.tsx`, `.py` ou `.js`
- Verifique se o autor executou os testes antes do commit (pre-commit hook)
- Adicione um comentário automático em PRs que contenham arquivos modificados por IA solicitando revisão explícita

#### 4. Exemplo de Pull Request Modelo

Crie um template de PR (`.github/PULL_REQUEST_TEMPLATE.md`) que inclua:

- Checklist específico para código gerado por IA
- Campo obrigatório: "Este PR contém código gerado por IA? Sim/Não. Se sim, quais partes?"
- Campo obrigatório: "Os testes foram executados e passaram?"
- Campo obrigatório: "Houve revisão de outro desenvolvedor?"

### Entregáveis esperados

| Entregável | Arquivo | Formato |
|------------|---------|---------|
| Guia de uso de IA | `GUIDE.md` | Markdown |
| Instruções do agente | `AGENTS.md` | Markdown (12+ regras) |
| Script de pré-commit | `.husky/pre-commit` ou `scripts/pre-commit.sh` | Shell / Node |
| Workflow de revisão | `.github/workflows/ai-review.yml` | YAML |
| Template de PR | `.github/PULL_REQUEST_TEMPLATE.md` | Markdown |

### Critérios de avaliação

| Critério | Peso | Descrição |
|----------|------|-----------|
| **Completude** | 25% | Todos os 5 entregáveis estão presentes e funcionais |
| **Aderência ao módulo** | 20% | O guia reflete os 5 erros e as correções do módulo de referência |
| **Clareza** | 15% | A documentação é clara, direta e executável por qualquer dev do time |
| **Aplicabilidade** | 20% | As regras do AGENTS.md e o fluxo de revisão são realistas para um time de 6 pessoas |
| **Qualidade técnica** | 20% | Scripts funcionam, template cobre os cenários, exemplos são corretos |

### Exemplo parcial (GUIDE.md — seção de abertura)

```markdown
# Guia de Uso de IA — Time de Engenharia

## Propósito

Este guia define **como, quando e com quais cuidados** usar assistentes de IA
no nosso fluxo de desenvolvimento. Ele existe para maximizar a produtividade
sem comprometer a qualidade e segurança do código.

## Política de Uso

### ✅ Quando usar IA
- Geração de código boilerplate (schemas, migrações, componentes simples)
- Criação de testes unitários e de integração
- Documentação técnica e comentários
- Refatoração de código existente (com supervisão)
- Geração de queries SQL simples
- Sugestão de nomes de variáveis e tipos

### ❌ Quando EVITAR usar IA
- Lógica crítica de negócio (regras de pricing, cálculos financeiros)
- Código de segurança (autenticação, autorização, criptografia)
- Decisões arquiteturais (qual padrão usar, como estruturar o projeto)
- Código que você não consegue revisar linha por linha
- Em produção sem passar por todos os checks obrigatórios

## Classificação de Risco

| Risco | Exemplos | Fluxo Exigido |
|-------|----------|---------------|
| 🟢 Baixo | Testes, tipos, docs | IA liberada, revisão rápida |
| 🟡 Médio | Lógica de negócio, queries | IA + revisão obrigatória de outro dev |
| 🔴 Alto | Auth, pagamento, dados | Rascunho com IA + implementação manual + pair review |
```

### Exemplo parcial (AGENTS.md)

````markdown
# Agente: Plataforma Principal

## Stack
- Runtime: Node.js 22 LTS
- Linguagem: TypeScript 5.x (strict mode)
- Frontend: React 18 + Next.js 14 (App Router)
- Estilo: Tailwind CSS + shadcn/ui
- Banco: PostgreSQL 16 + Prisma ORM
- Testes: Vitest + Playwright
- CI/CD: GitHub Actions

## Convenções de Código
- Use `function` apenas para top-level; use arrow functions para componentes e callbacks
- Prefira `const` sobre `let` — `let` só é aceitável em loops com contador
- Nomes de arquivo em kebab-case: `user-profile.tsx`, não `userProfile.tsx`
- Componentes de página em `src/app/`, componentes reutilizáveis em `src/components/`
- Tipos e interfaces em `src/types/`, exportados como `export type`
- Imports organizados: 1) pacotes externos, 2) módulos internos, 3) tipos, 4) estilos

## Testes
- Framework: Vitest (nunca Jest)
- Cobertura mínima: 80% em funções de lógica de negócio
- Testes de componente com Testing Library + Playwright para E2E
- Todo PR deve incluir testes para novas funcionalidades

## Tratamento de Erros
- Erros esperados: use discriminated unions / Result pattern (`{ success: true; data: T } | { success: false; error: E }`)
- Erros inesperados: capture em middleware e retorne 500 padronizado
- Nunca use `throw` em controllers — delegue ao error handler
- Logs estruturados com contexto (requestId, userId, operation)

## Segurança
- Toda query ao banco deve usar Prisma (nunca raw queries a menos que inevitável)
- Toda validação de input deve ser feita com Zod no boundary da API
- Senhas: bcrypt com salt rounds 12
- Tokens JWT com expiração máxima de 1h + refresh token rotativo
- Sanitize qualquer saída que contenha input do usuário (XSS prevention)

## Performance
- Cache com padrão getOrSet (proteção contra cache stampede)
- Lazy loading em componentes que não estão no viewport
- Bundle size: warning se exceder 200KB por chunk
- Queries N+1 são proibidas — use `include` ou `select` do Prisma
- Paginação obrigatória em listagens (cursor-based, não offset)
````

---

## 3. Laboratório Guiado: Configure AGENTS.md do Zero e Teste com Prompts Reais

**Nível:** Prático
**Tempo estimado:** 40–60 minutos
**Pré-requisitos:**

- VS Code ou similar instalado
- Acesso a um assistente de IA (Claude Code, OpenCode, GitHub Copilot, ou ChatGPT)
- Node.js 18+ instalado (para o projeto de teste)
- Git instalado
- Conta no GitHub (para testar templates)

### Objetivo

Ao final deste laboratório, você terá um `AGENTS.md` funcional na raiz de um projeto real e terá testado seu impacto com prompts antes e depois da configuração.

---

### Roteiro

#### Passo 1 — Crie um projeto de teste

```bash
mkdir -p ~/lab-agents && cd ~/lab-agents
git init
npm init -y
```

**Verificação:** O diretório existe e tem um `package.json`.

---

#### Passo 2 — Crie uma estrutura mínima de projeto

```bash
mkdir -p src/components src/utils src/types src/pages __tests__
```

**Verificação:** Os diretórios foram criados.

---

#### Passo 3 — Crie um arquivo de código sem contexto

Crie o arquivo `src/utils/helpers.ts`:

```typescript
export function formatDate(date: Date): string {
  return date.toISOString().split('T')[0];
}

export function capitalize(str: string): string {
  return str.charAt(0).toUpperCase() + str.slice(1);
}
```

**Verificação:** O arquivo existe e contém o código acima.

---

#### Passo 4 — Prompt de teste ANTES da configuração

Abra seu assistente de IA e execute o seguinte prompt:

> "Adicione validação e testes para essas funções"

Cole o código do `helpers.ts`.

**Verificação:** Anote a saída. Observe: a IA provavelmente perguntou qual framework de teste, qual estilo de validação, se deve usar `throw` ou `Result`, etc.

---

#### Passo 5 — Crie o AGENTS.md

Crie o arquivo `AGENTS.md` na raiz do projeto:

```markdown
# Agente: Laboratório de Teste

## Stack
- Runtime: Node.js 22
- Linguagem: TypeScript 5.x (strict mode)
- Testes: Vitest
- Formatação: Prettier

## Regras de Código
- Prefira `const` sobre `let`
- Funções puras sempre que possível
- Erros devem ser retornados como `Result<T, E>`, nunca `throw`
- Nomes em camelCase para variáveis e funções

## Regras de Teste
- Testes em `__tests__/` com sufixo `.test.ts`
- Use `describe` + `it` (não `test`)
- Cobertura mínima: 100% das funções exportadas

## Formato da Resposta
- Código em TypeScript estrito
- Com testes em Vitest
- Sem dependências externas além das já listadas
```

**Verificação:** O arquivo existe e contém pelo menos 12 linhas.

---

#### Passo 6 — Crie um teste base para referência

Crie `__tests__/helpers.test.ts`:

```typescript
import { describe, it, expect } from 'vitest';
import { formatDate, capitalize } from '../src/utils/helpers';

describe('formatDate', () => {
  it('formata data no formato YYYY-MM-DD', () => {
    expect(formatDate(new Date('2025-06-15'))).toBe('2025-06-15');
  });
});

describe('capitalize', () => {
  it('capitaliza primeira letra', () => {
    expect(capitalize('hello')).toBe('Hello');
  });
});
```

**Verificação:** O arquivo de teste existe.

---

#### Passo 7 — Prompt de teste DEPOIS da configuração

No mesmo assistente de IA, execute novamente:

> "Adicione validação e testes para essas funções"

Cole o código do `helpers.ts` **e também** o conteúdo do `AGENTS.md`.

**Verificação:** Compare a resposta agora com a do Passo 4. A resposta deve ser mais específica: usar Vitest (não Jest), usar `describe`/`it`, adicionar validação com Result type, etc.

---

#### Passo 8 — Documente a diferença

Crie um arquivo `COMPARISON.md` com suas observações:

```markdown
# Comparação: Antes vs Depois do AGENTS.md

## Prompt usado
"Adicione validação e testes para essas funções"

## Antes (sem AGENTS.md)
- A IA perguntou qual framework de teste usar
- Sugeriu `throw` para erros
- Usou `test()` em vez de `describe`/`it`

## Depois (com AGENTS.md)
- Usou Vitest automaticamente
- Retornou Result type em vez de throw
- Seguiu as convenções de nomenclatura

## Conclusão
[Escreva aqui sua reflexão]
```

**Verificação:** O arquivo foi criado com suas anotações.

---

#### Passo 9 — Teste com um prompt complexo

Execute este prompt no assistente (com o AGENTS.md no contexto):

> "Crie um hook React `useLocalStorage` que persista estado no localStorage com suporte a serialização JSON e tratamento de erros. Deve ter os mesmos padrões de validação e teste do projeto."

**Verificação:** A IA deve criar o hook seguindo as regras do AGENTS.md (Result type, Vitest, camelCase, etc.).

---

#### Passo 10 — Revise o código gerado

Analise o código gerado e preencha a tabela:

| Critério | Atende? | Observação |
|----------|---------|------------|
| Usa Result type em vez de throw | ✅ / ❌ | |
| Testes em `__tests__/` com `.test.ts` | ✅ / ❌ | |
| Usa `describe` + `it` | ✅ / ❌ | |
| camelCase para variáveis | ✅ / ❌ | |
| Sem dependências externas não listadas | ✅ / ❌ | |

**Verificação:** Todos os critérios devem ser atendidos. Se algum falhar, refine o AGENTS.md.

---

#### Passo 11 — Refine o AGENTS.md com feedback

Com base na revisão do Passo 10, adicione regras faltantes ao `AGENTS.md`. Por exemplo, se a IA usou `any`, adicione:

```markdown
- Evite `any` — use `unknown` com type narrowing
```

**Verificação:** O AGENTS.md foi atualizado.

---

#### Passo 12 — Teste de regressão (ciclo completo)

Repita o prompt do Passo 9 com o AGENTS.md atualizado e verifique se as correções foram aplicadas.

**Verificação:** O novo código gerado atende agora a todos os critérios da tabela.

---

#### Passo 13 — Teste de consistência entre sessões

Feche e abra uma nova sessão do assistente. Repita o mesmo prompt do Passo 9 com o mesmo AGENTS.md.

**Verificação:** A resposta deve ser consistente com a do Passo 12, demonstrando que o AGENTS.md garante reprodutibilidade.

---

#### Passo 14 — Configure o template de PR

Crie a estrutura de template:

```bash
mkdir -p .github
```

Crie `.github/PULL_REQUEST_TEMPLATE.md`:

```markdown
## Descrição

[Descreva o que este PR faz]

## Código gerado por IA?

- [ ] Sim
- [ ] Não

Se sim, quais partes? _________________

## Testes

- [ ] Testes unitários foram escritos/atualizados
- [ ] Testes passam localmente (`npm test`)
- [ ] Cobertura mínima de 80% foi mantida

## Revisão

- [ ] Outro desenvolvedor revisou o código
- [ ] O código segue as regras do `AGENTS.md`
```

**Verificação:** O arquivo existe.

---

#### Passo 15 — Reflexão final

Adicione ao `COMPARISON.md` suas conclusões finais respondendo:

1. Quantas regras seu AGENTS.md tem agora?
2. Qual foi a maior melhoria que o AGENTS.md trouxe nas respostas da IA?
3. Quanto tempo você acha que esse arquivo economizará por semana?
4. Você identificou algum dos 5 erros do módulo nas respostas da IA **antes** da configuração?

**Verificação:** O arquivo `COMPARISON.md` está completo com as 4 respostas.

---

### Checklist final do laboratório

| Passo | Atividade | Status |
|-------|-----------|--------|
| 1 | Projeto criado com `git init` | ☐ |
| 2 | Estrutura de diretórios criada | ☐ |
| 3 | Arquivo `helpers.ts` criado | ☐ |
| 4 | Prompt ANTES da configuração executado | ☐ |
| 5 | `AGENTS.md` criado | ☐ |
| 6 | Teste base criado | ☐ |
| 7 | Prompt DEPOIS da configuração executado | ☐ |
| 8 | `COMPARISON.md` com observações iniciais | ☐ |
| 9 | Prompt complexo executado | ☐ |
| 10 | Tabela de revisão preenchida | ☐ |
| 11 | AGENTS.md refinado | ☐ |
| 12 | Teste de regressão concluído | ☐ |
| 13 | Teste de consistência entre sessões | ☐ |
| 14 | Template de PR criado | ☐ |
| 15 | Reflexão final documentada | ☐ |

### Para ir além

- Faça o mesmo experimento com outras linguagens (Python + pytest, Java + JUnit)
- Teste o AGENTS.md em diferentes assistentes (Claude Code vs ChatGPT vs Copilot) e documente as diferenças
- Crie um script que valide automaticamente se o AGENTS.md está presente no repositório e exibe um warning se não estiver
- Leia o guia oficial do OpenCode sobre AGENTS.md em https://opencode.ai

---

> **Referência:** Este exercício complementa o módulo "O erro que 90% das pessoas cometem usando IA para programar" (`content/modules/001-erro-90-por-cento-ia-programar.md`).
