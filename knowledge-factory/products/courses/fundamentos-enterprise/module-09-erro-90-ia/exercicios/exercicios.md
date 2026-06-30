# Exercícios — Módulo 09 — O Erro de 90% ao Usar IA para Programar

---

## Exercício 1 — Fácil: Identificação dos 5 Erros

**Contexto:** Você estudou os 5 erros mais comuns ao usar IA para programar. Agora precisa identificá-los em situações do dia a dia.

**Instruções:** Leia cada cenário e identifique qual dos 5 erros está sendo cometido:

**a)** Um desenvolvedor pede "Faz uma API de login para mim". A IA gera código com MongoDB, mas o projeto usa PostgreSQL. O dev só descobre o erro ao tentar rodar.

**b)** Um código gerado por IA para validação de CPF é copiado diretamente para produção sem revisão. Só aceita números de 11 dígitos, ignorando formatação e dígitos verificadores.

**c)** Um desenvolvedor pergunta "Como criar um dropdown?" e recebe resposta genérica em HTML puro. O projeto usa React com Chakra UI.

**d)** O time nunca criou um arquivo de instruções para o agente. Cada interação gera código em estilos diferentes: ora classes, ora funções, ora componentes de classe.

**e)** Na primeira tentativa, a IA sugere usar `localStorage` para armazenar tokens JWT. O dev aceita a sugestão e implementa sem questionar segurança.

---

## Exercício 2 — Médio: Transformando Prompts

**Contexto:** Prompts vagos geram respostas genéricas. Reescreva cada prompt seguindo o formato **Contexto + Intenção + Formato Esperado**.

**a)** "Faz aí uma função de validação"

**b)** "Otimiza esse código"

**c)** "Faz um teste unitário"

**d)** "Explica essa query"

---

## Exercício 3 — Difícil: Auditoria de Código

**Contexto:** Você recebeu este código 100% gerado por IA. Identifique no mínimo 4 problemas graves.

```javascript
const express = require('express');
const app = express();

// Rota de login gerada por IA
app.post('/login', (req, res) => {
  const { username, password } = req.body;
  const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;
  db.query(query, (err, results) => {
    if (results.length > 0) {
      res.json({ token: '123456' });
    } else {
      res.status(401).json({ error: 'Invalid credentials' });
    }
  });
});

app.listen(3000);
```

---

## Exercício 4 — Médio: Criando AGENTS.md

**Contextão:** Crie um arquivo `AGENTS.md` para um projeto com:

- **Stack:** Next.js 14, TypeScript, Prisma ORM, PostgreSQL
- **Testes:** Vitest + Playwright
- **Estrutura:** `src/components/`, `src/app/`, `src/lib/`
- **Estilo:** arrow functions, `const`, kebab-case, CSS Modules
- **Banco:** Prisma schema em `prisma/schema.prisma`
