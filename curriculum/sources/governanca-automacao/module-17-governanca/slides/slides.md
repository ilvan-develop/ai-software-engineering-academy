# Módulo 17 — Slides

---

## Slide 1: Título

**Governança**
Código com responsabilidade

Da startup ao enterprise — o que muda?

---

## Slide 2: O que é Governança?

```
Sistema de regras, processos e práticas
que garante que a TI entregue valor
com riscos controlados.

Sem governança → caos
Com governança → previsibilidade
```

---

## Slide 3: Pilares da Governança de Software

```
┌─────────────┬───────────────┬──────────────┐
│  POLÍTICAS  │   PADRÕES     │  PROCESSOS   │
│  O que é    │   Como fazer  │  Quem faz    │
│  obrigatório│   o quê       │  e quando    │
├─────────────┼───────────────┼──────────────┤
│ Code review │ ESLint        │ CI/CD        │
│ Branch str. │ Prettier      │ Code review  │
│ Segredos    │ ADR template  │ Deploy       │
└─────────────┴───────────────┴──────────────┘
```

---

## Slide 4: Code Review

**Prática mais impactante de governança**

Gates obrigatórios:
- CI passa (lint + test + build)
- 1+ approval
- Segurança (se aplicável)
- Arquitetura (se mudança estrutural)

Checklist: solução, testes, padrões, docs, segredos?

---

## Slide 5: Template de PR

```markdown
## Descrição
## Tipo (bug / feature / breaking / refactor / docs)
## Como testar
## Checklist
  - [ ] Testes
  - [ ] Lint passa
  - [ ] Sem segredos
## Linked Issues
```

---

## Slide 6: Padrões de Código

| Ferramenta | Função |
|------------|--------|
| ESLint | Regras de código |
| Prettier | Formatação |
| EditorConfig | Configuração do editor |
| Husky | Hooks git |
| lint-staged | Lint só nos arquivos alterados |
| commitlint | Conventional Commits |

Automação > memorando

---

## Slide 7: Conventional Commits

```
feat(auth): add login com Google
fix(api): correct 404 para usuários
chore(deps): upgrade express
docs(readme): setup instructions
BREAKING CHANGE: nova API de pagamentos

Gera changelog automaticamente!
```

---

## Slide 8: Gestão de Dependências

```
Dependabot / Renovate:
  → Diário: patches (automerge)
  → Semanal: minor (automerge)
  → Mensal: major (revisão manual)

Snyk: scan de vulnerabilidades

Regra de ouro:
  CVE conhecida → atualizar em 48h
```

---

## Slide 9: Gestão de Segredos

**NUNCA commitar segredos!**

```
✓ .env.example (valores fictícios)
✓ .env no .gitignore
✓ Secrets no CI/CD (não no código)
✓ Vault / AWS Secrets Manager
✓ git-secrets (pre-commit hook)
✓ Rotação a cada 90 dias

Vazou? Rotacione IMEDIATAMENTE.
```

---

## Slide 10: Políticas de Deploy

```
Branch strategy:
  Git Flow vs Trunk-based

Rollback plan:
  → Tag da imagem atual
  → Backup de banco
  → Health check pós-deploy
  → Rollback automático se falhar
  → Monitoring por 30min
```

---

## Slide 11: ADRs — Architecture Decision Records

Documentar **decisões arquiteturais**:

```
ADR-001: PostgreSQL como banco principal
  Status: Aceito
  Contexto: Precisamos de ACID + multi-tenant
  Decisão: PostgreSQL 16
  Consequências: + maturidade, - escalabilidade horizontal
  Alternativas: MySQL, CockroachDB, MongoDB
```

---

## Slide 12: Compliance na prática

| Norma | Impacto no time de dev |
|-------|----------------------|
| **LGPD** | Não logar dados pessoais, endpoint de deleção |
| **SOC2** | Audit logs, change management, acessos |
| **ISO 27001** | Políticas documentadas, inventário, incidentes |

Compliance não é só do jurídico.

---

## Slide 13: SLAs, SLOs e SLIs

```
SLI → métrica técnica (p99 < 200ms)
SLO → meta (p99 < 200ms em 95% do mês)
SLA → compromisso contratual (crédito se falhar)

Dashboard executivo:
  🟢 Status geral
  ✅ SLOs atingidos?
  🔥 Incidentes relevantes
  📈 Tendência
```

---

## Slide 14: Auditoria e Rastreabilidade

```
Toda decisão técnica deve ser rastreável:

Issue → ADR → PR → Review → Testes → Commit

Audit logs: append-only, nunca alterar

Changelogs: automatizados com conventional commits
```

---

## Slide 15: Governança Leve

```
1. Automatize antes de burocratizar
2. Comece pequeno, evolua
3. Documente o "porquê"
4. Revise periodicamente
5. Liderança pelo exemplo

Métricas de saúde:
  → Tempo de review < 4h
  → ADR coverage > 80%
  → Dependency drift < 5%
  → Rollback rate < 2%
  → Incidentes de segredo: ZERO
```

---

## Slide 16: Para levar para casa

```
Governança não é burocracia — é responsabilidade.

Code review + padrões + ADRs + compliance
+ SLOs + auditoria = código que respeita
quem mantém, quem opera e quem usa.
```
