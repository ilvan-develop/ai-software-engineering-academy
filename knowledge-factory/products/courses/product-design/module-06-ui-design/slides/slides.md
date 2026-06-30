---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 06 — UI Design

## Módulo 06 - UI Design

---
## 1. O que é UI Design

- UI (User Interface) Design é a disciplina responsável pela **aparência e comportamento visual** de um produto digital...
- UI (User Interface)              UX (User Experience)
- ─────────────────────             ─────────────────────
- Aparência visual                 Experiência completa
- Cores, tipografia, ícones        Pesquisa, jornada, AI

---
## 2. Princípios de Design Visual — CRAP

- CRAP é um acrônimo para os 4 princípios fundamentais do design visual.
- Elementos diferentes devem **parecer diferentes**. Use contraste para destacar o que é importante.
- // ❌ Botão primário vs secundário quase iguais
- const bad = { primary: '#4A90D9', secondary: '#5BA0E9' };
- // ✅ Contraste claro entre ações

---
## 3. Cor

- Cores comunicam significado e emoção. No contexto enterprise, a escolha deve ser funcional, não apenas estética.
- | Cor | Significado comum | Uso em UI enterprise |
- |-----|------------------|---------------------|
- | Azul | Confiança, segurança | Primary action, links |
- | Verde | Sucesso, conclusão | Confirmação, status OK |

---
## 4. Tipografia

- A hierarquia guia o olho do usuário: o que é mais importante deve ser visualmente mais proeminente.
- interface TypographyScale {
- display: { size: number; lineHeight: number; weight: number };
- heading1: { size: number; lineHeight: number; weight: number };
- heading2: { size: number; lineHeight: number; weight: number };

---
## 5. Espaçamento e Grid

- Use uma escala de espaçamento, não valores arbitrários.
- const spacing = {
- xxs:  2,   // 2px  — divider finíssimo
- xs:   4,   // 4px  — ícone pequeno, gap mínimo
- sm:   8,   // 8px  — padding interno de inputs

---
## 6. Componentes de UI

- type ButtonVariant = 'primary' | 'secondary' | 'outline' | 'ghost' | 'danger';
- type ButtonSize = 'sm' | 'md' | 'lg';
- interface ButtonProps {
- variant: ButtonVariant;
- size: ButtonSize;

---
## 7. Design Patterns

- | Tipo | Quando usar | Exemplo |
- |------|------------|---------|
- | Sidebar | Muitas seções, hierarquia profunda | Dashboards |
- | Top nav | Poucas seções, conteúdo horizontal | Sites institucionais |
- | Tabs | Seções relacionadas, mesma página | Detalhes de registro |

---
## 8. Microinterações

- Microinterações são **pequenos momentos de feedback** que comunicam o resultado de uma ação.
- /* Botão — todos os estados */
- .button {
- background: #1A73E8;
- transition: background 0.15s ease, box-shadow 0.15s ease;

---
## 9. Dark Mode

- Dark mode não é apenas inverter cores — é um **tema alternativo** com paleta própria.
- type ThemeMode = 'light' | 'dark';
- interface Theme {
- mode: ThemeMode;
- colors: {

---
## 10. UI para Devs

- Ao inspecionar um layout no Figma, extraia:
- Elemento     | O que inspecionar
- ──────────────────────────────────────
- Botão        | width, height, padding, border-radius, font-size, bg
- Input        | padding, border, border-radius, font-size, label position

---
## Exemplo: text

```text
UI (User Interface)              UX (User Experience)
─────────────────────             ─────────────────────
Aparência visual                 Experiência completa
Cores, tipografia, ícones        Pesquisa, jornada, AI
Layout e componentes             Fluxo e arquitetura
Microinterações                  Emoção e usabilidade
"Como vê?"                       "Como se sente?"
```

---
## Exemplo: text

```text
UX sem UI: ideia sem forma, impossível de usar
UI sem UX: bonito mas inútil, frustrante
UI + UX: útil, usável e desejável
```

---
## Recap

- 1. O que é UI Design
- 2. Princípios de Design Visual — CRAP
- 3. Cor
- 4. Tipografia
- 5. Espaçamento e Grid
- 6. Componentes de UI
- 7. Design Patterns
- 8. Microinterações
- 9. Dark Mode
- 10. UI para Devs

---
# Obrigado!

## Perguntas?
