# Projeto Módulo 04 — Auditoria de UX e Refatoração

## Objetivo

Realizar uma **auditoria completa de UX** em um produto real (da sua empresa ou um open-source) e implementar melhorias baseadas nas heurísticas de Nielsen, acessibilidade WCAG e UX Writing.

## Contexto

Você é o dev responsável por melhorar a experiência do usuário em um **SaaS de gestão de tarefas** (ou escolha outro produto real que você usa no trabalho). O produto existe, tem funcionalidades, mas:

- Usuários reclamam que "é difícil de usar"
- O ticket médio de suporte é alto para tarefas simples
- A taxa de conversão (free → pago) é baixa
- Não há padronização de mensagens de erro
- A acessibilidade nunca foi considerada

Seu trabalho é **diagnosticar e propor correções** — e implementar as correções de código.

## Entregáveis

### 1. Persona e Jornada (documentação)

Crie:

- **1 data-driven persona** do usuário principal (baseada em dados reais ou suposições informadas)
- **1 anti-persona** (quem NÃO deve ser alvo)
- **User Journey Map** de uma tarefa crítica (ex: criar um projeto, convidar time, gerar relatório) com pelo menos 4 fases, identificando emoções e oportunidades
- **Service Blueprint** da mesma tarefa, mostrando backstage, frontstage e processos

### 2. Avaliação Heurística (documentação)

Avalie **3 telas principais** do produto usando as 10 heurísticas de Nielsen:

```
Tela 1: Dashboard / Home
Tela 2: Fluxo de criação/edição
Tela 3: Página de configurações
```

Para cada tela, entregue uma tabela:

| Heurística | Severidade (0-4) | Problema | Sugestão de correção |
|------------|------------------|----------|----------------------|
| 1. Status  | ...              | ...      | ...                  |
| 2. Mundo real | ...           | ...      | ...                  |
| ...        |                  |          |                      |

### 3. Auditoria de Acessibilidade (documentação + código)

Para as mesmas 3 telas, avalie:

- Contraste de cores (use ferramenta como WebAIM Contrast Checker)
- Navegação por teclado (consegue realizar todas as ações sem mouse?)
- HTML semântico (usa `<button>`, `<nav>`, `<main>`, `<label>`?)
- ARIA labels (ícones e ações sem texto têm label?)

Entregue uma tabela com:

| Tela | Problema de a11y | WCAG critério | Severidade | Correção |
|------|------------------|---------------|------------|----------|
| ...  | ...              | ...           | ...        | ...      |

### 4. Refatoração de Componentes (código)

Escolha **3 componentes** reais do produto e refatore para melhorar a UX:

**Componente 1 — Mensagens de erro**
```typescript
// Antes: mensagem genérica
// Algo deu errado

// Depois: mensagem clara + ação
<ErrorAlert
  title="Falha ao salvar"
  description="Verifique sua conexão e tente novamente."
  action="Tentar novamente"
  onAction={handleRetry}
/>
```

**Componente 2 — Botão de ação**
```typescript
// Antes: sem feedback de status
<button onClick={salvar}>Salvar</button>

// Depois: loading, success e error states
<Button
  variant="primary"
  loading={isSaving}
  success={isSaved}
  error={saveError}
  onClick={salvar}
>
  {isSaving ? 'Salvando...' : isSaved ? 'Salvo!' : 'Salvar'}
</Button>
```

**Componente 3 — Menu de navegação**
```typescript
// Antes: dropdown sem acessibilidade
// Depois: menu acessível com teclado
<nav aria-label="Navegação principal">
  <Menu>
    <MenuItem icon={DashboardIcon} href="/dashboard">Dashboard</MenuItem>
    <MenuItem icon={ProjectsIcon} href="/projetos">Projetos</MenuItem>
    <MenuItem icon={SettingsIcon} href="/configuracoes">Configurações</MenuItem>
  </Menu>
</nav>
```

Cada componente deve incluir:
- Estados: loading, vazio, erro, sucesso (quando aplicável)
- Acessibilidade: aria-labels, roles, tabIndex, foco visível
- UX Writing: mensagens claras e consistentes
- Teste rápido com teclado (documente o resultado)

### 5. Relatório Final

Compile tudo em um relatório com:

```
1. Resumo executivo (1 parágrafo)
2. Personas e Jornada
3. Avaliação heurística (3 telas)
4. Auditoria de acessibilidade
5. Código refatorado (3 componentes)
6. Próximos passos (top 3 prioridades)
```

## Critérios de avaliação

- [ ] Personas e anti-persona claras e baseadas em dados
- [ ] User Journey Map com emoções e oportunidades
- [ ] Service Blueprint com backstage e frontstage
- [ ] Avaliação heurística completa (10 heurísticas x 3 telas)
- [ ] Severidades justificadas
- [ ] Auditoria de acessibilidade com critérios WCAG
- [ ] 3 componentes refatorados com estados e a11y
- [ ] UX Writing aplicado em todas as mensagens
- [ ] Contraste mínimo 4.5:1 nos componentes
- [ ] Navegação por teclado funcional
- [ ] Relatório final compilado e organizado

## Extras (opcionais)

- Implementar um **tema de alto contraste** para usuários com baixa visão
- Criar um **teste automatizado de acessibilidade** (jest-axe ou axe-core)
- Conduzir o teste de usabilidade com 3 pessoas reais e documentar os resultados
- Propor um **sistema de feature flags** baseado em personas (como visto na aula)
