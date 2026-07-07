# Exercícios — Capítulo 4: Segurança

> **Progressão:** Fácil → Médio → Difícil  
> **Total:** 4 exercícios

---

## Exercício 1 — Fácil: Identifique Vulnerabilidades

**Tema:** OWASP Top 10

Identifique qual vulnerabilidade OWASP está presente em cada cenário:

| # | Cenário | Vulnerabilidade |
|---|---------|-----------------|
| 1 | Um endpoint aceita `user.role = 'admin'` direto do corpo da requisição. | ? |
| 2 | A query `SELECT * FROM users WHERE id = '${req.params.id}'` é usada diretamente. | ? |
| 3 | Senhas são armazenadas em MD5 no banco de dados. | ? |
| 4 | O token JWT não tem data de expiração e fica válido para sempre. | ? |

---

## Exercício 2 — Médio: Implemente RBAC

**Tema:** Role-Based Access Control

Implemente um guard `RolesGuard` que:
- Lê os metadados `@Roles('admin', 'manager')` do decorator customizado
- Verifica se o usuário autenticado (req.user) tem uma das roles necessárias
- Retorna 403 se não tiver permissão

```typescript
// Decorator
export const Roles = (...roles: string[]) => SetMetadata('roles', roles);

// Uso no controller
@Post()
@Roles('admin')
@UseGuards(JwtAuthGuard, RolesGuard)
createProduct(@Body() dto: CreateProductDto) { /* ... */ }
```

---

## Exercício 3 — Médio: Rate Limiting

**Tema:** Proteção contra abuso

Configure rate limiting em um endpoint de login usando `@nestjs/throttler`:
- Limite de 5 tentativas por minuto por IP
- Resposta com status 429 e header `Retry-After`
- Mensagem amigável: "Muitas tentativas. Tente novamente em X segundos."

---

## Exercício 4 — Difícil: Hash de Senha e Autenticação Segura

**Tema:** Proteção de credenciais

Implemente um service de autenticação completo:

```typescript
@Injectable()
export class AuthService {
  async register(dto: RegisterDto): Promise<AuthResult> { /* ... */ }
  async login(dto: LoginDto): Promise<AuthResult> { /* ... */ }
  async refreshToken(refreshToken: string): Promise<AuthResult> { /* ... */ }
  async logout(userId: string): Promise<void> { /* ... */ }
}
```

**Requisitos de segurança:**
- Senha hashada com bcrypt (cost 12)
- Access token JWT com expiração de 15 minutos
- Refresh token rotativo (invalida o anterior)
- Rate limit de login por IP
- Lockout após 5 tentativas falhas (15 min)
- Log de todas as tentativas de login (sucesso e falha)
