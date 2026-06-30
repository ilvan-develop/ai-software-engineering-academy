# AI Software Engineering Academy — Agentes

Este workspace e responsavel por transformar conhecimento tecnico em multiplos produtos educacionais.

## Estrutura de diretorios

```
curriculum/
├── sources/                         ← FONTE: conteudo canonicos dos cursos
│   └── <curso>/
│       └── <modulo>/
│           ├── aula/aula.md         ← conteudo da aula
│           ├── slides/slides.md     ← fonte dos slides
│           ├── exercicios/          ← fonte dos exercicios
│           ├── quiz/                ← fonte do quiz
│           ├── projeto/             ← fonte do projeto
│           └── agentes/             ← prompts de IA
│
├── books/                           ← Manifests de livros
│   └── <manifest>.yaml
│
├── bqs/                             ← Quality gates (BQS)
│
├── biblioteca-agentes/              ← Biblioteca de agentes de IA
│   └── <agent>/
│       ├── prompts/
│       ├── workflow.md
│       └── checklist.md
│
├── metodologia/                     ← Metodologia educacional
│
└── status.yaml                      ← Estado de modulos e livros

config/                              ← CONFIGURACAO DA FABRICA
├── editora/                         ← Brand book, tokens, departamentos, teams
├── templates/                       ← Templates de conteudo
│   └── prompts/                     ← Prompts para agentes

schemas/                             ← Validacao de schema
├── book-manifest.schema.json
└── catalog.schema.json

archive/                             ← Conteudo legado
└── legacy-content/

knowledge-factory/                   ← OUTPUT: conteudo gerado
├── MANIFEST.yaml                    ← Metadado raiz (versao, schema, ultimo build)
│
├── registry/                        ← Catalogo e taxonomia
│   ├── catalog.yaml                 ← TODO item registrado com metadados
│   ├── taxonomy.yaml                ← Tags, niveis, audiencias, topicos
│   └── graph.yaml                   ← Relacoes entre itens (modulo → livro)
│
├── pipeline/                        ← Orquestracao e auditoria
│   ├── runs/                        ← Logs de execucao (data, engine, resultado)
│   ├── reports/                     ← Pipeline reports e auditorias
│   └── gates/                       ← Quality gates (BQS)
│
├── products/                        ← OUTPUTS por formato
│   ├── books/{book-id}/             ← Livros (compiled/ + output/ + kdp/)
│   │   ├── compiled/                ← Markdown agregado
│   │   └── output/                  ← .docx, .epub, .pdf
│   ├── courses/{curso}/{modulo}/    ← Conteudo por modulo
│   │   ├── slides/                  ← slides gerados (.pdf, .pptx)
│   │   ├── videos/                  ← videos e roteiros gerados
│   │   ├── exercicios/              ← exercicios gerados (.pdf)
│   │   ├── quiz/                    ← quizzes gerados (.pdf)
│   │   ├── projeto/                 ← projetos gerados
│   │   └── workshop/                ← workshops do modulo
│   ├── social/{campaign}/           ← Redes sociais por campanha
│   ├── newsletters/{issue-id}/      ← Newsletters por edicao
│   ├── certificates/{cert-id}/      ← Certificacoes
│   └── online-courses/{course-id}/  ← LMS-ready (Udemy, Hotmart)
│
└── assets/                          ← Ativos compartilhados
    ├── diagrams/                    ← SVGs, diagramas
    ├── covers/                      ← Capas de livros
    └── templates/                   ← Templates DOCX, EPUB, tipografia
```

## Agentes de Producao

### content-writer
Gera documentacao, aulas, livros e artigos detalhados a partir do conteudo bruto dos modulos.

- **Input**: `curriculum/sources/<curso>/<modulo>/aula/aula.md`
- **Output**: `curriculum/sources/<curso>/<modulo>/aula/aula.md` (reescreve)
- **Instrucao**: Mantem tom tecnico e didatico. Usa exemplos reais com TypeScript. Inclui diagramas em ASCII quando relevante.

### slide-designer
Transforma aulas em apresentacoes para diferentes contextos.

- **Input**: `curriculum/sources/<curso>/<modulo>/slides/slides.md` ou `aula/aula.md`
- **Output**: `knowledge-factory/products/courses/<curso>/<modulo>/slides/`
- **Instrucao**: Maximo 15 slides por apresentacao. Prioriza imagens mentais, diagramas e codigo sobre texto corrido.

### video-scriptwriter
Cria roteiros completos para videoaulas, incluindo storyboard, cenas, narracao e elementos visuais.

- **Input**: `curriculum/sources/<curso>/<modulo>/aula/aula.md`
- **Output**: `knowledge-factory/products/courses/<curso>/<modulo>/videos/`
- **Instrucao**: Formato de roteiro dividido em cenas. Inclui tempo estimado por cena. Narracao em linguagem falada (nao escrita). Adiciona sugestoes de elementos visuais na tela.

### exercise-designer
Cria atividades praticas e exercicios complementares.

- **Input**: `curriculum/sources/<curso>/<modulo>/exercicios/exercicios.md`
- **Output**: `knowledge-factory/products/courses/<curso>/<modulo>/exercicios/`
- **Instrucao**: 3-5 exercicios por modulo. Progressao de dificuldade (facil -> medio -> dificil). Inclui template de resposta e criterios de correcao.

### checklist-creator
Extrai checklists objetivos e acionaveis do conteudo tecnico.

- **Input**: `curriculum/sources/<curso>/<modulo>/aula/aula.md`
- **Output**: `knowledge-factory/products/courses/<curso>/<modulo>/` (checklist.md)
- **Instrucao**: Checklist em formato de tarefas (checkboxes). Maximo 20 itens. Foco em acao -- "Fiz X" nao "Entender X".

### social-media-strategist
Cria conteudo para todas as redes sociais e prompts para geracao de assets visuais.

- **Input**: `curriculum/sources/<curso>/<modulo>/aula/aula.md`
- **Output**: `knowledge-factory/products/social/`
- **Instrucao**: Adapta o tom para cada rede (LinkedIn: profissional, Instagram: visual/didatico, YouTube: narrativo, Twitter/X: conciso). Gera prompts DALL-E/Midjourney para capas e artes. Gera prompts para edicao de videos curtos (Reels, Shorts, TikTok).

### newsletter-editor
Compila e edita conteudo para newsletters semanais/tematicas.

- **Input**: Conteudo de multiplos modulos
- **Output**: `knowledge-factory/products/newsletters/`
- **Instrucao**: Estrutura: assunto + introducao + 3 secoes de conteudo + CTA. Tom editorial, nao academico. Extensao maxima: 5 minutos de leitura.

### workshop-facilitator
Cria material completo para workshops presenciais ou online.

- **Input**: `curriculum/sources/<curso>/` (modulos inteiros)
- **Output**: `knowledge-factory/products/courses/<curso>/<modulo>/workshop/`
- **Instrucao**: Inclui agenda, objetivos, dinamicas, exercicios em grupo, slides do facilitador, material do participante. Duracao: 4h ou 8h.

### lms-structurer
Formata o conteudo para plataformas de curso online (Udemy, Hotmart, Teachable).

- **Input**: `curriculum/sources/<curso>/` (curso inteiro)
- **Output**: `knowledge-factory/products/online-courses/`
- **Instrucao**: Estrutura em secoes e aulas. Cada aula tem: titulo, descricao, recurso (video/texto), duracao estimada, material complementar. Inclui legenda e tags SEO.

### certification-designer
Cria provas, rubricase criterios de certificacao.

- **Input**: `curriculum/sources/` (multiplos cursos)
- **Output**: `knowledge-factory/products/certificates/`
- **Instrucao**: Prova objetiva (20 questoes) + prova pratica (1 projeto). Rubrica de avaliacao com pesos. Minimo 70% para aprovacao.

### consistency-auditor
Audita links, referencias, tom de voz e consistencia entre modulos.

- **Input**: `curriculum/sources/` (todos os modulos)
- **Output**: Relatorio de inconsistencias
- **Instrucao**: Verifica: links quebrados, referencias cruzadas corretas, tom de voz uniforme, nomenclatura consistente, profundidade equilibrada entre modulos.

### book-architect
Estrutura livros completos a partir de Book Manifests (YAML) que referenciam modulos dos cursos.

- **Input**: `curriculum/books/<manifest>.yaml` + `curriculum/sources/<curso>/<modulo>/aula/aula.md`
- **Output**: `knowledge-factory/products/books/<id>/compiled/` (Markdown agregado por capitulo + book.md completo)
- **Instrucao**: Le o Book Manifest, agrega modulos na ordem definida, gera prefacio, sumario, introducao, conclusao, glossario e apendices automaticamente. Garante progressao didatica entre capitulos. Gera prompt de capa para DALL-E/Midjourney.
- **Comando**: `python scripts/book_architect.py --manifest=curriculum/books/<manifest>.yaml`

### book-publisher
Converte o Markdown estruturado em formatos de livro comercial.

- **Input**: `knowledge-factory/products/books/<id>/compiled/book.md`
- **Output**: `knowledge-factory/products/books/<id>/output/livro.docx`, `livro.epub`, `livro-digital.pdf`, `livro-grafica.pdf`
- **Instrucao**: Gera DOCX formatado (fontes, sumario, cabecalho/rodape, capa), EPUB navegave, PDF digital (fpdf2) e PDF pronto para grafica (Pandoc + LaTeX). Formatos comerciais com sangria, marcas de corte e CMYK no PDF de impressao.
- **Comando**: `python scripts/book_publisher.py --manifest=curriculum/books/<manifest>.yaml --formats=docx,epub,pdf-digital,pdf-print`

## Fluxo de trabalho

1. Um modulo e concluido em `curriculum/sources/<curso>/<modulo>/aula/aula.md`
2. `content-writer` gera documentacao
3. Criar/editar Book Manifest em `curriculum/books/` definindo quais modulos viram capitulos
4. `book-architect` agrega os modulos no Markdown estruturado do livro
5. `slide-designer` e `video-scriptwriter` transformam em apresentacoes e roteiros
6. `social-media-strategist` e `newsletter-editor` distribuem o conteudo
7. `workshop-facilitator` e `lms-structurer` empacotam para entrega
8. `book-publisher` gera os formatos finais (DOCX, EPUB, PDF)
9. `consistency-auditor` valida a qualidade final
