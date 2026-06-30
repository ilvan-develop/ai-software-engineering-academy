==================================================
TWITTER/X — Thread
==================================================

🧵 Módulo 09 - Modelagem de Dados: Prisma e PostgreSQL

Uma thread para voce dominar esse conceito.

1. Por que modelagem importa:
→ Modelagem de dados é a **fundação** do sistema. Erros aqui são os mais caros de corrigir.
→ ┌──────────────────────────────────────────┐


2. Entidades e Relacionamentos:
→ 1:1  — Um usuário tem um perfil
→ 1:N  — Um usuário tem muitos pedidos


3. Soft Delete e Audit Trail:
→ Nunca delete dados definitivamente em sistemas Enterprise.
→ id        String    @id @default(cuid())


4. Índices e Performance:
→ id         String   @id @default(cuid())
→ status     OrderStatus


5. Migrações Seguras:
→ npx prisma migrate dev --name create-user-table
→ npx prisma migrate deploy


6. Estratégias de Backup:
→ Full:     Cópia completa do banco
→ Tempo:  Lento, ocupa espaço


Curtiu? Salve e compartilhe! 🚀

#DevTips #Arquitetura
