# Exercícios — Módulo 17

## Exercício 1: Configuração de Padrões de Código

Crie a configuração completa de padrões de código para um projeto TypeScript/Node.js com:

- ESLint com regras enterprise (no-unused-vars como erro, no-console como warn)
- Prettier (single quote, trailing comma, printWidth 100)
- EditorConfig (espaços, 2 espaços, UTF-8, LF)
- Husky com pre-commit hook rodando lint-staged
- commitlint com conventional commits
- lint-staged para formatar e fazer lint de arquivos .ts e .tsx

Escreva todos os arquivos de configuração necessários.

---

## Exercício 2: Template de PR e ADR

Crie dois templates para o repositório:

**a) Template de Pull Request** (`.github/PULL_REQUEST_TEMPLATE.md`)
- Descrição, tipo de mudança, como testar, checklist, screenshots, linked issues

**b) Architecture Decision Record** (`docs/adr/ADR-002-usar-redis-para-cache.md`)
- Contexto: API tem 500ms de resposta, precisa reduzir para < 100ms
- Decisão: Redis com TTL de 5 minutos
- Consequências: + performance, - consistência em tempo real
- Alternativas: cache em memória, CDN, banco de dados materializado

---

## Exercício 3: Política de Deploy

Você é o tech lead de um time que faz deploy toda semana. Desenhe:

1. **Branch strategy** — Git Flow ou Trunk-based? Justifique.
2. **Gates do pipeline** — O que precisa passar antes de ir para produção?
3. **Rollback plan** — Passo a passo do que fazer se o deploy quebrar produção.
4. **Health checks** — O que verificar pós-deploy?

Escreva como um documento de política (`DEPLOY_POLICY.md`).

---

## Exercício 4: Auditoria e LGPD

Implemente um sistema de audit log para uma aplicação que lida com dados de usuários:

```typescript
interface AuditEntry {
  id: string;
  timestamp: Date;
  userId: string;
  action: 'CREATE' | 'UPDATE' | 'DELETE' | 'READ';
  resource: string;
  resourceId: string;
  previousValue?: unknown;
  newValue?: unknown;
  ipAddress?: string;
}
```sql

**Requisitos:**
- Função `createAuditLog` que salva no banco (append-only)
- Endpoint de deleção de conta que também audita a exclusão
- Comentário explicando por que audit logs nunca devem ser alterados ou excluídos
- Garantir que dados sensíveis (CPF, email) NÃO apareçam nos logs

---

## Exercício 5: SLOs para uma API de Pagamentos

Defina SLIs e SLOs para uma API de processamento de pagamentos:

**Requisitos de negócio:**
- Clientes esperam pagamento em < 5 segundos
- Disponibilidade: faturamento depende de estar online 24/7
- Precisão: nunca cobrar duas vezes o mesmo cliente
- Compliance: LGPD + PCI-DSS

**Entregue:**
1. 3 SLIs com suas métricas e janelas de medição
2. 3 SLOs baseados nos SLIs
3. Um SLA proposto (com consequências para o cliente e para o time)
4. Um dashboard de saúde com cores (🟢/🟡/🔴) e thresholds
