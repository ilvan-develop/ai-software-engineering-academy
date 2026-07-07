<!-- i18n: en-US | source: pt-BR | generated: 2026-07-07 -->
# Exercícios — Módulo 00

## Exercício 1: Matriz de Delegação

**Objetivo:** Praticar a decisão sobre o que delegar para a IA.

Analise cada tarefa abaixo e classifique segundo a Matriz de Delegação:
- **Humano decide**
- **Humano + Agente**
- **Agente faz**
- **Agente decide**

| # | Tarefa | Classificação | Justificativa |
|---|--------|---------------|---------------|
| 1 | Escolher entre PostgreSQL e MongoDB | | |
| 2 | Criar endpoint CRUD de usuários | | |
| 3 | Decidir se implementa feature X agora ou depois | | |
| 4 | Formatar código com Prettier | | |
| 5 | Revisar se há SQL injection nos endpoints | | |
| 6 | Definir a visão arquitetural do sistema | | |
| 7 | Escrever testes unitários para o serviço de autenticação | | |
| 8 | Decidir o nome das variáveis no código | | |
| 9 | Escolher Design System para o projeto | | |
| 10 | Documentar a API com Swagger | | |

---

## Exercício 2: Criando regras para agentes

**Objetivo:** Praticar a escrita de instruções claras para agentes de IA.

Você precisa criar um arquivo `AGENTS.md` para um novo projeto. Escreva regras para:

1. **Stack tecnológica** — Next.js + NestJS + Prisma + PostgreSQL
2. **Padrões de código** — TypeScript strict, sem `any`, nomes em inglês
3. **Testes** — Jest para backend, Testing Library para frontend
4. **Git** — commits semânticos (feat:, fix:, docs:, refactor:)
5. **Segurança** — JWT, bcrypt, validação em todos os inputs

Use o formato:
```markdown
# Regras para Agentes

## Stack
- ...

## Código
- ...

## Testes
- ...
```

---

## Exercício 3: O ciclo de desenvolvimento

**Objetivo:** Mapear o ciclo de desenvolvimento com agentes.

Dado o seguinte requisito:

> "Um sistema de gestão de tarefas onde usuários podem criar projetos, adicionar membros, atribuir tarefas e acompanhar o progresso em um kanban."

Mapeie as etapas do ciclo de desenvolvimento, identificando:
1. Qual agente atua em cada etapa
2. Qual artefato é produzido
3. O que o humano faz vs. o que o agente faz

Use a tabela:

| Etapa | Agente | Artefato | Humano | Agente |
|-------|--------|----------|--------|--------|
| Discovery | Product Discovery | User Stories | ... | ... |
| ... | ... | ... | ... | ... |
