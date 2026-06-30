# Quiz — Módulo 14

## Pergunta 1

Qual o principal benefício do Docker?

- a) Aumentar performance do servidor
- b) Ambiente consistente em dev, staging e produção
- c) Substituir bancos de dados
- d) Gerenciar usuários

**Resposta:** b

---

## Pergunta 2

O que é multi-stage build no Docker?

- a) Construir múltiplas imagens ao mesmo tempo
- b) Usar múltiplos estágios para separar build do runtime, resultando em imagem final leve
- c) Rodar múltiplos containers
- d) Fazer deploy em múltiplos servidores

**Resposta:** b

---

## Pergunta 3

Qual a diferença entre CI e CD?

- a) São a mesma coisa
- b) CI integra e testa código automaticamente; CD faz deploy automático
- c) CI faz deploy; CD testa código
- d) CI é para frontend; CD é para backend

**Resposta:** b

---

## Pergunta 4

O que é um health check?

- a) Uma verificação de performance
- b) Um endpoint que verifica a saúde das dependências do sistema
- c) Um teste de carga
- d) Uma auditoria de segurança

**Resposta:** b

---

## Pergunta 5

Qual estratégia de deploy envolve enviar 5% do tráfego para a nova versão?

- a) Blue-Green
- b) Rolling Update
- c) Canary Release
- d) Big Bang

**Resposta:** c

---

## Pergunta 6

Para que serve o .dockerignore?

- a) Ignorar containers parados
- b) Excluir arquivos do contexto de build (node_modules, .env, .git)
- c) Ignorar erros no Docker
- d) Definir portas a ignorar

**Resposta:** b

---

## Pergunta 7

O que é graceful shutdown?

- a) Desligar o servidor rapidamente
- b) Finalizar requisições em andamento antes de desligar
- c) Reiniciar o servidor automaticamente
- d) Ignorar erros ao desligar

**Resposta:** b

---

## Pergunta 8

Por que logs devem ser estruturados (JSON)?

- a) Ocupam menos espaço
- b) São mais legíveis para humanos
- c) São searcháveis por ferramentas de observabilidade
- d) São mais rápidos de escrever

**Resposta:** c

---

## Pergunta 9

O que acontece se uma variável de ambiente obrigatória não for configurada?

- a) O sistema usa um valor padrão
- b) O sistema deve falhar na inicialização com erro claro
- c) O sistema ignora e continua
- d) O sistema pergunta ao usuário

**Resposta:** b

---

## Pergunta 10

Qual a diferença entre /health, /ready e /live?

- a) São a mesma coisa
- b) /health verifica dependências, /ready verifica se está apto a receber tráfego, /live verifica se o processo está rodando
- c) /live é para banco, /ready é para cache
- d) /health é para Kubernetes, /ready é para Docker

**Resposta:** b
