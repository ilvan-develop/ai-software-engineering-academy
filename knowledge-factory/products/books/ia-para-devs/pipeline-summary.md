# Pipeline Status — Livro: IA para Desenvolvedores
# Atualizado em 2026-06-27

## Estado Geral

```
📗 IA para Desenvolvedores
├── 🟢 book-architect    (concluído)  → book.md + book-src-comparison.md
├── 🟢 content-writer    (concluído)  → conteúdo revisado e aprovado
├── 🟢 revisor           (concluído)  → 8 issues encontradas, 2 críticas
├── 🟢 book-publisher    (concluído)  → DOCX + EPUB + PDFs gerados
├── 🟢 designer-visual   (concluído)  → layout-book.yaml, cover-spec, slide-template
├── 🟢 criador-imagens   (concluído)  → prompts DALL-E/Midjourney gerados
├── 🟢 revisor-linguagem (concluído)  → português aprovado sem correções obrigatórias
├── 🟢 indexador-seo     (concluído)  → metadados, keywords, SEO metadata gerados
├── 🟢 consistency-auditor (concluído) → relatório com 3 achados menores
└── 🟢 pipeline-summary  (concluído)  → este arquivo
```

## Artefatos Gerados

### 📄 Conteúdo Compilado
| Arquivo | Tamanho | Descrição |
|---------|---------|-----------|
| `compiled/book.md` | 2.269 linhas | Livro completo agregado |
| `compiled/book-src-comparison.md` | — | Diff entre módulos fonte e compilado |
| `compiled/capitulo-01.md` | 503 linhas | Capítulo 1 separado |
| `compiled/capitulo-02.md` | 431 linhas | Capítulo 2 separado |
| `compiled/capitulo-03.md` | ~1.300 linhas | Capítulo 3 separado |

### 📚 Formatos de Publicação
| Arquivo | Descrição |
|---------|-----------|
| `output/livro.docx` | DOCX formatado para edição |
| `output/livro.epub` | EPUB navegável |
| `output/livro-digital.pdf` | PDF digital |
| `output/livro-grafica.pdf` | PDF para gráfica |

### 🎨 Design e Imagens
| Arquivo | Descrição |
|---------|-----------|
| `assets/layout-book.yaml` | Especificação completa de layout |
| `assets/cover-spec.md` | Especificação de capa (frente, lombada, quarta) |
| `assets/slide-template.md` | Template de slides 16:9 |
| `assets/cover-prompt.txt` | Prompts Midjourney + DALL-E para capa e diagramas |
| `assets/diagrams-prompt.txt` | Prompts específicos para diagramas internos |

### 📊 Relatórios
| Arquivo | Descrição |
|---------|-----------|
| `reports/review-report.md` | 8 issues de conteúdo |
| `reports/revisor-linguagem-report.md` | Revisão gramatical (aprovado) |
| `reports/consistency-audit-report.md` | Auditoria de consistência (3 achados) |

### 🔍 SEO
| Arquivo | Descrição |
|---------|-----------|
| `seo/seo-metadata.json` | Metadados Open Graph + JSON-LD + palavras-chave |

## Issues Pendentes (3)

| # | Severidade | Descrição | Local |
|---|-----------|-----------|-------|
| 1 | Média | Título duplicado nas primeiras linhas do Cap. 1 | `book.md:22-24` |
| 2 | Baixa | Dois H1 consecutivos nas transições de parte | `book.md:527-529` e `956-958` |
| 3 | Baixa | Capítulo 3 (Automação) ~2x maior que os demais | `book.md` |

## Next Steps Recomendados

1. Resolver issue #1 (título duplicado) antes da publicação final
2. Avaliar se part-titles (#2) devem ser ajustados
3. Considerar dividir Capítulo 3 em dois módulos (#3)
4. Executar book-publisher novamente após correções para regenerar formatos
5. Publicar nas plataformas-alvo (KDP, Hotmart, etc.)
