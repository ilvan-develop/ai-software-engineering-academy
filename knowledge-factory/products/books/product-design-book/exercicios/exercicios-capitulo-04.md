# Exercícios — Capítulo 4: Wireframes e Prototipação

> **Progressão:** Fácil → Médio → Difícil  
> **Total:** 4 exercícios

---

## Exercício 1 — Fácil: Identifique a Fidelidade

**Tema:** Níveis de fidelidade em protótipos

Classifique cada descrição como **Baixa**, **Média** ou **Alta** fidelidade:

| Descrição | Fidelidade |
|-----------|------------|
| Rabisco em papel com caixas e linhas | ? |
| Protótipo interativo no Figma com cores reais, tipografia e animações | ? |
| Wireframe digital em escala de cinza com espaçamentos definidos | ? |
| Esboço de tela feito em 5 minutos com caneta | ? |
| Layout funcional em código React com dados mockados | ? |

---

## Exercício 2 — Médio: Wireframe de Dashboard

**Tema:** Estruturar wireframe de baixa fidelidade

Desenhe (descreva) um wireframe de baixa fidelidade para um **dashboard de vendas** que deve conter:

1. Sidebar com navegação (5 itens)
2. Header com nome do usuário e notificações
3. Cards de métricas (4 cards: receita, pedidos, ticket médio, conversão)
4. Gráfico de vendas dos últimos 30 dias
5. Tabela de pedidos recentes (5 colunas, 10 linhas)

**Descreva:**
- Layout (grid, proporções)
- Hierarquia visual (o que é mais proeminente?)
- Onde cada elemento se encaixa
- Qual a jornada esperada do usuário

---

## Exercício 3 — Médio: Protótipo de Fluxo

**Tema:** Fluxo de telas conectadas

Descreva um protótipo funcional para o fluxo de **recuperação de senha**:

**Telas necessárias:**
1. Tela de login com link "Esqueci minha senha"
2. Tela de inserção de email
3. Tela de confirmação ("Email enviado")
4. Tela de redefinição de senha (email com link)
5. Tela de sucesso

**Para cada tela, descreva:**
- Elementos visuais
- Estados (carregando, erro, sucesso)
- Regras de validação
- Conexões entre telas (o que acontece ao clicar em cada botão)

---

## Exercício 4 — Difícil: Protótipo com Estados

**Tema:** Estados de componentes em protótipo

Crie a especificação para um **componente de upload de arquivo** com todos os estados:

**Estados obrigatórios:**
1. **Vazio** — "Arraste arquivo ou clique para selecionar"
2. **Arrastando** — feedback visual ao passar arquivo sobre a área
3. **Selecionando** — diálogo de seleção de arquivo aberto
4. **Carregando** — barra de progresso com percentual e nome do arquivo
5. **Sucesso** — check verde com nome do arquivo e tamanho
6. **Erro** — mensagem de erro (formato inválido, tamanho excedido, etc.)
7. **Múltiplos** — lista de arquivos com progresso individual
8. **Removendo** — animação de saída ao remover um arquivo

**Para cada estado:**
- Descrição visual (cores, ícones, texto)
- Comportamento (o que acontece ao interagir?)
- Tratamento de borda (e se o usuário clicar em cancelar durante o upload?)
