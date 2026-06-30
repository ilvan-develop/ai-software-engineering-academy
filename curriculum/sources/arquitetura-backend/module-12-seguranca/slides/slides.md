# Módulo 12 — Slides

---

## Slide 1: Título

**Segurança**
Protegendo sistemas Enterprise contra ameaças reais

---

## Slide 2: O custo de uma falha

```
Dados vazados
Multas LGPD (até 2% do faturamento)
Perda de confiança dos clientes
Custo de remediação: R$ 200k-2M
```

Custo de prevenir: treinamento + ferramentas + processo

---

## Slide 3: Mindset de segurança

```
❌ "Segurança é do DevOps"
❌ "Depois a gente adiciona"
❌ "Ninguém vai atacar"

✅ "Segurança é de todos"
✅ "Parte da definição de 'pronto'"
✅ "Se tem valor, vai ser atacado"
```

---

## Slide 4: OWASP Top 10 (1-5)

1. **Broken Access Control** — verificar propriedade do recurso
2. **Cryptographic Failures** — bcrypt, não MD5
3. **Injection** — ORM, query parameters
4. **Insecure Design** — rate limiting, MFA
5. **Security Misconfiguration** — CORS restrito, Helmet

---

## Slide 5: OWASP Top 10 (6-10)

6. **Vulnerable Components** — npm audit, Dependabot
7. **Auth Failures** — JWT com expiração curta
8. **Data Integrity** — assinatura de dados
9. **Logging Failures** — logs estruturados
10. **SSRF** — validar URLs

---

## Slide 6: JWT Flow

```
Login → Access Token (15min) + Refresh Token (7d)

Requisição:
  Header: Authorization: Bearer <access_token>

Expirou?
  POST /auth/refresh { refreshToken }
  → novos tokens (com rotação)
```

---

## Slide 7: Autorização com CASL

```typescript
// Admin pode tudo
if (user.role === 'admin') {
  can('manage', 'all');
}

// Usuário comum
can('read', 'Order', { userId: user.id });
can('update', 'Order', { userId: user.id, status: 'pending' });

// Ninguém deleta
cannot('delete', 'all');
```

---

## Slide 8: Rate Limiting

```
Login:       5 tentativas/minuto
Password Reset: 3 tentativas/minuto
API geral:   60 requisições/minuto
Upload:      10 requisições/minuto

Resposta: 429 Too Many Requests
```

---

## Slide 9: Headers de Segurança

```
Helmet ativa:
  Content-Security-Policy
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Strict-Transport-Security
  Referrer-Policy: no-referrer
```

---

## Slide 10: Proteções específicas

```
SQL Injection:    ORM + queries parametrizadas
XSS:              DOMPurify (frontend)
CSRF:             csurf token (backend)

Nunca:
  SELECT * FROM users WHERE email = '${email}'
```

---

## Slide 11: Secrets Management

```
❌ Código fonte:         API_KEY = 'sk-123'
❌ .env commitado:       DB_PASSWORD=minha-senha
❌ Logs:                 console.log(user.cpf)

✅ .env.example (sem valores reais)
✅ .env oculto (.gitignore)
✅ Validação na inicialização
```

---

## Slide 12: Para refletir

> "A única segurança real é saber que você nunca está 100% seguro — e agir de acordo."

> "Segurança não é um produto, é um processo." — Bruce Schneier
