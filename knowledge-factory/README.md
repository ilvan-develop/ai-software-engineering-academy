# Knowledge Factory

Output gerado pelos agentes de produção.

## Estrutura

```
knowledge-factory/
├── livros/                       ← Cross-course: livros completos
│   └── <book-id>/
│       ├── compiled/             ← Markdown agregado por capítulo
│       └── output/               ← Formatos finais (docx, epub, pdf)
│
├── cursos/                       ← Per-course: outputs por módulo
│   └── <curso>/
│       └── <modulo>/
│           ├── slides/           ← Slides gerados (.pdf, .pptx)
│           ├── videos/           ← Vídeos e roteiros gerados
│           ├── exercicios/       ← Exercícios gerados (.pdf)
│           ├── quiz/             ← Quizzes gerados (.pdf)
│           └── projeto/          ← Projetos gerados
│
├── certificacao/                 ← Provas, rubricas, certificados
├── curso-online/                 ← Conteúdo formatado para LMS
├── newsletter/                   ← Newsletters compiladas
└── social-media/                 ← Posts e artigos para redes sociais
```

## Como gerar

```bash
# Livro completo
python scripts/book_publisher.py \
  --manifest=curriculum/books/<manifest>.yaml \
  --formats=docx,epub,pdf-digital

# Slides de um módulo (em breve)
python scripts/build_slides.py \
  --course=<curso> --module=<modulo>
```
