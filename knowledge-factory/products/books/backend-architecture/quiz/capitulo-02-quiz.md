# Quiz — Capítulo 2: Modelagem de Sistemas

**Instruções:** 5 perguntas de múltipla escolha. Apenas uma alternativa correta.

---

## Pergunta 1 (Fácil)

Qual atributo do Prisma é usado para criar um campo que é preenchido automaticamente com a data/hora da criação?

- [ ] A) `@updatedAt`
- [ ] B) `@default(cuid())`
- [ ] C) **`@default(now())`**
- [ ] D) `@map(created_at)`

**Resposta:** C

---

## Pergunta 2 (Fácil)

Para criar uma relação 1:N no Prisma, qual configuração é necessária?

- [ ] A) Apenas decorar o campo com `@relation`
- [ ] B) **Um campo com `@relation` que referencie um campo da tabela relacionada**
- [ ] C) Usar `@@unique` na chave estrangeira
- [ ] D) Criar uma tabela intermediária sempre

**Resposta:** B

---

## Pergunta 3 (Médio)

Qual é o propósito de um índice composto no banco de dados?

- [ ] A) Garantir unicidade de uma coluna
- [ ] B) **Otimizar queries que filtram por múltiplas colunas simultaneamente**
- [ ] C) Criar uma chave estrangeira automática
- [ ] D) Acelerar operações de INSERT

**Resposta:** B

---

## Pergunta 4 (Médio)

No Prisma, como se define soft delete em um modelo?

- [ ] A) Usando `@deletedAt` automático
- [ ] B) **Adicionando um campo `deletedAt: DateTime?` e filtrando manualmente**
- [ ] C) Usando o atributo `@softDelete`
- [ ] D) Criando uma migration que marca registros como deletados

**Resposta:** B

---

## Pergunta 5 (Difícil)

Por que a ordem das colunas em um índice composto importa?

- [ ] A) Não importa, o banco otimiza automaticamente
- [ ] B) **O índice só é eficiente se a primeira coluna do índice for usada na query**
- [ ] C) Colunas mais seletivas devem vir por último
- [ ] D) A ordem alfabética é a mais performática

**Resposta:** B
