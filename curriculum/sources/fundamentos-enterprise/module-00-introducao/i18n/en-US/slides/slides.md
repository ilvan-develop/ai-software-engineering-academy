<!-- i18n: en-US | source: pt-BR | generated: 2026-07-07 -->
# Módulo 00 — Slides

---

## Slide 1: Título

**A Nova Engenharia de Software**
Como a IA transformou o desenvolvimento

---

## Slide 2: O cenário antes vs. depois da IA

| Antes | Depois |
|-------|--------|
| 100% manual | Orquestração de agentes |
| Velocidade = digitação | Velocidade = clareza das instruções |
| Erros em runtime | Erros prevenidos por checklists |
| Conhecimento fragmentado | Contexto integrado no LLM |

---

## Slide 3: A virada de chave

> "O desenvolvedor do futuro não será avaliado pela quantidade de código que escreve, mas pela qualidade das decisões que toma."

Diferenciais:
1. Saber o que construir (Discovery)
2. Saber como arquitetar (Architecture)
3. Saber o que delegar (Orchestration)
4. Saber validar (Auditing)

---

## Slide 4: 63% dos desenvolvedores reportam erros

Fonte: Stack Overflow Survey 2024

- **63%** — código gerado por IA contém erros inesperados
- **40%** — retrabalho sem configuração adequada
- **~3%** — erro com **12+ regras** de projeto definidas

**Conclusão:** IA sem governança = dívida técnica acelerada

---

## Slide 5: O papel do Arquiteto

```
Antes:
• Escolher tecnologia
• Desenhar diagramas
• Revisar código

Agora (+):
• Definir regras para agentes
• Criar templates de prompt
• Configurar checklists
• Decidir o que delegar vs. reter
```

---

## Slide 6: O que NÃO delegar para a IA

1. Visão arquitetural do sistema
2. Trade-offs críticos (custo vs. performance)
3. Padrões e convenções
4. Revisão estratégica
5. Contexto de negócio

---

## Slide 7: O que DELEGAR para a IA

1. Implementação de CRUDs
2. Testes unitários
3. Documentação técnica
4. Validação de boas práticas (checklists)
5. Refatoração de código legado

---

## Slide 8: A Matriz de Delegação

```
                    Alta complexidade
                          │
    HUMANO DECIDE         │   HUMANO + AGENTE
    (o que construir)     │   (arquitetura, revisão)
                          │
──────────────────────────┼───────────────────
                          │
    AGENTE FAZ            │   AGENTE DECIDE
    (CRUD, testes)        │   (lint, formatação)
                          │
                    Baixa complexidade

                  Baixo risco      Alto risco
```

---

## Slide 9: O ciclo de desenvolvimento

```
Product Discovery → Design → Arquitetura → Modelagem
                                             ↓
                                    Implementação
                                             ↓
                              Segurança → Testes → DevOps
                                             ↓
                                    Auditoria
                                             ↓
                                    Refatoração
```

Cada etapa: agente especializado + artefato revisável

---

## Slide 10: A formação em 21 módulos

- **Módulos 0-7:** Produto, Design, Prototipação
- **Módulos 8-12:** Arquitetura, Backend, Frontend, Segurança
- **Módulos 13-17:** Multi-tenant, DevOps, QA, Observabilidade, Governança
- **Módulos 18-21:** Agentes de IA, Auditorias, Automação, Projeto Final

---

## Slide 11: Para refletir

> "A IA não vai substituir desenvolvedores. Desenvolvedores **que usam IA** vão substituir desenvolvedores **que não usam**."

Mas também:

> "Desenvolvedores que usam IA **sem governança** vão substituir desenvolvedores que usam IA **com governança**."

---

## Slide 12: Próximos passos

1. Configurar OpenCode / ambiente
2. Conhecer os agentes da formação
3. Módulo 01: Mentalidade Enterprise
