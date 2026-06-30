# Roteiro de Videoaula — Módulo 21 — Projeto Final: Enterprise SaaS de Gestão de Projetos e Tarefas

**Duracao total estimada:** 34 minutos
**Formato:** Videoaula gravada / Streaming
**Publico-alvo:** Desenvolvedores intermediarios

---

## Visao Geral do Video

| Item | Detalhe |
|------|---------|
| Titulo | Módulo 21 — Projeto Final: Enterprise SaaS de Gestão de Projetos e Tarefas |
| Duracao | 34 min |
| Cenas | 13 |
| Formato | Expositivo com demonstracao pratica |
| Nivel | Intermediario |

---

## Roteiro por Cena

### Cena 1 — INTRO

**Duracao:** 1:30

**Narracao:**
> Ola! Nesta aula vamos explorar: Módulo 21 — Projeto Final: Enterprise SaaS de Gestão de Projetos e Tarefas. Ao final, voce vai entender os conceitos fundamentais e como aplica-los na pratica. Vamos la?

**Visuais:**
- Tela de abertura com titulo do modulo. Animacao suave com o nome do curso.

**Texto na tela:**
```
[TITULO] Módulo 21 — Projeto Final: Enterprise SaaS de Gestão de Projetos e Tarefas
```

**Notas de direcao:**
- Tom energico e convidativo. Apresentar o problema que sera resolvido.

---

### Cena 2 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 1. Visão Geral do Projeto. O Projeto Final é a culminação de toda a jornada de 20 módulos. O aluno deve construir, de forma individual ou em squad de até 3 pessoas, uma plataforma **SaaS de Gestão de Projetos e Tarefas** completa — similar a um Trello/Asana/ClickUp simplificado, porém com arquitetura Enterprise real. O objetivo não é apenas "fazer funcionar". É demonstrar domínio sobre: Arquitetura limpa e modular (Módulo 08) Design System e UI/UX profissional (Módulos 04–07)

**Visuais:**
- Slides com topicos-chave. ```text
Empresas usam:     NestJS + Next.js + PostgreSQL + Redis + Docker + AWS
Não usam:          PHP puro, jQuery, MySQL sem ORM, servidor único

A stack escolhida prepara o aluno para:
  → 85% das vagas de SaaS Enterprise no Brasil
  → Escalabilidade real (horizontal, stateless)
  → Ecossistema com alta empregabilidade
```

**Texto na tela:**
```
[1. Visão Geral do Projeto]
```

**Notas de direcao:**
- Secao 2 de 10. Usar exemplos praticos.

---

### Cena 3 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 2. Escopo Completo. Cadastro de empresas (tenants) com plano gratuito e trial de 14 dias Cadastro de usuários com convite por e-mail (fluxo de onboarding) Login com e-mail/senha + OAuth2 (Google/GitHub) JWT com refresh token e rotação de tokens

**Visuais:**
- Slides com topicos-chave. ```text
Empresas usam:     NestJS + Next.js + PostgreSQL + Redis + Docker + AWS
Não usam:          PHP puro, jQuery, MySQL sem ORM, servidor único

A stack escolhida prepara o aluno para:
  → 85% das vagas de SaaS Enterprise no Brasil
  → Escalabilidade real (horizontal, stateless)
  → Ecossistema com alta empregabilidade
```

**Texto na tela:**
```
[2. Escopo Completo]
```

**Notas de direcao:**
- Secao 3 de 10. Usar exemplos praticos.

---

### Cena 4 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 3. Requisitos Funcionais. | ID | Requisito | Prioridade | |----|-----------|------------| | RF01.1 | Usuário deve se registrar com e-mail + senha | Alta | | RF01.2 | Usuário pode registrar uma empresa (tenant) no ato do cadastro | Alta |

**Visuais:**
- Slides com topicos-chave. ```text
Empresas usam:     NestJS + Next.js + PostgreSQL + Redis + Docker + AWS
Não usam:          PHP puro, jQuery, MySQL sem ORM, servidor único

A stack escolhida prepara o aluno para:
  → 85% das vagas de SaaS Enterprise no Brasil
  → Escalabilidade real (horizontal, stateless)
  → Ecossistema com alta empregabilidade
```

**Texto na tela:**
```
[3. Requisitos Funcionais]
```

**Notas de direcao:**
- Secao 4 de 10. Usar exemplos praticos.

---

### Cena 5 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 4. Requisitos Não-Funcionais. | Requisito | Meta | Medição | |-----------|------|---------| | Latência p95 de API | < 200ms | Grafana + Prometheus | | Tempo de carregamento de página | < 2s (FCP), < 3s (LCP) | Lighthouse CI |

**Visuais:**
- Slides com topicos-chave. ```text
Empresas usam:     NestJS + Next.js + PostgreSQL + Redis + Docker + AWS
Não usam:          PHP puro, jQuery, MySQL sem ORM, servidor único

A stack escolhida prepara o aluno para:
  → 85% das vagas de SaaS Enterprise no Brasil
  → Escalabilidade real (horizontal, stateless)
  → Ecossistema com alta empregabilidade
```

**Texto na tela:**
```
[4. Requisitos Não-Funcionais]
```

**Notas de direcao:**
- Secao 5 de 10. Usar exemplos praticos.

---

### Cena 6 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 5. Stack Tecnológica. | Camada | Tecnologia | Justificativa | |--------|-----------|---------------| | Backend | NestJS + TypeScript | Framework Enterprise com DI, módulos, guards, interceptors | | API | REST + GraphQL (opcional) | REST padrão; GraphQL para dashboards complexos |

**Visuais:**
- Slides com topicos-chave. ```text
Empresas usam:     NestJS + Next.js + PostgreSQL + Redis + Docker + AWS
Não usam:          PHP puro, jQuery, MySQL sem ORM, servidor único

A stack escolhida prepara o aluno para:
  → 85% das vagas de SaaS Enterprise no Brasil
  → Escalabilidade real (horizontal, stateless)
  → Ecossistema com alta empregabilidade
```

**Texto na tela:**
```
[5. Stack Tecnológica]
```

**Notas de direcao:**
- Secao 6 de 10. Usar exemplos praticos.

---

### Cena 7 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 6. Arquitetura. ┌─────────────────────────────────────────────────────────────────────┐ │                        CLIENT (Browser)                             │ │  ┌───────────────────────────────────────────────────────────────┐  │ │  │               Next.js App (Vercel / ECS)                      │  │

**Visuais:**
- Slides com topicos-chave. ```text
Empresas usam:     NestJS + Next.js + PostgreSQL + Redis + Docker + AWS
Não usam:          PHP puro, jQuery, MySQL sem ORM, servidor único

A stack escolhida prepara o aluno para:
  → 85% das vagas de SaaS Enterprise no Brasil
  → Escalabilidade real (horizontal, stateless)
  → Ecossistema com alta empregabilidade
```

**Texto na tela:**
```
[6. Arquitetura]
```

**Notas de direcao:**
- Secao 7 de 10. Usar exemplos praticos.

---

### Cena 8 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 7. Módulos do Sistema. Responsabilidade:** Gerenciar usuários, empresas (tenants), convites, perfis. src/modules/users/ ├── user.module.ts ├── user.controller.ts

**Visuais:**
- Slides com topicos-chave. ```text
Empresas usam:     NestJS + Next.js + PostgreSQL + Redis + Docker + AWS
Não usam:          PHP puro, jQuery, MySQL sem ORM, servidor único

A stack escolhida prepara o aluno para:
  → 85% das vagas de SaaS Enterprise no Brasil
  → Escalabilidade real (horizontal, stateless)
  → Ecossistema com alta empregabilidade
```

**Texto na tela:**
```
[7. Módulos do Sistema]
```

**Notas de direcao:**
- Secao 8 de 10. Usar exemplos praticos.

---

### Cena 9 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 8. Critérios de Avaliação. | Critério | Peso | Descrição | |----------|------|-----------| | Estrutura de pastas | 5 | Segue padrão modular, separação clara de responsabilidades | | Código limpo | 5 | Nomes significativos, funções pequenas, sem duplicação |

**Visuais:**
- Slides com topicos-chave. ```text
Empresas usam:     NestJS + Next.js + PostgreSQL + Redis + Docker + AWS
Não usam:          PHP puro, jQuery, MySQL sem ORM, servidor único

A stack escolhida prepara o aluno para:
  → 85% das vagas de SaaS Enterprise no Brasil
  → Escalabilidade real (horizontal, stateless)
  → Ecossistema com alta empregabilidade
```

**Texto na tela:**
```
[8. Critérios de Avaliação]
```

**Notas de direcao:**
- Secao 9 de 10. Usar exemplos praticos.

---

### Cena 10 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 9. Entregáveis. Um repositório GitHub (monorepo com `apps/backend`, `apps/frontend`, `packages/shared`) Ou dois repositórios separados (backend + frontend) Branch principal: `main` com proteção (PR obrigatório, CI obrigatório) Commits seguindo Conventional Commits

**Visuais:**
- Slides com topicos-chave. ```text
Empresas usam:     NestJS + Next.js + PostgreSQL + Redis + Docker + AWS
Não usam:          PHP puro, jQuery, MySQL sem ORM, servidor único

A stack escolhida prepara o aluno para:
  → 85% das vagas de SaaS Enterprise no Brasil
  → Escalabilidade real (horizontal, stateless)
  → Ecossistema com alta empregabilidade
```

**Texto na tela:**
```
[9. Entregáveis]
```

**Notas de direcao:**
- Secao 10 de 10. Usar exemplos praticos.

---

### Cena 11 — CODE-DEMO

**Duracao:** 4:00

**Narracao:**
> Vamos ver na pratica como isso funciona. Observe este codigo em text:

**Visuais:**
- Tela dividida: editor de codigo a esquerda, terminal/output a direita.

**Texto na tela:**
```
```text
Empresas usam:     NestJS + Next.js + PostgreSQL + Redis + Docker + AWS
Não usam:          PHP puro, jQuery, MySQL sem ORM, servidor único

A stack escolhida prepara o aluno para:
  → 85% das vagas de SaaS Enterprise no Brasil
  → Escalabilidade real (horizontal, stateless)
  → Ecossistema com alta empregabilidade
```
```

**Notas de direcao:**
- Explicar linha por linha. Destacar pontos importantes com zoom ou realce.

---

### Cena 12 — SUMMARY

**Duracao:** 1:30

**Narracao:**
> Recapitulando: vimos 1. Visão Geral do Projeto, 2. Escopo Completo, 3. Requisitos Funcionais, 4. Requisitos Não-Funcionais, 5. Stack Tecnológica, 6. Arquitetura. Esses conceitos sao fundamentais para sua formacao.

**Visuais:**
- Lista resumida com icones. Transicao suave para encerramento.

**Texto na tela:**
```
✓ 1. Visão Geral do Projeto
✓ 2. Escopo Completo
✓ 3. Requisitos Funcionais
✓ 4. Requisitos Não-Funcionais
✓ 5. Stack Tecnológica
✓ 6. Arquitetura
```

**Notas de direcao:**
- Reforcar os aprendizados principais. Conectar com o proximo modulo.

---

### Cena 13 — OUTRO

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

- Texto: 'Módulo 21 '
- Cor de fundo: azul escuro (#1a2332)
- Destaque: codigo ou diagrama ao fundo
- Rosto do apresentador no canto inferior direito

---

## SEO

**Titulo:** Módulo 21 — Projeto Final: Enterprise SaaS de Gestão de Projetos e Tarefas | Arquitetura Enterprise
**Descricao:** Aprenda módulo 21 — projeto final: enterprise saas de gestão de projetos e tarefas. Nesta aula abordamos conceitos fundamentais com exemplos praticos em TypeScript.
**Tags:** arquitetura, software, enterprise, typescript, desenvolvimento
