# Exercícios — Módulo 03

## Exercício 1: Mapa de Empatia

Você é o tech lead de um time que vai construir um novo **sistema de onboarding para desenvolvedores juniores** que entram na empresa.

Conduza uma sessão de empatia fictícia e preencha o mapa de empatia para o persona **"Carlos, dev junior de 24 anos, primeiro emprego em tech"** :

```text
┌──────────────────────────────────────────────────────┐
│                   MAPA DE EMPATIA                     │
├──────────────┬───────────────────────────────────────┤
│              │                                       │
│  O QUE ELE   │    O QUE ELE FAZ?                     │
│  FALA?       │    (comportamentos observáveis)        │
│              │                                       │
├──────────────┼───────────────────────────────────────┤
│              │                                       │
│  O QUE ELE   │    O QUE ELE PENSA E SENTE?           │
│  OUVE?       │    (medos, desejos, frustrações)       │
│              │                                       │
├──────────────┴───────────────────────────────────────┤
│                                                       │
│  DORES (Frustrações)     GANHOS (Desejos)             │
│                                                       │
└───────────────────────────────────────────────────────┘
```markdown

**Entregue:** O mapa preenchido com pelo menos 3 itens por quadrante.

---

## Exercício 2: Problem Statement + HMW

Com base no mapa de empatia do Exercício 1, crie:

1. **Um Problem Statement** seguindo a estrutura `[USUÁRIO] precisa de [NECESSIDADE] porque [INSIGHT]`
2. **8 perguntas HMW** (How Might We) em direções diferentes

Avalie cada HMW usando a matriz de priorização:

```text
               ALTO IMPACTO
                    │
    ┌───────────────┼───────────────┐
    │               │               │
    │  FAÇA AGORA   │   BIG BETS    │
    │               │               │
    ├───────────────┼───────────────┤
    │               │               │
    │  FILL-INS     │    EVITE      │
    │               │               │
    └───────────────┼───────────────┘
                    │
               BAIXO IMPACTO
     BAIXO ESFORÇO ──────── ALTO ESFORÇO
```markdown

**Entregue:** Problem statement + 8 HMWs + matriz priorizada com os HMWs posicionados.

---

## Exercício 3: Crazy 8 + Protótipo de papel

Você vai redesenhar o **fluxo de solicitação de férias** de um sistema corporativo.

**Cenário atual:** O funcionário precisa:
1. Abrir chamado no service desk
2. Preencher formulário em PDF
3. Enviar para o RH por email
4. RH abre planilha manual
5. Gestor aprova em outro sistema
6. Resultado volta por email em 3-5 dias úteis

**Parte 1 — Crazy 8 (individual):**
- Dobre uma folha A4 em 8 partes
- Em 8 minutos, esboce 8 ideias diferentes para um novo fluxo digital
- Foque em rapidez, transparência e automação

**Parte 2 — Protótipo de baixa fidelidade (em dupla):**
- Escolha a melhor ideia do Crazy 8
- Desenhe em papel as 3-5 telas principais do fluxo
- Inclua: tela inicial, formulário, confirmação, status
- Mostre estados: loading, sucesso, erro

**Entregue:** Fotos do Crazy 8 + fotos do protótipo de papel + descrição da ideia escolhida.

---

## Exercício 4: Teste de usabilidade

Com o protótipo do Exercício 3, conduza um teste de usabilidade com um colega.

**Roteiro:**

```markdown
## Tarefas para o participante

1. "Você quer solicitar 5 dias de férias para janeiro. Como faria?"
2. "Você percebeu que colocou as datas erradas. Como corrige?"
3. "Onde você vê o status da sua solicitação?"
4. "Você quer cancelar a solicitação. Como faz?"

## Observações

| Tarefa | Completou? | Tempo | Hesitações | Erros | Observações |
|--------|------------|-------|------------|-------|-------------|
| 1      |            |       |            |       |             |
| 2      |            |       |            |       |             |
| 3      |            |       |            |       |             |
| 4      |            |       |            |       |             |
```text

**Entregue:** Relatório de teste com:
- Tabela de observações preenchida
- 3 problemas identificados com gravidade (alta/média/baixa)
- 3 sugestões de melhoria
- Uma iteração do protótipo (foto do protótipo ajustado)

---

## Exercício 5: Discovery Sprint para uma feature real

Sua squad vai implementar um **sistema de feedback contínuo** (substituindo a avaliação anual).

Planeje uma Discovery Sprint de 2 semanas seguindo o Design Thinking. Preencha:

```markdown
## Discovery Sprint — Feedback Contínuo

### Semana 1 — Empatizar + Definir

| Dia | Atividade | Participantes | Duração | Entregável |
|-----|-----------|---------------|---------|------------|
| Seg |           |               |         |            |
| Ter |           |               |         |            |
| Qua |           |               |         |            |
| Qui |           |               |         |            |
| Sex |           |               |         |            |

### Semana 2 — Ideiar + Prototipar + Testar

| Dia | Atividade | Participantes | Duração | Entregável |
|-----|-----------|---------------|---------|------------|
| Seg |           |               |         |            |
| Ter |           |               |         |            |
| Qua |           |               |         |            |
| Qui |           |               |         |            |
| Sex |           |               |         |            |
```text

**Entregue:** O cronograma completo com:
- Mínimo de 5 técnicas diferentes de DT
- Participantes diversos (cite cargos)
- Duração realista de cada atividade
- Entregáveis específicos

**Bônus:** Escreva 3 Hills (metas IBM Enterprise Design Thinking) que descrevam a mudança de comportamento esperada.
