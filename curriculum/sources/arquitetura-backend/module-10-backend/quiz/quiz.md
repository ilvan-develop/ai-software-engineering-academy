# Quiz — Módulo 10

## Pergunta 1

Qual a principal vantagem do NestJS sobre Express para aplicações Enterprise?

- a) É mais rápido
- b) Tem DI nativa, módulos, guards e interceptors
- c) É mais leve
- d) Não precisa de TypeScript

**Resposta:** b

---

## Pergunta 2

Qual a responsabilidade de um Service no NestJS?

- a) Definir rotas HTTP
- b) Conter lógica de negócio e orquestração
- c) Acessar o banco de dados diretamente
- d) Validar entrada do usuário

**Resposta:** b

---

## Pergunta 3

O que um Exception Filter faz?

- a) Filtra requisições por IP
- b) Trata erros globalmente e padroniza respostas
- c) Valida dados de entrada
- d) Transforma respostas

**Resposta:** b

---

## Pergunta 4

Qual a diferença entre validação e sanitização?

- a) São a mesma coisa
- b) Validação rejeita dados inválidos; sanitização transforma dados
- c) Sanitização rejeita; validação transforma
- d) Nenhuma das anteriores

**Resposta:** b

---

## Pergunta 5

Qual tipo de paginação é recomendado para grandes datasets?

- a) Offset-based (page/limit)
- b) Cursor-based
- c) Limit-based
- d) Nenhum

**Resposta:** b

---

## Pergunta 6

O que o decorator `@UseGuards(JwtAuthGuard)` faz?

- a) Documenta a rota no Swagger
- b) Protege a rota exigindo autenticação JWT
- c) Valida o body da requisição
- d) Transforma a resposta

**Resposta:** b

---

## Pergunta 7

Qual o propósito de um Interceptor?

- a) Proteger rotas
- b) Validar dados
- c) Transformar requisições/respostas e adicionar lógica transversal
- d) Gerenciar banco de dados

**Resposta:** c

---

## Pergunta 8

O que é um Domain Error?

- a) Um erro HTTP 500
- b) Um erro específico do domínio de negócio com código próprio
- c) Um erro de validação de schema
- d) Um erro de banco de dados

**Resposta:** b

---

## Pergunta 9

O que um Health Check faz?

- a) Verifica se o servidor está rodando
- b) Verifica a saúde de dependências (banco, redis, etc.)
- c) Autentica o usuário
- d) Testa a performance da API

**Resposta:** b

---

## Pergunta 10

Para que serve o padrão Repository?

- a) Abstrair a lógica de persistência do domínio
- b) Criar rotas REST
- c) Validar dados de entrada
- d) Gerenciar cache

**Resposta:** a
