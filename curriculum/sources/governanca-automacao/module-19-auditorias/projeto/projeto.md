# Projeto Módulo 19 — Auditoria Completa de um Sistema

## Objetivo

Realizar uma auditoria completa em um sistema real (ou simulado), gerando relatório, score, riscos e plano de ação.

## Contexto

Você recebeu o código de um **SaaS de Gestão de Tarefas** que está prestes a ser lançado. O time precisa de uma auditoria completa antes do deploy.

O sistema tem:
- Next.js 14 (frontend)
- NestJS (backend)
- Prisma + PostgreSQL
- Docker
- JWT authentication
- 5 endpoints: CRUD de tarefas + login
- 3 componentes: formulário, lista, dashboard

## Entregáveis

### 1. Relatório Consolidado

Execute as seguintes auditorias e consolide em um relatório único:

**Obrigatórias:**
- Segurança
- Código
- APIs
- TypeScript
- Performance

**Recomendadas (se tempo):**
- Arquitetura
- Banco de Dados
- DevOps

### 2. Score Geral

Calcule o score geral a partir das notas de cada auditoria.

### 3. Riscos por Prioridade

Liste todos os riscos encontrados, classificados e organizados por prioridade.

### 4. Plano de Ação

Crie um plano de ação com:
- Correções para riscos Blocker e Critical (prazo: imediato/24h)
- Correções para riscos Major (prazo: 1 sprint)
- Melhorias para riscos Minor (prazo: backlog)

### 5. Recomendações

3 recomendações estratégicas para o time melhorar o score na próxima auditoria.

## Formato

```markdown
# Auditoria Consolidada: SaaS Gestão de Tarefas

## Score Geral: [X.X]/10

| Auditoria | Score | Riscos |
|-----------|-------|--------|
| Segurança | ...   | ...    |
| Código    | ...   | ...    |
| APIs      | ...   | ...    |
| TypeScript| ...   | ...    |
| Performance| ...  | ...    |

## Riscos Blocker/Critical (agora!)
...

## Plano de Ação
...

## Recomendações
...
```

## Critérios de avaliação

- [ ] Mínimo 5 tipos de auditoria executados
- [ ] Score calculado e justificado
- [ ] Riscos classificados corretamente (Blocker a Minor)
- [ ] Plano de ação com prazos realistas
- [ ] Relatório no formato padronizado
- [ ] Recomendações acionáveis
