# Exercícios — Módulo 09

## Exercício 1: Identificando o erro (fácil)

Leia cada cenário e identifique **qual dos 5 erros** está sendo cometido:

**a)** Um dev pede "Faz aí uma API de login" e recebe um código que funciona, mas usa MongoDB quando o projeto usa PostgreSQL.

**b)** Um código gerado por IA para validação de CPF é copiado para produção sem ninguém ler. Só aceita números e ignora formatação.

**c)** Um desenvolvedor pergunta "Como faço um botão?" e recebe um exemplo genérico em Bootstrap. O projeto usa Tailwind.

**d)** O time não tem arquivo de instruções para o agente. Cada interação gera código com estilos diferentes: às vezes classes, às vezes functions.

**e)** Na primeira tentativa, a IA gera uma função de hash com MD5. O dev aceita e segue em frente. Mais tarde descobre que MD5 é inseguro.

---

## Exercício 2: Reescrevendo prompts ruins (médio)

Abai xo há prompts usados por um desenvolvedor. Reescreva cada um seguindo a estrutura **Contexto + Intenção + Formato Esperado**:

**a)** "Conserta esse código"

**b)** "Faz um teste pra mim"

**c)** "Otimiza a query"

**d)** "Explica isso aqui"

---

## Exercício 3: Auditando código de IA (difícil)

Analise o código abaixo, gerado por IA. Identifique **todos os erros** (mínimo 4):

```javascript
// Gerado por IA — supostamente uma função de upload
const multer = require('multer');
const path = require('path');

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, '/uploads');
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname);
  }
});

const upload = multer({ storage });

app.post('/upload', upload.single('file'), (req, res) => {
  res.json({ message: 'Arquivo enviado com sucesso!' });
});
```text

**O que verificar:**
- Erro 1: confiar cegamente? Há problemas de segurança?
- Erro 2: o prompt que gerou isso foi vago?
- Erro 3: testes e validação?
- Erro 5: primeira resposta sem refinamento?

---

## Exercício 4: Criando um AGENTS.md (médio)

Crie um arquivo `AGENTS.md` para um projeto com as seguintes características:

- **Stack:** Next.js 14, TypeScript, Prisma ORM, PostgreSQL
- **Testes:** Vitest + Playwright
- **Estilo:** Componentes em `src/components/`, páginas em `src/app/`, lib em `src/lib/`
- **Convenções:** arrow functions, `const`, nomes em kebab-case, CSS Modules
- **Banco:** Prisma com `schema.prisma` em `prisma/`

Inclua pelo menos 8 regras claras e acionáveis.
