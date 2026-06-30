---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 05 — Wireframes

## Módulo 05 - Wireframes

---
## 1. O que são Wireframes

- Wireframe é o **esqueleto visual** de uma tela. É a representação estrutural da interface, focando em **layout, hiera...
- Wireframe serve para:
- ┌──────────────────────────────────────────────┐
- │  Validar fluxo e navegação antes do design   │
- │  Alinhar time sobre a estrutura da tela      │

---
## 2. Wireframe vs Mockup vs Protótipo

- É comum confundir os três. A diferença está no **nível de detalhe** e no **propósito**.
- DETALHE VISUAL
- ──────────────▶
- Wireframe ───▶  Mockup ───▶  Protótipo
- Estrutura        Visual        Interação
- ────────         ──────        ─────────

---
## 3. Princípios de Layout

- Wireframe eficiente segue princípios de design visual, mesmo sem cores.
- O grid é a **espinha dorsal** do layout. Ele garante alinhamento, consistência e ritmo.
- interface Grid {
- columns: number;       // ex: 12
- gutter: number;        // ex: 16px (espaço entre colunas)

---
## 4. Ferramentas

- | Ferramenta | Tipo | Fidelidade | Curva | Colaboração | Preço |
- |------------|------|-----------|-------|-------------|-------|
- | **Papel e caneta** | Físico | Baixa | Zero | Presencial | Grátis |
- | **Excalidraw** | Web | Baixa | 5 min | Tempo real (link) | Grátis |
- | **Balsamiq** | Desktop/Web | Baixa-média | 30 min | Compartilhamento | Pago (~$12/mês) |

---
## 5. Técnicas de Wireframing

- Técnica de **divergência criativa**: dobre uma folha em 8 partes, desenhe 8 variações diferentes de uma mesma tela em...
- Como fazer:
- 1. Defina o problema: "Tela de dashboard pós-login"
- 2. Configure timer de 8 minutos
- 3. Desenhe 8 versões diferentes (sem repetir)

---
## 6. Anatomia de uma Tela

- Toda tela segue uma estrutura comum. Conhecer a anatomia ajuda a criar wireframes consistentes.
- Anatomia padrão de uma página:
- ┌──────────────────────────────────────────────────────┐
- │  HEADER                                               │
- │  ┌──────┐  ┌──────────────────────┐  ┌────┐ ┌────┐  │
- │  │ LOGO │  │ Nav: Prod | Preços   │  │ Bus│ │User│  │

---
## 7. Interação — Estados e Transições

- Wireframes de média/alta fidelidade devem representar **estados da interface**.
- Cada componente pode estar em um dos seguintes estados:
- type ComponentState = 'loading' | 'empty' | 'error' | 'success' | 'disabled' | 'default' | 'hover' | 'active';
- interface StatefulComponent {
- name: string;

---
## 8. Validação de Wireframes

- Wireframe não é o destino — é um **meio para validar**.
- Transforme wireframes estáticos em protótipos clicáveis para testar fluxo:
- interface ClickableWireframe {
- screens: WireframeSpec[];
- hotspots: Hotspot[];

---
## 9. Wireframes em Enterprise

- Em contexto enterprise, wireframes vão além do esboço — eles se tornam **documentos de especificação**.
- Cada wireframe deve incluir metadados:
- interface WireframeDocumentation {
- // Metadados
- id: string;                    // "WF-001"

---
## Exemplo: text

```text
Wireframe serve para:
┌──────────────────────────────────────────────┐
│  Validar fluxo e navegação antes do design   │
│  Alinhar time sobre a estrutura da tela      │
│  Identificar inconsistências cedo            │
│  Servir de contrato entre produto e dev      │
│  Acelerar o ciclo de iteração                │
└──────────────────────────────────────────────┘
```

---
## Exemplo: typescript

```typescript
// Representação de níveis de fidelidade
type Fidelity = 'low' | 'medium' | 'high';

interface WireframeSpec {
  fidelity: Fidelity;
  elements: WireframeElement[];
  interactions?: Interaction[];
}

interface WireframeElement {
  type: 'header' | 'hero' | 'card' | 'form' | 'button' | 'footer';
  boundingBox: { x: number; y: number; w: number; h: number };
  placeholder: string; // "imagem do produto", "título"
}
```

---
## Recap

- 1. O que são Wireframes
- 2. Wireframe vs Mockup vs Protótipo
- 3. Princípios de Layout
- 4. Ferramentas
- 5. Técnicas de Wireframing
- 6. Anatomia de uma Tela
- 7. Interação — Estados e Transições
- 8. Validação de Wireframes
- 9. Wireframes em Enterprise

---
# Obrigado!

## Perguntas?
