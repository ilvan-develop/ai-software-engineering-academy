---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 17 — Governança

## Módulo 17 - Governança

---
## 1. O que é Governança de TI

- Governança de TI é o **sistema de regras, processos e práticas** que garante que a área de tecnologia entregue valor ...
- Sem governança:
- → Cada time faz do seu jeito
- → Código sem padrão, difícil de manter
- → Segredos vazam para o repositório

---
## 2. Governança de Software

- Governança de software é a aplicação prática dos princípios de governança no **ciclo de vida do software**: desde a c...
- ┌─────────────────────────────────────────────┐
- │         GOVERNANÇA DE SOFTWARE              │
- ├─────────────┬───────────────┬───────────────┤
- │  POLÍTICAS  │   PADRÕES     │   PROCESSOS   │

---
## 3. Code Review

- Code review é a **prática mais impactante** de governança de código. Mais do que encontrar bugs, é um processo de **t...
- Obrigatório para todo PR que:
- → Altere lógica de negócio
- → Adicione ou remova dependências
- → Modifique APIs públicas

---
## Descrição

- <!-- O que este PR faz? Por quê? -->

---
## Tipo de mudança

- [ ] Bug fix
- [ ] Nova feature
- [ ] Breaking change
- [ ] Refatoração
- [ ] Documentação

---
## Como testar

- 1. `npm run dev`
- 2. Acesse `/rota`
- 3. Verifique que [comportamento esperado]

---
## Checklist

- [ ] Testes unitários/integração
- [ ] Testes manuais realizados
- [ ] Lint passa (`npm run lint`)
- [ ] Documentação atualizada
- [ ] Nenhum segredo vazou

---
## Screenshots (se aplicável)


---
## Linked Issues

- Closes #123
- 

---
## 4. Padrões de Código

- Padrões de código são **regras automatizadas** que garantem consistência sem depender de vontade individual.
- // .eslintrc.json — Configuração enterprise
- {
- "env": {
- "es2022": true,

---
## 5. Gestão de Dependências

- Dependências desatualizadas são uma das **maiores fontes de vulnerabilidade** em software enterprise.
- | Ferramenta | O que faz | Quando usar |
- |------------|-----------|-------------|
- | **Dependabot** | PRs automáticos de atualização | GitHub nativo, projetos pequenos/médios |
- | **Renovate** | Configurável, agenda, grouping | Projetos médios/grandes, times maduros |

---
## Exemplo: text

```text
Sem governança:
  → Cada time faz do seu jeito
  → Código sem padrão, difícil de manter
  → Segredos vazam para o repositório
  → Deploy é um evento estressante
  → Ninguém sabe por que uma decisão foi tomada
  → Auditoria vira um pesadelo

Com governança:
  → Padrões claros, código consistente
  → Segurança por padrão
  → Deploy previsível e seguro
  → Decisões documentadas e rastreáveis
  → Auditoria tranquila
```

---
## Exemplo: text

```text
┌─────────────────────────────────────────────┐
│         GOVERNANÇA DE SOFTWARE              │
├─────────────┬───────────────┬───────────────┤
│  POLÍTICAS  │   PADRÕES     │   PROCESSOS   │
│  O que é    │   Como fazer  │   Quem faz    │
│  obrigatório│   o quê       │   e quando    │
├─────────────┼───────────────┼───────────────┤
│ - Code      │ - ESLint/     │ - Code review │
│   review    │   Prettier    │   workflow    │
│ - Branch    │ - Commit      │ - Deploy      │
│   strategy  │   conventions │   pipeline    │
│ - Segredos  │ - ADR         │ - Auditoria   │
│   nunca no  │   template    │   periódica   │
│   reposit.  │               │               │
└─────────────┴───────────────┴───────────────┘
```

---
## Recap

- 1. O que é Governança de TI
- 2. Governança de Software
- 3. Code Review
- Descrição
- Tipo de mudança
- Como testar
- Checklist
- Screenshots (se aplicável)
- Linked Issues
- 4. Padrões de Código
- 5. Gestão de Dependências

---
# Obrigado!

## Perguntas?
