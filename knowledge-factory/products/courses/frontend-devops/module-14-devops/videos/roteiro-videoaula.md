# Roteiro de Videoaula — Módulo 14 — DevOps: Docker, CI/CD e Deploy

**Duracao total estimada:** 31 minutos
**Formato:** Videoaula gravada / Streaming
**Publico-alvo:** Desenvolvedores intermediarios

---

## Visao Geral do Video

| Item | Detalhe |
|------|---------|
| Titulo | Módulo 14 — DevOps: Docker, CI/CD e Deploy |
| Duracao | 31 min |
| Cenas | 12 |
| Formato | Expositivo com demonstracao pratica |
| Nivel | Intermediario |

---

## Roteiro por Cena

### Cena 1 — INTRO

**Duracao:** 1:30

**Narracao:**
> Ola! Nesta aula vamos explorar: Módulo 14 — DevOps: Docker, CI/CD e Deploy. Ao final, voce vai entender os conceitos fundamentais e como aplica-los na pratica. Vamos la?

**Visuais:**
- Tela de abertura com titulo do modulo. Animacao suave com o nome do curso.

**Texto na tela:**
```
[TITULO] Módulo 14 — DevOps: Docker, CI/CD e Deploy
```

**Notas de direcao:**
- Tom energico e convidativo. Apresentar o problema que sera resolvido.

---

### Cena 2 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 1. Por que DevOps importa. DevOps é a ponte entre o **código funcionando na máquina do dev** e o **código funcionando em produção**. "Funciona na minha máquina" → "Não funciona no servidor" Causas: Versões diferentes de dependências

**Visuais:**
- Slides com topicos-chave. ```text
"Funciona na minha máquina" → "Não funciona no servidor"

Causas:
  - Versões diferentes de dependências
  - Variáveis de ambiente não configuradas
  - Banco de dados diferente
  - Sistema operacional diferente
  - Permissões diferentes
```

**Texto na tela:**
```
[1. Por que DevOps importa]
```

**Notas de direcao:**
- Secao 2 de 9. Usar exemplos praticos.

---

### Cena 3 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 2. Docker — Containerização. ┌────────────────────────────────────────┐ │  CONTAINER                             │ │  ┌──────────────────────────────────┐  │ │  │  Aplicação (Node.js)             │  │

**Visuais:**
- Slides com topicos-chave. ```text
"Funciona na minha máquina" → "Não funciona no servidor"

Causas:
  - Versões diferentes de dependências
  - Variáveis de ambiente não configuradas
  - Banco de dados diferente
  - Sistema operacional diferente
  - Permissões diferentes
```

**Texto na tela:**
```
[2. Docker — Containerização]
```

**Notas de direcao:**
- Secao 3 de 9. Usar exemplos praticos.

---

### Cena 4 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 3. GitHub Actions — CI/CD. name: CI on: push: branches: [main, develop]

**Visuais:**
- Slides com topicos-chave. ```text
"Funciona na minha máquina" → "Não funciona no servidor"

Causas:
  - Versões diferentes de dependências
  - Variáveis de ambiente não configuradas
  - Banco de dados diferente
  - Sistema operacional diferente
  - Permissões diferentes
```

**Texto na tela:**
```
[3. GitHub Actions — CI/CD]
```

**Notas de direcao:**
- Secao 4 de 9. Usar exemplos praticos.

---

### Cena 5 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 4. Variáveis de Ambiente. DATABASE_URL=postgresql://user:password@localhost:5432/db JWT_SECRET=change-me JWT_REFRESH_SECRET=change-me REDIS_URL=redis://localhost:6379

**Visuais:**
- Slides com topicos-chave. ```text
"Funciona na minha máquina" → "Não funciona no servidor"

Causas:
  - Versões diferentes de dependências
  - Variáveis de ambiente não configuradas
  - Banco de dados diferente
  - Sistema operacional diferente
  - Permissões diferentes
```

**Texto na tela:**
```
[4. Variáveis de Ambiente]
```

**Notas de direcao:**
- Secao 5 de 9. Usar exemplos praticos.

---

### Cena 6 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 5. Estratégias de Deploy. Versão Azul (atual): ┌──────────┐ │ app:v1   │ ← Load Balancer (tráfego ativo) └──────────┘

**Visuais:**
- Slides com topicos-chave. ```text
"Funciona na minha máquina" → "Não funciona no servidor"

Causas:
  - Versões diferentes de dependências
  - Variáveis de ambiente não configuradas
  - Banco de dados diferente
  - Sistema operacional diferente
  - Permissões diferentes
```

**Texto na tela:**
```
[5. Estratégias de Deploy]
```

**Notas de direcao:**
- Secao 6 de 9. Usar exemplos praticos.

---

### Cena 7 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 6. Docker Compose para múltiplos ambientes. services: api: build: context: .

**Visuais:**
- Slides com topicos-chave. ```text
"Funciona na minha máquina" → "Não funciona no servidor"

Causas:
  - Versões diferentes de dependências
  - Variáveis de ambiente não configuradas
  - Banco de dados diferente
  - Sistema operacional diferente
  - Permissões diferentes
```

**Texto na tela:**
```
[6. Docker Compose para múltiplos ambientes]
```

**Notas de direcao:**
- Secao 7 de 9. Usar exemplos praticos.

---

### Cena 8 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 7. Health Checks e Graceful Shutdown. @Controller('health') export class HealthController { constructor( private prisma: PrismaService,

**Visuais:**
- Slides com topicos-chave. ```text
"Funciona na minha máquina" → "Não funciona no servidor"

Causas:
  - Versões diferentes de dependências
  - Variáveis de ambiente não configuradas
  - Banco de dados diferente
  - Sistema operacional diferente
  - Permissões diferentes
```

**Texto na tela:**
```
[7. Health Checks e Graceful Shutdown]
```

**Notas de direcao:**
- Secao 8 de 9. Usar exemplos praticos.

---

### Cena 9 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 8. Logs Estruturados. import { Logger } from '@nestjs/common'; import { utilities as nestWinstonModuleUtilities } from 'nest-winston'; import * as winston from 'winston'; // main.ts

**Visuais:**
- Slides com topicos-chave. ```text
"Funciona na minha máquina" → "Não funciona no servidor"

Causas:
  - Versões diferentes de dependências
  - Variáveis de ambiente não configuradas
  - Banco de dados diferente
  - Sistema operacional diferente
  - Permissões diferentes
```

**Texto na tela:**
```
[8. Logs Estruturados]
```

**Notas de direcao:**
- Secao 9 de 9. Usar exemplos praticos.

---

### Cena 10 — CODE-DEMO

**Duracao:** 4:00

**Narracao:**
> Vamos ver na pratica como isso funciona. Observe este codigo em text:

**Visuais:**
- Tela dividida: editor de codigo a esquerda, terminal/output a direita.

**Texto na tela:**
```
```text
"Funciona na minha máquina" → "Não funciona no servidor"

Causas:
  - Versões diferentes de dependências
  - Variáveis de ambiente não configuradas
  - Banco de dados diferente
  - Sistema operacional diferente
  - Permissões diferentes
```
```

**Notas de direcao:**
- Explicar linha por linha. Destacar pontos importantes com zoom ou realce.

---

### Cena 11 — SUMMARY

**Duracao:** 1:30

**Narracao:**
> Recapitulando: vimos 1. Por que DevOps importa, 2. Docker — Containerização, 3. GitHub Actions — CI/CD, 4. Variáveis de Ambiente, 5. Estratégias de Deploy, 6. Docker Compose para múltiplos ambientes. Esses conceitos sao fundamentais para sua formacao.

**Visuais:**
- Lista resumida com icones. Transicao suave para encerramento.

**Texto na tela:**
```
✓ 1. Por que DevOps importa
✓ 2. Docker — Containerização
✓ 3. GitHub Actions — CI/CD
✓ 4. Variáveis de Ambiente
✓ 5. Estratégias de Deploy
✓ 6. Docker Compose para múltiplos ambientes
```

**Notas de direcao:**
- Reforcar os aprendizados principais. Conectar com o proximo modulo.

---

### Cena 12 — OUTRO

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

- Texto: 'Módulo 14 '
- Cor de fundo: azul escuro (#1a2332)
- Destaque: codigo ou diagrama ao fundo
- Rosto do apresentador no canto inferior direito

---

## SEO

**Titulo:** Módulo 14 — DevOps: Docker, CI/CD e Deploy | Arquitetura Enterprise
**Descricao:** Aprenda módulo 14 — devops: docker, ci/cd e deploy. Nesta aula abordamos conceitos fundamentais com exemplos praticos em TypeScript.
**Tags:** arquitetura, software, enterprise, typescript, desenvolvimento
