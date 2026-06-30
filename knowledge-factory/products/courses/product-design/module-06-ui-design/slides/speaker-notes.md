## Introducao

# Módulo 06 — UI Design
**Transformar wireframes em interfaces funcionais, acessíveis e visualmente consistentes.**
---

---
## 1. O que é UI Design

UI (User Interface) Design é a disciplina responsável pela **aparência e comportamento visual** de um produto digital. Enquanto UX define a estrutura e a experiência, UI traduz essa estrutura em pixels — cores, tipografia, espaçamento, componentes e animações.
### UI ≠ UX
UI (User Interface)              UX (User Experience)
─────────────────────             ─────────────────────
Aparência visual                 Experiência completa
Cores, tipografia, ícones        Pesquisa, jornada, AI
Layout e componentes             Fluxo e arquitetura
Microinterações                  Emoção e usabilidade

---
## 2. Princípios de Design Visual — CRAP

CRAP é um acrônimo para os 4 princípios fundamentais do design visual.
### Contraste
Elementos diferentes devem **parecer diferentes**. Use contraste para destacar o que é importante.
// ❌ Botão primário vs secundário quase iguais
const bad = { primary: '#4A90D9', secondary: '#5BA0E9' };
// ✅ Contraste claro entre ações
const good = { primary: '#1A73E8', secondary: '#E8F0FE' };
- Contraste de **cor**: fundo vs texto, botão primário vs secundário

---
## 3. Cor

### Teoria das Cores
Cores comunicam significado e emoção. No contexto enterprise, a escolha deve ser funcional, não apenas estética.
| Cor | Significado comum | Uso em UI enterprise |
|-----|------------------|---------------------|
| Azul | Confiança, segurança | Primary action, links |
| Verde | Sucesso, conclusão | Confirmação, status OK |
| Vermelho | Erro, perigo | Erro, ação destrutiva |
| Amarelo | Atenção, aviso | Warning, alerta |

---
## 4. Tipografia

### Hierarquia Tipográfica
A hierarquia guia o olho do usuário: o que é mais importante deve ser visualmente mais proeminente.
interface TypographyScale {
display: { size: number; lineHeight: number; weight: number };
heading1: { size: number; lineHeight: number; weight: number };
heading2: { size: number; lineHeight: number; weight: number };
heading3: { size: number; lineHeight: number; weight: number };
body: { size: number; lineHeight: number; weight: number };

---
## 5. Espaçamento e Grid

### Box Model e Spacing Consistente
Use uma escala de espaçamento, não valores arbitrários.
const spacing = {
xxs:  2,   // 2px  — divider finíssimo
xs:   4,   // 4px  — ícone pequeno, gap mínimo
sm:   8,   // 8px  — padding interno de inputs
md:   12,  // 12px — gap entre label e input
lg:   16,  // 16px — padding de cards, seções

---
## 6. Componentes de UI

### Botões
type ButtonVariant = 'primary' | 'secondary' | 'outline' | 'ghost' | 'danger';
type ButtonSize = 'sm' | 'md' | 'lg';
interface ButtonProps {
variant: ButtonVariant;
size: ButtonSize;
disabled?: boolean;
loading?: boolean;

---
## 7. Design Patterns

### Navegação
| Tipo | Quando usar | Exemplo |
|------|------------|---------|
| Sidebar | Muitas seções, hierarquia profunda | Dashboards |
| Top nav | Poucas seções, conteúdo horizontal | Sites institucionais |
| Tabs | Seções relacionadas, mesma página | Detalhes de registro |
| Breadcrumb | Hierarquia profunda, orientação | E-commerce, docs |
| Stepper | Fluxo sequencial | Wizard, checkout |

---
## 8. Microinterações

Microinterações são **pequenos momentos de feedback** que comunicam o resultado de uma ação.
### Estados Visuais
/* Botão — todos os estados */
.button {
background: #1A73E8;
transition: background 0.15s ease, box-shadow 0.15s ease;
cursor: pointer;
}

---
## 9. Dark Mode

### Estratégia de Implementação
Dark mode não é apenas inverter cores — é um **tema alternativo** com paleta própria.
type ThemeMode = 'light' | 'dark';
interface Theme {
mode: ThemeMode;
colors: {
background: {
primary: string;

---
## 10. UI para Devs

### Inspeção no Figma
Ao inspecionar um layout no Figma, extraia:
Elemento     | O que inspecionar
──────────────────────────────────────
Botão        | width, height, padding, border-radius, font-size, bg
Input        | padding, border, border-radius, font-size, label position
Card         | padding, border-radius, box-shadow, gap entre filhos
Text         | font-family, font-size, line-height, letter-spacing, color

---
