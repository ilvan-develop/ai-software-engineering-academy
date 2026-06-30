# Roteiro de Videoaula — Módulo 16 — Observabilidade: Logs, Métricas e Tracing

**Duracao total estimada:** 31 minutos
**Formato:** Videoaula gravada / Streaming
**Publico-alvo:** Desenvolvedores intermediarios

---

## Visao Geral do Video

| Item | Detalhe |
|------|---------|
| Titulo | Módulo 16 — Observabilidade: Logs, Métricas e Tracing |
| Duracao | 31 min |
| Cenas | 12 |
| Formato | Expositivo com demonstracao pratica |
| Nivel | Intermediario |

---

## Roteiro por Cena

### Cena 1 — INTRO

**Duracao:** 1:30

**Narracao:**
> Ola! Nesta aula vamos explorar: Módulo 16 — Observabilidade: Logs, Métricas e Tracing. Ao final, voce vai entender os conceitos fundamentais e como aplica-los na pratica. Vamos la?

**Visuais:**
- Tela de abertura com titulo do modulo. Animacao suave com o nome do curso.

**Texto na tela:**
```
[TITULO] Módulo 16 — Observabilidade: Logs, Métricas e Tracing
```

**Notas de direcao:**
- Tom energico e convidativo. Apresentar o problema que sera resolvido.

---

### Cena 2 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 1. O que é observabilidade?. Observabilidade é a capacidade de **entender o estado interno do sistema** a partir de seus outputs externos (logs, métricas, traces). LOGS                           MÉTRICAS                         TRACING Eventos discretos              Dados agregados                  Fluxo de requisições "O quê aconteceu?"             "Quantos/quanto tempo?"          "Por onde passou?"

**Visuais:**
- Slides com topicos-chave. ```text
LOGS                           MÉTRICAS                         TRACING
Eventos discretos              Dados agregados                  Fluxo de requisições
"O quê aconteceu?"             "Quantos/quanto tempo?"          "Por onde passou?"

Ex:                            Ex:                              Ex:
"Usuário X fez login"          "500 req/s, p95=200ms"           "GET /orders → Auth → DB"
"Falha no pagamento"            "Error rate: 0.5%"              "POST /payment → API → Queue"
```

**Texto na tela:**
```
[1. O que é observabilidade?]
```

**Notas de direcao:**
- Secao 2 de 9. Usar exemplos praticos.

---

### Cena 3 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 2. Logs Estruturados. // ❌ Log em texto (não searchável) console.log('Usuário', userId, 'fez login de', ip); // ✅ Log estruturado (JSON) logger.info('Usuário autenticado', {

**Visuais:**
- Slides com topicos-chave. ```text
LOGS                           MÉTRICAS                         TRACING
Eventos discretos              Dados agregados                  Fluxo de requisições
"O quê aconteceu?"             "Quantos/quanto tempo?"          "Por onde passou?"

Ex:                            Ex:                              Ex:
"Usuário X fez login"          "500 req/s, p95=200ms"           "GET /orders → Auth → DB"
"Falha no pagamento"            "Error rate: 0.5%"              "POST /payment → API → Queue"
```

**Texto na tela:**
```
[2. Logs Estruturados]
```

**Notas de direcao:**
- Secao 3 de 9. Usar exemplos praticos.

---

### Cena 4 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 3. Métricas. Counter:      Valor que só aumenta (req total, errors total) Gauge:        Valor que sobe e desce (memória, conexões ativas) Histogram:    Distribuição de valores (response time p50, p95, p99) Summary:      Similar ao histogram (latência, tamanho de resposta)

**Visuais:**
- Slides com topicos-chave. ```text
LOGS                           MÉTRICAS                         TRACING
Eventos discretos              Dados agregados                  Fluxo de requisições
"O quê aconteceu?"             "Quantos/quanto tempo?"          "Por onde passou?"

Ex:                            Ex:                              Ex:
"Usuário X fez login"          "500 req/s, p95=200ms"           "GET /orders → Auth → DB"
"Falha no pagamento"            "Error rate: 0.5%"              "POST /payment → API → Queue"
```

**Texto na tela:**
```
[3. Métricas]
```

**Notas de direcao:**
- Secao 4 de 9. Usar exemplos praticos.

---

### Cena 5 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 4. Tracing Distribuído. Requisição: POST /api/orders ┌─────────────────────────────────────────────────────┐ │ Trace ID: abc123                                     │ │                                                      │

**Visuais:**
- Slides com topicos-chave. ```text
LOGS                           MÉTRICAS                         TRACING
Eventos discretos              Dados agregados                  Fluxo de requisições
"O quê aconteceu?"             "Quantos/quanto tempo?"          "Por onde passou?"

Ex:                            Ex:                              Ex:
"Usuário X fez login"          "500 req/s, p95=200ms"           "GET /orders → Auth → DB"
"Falha no pagamento"            "Error rate: 0.5%"              "POST /payment → API → Queue"
```

**Texto na tela:**
```
[4. Tracing Distribuído]
```

**Notas de direcao:**
- Secao 5 de 9. Usar exemplos praticos.

---

### Cena 6 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 5. Dashboards com Grafana. RED Method (Rate, Errors, Duration): | Métrica               | Descrição                 | Tipo     | |-----------------------|---------------------------|----------| | Request Rate          | req/s por endpoint         | Counter  |

**Visuais:**
- Slides com topicos-chave. ```text
LOGS                           MÉTRICAS                         TRACING
Eventos discretos              Dados agregados                  Fluxo de requisições
"O quê aconteceu?"             "Quantos/quanto tempo?"          "Por onde passou?"

Ex:                            Ex:                              Ex:
"Usuário X fez login"          "500 req/s, p95=200ms"           "GET /orders → Auth → DB"
"Falha no pagamento"            "Error rate: 0.5%"              "POST /payment → API → Queue"
```

**Texto na tela:**
```
[5. Dashboards com Grafana]
```

**Notas de direcao:**
- Secao 6 de 9. Usar exemplos praticos.

---

### Cena 7 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 6. Alertas. P0 (Resposta imediata): Error rate > 5% nos últimos 5 min p95 latency > 2s Servidor down

**Visuais:**
- Slides com topicos-chave. ```text
LOGS                           MÉTRICAS                         TRACING
Eventos discretos              Dados agregados                  Fluxo de requisições
"O quê aconteceu?"             "Quantos/quanto tempo?"          "Por onde passou?"

Ex:                            Ex:                              Ex:
"Usuário X fez login"          "500 req/s, p95=200ms"           "GET /orders → Auth → DB"
"Falha no pagamento"            "Error rate: 0.5%"              "POST /payment → API → Queue"
```

**Texto na tela:**
```
[6. Alertas]
```

**Notas de direcao:**
- Secao 7 de 9. Usar exemplos praticos.

---

### Cena 8 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 7. Centralização de Logs (Loki + Grafana). services: prometheus: image: prom/prometheus ports:

**Visuais:**
- Slides com topicos-chave. ```text
LOGS                           MÉTRICAS                         TRACING
Eventos discretos              Dados agregados                  Fluxo de requisições
"O quê aconteceu?"             "Quantos/quanto tempo?"          "Por onde passou?"

Ex:                            Ex:                              Ex:
"Usuário X fez login"          "500 req/s, p95=200ms"           "GET /orders → Auth → DB"
"Falha no pagamento"            "Error rate: 0.5%"              "POST /payment → API → Queue"
```

**Texto na tela:**
```
[7. Centralização de Logs (Loki + Grafana)]
```

**Notas de direcao:**
- Secao 8 de 9. Usar exemplos praticos.

---

### Cena 9 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: Resumo. 1. **Observabilidade** = Logs + Métricas + Tracing 2. **Logs estruturados** — JSON, níveis (error/warn/info/debug), nunca dados sensíveis 3. **Métricas** — RED method (Rate, Errors, Duration) com Prometheus 4. **Tracing** — OpenTelemetry para rastrear requisições entre serviços

**Visuais:**
- Slides com topicos-chave. ```text
LOGS                           MÉTRICAS                         TRACING
Eventos discretos              Dados agregados                  Fluxo de requisições
"O quê aconteceu?"             "Quantos/quanto tempo?"          "Por onde passou?"

Ex:                            Ex:                              Ex:
"Usuário X fez login"          "500 req/s, p95=200ms"           "GET /orders → Auth → DB"
"Falha no pagamento"            "Error rate: 0.5%"              "POST /payment → API → Queue"
```

**Texto na tela:**
```
[Resumo]
```

**Notas de direcao:**
- Secao 9 de 9. Usar exemplos praticos.

---

### Cena 10 — CODE-DEMO

**Duracao:** 4:00

**Narracao:**
> Vamos ver na pratica como isso funciona. Observe este codigo em text:

**Visuais:**
- Tela dividida: editor de codigo a esquerda, terminal/output a direita.

**Texto na tela:**
```
```text
LOGS                           MÉTRICAS                         TRACING
Eventos discretos              Dados agregados                  Fluxo de requisições
"O quê aconteceu?"             "Quantos/quanto tempo?"          "Por onde passou?"

Ex:                            Ex:                              Ex:
"Usuário X fez login"          "500 req/s, p95=200ms"           "GET /orders → Auth → DB"
"Falha no pagamento"            "Error rate: 0.5%"              "POST /payment → API → Queue"
```
```

**Notas de direcao:**
- Explicar linha por linha. Destacar pontos importantes com zoom ou realce.

---

### Cena 11 — SUMMARY

**Duracao:** 1:30

**Narracao:**
> Recapitulando: vimos 1. O que é observabilidade?, 2. Logs Estruturados, 3. Métricas, 4. Tracing Distribuído, 5. Dashboards com Grafana, 6. Alertas. Esses conceitos sao fundamentais para sua formacao.

**Visuais:**
- Lista resumida com icones. Transicao suave para encerramento.

**Texto na tela:**
```
✓ 1. O que é observabilidade?
✓ 2. Logs Estruturados
✓ 3. Métricas
✓ 4. Tracing Distribuído
✓ 5. Dashboards com Grafana
✓ 6. Alertas
```

**Notas de direcao:**
- Reforcar os aprendizados principais. Conectar com o proximo modulo.

---

### Cena 12 — OUTRO

**Duracao:** 0:30

**Narracao:**
> Na proxima aula, vamos aprofundar esses conceitos. Nao perca!

**Visuais:**
- Tela final com links, inscricao, e teaser da proxima aula.

**Texto na tela:**
```
Proximo modulo: [TITULO DO PROXIMO MODULO]
```

**Notas de direcao:**
- Chamada para acao: inscrever-se, comentar, compartilhar.

---

## Checklist de Producao

- [ ] Roteiro revisado
- [ ] Slides preparados
- [ ] Ambiente de codigo configurado
- [ ] Microfone testado
- [ ] Gravacao de tela configurada (1920x1080)
- [ ] Exemplos de codigo testados
- [ ] Legendas geradas
- [ ] Thumbnail criada
- [ ] Descricao e tags preenchidas
- [ ] Capitulos do video marcados

---

## Sugestoes de Thumbnail

- Texto: 'Módulo 16 '
- Cor de fundo: azul escuro (#1a2332)
- Destaque: codigo ou diagrama ao fundo
- Rosto do apresentador no canto inferior direito

---

## SEO

**Titulo:** Módulo 16 — Observabilidade: Logs, Métricas e Tracing | Arquitetura Enterprise
**Descricao:** Aprenda módulo 16 — observabilidade: logs, métricas e tracing. Nesta aula abordamos conceitos fundamentais com exemplos praticos em TypeScript.
**Tags:** arquitetura, software, enterprise, typescript, desenvolvimento
