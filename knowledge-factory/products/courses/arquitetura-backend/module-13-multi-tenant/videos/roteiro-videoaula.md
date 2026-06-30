# Roteiro de Videoaula — Módulo 13 — Multi-Tenant: Conceitos e Estratégias de Isolamento

**Duracao total estimada:** 16 minutos
**Formato:** Videoaula gravada / Streaming
**Publico-alvo:** Desenvolvedores intermediarios

---

## Visao Geral do Video

| Item | Detalhe |
|------|---------|
| Titulo | Módulo 13 — Multi-Tenant: Conceitos e Estratégias de Isolamento |
| Duracao | 16 min |
| Cenas | 7 |
| Formato | Expositivo com demonstracao pratica |
| Nivel | Intermediario |

---

## Roteiro por Cena

### Cena 1 — INTRO

**Duracao:** 1:30

**Narracao:**
> Ola! Nesta aula vamos explorar: Módulo 13 — Multi-Tenant: Conceitos e Estratégias de Isolamento. Ao final, voce vai entender os conceitos fundamentais e como aplica-los na pratica. Vamos la?

**Visuais:**
- Tela de abertura com titulo do modulo. Animacao suave com o nome do curso.

**Texto na tela:**
```
[TITULO] Módulo 13 — Multi-Tenant: Conceitos e Estratégias de Isolamento
```

**Notas de direcao:**
- Tom energico e convidativo. Apresentar o problema que sera resolvido.

---

### Cena 2 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 1. O que é Multi-Tenancy?. Multi-tenancy é um padrão arquitetural onde **uma única instância de software atende múltiplos clientes (tenants)**, mantendo os dados de cada um logicamente isolados e invisíveis entre si. ┌──────────────────────────────────────────────────────┐ │                    SISTEMA (1 instância)               │ │                                                        │

**Visuais:**
- Slides com topicos-chave. ```text
┌──────────────────────────────────────────────┐
│                Connection Router               │
│                                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ DB Acme  │  │ DB Zeta  │  │ DB Omega │    │
│  │ tenant_1 │  │ tenant_2 │  │ tenant_3 │    │
│  └──────────┘  └──────────┘  └──────────┘    │
└──────────────────────────────────────────────┘
```

**Texto na tela:**
```
[1. O que é Multi-Tenancy?]
```

**Notas de direcao:**
- Secao 2 de 4. Usar exemplos praticos.

---

### Cena 3 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 2. Abordagens de Isolamento. Existem três estratégias principais para isolar dados entre tenants. Cada tenant tem **seu próprio banco de dados**. O roteador de conexão decide qual banco usar com base no tenant identificado. ┌──────────────────────────────────────────────┐ │                Connection Router               │

**Visuais:**
- Slides com topicos-chave. ```text
┌──────────────────────────────────────────────┐
│                Connection Router               │
│                                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ DB Acme  │  │ DB Zeta  │  │ DB Omega │    │
│  │ tenant_1 │  │ tenant_2 │  │ tenant_3 │    │
│  └──────────┘  └──────────┘  └──────────┘    │
└──────────────────────────────────────────────┘
```

**Texto na tela:**
```
[2. Abordagens de Isolamento]
```

**Notas de direcao:**
- Secao 3 de 4. Usar exemplos praticos.

---

### Cena 4 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 3. Análise Aprofundada por Dimensão. Database per Tenant:** Um vazamento de dados de um tenant não afeta os outros. Se um cliente exige compliance específico (LGPD, HIPAA, SOC2), pode-se isolar completamente em nível físico. Ataques de SQL injection ficam contidos no banco do tenant. Schema per Tenant:** Um invasor que ganha acesso ao banco pode potencialmente acessar múltiplos schemas. A segurança depende das permissões do usuário do banco (`GRANT USAGE ON SCHEMA`). Idealmente, o usuário da aplicação tem acesso apenas ao schema do tenant atual. Shared Database:** Um SQL injection ou bug no `WHERE` expõe **todos os dados de todos os tenants**. Requer: Testes de isolamento obrigatórios (ver seção 13)

**Visuais:**
- Slides com topicos-chave. ```text
┌──────────────────────────────────────────────┐
│                Connection Router               │
│                                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ DB Acme  │  │ DB Zeta  │  │ DB Omega │    │
│  │ tenant_1 │  │ tenant_2 │  │ tenant_3 │    │
│  └──────────┘  └──────────┘  └──────────┘    │
└──────────────────────────────────────────────┘
```

**Texto na tela:**
```
[3. Análise Aprofundada por Dimensão]
```

**Notas de direcao:**
- Secao 4 de 4. Usar exemplos praticos.

---

### Cena 5 — CODE-DEMO

**Duracao:** 4:00

**Narracao:**
> Vamos ver na pratica como isso funciona. Observe este codigo em text:

**Visuais:**
- Tela dividida: editor de codigo a esquerda, terminal/output a direita.

**Texto na tela:**
```
```text
┌──────────────────────────────────────────────────────┐
│                    SISTEMA (1 instância)               │
│                                                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │ Tenant A │  │ Tenant B │  │ Tenant C │            │
│  │ (Acme)   │  │ (Zeta)   │  │ (Omega)  │            │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘            │
│       │              │              │                   │
│       └──────────────┴──────────────┘                   │
│                      │                                  │
│              ┌───────┴───────┐                          │
│              │  API + DB     │                          │
```
```

**Notas de direcao:**
- Explicar linha por linha. Destacar pontos importantes com zoom ou realce.

---

### Cena 6 — SUMMARY

**Duracao:** 1:30

**Narracao:**
> Recapitulando: vimos 1. O que é Multi-Tenancy?, 2. Abordagens de Isolamento, 3. Análise Aprofundada por Dimensão. Esses conceitos sao fundamentais para sua formacao.

**Visuais:**
- Lista resumida com icones. Transicao suave para encerramento.

**Texto na tela:**
```
✓ 1. O que é Multi-Tenancy?
✓ 2. Abordagens de Isolamento
✓ 3. Análise Aprofundada por Dimensão
```

**Notas de direcao:**
- Reforcar os aprendizados principais. Conectar com o proximo modulo.

---

### Cena 7 — OUTRO

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

- Texto: 'Módulo 13 '
- Cor de fundo: azul escuro (#1a2332)
- Destaque: codigo ou diagrama ao fundo
- Rosto do apresentador no canto inferior direito

---

## SEO

**Titulo:** Módulo 13 — Multi-Tenant: Conceitos e Estratégias de Isolamento | Arquitetura Enterprise
**Descricao:** Aprenda módulo 13 — multi-tenant: conceitos e estratégias de isolamento. Nesta aula abordamos conceitos fundamentais com exemplos praticos em TypeScript.
**Tags:** arquitetura, software, enterprise, typescript, desenvolvimento
