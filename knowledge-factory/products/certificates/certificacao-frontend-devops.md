# Certificação — Frontend & DevOps

## Prova Objetiva (20 questões)

**Tempo estimado:** 60 minutos  
**Mínimo para aprovação:** 70% (14/20)  
**Pré-requisito:** Conclusão dos módulos 11, 14, 15, 16

---

### Questão 1
Qual a principal vantagem do Next.js como framework React?
a) Renderização server-side (SSR) e geração estática (SSG) integradas
b) Substitui completamente CSS
c) Elimina a necessidade de JavaScript
d) É mais rápido que React puro em todos os casos

**Gabarito:** A

### Questão 2
O que é CI/CD?
a) Continuous Integration / Continuous Delivery — integração contínua e entrega contínua automatizadas
b) Code Inspection / Code Deployment
c) Cloud Integration / Cloud Development
d) Continuous Improvement / Continuous Design

**Gabarito:** A

### Questão 3
O que é um container Docker?
a) Uma máquina virtual completa
b) Uma unidade padronizada de software que empacota código e dependências para execução isolada
c) Um sistema operacional
d) Um tipo de banco de dados

**Gabarito:** B

### Questão 4
O que é Kubernetes?
a) Um provedor de nuvem
b) Uma plataforma para orquestração de containers, automatizando deploy, scaling e operação
c) Um banco de dados distribuído
d) Um framework de testes

**Gabarito:** B

### Questão 5
Qual a diferença entre teste unitário e teste de integração?
a) Unitário testa funções isoladas; Integração testa a interação entre componentes
b) São a mesma coisa
c) Integração é mais rápido
d) Unitário precisa de banco de dados

**Gabarito:** A

### Questão 6
O que é observabilidade?
a) A capacidade de monitorar sistemas
b) A capacidade de entender o estado interno de um sistema através de seus outputs (logs, métricas, traces)
c) Um dashboard de métricas
d) Uma ferramenta de logging

**Gabarito:** B

### Questão 7
O que os três pilares da observabilidade (logs, métricas, traces) oferecem?
a) Visão completa do comportamento do sistema para debugging e análise
b) Apenas logs de erro
c) Métricas de negócio
d) Testes automatizados

**Gabarito:** A

### Questão 8
O que é um Pod no Kubernetes?
a) A menor unidade implantável, que contém um ou mais containers
b) Um nó do cluster
c) Um serviço de rede
d) Um volume de armazenamento

**Gabarito:** A

### Questão 9
O que é Server-Side Rendering (SSR)?
a) Renderizar a página no servidor e enviar HTML pronto para o cliente
b) Renderizar no navegador usando JavaScript
c) Cache de páginas estáticas
d) API de servidor

**Gabarito:** A

### Questão 10
O que é um Service no Kubernetes?
a) Uma abstração que expõe um conjunto de Pods como um serviço de rede
b) Um container
c) Um deployment
d) Um volume de dados

**Gabarito:** A

### Questão 11
Qual a diferença entre teste E2E e teste de componente?
a) E2E testa fluxos completos do sistema; componente testa partes isoladas da UI
b) São equivalentes
c) Componente é mais lento
d) E2E não usa navegador

**Gabarito:** A

### Questão 12
O que é Prometheus?
a) Um sistema de monitoramento e alerta open source, especializado em séries temporais
b) Um banco de dados SQL
c) Um framework frontend
d) Uma ferramenta de deploy

**Gabarito:** A

### Questão 13
O que é um Deployment no Kubernetes?
a) Um recurso que gerencia o rollout de Pods com estratégias de atualização
b) Um container
c) Um serviço de rede
d) Um volume persistente

**Gabarito:** A

### Questão 14
Qual a vantagem de GitOps?
a) Usar Git como única fonte de verdade para infraestrutura e deploy
b) Eliminar a necessidade de CI/CD
c) Deploy manual
d) Versionar apenas código

**Gabarito:** A

### Questão 15
O que é Core Web Vitals?
a) Métricas do Google que medem performance, responsividade e estabilidade visual de páginas web
b) Um framework de CSS
c) Uma biblioteca React
d) Um padrão de design

**Gabarito:** A

### Questão 16
O que é LCP (Largest Contentful Paint)?
a) Mede o tempo até o maior elemento de conteúdo ser renderizado na tela
b) Mede o tempo de carregamento total
c) Mede interatividade
d) Mede estabilidade visual

**Gabarito:** A

### Questão 17
O que é um HorizontalPodAutoscaler?
a) Um recurso que ajusta automaticamente o número de Pods baseado em métricas de CPU/memória
b) Um balanceador de carga manual
c) Um tipo de Pod
d) Um volume de armazenamento

**Gabarito:** A

### Questão 18
O que diferencia teste de performance de teste de carga?
a) Performance testa comportamento geral; Carga testa sistema sob condições esperadas/pico
b) São a mesma coisa
c) Carga não usa métricas
d) Performance é manual

**Gabarito:** A

### Questão 19
O que é um Ingress no Kubernetes?
a) Um recurso que gerencia acesso externo a serviços HTTP/HTTPS com regras de roteamento
b) Um container de entrada
c) Um tipo de Pod
d) Um volume de rede

**Gabarito:** A

### Questão 20
Qual a melhor prática para secrets em CI/CD?
a) Usar GitHub Secrets ou ferramenta de gerenciamento de secrets (Vault)
b) Commitar .env no repositório
c) Compartilhar por mensagem
d) Usar variáveis de ambiente fixas no código

**Gabarito:** A

---

## Prova Prática — Projeto

**Título:** Pipeline CI/CD + Observabilidade

**Descrição:** Configure um pipeline completo para uma aplicação Next.js:
1. CI com testes unitários e de integração
2. Dockerfile multi-stage otimizado
3. Deploy Kubernetes com HPA
4. Configuração de Prometheus + Grafana para métricas
