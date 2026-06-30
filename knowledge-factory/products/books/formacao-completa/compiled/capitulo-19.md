
# Agentes de IA

# Módulo 18 — Agentes de IA: Criação de Agentes Especializados

**Construindo seu exército de agentes.**

---

## 1. Por que agentes especializados?

Um único agente genérico (ex: "você é um desenvolvedor full stack") produz resultados **medianos em todas as áreas**.

Um ecossistema de agentes especializados produz **resultados excelentes em cada área**.

### O problema do agente genérico

```
Agente Genérico:
  Conhecimento: "sabe de tudo um pouco"
  ├── Frontend: ⭐⭐☆☆☆  (sabe React, mas não Next.js App Router)
  ├── Backend:  ⭐⭐⭐☆☆  (sabe criar API, mas não DDD)
  ├── Segurança: ⭐☆☆☆☆  (esquece CSRF, rate limiting)
  ├── Banco:    ⭐⭐☆☆☆  (faz N+1 sem perceber)
  └── DevOps:   ⭐☆☆☆☆  (Dockerfile sem multi-stage)

Resultado: código "funciona", mas cheio de dívida técnica
```

### A solução dos agentes especializados

```
Agente Frontend:
  Conhecimento: Next.js 14, RSC, Tailwind, shadcn/ui
  ├── Performance: ⭐⭐⭐⭐⭐ (Lazy loading, Suspense, Image optimization)
  ├── Acessibilidade: ⭐⭐⭐⭐⭐ (ARIA, WCAG 2.1, keyboard nav)
  ├── SEO: ⭐⭐⭐⭐⭐ (Metadata API, OG tags, sitemap)
  └── TypeScript: ⭐⭐⭐⭐⭐ (strict mode, generics)

Resultado: código de produção, pronto para review
```

---

## 2. Anatomia de um agente

Cada agente da nossa biblioteca segue a mesma estrutura:

```text
agente/
├── README.md           # Identidade: objetivo, responsabilidades, stack
├── workflow.md         # Processo: fluxo de trabalho passo a passo
├── checklist.md        # Qualidade: o que validar antes de entregar
├── prompts/            # Instruções: templates de prompt para tarefas comuns
│   ├── prompt-tarefa-1.md
│   └── prompt-tarefa-2.md
```

### Componentes de um agente eficaz

```text
┌──────────────────────────────────────┐
│           IDENTIDADE                  │
│  Quem é este agente?                  │
│  O que ele sabe fazer?               │
│  O que ele NÃO faz?                   │
├──────────────────────────────────────┤
│           CONHECIMENTO                │
│  Stack tecnológica                    │
│  Padrões e boas práticas             │
│  Referências externas                │
├──────────────────────────────────────┤
│           PROCESSO                    │
│  Fluxo de trabalho                   │
│  Entrada → Transformação → Saída     │
├──────────────────────────────────────┤
│           QUALIDADE                   │
│  Checklist de validação              │
│  Critérios de aceite                 │
│  Anti-padrões a evitar               │
├──────────────────────────────────────┤
│           COMUNICAÇÃO                 │
│  Formato de entrada (o que recebe)   │
│  Formato de saída (o que entrega)    │
│  Como reportar problemas             │
└──────────────────────────────────────┘
```

---

## 3. Os 17 agentes da formação

### Agentes de Produto

| Agente | Função | Stack/Conhecimento |
|--------|--------|-------------------|
| **Product Discovery** | Transformar problemas em requisitos | User Stories, RICE, MoSCoW, BDD |
| **UX Research** | Validar hipóteses com usuários | Entrevistas, testes de usabilidade, personas |

### Agentes de Design

| Agente | Função | Stack/Conhecimento |
|--------|--------|-------------------|
| **UX Designer** | Projetar experiência do usuário | User flows, wireframes, acessibilidade (WCAG) |
| **UI Designer** | Projetar interface visual | Design System, tokens, dark mode, responsividade |

### Agentes de Arquitetura

| Agente | Função | Stack/Conhecimento |
|--------|--------|-------------------|
| **Enterprise Architect** | Decisões arquiteturais | Clean Arch, DDD, ADRs, C4 Model |
| **Database Architect** | Modelagem de dados | PostgreSQL, índices, partições, migrações |

### Agentes de Desenvolvimento

| Agente | Função | Stack/Conhecimento |
|--------|--------|-------------------|
| **Backend Expert** | APIs e regras de domínio | NestJS, Prisma, REST, GraphQL, Zod |
| **Frontend Expert** | Interfaces e componentes | Next.js 14, RSC, Tailwind, shadcn/ui, TanStack Query |
| **Prisma Expert** | Schema e queries | Prisma ORM, migrations, N+1 prevention, soft delete |

### Agentes de Infraestrutura

| Agente | Função | Stack/Conhecimento |
|--------|--------|-------------------|
| **DevOps Expert** | Docker, CI/CD, deploy | Docker multi-stage, GitHub Actions, health checks |
| **Security Expert** | Proteção do sistema | OWASP Top 10, JWT, bcrypt, rate limiting, CSP |

### Agentes de Qualidade

| Agente | Função | Stack/Conhecimento |
|--------|--------|-------------------|
| **QA Expert** | Testes automatizados | Jest, Playwright, Testing Library, cobertura >80% |
| **Performance Expert** | Otimização | Core Web Vitals, caching, bundle analysis, load testing |

### Agentes de Governança

| Agente | Função | Stack/Conhecimento |
|--------|--------|-------------------|
| **Auditor** | 16 tipos de auditoria | Score (0-10), riscos (Blocker a Minor), planos de ação |
| **Documentation** | Documentação técnica | ADRs, README, Swagger, CHANGELOG, CONTRIBUTING |
| **Refactoring** | Refatoração guiada | Code smells, patterns, TypeScript strict, preservar comportamento |

---

## 4. Como criar um novo agente

### Passo a passo

```
1. Definir o DOMÍNIO do agente
   → Qual área ele cobre? (ex: "segurança de aplicações web")

2. Definir o CONHECIMENTO BASE
   → Quais tecnologias, padrões e boas práticas ele domina?

3. Definir RESPONSABILIDADES
   → O que ele faz? O que ele NÃO faz? (limites são importantes)

4. Definir o PROCESSO
   → Qual o fluxo de trabalho? O que recebe na entrada? O que entrega?

5. Criar CHECKLIST DE QUALIDADE
   → O que validar antes de considerar o trabalho concluído?

6. Criar TEMPLATES DE PROMPT
   → Prompts reutilizáveis para as tarefas mais comuns

7. TESTAR com um caso real
   → Executar o agente, revisar o output, ajustar
```

### Exemplo: Criando o Security Expert Agent

**Domínio:** Segurança de aplicações web

**Conhecimento base:**
- OWASP Top 10 (2021)
- JWT, OAuth2, MFA
- bcrypt, Helmet, CORS, CSP
- NestJS Guards, CASL (autorização)

**Responsabilidades:**
- Implementar autenticação e autorização
- Prevenir SQL injection, XSS, CSRF
- Configurar rate limiting
- Gerenciar segredos

**Limites:**
- Não define arquitetura geral
- Não implementa lógica de negócio
- Não gerencia infraestrutura

**Checklist:**
```text
- [ ] Senhas com hash bcrypt/argon2
- [ ] JWT com expiração curta + refresh token
- [ ] Rate limiting no login
- [ ] CSP header configurado
- [ ] Helmet.js ativado
- [ ] Input validation em todos os endpoints
- [ ] SQL injection prevenido (ORM)
```

---

## 5. Como combinar agentes em pipeline

O verdadeiro poder está em **compor** agentes em sequência.

### Pipeline de features

```text
Product Discovery  ──→  UX Designer  ──→  UI Designer
     │                       │                  │
     │                  Enterprise Architect     │
     │                       │                  │
     └───────────────────────┼──────────────────┘
                             │
                    Backend Expert
                    Frontend Expert
                    Prisma Expert
                    Security Expert
                             │
                         QA Expert
                             │
                    DevOps Expert (deploy)
                             │
                     Auditor Agent
                             │
                    Documentation Agent
```

### Pipeline de auditoria

```
Feature implementada
        │
        ▼
Security Auditor ──→ Se Bloquer/Critical → Backend Expert (corrige)
        │                                     │
        ▼                                     ▼
Architecture Auditor ──→ Se problema → Enterprise Architect (revisa)
        │
        ▼
Performance Auditor ──→ Se lento → Performance Expert (otimiza)
        │
        ▼
Code Quality Auditor ──→ Se abaixo do padrão → Refactoring Agent
        │
        ▼
Relatório consolidado com score geral
```

### Pipeline de onboarding

```
PO descreve problema em linguagem natural
        │
        ▼
Product Discovery Agent → User Stories + Acceptance Criteria
        │
        ▼
UX Researcher Agent → Valida com usuários → Personas + Jornada
        │
        ▼
UX Designer Agent → Wireframes + User Flows
        │
        ▼
UI Designer Agent → Mockups com Design System
        │
        ▼
Enterprise Architect → Arquitetura + ADRs
        │
        ▼
Backend + Frontend + Prisma + Security → Implementação
        │
        ▼
QA Agent → Testes
        │
        ▼
DevOps Agent → Deploy
        │
        ▼
Auditor Agent → Score final
```

---

## 6. Integração com OpenCode

### Configuração de agentes no opencode.json

```json
{
  "agents": {
    "frontend-expert": {
      "prompt": ".opencode/agents/frontend-expert.md",
      "permissions": {
        "bash": true,
        "read": true,
        "edit": true,
        "glob": true,
        "grep": true
      }
    },
    "auditor": {
      "prompt": ".opencode/agents/auditor.md",
      "permissions": {
        "bash": true,
        "read": true,
        "edit": false,
        "glob": true,
        "grep": true
      }
    }
  }
}
```text

### Como invocar um agente

```text
@frontend-expert Crie um componente de tabela com:
- Server Component
- Suporte a sort e filter
- Paginação
- Loading state com Suspense
```

### Como fazer um agente revisar outro

```text
@auditor Revise a segurança deste endpoint.

[endpoint code]
```

---

## 7. Boas práticas na criação de agentes

### Faça

- **Seja específico** — "Crie componente com Server Component" não "Faça um componente bonito"
- **Defina limites** — "Este agente NÃO implementa regras de domínio"
- **Forneça exemplos** — "Siga este padrão: [exemplo]"
- **Crie checklists** — "Antes de entregar, verifique: [itens]"
- **Itere** — Ajuste os prompts baseado nos resultados

### Não faça

- **Não misture domínios** — Um agente de backend não deve ter responsabilidades de frontend
- **Não seja vago** — "Seja criativo" não é uma instrução útil
- **Não ignore limites** — Se o agente não tem conhecimento, ele vai alucinar
- **Não pule a revisão** — Sempre revise o output, especialmente no início

### Padrão de prompt eficaz

```text
Ruim:
"Crie uma API de usuários."

Bom:
"Crie uma API REST de usuários com NestJS seguindo Clean Architecture.

Requisitos:
- POST /users (criar)
- GET /users (listar com paginação)
- GET /users/:id (detalhe)
- PUT /users/:id (atualizar)
- DELETE /users/:id (soft delete)

Validações:
- Email: formato válido, único
- Nome: 3-100 caracteres
- Senha: mínimo 8 caracteres, 1 número, 1 maiúscula

Regras:
- Usar Prisma para persistência
- Zod para validação
- Swagger para documentação
- Tratamento de erros com NestJS exception filters"
```

---

## 8. O futuro: agentes que criam agentes

O próximo passo natural: um **Meta-Agent** que cria agentes especializados sob demanda.

### Como funcionaria

```
1. Meta-Agent analisa o problema
2. Identifica os domínios necessários
3. Cria um agente especializado para cada domínio
4. Define os limites e responsabilidades
5. Testa e ajusta cada agente
6. Combina em pipeline
7. Executa o pipeline completo

