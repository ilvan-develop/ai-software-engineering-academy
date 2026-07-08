# Certificação — Governança & Automação

## Prova Objetiva (20 questões)

**Tempo estimado:** 60 minutos  
**Mínimo para aprovação:** 70% (14/20)  
**Pré-requisito:** Conclusão dos módulos 17 a 20

---

### Questão 1
O que é governança de software?
a) Um conjunto de políticas, processos e controles para alinhar tecnologia com objetivos de negócio e gerenciar riscos
b) Um framework de desenvolvimento
c) Uma ferramenta de deploy
d) Um padrão de código

**Gabarito:** A

### Questão 2
O que é um Quality Gate?
a) Um portão de qualidade que define critérios mínimos para aprovação em cada etapa do pipeline editorial
b) Uma ferramenta de teste
c) Um repositório de código
d) Um tipo de deploy

**Gabarito:** A

### Questão 3
O que são Agentes de IA no contexto da academia?
a) Agentes autônomos especializados que executam tarefas específicas na cadeia editorial
b) Chatbots genéricos
c) Ferramentas de busca
d) Sistemas de recomendação

**Gabarito:** A

### Questão 4
O que é uma auditoria técnica?
a) Uma revisão sistemática para verificar conformidade com padrões, boas práticas e requisitos
b) Uma reunião de status
c) Uma ferramenta de teste
d) Um relatório financeiro

**Gabarito:** A

### Questão 5
Qual o objetivo da automação em qualidade?
a) Reduzir erro humano, aumentar consistência e escalar revisões sem aumento proporcional de recursos
b) Substituir completamente revisão humana
c) Acelerar deploys
d) Reduzir custos de infraestrutura

**Gabarito:** A

### Questão 6
O que é BQS (Book Quality Score)?
a) Um sistema de 16 categorias que avalia a qualidade de livros e módulos editorialmente
b) Um ranking de vendas
c) Uma métrica de performance
d) Um tipo de teste

**Gabarito:** A

### Questão 7
Quantas categorias o BQS avalia?
a) 10
b) 16
c) 20
d) 5

**Gabarito:** B

### Questão 8
O que é um ADR (Architecture Decision Record)?
a) Um registro de decisão arquitetural incluindo contexto, opções e justificativa
b) Um documento de requisitos
c) Um bug report
d) Um relatório de auditoria

**Gabarito:** A

### Questão 9
Qual o papel de um auditor editorial?
a) Verificar consistência, precisão e aderência a padrões em todo o conteúdo produzido
b) Escrever conteúdo
c) Programar pipelines
d) Gerenciar equipe

**Gabarito:** A

### Questão 10
O que é um agente orquestrador?
a) Um agente que coordena múltiplos agentes especializados para executar um fluxo de trabalho
b) Um framework de IA
c) Um tipo de LLM
d) Uma ferramenta de deploy

**Gabarito:** A

### Questão 11
O que a categoria `progressao_pedagogica` avalia no BQS?
a) Se o conteúdo tem objetivos claros, sequência didática e adequação ao público
b) A quantidade de diagramas
c) A formatação do markdown
d) A qualidade dos metadados

**Gabarito:** A

### Questão 12
O que significa "gate passa/não passa" em um pipeline editorial?
a) Um critério binário que determina se o artefato avança ou precisa ser corrigido
b) Uma nota de 0-100
c) Uma revisão opcional
d) Um status de deploy

**Gabarito:** A

### Questão 13
Por que usar agentes especializados em vez de um único agente geral?
a) Agentes especializados têm foco, contexto e ferramentas específicas para cada tarefa, aumentando precisão
b) Agentes gerais são proibidos
c) Especialização reduz custo
d) Agentes especializados são mais rápidos

**Gabarito:** A

### Questão 14
O que é um "gap" em um contexto editorial?
a) Uma lacuna entre o estado atual e o desejado (score, conteúdo ou processo faltante)
b) Um erro de código
c) Uma falha de segurança
d) Um bug no sistema

**Gabarito:** A

### Questão 15
O que o módulo de automação cobre?
a) Automação de qualidade, pipelines, CI/CD editorial e orquestração de agentes
b) Automação residencial
c) Robótica industrial
d) Automação de marketing

**Gabarito:** A

### Questão 16
Qual a diferença entre verificação e validação?
a) Verificação: "fizemos certo?"; Validação: "fizemos a coisa certa?"
b) São sinônimos
c) Validação é técnica
d) Verificação é manual

**Gabarito:** A

### Questão 17
O que é rastreabilidade em auditoria?
a) A capacidade de rastrear cada artefato desde sua origem até o output final
b) Um log de erros
c) Uma métrica de performance
d) Um sistema de versionamento

**Gabarito:** A

### Questão 18
O que o BQS avalia em `qualidade_markdown`?
a) Validade do markdown, language tags em code blocks, links e formatação
b) Apenas links quebrados
c) A gramática do texto
d) A estrutura visual

**Gabarito:** A

### Questão 19
O que é um gatekeeper em QA editorial?
a) O agente que aplica os critérios mínimos de qualidade e bloqueia artefatos que não passam
b) Um segurança do prédio
c) Um revisor de código
d) Um gerente de projeto

**Gabarito:** A

### Questão 20
Qual o objetivo final da governança editorial com IA?
a) Produzir conteúdo de alta qualidade de forma consistente, escalável e auditável
b) Eliminar editores humanos
c) Reduzir custo a zero
d) Automatizar tudo sem supervisão

**Gabarito:** A

---

## Prova Prática — Projeto

**Título:** Quality Gate Pipeline

**Descrição:** Projete um pipeline de quality gates para um curso completo:
1. Defina 5 gates com critérios de aprovação
2. Configure um agente orquestrador que decide o próximo gap
3. Crie uma auditoria de consistência entre módulos
4. Defina métricas BQS customizadas para o contexto
