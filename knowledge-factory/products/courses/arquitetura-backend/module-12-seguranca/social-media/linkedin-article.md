# Módulo 12 - Segurança

---

## 1. Por que segurança é o requisito mais importante

Segurança não é uma feature — é um **pré-requisito**. Um sistema inseguro é um passivo, não um ativo.
### O custo de uma falha de segurança
Falha de segurança típica:
┌──────────────────────────────────────────────┐

## 2. OWASP Top 10 (2021)

As 10 vulnerabilidades mais críticas em aplicações web.
### 1. Broken Access Control
> Usuário acessa recursos que não deveria.
// ❌ Ruim: Não verifica se o recurso pertence ao usuário

## 3. Autenticação com JWT

### Fluxo completo
1. Usuário envia email + senha
2. Servidor valida credenciais
3. Servidor gera ACCESS TOKEN (15min) + REFRESH TOKEN (7d)

## 4. Autorização com CASL (RBAC)

### Definição de abilities
// abilities.ts
export type Action = 'manage' | 'create' | 'read' | 'update' | 'delete';
export type Subject = 'User' | 'Order' | 'Product' | 'Report' | 'all';

## 5. Rate Limiting

Protege contra brute force, DDoS e abuso.
### Implementação com @nestjs/throttler
// app.module.ts
@Module({

## 6. Headers de Segurança (Helmet + CSP)

### Helmet (NestJS)
import helmet from 'helmet';
app.use(helmet());
// Configura automaticamente:

---
*Este artigo faz parte da formacao Arquitetura de Software Enterprise com IA*