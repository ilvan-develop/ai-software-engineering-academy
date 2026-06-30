# Quiz — Módulo 09

## Pergunta 1

Qual a consequência mais grave de uma modelagem de dados ruim?

- a) Código mais feio
- b) Erros mais caros de corrigir (fundação do sistema)
- c) Mais linhas de código
- d) Menos testes

**Resposta:** b

---

## Pergunta 2

Qual decorator Prisma define uma relação 1:1?

- a) @relation
- b) @unique + @relation
- c) @@id
- d) @@index

**Resposta:** b

---

## Pergunta 3

O que é soft delete?

- a) Excluir dados sem confirmação
- b) Marcar registro como deletado (deletedAt) sem remover fisicamente
- c) Deletar dados após um tempo
- d) Deletar apenas dados não usados

**Resposta:** b

---

## Pergunta 4

Qual o problema N+1?

- a) Uma query que retorna N+1 registros
- b) Fazer N queries adicionais dentro de um loop
- c) Um tipo de índice
- d) Uma migration com erro

**Resposta:** b

---

## Pergunta 5

O que a estratégia expand-migrate-contract resolve?

- a) Backup de dados
- b) Migrações sem downtime
- c) Índices lentos
- d) Soft delete

**Resposta:** b

---

## Pergunta 6

Qual campo deve ter índice obrigatoriamente?

- a) Boolean
- b) Foreign key
- c) Text longo
- d) JSON

**Resposta:** b

---

## Pergunta 7

Qual o formato ideal de backup para point-in-time recovery?

- a) Full apenas
- b) Full + WAL (Write-Ahead Log)
- c) Incremental apenas
- d) Cópia manual dos arquivos

**Resposta:** b

---

## Pergunta 8

O que o `@@index([userId, status])` faz?

- a) Cria dois índices separados
- b) Cria um índice composto para queries que filtram por userId e status
- c) Cria um índice apenas para status
- d) Cria uma constraint unique

**Resposta:** b

---

## Pergunta 9

Como prevenir N+1 no Prisma?

- a) Usar findMany
- b) Usar include para eager loading
- c) Usar deleteMany
- d) Usar raw queries

**Resposta:** b

---

## Pergunta 10

O que deve ser registrado em um audit trail?

- a) Apenas operações de delete
- b) Entidade, ID, ação, mudanças (before/after), usuário, timestamp
- c) Apenas login dos usuários
- d) Apenas erros do sistema

**Resposta:** b
