# Agentes — O Erro de 90% ao Usar IA para Programar

## Agentes responsaveis

| Agente | Input | Output |
|--------|-------|--------|
| content-writer | `aula/aula.md` | `aula/aula.md` (reescreve) |
| slide-designer | `aula/aula.md`, `slides/slides.md` | `knowledge-factory/.../slides/` |
| video-scriptwriter | `aula/aula.md` | `knowledge-factory/.../videos/` |
| exercise-designer | `exercicios/exercicios.md` | `knowledge-factory/.../exercicios/` |
| quiz-creator | `quiz/quiz.md` | `knowledge-factory/.../quiz/` |
| project-engine | `projeto/projeto.md` | `knowledge-factory/.../projeto/` |

## Prompts por agente

### content-writer
Reescrever `aula.md` com tom tecnico e didatico. Manter exemplos reais com TypeScript. Incluir diagramas ASCII quando relevante. Tema: armadilhas comuns no uso de IA para programacao, por que 90% dos devs erram, e como usar IA corretamente.

### slide-designer
Maximo 15 slides. Priorizar: contraste entre "codigo gerado por IA" vs "codigo revisado por humano", demonstracoes de prompt engineering, comparacoes antes/depois.

### video-scriptwriter
Formato de roteiro com cenas. Duracao estimada: 15-20 min. Linguagem falada. Sugestoes de elementos visuais: comparacao de codigo, graficos de produtividade, demonstracoes ao vivo.

### exercise-designer
3-5 exercicios: (1) identificar erros em codigo gerado por IA, (2) escrever prompts eficazes, (3) revisar codigo gerado, (4) [dificil] criar pipeline de revisao automatizada. Incluir template de resposta.

### quiz-creator
10 perguntas de multipla escolha. Topics: limitacoes da IA, quando confiar/noa confiar, melhores praticas de prompting, revisao de codigo gerado.

### project-engine
Mini-projeto: criar uma ferramenta de code review assistida por IA. Enunciado, rubrica de avaliacao, entregaveis.
