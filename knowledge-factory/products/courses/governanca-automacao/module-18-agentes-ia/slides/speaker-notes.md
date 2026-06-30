## Introducao

# Módulo 18 — Agentes de IA: Criação de Agentes Especializados
**Construindo seu exército de agentes.**
---

---
## 1. Por que agentes especializados?

Um único agente genérico (ex: "você é um desenvolvedor full stack") produz resultados **medianos em todas as áreas**.
Um ecossistema de agentes especializados produz **resultados excelentes em cada área**.
### O problema do agente genérico
Agente Genérico:
Conhecimento: "sabe de tudo um pouco"
├── Frontend: ⭐⭐☆☆☆  (sabe React, mas não Next.js App Router)
├── Backend:  ⭐⭐⭐☆☆  (sabe criar API, mas não DDD)
├── Segurança: ⭐☆☆☆☆  (esquece CSRF, rate limiting)

---
## 2. Anatomia de um agente

Cada agente da nossa biblioteca segue a mesma estrutura:
agente/
├── README.md           # Identidade: objetivo, responsabilidades, stack
├── workflow.md         # Processo: fluxo de trabalho passo a passo
├── checklist.md        # Qualidade: o que validar antes de entregar
├── prompts/            # Instruções: templates de prompt para tarefas comuns
│   ├── prompt-tarefa-1.md
│   └── prompt-tarefa-2.md

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

---
## 4. Como criar um novo agente

### Passo a passo
1. Definir o DOMÍNIO do agente
→ Qual área ele cobre? (ex: "segurança de aplicações web")
2. Definir o CONHECIMENTO BASE
→ Quais tecnologias, padrões e boas práticas ele domina?
3. Definir RESPONSABILIDADES
→ O que ele faz? O que ele NÃO faz? (limites são importantes)
4. Definir o PROCESSO

---
## 5. Como combinar agentes em pipeline

O verdadeiro poder está em **compor** agentes em sequência.
### Pipeline de features
Product Discovery  ──→  UX Designer  ──→  UI Designer
│                       │                  │
│                  Enterprise Architect     │
│                       │                  │
└───────────────────────┼──────────────────┘
│

---
## 6. Integração com OpenCode

### Configuração de agentes no opencode.json
{
"agents": {
"frontend-expert": {
"prompt": ".opencode/agents/frontend-expert.md",
"permissions": {
"bash": true,
"read": true,

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

---
## 8. O futuro: agentes que criam agentes

O próximo passo natural: um **Meta-Agent** que cria agentes especializados sob demanda.
### Como funcionaria

---
