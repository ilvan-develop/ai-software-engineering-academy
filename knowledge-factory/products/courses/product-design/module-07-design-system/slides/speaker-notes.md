## Introducao

# Módulo 07 — Design System: Consistência em Escala
**Um Design System não é um projeto. É um produto que serve outros produtos.**
---

---
## 1. O que é Design System

Design System é um **conjunto integrado de padrões, componentes, diretrizes e ferramentas** que orientam a criação de interfaces digitais de forma consistente e escalável.
### Design System vs Style Guide vs Component Library
Style Guide:                    Component Library:              Design System:
"Guia de estilos"               "Biblioteca de componentes"    "Sistema integrado"
─────────────────────           ─────────────────────           ────────────────────
Cores, tipografia,              Botões, inputs, modais,         Tudo acima +
grid, regras de uso             tabelas, cards                  processos, governance,
documentação,

---
## 2. Atomic Design

Criado por **Brad Frost**, o Atomic Design é uma metodologia que divide interfaces em **níveis hierárquicos** de complexidade.
### Os 5 níveis
Átomos ─→ Moléculas ─→ Organismos ─→ Templates ─→ Páginas
│            │             │             │            │
│          Combina       Junta         Define       Aplica
│          átomos        moléculas     layout       conteúdo
▼            ▼             ▼             ▼            ▼
Botão      Input +       Formulário    Página de     Página de

---
## 3. Design Tokens

Design Tokens são as **variáveis visuais** do sistema. Eles abstraem decisões de design em valores únicos e reutilizáveis.
### Definição em TypeScript
// tokens/colors.ts
export const colors = {
brand: {
primary:    { 50: '#eff6ff', 100: '#dbeafe', 200: '#bfdbfe',
300: '#93c5fd', 400: '#60a5fa', 500: '#3b82f6',
600: '#2563eb', 700: '#1d4ed8', 800: '#1e40af',

---
## 4. Componentes

Componentes são a **implementação concreta** dos tokens. Cada componente deve ser:
- **Padronizado** — props consistentes entre componentes
- **Documentado** — spec, variantes, exemplos
- **Acessível** — ARIA, teclado, contraste
- **Testado** — unitário, visual, acessibilidade
### Botão
// components/Button/Button.tsx
import { ButtonHTMLAttributes, forwardRef } from 'react';

---
## 5. Documentação

Documentação é o que **transforma uma biblioteca de componentes em um Design System**.
### Storybook
Storybook é a ferramenta mais popular para documentar, testar e explorar componentes visualmente.
// components/Button/Button.stories.ts
import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';
const meta: Meta<typeof Button> = {
title: 'Components/Button',

---
## Button — Especificação Técnica

### Props
| Prop | Type | Default | Description |
|------|------|---------|-------------|
| variant | `'primary' \| 'secondary' \| 'outline' \| 'ghost' \| 'danger'` | `'primary'` | Estilo visual do botão |
| size | `'sm' \| 'md' \| 'lg'` | `'md'` | Tamanho do botão |
| loading | `boolean` | `false` | Exibe spinner e desabilita |
| disabled | `boolean` | `false` | Desabilita interação |
| fullWidth | `boolean` | `false` | Ocupa 100% do container |

---
## 6. Versionamento

Design Systems evoluem. Versionamento garante que **mudanças sejam previsíveis e seguras**.
### SemVer (Semantic Versioning)
MAJOR.MINOR.PATCH
MAJOR (1.x.x → 2.0.0):
Breaking changes — componente renomeado, prop removida, token alterado
Ex: Button: `variant="primary"` → `variant="filled"`
MINOR (x.1.x → x.2.0):
Novas funcionalidades — novo componente, nova variante, nova prop

---
## Breaking Changes

### Button: `appearance` → `variant`
**Antes:**
<Button appearance="primary" />
**Depois:**
<Button variant="primary" />
**Codemod:**
npx @acme/ds-codemod button-appearance-to-variant
### Modal: sizes renomeados

---
## [2.1.0] — 2026-06-15

### Added
- Novo componente: `Tooltip`
- Button: nova prop `leftIcon` e `rightIcon`
- Modal: nova variante `size="xl"`
### Changed
- Input: cor de foco agora usa token primary ao invés de blue-500 fixo
- Table: sortable agora é opcional (default: true)
### Fixed

---
## [2.0.0] — 2026-05-20

### Breaking
- Button: `appearance` → `variant`
- Modal: `size="small"|"medium"|"large"` → `size="sm"|"md"|"lg"`
- Tokens: `--color-blue-*` → `--color-primary-*`
---

---
## 7. Consumo em Projetos

### Publicação como npm Package
// package.json (do Design System)
{
"name": "@empresa/design-system",
"version": "2.1.0",
"main": "dist/cjs/index.js",
"module": "dist/esm/index.js",
"types": "dist/types/index.d.ts",

---
## 8. Manutenção

### Governance
Equipe de Design System (DS Squad):
┌─────────────────────────────────────────────────────┐
│                     DS SQUAD                         │
├───────────────────┬─────────────────────────────────┤
│  Core Team        │  Contributors                    │
│  (dedicado)       │  (de cada squad)                 │
├───────────────────┼─────────────────────────────────┤

---
## Como contribuir com um novo componente

1. **RFC**: Abra uma RFC no repositório do DS
- Problema que resolve
- Alternativas consideradas
- Mockup / protótipo
2. **Review**: DS Squad revisa a RFC em até 1 semana
3. **Implementação**:
- Componente + stories + specs + testes
- Tokens se necessário

---
## 9. Design System no Enterprise

### Escalabilidade
Sem DS:                          Com DS:
┌───┐ ┌───┐ ┌───┐               ┌──────────────────────┐
│P1  │ │P2  │ │P3  │              │      Design System   │
│    │ │    │ │    │              │                      │
│azul│ │azul│ │roxo│              │ primary: azul        │
│8px │ │12px│ │8px │              │ spacing: 8px base    │
│sm  │ │md  │ │sm  │              │ radius: 8px          │

---
## 10. Implementação Prática

Vamos configurar um Design System básico com **React + TypeScript + Storybook + tokens**.
### Setup inicial
# 1. Criar monorepo
mkdir my-design-system && cd my-design-system
pnpm init
# 2. Instalar dependências
pnpm add react react-dom
pnpm add -D typescript @types/react @types/react-dom

---
