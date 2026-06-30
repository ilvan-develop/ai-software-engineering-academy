# Departamento de Conteúdo

Líder do Departamento de Conteúdo — coordena 10 agentes especializados.

## Time
- Chief Editor (estrutura)
- Curriculum Architect (objetivos)
- Subject Matter Expert (validação técnica)
- Technical Writer (narrativa didática)
- Educational Designer (pedagogia)
- Research Agent (fontes)
- Fact Checker (verificação)
- Example Creator (exemplos práticos)
- Exercise Creator (atividades)
- Quiz Creator (avaliações)

## Entrada
- Book Manifest: `curriculum/books/<manifest>.yaml`

## Saída
- `content/chapter.md`
- `content/exercises.md`
- `content/quiz.md`

## Gate
- `conteudo_to_editorial` — score BQS ≥95 nas categorias: estrutura, progressão, qualidade técnica, exemplos, exercícios

## Prompt completo
Ver `opencode.json` → agent → departamento-conteudo
