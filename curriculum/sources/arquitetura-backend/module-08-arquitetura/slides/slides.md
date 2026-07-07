# Módulo 08 — Slides

---

## Slide 1: Título

**Arquitetura de Software**
Clean Architecture, DDD, SOLID e padrões Enterprise

---

## Slide 2: Por que arquitetura importa?

```text
Arquitetura Ruim:
  Feature nova: 2 semanas ("código macarrão")
  Bug: quebra tudo ("medo de mexer")

Arquitetura Boa:
  Feature nova: 2 dias ("só adicionar módulo")
  Bug: localizado ("testes garantem")
```markdown

---

## Slide 3: SOLID

- **S** — Single Responsibility (1 motivo para mudar)
- **O** — Open/Closed (extensão, não modificação)
- **L** — Liskov Substitution (subtipos substituíveis)
- **I** — Interface Segregation (interfaces específicas)
- **D** — Dependency Inversion (abstrações, não concretas)

---

## Slide 4: Clean Architecture

```text
       ENTITIES (regras enterprise)
    ┌─┴─┐
    │ UC │ USE CASES (regras da aplicação)
  ┌─┴───┴─┐
  │ ADAPTERS │ (controllers, presenters, gateways)
┌─┴─────────┴─┐
│ FRAMEWORKS   │ (NestJS, Prisma, Next.js)
└──────────────┘
```yaml

Regra: dependências apontam **para dentro**

---

## Slide 5: DDD — Domain-Driven Design

**Linguagem Ubíqua:** mesma do negócio, mesma do código

**Bounded Context:**
- Vendas: "Cliente = quem compra"
- Logística: "Cliente = quem recebe"

**Elementos:**
- Entity (tem identidade)
- Value Object (descrito por atributos)
- Aggregate (grupo com raiz)
- Repository (abstração de persistência)

---

## Slide 6: Exemplo DDD

```typescript
class Usuario {
  private readonly id: UsuarioId;
  private email: Email;  // Value Object

  alterarPerfil(novo: Perfil) {
    // Regra de negócio aqui!
    if (this.perfil.eAdmin() && !novo.eAdmin()
        && !this.temOutroAdmin()) {
      throw new Error('Precisa de ao menos 1 admin');
    }
    this.perfil = novo;
  }
}
```markdown

---

## Slide 7: Hexagonal (Ports & Adapters)

```javascript
DOMAIN ←──→ Ports ←──→ Adapters ←──→ External

Porta (interface):    PedidoRepository { save, findById }
Adaptador (impl):     PrismaPedidoRepository

Vantagem: troca Prisma por TypeORM sem tocar no domínio
```markdown

---

## Slide 8: Modular Monolith vs Microservices

| Monolith Modular | Microservices |
|-----------------|---------------|
| Deploy único | Deploy independente |
| Dados consistentes | Dados distribuídos |
| Simples | Complexo |
| Time < 10 devs | Time > 10 devs/serviço |

**Recomendação:** Comece com monólito, extraia depois.

---

## Slide 9: Event-Driven Architecture

```text
PedidoCriado → EventBus → EmailService (envia confirmação)
                        → EstoqueService (baixa estoque)
                        → FaturamentoService (emite nota)
```markdown

Desacopla produtores de consumidores

---

## Slide 10: Estrutura NestJS + Clean Arch

```javascript
src/
├── domain/           Entities, VOs, Repository interfaces
├── application/      Use Cases, DTOs
├── infrastructure/   Prisma, email, queue (implementações)
├── presentation/     Controllers, guards
└── main.ts
```javascript

Regra de ouro: **Domain não importa nada externo**

---

## Slide 11: Anti-padrões

- **Anemic Domain Model** — entidades sem comportamento
- **God Class** — classe que faz tudo
- **Dependency hell** — dependências circulares
- **Ripple effect** — mudança num lugar quebra vários
- **DTO reuse** — mesma classe para request, response, persistência

---

## Slide 12: Para refletir

> "Arquitetura não é sobre acertar de primeira. É sobre tornar fácil mudar quando você descobrir que errou."

> "Código sem arquitetura funciona hoje. Código com arquitetura funciona **todos os dias**."
