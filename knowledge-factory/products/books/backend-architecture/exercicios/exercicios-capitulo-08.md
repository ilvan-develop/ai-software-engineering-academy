# Exercícios — Capítulo 8: Multi-Tenant — Operações e Qualidade

> **Progressão:** Fácil → Médio → Difícil  
> **Total:** 4 exercícios

---

## Exercício 1 — Fácil: Teste de Isolamento

**Tema:** Garantia de isolamento entre tenants

Escreva um teste de integração que verifique o isolamento entre tenants:

```typescript
describe('Isolamento entre Tenants', () => {
  it('deve impedir que Tenant A veja dados do Tenant B', async () => {
    // 1. Cria dois tenants com dados
    // 2. Autentica como usuário do Tenant A
    // 3. Tenta acessar um recurso do Tenant B
    // 4. Verifica que retorna 403 ou 404
  });
});
```

---

## Exercício 2 — Médio: Métricas por Tenant

**Tema:** Observabilidade e monitoramento

Implemente um interceptor que coleta métricas por tenant:

```typescript
@Injectable()
export class TenantMetricsInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    // 1. Extrai tenantId do request
    // 2. Inicia timer
    // 3. No final, registra métrica: tenant, endpoint, status, duração
    // 4. Usa counter e histogram do Prometheus
  }
}
```

**Métricas a coletar:**
- `tenant_requests_total` — contador de requisições por tenant
- `tenant_request_duration_seconds` — histograma de duração
- `tenant_errors_total` — contador de erros por tenant
- `tenant_active_users` — gauge de usuários ativos

---

## Exercício 3 — Médio: Rate Limiting por Tenant

**Tema:** Proteção de recursos por inquilino

Configure rate limiting que seja **por tenant**, não global:

```typescript
@Injectable()
export class TenantRateLimitGuard implements CanActivate {
  constructor(
    @Inject('CACHE_MANAGER') private cache: Cache,
    private reflector: Reflector,
  ) {}

  async canActivate(context: ExecutionContext): Promise<boolean> {
    // Implementa rate limit considerando tenantId + IP
    // Limites configuráveis por plano (gratuito: 100 req/min, pro: 1000 req/min)
    // Armazenamento em Redis com TTL
  }
}
```

---

## Exercício 4 — Difícil: Onboarding Automatizado de Tenant

**Tema:** Pipeline de provisionamento de novos inquilinos

Projete um sistema de onboarding automático para novos tenants que inclui:

1. **API de criação** — recebe dados do tenant e do admin
2. **Data Migration** — cria schemas, tabelas e dados iniciais
3. **Infrastructure** — provisiona recursos (se banco por tenant)
4. **Notifications** — envia email de boas-vindas com credenciais
5. **Monitoring** — configura alertas e dashboards para o novo tenant

**Tarefa:** Crie uma classe `TenantOnboardingService` que orquestra todo o pipeline:

```typescript
@Injectable()
export class TenantOnboardingService {
  async onboard(dto: OnboardTenantDto): Promise<OnboardingResult> {
    // 1. Validar dados
    // 2. Criar tenant no banco
    // 3. Provisionar infraestrutura (se necessário)
    // 4. Rodar migrations específicas
    // 5. Popular dados iniciais (seed)
    // 6. Criar usuário admin
    // 7. Configurar monitoramento
    // 8. Enviar notificação
    // 9. Retornar resultado com credenciais
  }
}
```

**Bônus:** Implemente resiliência com fila (Bull/RabbitMQ) para que o onboarding seja assíncrono e tolerante a falhas.
