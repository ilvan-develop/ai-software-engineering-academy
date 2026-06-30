# Checklist: DevOps Expert Agent

- [ ] Dockerfile multi-stage (build separado de runtime)
- [ ] Imagem final leve (alpine/slim)
- [ ] Health checks no Dockerfile (HEALTHCHECK)
- [ ] .dockerignore configurado
- [ ] docker-compose com serviços: app, db, redis, queue
- [ ] Volumes persistentes configurados
- [ ] CI/CD com cache otimizado
- [ ] Testes rodam no pipeline
- [ ] Lint e type check no pipeline
- [ ] Deploy automático em staging
- [ ] Variáveis de ambiente via .env.example
- [ ] Logs estruturados (JSON)
- [ ] Backup automático do banco
- [ ] Monitoramento básico (health endpoint + logs)
