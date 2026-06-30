# Roteiro de Videoaula — Módulo 20 — Automação

**Duracao total estimada:** 34 minutos
**Formato:** Videoaula gravada / Streaming
**Publico-alvo:** Desenvolvedores intermediarios

---

## Visao Geral do Video

| Item | Detalhe |
|------|---------|
| Titulo | Módulo 20 — Automação |
| Duracao | 34 min |
| Cenas | 13 |
| Formato | Expositivo com demonstracao pratica |
| Nivel | Intermediario |

---

## Roteiro por Cena

### Cena 1 — INTRO

**Duracao:** 1:30

**Narracao:**
> Ola! Nesta aula vamos explorar: Módulo 20 — Automação. Ao final, voce vai entender os conceitos fundamentais e como aplica-los na pratica. Vamos la?

**Visuais:**
- Tela de abertura com titulo do modulo. Animacao suave com o nome do curso.

**Texto na tela:**
```
[TITULO] Módulo 20 — Automação
```

**Notas de direcao:**
- Tom energico e convidativo. Apresentar o problema que sera resolvido.

---

### Cena 2 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 1. O que é Automação. Automação é a substituição de processos manuais repetitivos por scripts, pipelines e ferramentas que executam essas tarefas de forma confiável, auditável e escalável. | Motivo | Impacto | |--------|---------| | Reduzir erro humano | O maior causador de incidentes em produção ainda é o operador humano |

**Visuais:**
- Slides com topicos-chave. ```text
Custo de automatizar = (tempo para criar + tempo para manter) × custo-hora
Benefício = (tempo economizado por execução × frequência × horizonte) - custo
```

**Texto na tela:**
```
[1. O que é Automação]
```

**Notas de direcao:**
- Secao 2 de 10. Usar exemplos praticos.

---

### Cena 3 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 2. CI/CD — Pipelines de Integração e Deploy Contínuo. CI/CD é a espinha dorsal da automação em engenharia de software. Todo push para branches compartilhadas dispara: 1. Checkout do código 2. Instalação de dependências

**Visuais:**
- Slides com topicos-chave. ```text
Custo de automatizar = (tempo para criar + tempo para manter) × custo-hora
Benefício = (tempo economizado por execução × frequência × horizonte) - custo
```

**Texto na tela:**
```
[2. CI/CD — Pipelines de Integração e Deploy Contínuo]
```

**Notas de direcao:**
- Secao 3 de 10. Usar exemplos praticos.

---

### Cena 4 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 3. Automação de Testes. A pipeline de CI deve executar testes em camadas, respeitando a **pirâmide de testes**. Executados primeiro — são rápidos e isolados. // Exemplo com vitest import { describe, it, expect } from 'vitest'

**Visuais:**
- Slides com topicos-chave. ```text
Custo de automatizar = (tempo para criar + tempo para manter) × custo-hora
Benefício = (tempo economizado por execução × frequência × horizonte) - custo
```

**Texto na tela:**
```
[3. Automação de Testes]
```

**Notas de direcao:**
- Secao 4 de 10. Usar exemplos praticos.

---

### Cena 5 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 4. Automação de Infraestrutura — IaC. Infrastructure as Code (IaC) é o gerenciamento de infraestrutura (servidores, bancos, redes) através de arquivos de configuração versionados. terraform { required_providers { aws = {

**Visuais:**
- Slides com topicos-chave. ```text
Custo de automatizar = (tempo para criar + tempo para manter) × custo-hora
Benefício = (tempo economizado por execução × frequência × horizonte) - custo
```

**Texto na tela:**
```
[4. Automação de Infraestrutura — IaC]
```

**Notas de direcao:**
- Secao 5 de 10. Usar exemplos praticos.

---

### Cena 6 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 5. Automação de Deploys. Duas versões do ambiente (blue = atual, green = nova). O balanceador de carga muda o tráfego da blue para a green. USUÁRIOS → Load Balancer → Blue (v1.0) ✅ → Green (v1.1) 🟢 (após validação) Switch: DNS/ALB aponta para Green

**Visuais:**
- Slides com topicos-chave. ```text
Custo de automatizar = (tempo para criar + tempo para manter) × custo-hora
Benefício = (tempo economizado por execução × frequência × horizonte) - custo
```

**Texto na tela:**
```
[5. Automação de Deploys]
```

**Notas de direcao:**
- Secao 6 de 10. Usar exemplos praticos.

---

### Cena 7 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 6. Automação de Banco de Dados. migrate: name: Rodar Migrations needs: build runs-on: ubuntu-latest

**Visuais:**
- Slides com topicos-chave. ```text
Custo de automatizar = (tempo para criar + tempo para manter) × custo-hora
Benefício = (tempo economizado por execução × frequência × horizonte) - custo
```

**Texto na tela:**
```
[6. Automação de Banco de Dados]
```

**Notas de direcao:**
- Secao 7 de 10. Usar exemplos praticos.

---

### Cena 8 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 7. Automação de Segurança. Análise estática de segurança diretamente no pipeline. security-sast: name: Análise Estática (SAST) runs-on: ubuntu-latest

**Visuais:**
- Slides com topicos-chave. ```text
Custo de automatizar = (tempo para criar + tempo para manter) × custo-hora
Benefício = (tempo economizado por execução × frequência × horizonte) - custo
```

**Texto na tela:**
```
[7. Automação de Segurança]
```

**Notas de direcao:**
- Secao 8 de 10. Usar exemplos praticos.

---

### Cena 9 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 8. Automação de Code Review. code-review: name: Revisão Automática runs-on: ubuntu-latest steps:

**Visuais:**
- Slides com topicos-chave. ```text
Custo de automatizar = (tempo para criar + tempo para manter) × custo-hora
Benefício = (tempo economizado por execução × frequência × horizonte) - custo
```

**Texto na tela:**
```
[8. Automação de Code Review]
```

**Notas de direcao:**
- Secao 9 de 10. Usar exemplos praticos.

---

### Cena 10 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 9. Automação de Releases. release: name: Gerar Release needs: build runs-on: ubuntu-latest

**Visuais:**
- Slides com topicos-chave. ```text
Custo de automatizar = (tempo para criar + tempo para manter) × custo-hora
Benefício = (tempo economizado por execução × frequência × horizonte) - custo
```

**Texto na tela:**
```
[9. Automação de Releases]
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
Custo de automatizar = (tempo para criar + tempo para manter) × custo-hora
Benefício = (tempo economizado por execução × frequência × horizonte) - custo
```
```

**Notas de direcao:**
- Explicar linha por linha. Destacar pontos importantes com zoom ou realce.

---

### Cena 12 — SUMMARY

**Duracao:** 1:30

**Narracao:**
> Recapitulando: vimos 1. O que é Automação, 2. CI/CD — Pipelines de Integração e Deploy Contínuo, 3. Automação de Testes, 4. Automação de Infraestrutura — IaC, 5. Automação de Deploys, 6. Automação de Banco de Dados. Esses conceitos sao fundamentais para sua formacao.

**Visuais:**
- Lista resumida com icones. Transicao suave para encerramento.

**Texto na tela:**
```
✓ 1. O que é Automação
✓ 2. CI/CD — Pipelines de Integração e Deploy Contínuo
✓ 3. Automação de Testes
✓ 4. Automação de Infraestrutura — IaC
✓ 5. Automação de Deploys
✓ 6. Automação de Banco de Dados
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

- Texto: 'Módulo 20 '
- Cor de fundo: azul escuro (#1a2332)
- Destaque: codigo ou diagrama ao fundo
- Rosto do apresentador no canto inferior direito

---

## SEO

**Titulo:** Módulo 20 — Automação | Arquitetura Enterprise
**Descricao:** Aprenda módulo 20 — automação. Nesta aula abordamos conceitos fundamentais com exemplos praticos em TypeScript.
**Tags:** arquitetura, software, enterprise, typescript, desenvolvimento
