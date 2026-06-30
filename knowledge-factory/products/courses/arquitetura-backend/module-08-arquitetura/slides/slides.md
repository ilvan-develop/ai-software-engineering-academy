---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 08 — Arquitetura: Clean Architecture, DDD e SOLID

## Módulo 08 - Arquitetura: Clean Architecture, DDD e SOLID

---
## 1. Por que arquitetura importa

- Arquitetura é a **estrutura fundamental** de um sistema. São as decisões que, se tomadas errado, custam caro para mudar.
- Arquitetura Ruim:
- ┌──────────────────────────────────────────┐
- │  Feature nova: 2 semanas                 │
- │  Por quê? "O código é um macarrão"       │

---
## 2. SOLID — Os 5 princípios

- SOLID não é uma arquitetura — é um **conjunto de princípios** que boas arquiteturas seguem.
- > Uma classe deve ter um, e apenas um, motivo para mudar.
- // ❌ Ruim: Service faz tudo
- class UserService {
- createUser(data: CreateUserDto) { /* ... */ }

---
## 3. Clean Architecture — A Regra da Dependência

- Clean Architecture é uma arquitetura que organiza o código em **círculos concêntricos**.
- ┌─────────────────────┐
- │   ENTITIES          │
- │  (Regras de         │
- │   negócio           │

---
## 4. DDD — Domain-Driven Design

- DDD é uma abordagem que coloca o **domínio do negócio** no centro do desenvolvimento.
- > A mesma linguagem usada pelo negócio deve ser usada no código.
- Negócio: "Um cliente pode abrir um chamado"
- Código:  client.openTicket(ticket)  ✅
- Negócio: "Um cliente pode abrir um ticket de suporte"

---
## 5. Arquitetura Hexagonal (Ports & Adapters)

- A arquitetura hexagonal é uma variação da Clean Architecture que usa o conceito de **portas** e **adaptadores**.
- ┌───────────────────────┐
- │     DOMAIN            │
- │  (core do negócio)    │
- │                       │
- │  ┌─────────────────┐  │

---
## 6. Modular Monolith vs Microservices

- Um monólito **modularizado** — código em módulos bem definidos, mas deploy único.
- Prós:                     Contras:
- Simplicidade            - Escala tudo junto
- Deploy único            - Ponto único de falha
- Sem latência de rede    - Stack única

---
## 7. Event-Driven Architecture

- Event-Driven Architecture usa **eventos** para comunicação entre componentes.
- Evento:           "Algo aconteceu"
- → PedidoCriado, UsuarioCadastrado, PagamentoConfirmado
- Produtor:         Quem gera o evento
- → Serviço de pedidos publica "PedidoCriado"

---
## 8. Aplicando na prática com NestJS + Prisma

- src/
- ├── domain/                    # Círculo mais interno
- │   ├── entities/              # Entidades de domínio
- │   │   └── usuario.ts
- │   ├── value-objects/         # Value Objects

---
## Exemplo: text

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
  │  "Mudei uma coisa sem quebrar nada"      │
  │  "Testes garantem que funciona"          │
  └──────────────────────────────────────────┘
```

---
## Exemplo: text

```text
Componentes:      Em quais partes o sistema se divide?
Comunicação:      Como as partes se comunicam?
Dados:            Como os dados fluem e são armazenados?
Tecnologia:       Qual stack suporta a estrutura?
Equipe:           Como o time se organiza para desenvolver?
```

---
## Recap

- 1. Por que arquitetura importa
- 2. SOLID — Os 5 princípios
- 3. Clean Architecture — A Regra da Dependência
- 4. DDD — Domain-Driven Design
- 5. Arquitetura Hexagonal (Ports & Adapters)
- 6. Modular Monolith vs Microservices
- 7. Event-Driven Architecture
- 8. Aplicando na prática com NestJS + Prisma

---
# Obrigado!

## Perguntas?
