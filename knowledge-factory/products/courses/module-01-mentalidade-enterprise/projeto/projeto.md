# Módulo 01 — Mentalidade Enterprise

**Como empresas de verdade desenvolvem software.**

---

## 1. O que é software Enterprise?

Software Enterprise é aquele construído para **organizações**, não para indivíduos.

### Características

| Característica | Exemplo de problema se ignorada |
|----------------|-------------------------------|
| **Multi-usuário** | Dois usuários editam o mesmo registro e um perde as alterações |
| **Multi-tenant** | Cliente A vê dados do Cliente B |
| **Segurança** | Dado sensível exposto por falta de autorização |
| **Auditabilidade** | Não é possível rastrear quem fez o quê |
| **Disponibilidade** | Sistema fora do ar em horário comercial |
| **Performance** | Relatório leva 5 minutos para carregar |

### Diferença entre software de consumo e Enterprise

```
Software de Consumo:                Software Enterprise:
- Um usuário                        - Centenas/milhares de usuários
- Dados isolados                    - Dados compartilhados com permissões
- "Funcionou no meu PC"             - Funciona em múltiplos ambientes
- Atualização quando quiser         - Atualização com rollback e migração
- Suporte via chat                  - SLA definido contratualmente
- Compliance: nenhum                - Compliance: LGPD, SOC2, ISO 27001
```

---

## 2. Escalabilidade

Escalabilidade é a capacidade do sistema de **manter a performance** à medida que a demanda cresce.

### Tipos de escala

```
Escala Vertical (Scale Up):
  Aumentar recursos da máquina
  CPU: 4 cores → 16 cores
  RAM: 8GB → 64GB
  Limite: hardware máximo

Escala Horizontal (Scale Out):
  Adicionar mais máquinas
  1 servidor → 10 servidores
  Balanceador de carga na frente
  Limite: gerenciamento de estado
```

### O que escalar no sistema Enterprise

```
Usuários       → Autenticação, session, rate limiting
Dados          → Índices, partições, sharding
Funcionalidades→ Módulos, microserviços, feature flags
Times          → Código modular, documentação, padronização
```

### Anti-padrões de escalabilidade

- **Banco como broker de mensagens** — usar fila dedicada (RabbitMQ, Redis)
- **N+1 queries** — usar eager loading ou batch
- **Session in-process** — usar Redis session store
- **Arquivos no servidor** — usar S3/CDN
- **Monólito sem modularização** — pelo menos módulos bem definidos

---

## 3. Governança

Governança é o conjunto de **regras e processos** que garantem consistência e qualidade no desenvolvimento.

### Pilares da governança

```
┌──────────────────────────────────────────────┐
│                 GOVERNANÇA                    │
├──────────────────────────────────────────────┤
│  Código       │  Processo     │  Dados        │
│───────────────┼───────────────┼──────────────│
│ TypeScript    │ Git Flow      │ Migrações     │
│ strict        │ Code Review   │ Audit trail   │
│ Lint/format   │ CI/CD         │ Backup        │
│ Padrões       │ ADRs          │ Retention     │
│ Arquitetura   │ Documentação  │ Compliance    │
└───────────────┴───────────────┴──────────────┘
```

### Exemplos de regras de governança

```markdown
## Regras de Governança

### Código
- TypeScript strict mode obrigatório
- Sem `any` — exceções revisadas em PR
- Lint e format automáticos (pre-commit hook)

### Processo
- Toda feature começa com ADR se mudar arquitetura
- PR aprovado por 1 reviewer + CI verde
- Commits semânticos: feat, fix, refactor, docs, test

### Dados
- Migrações são revisadas como código
- Soft delete para dados críticos
- Audit trail para todas as alterações
```

---

## 4. Manutenibilidade

Manutenibilidade é a facilidade de **entender, modificar e estender** o sistema.

### O custo da falta de manutenibilidade

```
Código sem manutenibilidade:
  ┌────────────────────────────────────────────┐
  │  Feature nova         │  2 semanas         │
  │  Corrigir bug         │  3 dias            │
  │  Onboarding dev novo   │  2 meses           │
  │  Refatorar módulo     │  "melhor reescrever"│
  └────────────────────────────────────────────┘

Código com manutenibilidade:
  ┌────────────────────────────────────────────┐
  │  Feature nova         │  2 dias            │
  │  Corrigir bug         │  2 horas           │
  │  Onboarding dev novo   │  1 semana          │
  │  Refatorar módulo     │  2 dias            │
  └────────────────────────────────────────────┘
```

### Como garantir manutenibilidade

1. **Código limpo** — nomes descritivos, funções pequenas, sem duplicação
2. **Testes** — unitários + integração + E2E
3. **Documentação** — README, ADRs, Swagger
4. **Modularização** — baixo acoplamento, alta coesão
5. **Padronização** — mesmas convenções em todo o código

---

## 5. Observabilidade

Observabilidade é a capacidade de **entender o estado interno do sistema** a partir de seus outputs externos.

### Os 3 pilares

```
LOGS                            MÉTRICAS                    TRACING
Eventos discretos               Dados agregados             Fluxo de requisições
"Usuário X fez Y"              "500 requisições/segundo"   "Requisição passou por A→B→C"
                                                              
Exemplos:                       Exemplos:                   Exemplos:
- log.error("Falha no pgto")    - response_time_p95         - span do endpoint
- log.info("Usuário logou")     - error_rate                - span do banco
- log.warn("Rate limit")        - cpu/memory usage          - span do cache
```

### O que observar em um sistema Enterprise

```
Saúde da aplicação:
  - Uptime, memory, CPU, conexões ativas
  - Health check endpoints (/health, /ready)

Performance:
  - Response time (p50, p95, p99)
  - Throughput (req/s)
  - Error rate

Negócio:
  - Usuários ativos, signups, churn
  - Funcionalidades mais usadas
  - Funis de conversão

Segurança:
  - Tentativas de login falhas
  - Rate limiting acionado
  - Acessos não autorizados
```

---

## 6. Segurança

Segurança em software Enterprise não é opcional — é **pré-requisito**.

### Mindset de segurança

```
Não: "Vamos adicionar segurança depois"
Sim: "Segurança é parte da definição de "pronto""
```

### Camadas de segurança

```
Camada 1: Código
  → Input validation, ORM (previne injection), prepared statements

Camada 2: Autenticação
  → JWT, OAuth2, MFA, senhas com hash

Camada 3: Autorização
  → RBAC, CASL abilities, verificação por recurso

Camada 4: Rede
  → HTTPS, CORS, CSP, firewall, VPN

Camada 5: Infraestrutura
  → Secrets management, network isolation, backup
```

### Checklist Enterprise de segurança

- [ ] Nenhum segredo no código (.env, secrets manager)
- [ ] HTTPS obrigatório (redirect HTTP→HTTPS)
- [ ] CSP header configurado
- [ ] CORS com origens específicas (não `*`)
- [ ] Rate limiting em endpoints críticos
- [ ] Validação de entrada em todos os endpoints
- [ ] Autenticação em todas as rotas protegidas
- [ ] Auditoria de ações sensíveis

---

## 7. Compliance

Compliance é a **conformidade com leis e regulamentações**.

### Principais regulamentações

| Regulamentação | Região | Foco |
|---------------|--------|------|
| LGPD | Brasil | Dados pessoais |
| GDPR | Europa | Dados pessoais |
| PCI DSS | Global | Dados de cartão |
| HIPAA | EUA | Dados de saúde |
| SOC 2 | Global | Controles internos |

### O que a LGPD exige

1. **Consentimento** — usuário autoriza coleta de dados
2. **Finalidade** — dados coletados para propósito específico
3. **Minimização** — colete apenas o necessário
4. **Transparência** — informe como os dados são usados
5. **Segurança** — proteja os dados armazenados
6. **Direitos do titular** — acesso, correção, exclusão
7. **Registro de tratamento** — documente o que faz com os dados

### Implementando compliance no código

```typescript
// Consentimento
interface Consentimento {
  usuarioId: string;
  finalidade: string; // "marketing", "analytics", "essencial"
  autorizado: boolean;
  data: DateTime;
}

// Direito de exclusão (right to erasure)
async function esquecerUsuario(usuarioId: string) {
  await prisma.usuario.update({
    where: { id: usuarioId },
    data: {
      nome: anonimizar(usuario.nome),
      email: anonimizar(usuario.email),
      deletedAt: new Date(),
    },
  });
  await prisma.consentimento.deleteMany({
    where: { usuarioId },
  });
}
```

---

## 8. Multi-tenant

Multi-tenant é a capacidade de **atender múltiplos clientes** (tenants) com uma única instância do sistema.

### Estratégias de isolamento

```
Database per Tenant:
  Prós: isolamento máximo, backup individual
  Contras: caro, complexo (migrations em N bancos)
  Quando: dados sensíveis (saúde, finanças)
  Custo: $$$$$

Schema per Tenant:
  Prós: bom isolamento, um banco
  Contras: migrations complexas, conexões
  Quando: dados moderadamente sensíveis
  Custo: $$$

Row-Level Security:
  Prós: simples, barato, migrations únicas
  Contras: risco de vazamento entre tenants
  Quando: dados de baixa sensibilidade
  Custo: $
```

### Implementação prática (RLS no Prisma)

```prisma
model Tenant {
  id   String @id
  slug String @unique
  name String
}

model Usuario {
  id        String   @id
  tenantId  String
  tenant    Tenant   @relation(fields: [tenantId], references: [id])
  email     String
}
```

```typescript
// Middleware que filtra por tenant
async function getUsuarios(tenantId: string) {
  return prisma.usuario.findMany({
    where: { tenantId },
  });
}
```

---

## 9. Alta disponibilidade

Alta disponibilidade (HA) é a capacidade do sistema de **permanecer acessível** mesmo com falhas.

### Métricas de disponibilidade

```
Disponibilidade     Downtime/ano       Exemplo
99% (1 nove)       3.65 dias           Sistemas internos
99.9% (2 noves)    8.76 horas          SaaS padrão
99.99% (3 noves)   52.56 minutos       Enterprise crítico
99.999% (4 noves)  5.26 minutos        Missão crítica
```

### Estratégias de HA

```
Sem ponto único de falha:
  - Múltiplas instâncias do servidor
  - Múltiplas réplicas do banco
  - CDN para assets estáticos

Redundância:
  - Load balancer (distribui tráfego)
  - Database replica (leitura em réplicas)
  - Cache (Redis cluster)

Recuperação:
  - Health checks → reinício automático
  - Backup automático + testado
  - Disaster recovery plan
```

---

## Resumo

1. **Software Enterprise** é construído para organizações — multi-usuário, seguro, auditável
2. **Escalabilidade** — horizontal > vertical; banco não é broker
3. **Governança** — código + processo + dados com regras claras
4. **Manutenibilidade** — código limpo, testado, documentado, modular
5. **Observabilidade** — logs + métricas + tracing = entender o sistema
6. **Segurança** — em camadas, desde o código até a infra
7. **Compliance** — LGPD/GDPR não são opcionais
8. **Multi-tenant** — escolha a estratégia de isolamento certa
9. **Alta disponibilidade** — sem ponto único de falha
