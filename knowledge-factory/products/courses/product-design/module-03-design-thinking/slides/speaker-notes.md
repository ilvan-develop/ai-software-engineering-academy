## Introducao

# Módulo 03 — Design Thinking: Inovação Centrada no Usuário
**Uma abordagem human-centered para resolver problemas complexos.**
---

---
## 1. O que é Design Thinking

Design Thinking é uma abordagem **centrada no ser humano** para solução de problemas que combina empatia, criatividade e racionalidade. Diferente de métodos tradicionais que partem de uma solução técnica, o Design Thinking começa com o **usuário** e suas necessidades reais.
### Origem
| Ano | Marco |
|-----|-------|
| 1969 | Herbert Simon publica "The Sciences of the Artificial" — primeiras bases |
| 1987 | Peter Rowe usa o termo "Design Thinking" em livro de arquitetura |
| 1991 | David Kelley funda a IDEO, que populariza o método |
| 2005 | D.School de Stanford sistematiza o processo em 5 fases |

---
## 2. As 5 Fases do Design Thinking

O processo é dividido em 5 fases **não-lineares** — você pode (e deve) voltar a fases anteriores conforme aprende.
┌─────────────┐
│   EMPATIZAR  │
└──────┬──────┘
↓
┌─────────────┐
│   DEFINIR   │
└──────┬──────┘

---
## 3. Fase 1: Empatizar

### Por que empatizar?
Sem empatia, você constrói soluções baseadas em **suposições**. Com empatia, você constrói baseado em **fatos** sobre o que o usuário realmente vive.
### Técnicas de empatia
#### 3.1 Entrevistas com usuários
# Roteiro de entrevista — Exemplo

---
## Abertura (5 min)

- "Conte um pouco sobre seu trabalho/dia a dia"
- "Como você lida com [tópico] atualmente?"

---
## Exploração (15 min)

- "Me conte a última vez que você precisei fazer [ação]"
- "O que foi mais frustrante nesse processo?"
- "O que você fez para contornar?"

---
## Aprofundamento (10 min)

- "Por que isso é importante para você?"
- "O que aconteceria se você não conseguisse fazer isso?"
- "Como você descreveria a solução ideal?"

---
## Fechamento (5 min)

- "Mais alguma coisa que gostaria de compartilhar?"
- "Posso voltar a falar com você se surgir mais dúvidas?"
**Regras de ouro para entrevistas:**
✅ Faça:
• Perguntas abertas ("Me conte sobre...")
• Escute mais do que fala (proporção 80/20)
• Pergunte "por quê?" repetidamente (técnica dos 5 porquês)
• Observe linguagem corporal e tom de voz

---
## 4. Fase 2: Definir

### Do problema amplo ao ponto de vista
Na fase de Definir, você sintetiza tudo que aprendeu na empatia para criar um **ponto de vista** (POV) claro.
### Problem Statement
Uma boa declaração de problema segue esta estrutura:
[USUÁRIO] precisa de [NECESSIDADE] porque [INSIGHT]
**Exemplos:**
❌ Ruim: "O sistema de relatórios é lento"
(focado na solução, não no usuário)

---
## 5. Fase 3: Ideiar

### Princípios do brainstorming
REGRAS DO BRAINSTORMING:
1. ⭐ Quantidade gera qualidade — quanto mais ideias, melhor
2. 🚫 Não critique — julgamento só depois
3. 🚀 Construa sobre ideias alheias ("Sim, e...")
4. 🌊 Busque ideias selvagens — as mais loucas viram as melhores
5. 🎯 Seja visual — desenhe, rabisque, use post-its
6. ⏱ Tempo curto — 15-30 minutos no máximo

---
## 6. Fase 4: Prototipar

### Por que prototipar?
> "Um protótipo vale mais que mil reuniões."
Prototipar transforma ideias abstratas em algo **tangível** que pode ser testado, discutido e melhorado.
### Níveis de fidelidade
BAIXA FIDELIDADE                        ALTA FIDELIDADE
├─────────────────────────────────────────────────────┤
Papel → Wireframe → Mockup → Protótipo clicável → MVP
#### Protótipos de baixa fidelidade

---
## 7. Fase 5: Testar

### O ciclo de teste
┌─────────────────────────────────────────────────────────┐
│                                                          │
│   PROTÓTIPO → TESTAR → APRENDER → ITERAR → PROTÓTIPO    │
│                                                          │
│                    (e recomeça)                           │
└─────────────────────────────────────────────────────────┘
### Tipos de teste

---
## Setup

1. Defina as tarefas que o usuário deve executar
2. Prepare o protótipo (papel, figma, código)
3. Configure gravação (tela + áudio + câmera)
4. Prepare o roteiro de moderação

---
## Roteiro (20-30 min)

1. Aquecimento (3 min):
- "Conte um pouco sobre você"
- "O que você entende que esse sistema faz?"
2. Tarefas (15 min):
- "Você quer comprar um presente para sua mãe. Como faria?"
- "Você percebeu que o endereço está errado. Como corrige?"
- "Quanto custou seu último pedido?"
3. Exploração livre (5 min):

---
## O que observar

✓ O usuário conseguiu completar a tarefa?
✓ Quanto tempo levou?
✓ Onde ele hesitou?
✓ Onde ele errou?
✓ O que ele verbalizou? (pensar em voz alta)
✓ Expressões faciais e linguagem corporal

---
## Erro comum: explicar o protótipo

❌ Moderador: "Aqui você clica nesse botão e abre um modal..."
✅ Moderador: "O que você faria agora?"
### Feedback Loop
COLETA                  SÍNTESE                  AÇÃO
─────────────────────────────────────────────────────────
Gravações              Agrupar padrões          Definir o que
Anotações              Priorizar problemas      mudar no protótipo
Métricas (tempo,       Identificar              Iterar e testar

---
## Relatório de teste — Sprint 3

| # | Problema | Gravidade | Frequência | Solução proposta |
|---|----------|-----------|------------|------------------|
| 1 | Usuário não encontra o botão "Finalizar" | Alta | 4/5 | Mover para o topo da página |
| 2 | Confunde "Salvar" com "Enviar" | Média | 3/5 | Renomear botões |
| 3 | Campos de data aceitam formato errado | Baixa | 5/5 | Adicionar máscara e validação |
---

---
## 8. Design Thinking + Ágil

### Integração com Scrum e Kanban
Design Thinking e Métodos Ágeis são **complementares**, não concorrentes.
DESIGN THINKING                         SCRUM
───────────────────────────            ───────────────────────────
Emponder (descobrir)       ───────→    Sprint 0 / Discovery Sprint
Definir (problema)         ───────→    Product Backlog (PBI bem definidos)
Ideiar (soluções)          ───────→    Sprint Planning (discutir abordagens)
Prototipar (testar)        ───────→    Sprint (desenvolvimento)

---
## 9. Design Thinking em Enterprise

### Desafios de escala
Em empresas de grande porte, Design Thinking enfrenta desafios específicos:
| Desafio | Impacto | Como mitigar |
|---------|---------|--------------|
| **Stakeholders demais** | Decisões lentas, conflitos de interesse | Mapear influenciadores, sessões de alinhamento |
| **Processos engessados** | Dificuldade de iterar rápido | Criar espaços protegidos (innovation lab) |
| **Usuários internos complexos** | Múltiplos perfis com necessidades conflitantes | Segmentar personas, design por jornada |
| **Regulamentação** | Restrições legais para testes | Envolver compliance desde o início |

---
## 10. Anti-padrões em Design Thinking

❌ Pular a fase de empatia
"Já conhecemos nossos usuários" — Não, você não conhece.
Consequência: Solução para o problema errado.
❌ Brainstorming sem regras
Sem moderação, líderes dominam e ideias tímidas morrem.
Consequência: Mesmas soluções de sempre.
❌ Protótipo fotorrealista antes da hora
Gastar dias no Figma antes de validar a ideia com papel.

---
## Resumo

1. **Design Thinking** é uma abordagem human-centered para resolver problemas complexos
2. **5 fases não-lineares:** Empatizar → Definir → Ideiar → Prototipar → Testar
3. **Empatia** é a base — entrevistas, observação e imersão revelam necessidades reais
4. **Definir** sintetiza aprendizados em problem statement e perguntas HMW
5. **Ideiar** prioriza quantidade com brainstorming, Crazy 8 e matriz impacto x esforço
6. **Prototipar** vai do papel ao código, do rápido ao refinado
7. **Testar** valida com usuários reais e alimenta o ciclo de iteração
8. **Design Thinking + Ágil** funciona com Discovery Sprints e Kanban com discovery track

---
