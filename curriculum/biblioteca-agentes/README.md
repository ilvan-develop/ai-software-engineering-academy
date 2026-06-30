# Biblioteca de Agentes

Agentes especializados pré-construídos para cada domínio da Engenharia de Software Enterprise.

## Estrutura de cada agente

```
agente/
├── README.md          → Objetivo, responsabilidades, conhecimentos
├── workflow.md        → Fluxo de trabalho passo a passo
├── checklist.md       → Checklist de validação
├── prompts/
│   ├── planejamento.md
│   ├── implementacao.md
│   └── auditoria.md
└── criterios.md       → Critérios de qualidade e entregáveis
```

## Agentes

### Produto
- `product-discovery-agent` — Discovery, canvas, roadmap
- `ux-research-agent` — Pesquisa, entrevistas, personas

### Design
- `ux-designer-agent` — User flow, arquitetura da informação
- `ui-designer-agent` — Design System, tokens, componentes

### Arquitetura
- `enterprise-architect-agent` — Clean Arch, DDD, decisões técnicas
- `database-architect-agent` — Modelagem, ERD, Prisma schema

### Desenvolvimento
- `backend-expert-agent` — NestJS, APIs, validação
- `frontend-expert-agent` — Next.js, React, Server Components
- `prisma-expert-agent` — Schema, migrations, queries

### Infraestrutura
- `devops-expert-agent` — Docker, CI/CD, Kubernetes
- `security-expert-agent` — OWASP, autenticação, autorização

### Qualidade
- `qa-expert-agent` — Testes, Playwright, Vitest
- `performance-expert-agent` — Otimização, caching, N+1

### Governança
- `auditor-agent` — 16 tipos de auditoria com score
- `documentation-agent` — ADRs, RFCs, docs
- `refactoring-agent` — Refatoração guiada por regras

---

> Cada agente é independente de ferramenta e pode ser usado no OpenCode, Claude Code, Cursor ou qualquer assistente compatível com arquivos de instrução.
