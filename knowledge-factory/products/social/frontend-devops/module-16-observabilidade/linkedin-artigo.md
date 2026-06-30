==================================================
LINKEDIN — Artigo
==================================================

Titulo: Módulo 16 - Observabilidade: Logs, Métricas e Tracing: O Que Todo Arquiteto Deveria Saber


## 1. O que é observabilidade?

- Observabilidade é a capacidade de **entender o estado interno do sistema** a partir de seus outputs externos (logs, métricas, traces).
- LOGS                           MÉTRICAS                         TRACING
- Eventos discretos              Dados agregados                  Fluxo de requisições

## 2. Logs Estruturados

- // ❌ Log em texto (não searchável)
- console.log('Usuário', userId, 'fez login de', ip);
- // ✅ Log estruturado (JSON)

## 3. Métricas

- Counter:      Valor que só aumenta (req total, errors total)
- Gauge:        Valor que sobe e desce (memória, conexões ativas)
- Histogram:    Distribuição de valores (response time p50, p95, p99)

## 4. Tracing Distribuído

- Requisição: POST /api/orders
- ┌─────────────────────────────────────────────────────┐
- │ Trace ID: abc123                                     │

## 5. Dashboards com Grafana

- RED Method (Rate, Errors, Duration):
- | Métrica               | Descrição                 | Tipo     |
- |-----------------------|---------------------------|----------|


---

🔥 Gostou? Compartilhe e marque alguem que precisa ler isso.

#ArquiteturaDeSoftware #EngenhariaDeSoftware #CarreiraDev
