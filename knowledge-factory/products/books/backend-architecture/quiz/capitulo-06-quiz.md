# Quiz — Capítulo 6: Multi-Tenant — Implementação com NestJS e Prisma

**Instruções:** 5 perguntas de múltipla escolha. Apenas uma alternativa correta.

---

## Pergunta 1 (Fácil)

Onde o tenantId deve ser extraído em uma aplicação NestJS multi-tenant?

- [ ] A) Do banco de dados
- [ ] B) **Do header da requisição (X-Tenant-Id) ou do subdomínio**
- [ ] C) Do corpo da resposta
- [ ] D) Do arquivo de configuração

**Resposta:** B

---

## Pergunta 2 (Fácil)

Qual decorator do NestJS é usado para criar um middleware que será aplicado a todas as rotas?

- [ ] A) `@Module()`
- [ ] B) `@Controller()`
- [ ] C) **`@Injectable()` (com NestModule)**
- [ ] D) `@Global()`

**Resposta:** C

---

## Pergunta 3 (Médio)

Qual a função do middleware Prisma em uma aplicação multi-tenant?

- [ ] A) Criptografar dados sensíveis automaticamente
- [ ] B) **Injetar automaticamente o tenantId em todas as queries**
- [ ] C) Gerenciar conexões com múltiplos bancos de dados
- [ ] D) Fazer cache de consultas frequentes

**Resposta:** B

---

## Pergunta 4 (Médio)

Em uma arquitetura de "Banco por Tenant" com Prisma, como gerenciar as conexões?

- [ ] A) Usando um único PrismaClient que alterna banco por tenant
- [ ] B) **Criando um pool de PrismaClients, um para cada banco**
- [ ] C) Usando SQL puro em vez de Prisma
- [ ] D) Não é possível usar Prisma com banco por tenant

**Resposta:** B

---

## Pergunta 5 (Difícil)

Por que o middleware de tenant deve ignorar a entidade `Tenant` ao filtrar dados?

- [ ] A) **Porque a tabela de tenants é global e não pertence a um tenant específico**
- [ ] B) Porque a tabela de tenants não tem coluna tenantId
- [ ] C) Porque tenants não podem se autenticar no sistema
- [ ] D) Porque a tabela de tenants é um cache

**Resposta:** A
