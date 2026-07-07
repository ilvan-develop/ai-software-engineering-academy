# Apêndice A — Glossário

## A

**ACID**
Conjunto de propriedades de transações em banco de dados: Atomicidade, Consistência, Isolamento, Durabilidade.

**Adapter (Adaptador)**
Implementação concreta de uma porta (interface) na Arquitetura Hexagonal.

**ADR (Architecture Decision Record)**
Documento que registra uma decisão arquitetural, seu contexto, alternativas consideradas e consequências.

**Aggregate (Agregado)**
Grupo de entidades tratado como unidade de consistência transacional no DDD. Possui uma raiz (Aggregate Root).

## B

**Bounded Context**
Limite explícito dentro do qual um modelo de domínio é válido. Conceito central do DDD.

**Breakpoint**
Ponto de observabilidade onde uma mudança de estado pode ser inspecionada.

## C

**C4 Model**
Modelo de documentação arquitetural em 4 níveis: Contexto, Container, Componente, Código.

**Clean Architecture**
Arquitetura em camadas concêntricas proposta por Robert C. Martin, onde as dependências apontam para dentro.

**CQRS (Command Query Responsibility Segregation)**
Padrão que separa operações de leitura (queries) e escrita (commands).

## D

**DDD (Domain-Driven Design)**
Abordagem de desenvolvimento que coloca o domínio do negócio no centro do modelo de software.

**Dependency Inversion**
Princípio SOLID que diz: dependa de abstrações, não de implementações concretas.

**Design Pattern**
Solução reutilizável para um problema recorrente em design de software.

**DTO (Data Transfer Object)**
Objeto usado para transferir dados entre camadas, sem comportamento.

## E

**Entity (Entidade)**
Objeto de domínio com identidade única e ciclo de vida rastreável.

**Event-Driven Architecture**
Arquitetura onde componentes se comunicam através de eventos assíncronos.

## G

**Guard (NestJS)**
Decorator do NestJS usado para autorização e validação de acesso a rotas.

## H

**Hexagonal Architecture (Ports & Adapters)**
Arquitetura que organiza o código em torno de portas (interfaces) e adaptadores (implementações).

## I

**Idempotência**
Propriedade de uma operação que pode ser executada múltiplas vezes sem efeitos colaterais além da primeira.

**Interface Segregation**
Princípio SOLID: interfaces específicas são melhores que interfaces genéricas.

## J

**JWT (JSON Web Token)**
Token de autenticação auto-contido, composto por header, payload e assinatura.

## K

**Kubernetes**
Orquestrador de containers para deploy, scaling e operação de aplicações.

## L

**LSP (Liskov Substitution Principle)**
Princípio SOLID: subtipos devem ser substituíveis por seus tipos base.

**Linguagem Ubíqua**
Vocabulário compartilhado e consistente entre equipe técnica e de negócios.

## M

**Microservices**
Estilo arquitetural onde o sistema é composto por serviços pequenos, independentes e fracamente acoplados.

**Middleware**
Função executada no ciclo request-response, usada para logging, autenticação, etc.

**Modular Monolith**
Monólito estruturado em módulos bem definidos, com boundaries claros, mas deploy único.

**Multi-Tenancy**
Arquitetura onde uma única instância de software atende múltiplos clientes (tenants) com isolamento de dados.

## N

**NestJS**
Framework Node.js progressivo para construção de aplicações server-side eficientes e escaláveis.

## O

**OCP (Open/Closed Principle)**
Princípio SOLID: aberto para extensão, fechado para modificação.

**Observabilidade**
Capacidade de inferir o estado interno de um sistema através de métricas, logs e traces.

## P

**Pipe (NestJS)**
Decorator para transformação e validação de dados de entrada no NestJS.

**Porta (Port)**
Interface que define um ponto de interação entre camadas na Arquitetura Hexagonal.

**Prisma ORM**
ORM moderno para Node.js/TypeScript com foco em type-safety e produtividade.

## R

**RBAC (Role-Based Access Control)**
Modelo de controle de acesso baseado em papéis atribuídos a usuários.

**Repository**
Padrão que abstrai a persistência de dados, provendo interface de coleção para o domínio.

## S

**Saga Pattern**
Padrão para gerenciar transações distribuídas através de uma sequência de etapas compensatórias.

**SOLID**
Acrônimo para 5 princípios de design: SRP, OCP, LSP, ISP, DIP.

**SRP (Single Responsibility Principle)**
Princípio SOLID: uma classe deve ter um, e apenas um, motivo para mudar.

## T

**Tenant**
Cliente ou inquilino em um sistema multi-tenant. Cada tenant possui dados e configurações isoladas.

**Token**
Representação segura de uma sessão de autenticação, comumente no formato JWT.

## U

**Use Case (Caso de Uso)**
Unidade de funcionalidade da aplicação que orquestra entidades e serviços de domínio.

## V

**Value Object**
Objeto imutável descrito por seus atributos, sem identidade própria.

## W

**WebSocket**
Protocolo de comunicação bidirecional full-duplex sobre TCP, usado para tempo real.

## Z

**Zero Trust**
Modelo de segurança que nunca confia implicitamente em nenhum request, mesmo dentro da rede interna.
