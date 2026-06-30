---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 16 — Observabilidade: Logs, Métricas e Tracing

## Módulo 16 - Observabilidade: Logs, Métricas e Tracing

---
## 1. O que é observabilidade?

- Observabilidade é a capacidade de **entender o estado interno do sistema** a partir de seus outputs externos (logs, m...
- LOGS                           MÉTRICAS                         TRACING
- Eventos discretos              Dados agregados                  Fluxo de requisições
- "O quê aconteceu?"             "Quantos/quanto tempo?"          "Por onde passou?"
- Ex:                            Ex:                              Ex:

---
## 2. Logs Estruturados

- // ❌ Log em texto (não searchável)
- console.log('Usuário', userId, 'fez login de', ip);
- // ✅ Log estruturado (JSON)
- logger.info('Usuário autenticado', {
- userId: 'abc123',

---
## 3. Métricas

- Counter:      Valor que só aumenta (req total, errors total)
- Gauge:        Valor que sobe e desce (memória, conexões ativas)
- Histogram:    Distribuição de valores (response time p50, p95, p99)
- Summary:      Similar ao histogram (latência, tamanho de resposta)

---
## 4. Tracing Distribuído

- Requisição: POST /api/orders
- ┌─────────────────────────────────────────────────────┐
- │ Trace ID: abc123                                     │
- │                                                      │
- │  Span 1: Gateway (2ms)                               │

---
## 5. Dashboards com Grafana

- RED Method (Rate, Errors, Duration):
- | Métrica               | Descrição                 | Tipo     |
- |-----------------------|---------------------------|----------|
- | Request Rate          | req/s por endpoint         | Counter  |
- | Error Rate            | % de erros                 | Counter  |

---
## 6. Alertas

- P0 (Resposta imediata):
- Error rate > 5% nos últimos 5 min
- p95 latency > 2s
- Servidor down
- Banco inacessível

---
## 7. Centralização de Logs (Loki + Grafana)

- services:
- prometheus:
- image: prom/prometheus
- ports:

---
## Resumo

- 1. **Observabilidade** = Logs + Métricas + Tracing
- 2. **Logs estruturados** — JSON, níveis (error/warn/info/debug), nunca dados sensíveis
- 3. **Métricas** — RED method (Rate, Errors, Duration) com Prometheus
- 4. **Tracing** — OpenTelemetry para rastrear requisições entre serviços
- 5. **Dashboards** — Grafana com métricas essenciais
- 6. **Alertas** — P0/P1/P2 com thresholds e canais de notificação

---
## Exemplo: text

```text
LOGS                           MÉTRICAS                         TRACING
Eventos discretos              Dados agregados                  Fluxo de requisições
"O quê aconteceu?"             "Quantos/quanto tempo?"          "Por onde passou?"

Ex:                            Ex:                              Ex:
"Usuário X fez login"          "500 req/s, p95=200ms"           "GET /orders → Auth → DB"
"Falha no pagamento"            "Error rate: 0.5%"              "POST /payment → API → Queue"
```

---
## Exemplo: text

```text
Usuário: "O sistema está lento"
Dev:     "Onde? Quando? Quanto?"
Usuário: "Não sei, só está lento"
Dev:     "Não consigo reproduzir"

→ Sem dados, sem diagnóstico
```

---
## Recap

- 1. O que é observabilidade?
- 2. Logs Estruturados
- 3. Métricas
- 4. Tracing Distribuído
- 5. Dashboards com Grafana
- 6. Alertas
- 7. Centralização de Logs (Loki + Grafana)
- Resumo

---
# Obrigado!

## Perguntas?
