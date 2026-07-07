# Agentes para o Módulo 13 — Multi-Tenant

## Agentes Envolvidos

| Agente | Função | Responsabilidades |
|--------|--------|-------------------|
| **Curriculum Architect** | Estruturar conceitos de multi-tenancy | Definir progressão pedagógica, exemplos reais, comparação entre abordagens |
| **Backend Engineer Agent** | Implementar middlewares, pools, repositórios | Código funcional NestJS/TypeScript, Prisma multi-tenant, migrations |
| **DevOps Expert Agent** | Estratégias de infraestrutura | Backup/restore, connection pooling, deploy multi-tenant, monitoring |
| **Security Analyst Agent** | Revisar isolamento e vazamento de dados | Testes de isolamento, RLS, prevenção de SQL injection cross-tenant |
| **Product Manager Agent** | Definir pricing e planos | Feature flags, limites por plano, relação isolamento × preço |
| **QA Engineer Agent** | Testar isolamento entre tenants | Testes automatizados de vazamento, concorrência, rate limit |

## Instruções Específicas

### Backend Engineer Agent

Ao escrever código para este módulo:

- **Middleware de tenant**: implementar extração de 3 fontes (JWT → Header → Subdomínio) com fallback
- **AsyncLocalStorage**: usar `AsyncLocalStorage` para propagar contexto do tenant sem poluirassinaturas de função
- **Repositórios**: toda query SQL deve incluir `WHERE tenant_id = $1` — nunca confiar no ORM para isso
- **Prisma**: mostrar duas abordagens — (a) client por schema com `schema` no datasource URL, (b) middleware `$use` para shared database com injeção automática de `tenantId`
- **Migrations**: criar script que itera sobre schemas/tenants e aplica migrations com transação e rollback individual
- **Seed**: dados iniciais ao criar tenant (admin, configurações, categorias padrão)

```typescript
// Template de código esperado
@Injectable()
export class TenantAwareService {
  constructor(
    private prisma: PrismaService,
    private tenantService: TenantService,
  ) {}

  async findUsers() {
    return this.prisma.user.findMany({
      where: { tenantId: this.tenantService.getTenantId() },
    });
  }
}
```markdown

### Security Analyst Agent

Verificar e garantir:

- **NENHUMA** query SQL pode ser executada sem filtro de `tenant_id`
- Middleware deve rejeitar requisições sem tenant identificado com 401
- JWT com claim `tid` deve ser validado em todo endpoint protegido
- Testes devem demonstrar vazamento zero entre tenants
- Implementar Row-Level Security (RLS) no PostgreSQL como camada extra de segurança
- Verificar que `tenant_id` vindo do body da requisição é IGNORADO (usar apenas o do middleware)
- Rate limiting deve ser aplicado por tenant, não global

**Checklist de segurança:**
- [ ] Middleware rejeita requisição sem tenant
- [ ] Middleware rejeita tenant inativo
- [ ] Repositório sempre usa `WHERE tenant_id`
- [ ] Insert sempre usa `tenant_id` do contexto, nunca do body
- [ ] RLS configurado para shared database
- [ ] Teste de quebra proposital do filtro

### Product Manager Agent

Ao definir o modelo de negócio:

- **Relacionar isolamento com plano de preço**: Free → Shared DB, Pro → Schema per Tenant, Enterprise → DB per Tenant
- **Feature flags**: cada plano tem um conjunto de features habilitadas (ex: Free não tem API access, Enterprise tem white label)
- **Limites técnicos**: max users, max storage, max connections — variam por plano
- **Upgrade path**: migrar tenant de Shared DB para Schema per Tenant deve ser documentado
- **Custo por tenant**: calcular quanto cada tenant custa em infraestrutura baseado no plano

```typescript
// Modelo de negócio esperado
interface PricingTier {
  name: string;
  isolationModel: 'shared' | 'schema' | 'database';
  maxUsers: number;
  maxStorageMB: number;
  pricePerMonth: number;
  features: string[];
  supportLevel: 'community' | 'email' | 'priority' | 'dedicated';
}
```markdown

### DevOps Expert Agent

Ao definir estratégias de infraestrutura:

- **Backup**: estratégia por plano — Free usa backup global, Enterprise tem backup dedicado com PITR
- **Pool**: connection pooling com limites por tenant (Free=2, Pro=10, Enterprise=25)
- **Monitoramento**: métricas por tenant (queries/s, latency, error rate, pool usage)
- **Deploy**: zero-downtime migrations para múltiplos schemas
- **Recuperação**: procedimento de restore para cada abordagem (DB per Tenant = restore individual, Shared = restore global + cleanup)

### QA Engineer Agent

Ao criar testes:

- **Vazamento zero**: teste que cria dados como Tenant A e verifica que Tenant B não enxerga
- **Concorrência**: Promise.all com 5+ tenants criando dados simultaneamente
- **Injeção**: tentar forçar tenant_id no body e verificar que é ignorado
- **Rate limit**: exceder limite de tenant Free, verificar 429
- **Feature flag**: acessar endpoint de Enterprise como Free, verificar 403
- **Quebra proposital**: fazer query sem WHERE tenant_id, verificar que retorna dados de todos (prova que o filtro é necessário)
