# Módulo 06 - UI Design

---

## 1. O que é UI Design

UI (User Interface) Design é a disciplina responsável pela **aparência e comportamento visual** de um produto digital. Enquanto UX define a estrutura e a experiência, UI traduz essa estrutura em pixels — cores, tipografia, espaçamento, componentes e animações.
### UI ≠ UX
UI (User Interface)              UX (User Experience)
─────────────────────             ─────────────────────

## 2. Princípios de Design Visual — CRAP

CRAP é um acrônimo para os 4 princípios fundamentais do design visual.
### Contraste
Elementos diferentes devem **parecer diferentes**. Use contraste para destacar o que é importante.
// ❌ Botão primário vs secundário quase iguais

## 3. Cor

### Teoria das Cores
Cores comunicam significado e emoção. No contexto enterprise, a escolha deve ser funcional, não apenas estética.
| Cor | Significado comum | Uso em UI enterprise |
|-----|------------------|---------------------|

## 4. Tipografia

### Hierarquia Tipográfica
A hierarquia guia o olho do usuário: o que é mais importante deve ser visualmente mais proeminente.
interface TypographyScale {
display: { size: number; lineHeight: number; weight: number };

## 5. Espaçamento e Grid

### Box Model e Spacing Consistente
Use uma escala de espaçamento, não valores arbitrários.
const spacing = {
xxs:  2,   // 2px  — divider finíssimo

## 6. Componentes de UI

### Botões
type ButtonVariant = 'primary' | 'secondary' | 'outline' | 'ghost' | 'danger';
type ButtonSize = 'sm' | 'md' | 'lg';
interface ButtonProps {

---
*Este artigo faz parte da formacao Arquitetura de Software Enterprise com IA*