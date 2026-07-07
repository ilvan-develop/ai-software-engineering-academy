# Roteiro de Videoaula — Módulo 13b — Multi-Tenant: Implementação com NestJS e Prisma

**Duracao total estimada:** 16 minutos
**Formato:** Videoaula gravada / Streaming
**Publico-alvo:** Desenvolvedores intermediarios

---

## Visao Geral do Video

| Item | Detalhe |
|------|---------|
| Titulo | Módulo 13b — Multi-Tenant: Implementação com NestJS e Prisma |
| Duracao | 16 min |
| Cenas | 7 |
| Formato | Expositivo com demonstracao pratica |
| Nivel | Intermediario |

---

## Roteiro por Cena

### Cena 1 — INTRO

**Duracao:** 1:30

**Narracao:**
> Ola! Nesta aula vamos explorar: Módulo 13b — Multi-Tenant: Implementação com NestJS e Prisma. Ao final, voce vai entender os conceitos fundamentais e como aplica-los na pratica. Vamos la?

**Visuais:**
- Tela de abertura com titulo do modulo. Animacao suave com o nome do curso.

**Texto na tela:**
```json
[TITULO] Módulo 13b — Multi-Tenant: Implementação com NestJS e Prisma
```text

**Notas de direcao:**
- Tom energico e convidativo. Apresentar o problema que sera resolvido.

---

### Cena 2 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 1. Identificação do Tenant. O sistema precisa identificar **qual tenant está fazendo a requisição** antes de qualquer lógica de negócio. | Estratégia | Exemplo | Segurança | Complexidade | Ideal para | |-----------|---------|:---------:|:------------:|-----------| | **Subdomínio** | `acme.minhasaas.com` | Média | Média | Apps web públicas |

**Visuais:**
- Slides com topicos-chave. ```typescript
// Útil para debug, mas não recomendado para produção
// Exemplo: GET /api/:tenant/users
@Get('/api/:tenant/users')
findUsers(@Param('tenant') tenantId: string) {
  return this.userService.findAll(tenantId);
}
```text

**Texto na tela:**
```json
[1. Identificação do Tenant]
```text

**Notas de direcao:**
- Secao 2 de 4. Usar exemplos praticos.

---

### Cena 3 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 2. Middleware de Tenant. // tenant.middleware.ts import { Injectable, NestMiddleware, UnauthorizedException } from '@nestjs/common'; import { Request, Response, NextFunction } from 'express'; import * as jwt from 'jsonwebtoken';

**Visuais:**
- Slides com topicos-chave. ```typescript
// Útil para debug, mas não recomendado para produção
// Exemplo: GET /api/:tenant/users
@Get('/api/:tenant/users')
findUsers(@Param('tenant') tenantId: string) {
  return this.userService.findAll(tenantId);
}
```text

**Texto na tela:**
```json
[2. Middleware de Tenant]
```text

**Notas de direcao:**
- Secao 3 de 4. Usar exemplos praticos.

---

### Cena 4 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 3. Prisma Multi-Tenant. // schema.prisma — modelo base generator client { provider = "prisma-client-js" }

**Visuais:**
- Slides com topicos-chave. ```typescript
// Útil para debug, mas não recomendado para produção
// Exemplo: GET /api/:tenant/users
@Get('/api/:tenant/users')
findUsers(@Param('tenant') tenantId: string) {
  return this.userService.findAll(tenantId);
}
```text

**Texto na tela:**
```json
[3. Prisma Multi-Tenant]
```text

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
```text
```typescript
// tenant.extractor.ts
function extractTenantFromHost(host: string): string | null {
  // host: "acme.minhasaas.com" → "acme"
  // host: "localhost:3000" → "localhost" (não é tenant)
  const parts = host.split('.');
  if (parts.length < 3) return null; // sem subdomínio
  return parts[0];
}

// Em produção, validar contra lista de tenants permitidos
async function validateTenantSubdomain(
  host: string,
```text
```javascript

**Notas de direcao:**
- Explicar linha por linha. Destacar pontos importantes com zoom ou realce.

---

### Cena 6 — SUMMARY

**Duracao:** 1:30

**Narracao:**
> Recapitulando: vimos 1. Identificação do Tenant, 2. Middleware de Tenant, 3. Prisma Multi-Tenant. Esses conceitos sao fundamentais para sua formacao.

**Visuais:**
- Lista resumida com icones. Transicao suave para encerramento.

**Texto na tela:**
```text
✓ 1. Identificação do Tenant
✓ 2. Middleware de Tenant
✓ 3. Prisma Multi-Tenant
```text

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
```text
Proximo modulo: [TITULO DO PROXIMO MODULO]
```text

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

- Texto: 'Módulo 13b '
- Cor de fundo: azul escuro (#1a2332)
- Destaque: codigo ou diagrama ao fundo
- Rosto do apresentador no canto inferior direito

---

## SEO

**Titulo:** Módulo 13b — Multi-Tenant: Implementação com NestJS e Prisma | Arquitetura Enterprise
**Descricao:** Aprenda módulo 13b — multi-tenant: implementação com nestjs e prisma. Nesta aula abordamos conceitos fundamentais com exemplos praticos em TypeScript.
**Tags:** arquitetura, software, enterprise, typescript, desenvolvimento
