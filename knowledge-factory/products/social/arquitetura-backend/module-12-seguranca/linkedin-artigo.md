==================================================
LINKEDIN — Artigo
==================================================

Titulo: Módulo 12 - Segurança: O Que Todo Arquiteto Deveria Saber


## 1. Por que segurança é o requisito mais importante

- Segurança não é uma feature — é um **pré-requisito**. Um sistema inseguro é um passivo, não um ativo.
- Falha de segurança típica:
- ┌──────────────────────────────────────────────┐

## 2. OWASP Top 10 (2021)

- As 10 vulnerabilidades mais críticas em aplicações web.
- > Usuário acessa recursos que não deveria.
- // ❌ Ruim: Não verifica se o recurso pertence ao usuário

## 3. Autenticação com JWT

- 1. Usuário envia email + senha
- 2. Servidor valida credenciais
- 3. Servidor gera ACCESS TOKEN (15min) + REFRESH TOKEN (7d)

## 4. Autorização com CASL (RBAC)

- export type Action = 'manage' | 'create' | 'read' | 'update' | 'delete';
- export type Subject = 'User' | 'Order' | 'Product' | 'Report' | 'all';
- export function defineAbilitiesFor(user: User): PureAbility {

## 5. Rate Limiting

- Protege contra brute force, DDoS e abuso.
- ThrottlerModule.forRoot([{
- ttl: 60000,      // 1 minuto


---

🔥 Gostou? Compartilhe e marque alguem que precisa ler isso.

#ArquiteturaDeSoftware #EngenhariaDeSoftware #CarreiraDev
