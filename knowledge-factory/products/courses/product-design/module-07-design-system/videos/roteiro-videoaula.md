# Roteiro de Videoaula — Módulo 07 — Design System: Consistência em Escala

**Duracao total estimada:** 34 minutos
**Formato:** Videoaula gravada / Streaming
**Publico-alvo:** Desenvolvedores intermediarios

---

## Visao Geral do Video

| Item | Detalhe |
|------|---------|
| Titulo | Módulo 07 — Design System: Consistência em Escala |
| Duracao | 34 min |
| Cenas | 13 |
| Formato | Expositivo com demonstracao pratica |
| Nivel | Intermediario |

---

## Roteiro por Cena

### Cena 1 — INTRO

**Duracao:** 1:30

**Narracao:**
> Ola! Nesta aula vamos explorar: Módulo 07 — Design System: Consistência em Escala. Ao final, voce vai entender os conceitos fundamentais e como aplica-los na pratica. Vamos la?

**Visuais:**
- Tela de abertura com titulo do modulo. Animacao suave com o nome do curso.

**Texto na tela:**
```
[TITULO] Módulo 07 — Design System: Consistência em Escala
```

**Notas de direcao:**
- Tom energico e convidativo. Apresentar o problema que sera resolvido.

---

### Cena 2 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 1. O que é Design System. Design System é um **conjunto integrado de padrões, componentes, diretrizes e ferramentas** que orientam a criação de interfaces digitais de forma consistente e escalável. Style Guide:                    Component Library:              Design System: "Guia de estilos"               "Biblioteca de componentes"    "Sistema integrado" ─────────────────────           ─────────────────────           ────────────────────

**Visuais:**
- Slides com topicos-chave. ```typescript
interface DesignSystemPurpose {
  consistencia:  'Mesma aparência e comportamento em todo o ecossistema';
  eficiencia:    'Devs e designers produzem mais rápido, sem recriar o óbvio';
  escalabilidade:'Novos produtos/heranças adotam o sistema sem retrabalho';
  qualidade:     'Componentes testados, acessíveis, documentados';
  colaboracao:   'Linguagem comum entre devs, designers, PMs, QA';
}
```

**Texto na tela:**
```
[1. O que é Design System]
```

**Notas de direcao:**
- Secao 2 de 10. Usar exemplos praticos.

---

### Cena 3 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 2. Atomic Design. Criado por **Brad Frost**, o Atomic Design é uma metodologia que divide interfaces em **níveis hierárquicos** de complexidade. Átomos ─→ Moléculas ─→ Organismos ─→ Templates ─→ Páginas │            │             │             │            │ │          Combina       Junta         Define       Aplica

**Visuais:**
- Slides com topicos-chave. ```typescript
interface DesignSystemPurpose {
  consistencia:  'Mesma aparência e comportamento em todo o ecossistema';
  eficiencia:    'Devs e designers produzem mais rápido, sem recriar o óbvio';
  escalabilidade:'Novos produtos/heranças adotam o sistema sem retrabalho';
  qualidade:     'Componentes testados, acessíveis, documentados';
  colaboracao:   'Linguagem comum entre devs, designers, PMs, QA';
}
```

**Texto na tela:**
```
[2. Atomic Design]
```

**Notas de direcao:**
- Secao 3 de 10. Usar exemplos praticos.

---

### Cena 4 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 3. Design Tokens. Design Tokens são as **variáveis visuais** do sistema. Eles abstraem decisões de design em valores únicos e reutilizáveis. // tokens/colors.ts export const colors = { brand: {

**Visuais:**
- Slides com topicos-chave. ```typescript
interface DesignSystemPurpose {
  consistencia:  'Mesma aparência e comportamento em todo o ecossistema';
  eficiencia:    'Devs e designers produzem mais rápido, sem recriar o óbvio';
  escalabilidade:'Novos produtos/heranças adotam o sistema sem retrabalho';
  qualidade:     'Componentes testados, acessíveis, documentados';
  colaboracao:   'Linguagem comum entre devs, designers, PMs, QA';
}
```

**Texto na tela:**
```
[3. Design Tokens]
```

**Notas de direcao:**
- Secao 4 de 10. Usar exemplos praticos.

---

### Cena 5 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 4. Componentes. Componentes são a **implementação concreta** dos tokens. Cada componente deve ser: Padronizado** — props consistentes entre componentes Documentado** — spec, variantes, exemplos Acessível** — ARIA, teclado, contraste

**Visuais:**
- Slides com topicos-chave. ```typescript
interface DesignSystemPurpose {
  consistencia:  'Mesma aparência e comportamento em todo o ecossistema';
  eficiencia:    'Devs e designers produzem mais rápido, sem recriar o óbvio';
  escalabilidade:'Novos produtos/heranças adotam o sistema sem retrabalho';
  qualidade:     'Componentes testados, acessíveis, documentados';
  colaboracao:   'Linguagem comum entre devs, designers, PMs, QA';
}
```

**Texto na tela:**
```
[4. Componentes]
```

**Notas de direcao:**
- Secao 5 de 10. Usar exemplos praticos.

---

### Cena 6 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 5. Documentação. Documentação é o que **transforma uma biblioteca de componentes em um Design System**. Storybook é a ferramenta mais popular para documentar, testar e explorar componentes visualmente. // components/Button/Button.stories.ts import type { Meta, StoryObj } from '@storybook/react';

**Visuais:**
- Slides com topicos-chave. ```typescript
interface DesignSystemPurpose {
  consistencia:  'Mesma aparência e comportamento em todo o ecossistema';
  eficiencia:    'Devs e designers produzem mais rápido, sem recriar o óbvio';
  escalabilidade:'Novos produtos/heranças adotam o sistema sem retrabalho';
  qualidade:     'Componentes testados, acessíveis, documentados';
  colaboracao:   'Linguagem comum entre devs, designers, PMs, QA';
}
```

**Texto na tela:**
```
[5. Documentação]
```

**Notas de direcao:**
- Secao 6 de 10. Usar exemplos praticos.

---

### Cena 7 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: Button — Especificação Técnica. | Prop | Type | Default | Description | |------|------|---------|-------------| | variant | `'primary' \| 'secondary' \| 'outline' \| 'ghost' \| 'danger'` | `'primary'` | Estilo visual do botão | | size | `'sm' \| 'md' \| 'lg'` | `'md'` | Tamanho do botão |

**Visuais:**
- Slides com topicos-chave. ```typescript
interface DesignSystemPurpose {
  consistencia:  'Mesma aparência e comportamento em todo o ecossistema';
  eficiencia:    'Devs e designers produzem mais rápido, sem recriar o óbvio';
  escalabilidade:'Novos produtos/heranças adotam o sistema sem retrabalho';
  qualidade:     'Componentes testados, acessíveis, documentados';
  colaboracao:   'Linguagem comum entre devs, designers, PMs, QA';
}
```

**Texto na tela:**
```
[Button — Especificação Técnica]
```

**Notas de direcao:**
- Secao 7 de 10. Usar exemplos praticos.

---

### Cena 8 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 6. Versionamento. Design Systems evoluem. Versionamento garante que **mudanças sejam previsíveis e seguras**. MAJOR.MINOR.PATCH MAJOR (1.x.x → 2.0.0): Breaking changes — componente renomeado, prop removida, token alterado

**Visuais:**
- Slides com topicos-chave. ```typescript
interface DesignSystemPurpose {
  consistencia:  'Mesma aparência e comportamento em todo o ecossistema';
  eficiencia:    'Devs e designers produzem mais rápido, sem recriar o óbvio';
  escalabilidade:'Novos produtos/heranças adotam o sistema sem retrabalho';
  qualidade:     'Componentes testados, acessíveis, documentados';
  colaboracao:   'Linguagem comum entre devs, designers, PMs, QA';
}
```

**Texto na tela:**
```
[6. Versionamento]
```

**Notas de direcao:**
- Secao 8 de 10. Usar exemplos praticos.

---

### Cena 9 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: Breaking Changes. Antes:** <Button appearance="primary" /> Depois:** <Button variant="primary" />

**Visuais:**
- Slides com topicos-chave. ```typescript
interface DesignSystemPurpose {
  consistencia:  'Mesma aparência e comportamento em todo o ecossistema';
  eficiencia:    'Devs e designers produzem mais rápido, sem recriar o óbvio';
  escalabilidade:'Novos produtos/heranças adotam o sistema sem retrabalho';
  qualidade:     'Componentes testados, acessíveis, documentados';
  colaboracao:   'Linguagem comum entre devs, designers, PMs, QA';
}
```

**Texto na tela:**
```
[Breaking Changes]
```

**Notas de direcao:**
- Secao 9 de 10. Usar exemplos praticos.

---

### Cena 10 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: [2.1.0] — 2026-06-15. Novo componente: `Tooltip` Button: nova prop `leftIcon` e `rightIcon` Modal: nova variante `size="xl"` Input: cor de foco agora usa token primary ao invés de blue-500 fixo

**Visuais:**
- Slides com topicos-chave. ```typescript
interface DesignSystemPurpose {
  consistencia:  'Mesma aparência e comportamento em todo o ecossistema';
  eficiencia:    'Devs e designers produzem mais rápido, sem recriar o óbvio';
  escalabilidade:'Novos produtos/heranças adotam o sistema sem retrabalho';
  qualidade:     'Componentes testados, acessíveis, documentados';
  colaboracao:   'Linguagem comum entre devs, designers, PMs, QA';
}
```

**Texto na tela:**
```
[[2.1.0] — 2026-06-15]
```

**Notas de direcao:**
- Secao 10 de 10. Usar exemplos praticos.

---

### Cena 11 — CODE-DEMO

**Duracao:** 4:00

**Narracao:**
> Vamos ver na pratica como isso funciona. Observe este codigo em text:

**Visuais:**
- Tela dividida: editor de codigo a esquerda, terminal/output a direita.

**Texto na tela:**
```
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
```

**Notas de direcao:**
- Explicar linha por linha. Destacar pontos importantes com zoom ou realce.

---

### Cena 12 — SUMMARY

**Duracao:** 1:30

**Narracao:**
> Recapitulando: vimos 1. O que é Design System, 2. Atomic Design, 3. Design Tokens, 4. Componentes, 5. Documentação, Button — Especificação Técnica. Esses conceitos sao fundamentais para sua formacao.

**Visuais:**
- Lista resumida com icones. Transicao suave para encerramento.

**Texto na tela:**
```
✓ 1. O que é Design System
✓ 2. Atomic Design
✓ 3. Design Tokens
✓ 4. Componentes
✓ 5. Documentação
✓ Button — Especificação Técnica
```

**Notas de direcao:**
- Reforcar os aprendizados principais. Conectar com o proximo modulo.

---

### Cena 13 — OUTRO

**Duracao:** 0:30

**Narracao:**
> Na proxima aula, vamos aprofundar esses conceitos. Nao perca!

**Visuais:**
- Tela final com links, inscricao, e teaser da proxima aula.

**Texto na tela:**
```
Proximo modulo: [TITULO DO PROXIMO MODULO]
```

**Notas de direcao:**
- Chamada para acao: inscrever-se, comentar, compartilhar.

---

## Checklist de Producao

- [ ] Roteiro revisado
- [ ] Slides preparados
- [ ] Ambiente de codigo configurado
- [ ] Microfone testado
- [ ] Gravacao de tela configurada (1920x1080)
- [ ] Exemplos de codigo testados
- [ ] Legendas geradas
- [ ] Thumbnail criada
- [ ] Descricao e tags preenchidas
- [ ] Capitulos do video marcados

---

## Sugestoes de Thumbnail

- Texto: 'Módulo 07 '
- Cor de fundo: azul escuro (#1a2332)
- Destaque: codigo ou diagrama ao fundo
- Rosto do apresentador no canto inferior direito

---

## SEO

**Titulo:** Módulo 07 — Design System: Consistência em Escala | Arquitetura Enterprise
**Descricao:** Aprenda módulo 07 — design system: consistência em escala. Nesta aula abordamos conceitos fundamentais com exemplos praticos em TypeScript.
**Tags:** arquitetura, software, enterprise, typescript, desenvolvimento
