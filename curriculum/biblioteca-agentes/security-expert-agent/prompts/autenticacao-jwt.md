# Prompt: Autenticação JWT

Você é um Security Expert Agent.

Implemente autenticação JWT completa para um sistema NestJS.

## Requisitos

1. **Registro** — email + senha com hash bcrypt
2. **Login** — validação, geração access token (15min) + refresh token (7d)
3. **Refresh** — endpoint para renovar access token
4. **Logout** — invalidar refresh token
5. **Proteção de rotas** — AuthGuard
6. **Rate limiting** — 5 tentativas de login por minuto
7. **Headers de segurança** — Helmet, CORS configurado

## Estrutura de arquivos

```
src/auth/
  auth.controller.ts
  auth.service.ts
  auth.module.ts
  strategies/jwt.strategy.ts
  strategies/jwt-refresh.strategy.ts
  guards/jwt-auth.guard.ts
  guards/roles.guard.ts
  dto/login.dto.ts
  dto/register.dto.ts
```
