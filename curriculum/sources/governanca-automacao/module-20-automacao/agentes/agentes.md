# Agentes — Módulo 20: Automação

Papéis e responsabilidades dos envolvidos no processo de automação dentro de uma organização de engenharia de software.

---

## Squad de Desenvolvimento

### Tech Lead (Líder Técnico)

**Responsabilidades:**
- Definir a estratégia de automação do squad
- Projetar a arquitetura dos pipelines CI/CD
- Escolher ferramentas (GitHub Actions vs GitLab CI, Terraform vs Pulumi)
- Definir padrões de pipeline as code
- Revisar PRs relacionados a automação
- Garantir que métricas de pipeline (tempo, taxa de falha, MTTR) sejam monitoradas
- Mentorar devs nas práticas de automação

**Entregáveis:**
- Pipeline CI/CD do squad
- Documentação de estratégia de deploy
- Definição de feature flags e estratégia de liberação

### Desenvolvedor(a) Sênior

**Responsabilidades:**
- Implementar pipelines e scripts de automação
- Criar actions/jobs reutilizáveis
- Configurar ferramentas de SAST (SonarQube, ESLint security)
- Implementar testes automatizados (unitários, integração, e2e)
- Configurar ambientes efêmeros para features
- Participar de on-call e execução de runbooks

**Entregáveis:**
- Código de pipeline (YAML, scripts)
- Testes automatizados
- Scripts de automação (deploy, migration, self-healing)

### Desenvolvedor(a) Pleno/Júnior

**Responsabilidades:**
- Seguir os padrões de pipeline definidos
- Escrever testes automatizados para suas entregas
- Manter dependências atualizadas (Dependabot)
- Reportar pipelines quebradas e propor melhorias
- Aprender e aplicar Conventional Commits

---

## Squad de DevOps / Plataforma

### DevOps Engineer / SRE

**Responsabilidades:**
- Gerenciar a infraestrutura de CI/CD (runners, agents, self-hosted)
- Configurar e manter ferramentas de IaC (Terraform Cloud, Pulumi)
- Gerenciar secrets e acesso a ambientes
- Implementar self-healing e runbooks automáticos
- Configurar monitoramento e alertas (Datadog, Grafana, New Relic)
- Garantir SLA das pipelines (disponibilidade, tempo de execução)
- Gerenciar custos de infraestrutura (ambientes efêmeros, RDS, ECS)

**Entregáveis:**
- Infraestrutura de CI/CD
- Runbooks automáticos
- Dashboards de observabilidade
- Políticas de segurança (SAST, DAST, SCA)

### Platform Engineer

**Responsabilidades:**
- Construir plataforma interna (IDP) com automações reutilizáveis
- Criar templates de pipeline para uso dos squads
- Desenvolver actions/plugins internos
- Gerenciar feature flag platform (LaunchDarkly, Configu)
- Prover self-service para criação de ambientes efêmeros
- Versionar e distribuir módulos de IaC para os times

**Entregáveis:**
- Internal Developer Platform
- Templates de pipeline
- Módulos de IaC compartilhados

---

## Squad de Qualidade (QA)

### QA Engineer

**Responsabilidades:**
- Escrever e manter testes E2E automatizados
- Definir cenários de teste para canary deployment
- Validar ambientes efêmeros
- Configurar ferramentas de DAST (OWASP ZAP, Burp)
- Participar da definição de métricas de qualidade no pipeline
- Garantir que testes de regressão sejam executados automaticamente

**Entregáveis:**
- Suíte de testes E2E
- Cenários de validação de deploy
- Relatórios de qualidade automatizados

---

## Squad de Segurança (InfoSec)

### Security Engineer

**Responsabilidades:**
- Configurar e manter ferramentas de SAST (SonarQube, CodeQL)
- Definir políticas de dependency scanning (Snyk, Trivy)
- Revisar e aprovar mudanças em regras de segurança no pipeline
- Configurar gates de segurança que bloqueiam deploys
- Treinar o time em segurança ofensiva e defensiva
- Auditar logs de pipeline para incidentes de segurança

**Entregáveis:**
- Políticas de segurança automatizadas
- Gates de segurança no pipeline
- Relatórios trimestrais de vulnerabilidades

---

## Product Manager (PM)

**Responsabilidades:**
- Priorizar investimentos em automação (custos vs benefícios)
- Definir SLAs para deploy (quantas vezes por dia/semana)
- Aprovar releases em ambientes críticos
- Comunicar janelas de deploy e mudanças para stakeholders
- Definir métricas de negócio para feature flags (conversão, adoção)

**Entregáveis:**
- Roadmap de automação
- SLAs de deploy
- OKRs de engenharia relacionados a automação

---

## Fluxo de Interação entre Agentes

```
[Dev] escreve código + testes
  → push → [Pipeline CI] executa lint, test, build, SAST
  → [Code Review] humano + bots (Dependabot, CodeQL)
  → merge na main
  → [Pipeline CD] build imagem, scan, deploy staging
  → [QA] valida em staging (e2e, DAST)
  → [PM] aprova release
  → [Pipeline Deploy] canary → 100% (com feature flags)
  → [SRE] monitora métricas e alertas
  → [Self-Healing] responde automaticamente a incidentes
```

---

## Matriz de Responsabilidades (RACI)

| Atividade | Tech Lead | Dev | DevOps | QA | Security | PM |
|-----------|-----------|-----|--------|-----|----------|-----|
| Definir estratégia de automação | R | C | C | I | C | A |
| Implementar pipeline CI | A | R | C | I | I | I |
| Configurar IaC | I | C | R | I | C | I |
| Criar testes E2E | A | C | I | R | I | I |
| Configurar SAST | C | C | A | I | R | I |
| Gerenciar feature flags | A | R | C | I | I | C |
| Aprovar release em produção | I | I | I | C | C | R |
| Monitorar métricas de pipeline | A | C | R | I | I | I |
| Executar runbook de incidente | C | C | R | I | I | I |

**Legenda:** R = Responsável, A = Aprovador, C = Consultado, I = Informado

---

## Referências

- [GitHub Actions Docs](https://docs.github.com/actions)
- [GitLab CI Docs](https://docs.gitlab.com/ee/ci/)
- [Terraform Best Practices](https://developer.hashicorp.com/terraform/tutorials)
- [Semantic Release](https://semantic-release.gitbook.io/)
- [Conventional Commits](https://www.conventionalcommits.org/)
