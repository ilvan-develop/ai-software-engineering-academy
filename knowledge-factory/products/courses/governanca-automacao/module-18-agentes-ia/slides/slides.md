---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 18 — Agentes de IA: Criação de Agentes Especializados

## Módulo 18 - Agentes de IA: Criação de Agentes Especializados

---
## 1. Por que agentes especializados?

- Um único agente genérico (ex: "você é um desenvolvedor full stack") produz resultados **medianos em todas as áreas**.
- Um ecossistema de agentes especializados produz **resultados excelentes em cada área**.
- Agente Genérico:
- Conhecimento: "sabe de tudo um pouco"
- ├── Frontend: ⭐⭐☆☆☆  (sabe React, mas não Next.js App Router)

---
## 2. Anatomia de um agente

- Cada agente da nossa biblioteca segue a mesma estrutura:
- agente/
- ├── README.md           # Identidade: objetivo, responsabilidades, stack
- ├── workflow.md         # Processo: fluxo de trabalho passo a passo
- ├── checklist.md        # Qualidade: o que validar antes de entregar
- ├── prompts/            # Instruções: templates de prompt para tarefas comuns

---
## 3. Os 17 agentes da formação

- | Agente | Função | Stack/Conhecimento |
- |--------|--------|-------------------|
- | **Product Discovery** | Transformar problemas em requisitos | User Stories, RICE, MoSCoW, BDD |
- | **UX Research** | Validar hipóteses com usuários | Entrevistas, testes de usabilidade, personas |

---
## 4. Como criar um novo agente

- 1. Definir o DOMÍNIO do agente
- → Qual área ele cobre? (ex: "segurança de aplicações web")
- 2. Definir o CONHECIMENTO BASE
- → Quais tecnologias, padrões e boas práticas ele domina?
- 3. Definir RESPONSABILIDADES

---
## 5. Como combinar agentes em pipeline

- O verdadeiro poder está em **compor** agentes em sequência.
- Product Discovery  ──→  UX Designer  ──→  UI Designer
- │                       │                  │
- │                  Enterprise Architect     │
- │                       │                  │

---
## 6. Integração com OpenCode

- {
- "agents": {
- "frontend-expert": {
- "prompt": ".opencode/agents/frontend-expert.md",
- "permissions": {

---
## 7. Boas práticas na criação de agentes

- Seja específico** — "Crie componente com Server Component" não "Faça um componente bonito"
- Defina limites** — "Este agente NÃO implementa regras de domínio"
- Forneça exemplos** — "Siga este padrão: [exemplo]"
- Crie checklists** — "Antes de entregar, verifique: [itens]"
- Itere** — Ajuste os prompts baseado nos resultados

---
## 8. O futuro: agentes que criam agentes

- O próximo passo natural: um **Meta-Agent** que cria agentes especializados sob demanda.

---
## Exemplo: text

```text
Agente Genérico:
  Conhecimento: "sabe de tudo um pouco"
  ├── Frontend: ⭐⭐☆☆☆  (sabe React, mas não Next.js App Router)
  ├── Backend:  ⭐⭐⭐☆☆  (sabe criar API, mas não DDD)
  ├── Segurança: ⭐☆☆☆☆  (esquece CSRF, rate limiting)
  ├── Banco:    ⭐⭐☆☆☆  (faz N+1 sem perceber)
  └── DevOps:   ⭐☆☆☆☆  (Dockerfile sem multi-stage)

Resultado: código "funciona", mas cheio de dívida técnica
```

---
## Exemplo: text

```text
Agente Frontend:
  Conhecimento: Next.js 14, RSC, Tailwind, shadcn/ui
  ├── Performance: ⭐⭐⭐⭐⭐ (Lazy loading, Suspense, Image optimization)
  ├── Acessibilidade: ⭐⭐⭐⭐⭐ (ARIA, WCAG 2.1, keyboard nav)
  ├── SEO: ⭐⭐⭐⭐⭐ (Metadata API, OG tags, sitemap)
  └── TypeScript: ⭐⭐⭐⭐⭐ (strict mode, generics)

Resultado: código de produção, pronto para review
```

---
## Recap

- 1. Por que agentes especializados?
- 2. Anatomia de um agente
- 3. Os 17 agentes da formação
- 4. Como criar um novo agente
- 5. Como combinar agentes em pipeline
- 6. Integração com OpenCode
- 7. Boas práticas na criação de agentes
- 8. O futuro: agentes que criam agentes

---
# Obrigado!

## Perguntas?
