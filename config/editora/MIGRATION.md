# Migração: Book Factory → Editorial Enterprise Pipeline
# Este documento mapeia os agentes antigos para a nova estrutura de 5 departamentos

## Agentes Existentes → Novo Departamento

| Agente Antigo | Departamento Novo | Novo Nome | Ação |
|--------------|------------------|-----------|------|
| curriculum-architect | Conteúdo | curriculum-architect | Manter, atualizar prompt |
| technical-writer | Conteúdo | technical-writer | Manter, atualizar prompt |
| exercise-creator | Conteúdo | exercise-creator | Manter, atualizar prompt |
| quiz-creator | Conteúdo | quiz-creator | Manter, atualizar prompt |
| curador-conteudo | Conteúdo | research-agent | Renomear |
| copy-editor | Editorial | grammar-reviewer | Novo prompt |
| style-reviewer | Editorial | style-reviewer | Novo prompt |
| consistency-auditor | Editorial | consistency-auditor | Novo prompt |
| readability-auditor | Editorial | readability-auditor | Novo prompt |
| terminology-auditor | Editorial | terminology-auditor | Novo prompt |
| technical-accuracy-reviewer | Editorial | technical-accuracy-reviewer | Novo prompt |
| reviewer | QA Editorial | book-quality-auditor | Renomear + expandir |
| revisor-linguagem | Editorial | grammar-reviewer | Mesclar |
| designer-visual | Design | book-designer | Mesclar |
| slide-creator | Design | layout-designer | Renomear |
| design-system-editorial | Design | book-designer | Mesclar |
| criador-imagens | Design | diagram-designer | Renomear |
| indexador-seo | Publicação | markdown-auditor | Renomear |
| book-architect | (orquestrador) | book-architect | Manter (script-based) |
| book-publisher | Publicação | docx-generator | Expandir |
| gestor-pipeline | (orquestrador) | gestor-pipeline | Manter (script-based) |
| tradutor-conteudo | (transversal) | tradutor-conteudo | Manter como serviço |
| linkedin-creator | (distribuição) | linkedin-creator | Manter como serviço |

## Agentes NOVOS (sem equivalente antigo)
- Chief Editor (Conteúdo)
- Subject Matter Expert (Conteúdo)
- Educational Designer (Conteúdo)
- Research Agent (Conteúdo)
- Fact Checker (Conteúdo)
- Example Creator (Conteúdo)
- Copy Editor (Editorial)
- Typography Specialist (Design)
- Color Specialist (Design)
- Illustration Planner (Design)
- Table Designer (Design)
- Callout Designer (Design)
- Cover Designer (Design)
- Markdown Auditor (Publicação)
- PDF Generator (Publicação)
- EPUB Generator (Publicação)
- Template Manager (Publicação)
- Brand Consistency Agent (Publicação)
- Accessibility Auditor (Publicação)
- Pedagogical Auditor (QA)
- Technical Auditor (QA)
- Visual Auditor (QA)
- Publishing Auditor (QA)
- Score Aggregator (QA)
- Compliance Reporter (QA)
- Gatekeeper (QA)
- Audit Trail Recorder (QA)

## Ações Recomendadas

### Imediatas (já executadas nesta sessão)
1. ✅ BQS Core criado em curriculum/bqs/bqs-core.yaml
2. ✅ 5 conjuntos de critérios por departamento
3. ✅ Gate policy criada
4. ✅ 42 agent prompts criados em config/editora/teams/
5. ✅ Pipeline gates definido
6. ✅ Scripts Python (bqs_scorer, gate_keeper, audit_recorder)

### Próximas
7. ⬜ Registrar 5 department leads no opencode.json
8. ⬜ Atualizar prompts dos 7 agentes existentes
9. ⬜ Rodar baseline BQS contra ia-para-devs
10. ⬜ Substituir pipeline_manager.py pelo novo pipeline gated

---
**Última atualização:** 2026-06-28

## Sessão 2026-06-28: Design Tokens + Novos Agentes de Design

### Criados
- `config/editora/design-tokens.yaml` — tokens de cores, tipografia, espaçamento, elevação, breakpoints (v1.0.0)
- `config/editora/brand-book.md` — manual de identidade visual completo (10 seções)
- `config/editora/layout-grid.yaml` — grid modular multi-formato (6×9, 7×10, A4, digital)

### Registrados no opencode.json
- 10 novos subagentes de design: brand-book-designer, information-designer, epub-css-architect, print-production-specialist, accessible-design-specialist, visual-hierarchy-auditor, design-token-manager, template-developer, cover-illustration-director, layout-system-architect
- departamento-design expandido de 9 para 20 agentes (6 steps sequenciais)
- book-factory atualizado: 16 categorias BQS, 3 novos assets globais

### Modificados
- `curriculum/bqs/bqs-core.yaml` → v2.0, 16 categorias (+5 design visual), pesos rebalanceados
- `opencode.json` → book-factory prompt com 16 cats e novos comandos
- `scripts/editora/bqs_scorer.py` → matching por critério explícito (não prefixo)
- `knowledge-factory/livros/ia-para-devs/assets/layout-book.yaml` → v2.0, consumindo tokens globais
- `knowledge-factory/livros/ia-para-devs/compiled/book.md` → design system metadata + paleta

### BQS Baseline v2.0 — ia-para-devs
- Score geral: 92.8/100 (REPROVADO — esperado, 5 novas categorias)
- 11/11 categorias originais aprovadas (≥95)
- 5 novas categorias de design visual: gap médio de 9.7 pts
- Gaps principais: Identidade Visual (-7.0), Qualidade Tipográfica (-7.2), Design de Informação (-13.5), Acessibilidade Visual (-13.2), Consistência entre Formatos (-13.5)
- Score-card salvo em: `knowledge-factory/livros/ia-para-devs/reports/score-card-ia-para-devs.yaml`

### Bugs corrigidos
- `bqs_scorer.py`: prefix-matching colidia `qualidade_tecnica` (qt1-qt5) com `qualidade_tipografica` (qt1→tp1-qt5→tp5)
- `bqs-core.yaml`: IDs duplicados `qt1-qt5` renomeados para `tp1-tp5` em qualidade_tipografica
