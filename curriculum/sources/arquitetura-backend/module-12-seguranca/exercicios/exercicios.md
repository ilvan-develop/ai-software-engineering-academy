# Exercícios — Módulo 12

## Exercício 1: Identificando vulnerabilidades

Para cada código, identifique qual vulnerabilidade OWASP está presente e proponha a correção.

**Código A:**
```typescript
@Get('/users')
async listUsers() {
  return this.userRepo.findAll();
}
```text

**Código B:**
```typescript
const user = await prisma.$queryRawUnsafe(
  `SELECT * FROM users WHERE email = '${email}'`
);
```text

**Código C:**
```typescript
@Post('/login')
async login(@Body() dto: LoginDto) {
  const user = await this.userRepo.findByEmail(dto.email);
  if (!user) throw new UnauthorizedException();
  if (user.password !== dto.password) throw new UnauthorizedException();
  return this.jwtService.sign({ userId: user.id });
}
```text

**Código D:**
```typescript
app.enableCors();
```text

**Código E:**
```typescript
const apiKey = 'sk-proj-abc123def456';
```markdown

---

## Exercício 2: Implementando autenticação JWT

Complete a implementação abaixo com:

1. Validação de senha com bcrypt
2. Geração de access token (15min) + refresh token (7d)
3. Rate limiting (5 tentativas/min)
4. Log de auditoria

```typescript
@Controller('/auth')
export class AuthController {
  @Post('/login')
  async login(@Body() dto: LoginDto) {
    // Implementar:
    // 1. Buscar usuário por email
    // 2. Validar senha com bcrypt
    // 3. Verificar rate limit
    // 4. Gerar tokens
    // 5. Log de auditoria
    // 6. Retornar tokens
  }
}
```markdown

---

## Exercício 3: Definindo abilities CASL

Crie as abilities para um sistema de **gestão de projetos** com as seguintes regras:

- **Admin:** pode gerenciar tudo
- **Gerente:** pode criar/editar projetos, gerenciar membros do time, ver relatórios
- **Desenvolvedor:** pode ver projetos do seu time, criar tarefas, atualizar tarefas atribuídas a ele
- **Cliente:** pode ver apenas projetos onde é stakeholder, criar tickets

```typescript
export function defineAbilitiesFor(user: User): PureAbility {
  return AbilityBuilder.define((can, cannot) => {
    // Implementar regras
  });
}
```markdown

---

## Exercício 4: Configurando segurança

Configure a segurança para uma aplicação NestJS:

```typescript
async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // 1. Configurar Helmet com CSP
  // 2. Configurar CORS (origem específica)
  // 3. Configurar CSRF protection
  // 4. Configurar rate limiting global (60 req/min)
  // 5. Validar variáveis de ambiente na inicialização
  // 6. Configurar logging de requisições

  await app.listen(3000);
}
```markdown

---

## Exercício 5: Plano de segurança

Crie um plano de segurança para um SaaS de **saúde** (dados sensíveis, LGPD, HIPAA).

O plano deve incluir:

1. **Autenticação** — JWT, MFA, refresh token rotation
2. **Autorização** — RBAC + verificação de propriedade
3. **Dados** — criptografia em repouso e em trânsito
4. **Auditoria** — logs de acesso a dados sensíveis
5. **Rate limiting** — endpoints críticos
6. **Headers de segurança** — CSP, HSTS, CORS
7. **Secrets** — gerenciamento de chaves
8. **Incident response** — o que fazer em caso de vazamento
