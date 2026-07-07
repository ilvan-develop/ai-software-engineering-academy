# Quiz — Capítulo 7: Multi-Tenant — Migrations, Dados e Seed

**Instruções:** 5 perguntas de múltipla escolha. Apenas uma alternativa correta.

---

## Pergunta 1 (Fácil)

O que é um "seed" no contexto de bancos de dados?

- [ ] A) Uma migration que altera a estrutura do banco
- [ ] B) **Dados iniciais populados no banco para teste ou desenvolvimento**
- [ ] C) Um backup do banco de dados
- [ ] D) Uma query de limpeza de dados

**Resposta:** B

---

## Pergunta 2 (Fácil)

No Prisma, qual comando executa as migrations pendentes?

- [ ] A) `prisma generate`
- [ ] B) `prisma studio`
- [ ] C) **`prisma migrate deploy`**
- [ ] D) `prisma db push`

**Resposta:** C

---

## Pergunta 3 (Médio)

Por que migrations multi-tenant exigem cuidado extra?

- [ ] A) Porque Prisma não suporta migrations em schema multi-tenant
- [ ] B) **Porque a migração precisa ser aplicada a todos os schemas/banco de cada tenant sem quebrar dados existentes**
- [ ] C) Porque cada tenant tem um schema diferente
- [ ] D) Porque migrations não funcionam com coluna tenantId

**Resposta:** B

---

## Pergunta 4 (Médio)

Qual a melhor forma de popular dados iniciais para um novo tenant?

- [ ] A) Pedir para o usuário digitar tudo manualmente
- [ ] B) **Usar um script de seed parametrizado por tenantId**
- [ ] C) Copiar dados de outro tenant existente
- [ ] D) Deixar o banco vazio e criar dados sob demanda

**Resposta:** B

---

## Pergunta 5 (Difícil)

Em uma migração de dados entre tenants (ex: dividindo um tenant em três), qual a estratégia mais segura?

- [ ] A) Migrar tudo em uma única transação
- [ ] B) **Fazer a migração em etapas com validação, cutover e rollback planejado**
- [ ] C) Exportar tudo para CSV, importar nos novos tenants
- [ ] D) Desligar o sistema, migrar, religar

**Resposta:** B
