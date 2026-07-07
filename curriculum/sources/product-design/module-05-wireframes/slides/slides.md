# Módulo 05 — Slides

---

## Slide 1: Título

**Wireframes — Esboçar para validar**
Estrutura antes de visual. Validação antes de código.

---

## Slide 2: O que são Wireframes?

Esqueleto visual da interface — foco em **layout, hierarquia, conteúdo**.

```text
❌ SEM CORES    ❌ SEM FONTES    ❌ SEM IMAGENS
✅ ESTRUTURA    ✅ FLUXO         ✅ FUNCIONALIDADE
```markdown

---

## Slide 3: Níveis de Fidelidade

| Fidelidade | Aparência | Quando usar |
|------------|-----------|-------------|
| **Baixa** | Esboço à mão | Brainstorming, ideação |
| **Média** | Grey box (cinzas) | Validar fluxo, testar |
| **Alta** | Quase real com grid | Handoff, aprovação |

---

## Slide 4: Wireframe vs Mockup vs Protótipo

```text
Wireframe     Mockup       Protótipo
Estrutura     Visual       Interação
Caixas        Cores        Clica
Hierarquia    Fontes       Navega
```markdown

Wireframe = **o que**. Mockup = **como parece**. Protótipo = **como funciona**.

---

## Slide 5: Princípios de Layout — Grid

Grid de 12 colunas é o padrão da indústria.

```text
┌──────────────────────────────────────────┐
│  Header (12 col)                         │
├──────┬──────┬──────┬────────────────────┤
│  3   │  3   │  3   │  3                 │
├──────┴──────┴──────┴────────────────────┤
│  Content (8 col)       │ Sidebar (4 col)│
├────────────────────────┴────────────────┤
│  Footer (12 col)                        │
└──────────────────────────────────────────┘
```javascript

---

## Slide 6: Hierarquia Visual

Organize por **importância**:

1. Hero / Título principal — maior, central
2. CTA — destaque visual (contraste de forma)
3. Conteúdo — blocos organizados
4. Navegação — secundária, no topo
5. Footer — menor destaque

---

## Slide 7: Ferramentas de Wireframing

| Ferramenta | Curva | Ideal para |
|------------|-------|------------|
| Papel | Zero | Brainstorming individual |
| Excalidraw | 5 min | Esboço remoto rápido |
| Balsamiq | 30 min | Documentação regulatória |
| Figma | 2h | Enterprise, handoff, DS |

---

## Slide 8: Técnica — Crazy 8s

8 variações de uma tela em 8 minutos.

```text
1. Defina o problema
2. Dobre a folha em 8 partes
3. 1 minuto por quadro — sem repetir
4. Vote na melhor ideia
5. Refine em um wireframe único
```markdown

Força **divergência criativa** antes de convergir.

---

## Slide 9: Técnica — Grey Box

Caixas cinzas para representar elementos.

```text
┌─────────────────────────────────────┐
│  ████  ████████████████  ██  ██  │  ← header
├─────────────────────────────────────┤
│  ┌───────────────────────────┐      │
│  │  ████████████████████    │      │  ← hero
│  └───────────────────────────┘      │
│  ┌────┐ ┌────┐ ┌────┐              │
│  │ ██ │ │ ██ │ │ ██ │              │  ← cards
│  └────┘ └────┘ └────┘              │
└─────────────────────────────────────┘
```markdown

---

## Slide 10: Anatomia de uma Tela

```text
HEADER → Logo + Navegação
HERO   → Título + CTA
CONTEÚDO → Cards, listas, formulários
CTA    → Ação principal (destacado)
FOOTER → Links + Legal
```markdown

Toda tela segue essa estrutura básica.

---

## Slide 11: Estados da Interface

| Estado | Representação |
|--------|---------------|
| Loading | Skeleton boxes |
| Empty | "Nada aqui" + CTA |
| Error | Mensagem + ação |
| Success | Confirmação |
| Disabled | Opaco |

Sempre mapeie **todos os estados** no wireframe.

---

## Slide 12: Validação

Clickable wireframe → Teste com usuário → Itere

```text
Esboçar → Validar → Aprender → Refinar → (repetir)
```javascript

Ferramentas: Figma (prototype mode), Balsamiq (links).

---

## Slide 13: Wireframes em Enterprise

Wireframe vira **documento de especificação**:

```json
[ ] ID: WF-001
[ ] User Story: US-042
[ ] Versão: 1.3
[ ] Aprovações: PO, DesignLead, TechLead
[ ] Handoff: medidas, grid, breakpoints, estados
[ ] Changelog por versão
```yaml

---

## Slide 14: Handoff para Devs

Checklist:

```json
[ ] Grid definido (colunas, gutters)
[ ] Medidas exatas dos elementos
[ ] Espaçamentos documentados
[ ] Estados mapeados (loading, empty, error)
[ ] Breakpoints (mobile, tablet, desktop)
[ ] Nomes consistentes com design system
[ ] Fluxo de navegação diagramado
```markdown

---

## Slide 15: Para refletir

> "Wireframes são sobre **o que** a tela faz, não **como** ela parece."

> "Um wireframe bem feito economiza semanas de retrabalho."

> "Se você não pode validar no wireframe, não vai consertar no código."
