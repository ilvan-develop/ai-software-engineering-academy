# Roteiro de Videoaula — Módulo 09 — Modelagem de Dados: Prisma e PostgreSQL

**Duracao total estimada:** 31 minutos
**Formato:** Videoaula gravada / Streaming
**Publico-alvo:** Desenvolvedores intermediarios

---

## Visao Geral do Video

| Item | Detalhe |
|------|---------|
| Titulo | Módulo 09 — Modelagem de Dados: Prisma e PostgreSQL |
| Duracao | 31 min |
| Cenas | 12 |
| Formato | Expositivo com demonstracao pratica |
| Nivel | Intermediario |

---

## Roteiro por Cena

### Cena 1 — INTRO

**Duracao:** 1:30

**Narracao:**
> Ola! Nesta aula vamos explorar: Módulo 09 — Modelagem de Dados: Prisma e PostgreSQL. Ao final, voce vai entender os conceitos fundamentais e como aplica-los na pratica. Vamos la?

**Visuais:**
- Tela de abertura com titulo do modulo. Animacao suave com o nome do curso.

**Texto na tela:**
```
[TITULO] Módulo 09 — Modelagem de Dados: Prisma e PostgreSQL
```

**Notas de direcao:**
- Tom energico e convidativo. Apresentar o problema que sera resolvido.

---

### Cena 2 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 1. Por que modelagem importa. Modelagem de dados é a **fundação** do sistema. Erros aqui são os mais caros de corrigir. Modelagem ruim: ┌──────────────────────────────────────────┐ │  Tabela sem índices → query lenta        │

**Visuais:**
- Slides com topicos-chave. ```text
1:1  — Um usuário tem um perfil
1:N  — Um usuário tem muitos pedidos
N:M  — Um produto está em muitas categorias
```

**Texto na tela:**
```
[1. Por que modelagem importa]
```

**Notas de direcao:**
- Secao 2 de 9. Usar exemplos praticos.

---

### Cena 3 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 2. Entidades e Relacionamentos. 1:1  — Um usuário tem um perfil 1:N  — Um usuário tem muitos pedidos N:M  — Um produto está em muitas categorias // 1:1

**Visuais:**
- Slides com topicos-chave. ```text
1:1  — Um usuário tem um perfil
1:N  — Um usuário tem muitos pedidos
N:M  — Um produto está em muitas categorias
```

**Texto na tela:**
```
[2. Entidades e Relacionamentos]
```

**Notas de direcao:**
- Secao 3 de 9. Usar exemplos praticos.

---

### Cena 4 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 3. Soft Delete e Audit Trail. Nunca delete dados definitivamente em sistemas Enterprise. model User { id        String    @id @default(cuid()) email     String    @unique

**Visuais:**
- Slides com topicos-chave. ```text
1:1  — Um usuário tem um perfil
1:N  — Um usuário tem muitos pedidos
N:M  — Um produto está em muitas categorias
```

**Texto na tela:**
```
[3. Soft Delete e Audit Trail]
```

**Notas de direcao:**
- Secao 4 de 9. Usar exemplos praticos.

---

### Cena 5 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 4. Índices e Performance. model Order { id         String   @id @default(cuid()) userId     String status     OrderStatus

**Visuais:**
- Slides com topicos-chave. ```text
1:1  — Um usuário tem um perfil
1:N  — Um usuário tem muitos pedidos
N:M  — Um produto está em muitas categorias
```

**Texto na tela:**
```
[4. Índices e Performance]
```

**Notas de direcao:**
- Secao 5 de 9. Usar exemplos praticos.

---

### Cena 6 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 5. Migrações Seguras. npx prisma migrate dev --name create-user-table npx prisma migrate deploy npx prisma migrate reset // ❌ Ruim: renomear coluna diretamente (quebra queries em execução)

**Visuais:**
- Slides com topicos-chave. ```text
1:1  — Um usuário tem um perfil
1:N  — Um usuário tem muitos pedidos
N:M  — Um produto está em muitas categorias
```

**Texto na tela:**
```
[5. Migrações Seguras]
```

**Notas de direcao:**
- Secao 6 de 9. Usar exemplos praticos.

---

### Cena 7 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 6. Estratégias de Backup. Full:     Cópia completa do banco Quando: Diário Tempo:  Lento, ocupa espaço Restore: Completo, mais simples

**Visuais:**
- Slides com topicos-chave. ```text
1:1  — Um usuário tem um perfil
1:N  — Um usuário tem muitos pedidos
N:M  — Um produto está em muitas categorias
```

**Texto na tela:**
```
[6. Estratégias de Backup]
```

**Notas de direcao:**
- Secao 7 de 9. Usar exemplos praticos.

---

### Cena 8 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 7. Schema completo de exemplo. O diagrama abaixo resume as entidades, atributos e cardinalidades do schema: ![Modelo Entidade-Relacionamento Enterprise](/knowledge-factory/products/courses/arquitetura-backend/module-09-modelagem/assets/diagram-er-schema-enterprise.svg) generator client { provider = "prisma-client-js"

**Visuais:**
- Slides com topicos-chave. ```text
1:1  — Um usuário tem um perfil
1:N  — Um usuário tem muitos pedidos
N:M  — Um produto está em muitas categorias
```

**Texto na tela:**
```
[7. Schema completo de exemplo]
```

**Notas de direcao:**
- Secao 8 de 9. Usar exemplos praticos.

---

### Cena 9 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: Resumo. 1. **Modelagem é a fundação** — erros aqui são os mais caros 2. **1:1, 1:N, N:M** — conheça os 3 tipos de relacionamento 3. **Soft Delete** — nunca delete dados (deletedAt) 4. **Audit Trail** — toda ação importante deve ser registrada

**Visuais:**
- Slides com topicos-chave. ```text
1:1  — Um usuário tem um perfil
1:N  — Um usuário tem muitos pedidos
N:M  — Um produto está em muitas categorias
```

**Texto na tela:**
```
[Resumo]
```

**Notas de direcao:**
- Secao 9 de 9. Usar exemplos praticos.

---

### Cena 10 — CODE-DEMO

**Duracao:** 4:00

**Narracao:**
> Vamos ver na pratica como isso funciona. Observe este codigo em text:

**Visuais:**
- Tela dividida: editor de codigo a esquerda, terminal/output a direita.

**Texto na tela:**
```
```text
Modelagem ruim:
  ┌──────────────────────────────────────────┐
  │  Tabela sem índices → query lenta        │
  │  Relação errada → dados inconsistentes   │
  │  Falta de soft delete → perda de dados   │
  │  Sem audit trail → impossível auditar    │
  │  Migração corretiva → horas de trabalho  │
  └──────────────────────────────────────────┘

Modelagem boa:
  ┌──────────────────────────────────────────┐
  │  Índices certos → queries rápidas        │
```
```

**Notas de direcao:**
- Explicar linha por linha. Destacar pontos importantes com zoom ou realce.

---

### Cena 11 — SUMMARY

**Duracao:** 1:30

**Narracao:**
> Recapitulando: vimos 1. Por que modelagem importa, 2. Entidades e Relacionamentos, 3. Soft Delete e Audit Trail, 4. Índices e Performance, 5. Migrações Seguras, 6. Estratégias de Backup. Esses conceitos sao fundamentais para sua formacao.

**Visuais:**
- Lista resumida com icones. Transicao suave para encerramento.

**Texto na tela:**
```
✓ 1. Por que modelagem importa
✓ 2. Entidades e Relacionamentos
✓ 3. Soft Delete e Audit Trail
✓ 4. Índices e Performance
✓ 5. Migrações Seguras
✓ 6. Estratégias de Backup
```

**Notas de direcao:**
- Reforcar os aprendizados principais. Conectar com o proximo modulo.

---

### Cena 12 — OUTRO

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

- Texto: 'Módulo 09 '
- Cor de fundo: azul escuro (#1a2332)
- Destaque: codigo ou diagrama ao fundo
- Rosto do apresentador no canto inferior direito

---

## SEO

**Titulo:** Módulo 09 — Modelagem de Dados: Prisma e PostgreSQL | Arquitetura Enterprise
**Descricao:** Aprenda módulo 09 — modelagem de dados: prisma e postgresql. Nesta aula abordamos conceitos fundamentais com exemplos praticos em TypeScript.
**Tags:** arquitetura, software, enterprise, typescript, desenvolvimento
