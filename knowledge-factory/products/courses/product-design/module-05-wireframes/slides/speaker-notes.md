## Introducao

# Módulo 05 — Wireframes
**Esboçar telas antes de codar. Validar antes de investir.**
---

---
## 1. O que são Wireframes

Wireframe é o **esqueleto visual** de uma tela. É a representação estrutural da interface, focando em **layout, hierarquia, conteúdo e funcionalidade** — sem nenhum polimento visual (cores, fontes, imagens).
### Propósito
Wireframe serve para:
┌──────────────────────────────────────────────┐
│  Validar fluxo e navegação antes do design   │
│  Alinhar time sobre a estrutura da tela      │
│  Identificar inconsistências cedo            │
│  Servir de contrato entre produto e dev      │

---
## 2. Wireframe vs Mockup vs Protótipo

É comum confundir os três. A diferença está no **nível de detalhe** e no **propósito**.
DETALHE VISUAL
──────────────▶
Wireframe ───▶  Mockup ───▶  Protótipo
Estrutura        Visual        Interação
────────         ──────        ─────────
Caixas           Cores         Clica
Hierarquia       Fontes        Navega

---
## 3. Princípios de Layout

Wireframe eficiente segue princípios de design visual, mesmo sem cores.
### Grid
O grid é a **espinha dorsal** do layout. Ele garante alinhamento, consistência e ritmo.
interface Grid {
columns: number;       // ex: 12
gutter: number;        // ex: 16px (espaço entre colunas)
margin: number;        // ex: 24px (margem lateral)
breakpoints: Record<string, number>;

---
## 4. Ferramentas

### Comparação
| Ferramenta | Tipo | Fidelidade | Curva | Colaboração | Preço |
|------------|------|-----------|-------|-------------|-------|
| **Papel e caneta** | Físico | Baixa | Zero | Presencial | Grátis |
| **Excalidraw** | Web | Baixa | 5 min | Tempo real (link) | Grátis |
| **Balsamiq** | Desktop/Web | Baixa-média | 30 min | Compartilhamento | Pago (~$12/mês) |
| **Figma** | Web | Média-alta | 2h | Tempo real + comentários | Grátis (inicio) |
| **Whimsical** | Web | Baixa-média | 15 min | Link compartilhável | Grátis (limitado) |

---
## 5. Técnicas de Wireframing

### Esboço Rápido (Crazy 8s)
Técnica de **divergência criativa**: dobre uma folha em 8 partes, desenhe 8 variações diferentes de uma mesma tela em **8 minutos** (1 minuto cada).
Como fazer:
1. Defina o problema: "Tela de dashboard pós-login"
2. Configure timer de 8 minutos
3. Desenhe 8 versões diferentes (sem repetir)
4. Ao final, vote na melhor ideia
5. Refine a vencedora em um wireframe único

---
## 6. Anatomia de uma Tela

Toda tela segue uma estrutura comum. Conhecer a anatomia ajuda a criar wireframes consistentes.
Anatomia padrão de uma página:
┌──────────────────────────────────────────────────────┐
│  HEADER                                               │
│  ┌──────┐  ┌──────────────────────┐  ┌────┐ ┌────┐  │
│  │ LOGO │  │ Nav: Prod | Preços   │  │ Bus│ │User│  │
│  └──────┘  └──────────────────────┘  └────┘ └────┘  │
├──────────────────────────────────────────────────────┤

---
## 7. Interação — Estados e Transições

Wireframes de média/alta fidelidade devem representar **estados da interface**.
### Estados de Componentes
Cada componente pode estar em um dos seguintes estados:
type ComponentState = 'loading' | 'empty' | 'error' | 'success' | 'disabled' | 'default' | 'hover' | 'active';
interface StatefulComponent {
name: string;
states: Record<ComponentState, WireframeElement>;
}

---
## 8. Validação de Wireframes

Wireframe não é o destino — é um **meio para validar**.
### Clickable Wireframes
Transforme wireframes estáticos em protótipos clicáveis para testar fluxo:
interface ClickableWireframe {
screens: WireframeSpec[];
hotspots: Hotspot[];
}
interface Hotspot {

---
## 9. Wireframes em Enterprise

Em contexto enterprise, wireframes vão além do esboço — eles se tornam **documentos de especificação**.
### Documentação
Cada wireframe deve incluir metadados:
interface WireframeDocumentation {
// Metadados
id: string;                    // "WF-001"
title: string;                 // "Tela de Login"
module: string;                // "Autenticação"

---
