# Exercícios — Módulo 19

## Exercício 1: Classificando riscos

Classifique cada cenário como Blocker, Critical, Major ou Minor.

| # | Cenário | Classificação |
|---|---------|---------------|
| 1 | Senha armazenada em plain text | |
| 2 | Nome de variável em português | |
| 3 | Rota GET sem autenticação que retorna dados de todos os usuários | |
| 4 | Falta de documentação em 1 endpoint de 50 | |
| 5 | Query N+1 que adiciona 2s ao carregamento de uma página | |
| 6 | CSP header não configurado | |
| 7 | Função com 80 linhas (muito longa) | |
| 8 | Chave de API hardcoded no código | |
| 9 | Estilo inline em vez de classe CSS | |
| 10 | Migração de banco que dropa coluna sem verificar se há dados | |

---

## Exercício 2: Auditoria completa

Realize uma auditoria completa no cenário abaixo.

**Sistema:** API de autenticação

**Código identificado:**

```typescript
// auth.service.ts
async function login(email: string, senha: string) {
  const user = await prisma.user.findUnique({
    where: { email }
  });
  if (user.senha === senha) {
    const token = jwt.sign({ userId: user.id }, 'minha-chave-secreta');
    return { token };
  }
  throw new Error('Credenciais inválidas');
}
```

**Problemas a identificar:**

1. Liste todos os problemas de segurança
2. Classifique cada um (Blocker a Minor)
3. Proponha correções com código
4. Calcule o score geral

Formato:

```markdown
## Riscos Identificados

### [Gravidade] [Título]
- Localização:
- Descrição:
- Impacto:
- Correção:

## Score
[Score calculado com justificativa]
```

---

## Exercício 3: Criando checklists de auditoria

Para cada tipo de auditoria abaixo, crie 5 itens de checklist:

**Auditoria de Backend (NestJS):**
1. ...
2. ...
3. ...
4. ...
5. ...

**Auditoria de Frontend (Next.js):**
1. ...
2. ...
3. ...
4. ...
5. ...

**Auditoria de TypeScript:**
1. ...
2. ...
3. ...
4. ...
5. ...

---

## Exercício 4: Plano de ação

Dado o relatório de auditoria abaixo, crie um plano de ação priorizado:

```
Score geral: 4.2/10
Riscos: 2 Blocker, 3 Critical, 5 Major, 8 Minor

Blocker:
1. Upload de arquivos sem validação de tipo (RCE possível)
2. Refresh token não é invalidado no logout

Critical:
1. Logs expõem dados pessoais (CPF, email)
2. CORS configurado como *
3. SQL injection possível em 2 endpoints de busca

Major:
1. Dockerfile sem multi-stage (1.2GB)
2. Testes com cobertura de 23%
3. Sem health checks nos serviços
4. Variáveis de ambiente sem .env.example
5. Imagens sem lazy loading
```

Crie o plano:

| Prioridade | Ação | Responsável | Prazo | Esforço (horas) |
|------------|------|-------------|-------|-----------------|
| P0 | ... | ... | ... | ... |
| P1 | ... | ... | ... | ... |
| P2 | ... | ... | ... | ... |
| P3 | ... | ... | ... | ... |

---

## Exercício 5: Comparação de scores

Duas equipes entregaram o mesmo módulo. Compare os scores:

**Equipe A:**
- Arquitetura: 9, Segurança: 8, Código: 7, Performance: 6, Docs: 5
- Blocker: 0, Critical: 1, Major: 4

**Equipe B:**
- Arquitetura: 6, Segurança: 9, Código: 8, Performance: 8, Docs: 8
- Blocker: 0, Critical: 0, Major: 3

Responda:
1. Qual o score geral de cada equipe?
2. Qual equipe entrega o código mais seguro?
3. Qual equipe entrega o código mais arquiteturalmente sólido?
4. Considerando que o sistema lida com dados financeiros, qual equipe você aprovaria para deploy?
5. O que cada equipe precisa melhorar?
