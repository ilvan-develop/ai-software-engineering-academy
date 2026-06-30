# Módulo 08 — Arquitetura: Clean Architecture, DDD e SOLID

**Pensar antes de programar.**

---

## 1. Por que arquitetura importa

Arquitetura é a **estrutura fundamental** de um sistema. São as decisões que, se tomadas errado, custam caro para mudar.

### O custo de uma arquitetura ruim

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

### O que arquitetura define

```text
Componentes:      Em quais partes o sistema se divide?
Comunicação:      Como as partes se comunicam?
Dados:            Como os dados fluem e são armazenados?
Tecnologia:       Qual stack suporta a estrutura?
Equipe:           Como o time se organiza para desenvolver?
```

---

## 2. SOLID — Os 5 princípios

SOLID não é uma arquitetura — é um **conjunto de princípios** que boas arquiteturas seguem.

### S — Single Responsibility Principle

> Uma classe deve ter um, e apenas um, motivo para mudar.

```typescript
// ❌ Ruim: Service faz tudo
class UserService {
  createUser(data: CreateUserDto) { /* ... */ }
  sendWelcomeEmail(email: string) { /* ... */ }
  generateReport() { /* ... */ }
}

// ✅ Bom: Responsabilidades separadas
class CreateUserUseCase {
  execute(data: CreateUserDto) { /* ... */ }
}

class EmailService {
  sendWelcome(user: User) { /* ... */ }
}

class ReportGenerator {
  generate(): Report { /* ... */ }
}
```text

### O — Open/Closed Principle

> Aberto para extensão, fechado para modificação.

```typescript
// ❌ Ruim: Modificar para adicionar tipo
class PaymentProcessor {
  process(type: string, amount: number) {
    if (type === 'credit') { /* ... */ }
    if (type === 'debit') { /* ... */ }
    if (type === 'pix') { /* ... */ }  // modifiquei!
  }
}

// ✅ Bom: Estender sem modificar
interface PaymentMethod {
  process(amount: number): void;
}

class CreditCardPayment implements PaymentMethod { /* ... */ }
class PixPayment implements PaymentMethod { /* ... */ }
```

### L — Liskov Substitution Principle

> Subtipos devem ser substituíveis por seus tipos base.

```typescript
// ❌ Ruim: Quebra a expectativa
class Bird {
  fly(): void { /* voa */ }
}

class Penguin extends Bird {
  fly(): void { throw new Error('Pinguins não voam'); }  // 💥
}

// ✅ Bom: Abstração correta
interface Bird { }
interface FlyingBird extends Bird {
  fly(): void;
}
class Penguin implements Bird { }
class Sparrow implements Bird, FlyingBird { }
```text

### I — Interface Segregation Principle

> Interfaces específicas são melhores que interfaces genéricas.

```typescript
// ❌ Ruim: Interface genérica
interface Worker {
  work(): void;
  eat(): void;
  sleep(): void;
}

// ✅ Bom: Interfaces específicas
interface Workable { work(): void; }
interface Eatable { eat(): void; }
interface Sleepable { sleep(): void; }
```

### D — Dependency Inversion Principle

> Dependa de abstrações, não de implementações concretas.

```typescript
// ❌ Ruim: Dependência concreta
class OrderService {
  private repository = new PrismaOrderRepository();  // concreto!
}

// ✅ Bom: Dependência abstrata
class OrderService {
  constructor(
    private repository: OrderRepository  // interface
  ) { }
}
```text

---

## 3. Clean Architecture — A Regra da Dependência

Clean Architecture é uma arquitetura que organiza o código em **círculos concêntricos**.

### As camadas

```text
                     ┌─────────────────────┐
                     │   ENTITIES          │
                     │  (Regras de         │
                     │   negócio           │
                     │   enterprise-wide)  │
                     │                     │
              ┌──────┴─────────┬───────────┴──────┐
              │   USE CASES    │                   │
              │  (Regras de    │                   │
              │   negócio      │                   │
              │   da aplicação)│                   │
              │                │                   │
         ┌────┴──────────┬─────┴────────────┬──────┴────┐
         │  CONTROLLERS  │  PRESENTERS      │ GATEWAYS  │
         │  (Adaptadores │  (Adaptadores    │(Adaptadores│
         │   de entrada) │  de saída)       │ de saída) │
         │               │                  │           │
    ┌────┴──────────┬────┴──────────┬───────┴─────┬─────┴────┐
    │   FRAMEWORKS & DRIVERS                        │
    │  (NestJS, Prisma, Next.js, PostgreSQL...)     │
    └──────────────────────────────────────────────┘
```

### A Regra da Dependência

> As dependências de código fonte apontam **para dentro**, em direção ao centro.
> Nada no círculo interno pode saber algo sobre o círculo externo.

```text
❌ ERRADO: Use Case importa Prisma
  UseCase → PrismaClient  (dependência para fora!)

✅ CERTO: Use Case depende de interface
  UseCase → UserRepository (interface)
  PrismaUserRepository → UserRepository (implementa)
```

### O que vai em cada camada

| Camada | O que contém | Pode importar |
|--------|-------------|---------------|
| **Entities** | Regras de negócio Enterprise | Nada externo |
| **Use Cases** | Regras de negócio da aplicação | Entities |
| **Controllers/Presenters** | Adaptação de entrada/saída | Use Cases |
| **Frameworks** | Implementações concretas | Qualquer adaptador |

---

## 4. DDD — Domain-Driven Design

DDD é uma abordagem que coloca o **domínio do negócio** no centro do desenvolvimento.

### Linguagem Ubíqua

> A mesma linguagem usada pelo negócio deve ser usada no código.

```text
Negócio: "Um cliente pode abrir um chamado"
Código:  client.openTicket(ticket)  ✅

Negócio: "Um cliente pode abrir um ticket de suporte"
Código:  client.createSupportTicket(ticket)  ❌ (outra linguagem)
```

### Bounded Contexts

Um Bounded Context é um **limite explícito** onde um modelo de domínio se aplica.

```text
Contexto de Vendas:         Contexto de Logística:
  Cliente = quem compra      Cliente = quem recebe
  Produto = item no catálogo Produto = item no estoque
  Pedido = carrinho          Pedido = carga para entrega

São modelos DIFERENTES do mesmo conceito!
```

### Elementos do DDD

```text
┌──────────────────────────────────────────┐
│  ENTITY                                  │
│  → Tem identidade única (id)             │
│  → Muda ao longo do tempo               │
│  → Ex: Usuario, Pedido, Produto          │
├──────────────────────────────────────────┤
│  VALUE OBJECT                            │
│  → Descrito por seus atributos           │
│  → Imutável                              │
│  → Ex: Endereco, Email, CPF              │
├──────────────────────────────────────────┤
│  AGGREGATE                               │
│  → Grupo de entidades com raiz           │
│  → Consistência transacional             │
│  → Ex: Pedido + Itens (Pedido é raiz)    │
├──────────────────────────────────────────┤
│  REPOSITORY                              │
│  → Abstração de persistência             │
│  → Interface no domínio                  │
│  → Implementação externa                 │
├──────────────────────────────────────────┤
│  DOMAIN SERVICE                          │
│  → Regra de negócio sem estado           │
│  → Opera em múltiplas entidades          │
└──────────────────────────────────────────┘
```

### Exemplo prático de DDD

```typescript
// Entidade
class Usuario {
  private id: UsuarioId;
  private email: Email;  // Value Object
  private perfil: Perfil;

  constructor(id: UsuarioId, email: Email, perfil: Perfil) {
    this.id = id;
    this.email = email;
    this.perfil = perfil;
  }

  alterarPerfil(novoPerfil: Perfil): void {
    // Regra de negócio
    if (this.perfil.eAdmin() && !novoPerfil.eAdmin()
        && !this.temOutroAdmin()) {
      throw new Error('Deve haver pelo menos um admin');
    }
    this.perfil = novoPerfil;
  }
}

// Value Object
class Email {
  private readonly valor: string;

  constructor(valor: string) {
    if (!valor.includes('@')) {
      throw new Error('Email inválido');
    }
    this.valor = valor;
  }

  toString(): string { return this.valor; }
}

// Repository (interface no domínio)
interface UsuarioRepository {
  findById(id: UsuarioId): Promise<Usuario | null>;
  save(usuario: Usuario): Promise<void>;
  delete(id: UsuarioId): Promise<void>;
}

// Use Case
class AlterarPerfilUseCase {
  constructor(
    private usuarioRepo: UsuarioRepository,
    private emailService: EmailService
  ) {}

  async execute(input: { usuarioId: UsuarioId; novoPerfil: Perfil }) {
    const usuario = await this.usuarioRepo.findById(input.usuarioId);
    if (!usuario) throw new NotFoundError('Usuário não encontrado');

    usuario.alterarPerfil(input.novoPerfil);
    await this.usuarioRepo.save(usuario);

    // Efeito colateral via evento
    await this.emailService.enviarNotificacao(usuario.email);
  }
}
```

---

## 5. Arquitetura Hexagonal (Ports & Adapters)

A arquitetura hexagonal é uma variação da Clean Architecture que usa o conceito de **portas** e **adaptadores**.

```text
                    ┌───────────────────────┐
                    │     DOMAIN            │
                    │  (core do negócio)    │
                    │                       │
                    │  ┌─────────────────┐  │
                    │  │   APPLICATION    │  │
                    │  │   (use cases)   │  │
                    │  └─────────────────┘  │
                    └───────────────────────┘
                           │         ▲
                      ┌────┘         └────┐
                      ▼                   │
              ┌──────────────┐   ┌────────────────┐
              │   INPUT      │   │    OUTPUT       │
              │   PORTS      │   │    PORTS        │
              │  (Controllers│   │  (Repositories, │
              │   handlers)  │   │   event bus)    │
              └──────────────┘   └────────────────┘
                      │                   ▲
                      ▼                   │
              ┌──────────────┐   ┌────────────────┐
               │  ADAPTERS    │   │   ADAPTERS     │
               │  (NestJS,    │   │  (Prisma,      │
               │   Express)   │   │   email, queue)│
               └──────────────┘   └────────────────┘
```

Abaixo, uma visão de container C4 da mesma arquitetura:

![Arquitetura de Referencia Backend - Container](/knowledge-factory/products/courses/arquitetura-backend/module-08-arquitetura/assets/diagram-c4-container.svg)

### Portas

```typescript
// Porta de saída (interface no domínio)
interface PedidoRepository {
  save(pedido: Pedido): Promise<void>;
  findById(id: PedidoId): Promise<Pedido | null>;
}

// Porta de entrada (interface do use case)
interface CriarPedidoUseCase {
  execute(input: CriarPedidoInput): Promise<CriarPedidoOutput>;
}
```text

### Adaptadores

```typescript
// Adaptador de saída (implementação externa)
class PrismaPedidoRepository implements PedidoRepository {
  async save(pedido: Pedido): Promise<void> {
    await prisma.pedido.create({
      data: this.toPersistence(pedido),
    });
  }

  private toPersistence(pedido: Pedido): PrismaPedido {
    return {
      id: pedido.id.toString(),
      clienteId: pedido.clienteId.toString(),
      valor: pedido.valor,
    };
  }
}

// Adaptador de entrada (NestJS Controller)
@Controller('/pedidos')
class PedidoController {
  constructor(private criarPedido: CriarPedidoUseCase) {}

  @Post()
  async criar(@Body() body: CriarPedidoDto) {
    return this.criarPedido.execute(this.toInput(body));
  }
}
```

---

## 6. Modular Monolith vs Microservices

### Modular Monolith

Um monólito **modularizado** — código em módulos bem definidos, mas deploy único.

```text
Prós:                     Contras:
- Simplicidade            - Escala tudo junto
- Deploy único            - Ponto único de falha
- Sem latência de rede    - Stack única
- Dados consistentes      - Time grande conflita
- Transações ACID

Quando usar:
  - Time pequeno (< 10 devs)
  - Sistema com domínios fortemente acoplados
  - Startup / MVP
  - Quando velocidade > escala
```

### Microservices

Serviços independentes, cada um com seu banco e deploy.

```text
Prós:                     Contras:
- Escala independente     - Complexidade de rede
- Deploy independente     - Dados distribuídos
- Stack variada           - Consistência eventual
- Times autônomos         - Observabilidade complexa
- Isolamento de falhas    - Testes mais difíceis

Quando usar:
  - Time grande (> 10 devs por serviço)
  - Domínios claramente separados
  - Escala global
  - Times autônomos por domínio
```

### A recomendação

> **Comece com Modular Monolith. Extraia microservices quando necessário.**

A maioria dos sistemas **não precisa** de microservices. Os que precisam, geralmente começaram como monólito e extraíram os serviços que escalavam de forma diferente.

---

## 7. Event-Driven Architecture

Event-Driven Architecture usa **eventos** para comunicação entre componentes.

### Conceitos

```text
Evento:           "Algo aconteceu"
  → PedidoCriado, UsuarioCadastrado, PagamentoConfirmado

Produtor:         Quem gera o evento
  → Serviço de pedidos publica "PedidoCriado"

Consumidor:       Quem reage ao evento
  → Serviço de email escuta "PedidoCriado" e envia confirmação

Barramento:       Meio de transporte
  → RabbitMQ, Kafka, Redis Pub/Sub
```

### Exemplo

```typescript
// Evento
class PedidoCriadoEvent {
  constructor(
    readonly pedidoId: string,
    readonly clienteEmail: string,
    readonly valor: number,
  ) {}
}

// Produtor
class CriarPedidoUseCase {
  constructor(
    private pedidoRepo: PedidoRepository,
    private eventBus: EventBus,
  ) {}

  async execute(input: CriarPedidoInput): Promise<void> {
    const pedido = Pedido.criar(input.clienteId, input.itens);
    await this.pedidoRepo.save(pedido);

    // Publica evento
    await this.eventBus.publish(
      new PedidoCriadoEvent(pedido.id, input.clienteEmail, pedido.valor)
    );
  }
}

// Consumidor
class EmailHandler {
  @OnEvent(PedidoCriadoEvent)
  async enviarConfirmacao(event: PedidoCriadoEvent) {
    await this.emailService.send({
      to: event.clienteEmail,
      subject: 'Pedido confirmado!',
      body: `Pedido #${event.pedidoId} no valor de R$ ${event.valor}`,
    });
  }
}
```text

---

## 8. Aplicando na prática com NestJS + Prisma

### Estrutura de pastas seguindo Clean Architecture + DDD

```
src/
├── domain/                    # Círculo mais interno
│   ├── entities/              # Entidades de domínio
│   │   └── usuario.ts
│   ├── value-objects/         # Value Objects
│   │   └── email.ts
│   ├── repositories/          # Interfaces (portas)
│   │   └── usuario.repository.ts
│   └── services/              # Domain Services
│       └── autenticacao.service.ts
│
├── application/               # Use Cases
│   ├── use-cases/
│   │   └── criar-usuario.use-case.ts
│   └── dto/
│       └── criar-usuario.dto.ts
│
├── infrastructure/            # Adaptadores (implementações)
│   ├── persistence/
│   │   └── prisma/
│   │       ├── prisma.service.ts
│   │       └── repositories/
│   │           └── prisma-usuario.repository.ts
│   ├── messaging/
│   │   └── rabbitmq-event-bus.ts
│   └── email/
│       └── nodemailer-email.service.ts
│
├── presentation/              # Adaptadores de entrada
│   ├── controllers/
│   │   └── usuario.controller.ts
│   └── guards/
│       └── jwt-auth.guard.ts
│
└── main.ts
