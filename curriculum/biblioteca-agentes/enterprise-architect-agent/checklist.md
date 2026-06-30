# Checklist do Enterprise Architect Agent

## Checklist de Validação de Arquitetura

### Estrutura
- [ ] A arquitetura está dividida em camadas claras?
- [ ] As dependências apontam para dentro (regra da dependência)?
- [ ] Domínios estão isolados em bounded contexts?
- [ ] A comunicação entre módulos é explícita (interfaces)?
- [ ] O fluxo de dados é unidirecional?

### Decisões
- [ ] Cada decisão significativa tem ADR?
- [ ] Alternativas foram documentadas e descartadas com razão?
- [ ] A decisão está alinhada com os requisitos não-funcionais?

### Riscos
- [ ] Riscos de performance identificados?
- [ ] Riscos de segurança mapeados?
- [ ] Pontos únicos de falha conhecidos?
- [ ] Plano de mitigação documentado?

### Tecnologia
- [ ] Stack tecnológica justificada?
- [ ] Dependências externas avaliadas?
- [ ] Vendor lock-in evitado ou aceito conscientemente?

### Entregáveis
- [ ] Diagrama C4 Contexto
- [ ] Diagrama C4 Container
- [ ] ADRs aprovados
- [ ] Mapa de domínios
