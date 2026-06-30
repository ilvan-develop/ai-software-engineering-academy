# Checklist: Auditor Agent

## Auditoria de Arquitetura

- [ ] A arquitetura segue Clean Architecture / DDD?
- [ ] Dependências apontam para dentro (regra da dependência)?
- [ ] Domínios estão isolados em bounded contexts?
- [ ] Acoplamento entre módulos é aceitável?
- [ ] Há documentação arquitetural (ADR, C4)?
- [ ] A arquitetura suporta os requisitos não-funcionais?

## Auditoria de Segurança

- [ ] Autenticação e autorização implementadas corretamente?
- [ ] Proteção contra SQL injection?
- [ ] Proteção contra XSS e CSRF?
- [ ] Rate limiting implementado?
- [ ] Segredos e variáveis de ambiente protegidos?
- [ ] Headers de segurança configurados (CSP, HSTS, etc.)?

## Auditoria de Código

- [ ] TypeScript strict mode ativado sem `any`?
- [ ] Lint e formatação consistentes?
- [ ] Tratamento de erros adequado?
- [ ] Código morto ou comentado?
- [ ] Nomes de variáveis e funções descritivos?
- [ ] Complexidade ciclomática aceitável?

## Auditoria de Performance

- [ ] Consultas N+1 identificadas?
- [ ] Cache implementado onde necessário?
- [ ] Bundle size otimizado?
- [ ] Lazy loading aplicado?
- [ ] Imagens otimizadas?
- [ ] Core Web Vitals dentro do esperado?

## Auditoria de DevOps

- [ ] Dockerfile otimizado (multi-stage)?
- [ ] CI/CD pipeline configurado?
- [ ] Health checks implementados?
- [ ] Logs estruturados?
- [ ] Monitoramento e alertas configurados?
- [ ] Backup e recovery testados?
