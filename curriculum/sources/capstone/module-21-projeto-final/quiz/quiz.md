# Quiz — Módulo 21

## Pergunta 1

Qual abordagem arquitetural o ADR-001 recomenda para o projeto final e por quê?

- a) Microservices — porque escala melhor
- b) Modular Monolith — porque o time é pequeno e deploy é simples
- c) Serverless — porque não precisa gerenciar infraestrutura
- d) Event Sourcing — porque garante auditoria completa

**Resposta:** b

---

## Pergunta 2

Qual estratégia de multi-tenancy é recomendada no ADR-002?

- a) Database por tenant — isolamento máximo
- b) Schema por tenant — migrations separadas
- c) Discriminator column (tenant_id) + RLS — equilíbrio entre custo e isolamento
- d) Arquivo JSON por tenant — sem banco relacional

**Resposta:** c

---

## Pergunta 3

Qual o papel do Redis no projeto? (Selecione a opção mais completa)

- a) Apenas cache de queries
- b) Cache, sessões, filas de jobs, rate limiting
- c) Apenas filas de jobs assíncronos
- d) Banco de dados principal

**Resposta:** b

---

## Pergunta 4

Um usuário com papel Developer tentou criar um novo projeto via API. Qual deve ser o response HTTP?

- a) 200 OK — Developer pode criar projetos
- b) 403 Forbidden — Developer não tem permissão project:create
- c) 401 Unauthorized — precisa fazer login novamente
- d) 400 Bad Request — Developer não pode criar projetos

**Resposta:** b

---

## Pergunta 5

Qual a diferença entre os endpoints `/health` e `/ready`?

- a) São a mesma coisa
- b) `/health` verifica se o servidor está vivo; `/ready` verifica se dependências (banco, Redis) estão prontas
- c) `/health` verifica dependências; `/ready` verifica vida do servidor
- d) `/health` é público; `/ready` é autenticado

**Resposta:** b

---

## Pergunta 6

Qual o limite de tentativas de login antes do bloqueio temporário?

- a) 3 tentativas
- b) 5 tentativas
- c) 10 tentativas
- d) Ilimitado (bloqueio apenas por IP)

**Resposta:** b

---

## Pergunta 7

O que acontece quando o webhook do Stripe recebe `checkout.session.completed`?

- a) O sistema envia um e-mail de boas-vindas
- b) O sistema ativa a subscription do tenant e libera os limites do plano
- c) O sistema cria um novo tenant automaticamente
- d) O sistema gera uma nota fiscal

**Resposta:** b

---

## Pergunta 8

Qual o requisito mínimo de cobertura de testes para aprovação?

- a) 50% unitários, 30% integração
- b) 80% unitários, 60% integração
- c) 90% unitários, 80% integração
- d) 100% de cobertura em tudo

**Resposta:** b

---

## Pergunta 9

Durante a demo ao vivo, qual fluxo NÃO é obrigatório?

- a) Registrar novo tenant
- b) Criar tarefas e mover no Kanban
- c) Mostrar integração com GitHub
- d) Visualizar dashboard com gráficos

**Resposta:** c

---

## Pergunta 10

Qual situação causa reprovação automática no projeto final?

- a) Cobertura de testes abaixo de 60%
- b) Nota geral abaixo de 70%
- c) Dados vazando entre tenants (falha no isolamento multi-tenant)
- d) README incompleto

**Resposta:** c
