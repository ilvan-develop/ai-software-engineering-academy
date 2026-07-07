# Projeto Módulo 16 — Stack de Observabilidade

## Objetivo

Implementar a stack completa de observabilidade para um sistema Enterprise.

## Contexto

Você é o SRE responsável por implementar observabilidade no SaaS de Gestão de Projetos. O sistema tem:

- API NestJS (backend)
- Next.js (frontend)
- PostgreSQL (banco)
- Redis (cache)
- Docker (containerização)

## Entregáveis

### 1. Logs Estruturados

Configure Winston no backend com:
- Formato JSON em produção
- Pretty print em desenvolvimento
- Rotação de arquivos (10MB, 5 arquivos)
- Níveis: error, warn, info, debug
- Metadados: service name, environment, version

### 2. Métricas Prometheus

Implemente métricas para:
- HTTP requests (rate, errors, duration) por endpoint
- Database queries (rate, duration) por operação
- Conexões ativas
- Métricas de negócio (projetos criados, tarefas concluídas)

### 3. Tracing OpenTelemetry

Configure OpenTelemetry no backend com:
- Instrumentação automática (HTTP, NestJS, Prisma, Redis)
- Exportação para Jaeger ou Tempo
- Spans customizados em operações de negócio
- Atributos relevantes em cada span

### 4. Docker Compose de Observabilidade

```yaml
services:
  prometheus:
  loki:
  grafana:
  tempo:  # ou jaeger
```markdown

### 5. Dashboard Grafana

Crie um dashboard com:
- Visão geral (RED method)
- Latência por endpoint
- Erros por endpoint e tipo
- Banco de dados (conexões, queries lentas)
- Métricas de negócio
- Logs recentes (Loki)

### 6. Alertas

Configure alertas Prometheus para:
- Error rate > 5%
- p95 latency > 2s
- Disco > 80%
- Quedas de tráfego súbitas

## Critérios de avaliação

- [ ] Logs estruturados em JSON
- [ ] Métricas RED method implementadas
- [ ] Tracing com OpenTelemetry
- [ ] Docker compose com stack de observabilidade
- [ ] Dashboard Grafana com métricas essenciais
- [ ] Alertas configurados com thresholds
- [ ] Nenhum dado sensível em logs
