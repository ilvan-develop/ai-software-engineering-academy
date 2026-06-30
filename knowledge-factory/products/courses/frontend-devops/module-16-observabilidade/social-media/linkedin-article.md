# Módulo 16 - Observabilidade: Logs, Métricas e Tracing

---

## 1. O que é observabilidade?

Observabilidade é a capacidade de **entender o estado interno do sistema** a partir de seus outputs externos (logs, métricas, traces).
### Os 3 pilares
LOGS                           MÉTRICAS                         TRACING
Eventos discretos              Dados agregados                  Fluxo de requisições

## 2. Logs Estruturados

### Log em texto vs JSON
// ❌ Log em texto (não searchável)
console.log('Usuário', userId, 'fez login de', ip);
// ✅ Log estruturado (JSON)

## 3. Métricas

### Tipos de métricas
Counter:      Valor que só aumenta (req total, errors total)
Gauge:        Valor que sobe e desce (memória, conexões ativas)
Histogram:    Distribuição de valores (response time p50, p95, p99)

## 4. Tracing Distribuído

### O que é tracing
Requisição: POST /api/orders
┌─────────────────────────────────────────────────────┐
│ Trace ID: abc123                                     │

## 5. Dashboards com Grafana

### Métricas essenciais no dashboard
RED Method (Rate, Errors, Duration):
| Métrica               | Descrição                 | Tipo     |
|-----------------------|---------------------------|----------|

## 6. Alertas

### O que alertar
P0 (Resposta imediata):
- Error rate > 5% nos últimos 5 min
- p95 latency > 2s

---
*Este artigo faz parte da formacao Arquitetura de Software Enterprise com IA*