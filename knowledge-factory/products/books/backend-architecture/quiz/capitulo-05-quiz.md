# Quiz — Capítulo 5: Multi-Tenant — Conceitos e Estratégias

**Instruções:** 5 perguntas de múltipla escolha. Apenas uma alternativa correta.

---

## Pergunta 1 (Fácil)

O que é Multi-Tenancy?

- [ ] A) Várias instâncias do software, uma para cada cliente
- [ ] B) **Uma única instância de software atendendo múltiplos clientes com dados isolados**
- [ ] C) Um banco de dados por funcionalidade do sistema
- [ ] D) Múltiplas APIs para um mesmo cliente

**Resposta:** B

---

## Pergunta 2 (Fácil)

Qual estratégia de isolamento oferece o MAIOR nível de isolamento de dados?

- [ ] A) **Banco por Tenant**
- [ ] B) Schema por Tenant
- [ ] C) Coluna Discriminadora
- [ ] D) Todas oferecem o mesmo nível

**Resposta:** A

---

## Pergunta 3 (Médio)

Qual a principal desvantagem da estratégia "Banco por Tenant"?

- [ ] A) Baixo isolamento de dados
- [ ] B) **Custo elevado e complexidade operacional**
- [ ] C) Impossibilidade de customizações por tenant
- [ ] D) Quedas de performance em todas as queries

**Resposta:** B

---

## Pergunta 4 (Médio)

Na estratégia de Coluna Discriminadora, como os dados são separados?

- [ ] A) Cada tenant tem seu próprio banco de dados
- [ ] B) Cada tenant tem seu próprio schema no banco
- [ ] C) **Uma coluna `tenantId` em cada tabela identifica a qual tenant o registro pertence**
- [ ] D) Os dados são separados por prefixo no nome da tabela

**Resposta:** C

---

## Pergunta 5 (Difícil)

Por que queries cross-tenant (consultar dados de múltiplos tenants) são mais fáceis na estratégia de Coluna Discriminadora?

- [ ] A) Porque cada tenant tem seu próprio índice
- [ ] B) **Porque todos os dados estão nas mesmas tabelas, bastando filtrar por tenantId**
- [ ] C) Porque não há necessidade de índices
- [ ] D) Porque os dados são duplicados entre tenants

**Resposta:** B
