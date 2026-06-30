---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 07 — Design System: Consistência em Escala

## Módulo 07 - Design System: Consistência em Escala

---
## 1. O que é Design System

- Design System é um **conjunto integrado de padrões, componentes, diretrizes e ferramentas** que orientam a criação de...
- Style Guide:                    Component Library:              Design System:
- "Guia de estilos"               "Biblioteca de componentes"    "Sistema integrado"
- ─────────────────────           ─────────────────────           ────────────────────
- Cores, tipografia,              Botões, inputs, modais,         Tudo acima +

---
## 2. Atomic Design

- Criado por **Brad Frost**, o Atomic Design é uma metodologia que divide interfaces em **níveis hierárquicos** de comp...
- Átomos ─→ Moléculas ─→ Organismos ─→ Templates ─→ Páginas
- │            │             │             │            │
- │          Combina       Junta         Define       Aplica
- │          átomos        moléculas     layout       conteúdo

---
## 3. Design Tokens

- Design Tokens são as **variáveis visuais** do sistema. Eles abstraem decisões de design em valores únicos e reutilizá...
- // tokens/colors.ts
- export const colors = {
- brand: {
- primary:    { 50: '#eff6ff', 100: '#dbeafe', 200: '#bfdbfe',

---
## 4. Componentes

- Componentes são a **implementação concreta** dos tokens. Cada componente deve ser:
- Padronizado** — props consistentes entre componentes
- Documentado** — spec, variantes, exemplos
- Acessível** — ARIA, teclado, contraste
- Testado** — unitário, visual, acessibilidade

---
## 5. Documentação

- Documentação é o que **transforma uma biblioteca de componentes em um Design System**.
- Storybook é a ferramenta mais popular para documentar, testar e explorar componentes visualmente.
- // components/Button/Button.stories.ts
- import type { Meta, StoryObj } from '@storybook/react';
- import { Button } from './Button';

---
## Button — Especificação Técnica

- | Prop | Type | Default | Description |
- |------|------|---------|-------------|
- | variant | `'primary' \| 'secondary' \| 'outline' \| 'ghost' \| 'danger'` | `'primary'` | Estilo visual do botão |
- | size | `'sm' \| 'md' \| 'lg'` | `'md'` | Tamanho do botão |
- | loading | `boolean` | `false` | Exibe spinner e desabilita |

---
## 6. Versionamento

- Design Systems evoluem. Versionamento garante que **mudanças sejam previsíveis e seguras**.
- MAJOR.MINOR.PATCH
- MAJOR (1.x.x → 2.0.0):
- Breaking changes — componente renomeado, prop removida, token alterado
- Ex: Button: `variant="primary"` → `variant="filled"`

---
## Breaking Changes

- Antes:**
- <Button appearance="primary" />
- Depois:**
- <Button variant="primary" />
- Codemod:**

---
## [2.1.0] — 2026-06-15

- Novo componente: `Tooltip`
- Button: nova prop `leftIcon` e `rightIcon`
- Modal: nova variante `size="xl"`
- Input: cor de foco agora usa token primary ao invés de blue-500 fixo

---
## [2.0.0] — 2026-05-20

- Button: `appearance` → `variant`
- Modal: `size="small"|"medium"|"large"` → `size="sm"|"md"|"lg"`
- Tokens: `--color-blue-*` → `--color-primary-*`
- 

---
## 7. Consumo em Projetos

- // package.json (do Design System)
- {
- "name": "@empresa/design-system",
- "version": "2.1.0",
- "main": "dist/cjs/index.js",

---
## Exemplo: text

```text
Style Guide:                    Component Library:              Design System:
"Guia de estilos"               "Biblioteca de componentes"    "Sistema integrado"
─────────────────────           ─────────────────────           ────────────────────
Cores, tipografia,              Botões, inputs, modais,         Tudo acima +
grid, regras de uso             tabelas, cards                  processos, governance,
                                                                documentação,
─ Estático                      ─ Dinâmico                      tooling, princípios
─ PDF/doc                       ─ npm package                   ─ Ecossistema vivo
─ "O que usar"                  ─ "O que implementar"           ─ "Como pensar"

Exemplo:                        Exemplo:                        Exemplo:
Manual de marca                 Material UI                     Shopify Polaris
```

---
## Exemplo: typescript

```typescript
interface DesignSystemPurpose {
  consistencia:  'Mesma aparência e comportamento em todo o ecossistema';
  eficiencia:    'Devs e designers produzem mais rápido, sem recriar o óbvio';
  escalabilidade:'Novos produtos/heranças adotam o sistema sem retrabalho';
  qualidade:     'Componentes testados, acessíveis, documentados';
  colaboracao:   'Linguagem comum entre devs, designers, PMs, QA';
}
```

---
## Recap

- 1. O que é Design System
- 2. Atomic Design
- 3. Design Tokens
- 4. Componentes
- 5. Documentação
- Button — Especificação Técnica
- 6. Versionamento
- Breaking Changes
- [2.1.0] — 2026-06-15
- [2.0.0] — 2026-05-20
- 7. Consumo em Projetos

---
# Obrigado!

## Perguntas?
