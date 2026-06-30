## Introducao

# Módulo 08 — Arquitetura: Clean Architecture, DDD e SOLID
**Pensar antes de programar.**
---

---
## 1. Por que arquitetura importa

Arquitetura é a **estrutura fundamental** de um sistema. São as decisões que, se tomadas errado, custam caro para mudar.
### O custo de uma arquitetura ruim
Arquitetura Ruim:
┌──────────────────────────────────────────┐
│  Feature nova: 2 semanas                 │
│  Por quê? "O código é um macarrão"       │
│  "Toda mudança quebra algo"              │
│  "Melhor reescrever do zero"             │

---
## 2. SOLID — Os 5 princípios

SOLID não é uma arquitetura — é um **conjunto de princípios** que boas arquiteturas seguem.
### S — Single Responsibility Principle
> Uma classe deve ter um, e apenas um, motivo para mudar.
// ❌ Ruim: Service faz tudo
class UserService {
createUser(data: CreateUserDto) { /* ... */ }
sendWelcomeEmail(email: string) { /* ... */ }
generateReport() { /* ... */ }

---
## 3. Clean Architecture — A Regra da Dependência

Clean Architecture é uma arquitetura que organiza o código em **círculos concêntricos**.
### As camadas
┌─────────────────────┐
│   ENTITIES          │
│  (Regras de         │
│   negócio           │
│   enterprise-wide)  │
│                     │

---
## 4. DDD — Domain-Driven Design

DDD é uma abordagem que coloca o **domínio do negócio** no centro do desenvolvimento.
### Linguagem Ubíqua
> A mesma linguagem usada pelo negócio deve ser usada no código.
Negócio: "Um cliente pode abrir um chamado"
Código:  client.openTicket(ticket)  ✅
Negócio: "Um cliente pode abrir um ticket de suporte"
Código:  client.createSupportTicket(ticket)  ❌ (outra linguagem)
### Bounded Contexts

---
## 5. Arquitetura Hexagonal (Ports & Adapters)

A arquitetura hexagonal é uma variação da Clean Architecture que usa o conceito de **portas** e **adaptadores**.
┌───────────────────────┐
│     DOMAIN            │
│  (core do negócio)    │
│                       │
│  ┌─────────────────┐  │
│  │   APPLICATION    │  │
│  │   (use cases)   │  │

---
## 6. Modular Monolith vs Microservices

### Modular Monolith
Um monólito **modularizado** — código em módulos bem definidos, mas deploy único.
Prós:                     Contras:
- Simplicidade            - Escala tudo junto
- Deploy único            - Ponto único de falha
- Sem latência de rede    - Stack única
- Dados consistentes      - Time grande conflita
- Transações ACID

---
## 7. Event-Driven Architecture

Event-Driven Architecture usa **eventos** para comunicação entre componentes.
### Conceitos
Evento:           "Algo aconteceu"
→ PedidoCriado, UsuarioCadastrado, PagamentoConfirmado
Produtor:         Quem gera o evento
→ Serviço de pedidos publica "PedidoCriado"
Consumidor:       Quem reage ao evento
→ Serviço de email escuta "PedidoCriado" e envia confirmação

---
## 8. Aplicando na prática com NestJS + Prisma

### Estrutura de pastas seguindo Clean Architecture + DDD
src/
├── domain/                    # Círculo mais interno
│   ├── entities/              # Entidades de domínio
│   │   └── usuario.ts
│   ├── value-objects/         # Value Objects
│   │   └── email.ts
│   ├── repositories/          # Interfaces (portas)

---
