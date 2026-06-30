# Quiz — Módulo 13: Multi-Tenant

## Pergunta 1

O que é multi-tenancy?

- a) Múltiplos servidores rodando a mesma aplicação para um único cliente
- b) Uma única instância de software atendendo múltiplos clientes com dados isolados
- c) Um banco de dados separado para cada funcionalidade do sistema
- d) Várias versões diferentes do mesmo software para clientes diferentes

**Resposta:** b

---

## Pergunta 2

Qual abordagem de isolamento oferece o MAIOR nível de segurança entre tenants?

- a) Shared database com coluna tenant_id
- b) Schema per tenant no mesmo banco
- c) Database per tenant
- d) Tabelas separadas no mesmo schema com prefixo do tenant

**Resposta:** c

---

## Pergunta 3

Qual a principal desvantagem do Shared Database (discriminador) com coluna tenant_id?

- a) Alto custo de infraestrutura e licenciamento
- b) Complexidade de backup e restore
- c) Risco de vazamento de dados entre tenants se o WHERE tenant_id for esquecido em uma query
- d) Dificuldade de criar índices no banco

**Resposta:** c

---

## Pergunta 4

Qual estratégia de identificação de tenant é considerada mais segura por ser auto-contida, criptografada e validável sem consulta externa?

- a) Subdomínio (tenant.app.com)
- b) Header HTTP (X-Tenant-Id)
- c) Path na URL (/api/tenant/users)
- d) JWT claim (payload.tid)

**Resposta:** d

---

## Pergunta 5

Qual API do Node.js é usada para manter o contexto do tenant durante toda a requisição, evitando ter que passar o tenantId como parâmetro em cada função?

- a) process.nextTick
- b) AsyncLocalStorage (async_hooks)
- c) setImmediate
- d) EventEmitter

**Resposta:** b

---

## Pergunta 6

Em um schema per tenant, como as migrations de banco de dados devem ser aplicadas?

- a) Uma vez no schema público, e todos os tenants acessam por herança
- b) Em cada schema de cada tenant ativo
- c) Apenas no banco de dados mestre, que replica para os schemas
- d) Automaticamente pelo ORM sem configuração manual

**Resposta:** b

---

## Pergunta 7

Qual tipo de tabela deve ser COMPARTILHADA entre todos os tenants (global)?

- a) Tabela de usuários do sistema
- b) Tabela de pedidos e faturas
- c) Tabela de planos, preços e feature flags
- d) Tabela de produtos e catálogo

**Resposta:** c

---

## Pergunta 8

Em um shared database, como deve ser estruturado o índice para queries multi-tenant eficientes?

- a) Apenas na coluna id (PK)
- b) Apenas na coluna email (para login)
- c) Índice composto começando com tenant_id (ex: idx_users_tenant_email)
- d) Índice FULLTEXT para busca textual

**Resposta:** c

---

## Pergunta 9

Qual a melhor estratégia de backup para um tenant Enterprise que exige RTO (Recovery Time Objective) de 15 minutos?

- a) Backup diário compartilhado com todos os tenants
- b) Backup semanal com retention de 30 dias
- c) Backup dedicado com Point-in-Time Recovery (PITR) e réplica
- d) Apenas replicação síncrona entre regiões

**Resposta:** c

---

## Pergunta 10

O que NÃO pode faltar em um teste de isolamento entre tenants?

- a) Testar que o login funciona para todos os tenants
- b) Verificar que dados criados pelo Tenant A não são visíveis pelo Tenant B
- c) Testar a interface de usuário responsiva
- d) Verificar o tempo de resposta médio das requisições

**Resposta:** b

---

## Pergunta 11

No NestJS, qual decorator é usado para aplicar um guard de feature flag em um endpoint?

- a) @UsePipes
- b) @UseInterceptors
- c) @UseGuards
- d) @UseFilters

**Resposta:** c

---

## Pergunta 12

Em um cenário de schema per tenant, qual comando PostgreSQL cria o namespace para um novo tenant chamado "acme"?

- a) CREATE DATABASE tenant_acme;
- b) CREATE SCHEMA IF NOT EXISTS tenant_acme;
- c) CREATE TABLE tenant_acme;
- d) CREATE TENANT acme;

**Resposta:** b
