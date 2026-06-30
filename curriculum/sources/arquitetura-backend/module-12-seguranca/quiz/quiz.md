# Quiz — Módulo 12

## Pergunta 1

Qual vulnerabilidade OWASP ocorre quando um usuário pode acessar recursos que não lhe pertencem?

- a) Injection
- b) Broken Access Control
- c) Cryptographic Failure
- d) XSS

**Resposta:** b

---

## Pergunta 2

Qual o algoritmo correto para armazenar senhas?

- a) MD5
- b) SHA1
- c) bcrypt com salt rounds 12
- d) Base64

**Resposta:** c

---

## Pergunta 3

Qual a expiração recomendada para um Access Token JWT?

- a) 7 dias
- b) 30 dias
- c) 15 minutos
- d) 1 ano

**Resposta:** c

---

## Pergunta 4

O que o rate limiting previne?

- a) SQL injection
- b) XSS
- c) Brute force e DDoS
- d) CSRF

**Resposta:** c

---

## Pergunta 5

Como prevenir SQL injection no Prisma?

- a) Usar query builder (findUnique, findMany) em vez de raw queries
- b) Escapar aspas manualmente
- c) Usar JavaScript puro
- d) Não tem como prevenir

**Resposta:** a

---

## Pergunta 6

Qual header de segurança impede que o site seja carregado em um iframe?

- a) Content-Security-Policy
- b) X-Frame-Options: DENY
- c) X-Content-Type-Options
- d) Strict-Transport-Security

**Resposta:** b

---

## Pergunta 7

O que é CSRF?

- a) Um ataque de injeção de SQL
- b) Um ataque onde um site malicioso executa ações em nome do usuário autenticado
- c) Um ataque de força bruta
- d) Um tipo de malware

**Resposta:** b

---

## Pergunta 8

Qual a forma correta de gerenciar secrets em uma aplicação?

- a) Hardcoded no código
- b) No .env commitado
- c) Via variáveis de ambiente + .env.example sem valores reais
- d) Em um arquivo de texto na raiz

**Resposta:** c

---

## Pergunta 9

O que o Helmet faz em uma aplicação NestJS?

- a) Criptografa o banco de dados
- b) Configura headers de segurança automaticamente
- c) Gerencia autenticação JWT
- d) Faz rate limiting

**Resposta:** b

---

## Pergunta 10

Qual a melhor prática para refresh tokens?

- a) Refresh token com expiração de 1 ano
- b) Refresh token sem expiração
- c) Rotação de refresh token (revogar antigo ao usar)
- d) Não usar refresh token

**Resposta:** c
