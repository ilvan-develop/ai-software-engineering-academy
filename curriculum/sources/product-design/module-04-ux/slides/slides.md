# Módulo 04 — Slides

---

## Slide 1: Título

**UX — Experiência do Usuário**
Design centrado no usuário para produtos enterprise

---

## Slide 2: UX vs UI

```text
UX                                        UI
"Como o usuário se sente?"               "Como o produto se parece?"
Pesquisa, arquitetura, fluxo             Cores, tipografia, ícones
Funcionalidade e usabilidade             Estética e identidade

UI sem UX: carro bonito sem motor
UX sem UI: motor sem carroceria
```markdown

---

## Slide 3: Os 5 Planos de Garrett

```text
┌─────────────────────────────────┐
│ 5. SUPERFÍCIE    Visual Design  │
├─────────────────────────────────┤
│ 4. ESQUELETO     Layout / Nav   │
├─────────────────────────────────┤
│ 3. ESTRUTURA     Fluxos / IA    │
├─────────────────────────────────┤
│ 2. ESCOPO        Funcionalidades│
├─────────────────────────────────┤
│ 1. ESTRATÉGIA    Negócio        │
└─────────────────────────────────┘
```markdown

Cada plano responde um "por quê" diferente

---

## Slide 4: Pesquisa com Usuários

| Técnica | O que responde | Esforço |
|---------|---------------|---------|
| Entrevista | "Qual o problema real?" | Alto |
| Teste de usabilidade | "O usuário consegue fazer?" | Alto |
| Card sorting | "Como organizar o conteúdo?" | Médio |
| Survey | "Quantos têm esse problema?" | Médio |
| Analytics | "O que os dados mostram?" | Baixo |

Regra de ouro: **comportamento passado** > intenção futura

---

## Slide 5: Estrutura da Entrevista

```text
1. Abertura (5min)
   "Não estamos testando você"

2. Contexto (10min)
   "Me conta seu dia a dia com..."

3. Tarefa (15min)
   "Pense em voz alta enquanto faz X"

4. Exploração (10min)
   "Por que você fez isso?"

5. Fechamento (5min)
   "Algo mais?"
```markdown

Fale 20%, ouça 80%. Nada de perguntas indutoras.

---

## Slide 6: Arquitetura da Informação

**4 componentes:**

```text
ORGANIZAÇÃO   → Como o conteúdo é agrupado
NAVEGAÇÃO     → Como o usuário se movimenta
LABELING      → Nomes e rótulos (consistência > criatividade)
BUSCA         → Sistema de busca interna
```text

**Para devs:** URLs refletem sua IA

```javascript
❌ /products/list?type=all
✅ /produtos
✅ /minha-conta/pedidos
```markdown

---

## Slide 7: Jornada do Usuário

```text
FASE          AÇÕES                   EMOÇÃO
─────────     ──────────────           ─────────
DESCOBERTA    "Pesquisei soluções"     🤔 Curioso
AVALIAÇÃO     "Testei 14 dias"         😊 Animado
ATIVAÇÃO      "Configurei o time"      😰 Ansioso
RETENÇÃO      "Uso diário"             😍 Leal
```markdown

Service Blueprint: inclui o backstage (API, jobs, integrações)

---

## Slide 8: Personas

```text
Proto-persona                    Data-driven persona
Baseada em hipóteses             Baseada em dados reais
Rápida (1 workshop)              Leva semanas
"Eu acho que..."                 "Os dados mostram..."
```text

**Anti-persona:** quem NÃO é seu público
- Gera custo, não receita
- Não projete para ele

---

## Slide 9: Acessibilidade — WCAG

```text
P ─ Perceptível     Alt text, legendas, contraste
O ─ Operável        Navegação por teclado
U ─ Compreensível   Idioma, erros claros
R ─ Robusto         Screen readers, HTML semântico
```text

| Nível | Obrigatório | Contraste |
|-------|-------------|-----------|
| A | Mínimo | 3:1 |
| AA | **Padrão legal** | **4.5:1** |
| AAA | Avançado | 7:1 |

---

## Slide 10: Acessibilidade na prática

```html
<!-- ❌ -->
<div onClick={salvar}>Salvar</div>
<img src="lupa.png" />

<!-- ✅ -->
<button onClick={salvar}>Salvar</button>
<img src="lupa.png" alt="Pesquisar" />
<button aria-label="Configurações">
  <i class="icon-cog"></i>
</button>
```markdown

Teste com **teclado** antes de testar com mouse

---

## Slide 11: UX Writing

```text
❌ "Erro 0x87E50007: Falha na autenticação"
✅ "Seu login expirou. Faça login novamente."

❌ "Requisição inválida"
✅ "Preencha todos os campos obrigatórios."
```text

| Princípio | Exemplo |
|-----------|---------|
| Claro | "Salvar" (não "Persistir") |
| Conciso | "E-mail inválido" |
| Humano | "Algo deu errado, mas já estamos cuidando" |
| Consistente | Sempre "Excluir", nunca "Apagar"/"Remover" |

---

## Slide 12: Heurísticas de Nielsen

As 10 mais importantes em 1 slide:

```text
1.  Status do sistema         → "Salvando..." + "Salvo!"
2.  Mundo real                → "Pasta principal" (não "diretório raiz")
3.  Controle e liberdade      → Desfazer sempre disponível
4.  Consistência              → Mesmo label, mesma ação
5.  Prevenção de erros        → Datepicker > campo livre
6.  Reconhecimento            → Dropdown > campo em branco
7.  Flexibilidade             → Atalhos para expert, wizard para novato
8.  Design minimalista        → 5 métricas, não 20 gráficos
9.  Mensagens de erro         → Claras e acionáveis
10. Ajuda e documentação      → "?" contextual + FAQ
```markdown

---

## Slide 13: Severidade de problemas

```text
0 ─ Não é problema
1 ─ Cosmético (arrumar se sobrar tempo)
2 ─ Menor (baixo impacto)
3 ─ Grave (deve corrigir)
4 ─ Catástrofe (usuário não consegue usar)
```markdown

**Exemplo real:** "Erro 500" sem mensagem = severidade 4

---

## Slide 14: UX para Devs — Colaboração

| Recebeu um design | Faça |
|-------------------|------|
| Antes de codificar | "Qual o fluxo do usuário?" |
| Conflito técnico | Mostre dados, não opiniões |
| Review de design | Aponte acessibilidade |
| Na entrega | Teste rápido de usabilidade |

**Checklist mental:**
- [ ] Funciona só com teclado?
- [ ] Mensagem de erro é humana?
- [ ] Estados de loading/erro/vazio tratados?
- [ ] Contraste 4.5:1?

---

## Slide 15: Recado Final

```text
UX não é responsabilidade do designer.
É responsabilidade do time inteiro.

Cada componente que você cria,
cada mensagem de erro que você escreve,
cada fluxo que você implementa:

Isso é UX.
```text

Pergunte antes de codificar: **"Isso resolve o problema do usuário?"**
