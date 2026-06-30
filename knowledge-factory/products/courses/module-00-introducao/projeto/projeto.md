# Módulo 00 — Introdução: A Nova Engenharia de Software

**Antes de escrever uma linha de código.**

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
- Produtividade limitada pela qualidade das instruções (prompts)
- Conhecimento integrado no contexto do LLM
- Erros são prevenidos por revisão sistemática dos agentes

### A virada de chave

> "O desenvolvedor do futuro não será avaliado pela quantidade de código que escreve, mas pela qualidade das decisões que toma."

Isso porque o código em si se torna commodity — o diferencial está em:

1. **Saber o que construir** (Product Discovery)
2. **Saber como arquitetar** (Enterprise Architecture)
3. **Saber o que delegar** (Agent Orchestration)
4. **Saber validar o resultado** (Auditing & Review)

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
| Curva de aprendizado | Anos para dominar stack | Dias para configurar agentes |
| Testes | Muitas vezes negligenciados | Gerados e mantidos pelos agentes |

### O paradoxo da produtividade

Dados da pesquisa Stack Overflow 2024 mostram:

- **63%** dos desenvolvedores reportam que código gerado por IA frequentemente contém erros inesperados
- **40%** dos projetos com IA sem configuração adequada têm retrabalho
- **~3%** de erro quando o time define **12+ regras** de projeto (AGENTS.md, .cursorrules, etc.)

**Conclusão:** IA não elimina a necessidade de engenharia de qualidade — ela a torna mais importante do que nunca.

---

## 3. O papel do arquiteto

O arquiteto de software no mundo dos agentes não desapareceu — ele se tornou **mais estratégico**.

### Responsabilidades do Arquiteto

```
┌─────────────────────────────────────────────┐
│           ARQUITETO DE SOFTWARE              │
├─────────────────────────────────────────────┤
│  Antes:                                     │
│  • Escolher tecnologia                      │
│  • Desenhar diagramas                       │
│  • Revisar código                           │
│  • Resolver problemas técnicos              │
├─────────────────────────────────────────────┤
│  Agora (+):                                 │
│  • Definir regras para os agentes           │
│  • Criar templates de prompt                │
│  • Configurar checklists de auditoria       │
│  • Estruturar o workspace para IA           │
│  • Decidir o que delegar vs. o que reter    │
│  • Validar outputs dos agentes              │
└─────────────────────────────────────────────┘
```

### Decisões que o arquiteto **não pode** delegar

1. **Visão arquitetural** — o "desenho grande" do sistema
2. **Trade-offs críticos** — custo vs. performance vs. prazo
3. **Padrões e convenções** — o "jeito certo" de fazer as coisas
4. **Revisão estratégica** — o que entra e o que fica para depois
5. **Contexto de negócio** — o "porquê" por trás das decisões técnicas

### Decisões que o arquiteto **deve** delegar

1. **Implementação de CRUDs** — agentes geram com consistência
2. **Testes unitários** — agentes cobrem edge cases
3. **Documentação técnica** — agentes mantêm atualizada
4. **Validação de boas práticas** — checklists automáticos
5. **Refatoração de código legado** — agentes aplicam padrões

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
| Comunicação com time | Reuniões longas | Documentação assíncrona gerada por agentes |

### O PO define o "o quê", não o "como"

Com agentes, o PO pode:
1. Descrever o problema em linguagem natural
2. Um agente de discovery transforma em user stories
3. Um agente de design gera wireframes
4. Um agente de arquitetura valida a viabilidade
5. O time implementa com agentes especializados

---

## 5. O papel da IA

A IA não é um substituto — é um **membro do time** com habilidades específicas.

### Como a IA deve ser posicionada

```
NÃO:  "A IA vai substituir os desenvolvedores"
SIM:  "A IA é um desenvolvedor júnior infinitamente rápido e disposto,
       que precisa de supervisão técnica e contexto de negócio"
```

### O que a IA faz bem

- Geração de código repetitivo e padronizado
- Cobertura de edge cases em testes
- Documentação técnica
- Refatoração sistemática
- Revisão de boas práticas
- Sugestão de padrões e soluções conhecidas

### Onde a IA falha

- Compreensão profunda de negócio
- Decisões com contextos contraditórios
- Inovação fora dos padrões conhecidos
- Responsabilidade e ownership
- Compreensão de implicações de longo prazo

---

## 6. Como dividir trabalho entre humanos e agentes

### A Matriz de Delegação

```
                  Alta complexidade
                        │
    HUMANO DECIDE       │   HUMANO + AGENTE
    (o que construir)   │   (arquitetura, revisão)
                        │
────────────────────────┼─────────────────────────
                        │
    AGENTE FAZ          │   AGENTE DECIDE
    (CRUD, testes)      │   (formatação, lint)
                        │
                  Baixa complexidade

                Baixo risco              Alto risco
```

### Regras de ouro

1. **O humano decide o "quê" e o "porquê"** — o agente executa o "como"
2. **Sempre revisar o output do agente** — especialmente em produção
3. **Quanto maior o risco, mais supervisão humana**
4. **Crie checklists para os agentes seguirem** — eles seguem regras melhor que humanos
5. **Documente as regras** em AGENTS.md, .cursorrules, opencode.json
6. **Itere** — ajuste as regras conforme os agentes aprendem o contexto

---

## 7. O ciclo de desenvolvimento com agentes

O ciclo completo que usaremos na formação:

```
┌─────────────────────────────────────────────────────────┐
│                 CICLO DE DESENVOLVIMENTO                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. Product Discovery  ←→  2. Design (UX/UI)           │
│         │                           │                   │
│  3. Arquitetura  ←→  4. Modelagem de Dados              │
│         │                           │                   │
│  5. Implementação (Backend/Frontend)                     │
│         │                                                │
│  6. Segurança  ←→  7. Testes                            │
│         │                                                │
│  8. DevOps  ←→  9. Deploy                               │
│         │                                                │
│  10. Auditoria  ←→  11. Refatoração                     │
│                                                         │
│  Cada etapa usa agentes especializados                   │
│  Cada etapa produz artefatos revisáveis                  │
│  Cada etapa alimenta a próxima                           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

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

### O que você NÃO vai aprender

- Sintaxe básica de JavaScript/TypeScript (presume-se conhecimento)
- Configuração de ambiente de desenvolvimento
- Conceitos fundamentais de programação

### O formato

- **Módulos práticos** com exercícios e projetos
- **Agentes pré-configurados** para cada etapa
- **Auditoria** como mecanismo de qualidade
- **Projeto final** unificando todos os conceitos

---

## Resumo

1. A IA mudou o papel do desenvolvedor de **escritor de código** para **orquestrador de agentes**
2. O arquiteto se torna ainda mais importante — define as regras que os agentes seguem
3. O PO ganha ferramentas para especificar com mais precisão
4. A divisão de trabalho segue a **Matriz de Delegação** (complexidade x risco)
5. O ciclo de desenvolvimento com agentes é mais iterativo e com mais pontos de validação
6. Código gerado por IA sem governança tem **40% de erro** — com regras cai para **~3%**
