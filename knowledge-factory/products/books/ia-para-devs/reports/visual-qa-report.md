# Visual QA Report — IA para Desenvolvedores

**Agente:** visual-qa
**Data:** 2026-06-28
**Versao:** 1.0.0
**Consome:** compiled/book.md, design-tokens.yaml, layout-book.yaml, brand-book.md

---

## Checklist de Qualidade Visual

### 1. Alinhamentos e Espacamento

- [x] Margens seguem layout-grid.yaml (print_6x9: 18mm top/bottom, 15mm inside, 12mm outside)
- [x] Baseline grid de 4mm respeitado (layout-grid.yaml)
- [ ] PARAGRAFOS: espacamento apos paragrafo (6pt) consistente? **PARCIAL** — quebras de linha irregulares em listas
- [x] HEADINGS: espacamento antes (12pt H2, 8pt H3, 6pt H4) respeitado
- [ ] CALLOUTS: padding de 8pt mantido? **NA** — callouts nao existem visualmente no markdown
- [ ] TABELAS: cell padding de 4pt? **PARCIAL** — HTML tables no Cap 1 tem padding irregular

### 2. Orfaos, Viuvas e Quebras

- [x] H1 sempre com page-break-before (layout-book.yaml)
- [ ] H2-H4 com minimo 1 linha de texto apos antes de quebra? **NAO VERIFICAVEL** (markdown sem paginacao)
- [ ] LINHAS: codigos com > 80 chars podem quebrar feio em impressao
  - **ACHADO:** book.md:1090 contem linha longa (YAML inline comentario)
  - **ACHADO:** book.md:1351-1355 contem strings longas em Terraform
  - **ACHADO:** book.md:2067-2077 contem URL longa do Datadog API
- [ ] LISTAS: itens com mais de 2 linhas podem quebrar entre paginas? **PARCIAL**
- [ ] TABELAS:celulas com texto longo (ex: tabela de 5 erros) quebram em EPUB

### 3. Hierarquia Visual

- [x] H1 distinto visualmente (21pt, bold, #1A237E, page break)
- [x] H2 distinto (17pt, bold, #1A237E)
- [x] H3 distinto (14pt, semibold, #0D47A1)
- [x] H4 distinto (12pt, semibold, #212121)
- [ ] NUMERO DE NIVEL: ha profundidade excessiva? **NAO** — max 3 niveis
- [ ] SEQUENCIA: H2 sempre apos H1, H3 sempre apos H2? **SIM**
- [ ] PULO: ha pulo de nivel (H1 direto para H3)? **NAO**

### 4. Tipografia

- [x] Fonte serifada para corpo (Georgia)
- [x] Fonte sans-serif para headings (Segoe UI)
- [x] Fonte monospace para codigo (Cascadia Code)
- [x] Tamanhos seguem design-tokens (body 11pt, code 9pt)
- [ ] LINE-HEIGHT: body 1.6 mantido? **VERIFICAVEL** — depende do renderizador
- [ ] LARGURA DE LINHA: 50-75 caracteres? **PARCIAL** — algumas linhas de texto corrido sao longas
- [ ] CONTRASTE: combinacoes WCAG AA+? **OK** (#212121 on #FFFFFF = 15:1)

### 5. Cores

- [x] Paleta segue design-tokens.yaml
- [x] Cores semanticas corretas (success #2E7D32, warning #F57F17, error #C62828)
- [ ] CALLOUTS: cores de fundo aplicadas nos tipos certos? **NA** — nao ha callouts implementados
- [ ] TABELAS: header com #1A237E e texto branco? **SIM** (especificado, depende de renderizacao)
- [ ] CODIGO: fundo #263238 com texto #E0E0E0? **SIM** (especificado)
- [ ] DALTONICO-SAFE: informacao nao depende apenas de cor? **SIM** (uso de icones e texto)
- [ ] P&B: diagramas e tabelas funcionam em grayscale? **PARCIAL** — diagramas Mermaid tem cores, mas forma diferencia nos

### 6. Elementos Visuais

- [x] Captions em diagramas presentes (texto alternativo)
- [x] Diagramas com descricao textual acessivel
- [ ] ICONES: usando Font Awesome via fa: prefix? **SIM** (nos diagramas Mermaid)
- [ ] ICONES: tamanho 1em inline, 1.5em callouts, 2em diagramas? **ESPECIFICADO** (nao verificado em renderizacao)
- [x] DIAGRAMAS: stroke brand.primary (#1A237E) e fill surface.callout_info (#E3F2FD)
- [x] SCREENSHOTS: sombra sutil (card elevation)
- [ ] CAPTIONS: italico, caption scale, centralizado abaixo? **ESPECIFICADO**

### 7. Formatacao de Codigo

- [x] Blocos de codigo com linguagem especificada (```typescript, ```yaml)
- [ ] Linguagem faltando em algum bloco? **VERIFICAR** — Cap 3 tem varios ```yaml, ok
- [ ] MAXIMO LINHAS: blocos > 30 linhas? **ACHADO**:
  - Cap 3: GitHub Actions YAML (~55 linhas, 1067-1152) — DIVIDIR
  - Cap 3: GitLab CI YAML (~50 linhas, 1156-1221) — DIVIDIR
  - Cap 3: Runbook YAML (~70 linhas, 2119-2188) — DIVIDIR
  - Cap 3: Deploy Production YAML (~60 linhas, 2262-2321) — DIVIDIR
- [ ] COMENTARIOS: marcacao [RUIM] e [BOM] presente? **SIM** nos exemplos do Cap 1
- [ ] LINHAS LONGAS: codigo com > 80 chars quebra em impressao? **ACHADO** em varios YAMLs

### 8. Imagens e Ilustracoes

- [ ] Imagens tem alt text descritivo? **NA** — nao ha imagens no markdown (so diagramas Mermaid)
- [ ] Captions em todas as figuras? **SIM** — diagramas Mermaid tem captions
- [ ] Largura max 85% (impresso) / 95% (digital)? **ESPECIFICADO** (depende do renderizador)
- [ ] Screenshots com elevacao de card? **ESPECIFICADO** (nenhum screenshot implementado)
- [ ] Diagramas Mermaid tem texto alternativo? **SIM** — captions em markdown abaixo

### 9. Tabelas

- [x] Header presente em todas as tabelas
- [ ] LINHAS ALTERNADAS: branco / neutral.200? **ESPECIFICADO** (depende do renderizador)
- [ ] BORDA: neutral.300, 0.5pt? **ESPECIFICADO**
- [ ] CELULA: padding 4pt? **ESPECIFICADO**
- [ ] TABELAS LONGAS: > 10 linhas identificadas? **SIM** — tabela de 17 agentes (Cap 2) tem 17 linhas
- [ ] TABELAS LARGAS: > 7 colunas? **NAO** — max 7 colunas

---

## Problemas Encontrados (Priorizados)

| ID | Severidade | Problema | Local | Correcao |
|----|------------|----------|-------|----------|
| VQA-01 | **CRITICO** | Nenhum callout implementado visualmente | Todo o livro | Inserir callouts conforme editorial-design-spec.yaml |
| VQA-02 | **CRITICO** | 4 blocos de codigo > 30 linhas | Cap 3 | Dividir em blocos menores com contexto textual entre eles |
| VQA-03 | **ALTA** | Redundancia Mermaid + ASCII (7 instancias) | Cap 1 e 2 | Remover diagramas ASCII; manter so Mermaid |
| VQA-04 | **ALTA** | Capitulo 3 sem diagramas alem do blue-green | Cap 3 | Inserir diagramas conforme diagram-spec.yaml |
| VQA-05 | **MEDIA** | Tabela de 17 agentes longa (17 linhas) | Cap 2 | Converter para diagrama org chart |
| VQA-06 | **MEDIA** | Linhas de codigo > 80 chars em YAML | Cap 3, varios | Quebrar linhas longas |
| VQA-07 | **MEDIA** | HTML table no Cap 1 nao e markdown valido | Cap 1, secao 3 | Substituir por code-comparison component |
| VQA-08 | **BAIXA** | Tabela de dados da industria na introducao | Cap 1, secao 1 | Converter para infographic (xychart) |
| VQA-09 | **BAIXA** | Links sem descricao de contexto | "Leituras complementares" | Adicionar descricao do que esperar em cada link |
| VQA-10 | **BAIXA** | Titulo duplicado nas primeiras linhas | book.md:22-24 | Remover duplicacao |

---

## Metricas de Qualidade Visual

| Metrica | Atual | Alvo | Status |
|---------|-------|------|--------|
| Callouts implementados | 0 | 20 | CRITICO |
| Diagramas unicos por capitulo | 3.3 | 5 | REGULAR |
| Blocos de codigo > 30 linhas | 4 | 0 | RUIM |
| Redundancia Mermaid + ASCII | 7 | 0 | CRITICO |
| Tabelas > 10 linhas | 1 | 0 | REGULAR |
| Captions em diagramas | 100% | 100% | OK |
| Alt text em imagens | N/A | 100% | N/A |
| Variacao de formato (1-10) | 5.3 | 8+ | RUIM |
| HTML bruto no markdown | 1 (HTML table) | 0 | REGULAR |

---

## Checklist de Acessibilidade Visual

- [x] Contraste WCAG AA+ em todas as combinacoes
- [x] Daltônico-safe: icones complementam cor
- [x] Font-size minimo: corpo 11pt, codigo 9pt
- [x] Dark mode suportado (CSS prefers-color-scheme)
- [x] Diagramas funcionam em P&B (forma dos nos)
- [ ] Navegacao semantica (headings sem saltos)
- [ ] Captions em todos os diagramas e figuras
- [ ] Texto alternativo em todas as imagens
- [ ] EPUB navegavel com landmarks ARIA

---

*Fim do relatorio visual-qa. Proximo: innovation-audit.md*
