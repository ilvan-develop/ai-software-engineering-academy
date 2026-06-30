# Exercicios - Capitulo 2: Agentes de IA na Pratica

> **Modulo:** IA para Desenvolvedores  
> **Total de exercicios:** 5  
> **Progressao:** Facil -> Medio -> Dificil  
> **Tempo total estimado:** 80-110 min

---

## Exercicio 1 - Facil: Quem Chama Quem?

**Tempo estimado:** 10 min  
**Tema:** Identificar o agente certo para cada tarefa

### Contexto

Voce tem acesso aos 17 agentes especializados da biblioteca (Product Discovery, UX Research, UX Designer, UI Designer, Enterprise Architect, Database Architect, Backend Expert, Frontend Expert, Prisma Expert, DevOps Expert, Security Expert, QA Expert, Performance Expert, Auditor, Documentation, Refactoring). Cada tarefa abaixo deve ser atribuida ao agente mais adequado.

### Tarefa

Para cada tarefa, indique qual agente deve ser usado e em qual categoria ele se encaixa (Produto, Design, Arquitetura, Desenvolvimento, Infraestrutura, Qualidade, Governanca).

| # | Tarefa | Agente | Categoria |
|---|--------|--------|-----------|
| 1 | Modelar schema do banco de dados | | |
| 2 | Testar fluxo de checkout com Playwright | | |
| 3 | Revisar seguranca do endpoint de login | | |
| 4 | Escrever ADR sobre decisao de arquitetura | | |
| 5 | Otimizar consulta SQL que esta lenta | | |
| 6 | Criar Dockerfile e pipeline CI | | |
| 7 | Validar hipotese de produto com usuarios | | |
| 8 | Refatorar componente complexo em partes menores | | |
| 9 | Definir user stories e criterios de aceite | | |
| 10 | Projetar layout responsivo com Design System | | |

### Template

```
| # | Tarefa | Agente | Categoria |
|---|--------|--------|-----------|
| 1 | Modelar schema do BD | | |
```

### Criterios de correcao

| Criterio | Peso |
|----------|------|
| Agente correto para cada tarefa | 60% |
| Categoria correta | 40% |

Nota minima: 8/10 acertos.

### Gabarito

| # | Agente | Categoria |
|---|--------|-----------|
| 1 | Database Architect | Arquitetura |
| 2 | QA Expert | Qualidade |
| 3 | Security Expert | Infraestrutura |
| 4 | Documentation | Governanca |
| 5 | Performance Expert | Qualidade |
| 6 | DevOps Expert | Infraestrutura |
| 7 | UX Research | Produto |
| 8 | Refactoring | Governanca |
| 9 | Product Discovery | Produto |
| 10 | UI Designer | Design |

---

## Exercicio 2 - Facil/Medio: Anatomia de um Agente

**Tempo estimado:** 15 min  
**Tema:** Entender a estrutura padrao de agentes

### Contexto

Cada agente da biblioteca segue: README.md (identidade), workflow.md (processo), checklist.md (qualidade), prompts/ (templates).

### Tarefa

Para o agente **Security Expert**, complete os componentes abaixo:

```
1. IDENTIDADE
   - Proposito:
   - Stack/Conhecimento:
   - Responsabilidades:
   - Limites:

2. PROCESSO
   - Entrada:
   - Fluxo:
   - Saida:

3. QUALIDADE (checklist, minimo 6 intens):

4. COMUNICACAO: template de prompt para revisar seguranca de um endpoint
```

### Criterios de correcao

| Criterio | Peso |
|----------|------|
| Proposito claro e especifico | 15% |
| Stack/Conhecimento alinhado | 15% |
| Responsabilidades e limites definidos | 20% |
| Fluxo de trabalho logico | 20% |
| Checklist com >= 6 intens | 15% |
| Template de prompt viavel | 15% |

### Gabarito

**Proposito:** Garantir protecao contra OWASP Top 10
**Stack:** JWT, OAuth2, bcrypt, Helmet, CORS, CSP, rate limiting
**Responsabilidades:** Implementar auth, prevenir SQLi/XSS/CSRF, rate limiting
**Limites:** Nao define arquitetura, nao implementa regras de negocio, nao gerencia infra

**Checklist:** Senhas bcrypt, JWT curto + refresh, rate limiting login, CSP header, Helmet, input validation, SQLi prevenido, CORS whitelist

**Prompt:** "Revise seguranca do POST /api/login. Verifique: rate limiting, validacao input, https, headers seguranca, tratamento erros (nao vazar info)."

---

## Exercicio 3 - Medio: Composicao de Agentes em Pipeline

**Tempo estimado:** 20 min  
**Tema:** Combinar agentes em pipeline para uma feature completa

### Contexto

O Product Owner descreveu o problema: "Precisamos de uma funcionalidade de recuperacao de senha. O usuario clica em esqueci senha, recebe um email com link temporario, cria nova senha e e redirecionado ao login."

### Tarefa

Projete um pipeline de agentes que transforme essa descricao em codigo em producao. Inclua:

1. **Pipeline completo** - Quais agentes, em que ordem? (minimo 5 agentes)
2. **Entrada e saida de cada etapa** - O que cada agente recebe e entrega?
3. **Ponto de revisao humana** - Onde um humano deve validar antes de prosseguir?
4. **Criterio de aceite** - Como saber se o pipeline terminou com sucesso?

### Template

```
### Pipeline: Recuperacao de Senha

Etapa 1: [Agente]
  Entrada:
  Saida:
  Revisao humana: [Sim/Nao - porque]

Etapa 2: [Agente]
  ...

### Criterio de aceite final:
```

### Criterios de correcao

| Criterio | Peso |
|----------|------|
| Pipeline com >= 5 agentes em ordem logica | 30% |
| Entrada/saida definidas para cada etapa | 25% |
| Pontos de revisao humana identificados | 20% |
| Criterio de aceite claro e mensuravel | 15% |
| Clareza e completude | 10% |

### Gabarito (resumo)

1. **Product Discovery** - User stories + acceptance criteria
2. **UX Designer** - Fluxo de telas (wireframes)
3. **UI Designer** - Mockups com Design System
4. **Security Expert** - Token de reset, expiracao, rate limit
5. **Backend Expert** - API de reset senha
6. **Frontend Expert** - Componente de formulario
7. **QA Expert** - Testes e2e do fluxo completo
8. **Auditor** - Revisao final de seguranca
9. **DevOps Expert** - Deploy

Review humano: entre UX Designer e UI Designer (validar fluxo com PO), e antes do deploy (QA aprovou?).

---

## Exercicio 4 - Medio/Dificil: Criar um Novo Agente do Zero

**Tempo estimado:** 25 min  
**Tema:** Criar agente especializado seguindo a estrutura padrao

### Contexto

Sua equipe identificou a necessidade de um agente especializado em **Mobile Performance** para otimizar apps React Native. Nao existe na biblioteca atual.

### Tarefa

Crie o agente completo seguindo os 7 passos do capitulo:

1. Defina o **dominio** do agente
2. Defina o **conhecimento base** (ferramentas, metricas, padroes)
3. Defina **responsabilidades** e **limites**
4. Defina o **processo** (entrada -> transformacao -> saida)
5. Crie o **checklist de qualidade** (minimo 8 intens)
6. Crie **2 templates de prompt** para tarefas comuns
7. **Teste** com um cenario: "App React Native esta lento na tela de listagem de produtos. O FlatLayout trava ao scrollar com 100+ itens."

### Template

```
# Agente: Mobile Performance Expert

## Dominio

## Conhecimento Base

## Responsabilidades

## Limites

## Processo

## Checklist de Qualidade

## Templates de Prompt
### Prompt 1: Diagnosticar lentidao
### Prompt 2: Otimizar componente

## Teste: Cenario da listagem de produtos
```

### Criterios de correcao

| Criterio | Peso |
|----------|------|
| Dominio e conhecimento base pertinentes | 15% |
| Responsabilidades e limites claros | 15% |
| Processo bem definido | 20% |
| Checklist com >= 8 intens verificaveis | 20% |
| Templates de prompt iveis | 15% |
| Teste com cenario demonstra aplicacao pratica | 15% |

### Gabarito (trechos)

**Dominio:** Performance de aplicacoes React Native
**Conhecimento:** Hermes engine, FlatList otimizacao, FlashList, useMemo/useCallback, FPS monitor, RAM profiles, bundle size, imagem otimizacao

**Responsabilidades:** Diagnosticar causas de lentidao, otimizar renderizacao, reduzir bundle, melhorar tempo de inicializacao
**Limites:** Nao modifica logica de negocios, nao faz redesign UI, nao configura infra

**Checklist:**
- [ ] FlatList usando getItemLayout, keyExtractor, windowSize otimizado
- [ ] Imagens com cache e tamanho adequado
- [ ] Sem re-renders desnecessarios (React.memo/useMemo)
- [ ] Bundle size analisado e abaixo do limite
- [ ] FPS mantido em 60fps no cenario de uso tipico
- [ ] Hermes engine habilitado
- [ ] FlashList considerado para listas grandes > 50 intens
- [ ] Teste de performance no device real (nao emulador)

---

## Exercicio 5 - Dificil: Configurar Agentes no OpenCode + Pipeline de Revisao Cruzada

**Tempo estimado:** 30 min  
**Tema:** Integracao com OpenCode e revisao entre agentes

### Contexto

Sua equipe vai adotar o OpenCode com agentes especializados. Voce precisa:

1. Configurar 3 agentes no opencode.json
2. Definir permissoes adequadas para cada um
3. Projetar um fluxo de revisao cruzada onde um agente revisa o trabalho do outro

### Tarefa

Parte A - Configuracao (valendo 40%):
Crie a configuracao opencode.json para 3 agentes:
- **backend-expert**: tem acesso total (bash, read, edit, glob, grep)
- **security-auditor**: pode ler e revisar (bash, read, glob, grep), mas NAO pode editar
- **qa-expert**: pode ler e executar testes (bash, read, glob, grep), editar apenas arquivos de teste

Parte B - Pipeline de revisao (valendo 60%):
Um dev criou um novo endpoint PATCH /api/users/:id. Descreva:
1. Prompt para o backend-expert criar o endpoint (incluindo contexto, validacoes, regras)
2. Prompt para o security-auditor revisar o endpoint (o que verificar?)
3. Prompt para o qa-expert criar testes (quais cenarios?)
4. Fluxo: o que acontece se security-auditor encontra um blocker? E se QA encontra falha?

### Template

```json
// Parte A: opencode.json
{
  "agents": {
    "backend-expert": { ... },
    "security-auditor": { ... },
    "qa-expert": { ... }
  }
}
```

```
// Parte B: Pipeline
1. Prompt para backend-expert:
2. Prompt para security-auditor:
3. Prompt para qa-expert:
4. Fluxo de falha:
```

### Criterios de correcao

| Criterio | Peso |
|----------|------|
| Configuracao JSON valida e bem estruturada | 15% |
| Permissoes adequadas ao papel de cada agente | 25% |
| Prompts de alta qualidade (contexto + intencao + formato) | 25% |
| Fluxo de revisao e tratamento de falhas logicos | 25% |
| Clareza e organizacao | 10% |

### Gabarito

```json
{
  "agents": {
    "backend-expert": {
      "prompt": ".opencode/agents/backend-expert.md",
      "permissions": { "bash": true, "read": true, "edit": true, "glob": true, "grep": true }
    },
    "security-auditor": {
      "prompt": ".opencode/agents/security-auditor.md",
      "permissions": { "bash": true, "read": true, "edit": false, "glob": true, "grep": true }
    },
    "qa-expert": {
      "prompt": ".opencode/agents/qa-expert.md",
      "permissions": { "bash": true, "read": true, "edit": true, "glob": true, "grep": true }
    }
  }
}
```

**Prompt backend-expert:** "Crie PATCH /api/users/:id em NestJS. Valide corpo com Zod (name opcional, email opcional com formato). Use Prisma para persistencia. Retorne 200 com dados atualizados, 404 se id nao existir. Erros com exception filters."

**Prompt security-auditor:** "Revise o endpoint PATCH /api/users/:id. Verifique: authorization (so o proprio usuario ou admin pode editar?), injection (parametros sanitizados?), rate limiting, vazamento de dados sensiveis na resposta."

**Prompt qa-expert:** "Crie testes para PATCH /api/users/:id. Cenarios: atualizacao bem-sucedida, usuario inexistente (404), email invalido (400), sem autorizacao (401/403), concorrencia (dois updates simultaneos)."

**Fluxo de falha:** Se security blocker -> volta para backend-expert corrigir -> security re-revisa. Se QA blocker -> volta para backend-expert -> QA re-testa. So merge quando ambos aprovam.

---

## Exercicio 6 - Medio: Sistema de Delegacao com Fallback entre Agentes

**Tempo estimado:** 20 min  
**Tema:** Criar regras de delegacao e fallback quando um agente nao pode resolver

### Contexto
Voce projetou um sistema com 5 agentes especializados, mas em alguns cenarios o agente principal nao consegue executar a tarefa sozinho. Exemplos:

- **Security Expert** encontra uma vulnerabilidade que requer mudanca na arquitetura
- **Backend Expert** precisa de decisao de UX para definir o fluxo de erro
- **Frontend Expert** precisa de assets do UI Designer que nao existem
- **QA Expert** encontra um bug que pode ser tanto de frontend quanto de backend

### Tarefa
Para cada cenario:

1. Defina a **regra de delegacao**: quando o agente A deve chamar o agente B?
2. Defina o **formato da mensagem** entre agentes (o que um agente entrega para o outro?)
3. Defina o **criterio de fallback**: o que acontece se o agente B tambem nao conseguir resolver?
4. Crie um **exemplo de conversa** entre os 2 agentes usando o formato definido

### Template
```
### Cenario 1: Security encontra vulnerabilidade arquitetural
Regra de delegacao:
Formato da mensagem:
Criterio de fallback:
Exemplo de conversa:
[Security Expert] ->
[Enterprise Architect] ->
```

### Criterios de Correcao
| Criterio | Peso |
|----------|------|
| Regras de delegacao claras e justificadas | 30% |
| Formato de mensagem estruturado e reutilizavel | 25% |
| Criterio de fallback realista | 20% |
| Exemplo de conversa demonstra o protocolo | 25% |

### Gabarito (Cenario 1)
**Regra:** Security Expert delega ao Enterprise Architect quando a correcao requer mudanca na arquitetura (ex: adicionar API Gateway, mudar de monolitho para microservices). Seguranca nao decide arquitetura.
**Formato:** `{ "de": "security-expert", "para": "enterprise-architect", "tipo": "delegacao", "contexto": "endpoint /api/users", "problema": "SQL injection via raw query", "impacto": "Alto - requer prepared statements em toda a camada de dados", "decisao_necessaria": "Adotar Prisma + query builders em vez de raw SQL?" }`
**Fallback:** Se Enterprise Architect nao resolver, sobe para o humano (tech lead) com o resumo do debate.
**Conversa:**
- Security: `{ "de": "security-expert", "problema": "SQL injection detectado...", "decisao_necessaria": "...", "alternativas": ["Prisma queries", "Prepared statements manuais", "ORM + validator"] }`
- Architect: `{ "de": "enterprise-architect", "decisao": "Adotar Prisma queries com validador Zod", "justificativa": "Prisma ja previne SQLi, mantem produtividade, alinhado com stack existente", "acoes": ["Remover raw queries", "Substituir por Prisma findMany/findUnique", "Adicionar regra no AGENTS.md"] }`

---
## Exercicio 7 - Medio: Auditoria de Prompts de Agentes

**Tempo estimado:** 20 min  
**Tema:** Avaliar e melhorar prompts de agentes existentes

### Contexto
Voce encontrou os prompts abaixo em um repositorio de agentes. Todos tem problemas de qualidade.

```
### Prompt do Agente "Database Expert"
"cria banco"

### Prompt do Agente "Security Auditor"
"verifica seguranca"

### Prompt do Agente "Code Reviewer"
"revisa esse codigo"

### Prompt do Agente "DevOps Expert"
"faz deploy"

### Prompt do Agente "UX Researcher"
"pesquisa usuario"
```

### Tarefa
Para CADA agente:

1. Identifique o(s) **componente(s) da anatomia** que estao faltando (Identidade? Conhecimento? Processo? Qualidade? Comunicacao?)
2. Avalie o risco de usar esse prompt como esta: Baixo / Medio / Alto
3. Reescreva o prompt completo seguindo a estrutura padrao do capitulo:
   - Proposito (Identidade)
   - Stack/Conhecimento
   - Responsabilidades e Limites
   - Processo (Entrada -> Fluxo -> Saida)
   - Qualidade (checklist minimo 5 intens)
   - Template de comunicacao

Voce pode escolher 3 dos 5 agentes para reescrever (os outros 2 apenas identifique os problemas).

### Template
```
### Agente: [Nome]
**Componentes faltando:**
**Risco:**
**Prompt reescrito completo:**
## Identidade
## Conhecimento
## Responsabilidades
## Limites
## Processo
## Checklist
## Comunicacao
```

### Criterios de Correcao
| Criterio | Peso |
|----------|------|
| Identificacao correta dos componentes faltando | 25% |
| Avaliacao de risco coerente | 10% |
| Prompt reescrito tem todos os 5 componentes | 40% |
| Checklist com >= 5 intens verificaveis | 15% |
| Clareza e especificidade | 10% |

### Gabarito (Database Expert)
**Faltando:** Tudo (apenas intencao vaga, sem identidade, processo, qualidade ou comunicacao)
**Risco:** Alto - prompt "cria banco" pode gerar schema sem indices, sem normalizacao, sem migracoes

**Prompt reescrito:**
```
## Identidade
Proposito: Modelar e otimizar bancos de dados relacionais e NoSQL
Stack: PostgreSQL, MySQL, Prisma ORM, Redis, MongoDB
## Responsabilidades
- Modelar schemas normalizados (3FN)
- Criar migracoes seguras (NUNCA dropar colunas sem warning)
- Otimizar queries (EXPLAIN ANALYZE, indices, N+1)
## Limites
- Nao implementa logica de negocios
- Nao configura infraestrutura (deixa para DevOps Expert)
## Processo
Entrada: Descricao das entidades e relaciamentos
Fluxo: 1. Analisar requisitos de dados 2. Modelar entidades 3. Definir indices 4. Gerar migracao 5. Validar com EXPLAIN
Saida: Schema Prisma + migration SQL + justificativa das escolhas
## Checklist
- [ ] Normalizado ate 3FN (salvo justificativa)
- [ ] Indices para campos de busca e FK
- [ ] Migracao com rollback definido
- [ ] N+1 queries verificados
- [ ] Tipos adequados (NUNCA VARCHAR(255) padrao)
- [ ] Constraints de integridade (FK, UNIQUE, CHECK)
## Comunicacao
Template: "Modele o schema para [entidade]. Relaciamentos: [descricao]. Requisitos: [volume, consistencia, performance]."
```

---

## Resumo - Capitulo 2

| # | Exercicio | Dificuldade | Tema | Tempo |
|---|-----------|-------------|------|-------|
| 1 | Quem Chama Quem? | Facil | Identificar agente para cada tarefa | 10 min |
| 2 | Anatomia de um Agente | Facil/Medio | Estrutura padrao de agentes | 15 min |
| 3 | Pipeline de Agentes | Medio | Composicao em pipeline | 20 min |
| 4 | Criar Agente do Zero | Medio/Dificil | Novo agente especializado | 25 min |
| 5 | OpenCode + Revisao Cruzada | Dificil | Configuracao e pipeline | 30 min |