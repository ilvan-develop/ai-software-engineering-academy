# Roteiro de Videoaula — Módulo 13c — Multi-Tenant: Migrations, Dados e Seed

**Duracao total estimada:** 16 minutos
**Formato:** Videoaula gravada / Streaming
**Publico-alvo:** Desenvolvedores intermediarios

---

## Visao Geral do Video

| Item | Detalhe |
|------|---------|
| Titulo | Módulo 13c — Multi-Tenant: Migrations, Dados e Seed |
| Duracao | 16 min |
| Cenas | 7 |
| Formato | Expositivo com demonstracao pratica |
| Nivel | Intermediario |

---

## Roteiro por Cena

### Cena 1 — INTRO

**Duracao:** 1:30

**Narracao:**
> Ola! Nesta aula vamos explorar: Módulo 13c — Multi-Tenant: Migrations, Dados e Seed. Ao final, voce vai entender os conceitos fundamentais e como aplica-los na pratica. Vamos la?

**Visuais:**
- Tela de abertura com titulo do modulo. Animacao suave com o nome do curso.

**Texto na tela:**
```
[TITULO] Módulo 13c — Multi-Tenant: Migrations, Dados e Seed
```

**Notas de direcao:**
- Tom energico e convidativo. Apresentar o problema que sera resolvido.

---

### Cena 2 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 1. Migrations Multi-Tenant. // migrate-all-tenants.ts import { Pool } from 'pg'; import { readMigrationFiles } from './migration-runner'; async function migrateAllTenants(): Promise<void> {

**Visuais:**
- Slides com topicos-chave. Diagrama explicativo

**Texto na tela:**
```
[1. Migrations Multi-Tenant]
```

**Notas de direcao:**
- Secao 2 de 4. Usar exemplos praticos.

---

### Cena 3 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 2. Dados Compartilhados vs Por Tenant. Dados que **não pertencem a nenhum tenant específico** e são comuns a todos: // Globais — uma única instância para o sistema todo interface Plan { id: string;

**Visuais:**
- Slides com topicos-chave. Diagrama explicativo

**Texto na tela:**
```
[2. Dados Compartilhados vs Por Tenant]
```

**Notas de direcao:**
- Secao 3 de 4. Usar exemplos praticos.

---

### Cena 4 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 3. Seed por Tenant. // tenant-seed.ts async function seedNewTenant(tenantSlug: string, plan: string): Promise<void> { const schema = `tenant_${tenantSlug}`; const client = await pool.connect();

**Visuais:**
- Slides com topicos-chave. Diagrama explicativo

**Texto na tela:**
```
[3. Seed por Tenant]
```

**Notas de direcao:**
- Secao 4 de 4. Usar exemplos praticos.

---

### Cena 5 — CODE-DEMO

**Duracao:** 4:00

**Narracao:**
> Vamos ver na pratica como isso funciona. Observe este codigo em typescript:

**Visuais:**
- Tela dividida: editor de codigo a esquerda, terminal/output a direita.

**Texto na tela:**
```
```typescript
// migrate-all-tenants.ts
import { Pool } from 'pg';
import { readMigrationFiles } from './migration-runner';

async function migrateAllTenants(): Promise<void> {
  const tenants = [
    { id: 'acme', dbUrl: 'postgresql://.../acme' },
    { id: 'zeta', dbUrl: 'postgresql://.../zeta' },
    { id: 'omega', dbUrl: 'postgresql://.../omega' },
  ];

  const migrations = await readMigrationFiles();
```
```

**Notas de direcao:**
- Explicar linha por linha. Destacar pontos importantes com zoom ou realce.

---

### Cena 6 — SUMMARY

**Duracao:** 1:30

**Narracao:**
> Recapitulando: vimos 1. Migrations Multi-Tenant, 2. Dados Compartilhados vs Por Tenant, 3. Seed por Tenant. Esses conceitos sao fundamentais para sua formacao.

**Visuais:**
- Lista resumida com icones. Transicao suave para encerramento.

**Texto na tela:**
```
✓ 1. Migrations Multi-Tenant
✓ 2. Dados Compartilhados vs Por Tenant
✓ 3. Seed por Tenant
```

**Notas de direcao:**
- Reforcar os aprendizados principais. Conectar com o proximo modulo.

---

### Cena 7 — OUTRO

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

- Texto: 'Módulo 13c '
- Cor de fundo: azul escuro (#1a2332)
- Destaque: codigo ou diagrama ao fundo
- Rosto do apresentador no canto inferior direito

---

## SEO

**Titulo:** Módulo 13c — Multi-Tenant: Migrations, Dados e Seed | Arquitetura Enterprise
**Descricao:** Aprenda módulo 13c — multi-tenant: migrations, dados e seed. Nesta aula abordamos conceitos fundamentais com exemplos praticos em TypeScript.
**Tags:** arquitetura, software, enterprise, typescript, desenvolvimento
