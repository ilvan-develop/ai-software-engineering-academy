# Agentes para o Módulo 14

## Agentes envolvidos

| Agente | Função no módulo |
|--------|------------------|
| Curriculum Architect | Estruturar pipeline DevOps |
| Technical Writer | Escrever Dockerfiles e pipelines reais |
| Reviewer | Validar boas práticas de infraestrutura |
| DevOps Expert Agent | Referência prática |

## Instruções específicas

### Curriculum Architect

Ao planejar:
- Conectar com Módulo 10 (Backend) — o backend precisa ser dockerizado
- Conectar com Módulo 16 (Observabilidade) — logs e métricas
- Foco em Docker + GitHub Actions (Kubernetes é opcional)

### Technical Writer

Ao escrever:
- Dockerfiles que realmente funcionam (com multi-stage)
- Pipeline CI/CD que cobre lint, test, build e deploy
- Incluir validação de env na inicialização
- Explicar cada linha do Dockerfile
