# Brand Book — AI Software Engineering Academy Editora

**Versão:** 1.0.0
**Última atualização:** 2026-06-28
**Autoridade:** brand-book-designer
**Propósito:** Manual de identidade visual — todas as publicações DEVEM seguir estas diretrizes.

---

## 1. Missão Visual

Comunicar excelência técnica com clareza editorial. Nossos livros parecem publicações da O'Reilly, Manning ou No Starch Press — profissionais, minimalistas, com identidade própria.

---

## 2. Logotipo & Selo

**Logotipo principal:**
- Texto: "AI Software Engineering Academy" em fonte sans-serif
- Cor: brand.primary (#1A237E)
- Subtexto: "Editora" em brand.secondary (#0D47A1) — 60% do tamanho principal

**Selo da editora:**
- Forma: hexágono regular
- Cor: brand.primary (#1A237E)
- Símbolo interno: "A" estilizado (abertura de colchetes angulares: `<A>`)
- Grid: centralizado, borda de 2pt

**Usos proibidos:**
- Não distorcer proporções
- Não usar em fundo que cause contraste < 4.5:1
- Não adicionar sombras ou efeitos 3D no selo

---

## 3. Paleta de Cores

### Cores primárias
| Token          | Cor   | Hex       | Uso                            |
|----------------|-------|-----------|--------------------------------|
| brand.primary  | Azul  | `#1A237E` | Capa, headings, tabelas, capít |
| brand.secondary| Azul  | `#0D47A1` | Subtítulos, links              |
| brand.accent   | Teal  | `#00BFA5` | CTAs, destaques, ícones        |

### Neutros
A escala neutral (#FFFFFF a #000000) define toda a hierarquia tipográfica.

### Semântica
| Token                | Hex       | Uso                          |
|----------------------|-----------|------------------------------|
| semantic.success     | `#2E7D32` | Output correto, checklists   |
| semantic.warning     | `#F57F17` | Atenção, deprecações         |
| semantic.error       | `#C62828` | Erros, exceções              |
| semantic.info        | `#1565C0` | Notas, dicas, callouts info  |

### Callouts
- **Info:** fundo `#E3F2FD`, borda `#1565C0`
- **Warning:** fundo `#FFF8E1`, borda `#F57F17`
- **Tip:** fundo `#E8F5E9`, borda `#2E7D32`
- **Caution:** fundo `#FFEBEE`, borda `#C62828`

---

## 4. Tipografia

### Fontes
| Uso          | Família                    | Fallback stack                           |
|--------------|----------------------------|------------------------------------------|
| Corpo        | Georgia                    | `Georgia, 'Times New Roman', serif`      |
| Headings     | Segoe UI                   | `'Segoe UI', 'Helvetica Neue', Arial`    |
| Código       | Cascadia Code              | `'Cascadia Code', 'Fira Code', Consolas` |

### Escala (para impressão — pt)
| Nível | Tamanho | Peso    | Cor            | Uso                               |
|-------|---------|---------|----------------|-----------------------------------|
| H1    | 21pt    | Bold    | brand.primary  | Título de capítulo                |
| H2    | 17pt    | Bold    | brand.primary  | Seção principal                   |
| H3    | 14pt    | Semibold| brand.secondary| Subseção                          |
| H4    | 12pt    | Semibold| text.body      | Sub-subseção                      |
| Body  | 11pt    | Regular | text.body      | Parágrafos                        |
| Código| 9pt     | Regular | text.code      | Blocos de código                  |

### Regras tipográficas
- **Largura de linha:** 50-75 caracteres (impresso)
- **Leading:** 1.6× corpo (body), 1.3× (headings)
- **Tracking:** normal para body; +0.5px para headings H1-H2
- **H1 sempre:** quebra de página antes
- **H2-H4:** mínimo 1 linha de texto após antes de quebra

---

## 5. Grid & Layout

Ver `layout-grid.yaml` para especificações técnicas completas.

### Princípios
- Margens internas maiores que externas (impresso): 15mm inside, 12mm outside (6×9)
- Baseline grid de 4mm (6×9), 4.5mm (7×10), 5mm (A4)
- Digital: largura máxima de conteúdo 720px, margens 16px
- Impresso: sem colunas exceto A4 (2 colunas)
- Grid de rodapé: 10mm da borda inferior

---

## 6. Elementos Visuais

### Capa
- **Fundo:** brand.primary (#1A237E) degradê sutil para brand.secondary
- **Título:** branco (text.inverse), h1 size × 2, sans-serif display
- **Autor:** branco, body size
- **Selo:** canto superior direito, 25mm × 25mm
- **Ilustração:** central, monocromática (traço branco 2pt sobre fundo azul)

### Cabeçalhos/rodapés (impresso)
- **Cabeçalho:** título do capítulo (verso) / título do livro (frente) — 8pt, neutral.500
- **Rodapé:** número da página — 9pt, brand.primary
- **Linha separadora:** 0.5pt, neutral.300 — 30mm de largura

### Blocos de código
- Fundo: surface.code_block (#263238)
- Fonte: mono, 9pt
- Padding: 8px todos os lados
- Borda: border_radius.sm (2px)
- Número de linha: opcional, neutral.600 à esquerda

### Callouts
- Ícone à esquerda (informacional, alerta, dica, cuidado)
- Borda grossa à esquerda (4px) na cor semântica correspondente
- Fundo conforme tabela de callouts na seção 3
- Padding: 8px, border_radius: 3px

### Tabelas
- Header: brand.primary, texto branco, bold
- Linhas alternadas: branco / neutral.200
- Borda: neutral.300, 0.5pt
- Cell padding: 4px

### Imagens & Diagramas
- Largura máxima: 85% da página (impresso), 95% (digital)
- Caption: itálico, caption scale, centralizado abaixo
- Screenshots: sombra sutil (card elevation)
- Diagramas: stroke brand.primary, fill surface.callout_info

---

## 7. Tom & Voz Visual

- **Sóbrio mas não frio** — cores neutras dominam, cor aparece com propósito
- **Código é cidadão de primeira classe** — blocos de código têm destaque visual no layout
- **Hierarquia inconfundível** — o leitor sabe instantaneamente o que é título, subtítulo, corpo, callout
- **Minimalismo informado** — cada elemento visual tem função; sem decoração vazia
- **Consistência acima de criatividade** — templates primeiro, exceções só com justificativa

---

## 8. Acessibilidade

- **Contraste WCAG AA+** — todas as combinações ≥ 4.5:1 (normal) e ≥ 3:1 (grande)
- **Daltônico-safe** — nunca usar apenas cor para transmitir informação
- **Font-size mínimo:** corpo 11pt, código 9pt, notas 8pt
- **Dark mode** — EPUB/PDF digital: suportar prefers-color-scheme
- **Navegação:** landmarks ARIA, heading order sem saltos, TOC navegável

---

## 9. Formatos & Outputs

| Formato     | Grid          | Cor         | Interatividade | Prioridade |
|-------------|---------------|-------------|----------------|------------|
| PDF digital | digital       | RGB         | Links, TOC     | Alta       |
| PDF gráfica | print_6x9     | CMYK        | Nenhuma        | Alta       |
| EPUB        | digital       | RGB         | Full           | Alta       |
| DOCX        | digital       | RGB         | Links, TOC     | Média      |

- **RGB vs CMYK:** PDF digital, EPUB, DOCX em RGB. PDF gráfica convertido para CMYK (FOGRA39)
- **Fontes:** EPUB/DOCX usam fontes do sistema. PDF digital incorpora (subset). PDF gráfica requer fontes licenciadas.

---

## 10. Governança

1. **brand-book-designer** é a autoridade máxima sobre este documento
2. Mudanças requerem PR revisado por design-token-manager e visual-hierarchy-auditor
3. Este documento tem versão semântica (SemVer) — mesmo versionamento dos design tokens
4. Qualquer divergência visual entre formatos constitui bug e deve ser reportada
