# Quiz — Capítulo 2: Agentes de IA na Prática

**Instruções:** Responda às 5 perguntas de múltipla escolha. Apenas uma alternativa está correta.

---

## Pergunta 1 (Fácil)

Segundo o capítulo, qual é a principal desvantagem de usar um único agente genérico em vez de um ecossistema de agentes especializados?

- [ ] A) O agente genérico é mais lento para responder porque tem muito conhecimento.
- [ ] B) O agente genérico produz resultados medianos em todas as áreas, gerando código com dívida técnica.
- [ ] C) O agente genérico não consegue escrever código em TypeScript.
- [ ] D) O agente genérico se recusa a executar tarefas fora do seu domínio principal.

**Resposta correta:** B
**Explicação:** O capítulo demonstra que um agente genérico (ex: "você é um desenvolvedor full stack") tem conhecimento superficial em várias áreas — frontend ⭐⭐, backend ⭐⭐⭐, segurança ⭐, etc. O resultado é código que "funciona", mas cheio de dívida técnica. Agentes especializados, por outro lado, produzem resultados excelentes em cada domínio (⭐⭐⭐⭐⭐). As alternativas A, C e D não correspondem ao que o capítulo descreve sobre agentes genéricos.
**Nível:** Fácil

---

## Pergunta 2 (Fácil)

Quantos agentes especializados são apresentados na formação, distribuídos em quantas categorias?

- [ ] A) 10 agentes em 5 categorias
- [ ] B) 17 agentes em 7 categorias
- [ ] C) 20 agentes em 6 categorias
- [ ] D) 15 agentes em 8 categorias

**Resposta correta:** B
**Explicação:** O capítulo lista explicitamente 17 agentes organizados em 7 categorias: Produto (2 agentes), Design (2), Arquitetura (2), Desenvolvimento (3), Infraestrutura (2), Qualidade (2) e Governança (4 — Auditor, Documentation, Refactoring). As demais alternativas apresentam contagens que não correspondem aos dados do capítulo.
**Nível:** Fácil

---

## Pergunta 3 (Médio)

De acordo com a anatomia de um agente apresentada no capítulo, quais são os 5 componentes essenciais que todo agente deve ter?

- [ ] A) Nome, versão, autor, data e licença
- [ ] B) Identidade, conhecimento, processo, qualidade e comunicação
- [ ] C) README, workflow, checklist, prompts e testes
- [ ] D) Entrada, transformação, saída, validação e deploy

**Resposta correta:** B
**Explicação:** O diagrama da anatomia do agente mostra 5 componentes: **Identidade** (quem é, o que faz, o que NÃO faz), **Conhecimento** (stack, padrões, referências), **Processo** (fluxo de trabalho entrada → transformação → saída), **Qualidade** (checklist, critérios de aceite, anti-padrões) e **Comunicação** (formato de entrada/saída, como reportar problemas). A alternativa C descreve a estrutura de arquivos (README, workflow, checklist, prompts), que é diferente dos componentes conceituais. A alternativa D descreve um pipeline, não os componentes de um agente.
**Nível:** Médio

---

## Pergunta 4 (Médio)

No pipeline de desenvolvimento de features apresentado no capítulo, qual é a sequência CORRETA de agentes desde a concepção até a entrega?

- [ ] A) Backend Expert → Frontend Expert → QA Expert → DevOps Expert
- [ ] B) Product Discovery → UX Designer → UI Designer → Backend Expert → Frontend Expert → Security Expert → QA Expert → DevOps Expert → Auditor → Documentation
- [ ] C) Enterprise Architect → Database Architect → Backend Expert → DevOps Expert → Auditor
- [ ] D) UI Designer → Product Discovery → Backend Expert → QA Expert → DevOps Expert

**Resposta correta:** B
**Explicação:** O pipeline de features segue uma progressão lógica: começa com **Product Discovery** (problema → requisitos), passa por **UX/UI Designer** (experiência e interface), **Enterprise Architect** (arquitetura), **Backend/Frontend/Security/Prisma Experts** (implementação), **QA Expert** (testes), **DevOps Expert** (deploy), **Auditor** (score final) e **Documentation** (documentação). A alternativa A pula as etapas de descoberta e design. C pula design frontend e QA. D coloca UI Designer antes de Product Discovery, o que é invertido.
**Nível:** Médio

---

## Pergunta 5 (Difícil)

Um desenvolvedor cria um agente chamado "FullStack Expert" com as seguintes responsabilidades: implementar componentes React (frontend), criar APIs REST (backend), configurar segurança (OWASP, JWT), modelar banco de dados (Prisma), gerenciar infraestrutura (Docker, CI/CD) e realizar testes (Playwright). Com base nas boas práticas do capítulo, qual é o principal problema desse agente?

- [ ] A) O agente tem conhecimento insuficiente porque um único prompt não cabe tanta informação.
- [ ] B) O agente mistura múltiplos domínios em uma única entidade, o que resulta em conhecimento superficial em cada área e viola o princípio de especialização.
- [ ] C) O agente não tem permissão para executar comandos bash no OpenCode.
- [ ] D) O agente precisa de um checklist de qualidade, mas isso não é obrigatório.

**Resposta correta:** B
**Explicação:** O capítulo é enfático na seção "Não faça": **"Não misture domínios — Um agente de backend não deve ter responsabilidades de frontend"** e **"Não ignore limites — Se o agente não tem conhecimento, ele vai alucinar"**. Um agente que acumula frontend, backend, segurança, banco, infraestrutura e testes repete o problema do agente genérico: conhecimento superficial em todas as áreas (⭐ em cada uma), produzindo resultados medianos. A especialização é o princípio central do capítulo. A alternativa A não procede — prompts podem ser longos. C é uma limitação técnica que não invalida o conceito. D é verdadeiro (checklist é importante), mas não é o problema principal.
**Nível:** Difícil

---

---

## Pergunta 6 (Médio)

No pipeline de desenvolvimento com agentes especializados, os agentes são organizados em categorias. Em qual categoria está o agente "Auditor" e qual é sua função principal?

- [ ] A) Categoria Desenvolvimento — escrever testes automatizados para validar o código.
- [ ] B) Categoria Qualidade — revisar a experiência do usuário final.
- [ ] C) Categoria Governança — atribuir um score de qualidade para o projeto como um todo e verificar consistência entre módulos.
- [ ] D) Categoria Infraestrutura — auditar logs de servidor em produção.

**Resposta correta:** C
**Explicação:** O capítulo coloca o Auditor na categoria **Governança** (que inclui também Documentation e Refactoring). A função do Auditor é "atribuir um score de qualidade e consistência para o projeto", verificando se todos os padrões foram seguidos, se não há inconsistências entre módulos e se a documentação está alinhada com o código. A alternativa A confunde com QA Expert. B é função de UX Research/Designer. D não corresponde ao papel descrito.
**Nível:** Médio

---

## Pergunta 7 (Médio)

Um desenvolvedor precisa criar um novo endpoint de API que lida com dados financeiros. Ele decide usar apenas o Backend Expert. Qual(is) outro(s) agente(s) deveriam obrigatoriamente participar, segundo as boas práticas do capítulo?

- [ ] A) Nenhum — Backend Expert é suficiente para criar endpoints.
- [ ] B) Apenas Security Expert, para revisar autenticação e autorização.
- [ ] C) Security Expert (revisão de segurança), Prisma Expert (modelagem do schema), QA Expert (testes do endpoint) e DevOps Expert (deploy com variáveis de ambiente seguras).
- [ ] D) Apenas QA Expert e DevOps Expert.

**Resposta correta:** C
**Explicação:** O capítulo enfatiza que agentes especializados devem colaborar em pipeline — mesmo para um único endpoint, múltiplos agentes são necessários: **Security Expert** para garantir que dados financeiros estejam protegidos (OWASP, criptografia, rate limiting), **Prisma Expert** para modelar o schema com constraints e validações adequadas, **QA Expert** para testar cenários críticos (valores negativos, concorrência, saldo insuficiente) e **DevOps Expert** para configurar variáveis de ambiente seguras (nunca hardcoded). A alternativa A ignora todo o ecossistema. B esquece modelagem, testes e infraestrutura. D esquece segurança e modelagem.
**Nível:** Médio

---

## Gabarito

| Pergunta | Resposta | Nível |
|----------|----------|-------|
| 1 | B | Fácil |
| 2 | B | Fácil |
| 3 | B | Médio |
| 4 | B | Médio |
| 5 | B | Difícil |
| 6 | C | Médio |
| 7 | C | Médio |
