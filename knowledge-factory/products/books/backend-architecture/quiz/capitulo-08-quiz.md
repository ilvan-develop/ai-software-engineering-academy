# Quiz — Capítulo 8: Multi-Tenant — Operações e Qualidade

**Instruções:** 5 perguntas de múltipla escolha. Apenas uma alternativa correta.

---

## Pergunta 1 (Fácil)

Por que é importante ter métricas por tenant em um sistema multi-tenant?

- [ ] A) **Para identificar quais tenants estão sobrecarregando o sistema e quais estão ociosos**
- [ ] B) Para cobrar mais dos tenants que usam menos recursos
- [ ] C) Para desligar tenants que não usam o sistema
- [ ] D) Apenas para relatórios de auditoria

**Resposta:** A

---

## Pergunta 2 (Fácil)

O que um teste de isolamento entre tenants deve verificar?

- [ ] A) Se o sistema responde rápido para todos os tenants
- [ ] B) **Se um tenant não consegue acessar dados de outro tenant**
- [ ] C) Se a interface do usuário é consistente
- [ ] D) Se o custo por tenant é aceitável

**Resposta:** B

---

## Pergunta 3 (Médio)

Por que o rate limiting deve ser por tenant em vez de global?

- [ ] A) **Para que um tenant com alta demanda não afete a experiência dos demais**
- [ ] B) Porque é mais fácil de implementar
- [ ] C) Porque o rate limiting global não funciona
- [ ] D) Para reduzir o número de requisições totais

**Resposta:** A

---

## Pergunta 4 (Médio)

Em um onboarding automatizado de tenant, qual etapa deve vir ANTES da criação do usuário admin?

- [ ] A) Enviar email de boas-vindas
- [ ] B) **Provisionar infraestrutura e rodar migrations**
- [ ] C) Configurar dashboards de monitoramento
- [ ] D) Notificar a equipe de operações

**Resposta:** B

---

## Pergunta 5 (Difícil)

Qual padrão de resiliência é mais adequado para o onboarding de tenants em sistemas com alta disponibilidade?

- [ ] A) Request-Response síncrono com timeout
- [ ] B) **Processamento assíncrono com fila (Bull/RabbitMQ) e retry**
- [ ] C) Batch processing noturno
- [ ] D) Serverless functions com callback

**Resposta:** B
