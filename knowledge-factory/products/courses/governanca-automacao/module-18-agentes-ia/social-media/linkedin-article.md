# Módulo 18 - Agentes de IA: Criação de Agentes Especializados

---

## 1. Por que agentes especializados?

Um único agente genérico (ex: "você é um desenvolvedor full stack") produz resultados **medianos em todas as áreas**.
Um ecossistema de agentes especializados produz **resultados excelentes em cada área**.
### O problema do agente genérico
Agente Genérico:

## 2. Anatomia de um agente

Cada agente da nossa biblioteca segue a mesma estrutura:
agente/
├── README.md           # Identidade: objetivo, responsabilidades, stack
├── workflow.md         # Processo: fluxo de trabalho passo a passo

## 3. Os 17 agentes da formação

### Agentes de Produto
| Agente | Função | Stack/Conhecimento |
|--------|--------|-------------------|
| **Product Discovery** | Transformar problemas em requisitos | User Stories, RICE, MoSCoW, BDD |

## 4. Como criar um novo agente

### Passo a passo
1. Definir o DOMÍNIO do agente
→ Qual área ele cobre? (ex: "segurança de aplicações web")
2. Definir o CONHECIMENTO BASE

## 5. Como combinar agentes em pipeline

O verdadeiro poder está em **compor** agentes em sequência.
### Pipeline de features
Product Discovery  ──→  UX Designer  ──→  UI Designer
│                       │                  │

## 6. Integração com OpenCode

### Configuração de agentes no opencode.json
{
"agents": {
"frontend-expert": {

---
*Este artigo faz parte da formacao Arquitetura de Software Enterprise com IA*