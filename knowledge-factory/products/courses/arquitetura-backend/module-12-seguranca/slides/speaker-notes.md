## Introducao

# Módulo 12 — Segurança
**Protegendo sistemas Enterprise contra ameaças reais.**
---

---
## 1. Por que segurança é o requisito mais importante

Segurança não é uma feature — é um **pré-requisito**. Um sistema inseguro é um passivo, não um ativo.
### O custo de uma falha de segurança
Falha de segurança típica:
┌──────────────────────────────────────────────┐
│  Dados vazados                               │
│  Multas regulatórias (LGPD: até 2% do fat.) │
│  Perda de confiança dos clientes             │
│  Custos de remediação (R$ 200k-2M médio)     │

---
## 2. OWASP Top 10 (2021)

As 10 vulnerabilidades mais críticas em aplicações web.
### 1. Broken Access Control
> Usuário acessa recursos que não deveria.
// ❌ Ruim: Não verifica se o recurso pertence ao usuário
@Get('/orders/:id')
async getOrder(@Param('id') id: string) {
return this.orderRepo.findById(id);  // qualquer um vê qualquer pedido!
}

---
## 3. Autenticação com JWT

### Fluxo completo
1. Usuário envia email + senha
2. Servidor valida credenciais
3. Servidor gera ACCESS TOKEN (15min) + REFRESH TOKEN (7d)
4. Cliente armazena e envia access token em requisições
5. Servidor valida token em cada requisição (AuthGuard)
6. Quando access token expira, cliente usa refresh token para obter novo
### Implementação

---
## 4. Autorização com CASL (RBAC)

### Definição de abilities
// abilities.ts
export type Action = 'manage' | 'create' | 'read' | 'update' | 'delete';
export type Subject = 'User' | 'Order' | 'Product' | 'Report' | 'all';
export function defineAbilitiesFor(user: User): PureAbility {
return AbilityBuilder.define((can, cannot) => {
// Admin pode fazer tudo
if (user.role === 'admin') {

---
## 5. Rate Limiting

Protege contra brute force, DDoS e abuso.
### Implementação com @nestjs/throttler
// app.module.ts
@Module({
imports: [
ThrottlerModule.forRoot([{
ttl: 60000,      // 1 minuto
limit: 60,        // 60 requisições por minuto (global)

---
## 6. Headers de Segurança (Helmet + CSP)

### Helmet (NestJS)
import helmet from 'helmet';
app.use(helmet());
// Configura automaticamente:
// Content-Security-Policy
// X-Content-Type-Options: nosniff
// X-Frame-Options: DENY
// X-XSS-Protection: 0

---
## 7. Proteções Específicas

### SQL Injection
// ❌ Nunca fazer
const users = await prisma.$queryRawUnsafe(`SELECT * FROM users WHERE email = '${email}'`);
// ✅ Prisma previne com query builders
const user = await prisma.user.findUnique({ where: { email } });
// ✅ Se precisar de raw query, usar parametrização
const users = await prisma.$queryRaw`SELECT * FROM users WHERE email = ${email}`;
### XSS (Cross-Site Scripting)

---
## 8. Secrets Management

### O que NÃO fazer
// ❌ Hardcoded no código
const API_KEY = 'sk-1234567890abcdef';
const DB_PASSWORD = 'minha-senha-super-secreta';
// ❌ No .env comitado
.env
DB_PASSWORD=minha-senha
// ❌ No código fonte

---
## 9. Auditoria de Segurança

### O que auditar
// Log de ações sensíveis
@Injectable()
export class AuditService {
async log(action: AuditAction): Promise<void> {
await prisma.auditLog.create({
data: {
userId: action.userId,

---
