# O erro que 90% das pessoas cometem usando IA para programar

---

## Pré-requisitos

- Experiência básica com programação em qualquer linguagem
- Familiaridade com uso de assistentes de IA (GitHub Copilot, Claude Code, ChatGPT, etc.)
- Noções fundamentais de Git e versionamento

## Objetivos de aprendizagem

Ao final desta aula, o aluno será capaz de:
1. **Identificar** os 5 erros mais comuns ao usar IA para programar
2. **Diferenciar** uso produtivo de uso prejudicial de assistentes de IA
3. **Aplicar** técnicas de prompt estruturado para obter respostas precisas

## Competências desenvolvidas

**Hard skills:**
- Prompt engineering aplicado à programação
- Code review de código gerado por IA
- Configuração de assistentes de IA no projeto

## 1. Introdução: por que 90% cometem esse erro

Era uma terça-feira comum. O desenvolvedor precisava de uma função simples para validar emails. Pediu ao ChatGPT, copiou o código, fez deploy. Na sexta, o banco de dados estava cheio de registros com emails como "usuario@". Aquela função — que parecia perfeita — só verificava se existia um "@" na string.
A IA acertou a sintaxe. Errou a lógica. O desenvolvedor não revisou. Produção quebrou.
Esse cenário se repete milhares de vezes todos os dias. Assistentes de IA geram código em segundos — mas essa velocidade tem um custo oculto. Pesquisas da indústria revelam um padrão preocupante:
| Dado | Fonte |

## 2. Erro 1: Confiar cegamente na saída da IA

### Definição
Aceitar o código gerado pela IA como correto sem qualquer questionamento, validação ou revisão.
### Por que acontece
A IA gera respostas com **alta fluência e aparência de confiança**. O código parece correto, compila e muitas vezes até passa em testes simples — mas pode conter bugs sutis de lógica, segurança ou performance.

## 3. Erro 2: Prompts vagos sem contexto

### Definição
Fazer pedidos genéricos e esperar respostas precisas e úteis.
### Por que acontece
A IA opera com base em probabilidades: quanto menos contexto, mais genérica a resposta. É como perguntar "Me recomenda um filme?" para um amigo — você vai receber uma lista genérica. Agora pergunte "Me recomenda um filme de suspense coreano com menos de 2 horas" — a resposta muda completamente.

---
*Este artigo faz parte da formacao Arquitetura de Software Enterprise com IA*