# Quiz — Módulo 20: Automação

**10 questões de múltipla escolha**  
**Todas as questões têm apenas 1 resposta correta.**

---

### Questão 1

Qual é a principal diferença entre Continuous Delivery e Continuous Deployment?

- A) Continuous Delivery executa testes; Continuous Deployment não
- B) Continuous Delivery requer aprovação manual para deploy em produção; Continuous Deployment faz deploy automático
- C) Continuous Deployment só funciona com Kubernetes
- D) Continuous Delivery é mais rápido que Continuous Deployment

**Resposta correta: B**

---

### Questão 2

Em uma pipeline CI/CD, qual é a ordem mais eficiente para execução dos jobs?

- A) Build → Testes de Integração → Testes Unitários → Lint → Deploy
- B) Deploy → Testes E2E → Lint → Testes Unitários → Build
- C) Lint → Testes Unitários → Testes de Integração → Build → Deploy
- D) Testes E2E → Testes de Integração → Testes Unitários → Lint → Deploy

**Resposta correta: C**

Justificativa: Jobs mais rápidos e que mais provavelmente falham devem rodar primeiro (fail fast). Lint é o mais rápido, seguido de testes unitários, depois integração, build e deploy.

---

### Questão 3

O que é um "ephemeral environment"?

- A) Um ambiente de produção com alta disponibilidade
- B) Um ambiente temporário criado automaticamente para uma branch/PR e destruído após o merge
- C) Um ambiente de disaster recovery em outra região
- D) Um ambiente compartilhado entre todos os desenvolvedores

**Resposta correta: B**

---

### Questão 4

Qual estratégia de deploy expõe uma porcentagem pequena de tráfego para a nova versão antes de aumentar gradualmente até 100%?

- A) Blue-Green
- B) Rolling Update
- C) Canary
- D) Big Bang

**Resposta correta: C**

---

### Questão 5

No contexto de automação de segurança, o que significa SAST?

- A) Security Automated Scan Testing
- B) Static Application Security Testing — análise de segurança no código fonte sem executá-lo
- C) System Application Security Tool
- D) Smart Automated Security Test

**Resposta correta: B**

---

### Questão 6

Qual ferramenta NÃO é classificada como Infrastructure as Code (IaC)?

- A) Terraform
- B) Pulumi
- C) Docker Compose
- D) SonarQube

**Resposta correta: D**

Justificativa: SonarQube é uma ferramenta de qualidade e segurança de código (SAST), não de infraestrutura como código.

---

### Questão 7

O que é necessário para o semantic-release funcionar corretamente?

- A) Testes E2E passando
- B) Commits seguindo o padrão Conventional Commits (feat:, fix:, etc.)
- C) Code coverage > 80%
- D) Pipeline com menos de 5 minutos de execução

**Resposta correta: B**

Justificativa: O semantic-release analisa as mensagens de commit para determinar o próximo número de versão e gerar o changelog. Sem Conventional Commits, ele não consegue determinar se é uma feat (minor), fix (patch) ou breaking change (major).

---

### Questão 8

Em uma pipeline de CI/CD, qual é a melhor prática para lidar com migrations de banco de dados?

- A) Executar migrations manualmente antes do deploy
- B) Fazer backup do banco antes da migration, executar a migration, e ter rollback automatizado em caso de falha
- C) Nunca rodar migrations em pipeline — apenas em scripts locais
- D) Rodar a migration depois do deploy, sem backup

**Resposta correta: B**

---

### Questão 9

O que são feature flags?

- A) Flags que indicam quais funcionalidades estão em desenvolvimento
- B) Mecanismos para ativar/desativar funcionalidades sem fazer deploy, permitindo liberação gradual e rollback instantâneo
- C) Bandeiras visuais no frontend para indicar novas features
- D) Testes A/B exclusivos para designers

**Resposta correta: B**

---

### Questão 10

Qual das seguintes práticas NÃO é recomendada para pipelines as code?

- A) Modularizar jobs em actions reutilizáveis
- B) Usar cache de dependências para acelerar a pipeline
- C) Hardcodar secrets nos arquivos YAML da pipeline
- D) Usar matrix strategy para testar múltiplas versões da linguagem

**Resposta correta: C**

Justificativa: Secrets nunca devem ser hardcodados em arquivos de pipeline. Devem ser armazenados em segredos do repositório (GitHub Secrets, GitLab CI Variables, etc.) e referenciados via `${{ secrets.NOME_DO_SECRET }}`.
