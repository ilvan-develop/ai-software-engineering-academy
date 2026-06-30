# Roteiro de Videoaula — Módulo 08 — Arquitetura: Clean Architecture, DDD e SOLID

**Duracao total estimada:** 31 minutos
**Formato:** Videoaula gravada / Streaming
**Publico-alvo:** Desenvolvedores intermediarios

---

## Visao Geral do Video

| Item | Detalhe |
|------|---------|
| Titulo | Módulo 08 — Arquitetura: Clean Architecture, DDD e SOLID |
| Duracao | 31 min |
| Cenas | 12 |
| Formato | Expositivo com demonstracao pratica |
| Nivel | Intermediario |

---

## Roteiro por Cena

### Cena 1 — INTRO

**Duracao:** 1:30

**Narracao:**
> Ola! Nesta aula vamos explorar: Módulo 08 — Arquitetura: Clean Architecture, DDD e SOLID. Ao final, voce vai entender os conceitos fundamentais e como aplica-los na pratica. Vamos la?

**Visuais:**
- Tela de abertura com titulo do modulo. Animacao suave com o nome do curso.

**Texto na tela:**
```
[TITULO] Módulo 08 — Arquitetura: Clean Architecture, DDD e SOLID
```

**Notas de direcao:**
- Tom energico e convidativo. Apresentar o problema que sera resolvido.

---

### Cena 2 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 1. Por que arquitetura importa. Arquitetura é a **estrutura fundamental** de um sistema. São as decisões que, se tomadas errado, custam caro para mudar. Arquitetura Ruim: ┌──────────────────────────────────────────┐ │  Feature nova: 2 semanas                 │

**Visuais:**
- Slides com topicos-chave. ```text
Componentes:      Em quais partes o sistema se divide?
Comunicação:      Como as partes se comunicam?
Dados:            Como os dados fluem e são armazenados?
Tecnologia:       Qual stack suporta a estrutura?
Equipe:           Como o time se organiza para desenvolver?
```

**Texto na tela:**
```
[1. Por que arquitetura importa]
```

**Notas de direcao:**
- Secao 2 de 9. Usar exemplos praticos.

---

### Cena 3 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 2. SOLID — Os 5 princípios. SOLID não é uma arquitetura — é um **conjunto de princípios** que boas arquiteturas seguem. > Uma classe deve ter um, e apenas um, motivo para mudar. // ❌ Ruim: Service faz tudo class UserService {

**Visuais:**
- Slides com topicos-chave. ```text
Componentes:      Em quais partes o sistema se divide?
Comunicação:      Como as partes se comunicam?
Dados:            Como os dados fluem e são armazenados?
Tecnologia:       Qual stack suporta a estrutura?
Equipe:           Como o time se organiza para desenvolver?
```

**Texto na tela:**
```
[2. SOLID — Os 5 princípios]
```

**Notas de direcao:**
- Secao 3 de 9. Usar exemplos praticos.

---

### Cena 4 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 3. Clean Architecture — A Regra da Dependência. Clean Architecture é uma arquitetura que organiza o código em **círculos concêntricos**. ┌─────────────────────┐ │   ENTITIES          │ │  (Regras de         │

**Visuais:**
- Slides com topicos-chave. ```text
Componentes:      Em quais partes o sistema se divide?
Comunicação:      Como as partes se comunicam?
Dados:            Como os dados fluem e são armazenados?
Tecnologia:       Qual stack suporta a estrutura?
Equipe:           Como o time se organiza para desenvolver?
```

**Texto na tela:**
```
[3. Clean Architecture — A Regra da Dependência]
```

**Notas de direcao:**
- Secao 4 de 9. Usar exemplos praticos.

---

### Cena 5 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 4. DDD — Domain-Driven Design. DDD é uma abordagem que coloca o **domínio do negócio** no centro do desenvolvimento. > A mesma linguagem usada pelo negócio deve ser usada no código. Negócio: "Um cliente pode abrir um chamado" Código:  client.openTicket(ticket)  ✅

**Visuais:**
- Slides com topicos-chave. ```text
Componentes:      Em quais partes o sistema se divide?
Comunicação:      Como as partes se comunicam?
Dados:            Como os dados fluem e são armazenados?
Tecnologia:       Qual stack suporta a estrutura?
Equipe:           Como o time se organiza para desenvolver?
```

**Texto na tela:**
```
[4. DDD — Domain-Driven Design]
```

**Notas de direcao:**
- Secao 5 de 9. Usar exemplos praticos.

---

### Cena 6 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 5. Arquitetura Hexagonal (Ports & Adapters). A arquitetura hexagonal é uma variação da Clean Architecture que usa o conceito de **portas** e **adaptadores**. ┌───────────────────────┐ │     DOMAIN            │ │  (core do negócio)    │

**Visuais:**
- Slides com topicos-chave. ```text
Componentes:      Em quais partes o sistema se divide?
Comunicação:      Como as partes se comunicam?
Dados:            Como os dados fluem e são armazenados?
Tecnologia:       Qual stack suporta a estrutura?
Equipe:           Como o time se organiza para desenvolver?
```

**Texto na tela:**
```
[5. Arquitetura Hexagonal (Ports & Adapters)]
```

**Notas de direcao:**
- Secao 6 de 9. Usar exemplos praticos.

---

### Cena 7 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 6. Modular Monolith vs Microservices. Um monólito **modularizado** — código em módulos bem definidos, mas deploy único. Prós:                     Contras: Simplicidade            - Escala tudo junto Deploy único            - Ponto único de falha

**Visuais:**
- Slides com topicos-chave. ```text
Componentes:      Em quais partes o sistema se divide?
Comunicação:      Como as partes se comunicam?
Dados:            Como os dados fluem e são armazenados?
Tecnologia:       Qual stack suporta a estrutura?
Equipe:           Como o time se organiza para desenvolver?
```

**Texto na tela:**
```
[6. Modular Monolith vs Microservices]
```

**Notas de direcao:**
- Secao 7 de 9. Usar exemplos praticos.

---

### Cena 8 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 7. Event-Driven Architecture. Event-Driven Architecture usa **eventos** para comunicação entre componentes. Evento:           "Algo aconteceu" → PedidoCriado, UsuarioCadastrado, PagamentoConfirmado Produtor:         Quem gera o evento

**Visuais:**
- Slides com topicos-chave. ```text
Componentes:      Em quais partes o sistema se divide?
Comunicação:      Como as partes se comunicam?
Dados:            Como os dados fluem e são armazenados?
Tecnologia:       Qual stack suporta a estrutura?
Equipe:           Como o time se organiza para desenvolver?
```

**Texto na tela:**
```
[7. Event-Driven Architecture]
```

**Notas de direcao:**
- Secao 8 de 9. Usar exemplos praticos.

---

### Cena 9 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 8. Aplicando na prática com NestJS + Prisma. src/ ├── domain/                    # Círculo mais interno │   ├── entities/              # Entidades de domínio │   │   └── usuario.ts

**Visuais:**
- Slides com topicos-chave. ```text
Componentes:      Em quais partes o sistema se divide?
Comunicação:      Como as partes se comunicam?
Dados:            Como os dados fluem e são armazenados?
Tecnologia:       Qual stack suporta a estrutura?
Equipe:           Como o time se organiza para desenvolver?
```

**Texto na tela:**
```
[8. Aplicando na prática com NestJS + Prisma]
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
Arquitetura Ruim:
  ┌──────────────────────────────────────────┐
  │  Feature nova: 2 semanas                 │
  │  Por quê? "O código é um macarrão"       │
  │  "Toda mudança quebra algo"              │
  │  "Melhor reescrever do zero"             │
  └──────────────────────────────────────────┘

Arquitetura Boa:
  ┌──────────────────────────────────────────┐
  │  Feature nova: 2 dias                    │
  │  Por quê? "Só adicionar um módulo"       │
```
```

**Notas de direcao:**
- Explicar linha por linha. Destacar pontos importantes com zoom ou realce.

---

### Cena 11 — SUMMARY

**Duracao:** 1:30

**Narracao:**
> Recapitulando: vimos 1. Por que arquitetura importa, 2. SOLID — Os 5 princípios, 3. Clean Architecture — A Regra da Dependência, 4. DDD — Domain-Driven Design, 5. Arquitetura Hexagonal (Ports & Adapters), 6. Modular Monolith vs Microservices. Esses conceitos sao fundamentais para sua formacao.

**Visuais:**
- Lista resumida com icones. Transicao suave para encerramento.

**Texto na tela:**
```
✓ 1. Por que arquitetura importa
✓ 2. SOLID — Os 5 princípios
✓ 3. Clean Architecture — A Regra da Dependência
✓ 4. DDD — Domain-Driven Design
✓ 5. Arquitetura Hexagonal (Ports & Adapters)
✓ 6. Modular Monolith vs Microservices
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

- Texto: 'Módulo 08 '
- Cor de fundo: azul escuro (#1a2332)
- Destaque: codigo ou diagrama ao fundo
- Rosto do apresentador no canto inferior direito

---

## SEO

**Titulo:** Módulo 08 — Arquitetura: Clean Architecture, DDD e SOLID | Arquitetura Enterprise
**Descricao:** Aprenda módulo 08 — arquitetura: clean architecture, ddd e solid. Nesta aula abordamos conceitos fundamentais com exemplos praticos em TypeScript.
**Tags:** arquitetura, software, enterprise, typescript, desenvolvimento
