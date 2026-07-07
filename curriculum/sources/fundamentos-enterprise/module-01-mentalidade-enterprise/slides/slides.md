# Módulo 01 — Slides

---

## Slide 1: Título

**Mentalidade Enterprise**
Como empresas de verdade desenvolvem software

---

## Slide 2: O que é software Enterprise?

- Construído para **organizações**, não indivíduos
- Multi-usuário, multi-tenant, seguro, auditável

| Consumo | Enterprise |
|---------|------------|
| Um usuário | Milhares de usuários |
| "Funcionou no meu PC" | Múltiplos ambientes |
| Compliance: nenhum | Compliance: LGPD, SOC2 |

---

## Slide 3: Escalabilidade

**Manter performance sob crescimento**

```yaml
Vertical (↑):         Horizontal (→):
CPU: 4→16 cores      1→10 servidores
RAM: 8→64 GB         Load balancer
Limite: hardware      Limite: estado
```yaml

Anti-padrões:
- Banco como broker de mensagens
- N+1 queries
- Session in-process
- Arquivos no servidor

---

## Slide 4: Governança

```text
┌──────────────────────────────────┐
│           GOVERNANÇA              │
├────────────┬──────────┬──────────┤
│  Código    │ Processo │ Dados    │
│  strict    │ ADRs     │ Migrações│
│  lint      │ CI/CD    │ Audit    │
│  padrões   │ Review   │ Backup   │
└────────────┴──────────┴──────────┘
```markdown

---

## Slide 5: Manutenibilidade

| Sem | Com |
|-----|-----|
| Feature: 2 semanas | Feature: 2 dias |
| Bug: 3 dias | Bug: 2 horas |
| Onboarding: 2 meses | Onboarding: 1 semana |
| Refatorar: "reescrever" | Refatorar: 2 dias |

**Como garantir:**
1. Código limpo
2. Testes
3. Documentação
4. Modularização
5. Padronização

---

## Slide 6: Observabilidade — 3 pilares

```text
LOGS          MÉTRICAS         TRACING
"Usuário X    req/s            A → B → C
fez Y"        p95 latency      (requisição)
              error rate
```text

Sem observabilidade:
- "O sistema está lento" (mas onde?)
- "Deu erro" (mas qual? onde? quando?)

---

## Slide 7: Segurança em camadas

```text
Camada 1: Código     → input validation, ORM
Camada 2: Auth       → JWT, OAuth2, MFA
Camada 3: Autorização → RBAC, CASL
Camada 4: Rede       → HTTPS, CORS, CSP
Camada 5: Infra      → Secrets, backup
```markdown

> Segurança é parte da definição de "pronto"

---

## Slide 8: Compliance — LGPD

1. Consentimento
2. Finalidade específica
3. Minimização de dados
4. Transparência
5. Segurança
6. Direitos do titular
7. Registro de tratamento

---

## Slide 9: Multi-tenant

| Estratégia | Isolamento | Custo |
|------------|------------|-------|
| DB per Tenant | Máximo | $$$$$ |
| Schema per Tenant | Alto | $$$ |
| Row-Level Security | Médio | $ |

---

## Slide 10: Alta disponibilidade

```text
99%     → 3.65 dias/ano (sistemas internos)
99.9%   → 8.76 horas/ano (SaaS padrão)
99.99%  → 52 min/ano (Enterprise crítico)
99.999% → 5 min/ano (missão crítica)
```text

**Estratégias:**
- Sem ponto único de falha
- Redundância
- Recuperação automática

---

## Slide 11: O mindset Enterprise

```text
Desenvolvedor Júnior:         Arquiteto Enterprise:
"Funciona no meu PC"          "Funciona em produção"
"Depois a gente otimiza"      "Performance é requisito"
"Segurança é do DevOps"       "Segurança é de todos"
"Teste é opcional"            "Teste é investimento"
"Documentação?"}              "Código + Docs = verdade"
```markdown

---

## Slide 12: Para refletir

> "Software Enterprise não é sobre código que funciona. É sobre código que **continua funcionando** quando 10.000 usuários estão usando, quando alguém tenta invadir, quando o banco cai, quando um dado precisa ser auditado."
