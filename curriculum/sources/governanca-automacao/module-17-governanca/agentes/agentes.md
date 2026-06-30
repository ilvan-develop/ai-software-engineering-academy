# Agentes para o Módulo 17

## Agentes envolvidos

| Agente | Função no módulo |
|--------|------------------|
| Curriculum Architect | Estruturar conteúdo de governança |
| Technical Writer | Escrever políticas, templates e exemplos práticos |
| Reviewer | Validar consistência com frameworks reais (COBIT, ITIL, LGPD) |
| Security Expert Agent | Revisar práticas de gestão de segredos e compliance |
| DevOps Expert Agent | Validar policies de deploy e branch strategy |

## Instruções específicas

### Curriculum Architect

Ao planejar:
- Conectar com Módulo 12 (Segurança) — gestão de segredos e compliance
- Conectar com Módulo 14 (DevOps) — pipelines e deploy
- Conectar com Módulo 16 (Observabilidade) — SLOs, SLIs, monitoramento
- Conectar com Módulo 19 (Auditorias) — rastreabilidade e compliance
- Garantir que governança seja apresentada como facilitadora, não como burocracia
- Foco em práticas que um dev brasileiro encontra no dia a dia enterprise

### Technical Writer

Ao escrever:
- Usar exemplos reais de configuração (ESLint, husky, Renovate, ADR template)
- Incluir templates prontos para uso (PR template, ADR template)
- Demonstrar código TypeScript real nos exemplos de audit log
- Manter tom prático com "receitas de bolo" que o dev pode copiar
- Adaptar exemplos de compliance para a realidade brasileira (LGPD em destaque)

### Reviewer

Ao revisar:
- Verificar se as definições de COBIT, ITIL, SOC2, ISO 27001 e LGPD estão factualmente corretas
- Confirmar que os templates seguem boas práticas da indústria
- Validar que as configurações de ESLint/prettier/husky são funcionais
- Garantir que as métricas de SLO/SLI fazem sentido técnico

### Security Expert Agent

Ao contribuir:
- Reforçar que gestão de segredos é o ponto mais crítico do módulo
- Incluir cenário de resposta a incidente de vazamento
- Verificar conformidade LGPD nos exemplos de audit log
- Sugerir ferramentas adicionais de segurança (detect-secrets, truffleHog)

### DevOps Expert Agent

Ao contribuir:
- Validar branch strategy e rollback plan apresentados
- Garantir que os gates de deploy são realistas e implementáveis
- Sugerir integração com GitHub Actions / GitLab CI nos exemplos
- Revisar a seção de health checks pós-deploy
