# Módulo 19 — Slides

---

## Slide 1: Título

**Auditorias**
Como medir, pontuar e melhorar a qualidade de sistemas Enterprise

---

## Slide 2: Por que auditoria é o diferencial

```text
Cursos tradicionais:
  Construir → Testar → Deploy → (sem métrica)

Esta formação:
  Construir → Testar → AUDITAR → Score 0-10
```markdown

> Única formação que ensina a **avaliar** a qualidade com métricas quantitativas

---

## Slide 3: O sistema de score

| Score | Significado | Ação |
|-------|-------------|------|
| 9-10 | Excelente | Manutenção preventiva |
| 7-8 | Bom | Correções opcionais |
| 5-6 | Regular | Correções necessárias |
| 3-4 | Ruim | Correções urgentes |
| 0-2 | Crítico | Parar e corrigir |

---

## Slide 4: As 16 auditorias (visão geral)

```text
Arquitetura   Segurança   Frontend    Backend     UX
UI            Banco       APIs        Performance DevOps
Governança    Multi-Ten.  Código      Deps.       TypeScript
```text

6 obrigatórias antes de deploy
4 recomendadas a cada release
5 periódicas a cada trimestre

---

## Slide 5: Estrutura de uma auditoria

```yaml
Score geral: 0-10
Riscos: X Blocker, Y Critical, Z Major, W Minor

1. Resumo Executivo
2. Resultados por Dimensão (tabela)
3. Riscos Identificados (com localização)
4. Plano de Ação (com prazos)
5. Recomendações
```markdown

---

## Slide 6: Classificação de riscos

| Gravidade | Definição | Prazo |
|-----------|-----------|-------|
| **Blocker** | Impede deploy | Imediato |
| **Critical** | Vulnerabilidade grave | 24h |
| **Major** | Risco moderado | 1 semana |
| **Minor** | Sugestão de melhoria | Agenda |

---

## Slide 7: Exemplo — Auditoria de Segurança

```yaml
Score: 5.8/10 — 2 Critical, 3 Major, 3 Minor

[Critical] Senhas com MD5
  → arquivo: src/auth/password.service.ts:15
  → Correção: bcrypt salt rounds 12

[Critical] Sem rate limiting no login
  → arquivo: src/auth/auth.controller.ts:22
  → Correção: @Throttle(5, 60)
```markdown

---

## Slide 8: Ciclo contínuo

```bash
A cada PR:
  lint → npm audit → cobertura

A cada release:
  Auditoria segurança + performance + score

A cada trimestre:
  Arquitetura + governança + dependências
  Relatório executivo para stakeholders
```markdown

---

## Slide 9: Ferramentas de automação

| Tipo | Ferramenta |
|------|-----------|
| Código | ESLint, Prettier |
| Tipos | TypeScript strict |
| Segurança | npm audit, Snyk |
| Performance | Lighthouse CI |
| API | OpenAPI diff |
| Deps | Renovate, Dependabot |

---

## Slide 10: Para cada score

```yaml
0-4: ⚠️ Pare, corrija blocker/critical, não faça deploy
5-6: 📋 Planeje correções, priorize riscos altos
7-8: ✅ Deploy autorizado, corrija no ciclo normal
9-10: 🏆 Referência, compartilhe práticas
```markdown

---

## Slide 11: Auditoria com agentes

```text
@auditor auditar-seguranca src/pagamentos/
@auditor auditar-performance src/app/page.tsx
@auditor auditar-arquitetura . --format relatorio
```yaml

Pipeline:
```text
Implementação → QA → Auditor → Correção → Re-audita → Deploy
```markdown

---

## Slide 12: Para refletir

> "O que não é medido não pode ser melhorado."

> "Score 7 é o novo 10 — porque você sabe exatamente onde está e para onde ir."

> "A auditoria não é para punir. É para dar visibilidade."
