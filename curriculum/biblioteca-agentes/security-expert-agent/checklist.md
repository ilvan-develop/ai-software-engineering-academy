# Checklist: Security Expert Agent

## Checklist de Segurança

### Autenticação
- [ ] Senhas armazenadas com hash bcrypt/argon2
- [ ] JWT com expiração curta + refresh token
- [ ] Rate limiting no login
- [ ] MFA opcional implementado
- [ ] Session management seguro

### Autorização
- [ ] RBAC ou ABAC implementado
- [ ] Verificação em todas as rotas protegidas
- [ ] Permissões granulares por recurso
- [ ] Testes de autorização falhando corretamente

### Proteção
- [ ] CSP header configurado
- [ ] CORS configurado (não aberto)
- [ ] Helmet.js ativado
- [ ] Rate limiting global
- [ ] Input validation em todos os endpoints
- [ ] ORM usado (sem raw queries)
- [ ] Dependências auditadas (npm audit)
