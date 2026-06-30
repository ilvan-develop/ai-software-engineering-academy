# Projeto Pratico — Módulo 09 — Modelagem de Dados: Prisma e PostgreSQL

---

## Visao Geral

**Tema:** Módulo 09 - Modelagem de Dados: Prisma e PostgreSQL
**Duracao estimada:** 8-12 horas
**Dificuldade:** Intermediario/Avancado
**Linguagem:** text

---

## Contexto

Voce foi contratado como arquiteto de software para construir um sistema enterprise que aplica os conceitos de **Módulo 09 - Modelagem de Dados: Prisma e PostgreSQL**. Este projeto simula um cenario real onde voce precisa tomar decisoes arquiteturais, implementar solucoes e documentar suas escolhas.

**Cenario:** Uma empresa de medio porte precisa modernizar sua plataforma. O sistema atual e legado e nao atende mais as necessidades de escalabilidade e manutencao. Sua missao e projetar e implementar uma nova solucao seguindo as melhores praticas do modulo.

---

## Requisitos Funcionais

1. O sistema deve atender aos casos de uso principais do modulo
2. Deve implementar corretamente os conceitos de 1. Por que modelagem importa
3. Deve incluir tratamento de erros e casos de borda
4. Deve ter uma API bem definida (REST ou GraphQL)
5. Deve incluir documentacao de uso

## Requisitos Nao-Funcionais

1. Codigo limpo e seguindo principios SOLID
2. Testes unitarios para as principais funcionalidades
3. Documentacao clara das decisoes arquiteturais
4. Tratamento adequado de erros e excecoes
5. Seguir as convencoes do ecossistema {lang}

---

## Entregaveis

| # | Entregavel | Descricao | Peso |
|---|------------|-----------|------|
| 1 | Codigo Fonte | Implementacao completa do sistema | 40% |
| 2 | Documentacao | README, ADRs, diagramas | 20% |
| 3 | Testes | Testes unitarios e de integracao | 20% |
| 4 | Apresentacao | Pitch tecnico (5 min) | 10% |
| 5 | Deploy | Pipeline CI/CD configurado | 10% |

---

## Estrutura Esperada

```
projeto-módulo-09---modelagem-de-dados:-prisma-e-postgresql/
├── src/
│   ├── core/          # Logica de dominio
│   ├── application/   # Casos de uso
│   ├── infrastructure/# Adaptadores e frameworks
│   └── index.ts       # Entry point
├── tests/
│   ├── unit/
│   └── integration/
├── docs/
│   ├── ADR-001.md     # Decision records
│   └── arch.md        # Diagrama arquitetural
├── .github/
│   └── workflows/     # CI/CD
├── README.md
├── package.json
└── tsconfig.json
```

---

## Rubrica de Avaliacao

| Criterio | Peso | Insuficiente (0-4) | Adequado (5-7) | Excelente (8-10) |
|----------|------|-------------------|-----------------|-------------------|
| Correcao tecnica | 30% | Nao implementa 1. Por que modelagem importa corretamente | Implementa mas com falhas | Implementacao robusta e completa |
| Arquitetura | 25% | Sem separacao de camadas | Camadas definidas mas com vazamentos | Clean Architecture bem aplicada |
| Qualidade do codigo | 15% | Codigo desorganizado | Boas praticas inconsistentes | SOLID, DRY, nomes claros |
| Testes | 10% | Sem testes | Testes basicos | Cobertura > 80%, mocks bem usados |
| Documentacao | 10% | Sem docs | README basico | ADRs, diagramas, exemplos |
| Apresentacao | 5% | Nao apresentou | Explicou mas sem profundidade | Pitch claro com justificativas |
| Deploy/CI | 5% | Sem pipeline | Pipeline basico | CI/CD completo com quality gates |

**Nota minima para aprovacao:** 7.0

---

## Entregas Parciais (Opcional)

| Entrega | Prazo | Conteudo |
|---------|-------|---------|
| Design Review | Dia 3 | Documento de arquitetura + diagramas |
| Code Review | Dia 5 | Implementacao principal + testes |
| Entrega Final | Dia 7 | Codigo completo + apresentacao |

---

## Criterios de Correcao Detalhados

### 1. Correcao Tecnica (30%)

- A solucao resolve o problema proposto?
- Os conceitos do modulo foram aplicados corretamente?
- Existem bugs ou falhas de logica?
- Edge cases foram tratados?

### 2. Arquitetura (25%)

- A separacao de camadas e clara e consistente?
- As dependencias seguem a direcao correta?
- Os padroes de projeto foram usados adequadamente?
- A arquitetura e testavel e extensivel?

### 3. Qualidade do Codigo (15%)

- O codigo e legivel e bem formatado?
- Os nomes de variaveis/funcoes sao descritivos?
- Principios SOLID foram seguidos?
- Nao ha duplicacao desnecessaria?

### 4. Testes (10%)

- Os testes cobrem as principais funcionalidades?
- Testes sao independentes e deterministicos?
- Mocks/stubs sao usados adequadamente?
- Ha casos de borda sendo testados?

### 5. Documentacao (10%)

- README explica como rodar e testar?
- ADRs documentam decisoes importantes?
- Diagramas ilustram a arquitetura?
- Exemplos de uso sao fornecidos?

### 6. Apresentacao (5%)

- O pitch e claro e objetivo?
- As decisoes tecnicas sao justificadas?
- Trade-offs sao discutidos abertamente?

### 7. Deploy/CI (5%)

- Pipeline CI esta funcional?
- Qualidade e verificada automaticamente?
- Ha deploy automatizado para algum ambiente?

---

## Dicas

- Comece pelo esboco da arquitetura antes de codificar
- Documente as decisoes a medida que sao tomadas
- Teste primeiro as partes mais criticas do sistema
- Prepare a apresentacao como se fosse para um comite executivo
- Use o modulo como referencia, mas nao se limite a ele
