---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 04 — UX: Experiência do Usuário

## Módulo 04 - UX: Experiência do Usuário

---
## 1. O que é UX?

- UX (User Experience) é a **percepção geral que uma pessoa tem ao interagir com um produto, sistema ou serviço**. Não ...
- UX                                        UI
- Experiência completa                      Superfície visual
- "Como o usuário se sente?"               "Como o produto se parece?"
- Pesquisa, arquitetura, fluxo             Cores, tipografia, ícones

---
## 2. Pesquisa com Usuários

- Pesquisa não é opcional — é o que impede você de construir a feature errada.
- ❌ "Você usaria um botão de exportar CSV?"
- ✅ "Me conta como você faz para gerar relatórios hoje."
- Estrutura de uma entrevista:**
- 1. Abertura (5min) — "Não estamos testando você, queremos aprender"

---
## 3. Arquitetura da Informação (IA)

- Arquitetura da Informação é a **organização estrutural do conteúdo** — como as informações são categorizadas, rotulad...
- 1. ORGANIZAÇÃO      — Como o conteúdo é agrupado
- ├── Hierárquica  (ex: categorias e subcategorias)
- ├── Sequencial   (ex: wizard de cadastro)
- └── Matricial    (ex: tags, filtros)

---
## 4. Jornada do Usuário

- A jornada mapeia **cada passo que o usuário dá** ao interagir com o produto, incluindo emoções, canais e pontos de dor.
- FASE          AÇÕES                   EMOÇÃO     OPORTUNIDADE
- ─────────     ─────────────────────   ─────────   ─────────────────
- DESCOBERTA    "Pesquisei 'SaaS CRM'"  😕 Confuso  SEO melhor
- "Li review no Google"   🤔 Curioso  Comparativo claro

---
## 5. Personas

- Personas são **personagens fictícios baseados em dados reais** que representam segmentos de usuários.
- Proto-persona                        Data-driven persona
- Baseada em hipóteses do time         Baseada em dados reais
- Rápida (1 workshop)                  Leva semanas
- "Eu acho que o usuário..."           "Os dados mostram que..."

---
## 6. Acessibilidade (a11y)

- Acessibilidade não é um plus — é **requisito legal e moral**. No Brasil, a **Lei Brasileira de Inclusão (LBI)** exige...
- As diretrizes se organizam em 4 princípios:
- P
- ├── Perceptível     — O conteúdo deve ser percebível
- │   ├── Alternativas textuais para imagens

---
## 7. UX Writing

- UX Writing é a **criação de textos para interfaces** que guiam o usuário de forma clara e humana.
- // ❌ Texto focado no sistema
- "Erro 0x87E50007: Falha na autenticação do certificado"
- // ✅ Texto focado no usuário
- "Seu login expirou. Faça login novamente para continuar."

---
## 8. Heurísticas de Nielsen

- As 10 heurísticas são **critérios de usabilidade** que funcionam como checklist para avaliar qualquer interface.
- 1. VISIBILIDADE DO STATUS DO SISTEMA
- "O sistema deve sempre informar o que está acontecendo."
- ❌ Clica em "Salvar" e nada acontece por 10s
- ✅ Spinner + "Salvando..." + "Salvo!" com timestamp

---
## 9. UX para Devs

- ANTES                             DEPOIS
- "O usuário vai aprender"          "Como tornar isso intuitivo?"
- "Está no requisito"              "O usuário realmente precisa disso?"
- "Funciona no meu ambiente"       "Funciona para o usuário real?"
- "O design está errado"           "Qual problema estamos resolvendo?"

---
## Antes de codificar

- [ ] Entendi o problema do usuário (não só a solução)
- [ ] Verifiquei se existem dados/entrevistas que embasam a demanda
- [ ] Questionei: "essa é a melhor forma de resolver?"

---
## Durante o código

- [ ] Componentes são acessíveis (teclado, screen reader)
- [ ] Mensagens de erro são humanas e acionáveis
- [ ] Estados vazios, loading e erro estão tratados
- [ ] Contraste mínimo 4.5:1
- [ ] Microinterações informam o status do sistema

---
## Exemplo: text

```text
UX                                        UI
Experiência completa                      Superfície visual
"Como o usuário se sente?"               "Como o produto se parece?"
Pesquisa, arquitetura, fluxo             Cores, tipografia, ícones
Funcionalidade e usabilidade             Estética e identidade
Ciência + Design                         Design + Arte
```

---
## Exemplo: text

```text
┌─────────────────────────────────────────────┐
│ 5. SUPERFÍCIE      Visual Design            │  ← UI, cores, ícones
├─────────────────────────────────────────────┤
│ 4. ESQUELETO       Interface / Navegação    │  ← Layout, botões, inputs
├─────────────────────────────────────────────┤
│ 3. ESTRUTURA       Interação / Info Arch    │  ← Fluxos, jornadas
├─────────────────────────────────────────────┤
│ 2. ESCOPO          Funcionalidades          │  ← Features, conteúdo
├─────────────────────────────────────────────┤
│ 1. ESTRATÉGIA      Necessidades do negócio  │  ← Objetivos, dores
└─────────────────────────────────────────────┘
```

---
## Recap

- 1. O que é UX?
- 2. Pesquisa com Usuários
- 3. Arquitetura da Informação (IA)
- 4. Jornada do Usuário
- 5. Personas
- 6. Acessibilidade (a11y)
- 7. UX Writing
- 8. Heurísticas de Nielsen
- 9. UX para Devs
- Antes de codificar
- Durante o código

---
# Obrigado!

## Perguntas?
