==================================================
LINKEDIN — Artigo
==================================================

Titulo: Módulo 13 - Multi-Tenant: Conceitos e Estratégias de Isolamento: O Que Todo Arquiteto Deveria Saber


## 1. O que é Multi-Tenancy?

- Multi-tenancy é um padrão arquitetural onde **uma única instância de software atende múltiplos clientes (tenants)**, mantendo os dados de cada um logicamente isolados e invisíveis entre si.
- ┌──────────────────────────────────────────────────────┐
- │                    SISTEMA (1 instância)               │

## 2. Abordagens de Isolamento

- Existem três estratégias principais para isolar dados entre tenants.
- Cada tenant tem **seu próprio banco de dados**. O roteador de conexão decide qual banco usar com base no tenant identificado.
- ┌──────────────────────────────────────────────┐

## 3. Análise Aprofundada por Dimensão

- Database per Tenant:** Um vazamento de dados de um tenant não afeta os outros. Se um cliente exige compliance específico (LGPD, HIPAA, SOC2), pode-se isolar completamente em nível físico. Ataques de SQL injection ficam contidos no banco do tenant.
- Schema per Tenant:** Um invasor que ganha acesso ao banco pode potencialmente acessar múltiplos schemas. A segurança depende das permissões do usuário do banco (`GRANT USAGE ON SCHEMA`). Idealmente, o usuário da aplicação tem acesso apenas ao schema do tenant atual.
- Shared Database:** Um SQL injection ou bug no `WHERE` expõe **todos os dados de todos os tenants**. Requer:


---

🔥 Gostou? Compartilhe e marque alguem que precisa ler isso.

#ArquiteturaDeSoftware #EngenhariaDeSoftware #CarreiraDev
