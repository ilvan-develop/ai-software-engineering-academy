# Módulo 18 — Slides

---

## Slide 1: Título

**Agentes de IA**
Construindo seu exército de agentes especializados

---

## Slide 2: Agente genérico vs. especializados

```yaml
Genérico:                     Especializados:
Frontend: ⭐⭐                 Frontend: ⭐⭐⭐⭐⭐
Backend:  ⭐⭐⭐                Backend:  ⭐⭐⭐⭐⭐
Segurança: ⭐                  Segurança: ⭐⭐⭐⭐⭐
Banco:    ⭐⭐                  Banco:    ⭐⭐⭐⭐⭐
DevOps:   ⭐                    DevOps:   ⭐⭐⭐⭐⭐
```markdown

Código "funciona" vs. código de produção

---

## Slide 3: Anatomia de um agente

```text
┌──────────────────────────────┐
│  IDENTIDADE                  │
│  → Quem é, o que sabe, limites│
├──────────────────────────────┤
│  CONHECIMENTO                │
│  → Stack, padrões, referências│
├──────────────────────────────┤
│  PROCESSO                    │
│  → Fluxo de trabalho         │
├──────────────────────────────┤
│  QUALIDADE                   │
│  → Checklist, critérios      │
├──────────────────────────────┤
│  COMUNICAÇÃO                 │
│  → Formato entrada/saída     │
└──────────────────────────────┘
```markdown

---

## Slide 4: Os 17 agentes (parte 1)

**Produto:** Product Discovery, UX Research
**Design:** UX Designer, UI Designer
**Arquitetura:** Enterprise Architect, Database Architect
**Desenvolvimento:** Backend, Frontend, Prisma

---

## Slide 5: Os 17 agentes (parte 2)

**Infraestrutura:** DevOps, Security
**Qualidade:** QA, Performance
**Governança:** Auditor, Documentation, Refactoring

---

## Slide 6: Como criar um agente

1. Definir o DOMÍNIO
2. Definir o CONHECIMENTO BASE
3. Definir RESPONSABILIDADES e LIMITES
4. Definir o PROCESSO
5. Criar CHECKLIST
6. Criar TEMPLATES DE PROMPT
7. TESTAR com caso real

---

## Slide 7: Exemplo de agente bem definido

**Security Expert Agent**

```yaml
Domínio: Segurança de aplicações web
Conhecimento: OWASP Top 10, JWT, bcrypt, Helmet
Responsabilidades:
  ✅ Autenticação, autorização, rate limiting
  ❌ Arquitetura, lógica de negócio, infra
Checklist:
  - [ ] Senhas com bcrypt
  - [ ] JWT com expiração curta
  - [ ] CSP e Helmet configurados
```markdown

---

## Slide 8: Pipeline de features

```text
Product Discovery → UX Designer → UI Designer
         ↓
Enterprise Architect
         ↓
Backend + Frontend + Prisma + Security
         ↓
QA → DevOps → Auditor → Documentation
```markdown

Cada etapa: agente certo, artefato certo, qualidade certa

---

## Slide 9: Prompt eficaz vs. ineficaz

```yaml
RUIM: "Crie uma API de usuários."

BOM: "Crie API REST com NestJS + Clean Architecture.
      Endpoints: CRUD + soft delete.
      Validações: email único, senha 8+ chars.
      Stack: Prisma + Zod + Swagger.
      Regras: tratamento de erros com filters."
```markdown

---

## Slide 10: O futuro: Meta-Agent

**Agentes que criam agentes**

```text
1. Meta-Agent analisa o problema
2. Identifica domínios necessários
3. Cria agente para cada domínio
4. Define limites e responsabilidades
5. Testa e ajusta cada agente
6. Combina em pipeline
7. Executa o pipeline completo
```markdown

---

## Slide 11: Para refletir

> "O melhor desenvolvedor não é aquele que escreve o melhor código, mas aquele que **orquestra os melhores agentes** para escrever o melhor código."

> "Cada agente é um especialista contratado. O arquiteto é quem decide **quando** chamar **qual** especialista."

---

## Slide 12: Próximos passos

1. Estudar cada agente da biblioteca
2. Praticar: criar um novo agente do zero
3. Módulo 19: Auditorias — como medir a qualidade
4. Módulo 20: Automação — pipelines completos
5. Módulo 21: Projeto Final — tudo junto
