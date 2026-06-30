# Roteiro de Videoaula — Módulo 15 — QA: Testes e Qualidade

**Duracao total estimada:** 28 minutos
**Formato:** Videoaula gravada / Streaming
**Publico-alvo:** Desenvolvedores intermediarios

---

## Visao Geral do Video

| Item | Detalhe |
|------|---------|
| Titulo | Módulo 15 — QA: Testes e Qualidade |
| Duracao | 28 min |
| Cenas | 11 |
| Formato | Expositivo com demonstracao pratica |
| Nivel | Intermediario |

---

## Roteiro por Cena

### Cena 1 — INTRO

**Duracao:** 1:30

**Narracao:**
> Ola! Nesta aula vamos explorar: Módulo 15 — QA: Testes e Qualidade. Ao final, voce vai entender os conceitos fundamentais e como aplica-los na pratica. Vamos la?

**Visuais:**
- Tela de abertura com titulo do modulo. Animacao suave com o nome do curso.

**Texto na tela:**
```
[TITULO] Módulo 15 — QA: Testes e Qualidade
```

**Notas de direcao:**
- Tom energico e convidativo. Apresentar o problema que sera resolvido.

---

### Cena 2 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 1. Por que testar?. Sem testes: ┌────────────────────────────────────────────┐ │  Bug em produção: 2 dias pra achar         │ │  Correção: 1 hora                          │

**Visuais:**
- Slides com topicos-chave. ```text
Unitários:        70%+ cobertura (services, utils)
Integração:       20% (endpoints, fluxos críticos)
E2E:              10% (fluxos principais, felizes e infelizes)
```

**Texto na tela:**
```
[1. Por que testar?]
```

**Notas de direcao:**
- Secao 2 de 8. Usar exemplos praticos.

---

### Cena 3 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 2. Testes Unitários com Jest. describe('UserService', () => { describe('create', () => { it('deve criar usuário com sucesso', async () => { // Arrange — preparar dados

**Visuais:**
- Slides com topicos-chave. ```text
Unitários:        70%+ cobertura (services, utils)
Integração:       20% (endpoints, fluxos críticos)
E2E:              10% (fluxos principais, felizes e infelizes)
```

**Texto na tela:**
```
[2. Testes Unitários com Jest]
```

**Notas de direcao:**
- Secao 3 de 8. Usar exemplos praticos.

---

### Cena 4 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 3. Testes de Integração com Supertest. import * as request from 'supertest'; import { Test } from '@nestjs/testing'; import { INestApplication } from '@nestjs/common'; describe('UserController (integration)', () => {

**Visuais:**
- Slides com topicos-chave. ```text
Unitários:        70%+ cobertura (services, utils)
Integração:       20% (endpoints, fluxos críticos)
E2E:              10% (fluxos principais, felizes e infelizes)
```

**Texto na tela:**
```
[3. Testes de Integração com Supertest]
```

**Notas de direcao:**
- Secao 4 de 8. Usar exemplos praticos.

---

### Cena 5 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 4. Testes E2E com Playwright. // playwright.config.ts import { defineConfig } from '@playwright/test'; export default defineConfig({ testDir: './e2e',

**Visuais:**
- Slides com topicos-chave. ```text
Unitários:        70%+ cobertura (services, utils)
Integração:       20% (endpoints, fluxos críticos)
E2E:              10% (fluxos principais, felizes e infelizes)
```

**Texto na tela:**
```
[4. Testes E2E com Playwright]
```

**Notas de direcao:**
- Secao 5 de 8. Usar exemplos praticos.

---

### Cena 6 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 5. Cobertura de Código. // jest.config.ts export default { collectCoverageFrom: [ 'src/**/*.service.ts',

**Visuais:**
- Slides com topicos-chave. ```text
Unitários:        70%+ cobertura (services, utils)
Integração:       20% (endpoints, fluxos críticos)
E2E:              10% (fluxos principais, felizes e infelizes)
```

**Texto na tela:**
```
[5. Cobertura de Código]
```

**Notas de direcao:**
- Secao 6 de 8. Usar exemplos praticos.

---

### Cena 7 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 6. GitHub Actions com Testes. name: CI on: [push, pull_request] jobs: test:

**Visuais:**
- Slides com topicos-chave. ```text
Unitários:        70%+ cobertura (services, utils)
Integração:       20% (endpoints, fluxos críticos)
E2E:              10% (fluxos principais, felizes e infelizes)
```

**Texto na tela:**
```
[6. GitHub Actions com Testes]
```

**Notas de direcao:**
- Secao 7 de 8. Usar exemplos praticos.

---

### Cena 8 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 7. TDD — Test-Driven Development. Red:   Escreva um teste que falha Green: Faça o teste passar (código mínimo) Refactor: Melhore o código mantendo os verdes // 1. RED — Escrever teste primeiro

**Visuais:**
- Slides com topicos-chave. ```text
Unitários:        70%+ cobertura (services, utils)
Integração:       20% (endpoints, fluxos críticos)
E2E:              10% (fluxos principais, felizes e infelizes)
```

**Texto na tela:**
```
[7. TDD — Test-Driven Development]
```

**Notas de direcao:**
- Secao 8 de 8. Usar exemplos praticos.

---

### Cena 9 — CODE-DEMO

**Duracao:** 4:00

**Narracao:**
> Vamos ver na pratica como isso funciona. Observe este codigo em text:

**Visuais:**
- Tela dividida: editor de codigo a esquerda, terminal/output a direita.

**Texto na tela:**
```
```text
Sem testes:
  ┌────────────────────────────────────────────┐
  │  Bug em produção: 2 dias pra achar         │
  │  Correção: 1 hora                          │
  │  Regressão: 3 bugs novos (quebra outras    │
  │             funcionalidades)               │
  │  Confiança do time: baixa ("medo de mexer")│
  └────────────────────────────────────────────┘

Com testes:
  ┌────────────────────────────────────────────┐
  │  Bug em produção: 0 (teste pegou antes)    │
```
```

**Notas de direcao:**
- Explicar linha por linha. Destacar pontos importantes com zoom ou realce.

---

### Cena 10 — SUMMARY

**Duracao:** 1:30

**Narracao:**
> Recapitulando: vimos 1. Por que testar?, 2. Testes Unitários com Jest, 3. Testes de Integração com Supertest, 4. Testes E2E com Playwright, 5. Cobertura de Código, 6. GitHub Actions com Testes. Esses conceitos sao fundamentais para sua formacao.

**Visuais:**
- Lista resumida com icones. Transicao suave para encerramento.

**Texto na tela:**
```
✓ 1. Por que testar?
✓ 2. Testes Unitários com Jest
✓ 3. Testes de Integração com Supertest
✓ 4. Testes E2E com Playwright
✓ 5. Cobertura de Código
✓ 6. GitHub Actions com Testes
```

**Notas de direcao:**
- Reforcar os aprendizados principais. Conectar com o proximo modulo.

---

### Cena 11 — OUTRO

**Duracao:** 0:30

**Narracao:**
> Na proxima aula, vamos aprofundar esses conceitos. Nao perca!

**Visuais:**
- Tela final com links, inscricao, e teaser da proxima aula.

**Texto na tela:**
```
Proximo modulo: [TITULO DO PROXIMO MODULO]
```

**Notas de direcao:**
- Chamada para acao: inscrever-se, comentar, compartilhar.

---

## Checklist de Producao

- [ ] Roteiro revisado
- [ ] Slides preparados
- [ ] Ambiente de codigo configurado
- [ ] Microfone testado
- [ ] Gravacao de tela configurada (1920x1080)
- [ ] Exemplos de codigo testados
- [ ] Legendas geradas
- [ ] Thumbnail criada
- [ ] Descricao e tags preenchidas
- [ ] Capitulos do video marcados

---

## Sugestoes de Thumbnail

- Texto: 'Módulo 15 '
- Cor de fundo: azul escuro (#1a2332)
- Destaque: codigo ou diagrama ao fundo
- Rosto do apresentador no canto inferior direito

---

## SEO

**Titulo:** Módulo 15 — QA: Testes e Qualidade | Arquitetura Enterprise
**Descricao:** Aprenda módulo 15 — qa: testes e qualidade. Nesta aula abordamos conceitos fundamentais com exemplos praticos em TypeScript.
**Tags:** arquitetura, software, enterprise, typescript, desenvolvimento
