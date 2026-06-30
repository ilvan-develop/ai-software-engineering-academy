---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 19 — Auditorias

## Módulo 19 - Auditorias

---
## 1. Por que auditoria é o diferencial

- A maioria dos cursos ensina a **construir** software. Quase nenhum ensina a **avaliar** a qualidade do que foi constr...
- Cursos tradicionais:
- ┌────────────────────────────────────────────┐
- │  Construir  │  Testar  │  Deploy  │  Fim   │
- └────────────────────────────────────────────┘
- Nota: sem métrica de qualidade

---
## 2. O sistema de score (0-10)

- Cada auditoria produz um **score quantitativo** que permite comparar qualidade entre versões e módulos.
- | Score | Significado | Ação |
- |-------|-------------|------|
- | 9-10 | Excelente | Manutenção preventiva |
- | 7-8 | Bom | Correções opcionais menores |

---
## 3. Os 16 tipos de auditoria

- ┌───────────────────────────────────────────────────────────────┐
- │                     AUDITORIAS TÉCNICAS                        │
- ├───────────┬────────────┬───────────┬──────────┬──────────────┤
- │Arquitetura│ Segurança  │ Frontend  │ Backend  │ UX           │
- │Clean Arch │ OWASP      │ Next.js   │ NestJS   │ Heurísticas  │
- │DDD        │ Top 10     │ RSC       │ DDD      │ Jornada      │

---
## 4. Estrutura de cada auditoria

- Score geral:** [0-10]
- Riscos:** [Qtd] (Blocker: X, Critical: Y, Major: Z, Minor: W)
- Data:** [data]
- Auditor:** [agente responsável]

---
## Resumo Executivo

- [3-5 frases]

---
## Resultados por Dimensão

- | Dimensão | Score | Riscos | Observação |
- |----------|-------|--------|------------|
- | ...      | ...   | ...    | ...        |

---
## Riscos Identificados

- Localização:** arquivo:linha
- Descrição:** o que está errado
- Impacto:** o que pode acontecer
- Correção:** como corrigir
- Dependência:** precisa de outra correção antes?

---
## Plano de Ação

- | Prioridade | Ação | Responsável | Prazo | Esforço |
- |------------|------|-------------|-------|---------|
- | P0         | ...  | ...         | ...   | ...     |

---
## Recomendações

- [Melhorias opcionais para atingir score 10]
- | Gravidade | Definição | Prazo de correção |
- |-----------|-----------|-------------------|
- | **Blocker** | Impede deploy ou quebra funcionalidade crítica | Imediato |
- | **Critical** | Vulnerabilidade grave ou perda de dados | 24h |

---
## 5. Exemplo: Auditoria de Segurança

- Score geral:** 5.8/10
- Riscos:** 8 (2 Critical, 3 Major, 3 Minor)
- Data:** 2025-06-01
- Auditor:** Security Expert Agent

---
## Resumo Executivo

- A API de pagamentos apresenta 2 riscos críticos que impedem
- o deploy em produção: senhas armazenadas com MD5 e falta de
- rate limiting no endpoint de login. Recomenda-se corrigir
- estes itens antes de qualquer release.

---
## Exemplo: text

```text
Cursos tradicionais:
  ┌────────────────────────────────────────────┐
  │  Construir  │  Testar  │  Deploy  │  Fim   │
  └────────────────────────────────────────────┘
  Nota: sem métrica de qualidade

Esta formação:
  ┌────────────────────────────────────────────┐
  │  Construir  │  Testar  │  AUDITAR  │  OK   │
  └────────────────────────────────────────────┘
  Nota: score 0-10 com riscos classificados
```

---
## Exemplo: text

```text
Score = (∑ scores por dimensão) / número de dimensões

Cada dimensão = 0-10 baseado em:
  40% checklists automatizados
  30% análise estática (lint, types, cobertura)
  30% análise qualitativa do auditor
```

---
## Recap

- 1. Por que auditoria é o diferencial
- 2. O sistema de score (0-10)
- 3. Os 16 tipos de auditoria
- 4. Estrutura de cada auditoria
- Resumo Executivo
- Resultados por Dimensão
- Riscos Identificados
- Plano de Ação
- Recomendações
- 5. Exemplo: Auditoria de Segurança
- Resumo Executivo

---
# Obrigado!

## Perguntas?
