# Exercícios — Módulo 16

## Exercício 1: Logs estruturados

Converta os logs abaixo para o formato estruturado (JSON):

```typescript
// ❌ Antes
console.log('Usuário', email, 'criou pedido', orderId, 'de R$', total);
console.log('Erro ao processar pagamento:', error.message);
console.log('Login de', email, '- sucesso:', success);
```text

Formato esperado:
```typescript
logger.info('Pedido criado', {
  // ...
});
```yaml

Inclua: timestamp, userId, ip, user-agent, nível apropriado.

---

## Exercício 2: Métricas Prometheus

Implemente métricas para um módulo de **carrinho de compras**:

1. **CartController** — contar requisições e medir duração
2. **CartService** — contar itens adicionados/removidos
3. **Checkout** — contar pedidos criados por status

Use Counter, Histogram e Gauge.

```typescript
export const cartItemsAdded = new Counter({
  name: 'cart_items_added_total',
  help: 'Itens adicionados ao carrinho',
});
```markdown

---

## Exercício 3: Dashboard Grafana

Descreva um dashboard Grafana para um SaaS de e-commerce com:

1. **Row 1: Visão geral** — req/s, error rate, p95 latency, uptime
2. **Row 2: Por endpoint** — latência por rota, erros por rota
3. **Row 3: Banco de dados** — conexões ativas, query duration, slow queries
4. **Row 4: Negócio** — pedidos/hora, receita/hora, usuários ativos
5. **Row 5: Sistema** — CPU, memória, disco

Para cada painel, especifique:
- Tipo de gráfico (time series, stat, bar gauge, table)
- Query PromQL
- Threshold (se aplicável)

Exemplo:
```yaml
Painel: Request Rate
Tipo: Time series
Query: rate(http_requests_total[5m])
Threshold: warning > 1000, critical > 2000
```markdown

---

## Exercício 4: Criando spans

Adicione tracing com OpenTelemetry ao service abaixo:

```typescript
class PaymentService {
  async processPayment(orderId: string, amount: number): Promise<PaymentResult> {
    const payment = await this.createPaymentGatewayRecord(orderId, amount);
    const gatewayResult = await this.gateway.charge(payment);
    await this.updateOrderStatus(orderId, gatewayResult.status);
    await this.sendNotification(orderId, gatewayResult.status);
    return gatewayResult;
  }
}
```text

Crie spans para:
- `processPayment` — span principal
- `createPaymentGatewayRecord` — sub-span
- `gateway.charge` — sub-span (pode ser lento)
- `sendNotification` — sub-span

Inclua atributos relevantes (orderId, amount, gateway).

---

## Exercício 5: Configuração de alertas

Crie alertas Prometheus para:

1. **Alta taxa de erro** — error rate > 3% por 5 minutos
2. **Latência alta** — p95 > 1.5s por 5 minutos
3. **Queda de tráfego** — req/s caiu 50% em 5 minutos (possível outage)
4. **Muitas queries lentas** — db_query_duration > 500ms em mais de 10% das queries
5. **Disco cheio** — disk usage > 85%

Para cada alerta:
- Severidade (critical/warning)
- Expressão PromQL
- Tempo de avaliação
- Mensagem de notificação
- Canal de notificação (Slack, email, PagerDuty)
