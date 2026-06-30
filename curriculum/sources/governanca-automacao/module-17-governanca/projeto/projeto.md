# Projeto Módulo 17 — Framework de Governança para um SaaS Enterprise

## Objetivo

Criar o framework completo de governança para um SaaS enterprise, incluindo padrões de código, políticas de revisão, gestão de dependências, compliance e documentação de arquitetura.

## Contexto

Você é o **Tech Lead** de um SaaS de **gestão de contratos** com:

- Backend: NestJS (TypeScript)
- Frontend: Next.js (TypeScript)
- Banco: PostgreSQL 16
- 3 squads: 10 desenvolvedores no total
- Clientes enterprise com exigências de SOC2 e LGPD
- Deploy semanal com Git Flow

O time nunca teve governança formal. Cada dev faz do seu jeito. Resultado:
- Código inconsistente
- Review que não pega problemas reais
- Dependências desatualizadas (algumas com CVE conhecida)
- Ninguém sabe por que decisões foram tomadas
- Auditoria de cliente foi reprovada

Sua missão: implementar governança sem burocratizar o time.

## Entregáveis

### 1. Padrões de Código (arquivos de configuração)

Crie os arquivos de configuração completos para o projeto:

- `.eslintrc.json` — regras enterprise TypeScript (incluir no-unused-vars, no-console, eqeqeq)
- `.prettierrc` — single quote, trailing comma, printWidth 100
- `.editorconfig` — spaces, 2 spaces, UTF-8, LF
- `commitlint.config.js` — conventional commits
- `.husky/pre-commit` — rodar lint-staged
- `.husky/commit-msg` — rodar commitlint
- `.lintstagedrc.json` — lint + format em .ts/.tsx

### 2. Políticas de Repositório

Crie:

- `.github/PULL_REQUEST_TEMPLATE.md` — template de PR com checklist
- `.github/CODEOWNERS` — definir owners por área (ex: @team-backend para /api/*)
- `renovate.json` — configurar Renovate (diário patches, semanal minor, mensal major)
- `.env.example` — com valores fictícios e comentários
- `.pre-commit-config.yaml` — hook de detecção de segredos

### 3. Documentação de Arquitetura

Crie:

- `docs/adr/ADR-001-usar-nestjs-como-framework.md`
  - Contexto: time conhece Node.js, precisa de estrutura enterprise
  - Decisão: NestJS com modularização por domínio
  - Consequências: + estrutura, - curva de aprendizado
  - Alternativas: Express puro, Fastify

- `docs/adr/ADR-002-usar-postgresql-como-banco.md`
  - Contexto: dados relacionais, multi-tenant por schema
  - Decisão: PostgreSQL 16 com schema por tenant
  - Consequências: + isolation, - complexidade operacional
  - Alternativas: MySQL, MongoDB

### 4. Plano de Implementação

Escreva um plano (`GOVERNANCA_PLANO.md`) respondendo:

**Fase 1 — Quick wins (semana 1)**
- O que pode ser implementado em 1 semana com impacto imediato?
- Ex: ESLint, Prettier, .env.example, PR template

**Fase 2 — Estrutura (semanas 2-4)**
- O que precisa de mais planejamento?
- Ex: ADRs, code review gates, Renovate, branch protection

**Fase 3 — Cultura (mês 2+)**
- O que depende de mudança cultural?
- Ex: post-mortem sem blame, SLOs, compliance contínuo

**Riscos e mitigação**
- O que pode dar errado?
- Como engajar o time sem gerar resistência?
- Como medir se a governança está funcionando?

### 5. SLOs e Dashboard

Crie (`SLO_DASHBOARD.md`):

**SLIs e SLOs para 3 serviços:**
- API de contratos (latência, erro, disponibilidade)
- Serviço de notificações (freshness, entrega)
- Frontend (carregamento, erro de página)

**Dashboard de saúde:**
- Status geral 🟢🟡🔴
- Thresholds para cada indicador
- Frequência de medição
- Quem é notificado em caso de violação

## Critérios de avaliação

- [ ] Configurações de padrões de código funcionais e completas
- [ ] PR template com checklist abrangente
- [ ] ADRs seguindo o formato (contexto, decisão, consequências, alternativas)
- [ ] Renovate configurado com schedule e regras de automerge
- [ ] .env.example sem nenhum valor real
- [ ] Pre-commit hook para detecção de segredos
- [ ] Plano de implementação com fases claras e realistas
- [ ] SLOs bem definidos com SLIs mensuráveis
- [ ] Dashboard com thresholds e responsáveis
- [ ] Plano considera a cultura do time (não só ferramentas)
