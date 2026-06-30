# Quiz — Módulo 07

## Pergunta 1

Qual a diferença entre um Style Guide e um Design System?

- a) Style Guide é digital, Design System é impresso
- b) Style Guide é apenas o guia visual (cores, tipografia), enquanto o Design System inclui componentes, processos, documentação e tooling
- c) Style Guide é para designers, Design System é para devs
- d) Não há diferença — são sinônimos

**Resposta:** b

---

## Pergunta 2

No Atomic Design, qual a ordem correta dos níveis de complexidade?

- a) Páginas → Templates → Organismos → Moléculas → Átomos
- b) Átomos → Moléculas → Organismos → Templates → Páginas
- c) Átomos → Organismos → Moléculas → Templates → Páginas
- d) Moléculas → Átomos → Organismos → Páginas → Templates

**Resposta:** b

---

## Pergunta 3

O que são Design Tokens?

- a) Criptomoedas usadas para pagar designers
- b) Variáveis visuais que representam decisões de design (cores, tipografia, spacing)
- c) Componentes React pré-prontos
- d) Arquivos de configuração do Storybook

**Resposta:** b

---

## Pergunta 4

Qual versão SemVer você usaria para uma mudança que **remove uma prop** existente de um componente?

- a) PATCH (ex: 1.0.0 → 1.0.1)
- b) MINOR (ex: 1.0.0 → 1.1.0)
- c) MAJOR (ex: 1.0.0 → 2.0.0)
- d) Nenhuma — props podem ser removidas sem versionamento

**Resposta:** c

---

## Pergunta 5

Qual ferramenta é a mais utilizada para documentar componentes de Design System de forma interativa?

- a) Figma
- b) Storybook
- c) Swagger
- d) Notion

**Resposta:** b

---

## Pergunta 6

Para que o tree-shaking funcione corretamente ao consumir um Design System, é necessário:

- a) Usar CommonJS (require)
- b) Definir `"sideEffects": false` no package.json e usar exports individuais
- c) Compilar tudo em um único arquivo bundle.js
- d) Instalar o pacote globalmente

**Resposta:** b

---

## Pergunta 7

O que é uma breaking change em um Design System?

- a) Qualquer alteração em qualquer componente
- b) Uma mudança que quebra a compatibilidade com versões anteriores (ex: renomear prop, remover componente)
- c) Apenas mudanças visuais
- d) Correções de bugs

**Resposta:** b

---

## Pergunta 8

Qual estratégia de versionamento permite adicionar novas variantes a um componente sem quebrar projetos existentes?

- a) MAJOR — sempre quebra tudo
- b) MINOR — adiciona funcionalidade de forma backward-compatible
- c) PATCH — qualquer mudança
- d) Nenhuma — toda mudança requer nova MAJOR

**Resposta:** b

---

## Pergunta 9

Em um Design System Enterprise, qual o benefício de usar CSS Custom Properties (variáveis CSS) para os tokens?

- a) Permite que projetos consumidores sobrescrevam tokens sem modificar a biblioteca
- b) É mais rápido que CSS Modules
- c) Elimina a necessidade de JavaScript
- d) Funciona apenas no Google Chrome

**Resposta:** a

---

## Pergunta 10

Qual o principal ROI de um Design System em uma organização com múltiplos produtos?

- a) Redução do time de design para zero
- b) Consistência visual, redução de retrabalho, aceleração do desenvolvimento e onboarding mais rápido
- c) Eliminação da necessidade de testes de UI
- d) Aumento do número de bugs para justificar o DS

**Resposta:** b
