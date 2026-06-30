# Quiz — Capítulo 3: Automação do Ciclo de Desenvolvimento com IA

**Instruções:** Responda às 5 perguntas de múltipla escolha. Apenas uma alternativa está correta.

---

## Pergunta 1 (Fácil)

O capítulo lista diversos motivos para automatizar processos de desenvolvimento. Qual das alternativas abaixo **NÃO** é um desses motivos?

- [ ] A) Reduzir erro humano
- [ ] B) Aumentar a criatividade do time
- [ ] C) Garantir reprodutibilidade
- [ ] D) Permitir auditoria através de logs e artefatos

**Resposta correta:** B
**Explicação:** O capítulo apresenta 5 motivos para automatizar: reduzir erro humano, velocidade, reprodutibilidade, auditoria e escala. "Aumentar a criatividade do time" não é listado como motivo — automação elimina tarefas repetitivas, o que pode indiretamente liberar tempo para criatividade, mas o capítulo não apresenta isso como uma razão direta. As alternativas A, C e D estão explicitamente na tabela de motivos do capítulo.
**Nível:** Fácil

---

## Pergunta 2 (Fácil)

Qual é a diferença fundamental entre Continuous Delivery e Continuous Deployment, conforme explicado no capítulo?

- [ ] A) Continuous Delivery é para frontend; Continuous Deployment é para backend.
- [ ] B) Continuous Delivery requer testes manuais; Continuous Deployment usa apenas testes automatizados.
- [ ] C) No Continuous Delivery, o deploy em produção é manual (aprovado por um humano); no Continuous Deployment, o deploy é automático após a pipeline CI passar.
- [ ] D) Continuous Delivery usa GitHub Actions; Continuous Deployment usa GitLab CI.

**Resposta correta:** C
**Explicação:** O capítulo define claramente: **Continuous Delivery:** "O artefato é gerado e publicado em um repositório, mas o deploy em produção é manual (aprovado por um humano)". **Continuous Deployment:** "O deploy em produção é automático após a pipeline CI passar". A diferença está no gate humano, não na tecnologia usada (A e D estão errados) nem no tipo de teste (B está errado — ambos usam testes automatizados).
**Nível:** Fácil

---

## Pergunta 3 (Médio)

No contexto de estratégias de deploy, qual técnica consiste em manter duas versões completas do ambiente (uma atual e uma nova) e alternar o tráfego através do balanceador de carga?

- [ ] A) Rolling Update
- [ ] B) Canary Deployment
- [ ] C) Blue-Green Deployment
- [ ] D) Feature Flags

**Resposta correta:** C
**Explicação:** O **Blue-Green Deployment** mantém dois ambientes completos: Blue (versão atual, recebendo tráfego) e Green (nova versão). Após validação da Green, o balanceador de carga alterna o tráfego. O rollback é imediato, revertendo o DNS para Blue. **Rolling Update** (A) substitui instâncias gradualmente. **Canary** (B) envia uma porcentagem pequena de tráfego para a nova versão. **Feature Flags** (D) ativam/desativam funcionalidades sem deploy.
**Nível:** Médio

---

## Pergunta 4 (Médio)

O que é Infrastructure as Code (IaC) de acordo com o capítulo?

- [ ] A) Um framework para escrever código de infraestrutura em Python.
- [ ] B) O gerenciamento de servidores, bancos e redes através de arquivos de configuração versionados, tratando infraestrutura como software.
- [ ] C) Um serviço AWS que cria servidores virtualizados automaticamente.
- [ ] D) A prática de documentar a infraestrutura existente em arquivos README.

**Resposta correta:** B
**Explicação:** O capítulo define IaC como "o gerenciamento de infraestrutura (servidores, bancos, redes) através de arquivos de configuração versionados". Ferramentas como Terraform, Pulumi e CloudFormation permitem que a infraestrutura seja tratada como código — versionada, revisada, testada e reproduzível. A alternativa A é restritiva (IaC não se limita a Python). C descreve um serviço específico (AWS EC2), não o conceito de IaC. D confunde documentação com infraestrutura como código.
**Nível:** Médio

---

## Pergunta 5 (Difícil)

Um time implementou uma pipeline de CI/CD com as seguintes etapas em sequência:
1. Lint
2. Testes unitários
3. Build
4. Deploy automático em produção (Continuous Deployment)

Não há etapa de migração de banco de dados, análise de segurança, testes de integração, code review automatizado ou health check pós-deploy. O deploy usa rolling update.

Considerando as práticas recomendadas no capítulo, qual análise melhor descreve os riscos dessa pipeline?

- [ ] A) A pipeline está completa, pois lint + testes unitários + build + deploy cobre todos os aspectos essenciais.
- [ ] B) O maior risco é a falta de migração de banco, que pode causar inconsistência entre schema e código. Os demais itens são opcionais.
- [ ] C) A pipeline apresenta riscos graves: (1) sem migração de BD, o schema pode ficar inconsistente com o código; (2) sem análise de segurança (SAST/DAST), vulnerabilidades vão para produção; (3) sem testes de integração, bugs de interação entre módulos não são detectados; (4) sem health check, um deploy com falha passa despercebido até afetar usuários.
- [ ] D) O único problema é a falta de testes e2e; os demais itens são boas práticas mas não críticos.

**Resposta correta:** C
**Explicação:** O capítulo dedica seções inteiras a cada um desses riscos: **Migrações automáticas** (seção 6) — sem migração, o banco pode ficar fora de sincronia com o código. **Segurança** (seção 7) — SAST (SonarQube, ESLint security), DAST (OWASP ZAP) e varredura de dependências (Snyk, npm audit) são essenciais. **Testes de integração** (seção 3) — a pirâmide de testes inclui testes unitários, de integração e e2e; pular integração significa não testar a interação entre módulos com banco real. **Health check** (seção 12) — o capítulo mostra um exemplo explícito de health check pós-deploy com rollback automático em caso de falha. A alternativa A está errada porque ignora todos esses riscos. B subestima a gravidade da falta de segurança e testes de integração. D é incorreta porque testes e2e são apenas uma camada; faltam itens mais críticos como segurança e migração.
**Nível:** Difícil

---

---

## Pergunta 6 (Médio)

Em uma estratégia de Canary Deployment, qual é a principal vantagem em relação ao Blue-Green Deployment?

- [ ] A) Canary é mais barato porque não requer um ambiente duplicado completo.
- [ ] B) Canary permite testar a nova versão com uma fração do tráfego real antes de expandir, reduzindo o impacto de falhas.
- [ ] C) Canary não precisa de balanceador de carga.
- [ ] D) Canary funciona apenas em Kubernetes, enquanto Blue-Green funciona em qualquer plataforma.

**Resposta correta:** B
**Explicação:** O capítulo explica que Canary Deployment "envia uma pequena porcentagem do tráfego para a nova versão" e "monitora métricas antes de aumentar gradualmente". A principal vantagem sobre Blue-Green é que, no Canary, você expõe a mudança a um subconjunto real de usuários e observa o comportamento antes de liberar para todos — em vez de alternar todo o tráfego de uma vez como no Blue-Green. A alternativa A é incorreta: Blue-Green requer ambientes duplicados, Canary também precisa de múltiplas versões rodando simultaneamente. C é falsa — Canary também usa balanceador de carga. D é falsa — ambas as estratégias são independentes de plataforma.
**Nível:** Médio

---

## Pergunta 7 (Médio)

O capítulo apresenta uma hierarquia de observabilidade com 3 níveis. Qual das alternativas abaixo representa CORRETAMENTE essa hierarquia, do mais fundamental ao mais avançado?

- [ ] A) Logs → Métricas → Tracing
- [ ] B) Métricas → Logs → Dashboards
- [ ] C) Alertas → Dashboards → Logs
- [ ] D) Tracing → Métricas → Logs

**Resposta correta:** A
**Explicação:** O capítulo define a hierarquia de observabilidade como: **Logs** (base — todo evento gerado pelo sistema, mais granular), **Métricas** (intermediário — agregações como P95, error rate, requests/s), **Tracing** (topo — rastreamento de uma requisição através de múltiplos serviços). A metáfora usada é: "Logs dizem o que aconteceu em cada ponto, métricas mostram tendências agregadas, tracing revela o caminho completo de uma requisição." As alternativas B, C e D invertem ou omitem elementos dessa hierarquia.
**Nível:** Médio

---

## Gabarito

| Pergunta | Resposta | Nível |
|----------|----------|-------|
| 1 | B | Fácil |
| 2 | C | Fácil |
| 3 | C | Médio |
| 4 | B | Médio |
| 5 | C | Difícil |
| 6 | B | Médio |
| 7 | A | Médio |
