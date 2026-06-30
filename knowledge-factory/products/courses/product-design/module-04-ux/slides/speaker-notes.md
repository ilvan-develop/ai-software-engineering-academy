## Introducao

# Módulo 04 — UX: Experiência do Usuário
**Design centrado no usuário não é opcional — é o que separa produtos que vendem de produtos que acumulam poeira.**
---

---
## 1. O que é UX?

UX (User Experience) é a **percepção geral que uma pessoa tem ao interagir com um produto, sistema ou serviço**. Não se trata apenas de telas bonitas — envolve emoções, eficiência, acessibilidade e satisfação.
### UX vs UI
UX                                        UI
Experiência completa                      Superfície visual
"Como o usuário se sente?"               "Como o produto se parece?"
Pesquisa, arquitetura, fluxo             Cores, tipografia, ícones
Funcionalidade e usabilidade             Estética e identidade
Ciência + Design                         Design + Arte

---
## 2. Pesquisa com Usuários

Pesquisa não é opcional — é o que impede você de construir a feature errada.
### Entrevistas
❌ "Você usaria um botão de exportar CSV?"
✅ "Me conta como você faz para gerar relatórios hoje."
**Estrutura de uma entrevista:**
1. Abertura (5min) — "Não estamos testando você, queremos aprender"
2. Contexto (10min) — "Me conta seu dia a dia com..."
3. Tarefa (15min) — "Você pode tentar fazer X enquanto pensa em voz alta?"

---
## 3. Arquitetura da Informação (IA)

Arquitetura da Informação é a **organização estrutural do conteúdo** — como as informações são categorizadas, rotuladas e navegadas.
### Os 4 componentes da IA
1. ORGANIZAÇÃO      — Como o conteúdo é agrupado
├── Hierárquica  (ex: categorias e subcategorias)
├── Sequencial   (ex: wizard de cadastro)
└── Matricial    (ex: tags, filtros)
2. NAVEGAÇÃO        — Como o usuário se movimenta
├── Global       (menu principal)

---
## 4. Jornada do Usuário

A jornada mapeia **cada passo que o usuário dá** ao interagir com o produto, incluindo emoções, canais e pontos de dor.
### User Journey Map
FASE          AÇÕES                   EMOÇÃO     OPORTUNIDADE
─────────     ─────────────────────   ─────────   ─────────────────
DESCOBERTA    "Pesquisei 'SaaS CRM'"  😕 Confuso  SEO melhor
"Li review no Google"   🤔 Curioso  Comparativo claro
"Acessei landing page"  😐 Neutro   CTAs mais claros
AVALIAÇÃO     "Preenchi formulário"   😤 Irritado Formulário menor

---
## 5. Personas

Personas são **personagens fictícios baseados em dados reais** que representam segmentos de usuários.
### Proto-personas vs Data-driven
Proto-persona                        Data-driven persona
Baseada em hipóteses do time         Baseada em dados reais
Rápida (1 workshop)                  Leva semanas
"Eu acho que o usuário..."           "Os dados mostram que..."
Valida: "Erramos, vamos pesquisar"   Valida: "Confirmamos nossas hipóteses"
### Estrutura de uma persona

---
## 6. Acessibilidade (a11y)

Acessibilidade não é um plus — é **requisito legal e moral**. No Brasil, a **Lei Brasileira de Inclusão (LBI)** exige que sites e apps sejam acessíveis.
### WCAG (Web Content Accessibility Guidelines)
As diretrizes se organizam em 4 princípios:
P
├── Perceptível     — O conteúdo deve ser percebível
│   ├── Alternativas textuais para imagens
│   ├── Legendas para vídeos
│   └── Contraste suficiente

---
## 7. UX Writing

UX Writing é a **criação de textos para interfaces** que guiam o usuário de forma clara e humana.
### Microtexto
// ❌ Texto focado no sistema
"Erro 0x87E50007: Falha na autenticação do certificado"
// ✅ Texto focado no usuário
"Seu login expirou. Faça login novamente para continuar."
// ❌ Técnico e genérico
"Requisição inválida"

---
## 8. Heurísticas de Nielsen

As 10 heurísticas são **critérios de usabilidade** que funcionam como checklist para avaliar qualquer interface.
### As 10 Heurísticas
1. VISIBILIDADE DO STATUS DO SISTEMA
"O sistema deve sempre informar o que está acontecendo."
❌ Clica em "Salvar" e nada acontece por 10s
✅ Spinner + "Salvando..." + "Salvo!" com timestamp
2. CORRESPONDÊNCIA COM O MUNDO REAL
"Use linguagem do usuário, não do sistema."

---
## 9. UX para Devs

### Mentalidade centrada no usuário
ANTES                             DEPOIS
"O usuário vai aprender"          "Como tornar isso intuitivo?"
"Está no requisito"              "O usuário realmente precisa disso?"
"Funciona no meu ambiente"       "Funciona para o usuário real?"
"O design está errado"           "Qual problema estamos resolvendo?"
### Como colaborar com designers
| Situação | Faça | Não faça |

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
## Antes do deploy

- [ ] Testei com teclado apenas (sem mouse)
- [ ] Testei com zoom de 200%
- [ ] Textos estão consistentes (mesmo label para mesma ação)
- [ ] Performance: < 3s para carregar (mobile)
### Exemplo prático: refatorando uma feature com mentalidade UX
// ❌ Antes: feature-centrica
function TelaRelatorios() {
const [relatorios] = useQuery(GET_RELATORIOS);

---
## Resumo

| Tópico | Principal aprendizado |
|--------|-----------------------|
| UX vs UI | UX é a experiência completa; UI é a superfície visual |
| 5 Planos | Estratégia → Escopo → Estrutura → Esqueleto → Superfície |
| Pesquisa | Entreviste para entender, não para validar |
| IA | Organize conteúdo como o usuário espera |
| Jornada | Mapeie emoções, não só cliques |
| Personas | Baseie em dados, não em achismo |

---
