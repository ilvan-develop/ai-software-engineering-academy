# Módulo 09 - Modelagem de Dados: Prisma e PostgreSQL

---

## 1. Por que modelagem importa

Modelagem de dados é a **fundação** do sistema. Erros aqui são os mais caros de corrigir.
### O custo de uma modelagem ruim
Modelagem ruim:
┌──────────────────────────────────────────┐

## 2. Entidades e Relacionamentos

### Tipos de Relacionamento
1:1  — Um usuário tem um perfil
1:N  — Um usuário tem muitos pedidos
N:M  — Um produto está em muitas categorias

## 3. Soft Delete e Audit Trail

### Soft Delete
Nunca delete dados definitivamente em sistemas Enterprise.
model User {
id        String    @id @default(cuid())

## 4. Índices e Performance

### Quando criar índices
model Order {
id         String   @id @default(cuid())
userId     String

## 5. Migrações Seguras

### Criando migrações
# Criar migration baseada no schema
npx prisma migrate dev --name create-user-table
# Aplicar em produção

## 6. Estratégias de Backup

### Tipos de backup
Full:     Cópia completa do banco
Quando: Diário
Tempo:  Lento, ocupa espaço

---
*Este artigo faz parte da formacao Arquitetura de Software Enterprise com IA*