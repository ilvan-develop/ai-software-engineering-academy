---
marp: true
theme: uncover
class:
  - lead
  - invert
---

<!-- _class: lead invert -->
<!-- _backgroundColor: "#1A1A2E" -->
<!-- _color: "#FFFFFF" -->

# **IA para Desenvolvedores**

**CapÃ­tulo 2 â€” Agentes de IA na PrÃ¡tica**

---

AI Software Engineering Academy â€” 2026

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Agenda

- O problema do agente genÃ©rico
- A soluÃ§Ã£o: agentes especializados
- Anatomia de um agente
- Os 17 agentes da formaÃ§Ã£o
- Como criar um novo agente
- Como combinar agentes em pipeline
- IntegraÃ§Ã£o com OpenCode
- Boas prÃ¡ticas e o futuro (Meta-Agent)

*Nota do apresentador: Este mÃ³dulo Ã© sobre construir um ecossistema de agentes especializados. Diferencie de "um agente que faz tudo". Foco Ã© qualidade por domÃ­nio.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## O Problema do Agente GenÃ©rico

Um Ãºnico agente genÃ©rico produz resultados **medianos em todas as Ã¡reas**.

```
Agente Generico:
  Conhecimento: "sabe de tudo um pouco"
  +-- Frontend:    ** (sabe React, mas nao Next.js)
  +-- Backend:     *** (sabe API, mas nao DDD)
  +-- Seguranca:   *  (esquece CSRF, rate limiting)
  +-- Banco:       **  (faz N+1 sem perceber)
  +-- DevOps:      *  (Dockerfile sem multi-stage)

Resultado: codigo "funciona", mas cheio de divida tecnica
```

[imagem: grÃ¡fico radar mostrando notas baixas em mÃºltiplas Ã¡reas]

*Nota do apresentador: O mesmo vale para devs full-stack generalistas. EspecializaÃ§Ã£o Ã© a chave.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## A SoluÃ§Ã£o: Agentes Especializados

Cada domÃ­nio com um agente **expert** naquela Ã¡rea.

```
Agente Frontend Expert:
  Conhecimento: Next.js 14, RSC, Tailwind, shadcn/ui
  +-- Performance:       ***** (Lazy, Suspense, Images)
  +-- Acessibilidade:    ***** (ARIA, WCAG 2.1)
  +-- SEO:               ***** (Metadata, OG, sitemap)
  +-- TypeScript:        ***** (strict mode, generics)

Resultado: codigo de producao, pronto para review
```

**EficiÃªncia:** Ecossistema de especialistas >> um generalista.
**Papel do dev:** Orquestrador dos agentes.

*Nota do apresentador: A ideia nÃ£o Ã© substituir o dev, mas dar a ele especialistas sob demanda.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Anatomia de um Agente

Cada agente segue a mesma estrutura padronizada:

```
agente/
+-- README.md           # Identidade: objetivo, stack, limites
+-- workflow.md         # Processo: fluxo passo a passo
+-- checklist.md        # Qualidade: o que validar
+-- prompts/            # Templates para tarefas comuns
    +-- prompt-login.md
    +-- prompt-api.md
```

**5 Componentes de um agente eficaz:**

```
+---------+  +---------+  +--------+  +--------+  +---------+
|IDENTIDADE|  |CONHECIM.|  |PROCESSO|  |QUALIDADE|  |COMUNIC. |
+---------+  +---------+  +--------+  +--------+  +---------+
|Quem Ã©?   |  |Stack    |  |Entrada |  |Checklist|  |Formato  |
|O que faz?|  |PadrÃµes  |  |Transform|  |CritÃ©rios|  |Entrada  |
|Limites   |  |Refs ext.|  |SaÃ­da   |  |Anti-pat.|  |SaÃ­da    |
+---------+  +---------+  +--------+  +--------+  +---------+
```

*Nota do apresentador: Estrutura padronizada permite criar, entender e manter agentes.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Os 17 Agentes da FormaÃ§Ã£o

**7 categorias cobrindo todo o ciclo de desenvolvimento:**

| Categoria | Agentes |
|-----------|---------|
| **Produto** | Product Discovery, UX Research |
| **Design** | UX Designer, UI Designer |
| **Arquitetura** | Enterprise Architect, DB Architect |
| **Desenvolvimento** | Backend, Frontend, Prisma Expert |
| **Infraestrutura** | DevOps, Security Expert |
| **Qualidade** | QA, Performance Expert |
| **GovernanÃ§a** | Auditor, Documentation, Refactoring |

[imagem: diagrama mostrando os 17 agentes em 7 grupos]

*Nota do apresentador: Cada agente Ã© especialista em seu domÃ­nio. Juntos cobrem todo o ciclo.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Detalhamento dos Agentes

**Produto + Design + Arquitetura:**
| Agente | Stack |
|--------|-------|
| Product Discovery | User Stories, RICE, MoSCoW, BDD |
| UX/UI Designer | Wireframes, Design System, WCAG |
| Enterprise Architect | Clean Arch, DDD, ADRs, C4 Model |

**Desenvolvimento + Infra:**
| Agente | Stack |
|--------|-------|
| Backend Expert | NestJS, Prisma, REST, GraphQL, Zod |
| Frontend Expert | Next.js 14, RSC, Tailwind, shadcn/ui |
| Security Expert | OWASP Top 10, JWT, bcrypt, CSP |

**Qualidade + GovernanÃ§a:**
| Agente | FunÃ§Ã£o |
|--------|--------|
| QA Expert | Jest, Playwright, cobertura >80% |
| Auditor | 16 tipos de auditoria (score 0-10) |
| Refactoring | Code smells, preservar comportamento |

*Nota do apresentador: O Security Expert e o Auditor sÃ£o os mais crÃ­ticos para produÃ§Ã£o.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Como Criar um Novo Agente â€” Passo a Passo

```
1. DEFINIR o DOMINIO
   -> Qual area ele cobre?

2. DEFINIR o CONHECIMENTO BASE
   -> Quais tecnologias e padroes?

3. DEFINIR RESPONSABILIDADES
   -> O que faz? O que NAO faz? (limites!)

4. DEFINIR o PROCESSO
   -> Entrada -> Transformacao -> Saida

5. CRIAR CHECKLIST DE QUALIDADE
   -> O que validar antes de concluir?

6. CRIAR TEMPLATES DE PROMPT
   -> Prompts reutilizaveis

7. TESTAR com um caso real
   -> Executar, revisar, ajustar
```

*Nota do apresentador: O passo 3 (limites) Ã© o mais importante. Sem limites, o agente alucina.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Exemplo: Security Expert Agent

| Aspecto | DefiniÃ§Ã£o |
|---------|-----------|
| **DomÃ­nio** | SeguranÃ§a de aplicaÃ§Ãµes web |
| **Conhecimento** | OWASP Top 10, JWT, OAuth2, MFA, bcrypt, CSP |
| **Responsabilidades** | AutenticaÃ§Ã£o, autorizaÃ§Ã£o, rate limiting, segredos |
| **Limites** | NÃƒO define arquitetura, NÃƒO implementa regras de negÃ³cio |

**Checklist de qualidade:**
- [ ] Senhas com hash bcrypt/argon2
- [ ] JWT com expiraÃ§Ã£o curta + refresh token
- [ ] Rate limiting no login
- [ ] CSP header configurado
- [ ] Helmet.js ativado
- [ ] Input validation em todos os endpoints

*Nota do apresentador: O checklist vira instruÃ§Ã£o para o agente. Ele se auto-verifica.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## Como Combinar Agentes em Pipeline

O verdadeiro poder estÃ¡ em **compor** agentes em sequÃªncia.

```
Pipeline de Feature Completo:

Product Discovery -> UX Designer -> UI Designer
       |                 |               |
  Enterprise Architect   |               |
       +-----------------+---------------+
                         |
              Backend + Frontend + Prisma + Security
                         |
                     QA Expert
                         |
                DevOps Expert (deploy)
                         |
                  Auditor Agent (score final)
                         |
                Documentation Agent
```

[imagem: fluxograma visual do pipeline]

*Nota do apresentador: Cada agente recebe o output do anterior, transforma e passa adiante. O Auditor revisa no final. Linha de produÃ§Ã£o de software.*

---

<!-- _backgroundColor: "#FFFFFF" -->
<!-- _color: "#333333" -->

## IntegraÃ§Ã£o com OpenCode

Configure agentes no `opencode.json`:

```json
{
  "agents": {
    "frontend-expert": {
      "prompt": ".opencode/agents/frontend-expert.md",
      "permissions": {
        "bash": true, "read": true,
        "edit": true, "glob": true, "grep": true
      }
    },
    "auditor": {
      "prompt": ".opencode/agents/auditor.md",
      "permissions": {
        "bash": true, "read": true,
        "edit": false,
        "glob": true, "grep": true
      }
    }
  }
}
```

**InvocaÃ§Ã£o:** `@frontend-expert Crie
