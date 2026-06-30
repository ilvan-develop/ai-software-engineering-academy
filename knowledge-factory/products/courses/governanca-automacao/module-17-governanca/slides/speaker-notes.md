## Introducao

# Módulo 17 — Governança
**Código com responsabilidade.**
---

---
## 1. O que é Governança de TI

Governança de TI é o **sistema de regras, processos e práticas** que garante que a área de tecnologia entregue valor alinhado aos objetivos do negócio, com riscos controlados e recursos otimizados.
### Por que governança importa
Sem governança:
→ Cada time faz do seu jeito
→ Código sem padrão, difícil de manter
→ Segredos vazam para o repositório
→ Deploy é um evento estressante
→ Ninguém sabe por que uma decisão foi tomada

---
## 2. Governança de Software

Governança de software é a aplicação prática dos princípios de governança no **ciclo de vida do software**: desde a concepção até a produção.
### Pilares da governança de software
┌─────────────────────────────────────────────┐
│         GOVERNANÇA DE SOFTWARE              │
├─────────────┬───────────────┬───────────────┤
│  POLÍTICAS  │   PADRÕES     │   PROCESSOS   │
│  O que é    │   Como fazer  │   Quem faz    │
│  obrigatório│   o quê       │   e quando    │

---
## 3. Code Review

Code review é a **prática mais impactante** de governança de código. Mais do que encontrar bugs, é um processo de **transferência de conhecimento e garantia de qualidade**.
### Políticas de Code Review
Obrigatório para todo PR que:
→ Altere lógica de negócio
→ Adicione ou remova dependências
→ Modifique APIs públicas
→ Altere configurações de infraestrutura
→ Mexa em banco de dados (migrations)

---
## Descrição

<!-- O que este PR faz? Por quê? -->

---
## Tipo de mudança

- [ ] Bug fix
- [ ] Nova feature
- [ ] Breaking change
- [ ] Refatoração
- [ ] Documentação

---
## Como testar

1. `npm run dev`
2. Acesse `/rota`
3. Verifique que [comportamento esperado]

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

Closes #123
---

---
## 4. Padrões de Código

Padrões de código são **regras automatizadas** que garantem consistência sem depender de vontade individual.
### ESLint
// .eslintrc.json — Configuração enterprise
{
"env": {
"es2022": true,
"node": true
},

---
## 5. Gestão de Dependências

Dependências desatualizadas são uma das **maiores fontes de vulnerabilidade** em software enterprise.
### Ferramentas
| Ferramenta | O que faz | Quando usar |
|------------|-----------|-------------|
| **Dependabot** | PRs automáticos de atualização | GitHub nativo, projetos pequenos/médios |
| **Renovate** | Configurável, agenda, grouping | Projetos médios/grandes, times maduros |
| **Snyk** | Scan de vulnerabilidades + monitoramento | Compliance, relatórios de segurança |
| **npm audit / yarn audit** | Scan local de vulnerabilidades | Todo projeto, todo CI |

---
## 6. Gestão de Segredos

**Nunca, jamais, em hipótese alguma commitar segredos no repositório.** É a regra mais importante da governança.
### Práticas essenciais
✓ .env.example com valores fictícios (NUNCA reais)
✓ .env no .gitignore (sempre)
✓ Variáveis de ambiente em secrets do CI/CD
✓ Gestão centralizada: Vault (HashiCorp), AWS Secrets Manager, Azure Key Vault
✓ Rotação periódica de chaves (90 dias recomendado)
### .env.example

---
## 7. Políticas de Deploy

Deploy não é um evento — é um **processo** com gates, validações e rollback.
### Branch Strategy
Git Flow (projetos com releases versionadas):
main ──────┬──────────────────┬───────────
│  release/v1.0   │  hotfix
develop ───┼──────┬───────────┼────┬──────
│      │           │    │
feature/* ─┘──────┘           ┘────┘

---
## 8. Documentação de Arquitetura — ADRs

Architecture Decision Records (ADRs) documentam **decisões arquiteturais importantes** e seu contexto.
### Template de ADR
# ADR-{número}: {Título conciso}

---
## Status

- [ ] Proposto
- [ ] Aceito
- [ ] Depreciado
- [ ] Substituído por ADR-{número}

---
## Contexto

<!-- Por que essa decisão é necessária? Qual problema estamos resolvendo? -->

---
## Decisão

<!-- Qual foi a decisão tomada? -->

---
## Consequências

<!-- Positivas e negativas. O que ganhamos e o que sacrificamos? -->

---
## Alternativas consideradas

<!-- Quais outras opções foram avaliadas e por que foram descartadas? -->

---
## Referências

<!-- Links para docs, RFCs, outras ADRs -->
### Exemplo de ADR
# ADR-001: Usar PostgreSQL como banco principal

---
## Status: Aceito



---
## Contexto

Precisamos de um banco de dados relacional para o novo SaaS de gestão de projetos.
Requisitos: transações ACID, schemas multi-tenant, queries complexas de relatório.

---
## Decisão

Adotar PostgreSQL 16 como banco de dados principal.

---
## Consequências

- Positivas:成熟, boa documentação, suporte a JSONB, extensões, comunidade grande
- Negativas: escalabilidade vertical é o limite (sharding é complexo), custo de operação
- Sacrifício: não teremos escalabilidade horizontal nativa (vs. CockroachDB)

---
## Alternativas consideradas

- MySQL 8: similar, mas menos suporte a tipos avançados e extensões
- CockroachDB: escalabilidade horizontal excelente, mas maior complexidade operacional
- MongoDB: não atende requisitos de transações ACID multi-documento

---
## Referências

- https://www.postgresql.org/docs/16/index.html
### RFCs vs ADRs
ADR: Documenta uma decisão já tomada (ou em votação)
→ Tamanho: 1 página
→ Quando: após a decisão
→ Público: time de desenvolvimento
RFC: Proposta aberta para discussão
→ Tamanho: 2-5 páginas

---
## 9. Compliance

Compliance não é só coisa do jurídico — **impacta diretamente o time de desenvolvimento**.
### LGPD (Lei Geral de Proteção de Dados)
O que o time de dev precisa saber:
→ Dados pessoais não podem ser logados
→ Exclusão lógica não é suficiente: usuário pode solicitar exclusão real
→ Consentimento deve ser registrado (com timestamp)
→ Anonimização de dados em ambientes não-produção
→ Criptografia em repouso e em trânsito

---
## 10. SLAs, SLOs e SLIs

Métricas que **traduzem qualidade técnica em linguagem de negócio**.
### Definições
SLI (Service Level Indicator): métrica técnica
→ Latência p99 < 200ms
→ Error rate < 0.1%
→ Uptime > 99.9%
SLO (Service Level Objective): meta baseada no SLI
→ "Vamos entregar p99 < 200ms em 95% do tempo no mês"

---
## 11. Auditoria de Código

Auditoria não é caça às bruxas — é **rastreabilidade e transparência**.
### Logs de acesso
// Exemplo: audit log em uma operação crítica
interface AuditEntry {
id: string;
timestamp: Date;
userId: string;
action: 'CREATE' | 'UPDATE' | 'DELETE' | 'READ';

---
## 12. Governança em Equipes

O maior erro de governança é criar **burocracia que paralisa o time**. Governança efetiva é leve, automatizada e cultural.
### Princípios de governança leve
1. Automatize antes de burocratizar
→ Code review manual é caro; lint/pre-commit é grátis
→ Se pode ser automatizado, automatize
2. Comece pequeno, evolua
→ Não implemente 12 processos de uma vez
→ Comece com code review + lint, depois adicione ADRs, depois SLAs

---
## Resumo

Governança não é burocracia — é responsabilidade.
O que levar para o dia a dia:
→ Code review com checklist e approval gates
→ ESLint + Prettier + Husky (automação > memorando)
→ .env.example e git secrets (segurança por padrão)
→ ADRs para decisões importantes
→ Dependências sempre atualizadas
→ Deploy com rollback testado

---
