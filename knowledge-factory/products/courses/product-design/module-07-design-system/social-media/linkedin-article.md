# Módulo 07 - Design System: Consistência em Escala

---

## 1. O que é Design System

Design System é um **conjunto integrado de padrões, componentes, diretrizes e ferramentas** que orientam a criação de interfaces digitais de forma consistente e escalável.
### Design System vs Style Guide vs Component Library
Style Guide:                    Component Library:              Design System:
"Guia de estilos"               "Biblioteca de componentes"    "Sistema integrado"

## 2. Atomic Design

Criado por **Brad Frost**, o Atomic Design é uma metodologia que divide interfaces em **níveis hierárquicos** de complexidade.
### Os 5 níveis
Átomos ─→ Moléculas ─→ Organismos ─→ Templates ─→ Páginas
│            │             │             │            │

## 3. Design Tokens

Design Tokens são as **variáveis visuais** do sistema. Eles abstraem decisões de design em valores únicos e reutilizáveis.
### Definição em TypeScript
// tokens/colors.ts
export const colors = {

## 4. Componentes

Componentes são a **implementação concreta** dos tokens. Cada componente deve ser:
- **Padronizado** — props consistentes entre componentes
- **Documentado** — spec, variantes, exemplos
- **Acessível** — ARIA, teclado, contraste

## 5. Documentação

Documentação é o que **transforma uma biblioteca de componentes em um Design System**.
### Storybook
Storybook é a ferramenta mais popular para documentar, testar e explorar componentes visualmente.
// components/Button/Button.stories.ts

## Button — Especificação Técnica

### Props
| Prop | Type | Default | Description |
|------|------|---------|-------------|
| variant | `'primary' \| 'secondary' \| 'outline' \| 'ghost' \| 'danger'` | `'primary'` | Estilo visual do botão |

---
*Este artigo faz parte da formacao Arquitetura de Software Enterprise com IA*