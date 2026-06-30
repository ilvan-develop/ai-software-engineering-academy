# Content — Staging / Workspace

Area de desenvolvimento onde os agentes criam e iteram sobre o conteudo.

## Fluxo

```
raw/           -> Material bruto de entrada (artigos, transcricoes, docs)
modules/       -> Aula processada + review (versao em desenvolvimento)
slides/        -> Slides gerados
exercises/     -> Exercicios gerados
quizzes/       -> Quizzes gerados
marketing/     -> Posts e artigos para redes sociais
```

## Promocao para Producao

Quando o conteudo atinge qualidade suficiente:

1. Mover aula finalizada para `curriculum/cursos/<curso>/<modulo>/aula/aula.md`
2. Atualizar `curriculum/status.yaml` com status "publicado"
3. Executar `python scripts/pipeline_manager.py processar-modulo --curso=<curso> --modulo=<modulo>`

## Notas

- `content/` e o "dev environment" — aqui os agentes trabalham
- `curriculum/cursos/` e a "producao" — fonte canonica para livros e demais outputs
- Nao misture: tudo em `content/` pode ser reescrito; tudo em `curriculum/cursos/` e versao final
