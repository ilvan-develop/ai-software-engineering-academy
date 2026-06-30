# Knowledge Factory

**Materia-prima -> Multiplos produtos.** Transforma o conhecimento dos cursos em diversos formatos e canais.

## Estrutura atual

A partir da reorganizacao para escala, os outputs agora seguem duas estrategias:

### 1. Outputs por curso (per-course)

Slides, videos, exercicios, quizzes e projetos sao gerados **por modulo** e organizados na hierarquia de cursos:

```
knowledge-factory/products/courses/<curso>/<modulo>/
```

### 2. Outputs cross-course

Livros, certificacoes, newsletters e social-media agregam **multiplos cursos**:

```
knowledge-factory/products/books/<book-id>/
knowledge-factory/certificacao/
knowledge-factory/newsletter/
knowledge-factory/products/online-courses/
knowledge-factory/products/social/
```

## Produtos

| Diretorio | Produto | Tipo |
|-----------|---------|------|
| `cursos/` | Slides, videos, exercicios, quiz, projeto | Per-course |
| `livros/` | Livros completos (DOCX, EPUB, PDF) | Cross-course |
| `certificacao/` | Provas e rubricas | Cross-course |
| `newsletter/` | Newsletters | Cross-course |
| `curso-online/` | Conteudo formatado para LMS | Cross-course |
| `social-media/` | Posts e marketing | Cross-course |

## Fluxo

```
curriculum/sources/<curso>/<modulo>/aula/aula.md     ← fonte
        │
        ├── knowledge-factory/products/courses/<curso>/<modulo>/slides/     ← slides
        ├── knowledge-factory/products/courses/<curso>/<modulo>/videos/     ← videos
        └── curriculum/books/<manifest>.yaml                       ← manifest
                │
                └── knowledge-factory/products/books/<book-id>/output/     ← livro completo
```
