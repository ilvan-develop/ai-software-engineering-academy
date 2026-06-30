# Metodologia AI Enterprise Software Engineering

**Processo repetível, independente de ferramenta.**

## Ciclo de Desenvolvimento com IA

```
 1. DESCOBRIR (Discovery)
    ├── Pesquisa de mercado
    ├── Entrevistas com stakeholders
    ├── Análise de concorrência
    └── Definição do problema

 2. DEFINIR (Product)
    ├── Product Canvas
    ├── Lean Canvas
    ├── User Story Mapping
    └── Roadmap

 3. PROJETAR (UX/UI)
    ├── Personas e Jornadas
    ├── User Flow
    ├── Wireframes
    └── Design System + UI

 4. ARQUITETAR
    ├── Definição de domínios
    ├── Clean Architecture / DDD
    ├── Modelagem de dados
    └── Decisões técnicas (ADR)

 5. IMPLEMENTAR COM AGENTES
    ├── Ativação de agentes especializados
    ├── Backend (NestJS + Prisma)
    ├── Frontend (Next.js)
    └── Integrações

 6. AUDITAR CONTINUAMENTE
    ├── Auditoria de arquitetura
    ├── Auditoria de segurança
    ├── Auditoria de código
    └── Score + Plano de ação

 7. CORRIGIR E REFATORAR
    ├── Priorização de issues
    ├── Correção por agentes especializados
    └── Validação por auditoria

 8. TESTAR E VALIDAR
    ├── Testes unitários (Vitest)
    ├── Testes de integração
    ├── Testes E2E (Playwright)
    └── Code Review

 9. IMPLANTAR
    ├── Docker
    ├── CI/CD (GitHub Actions)
    └── Kubernetes (se aplicável)

10. MONITORAR E EVOLUIR
    ├── OpenTelemetry
    ├── Logs (Loki)
    ├── Métricas (Prometheus)
    ├── Dashboards (Grafana)
    └── Iteração contínua
```

## Princípios da Metodologia

1. **Humano decide, IA executa** — o arquiteto define o "o quê" e o "por quê"; a IA ajuda com o "como"
2. **Audite antes de aceitar** — todo código gerado por IA passa por auditoria antes de ir para produção
3. **Agentes especializados, não genéricos** — cada domínio tem seu próprio agente com conhecimento específico
4. **Processo sobre ferramenta** — a metodologia funciona com OpenCode, Claude Code, Cursor ou qualquer ferramenta
5. **Documentação como parte do código** — ADRs, RFCs e diagrams-as-code são gerados junto com a implementação

## Comparação: Tradicional vs. Com Agentes

| Aspecto | Tradicional | Com Agentes |
|---------|-------------|-------------|
| Velocidade | Dias para prototipar | Horas para prototipar |
| Qualidade | Dependente do dev mais fraco | Elevada por auditoria contínua |
| Consistência | Varia por desenvolvedor | Garantida por agentes + AGENTS.md |
| Documentação | Quase sempre atrasada | Gerada junto com o código |
| Escalabilidade | Contratação de pessoas | Criação de novos agentes |
