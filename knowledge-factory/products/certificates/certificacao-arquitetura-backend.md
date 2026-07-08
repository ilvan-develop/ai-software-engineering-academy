# Certificação — Arquitetura Backend

## Prova Objetiva (20 questões)

**Tempo estimado:** 60 minutos  
**Mínimo para aprovação:** 70% (14/20)  
**Pré-requisito:** Conclusão dos módulos 08 a 13d

---

### Questão 1
O que é Domain-Driven Design (DDD)?
a) Uma técnica de banco de dados
b) Uma abordagem de design de software que foca no domínio do problema e na colaboração entre especialistas e desenvolvedores
c) Um framework de frontend
d) Um padrão de segurança

**Gabarito:** B

### Questão 2
O que é um Bounded Context em DDD?
a) Um contexto de usuário limitado
b) Um limite explícito dentro do qual um modelo de domínio é consistente e aplicável
c) Uma restrição de segurança
d) Um tipo de banco de dados

**Gabarito:** B

### Questão 3
O que é CQRS (Command Query Responsibility Segregation)?
a) Um padrão que separa operações de leitura (queries) e escrita (commands) em modelos diferentes
b) Um tipo de banco de dados NoSQL
c) Uma técnica de cache
d) Um padrão de UI

**Gabarito:** A

### Questão 4
O que é Event Sourcing?
a) Um padrão que persiste o estado atual do sistema
b) Um padrão que armazena todas as mudanças de estado como uma sequência de eventos imutáveis
c) Um sistema de mensageria
d) Um framework de eventos

**Gabarito:** B

### Questão 5
Qual a diferença entre microservices e monólitos?
a) Microservices são sempre melhores
b) Microservices dividem o sistema em serviços independentes; monólitos concentram tudo em uma aplicação
c) Monólitos não têm API
d) Microservices não usam banco de dados

**Gabarito:** B

### Questão 6
O que é uma Entity em DDD?
a) Um objeto com identidade única que persiste ao longo do tempo
b) Uma tabela de banco de dados
c) Um valor sem identidade
d) Um serviço de domínio

**Gabarito:** A

### Questão 7
O que é um Value Object em DDD?
a) Um objeto imutável definido por seus atributos, sem identidade própria
b) Um objeto com identidade única
c) Um serviço externo
d) Um repositório de dados

**Gabarito:** A

### Questão 8
O que é um Aggregate em DDD?
a) Um conjunto de objetos de domínio tratados como uma única unidade para mudanças de estado
b) Uma função agregada SQL
c) Um serviço de infraestrutura
d) Um tipo de banco de dados

**Gabarito:** A

### Questão 9
O que é Hexagonal Architecture (Ports and Adapters)?
a) Uma arquitetura que isola o core da aplicação de dependências externas através de portas e adaptadores
b) Uma arquitetura de microserviços hexagonal
c) Um padrão de banco de dados
d) Um tipo de diagrama UML

**Gabarito:** A

### Questão 10
O que é Event Storming?
a) Um workshop colaborativo para modelagem de domínios complexos usando eventos como base
b) Uma técnica de estresse em sistemas
c) Um framework de eventos
d) Um padrão de segurança

**Gabarito:** A

### Questão 11
O que é multi-tenancy?
a) Uma arquitetura onde uma única instância de software atende múltiplos clientes (tenants)
b) Uma técnica de banco de dados distribuído
c) Um padrão de segurança
d) Um tipo de cache

**Gabarito:** A

### Questão 12
Qual estratégia de isolamento de dados é mais segura em multi-tenancy?
a) Database per Tenant
b) Shared Table
c) Schema per Tenant
d) Cache compartilhado

**Gabarito:** A (mais seguro, porém mais custoso)

### Questão 13
O que é um Domain Service em DDD?
a) Um serviço que orquestra regras de negócio que não pertencem naturalmente a uma Entity ou Value Object
b) Um microserviço
c) Uma API REST
d) Um serviço de infraestrutura

**Gabarito:** A

### Questão 14
O que é um Repository em DDD?
a) Um mecanismo que fornece acesso a objetos de domínio persistidos, abstraindo a infraestrutura
b) Um banco de dados SQL
c) Uma API REST
d) Um serviço de cache

**Gabarito:** A

### Questão 15
O que é um Anti-Corruption Layer?
a) Uma camada que protege o modelo de domínio de modelos externos inconsistentes
b) Uma camada de segurança
c) Um firewall de aplicação
d) Uma camada de cache

**Gabarito:** A

### Questão 16
Qual padrão de integração entre bounded contexts é mais acoplado?
a) Partnership
b) Shared Kernel
c) Customer-Supplier
d) Conformist

**Gabarito:** B (Shared Kernel compartilha modelo)

### Questão 17
O que é Saga Pattern em microservices?
a) Um padrão para gerenciar transações distribuídas através de uma sequência de etapas locais com compensação
b) Uma técnica de deploy
c) Um padrão de segurança
d) Um tipo de banco de dados

**Gabarito:** A

### Questão 18
Qual é a diferença entre Choreography e Orchestration em Sagas?
a) Coreografia é descentralizada (cada serviço reage a eventos); Orquestração tem um coordenador central
b) São sinônimos
c) Orquestração é sempre melhor
d) Coreografia usa REST, Orquestração usa mensageria

**Gabarito:** A

### Questão 19
O que é um Domain Event?
a) Um evento técnico do sistema
b) Um evento que representa algo significativo que aconteceu no domínio, processado por outros agregados/services
c) Um log de auditoria
d) Uma notificação push

**Gabarito:** B

### Questão 20
Por que usar DDD + CQRS + Event Sourcing juntos?
a) Porque combinam modelagem de domínio rica (DDD), segregação de responsabilidade (CQRS) e rastreabilidade total (ES)
b) Porque são frameworks obrigatórios
c) Porque são fáceis de implementar
d) Porque eliminam a necessidade de banco de dados

**Gabarito:** A

---

## Prova Prática — Projeto

**Título:** Modelagem de um Contexto Delimitado

**Descrição:** Modele um contexto delimitado de um sistema real:
1. Identifique Entities, Value Objects, Aggregates e Domain Events
2. Defina os bounded contexts vizinhos e suas relações (Context Map)
3. Escolha o padrão de integração para cada relação
4. Implemente um Aggregate Root com validações de domínio em TypeScript
