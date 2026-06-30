# Exercícios — Módulo 04

## Exercício 1: Classificando problemas com os 5 Planos de Garrett

Para cada situação abaixo, identifique **qual plano de Garrett** o problema pertence (Estratégia, Escopo, Estrutura, Esqueleto ou Superfície) e justifique:

```text
1. (  ) Usuários não encontram a opção "Criar relatório" — ela está no 3º nível do menu
2. (  ) O time não sabe qual problema de negócio está resolvendo
3. (  ) O botão "Salvar" tem padding de 2px, difícil de clicar no mobile
4. (  ) A feature de exportar CSV foi construída, mas ninguém pediu
5. (  ) Usuários demoram 4 minutos para completar um cadastro porque pulam entre 8 telas desconexas
6. (  ) A logo ocupa 40% da tela, empurrando o conteúdo principal para baixo do fold
7. (  ) O campo de busca filtra resultados, mas não há indicador de quantos resultados existem
8. (  ) O design system usa 4 variações de azul, mas nenhuma comunica "erro" ou "alerta"
```

---

## Exercício 2: Criando um roteiro de teste de usabilidade

Você é dev em um SaaS de gestão financeira para PMEs. O time acabou de implementar a **tela de conciliação bancária** (importar extrato → categorizar → reconciliar). O designer quer testar com 5 usuários antes do deploy.

Crie:

**a)** **3 tarefas** para o teste de usabilidade, cada uma com:
- Instrução para o usuário (em linguagem natural, sem jargão)
- Critério de sucesso mensurável
- O que observar (indicadores de dificuldade)

**b)** Uma **escala SUS** (System Usability Scale) simplificada com 5 afirmações que os usuários devem pontuar de 1 (discordo totalmente) a 5 (concordo totalmente)

**c)** Instruções para o moderador sobre o que **não** fazer durante o teste (pelo menos 3 regras)

Formato sugerido:

```typescript
interface TestTask {
  id: string;
  instrucao: string;
  criterioSucesso: string;
  observar: string[];
}

const tasks: TestTask[] = [
  // ...
];

interface SUSStatement {
  statement: string;
  type: 'positive' | 'negative'; // SUS alterna positivas e negativas
}
```

---

## Exercício 3: Card Sorting para reestruturar navegação

Uma plataforma de cursos online tem esta navegação atual:

```text
Home | Cursos | Meus Cursos | Professores | Comunidade | Blog | FAQ | Suporte | Sobre | Parcerias | Seja um Professor | Central de Ajuda | Configurações | Minha Conta | Sair
```

O time percebeu que usuários demoram para encontrar opções. A taxa de cliques nos itens de navegação é baixa (média de 1.2 itens por sessão).

**a)** Realize um **card sorting fechado** propondo uma nova arquitetura com no máximo 5 categorias principais. Distribua todos os links atuais nessas categorias.

**b)** Para cada categoria, defina um **label** claro e uma descrição do que o usuário encontra ali.

**c)** Explique por que sua organização é melhor que a atual, citando pelo menos 2 princípios de Arquitetura da Informação.

**d)** Proponha como isso ficaria em termos de rotas no frontend:

```typescript
// Exemplo
const routes = {
  '/': 'Home',
  '/cursos': 'Cursos',
  // ...
};
```

---

## Exercício 4: Avaliação heurística de uma tela real

Escolha uma tela de um produto que você usa no trabalho (ou um site famoso como Mercado Livre, Nubank, Pipefy, etc.). Analise-a contra as **10 heurísticas de Nielsen**.

Para cada heurística:

- **Nota** (0-4) de severidade
- **Problema encontrado** (ou "N/A" se não houver)
- **Sugestão de correção**

Use este formato:

```typescript
type Severity = 0 | 1 | 2 | 3 | 4;

interface HeuristicResult {
  heuristic: string;
  severity: Severity;
  problem: string;
  suggestion: string;
}
```

Entregue um array com 10 itens (um por heurística) identificando:
- Quais heurísticas estão violadas
- Qual a gravidade (justifique)
- Como você corrigiria (como dev)

---

## Exercício 5: Refatorando mensagens de erro com UX Writing

O backend da sua aplicação retorna estes erros:

```typescript
// Mensagens ATUAIS (retornadas pela API)
const currentErrors = {
  400: 'Bad Request',
  401: 'Unauthorized',
  403: 'Forbidden',
  404: 'Not Found',
  409: 'Conflict',
  422: 'Unprocessable Entity',
  429: 'Too Many Requests',
  500: 'Internal Server Error',
  502: 'Bad Gateway',
  503: 'Service Unavailable',
};
```

**a)** Reescreva cada mensagem seguindo os princípios de UX Writing (claro, conciso, útil, humano, consistente). Considere que o produto é um SaaS B2B de gestão de projetos.

```typescript
const improvedErrors: Record<number, { title: string; description: string }> = {
  // Exemplo:
  // 400: { title: 'Dados inválidos', description: 'Verifique os campos destacados e tente novamente.' },
  // ...
};
```

**b)** Crie um **componente React** que exiba essas mensagens de erro com:

- Ícone contextual (warning para 4xx, error para 5xx)
- Botão "Tentar novamente" para erros recuperáveis
- Suporte a `aria-live="polite"` para screen readers

```typescript
interface ErrorDisplayProps {
  statusCode: number;
  onRetry?: () => void;
}
```

**c)** Explique qual tom de voz foi usado para cada faixa de erro (4xx vs 5xx) e por quê.
