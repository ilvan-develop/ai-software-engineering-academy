# Quiz — Capítulo 1: Fundamentos de Arquitetura

**Instruções:** 5 perguntas de múltipla escolha. Apenas uma alternativa correta.

---

## Pergunta 1 (Fácil)

Qual princípio SOLID afirma que "uma classe deve ter um, e apenas um, motivo para mudar"?

- [ ] A) Open/Closed Principle (OCP)
- [ ] B) Liskov Substitution Principle (LSP)
- [ ] C) **Single Responsibility Principle (SRP)**
- [ ] D) Dependency Inversion Principle (DIP)

**Resposta:** C
**Explicação:** SRP diz que cada classe deve ter uma única responsabilidade, um único motivo para mudar.

---

## Pergunta 2 (Fácil)

Na Clean Architecture, as dependências de código fonte devem apontar:

- [ ] A) Para fora, em direção aos frameworks
- [ ] B) **Para dentro, em direção ao centro (entities/use cases)**
- [ ] C) Lateralmente, entre camadas do mesmo nível
- [ ] D) Não há regra de direção de dependências

**Resposta:** B

---

## Pergunta 3 (Médio)

Em DDD, qual conceito define um limite explícito onde um modelo de domínio se aplica?

- [ ] A) Aggregate
- [ ] B) **Bounded Context**
- [ ] C) Value Object
- [ ] D) Domain Event

**Resposta:** B

---

## Pergunta 4 (Médio)

Na Arquitetura Hexagonal, qual é a diferença entre Porta e Adaptador?

- [ ] A) Porta é a implementação concreta; Adaptador é a interface
- [ ] B) **Porta é a interface (abstração); Adaptador é a implementação concreta**
- [ ] C) Ambos são sinônimos para a mesma coisa
- [ ] D) Porta é para entrada de dados; Adaptador é para saída

**Resposta:** B

---

## Pergunta 5 (Difícil)

Qual é a recomendação do capítulo sobre Modular Monolith vs Microservices?

- [ ] A) Sempre usar microservices para garantir escalabilidade
- [ ] B) **Comece com Modular Monolith. Extraia microservices quando necessário.**
- [ ] C) Monoliths são sempre superiores para qualquer escala
- [ ] D) Microservices são a única arquitetura enterprise viável

**Resposta:** B
