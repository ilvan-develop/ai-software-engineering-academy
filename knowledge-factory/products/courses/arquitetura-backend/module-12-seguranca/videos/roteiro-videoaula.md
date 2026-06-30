# Roteiro de Videoaula — Módulo 12 — Segurança

**Duracao total estimada:** 34 minutos
**Formato:** Videoaula gravada / Streaming
**Publico-alvo:** Desenvolvedores intermediarios

---

## Visao Geral do Video

| Item | Detalhe |
|------|---------|
| Titulo | Módulo 12 — Segurança |
| Duracao | 34 min |
| Cenas | 13 |
| Formato | Expositivo com demonstracao pratica |
| Nivel | Intermediario |

---

## Roteiro por Cena

### Cena 1 — INTRO

**Duracao:** 1:30

**Narracao:**
> Ola! Nesta aula vamos explorar: Módulo 12 — Segurança. Ao final, voce vai entender os conceitos fundamentais e como aplica-los na pratica. Vamos la?

**Visuais:**
- Tela de abertura com titulo do modulo. Animacao suave com o nome do curso.

**Texto na tela:**
```
[TITULO] Módulo 12 — Segurança
```

**Notas de direcao:**
- Tom energico e convidativo. Apresentar o problema que sera resolvido.

---

### Cena 2 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 1. Por que segurança é o requisito mais importante. Segurança não é uma feature — é um **pré-requisito**. Um sistema inseguro é um passivo, não um ativo. Falha de segurança típica: ┌──────────────────────────────────────────────┐ │  Dados vazados                               │

**Visuais:**
- Slides com topicos-chave. ```text
❌ "Segurança é problema do DevOps"
❌ "Depois a gente adiciona segurança"
❌ "Ninguém vai atacar nosso sistema"

✅ "Segurança é responsabilidade de todos"
✅ "Segurança é parte da definição de 'pronto'"
✅ "Se tem valor, vai ser atacado"
```

**Texto na tela:**
```
[1. Por que segurança é o requisito mais importante]
```

**Notas de direcao:**
- Secao 2 de 10. Usar exemplos praticos.

---

### Cena 3 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 2. OWASP Top 10 (2021). As 10 vulnerabilidades mais críticas em aplicações web. > Usuário acessa recursos que não deveria. // ❌ Ruim: Não verifica se o recurso pertence ao usuário @Get('/orders/:id')

**Visuais:**
- Slides com topicos-chave. ```text
❌ "Segurança é problema do DevOps"
❌ "Depois a gente adiciona segurança"
❌ "Ninguém vai atacar nosso sistema"

✅ "Segurança é responsabilidade de todos"
✅ "Segurança é parte da definição de 'pronto'"
✅ "Se tem valor, vai ser atacado"
```

**Texto na tela:**
```
[2. OWASP Top 10 (2021)]
```

**Notas de direcao:**
- Secao 3 de 10. Usar exemplos praticos.

---

### Cena 4 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 3. Autenticação com JWT. 1. Usuário envia email + senha 2. Servidor valida credenciais 3. Servidor gera ACCESS TOKEN (15min) + REFRESH TOKEN (7d) 4. Cliente armazena e envia access token em requisições

**Visuais:**
- Slides com topicos-chave. ```text
❌ "Segurança é problema do DevOps"
❌ "Depois a gente adiciona segurança"
❌ "Ninguém vai atacar nosso sistema"

✅ "Segurança é responsabilidade de todos"
✅ "Segurança é parte da definição de 'pronto'"
✅ "Se tem valor, vai ser atacado"
```

**Texto na tela:**
```
[3. Autenticação com JWT]
```

**Notas de direcao:**
- Secao 4 de 10. Usar exemplos praticos.

---

### Cena 5 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 4. Autorização com CASL (RBAC). // abilities.ts export type Action = 'manage' | 'create' | 'read' | 'update' | 'delete'; export type Subject = 'User' | 'Order' | 'Product' | 'Report' | 'all'; export function defineAbilitiesFor(user: User): PureAbility {

**Visuais:**
- Slides com topicos-chave. ```text
❌ "Segurança é problema do DevOps"
❌ "Depois a gente adiciona segurança"
❌ "Ninguém vai atacar nosso sistema"

✅ "Segurança é responsabilidade de todos"
✅ "Segurança é parte da definição de 'pronto'"
✅ "Se tem valor, vai ser atacado"
```

**Texto na tela:**
```
[4. Autorização com CASL (RBAC)]
```

**Notas de direcao:**
- Secao 5 de 10. Usar exemplos praticos.

---

### Cena 6 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 5. Rate Limiting. Protege contra brute force, DDoS e abuso. // app.module.ts @Module({ imports: [

**Visuais:**
- Slides com topicos-chave. ```text
❌ "Segurança é problema do DevOps"
❌ "Depois a gente adiciona segurança"
❌ "Ninguém vai atacar nosso sistema"

✅ "Segurança é responsabilidade de todos"
✅ "Segurança é parte da definição de 'pronto'"
✅ "Se tem valor, vai ser atacado"
```

**Texto na tela:**
```
[5. Rate Limiting]
```

**Notas de direcao:**
- Secao 6 de 10. Usar exemplos praticos.

---

### Cena 7 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 6. Headers de Segurança (Helmet + CSP). import helmet from 'helmet'; app.use(helmet()); // Configura automaticamente: // Content-Security-Policy

**Visuais:**
- Slides com topicos-chave. ```text
❌ "Segurança é problema do DevOps"
❌ "Depois a gente adiciona segurança"
❌ "Ninguém vai atacar nosso sistema"

✅ "Segurança é responsabilidade de todos"
✅ "Segurança é parte da definição de 'pronto'"
✅ "Se tem valor, vai ser atacado"
```

**Texto na tela:**
```
[6. Headers de Segurança (Helmet + CSP)]
```

**Notas de direcao:**
- Secao 7 de 10. Usar exemplos praticos.

---

### Cena 8 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 7. Proteções Específicas. // ❌ Nunca fazer const users = await prisma.$queryRawUnsafe(`SELECT * FROM users WHERE email = '${email}'`); // ✅ Prisma previne com query builders const user = await prisma.user.findUnique({ where: { email } });

**Visuais:**
- Slides com topicos-chave. ```text
❌ "Segurança é problema do DevOps"
❌ "Depois a gente adiciona segurança"
❌ "Ninguém vai atacar nosso sistema"

✅ "Segurança é responsabilidade de todos"
✅ "Segurança é parte da definição de 'pronto'"
✅ "Se tem valor, vai ser atacado"
```

**Texto na tela:**
```
[7. Proteções Específicas]
```

**Notas de direcao:**
- Secao 8 de 10. Usar exemplos praticos.

---

### Cena 9 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 8. Secrets Management. // ❌ Hardcoded no código const API_KEY = 'sk-1234567890abcdef'; const DB_PASSWORD = 'minha-senha-super-secreta'; // ❌ No .env comitado

**Visuais:**
- Slides com topicos-chave. ```text
❌ "Segurança é problema do DevOps"
❌ "Depois a gente adiciona segurança"
❌ "Ninguém vai atacar nosso sistema"

✅ "Segurança é responsabilidade de todos"
✅ "Segurança é parte da definição de 'pronto'"
✅ "Se tem valor, vai ser atacado"
```

**Texto na tela:**
```
[8. Secrets Management]
```

**Notas de direcao:**
- Secao 9 de 10. Usar exemplos praticos.

---

### Cena 10 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 9. Auditoria de Segurança. // Log de ações sensíveis @Injectable() export class AuditService { async log(action: AuditAction): Promise<void> {

**Visuais:**
- Slides com topicos-chave. ```text
❌ "Segurança é problema do DevOps"
❌ "Depois a gente adiciona segurança"
❌ "Ninguém vai atacar nosso sistema"

✅ "Segurança é responsabilidade de todos"
✅ "Segurança é parte da definição de 'pronto'"
✅ "Se tem valor, vai ser atacado"
```

**Texto na tela:**
```
[9. Auditoria de Segurança]
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
Falha de segurança típica:
  ┌──────────────────────────────────────────────┐
  │  Dados vazados                               │
  │  Multas regulatórias (LGPD: até 2% do fat.) │
  │  Perda de confiança dos clientes             │
  │  Custos de remediação (R$ 200k-2M médio)     │
  │  Tempo de inatividade                        │
  └──────────────────────────────────────────────┘

Custo de prevenir:
  ┌──────────────────────────────────────────────┐
  │  Treinamento do time: R$ 5k                  │
```
```

**Notas de direcao:**
- Explicar linha por linha. Destacar pontos importantes com zoom ou realce.

---

### Cena 12 — SUMMARY

**Duracao:** 1:30

**Narracao:**
> Recapitulando: vimos 1. Por que segurança é o requisito mais importante, 2. OWASP Top 10 (2021), 3. Autenticação com JWT, 4. Autorização com CASL (RBAC), 5. Rate Limiting, 6. Headers de Segurança (Helmet + CSP). Esses conceitos sao fundamentais para sua formacao.

**Visuais:**
- Lista resumida com icones. Transicao suave para encerramento.

**Texto na tela:**
```
✓ 1. Por que segurança é o requisito mais importante
✓ 2. OWASP Top 10 (2021)
✓ 3. Autenticação com JWT
✓ 4. Autorização com CASL (RBAC)
✓ 5. Rate Limiting
✓ 6. Headers de Segurança (Helmet + CSP)
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

- Texto: 'Módulo 12 '
- Cor de fundo: azul escuro (#1a2332)
- Destaque: codigo ou diagrama ao fundo
- Rosto do apresentador no canto inferior direito

---

## SEO

**Titulo:** Módulo 12 — Segurança | Arquitetura Enterprise
**Descricao:** Aprenda módulo 12 — segurança. Nesta aula abordamos conceitos fundamentais com exemplos praticos em TypeScript.
**Tags:** arquitetura, software, enterprise, typescript, desenvolvimento
