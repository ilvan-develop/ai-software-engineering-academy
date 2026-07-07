# Módulo 16 — Slides

---

## Slide 1: Título

**Observabilidade**
Logs, Métricas e Tracing

---

## Slide 2: Os 3 pilares

```text
LOGS              MÉTRICAS           TRACING
"O quê?"          "Quantos?"         "Por onde?"
                  "Quanto tempo?"

Usuário logou     500 req/s          GET /orders → Auth → DB
Erro no pgto      p95: 200ms
```markdown

Sem observabilidade: "O sistema está lento" (e não sabe onde)

---

## Slide 3: Logs Estruturados

```javascript
❌ console.log('Usuário', id, 'logou')

✅ logger.info('Usuário autenticado', {
    userId: 'abc',
    email: 'joao@email.com',
    ip: '192.168.1.1',
  })
```yaml

Níveis: error → warn → info → debug
**Nunca** logar senhas, dados sensíveis

---

## Slide 4: Métricas — RED Method

| Métrica | O que mede | Exemplo |
|---------|-----------|---------|
| **R**ate | Requisições/s | 1.200 req/s |
| **E**rrors | % de erros | 0.05% |
| **D**uration | Latência | p95: 187ms |

+ Métricas de negócio (usuários ativos, pedidos)

---

## Slide 5: Implementação Prometheus

```typescript
const httpRequestDuration = new Histogram({
  name: 'http_request_duration_seconds',
  buckets: [0.01, 0.05, 0.1, 0.5, 1, 2, 5],
});
```markdown

Middleware captura: method, path, status, duration

---

## Slide 6: Tracing — Rastreando requisições

```text
POST /api/orders (Trace: abc123)
  ├── Auth Service (5ms)
  ├── Order Service (150ms)
  │   ├── DB Query (100ms)
  │   └── Redis Cache (20ms)
  └── Payment API (300ms)
  Total: 457ms
```yaml

OpenTelemetry: instrumentação automática

---

## Slide 7: OpenTelemetry

```typescript
const sdk = new NodeSDK({
  instrumentations: [
    getNodeAutoInstrumentations({
      http: {},
      express: {},
      nestjs: {},
      pg: {},
    }),
  ],
});
```markdown

Plug and play — instrumenta a maioria das bibliotecas

---

## Slide 8: Grafana Dashboard

```text
┌─────────────────────────────────────────────────┐
│  STATUS: ✅ OPERACIONAL                         │
├──────────┬──────────┬──────────────────────────┤
│ 1,234/s  │ 0.05%    │ p95: 187ms               │
│ Req Rate │ Erros    │ Latência                 │
└──────────┴──────────┴──────────────────────────┘
│ Latency by Endpoint                             │
│ GET /products     45ms  ████████               │
│ POST /orders     320ms  ██████████████████      │
```markdown

---

## Slide 9: Alertas

```text
P0 (imediato):
  Error rate > 5% │ p95 > 2s │ Servidor down

P1 (1 hora):
  Error rate > 1% │ Disco > 80% │ Memória > 85%

P2 (24h):
  Error rate > 0.5% │ Cache hit < 50%
```markdown

---

## Slide 10: Stack de Observabilidade

```text
App → Prometheus (métricas) → Grafana (dashboard)
App → Loki (logs) → Grafana (explore)
App → OpenTelemetry → Jaeger/Tempo (traces)
```markdown

Tudo centralizado no Grafana

---

## Slide 11: Anti-padrões

- **Log em texto** — não searchável
- **Logar dados sensíveis** — senha, CPF, token
- **Só log de erro** — sem info/warn, sem contexto
- **Sem métricas** — "está lento" e não sabe quanto
- **Sem alertas** — descobre problema pelo usuário
- **Dashboard sem ação** — bonito mas ninguém olha
- **Sem tracing** — requisição lenta mas não sabe onde

---

## Slide 12: Para refletir

> "Se você não consegue medir, não consegue melhorar."

> "Observabilidade não é sobre ferramentas. É sobre **conseguir fazer perguntas ao sistema e obter respostas**."
