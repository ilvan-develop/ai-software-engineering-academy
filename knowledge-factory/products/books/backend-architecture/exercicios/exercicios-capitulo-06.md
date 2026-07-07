# Exercícios — Capítulo 6: Multi-Tenant — Implementação com NestJS e Prisma

> **Progressão:** Fácil → Médio → Difícil  
> **Total:** 4 exercícios

---

## Exercício 1 — Fácil: Tenant Service

**Tema:** Serviço de gerenciamento de tenants

Crie um `TenantService` no NestJS com os seguintes métodos:

```typescript
@Injectable()
export class TenantService {
  async findById(id: string): Promise<Tenant | null> { /* ... */ }
  async findBySlug(slug: string): Promise<Tenant | null> { /* ... */ }
  async create(dto: CreateTenantDto): Promise<Tenant> { /* ... */ }
  async deactivate(id: string): Promise<void> { /* ... */ }
  async list(): Promise<Tenant[]> { /* ... */ }
}
```

Inclua validação de slug único e criação com dados iniciais.

---

## Exercício 2 — Médio: Prisma Middleware para Tenant

**Tema:** Middleware global de tenant no Prisma

Implemente um middleware Prisma que automaticamente filtra queries por `tenantId`:

```typescript
// prisma.middleware.ts
export function tenantMiddleware(prisma: PrismaClient, getTenant: () => string) {
  // Middleware que intercepta todas as queries
  // Adiciona tenantId no where de forma automática
  // Ignora a entidade Tenant (não filtrar a própria tabela de tenants)
}
```

**Requisitos:**
- Funciona para ações: findMany, findFirst, create, update, delete
- Não filtra a própria entidade `Tenant`
- Para `create`, injeta automaticamente o `tenantId`
- Deve permitir bypass explícito (ex: login entre tenants)

---

## Exercício 3 — Médio: Módulo Multi-Tenant

**Tema:** Estrutura modular para multi-tenancy

Estruture um módulo NestJS `MultiTenantModule` usando `forRoot()`:

```typescript
@Module({ /* ... */ })
export class MultiTenantModule {
  static forRoot(options: MultiTenantOptions): DynamicModule {
    // Configura providers baseados nas opções
    // Deve prover TenantService, TenantMiddleware e PrismaService com tenant
  }
}
```

**Requisitos:**
- Configurável por ambiente (qual estratégia usar)
- Provider para o PrismaService já configurado com tenant middleware
- TenantMiddleware configurado como global

---

## Exercício 4 — Difícil: Guard de Tenant

**Tema:** Verificação de acesso ao tenant

Implemente um guard `TenantGuard` que:

1. Verifica se o `tenantId` da rota corresponde ao tenant do usuário
2. Verifica se o usuário tem acesso àquele tenant (usuário pode pertencer a múltiplos tenants)
3. Admin pode acessar qualquer tenant (role-based)
4. Retorna 403 se não tiver acesso

```typescript
@Injectable()
export class TenantGuard implements CanActivate {
  constructor(
    private userTenantService: UserTenantService,
    private reflector: Reflector,
  ) {}

  canActivate(context: ExecutionContext): Promise<boolean> {
    // implementação
  }
}
```

**Uso:**
```typescript
@Controller(':tenantId/projects')
@UseGuards(TenantGuard)
export class ProjectController { /* ... */ }
```
