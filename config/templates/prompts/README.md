# Diretório de Templates de Prompt

Este diretório contém templates de prompt reutilizáveis para os agentes de produção da **AI Software Engineering Academy**. Cada template padroniza a comunicação com assistentes de IA, garantindo consistência na geração de conteúdo educacional.

## Templates Disponíveis

| Arquivo | Agente | Finalidade |
|---------|--------|------------|
| `prompt-content-writer.md` | Content Writer | Geração de documentação, aulas, livros e artigos |
| `prompt-slide-designer.md` | Slide Designer | Criação de apresentações em slides |
| `prompt-video-scriptwriter.md` | Video Scriptwriter | Roteiros completos para videoaulas |
| `prompt-social-media.md` | Social Media Strategist | Conteúdo para redes sociais e prompts de assets visuais |
| `prompt-exercise-designer.md` | Exercise Designer | Atividades práticas e exercícios complementares |
| `prompt-auditor.md` | Consistency Auditor | Auditoria de links, referências, tom e consistência |
| `prompt-designer-visual.md` | Designer Visual | Layout de livros, capas, diagramas e especificação visual |
| `prompt-curador-conteudo.md` | Curador de Conteúdo | Curadoria, análise de lacunas, roadmaps de conteúdo |
| `prompt-revisor-linguagem.md` | Revisor de Linguagem | Revisão gramatical, ortográfica e de estilo |
| `prompt-ds-editorial.md` | Design System Editorial | Guia de identidade visual unificada e tokens de design |
| `prompt-criador-imagens.md` | Criador de Imagens | Prompts DALL-E/Midjourney para capas, diagramas e ilustrações |
| `prompt-tradutor.md` | Tradutor de Conteúdo | Tradução pt-BR ↔ en-US de módulos e livros |
| `prompt-indexador-seo.md` | Indexador SEO | Metadados, tags e descrições para Udemy, KDP, Google |
| `prompt-gestor-pipeline.md` | Gestor de Pipeline | Orquestração de agentes, status e relatórios |

## Como Usar

1. Escolha o template correspondente ao tipo de conteúdo que deseja gerar
2. Substitua os placeholders (variáveis entre `{{ }}`) pelos valores reais
3. Envie o prompt completo para o assistente de IA
4. Revise o output gerado antes de publicar

## Convenção de Variáveis

Todas as variáveis seguem o padrão `{{NOME_DA_VARIAVEL}}` em MAIÚSCULAS com underscores.

### Variáveis Compartilhadas

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `{{CURSO_NAME}}` | Nome do curso | `nextjs-fundamentos` |
| `{{MODULO_PATH}}` | Caminho relativo do módulo | `cursos/nextjs-fundamentos/01-introducao` |
| `{{OUTPUT_DIR}}` | Diretório de saída do conteúdo gerado | `knowledge-factory/documentacao` |
| `{{AULA_PATH}}` | Caminho para o arquivo de aula | `cursos/nextjs-fundamentos/01-introducao/aula/aula.md` |
| `{{SLIDES_PATH}}` | Caminho para o arquivo de slides | `cursos/nextjs-fundamentos/01-introducao/slides/slides.md` |
| `{{EXERCICIOS_PATH}}` | Caminho para o arquivo de exercícios | `cursos/nextjs-fundamentos/01-introducao/exercicios/exercicios.md` |
| `{{TARGET_AUDIENCE}}` | Público-alvo do conteúdo | `iniciantes`, `intermediario`, `avancado` |
| `{{MODULO_TITLE}}` | Título legível do módulo | `Introdução ao Next.js` |
| `{{DATE}}` | Data de geração no formato ISO | `2026-06-27` |

## Boas Práticas

- Sempre informe o contexto completo do módulo no prompt (ementa, objetivos, conteúdo bruto)
- Prefira prompts específicos a genéricos — quanto mais detalhes, melhor o resultado
- Inclua exemplos de output desejado quando possível
- Revise e ajuste o template conforme o feedback dos alunos
