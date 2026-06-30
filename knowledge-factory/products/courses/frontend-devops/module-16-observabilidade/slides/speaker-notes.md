## Introducao

# Módulo 16 — Observabilidade: Logs, Métricas e Tracing
**Entendendo o que acontece em produção.**
---

---
## 1. O que é observabilidade?

Observabilidade é a capacidade de **entender o estado interno do sistema** a partir de seus outputs externos (logs, métricas, traces).
### Os 3 pilares
LOGS                           MÉTRICAS                         TRACING
Eventos discretos              Dados agregados                  Fluxo de requisições
"O quê aconteceu?"             "Quantos/quanto tempo?"          "Por onde passou?"
Ex:                            Ex:                              Ex:
"Usuário X fez login"          "500 req/s, p95=200ms"           "GET /orders → Auth → DB"
"Falha no pagamento"            "Error rate: 0.5%"              "POST /payment → API → Queue"

---
## 2. Logs Estruturados

### Log em texto vs JSON
// ❌ Log em texto (não searchável)
console.log('Usuário', userId, 'fez login de', ip);
// ✅ Log estruturado (JSON)
logger.info('Usuário autenticado', {
userId: 'abc123',
email: 'joao@email.com',
ip: '192.168.1.1',

---
## 3. Métricas

### Tipos de métricas
Counter:      Valor que só aumenta (req total, errors total)
Gauge:        Valor que sobe e desce (memória, conexões ativas)
Histogram:    Distribuição de valores (response time p50, p95, p99)
Summary:      Similar ao histogram (latência, tamanho de resposta)
### Métricas essenciais
// API
http_requests_total{method, path, status}

---
## 4. Tracing Distribuído

### O que é tracing
Requisição: POST /api/orders
┌─────────────────────────────────────────────────────┐
│ Trace ID: abc123                                     │
│                                                      │
│  Span 1: Gateway (2ms)                               │
│    ├── Span 2: Auth Service (5ms)                    │
│    ├── Span 3: Order Service (150ms)                 │

---
## 5. Dashboards com Grafana

### Métricas essenciais no dashboard
RED Method (Rate, Errors, Duration):
| Métrica               | Descrição                 | Tipo     |
|-----------------------|---------------------------|----------|
| Request Rate          | req/s por endpoint         | Counter  |
| Error Rate            | % de erros                 | Counter  |
| Latency (p50/p95/p99) | Tempo de resposta          | Histogram|
| Active Users          | Usuários simultâneos       | Gauge    |

---
## 6. Alertas

### O que alertar
P0 (Resposta imediata):
- Error rate > 5% nos últimos 5 min
- p95 latency > 2s
- Servidor down
- Banco inacessível
P1 (Resposta em 1 hora):
- Error rate > 1% nos últimos 15 min

---
## 7. Centralização de Logs (Loki + Grafana)

### Configuração
# docker-compose.obs.yml
services:
prometheus:
image: prom/prometheus
ports:
- "9090:9090"
volumes:

---
## Resumo

1. **Observabilidade** = Logs + Métricas + Tracing
2. **Logs estruturados** — JSON, níveis (error/warn/info/debug), nunca dados sensíveis
3. **Métricas** — RED method (Rate, Errors, Duration) com Prometheus
4. **Tracing** — OpenTelemetry para rastrear requisições entre serviços
5. **Dashboards** — Grafana com métricas essenciais
6. **Alertas** — P0/P1/P2 com thresholds e canais de notificação
7. **Centralização** — Loki + Grafana para logs searcháveis

---
