# Exercícios — Módulo 01

## Exercício 1: Classificação Enterprise

Classifique cada cenário como **Enterprise** ou **Consumo** e justifique.

| # | Cenário | Classificação | Justificativa |
|---|---------|---------------|---------------|
| 1 | App de lista de tarefas pessoal | | |
| 2 | Sistema de RH com 500 funcionários | | |
| 3 | Dashboard de vendas com dados reais da empresa | | |
| 4 | Jogo mobile single-player | | |
| 5 | Portal do cliente com login, contratos e boletos | | |
| 6 | Editor de texto offline | | |

---

## Exercício 2: Estratégia de escalabilidade

Você tem um sistema que começou com 100 usuários e agora precisa atender 100.000.

Para cada componente, descreva como escalar:

| Componente | Situação atual | Estratégia de escala |
|------------|---------------|---------------------|
| Banco de dados | 1 instância PostgreSQL | |
| Session do usuário | In-memory no servidor | |
| Upload de imagens | Salvas no disco do servidor | |
| API | 1 servidor Node.js | |
| Cache | Nenhum | |
| Logs | console.log | |

---

## Exercício 3: Criando regras de governança

Crie 5 regras de governança para cada pilar:

**Código**
1. ...
2. ...
3. ...
4. ...
5. ...

**Processo**
1. ...
2. ...
3. ...
4. ...
5. ...

**Dados**
1. ...
2. ...
3. ...
4. ...
5. ...

---

## Exercício 4: Análise de compliance

Um sistema de e-commerce coleta: nome, email, CPF, endereço, dados de cartão, histórico de compras, preferências de marketing.

Responda:
1. Quais regulamentações se aplicam?
2. Quais dados são sensíveis ou pessoais?
3. Como implementar os direitos do titular (acesso, correção, exclusão)?
4. Qual a justificativa legal para coletar cada dado?
5. Como minimizar a coleta?

---

## Exercício 5: Projetando multi-tenant

Um SaaS de gestão financeira atende contadores com múltiplos clientes cada.

Responda:
1. Qual estratégia de isolamento você recomenda? Por quê?
2. Como modelar as entidades Tenant, Usuário, Cliente, Transação?
3. Como garantir que um usuário não veja dados de outro tenant?
4. Como fazer backup de um tenant específico?
5. Como migrar um tenant para um banco dedicado no futuro?
