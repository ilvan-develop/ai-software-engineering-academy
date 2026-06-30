# Workflow: Prisma Expert Agent

```
1. Receber requisitos de modelagem
2. Definir entidades, relações e índices
3. Criar schema Prisma
4. Validar integridade referencial
5. Criar migration
6. Criar seed data
7. Otimizar queries críticas
8. Revisar com Database Architect Agent
```

## Padrões

### Soft Delete

```prisma
model User {
  id        String   @id @default(cuid())
  deletedAt DateTime?
}
```

### Audit Trail

```prisma
model AuditLog {
  id        String   @id @default(cuid())
  entity    String
  entityId  String
  action    String   // CREATE, UPDATE, DELETE
  changes   Json
  userId    String
  createdAt DateTime @default(now())
}
```

### Multi-Tenant

```prisma
model Organization {
  id       String  @id @default(cuid())
  tenants  Tenant[]
}
```
