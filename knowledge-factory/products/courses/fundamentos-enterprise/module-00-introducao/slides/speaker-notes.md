## Introducao

# Módulo 00 — Introdução: A Nova Engenharia de Software
**Antes de escrever uma linha de código.**
---

---
## 1. Como a IA mudou o desenvolvimento de software

A IA generativa não é apenas mais uma ferramenta no cinto do desenvolvedor. Ela muda fundamentalmente **quem** escreve código, **como** o código é escrito e **o que** significa ser um engenheiro de software.
### O cenário antes da IA
- Programador escrevia 100% do código manualmente
- Produtividade limitada pela velocidade de digitação
- Conhecimento fragmentado em fóruns, documentação e livros
- Cada erro era descoberto em tempo de execução ou compilação
### O cenário com IA
- Programador **orquestra** agentes que escrevem código

---
## 2. Desenvolvimento tradicional vs. com agentes

| Dimensão | Tradicional | Com Agentes |
|----------|-------------|-------------|
| Escrita de código | Manual, linha a linha | Gerada por agentes, revisada por humanos |
| Erros | Descobertos em runtime | Prevenidos por checklists e auditorias |
| Documentação | Esquecida ou desatualizada | Gerada automaticamente pelos agentes |
| Escopo do desenvolvedor | Full stack (código + infra + deploy) | Orquestrador (agentes + revisão + decisões) |
| Velocidade | Limitada pela digitação | Limitada pela clareza das instruções |
| Consistência | Varia por desenvolvedor | Garantida por templates e padrões |

---
## 3. O papel do arquiteto

O arquiteto de software no mundo dos agentes não desapareceu — ele se tornou **mais estratégico**.
### Responsabilidades do Arquiteto
┌─────────────────────────────────────────────┐
│           ARQUITETO DE SOFTWARE              │
├─────────────────────────────────────────────┤
│  Antes:                                     │
│  • Escolher tecnologia                      │
│  • Desenhar diagramas                       │

---
## 4. O papel do Product Owner

O Product Owner (PO) também evolui no contexto de times com agentes.
### Responsabilidades do PO
| Atividade | Tradicional | Com Agentes |
|-----------|-------------|-------------|
| Escrever histórias | Texto livre | Formato Gherkin (Given/When/Then) |
| Critérios de aceite | Descritivos vagos | Especificações executáveis |
| Priorização | Feeling | RICE score com dados dos agentes |
| Validação | Manual, no final | Contínua, com protótipos gerados por agentes |

---
## 5. O papel da IA

A IA não é um substituto — é um **membro do time** com habilidades específicas.
### Como a IA deve ser posicionada
NÃO:  "A IA vai substituir os desenvolvedores"
SIM:  "A IA é um desenvolvedor júnior infinitamente rápido e disposto,
que precisa de supervisão técnica e contexto de negócio"
### O que a IA faz bem
- Geração de código repetitivo e padronizado
- Cobertura de edge cases em testes

---
## 6. Como dividir trabalho entre humanos e agentes

### A Matriz de Delegação
Alta complexidade
│
HUMANO DECIDE       │   HUMANO + AGENTE
(o que construir)   │   (arquitetura, revisão)
│
────────────────────────┼─────────────────────────
│

---
## 7. O ciclo de desenvolvimento com agentes

O ciclo completo que usaremos na formação:
┌─────────────────────────────────────────────────────────┐
│                 CICLO DE DESENVOLVIMENTO                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. Product Discovery  ←→  2. Design (UX/UI)           │
│         │                           │                   │
│  3. Arquitetura  ←→  4. Modelagem de Dados              │

---
## 8. O que esperar desta formação

### O que você vai aprender
1. **Produto** — discovery, UX research, Design Thinking
2. **Design** — UI Design, Design System, wireframes
3. **Arquitetura** — Clean Arch, DDD, modelagem de dados
4. **Implementação** — Backend (NestJS), Frontend (Next.js), Prisma
5. **Qualidade** — Segurança, testes, performance
6. **Operações** — DevOps, observabilidade, governança
7. **Inovação** — Agentes de IA, automação, auditoria

---
## Resumo

1. A IA mudou o papel do desenvolvedor de **escritor de código** para **orquestrador de agentes**
2. O arquiteto se torna ainda mais importante — define as regras que os agentes seguem
3. O PO ganha ferramentas para especificar com mais precisão
4. A divisão de trabalho segue a **Matriz de Delegação** (complexidade x risco)
5. O ciclo de desenvolvimento com agentes é mais iterativo e com mais pontos de validação
6. Código gerado por IA sem governança tem **40% de erro** — com regras cai para **~3%**

---
