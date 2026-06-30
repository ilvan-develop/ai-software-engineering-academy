---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 12 — Segurança

## Módulo 12 - Segurança

---
## 1. Por que segurança é o requisito mais importante

- Segurança não é uma feature — é um **pré-requisito**. Um sistema inseguro é um passivo, não um ativo.
- Falha de segurança típica:
- ┌──────────────────────────────────────────────┐
- │  Dados vazados                               │
- │  Multas regulatórias (LGPD: até 2% do fat.) │

---
## 2. OWASP Top 10 (2021)

- As 10 vulnerabilidades mais críticas em aplicações web.
- > Usuário acessa recursos que não deveria.
- // ❌ Ruim: Não verifica se o recurso pertence ao usuário
- @Get('/orders/:id')
- async getOrder(@Param('id') id: string) {

---
## 3. Autenticação com JWT

- 1. Usuário envia email + senha
- 2. Servidor valida credenciais
- 3. Servidor gera ACCESS TOKEN (15min) + REFRESH TOKEN (7d)
- 4. Cliente armazena e envia access token em requisições
- 5. Servidor valida token em cada requisição (AuthGuard)

---
## 4. Autorização com CASL (RBAC)

- // abilities.ts
- export type Action = 'manage' | 'create' | 'read' | 'update' | 'delete';
- export type Subject = 'User' | 'Order' | 'Product' | 'Report' | 'all';
- export function defineAbilitiesFor(user: User): PureAbility {
- return AbilityBuilder.define((can, cannot) => {

---
## 5. Rate Limiting

- Protege contra brute force, DDoS e abuso.
- // app.module.ts
- @Module({
- imports: [
- ThrottlerModule.forRoot([{

---
## 6. Headers de Segurança (Helmet + CSP)

- import helmet from 'helmet';
- app.use(helmet());
- // Configura automaticamente:
- // Content-Security-Policy
- // X-Content-Type-Options: nosniff

---
## 7. Proteções Específicas

- // ❌ Nunca fazer
- const users = await prisma.$queryRawUnsafe(`SELECT * FROM users WHERE email = '${email}'`);
- // ✅ Prisma previne com query builders
- const user = await prisma.user.findUnique({ where: { email } });
- // ✅ Se precisar de raw query, usar parametrização

---
## 8. Secrets Management

- // ❌ Hardcoded no código
- const API_KEY = 'sk-1234567890abcdef';
- const DB_PASSWORD = 'minha-senha-super-secreta';
- // ❌ No .env comitado
- .env

---
## 9. Auditoria de Segurança

- // Log de ações sensíveis
- @Injectable()
- export class AuditService {
- async log(action: AuditAction): Promise<void> {
- await prisma.auditLog.create({

---
## Exemplo: text

```text
Falha de segurança típica:
  ┌──────────────────────────────────────────────┐
  │  Dados vazados                               │
  │  Multas regulatórias (LGPD: até 2% do fat.) │
  │  Perda de confiança dos clientes             │
  │  Custos de remediação (R$ 200k-2M médio)     │
  │  Tempo de inatividade                        │
  └──────────────────────────────────────────────┘

Custo de prevenir:
  ┌──────────────────────────────────────────────┐
  │  Treinamento do time: R$ 5k                  │
  │  Ferramentas de segurança: R$ 1k/mês         │
  │  Revisão de código: parte do processo        │
  └──────────────────────────────────────────────┘
```

---
## Exemplo: text

```text
❌ "Segurança é problema do DevOps"
❌ "Depois a gente adiciona segurança"
❌ "Ninguém vai atacar nosso sistema"

✅ "Segurança é responsabilidade de todos"
✅ "Segurança é parte da definição de 'pronto'"
✅ "Se tem valor, vai ser atacado"
```

---
## Recap

- 1. Por que segurança é o requisito mais importante
- 2. OWASP Top 10 (2021)
- 3. Autenticação com JWT
- 4. Autorização com CASL (RBAC)
- 5. Rate Limiting
- 6. Headers de Segurança (Helmet + CSP)
- 7. Proteções Específicas
- 8. Secrets Management
- 9. Auditoria de Segurança

---
# Obrigado!

## Perguntas?
