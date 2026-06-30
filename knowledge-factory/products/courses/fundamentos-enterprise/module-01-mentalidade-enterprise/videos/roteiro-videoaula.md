# Roteiro de Videoaula — Módulo 01 — Mentalidade Enterprise

**Duracao total estimada:** 34 minutos
**Formato:** Videoaula gravada / Streaming
**Publico-alvo:** Desenvolvedores intermediarios

---

## Visao Geral do Video

| Item | Detalhe |
|------|---------|
| Titulo | Módulo 01 — Mentalidade Enterprise |
| Duracao | 34 min |
| Cenas | 13 |
| Formato | Expositivo com demonstracao pratica |
| Nivel | Intermediario |

---

## Roteiro por Cena

### Cena 1 — INTRO

**Duracao:** 1:30

**Narracao:**
> Ola! Nesta aula vamos explorar: Módulo 01 — Mentalidade Enterprise. Ao final, voce vai entender os conceitos fundamentais e como aplica-los na pratica. Vamos la?

**Visuais:**
- Tela de abertura com titulo do modulo. Animacao suave com o nome do curso.

**Texto na tela:**
```
[TITULO] Módulo 01 — Mentalidade Enterprise
```

**Notas de direcao:**
- Tom energico e convidativo. Apresentar o problema que sera resolvido.

---

### Cena 2 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 1. O que é software Enterprise?. Software Enterprise é aquele construído para **organizações**, não para indivíduos. | Característica | Exemplo de problema se ignorada | |----------------|-------------------------------| | **Multi-usuário** | Dois usuários editam o mesmo registro e um perde as alterações |

**Visuais:**
- Slides com topicos-chave. ```text
Software de Consumo:                Software Enterprise:
- Um usuário                        - Centenas/milhares de usuários
- Dados isolados                    - Dados compartilhados com permissões
- "Funcionou no meu PC"             - Funciona em múltiplos ambientes
- Atualização quando quiser         - Atualização com rollback e migração
- Suporte via chat                  - SLA definido contratualmente
- Compliance: nenhum                - Compliance: LGPD, SOC2, ISO 27001
```

**Texto na tela:**
```
[1. O que é software Enterprise?]
```

**Notas de direcao:**
- Secao 2 de 10. Usar exemplos praticos.

---

### Cena 3 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 2. Escalabilidade. Escalabilidade é a capacidade do sistema de **manter a performance** à medida que a demanda cresce. Escala Vertical (Scale Up): Aumentar recursos da máquina CPU: 4 cores → 16 cores

**Visuais:**
- Slides com topicos-chave. ```text
Software de Consumo:                Software Enterprise:
- Um usuário                        - Centenas/milhares de usuários
- Dados isolados                    - Dados compartilhados com permissões
- "Funcionou no meu PC"             - Funciona em múltiplos ambientes
- Atualização quando quiser         - Atualização com rollback e migração
- Suporte via chat                  - SLA definido contratualmente
- Compliance: nenhum                - Compliance: LGPD, SOC2, ISO 27001
```

**Texto na tela:**
```
[2. Escalabilidade]
```

**Notas de direcao:**
- Secao 3 de 10. Usar exemplos praticos.

---

### Cena 4 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 3. Governança. Governança é o conjunto de **regras e processos** que garantem consistência e qualidade no desenvolvimento. ┌──────────────────────────────────────────────┐ │                 GOVERNANÇA                    │ ├──────────────────────────────────────────────┤

**Visuais:**
- Slides com topicos-chave. ```text
Software de Consumo:                Software Enterprise:
- Um usuário                        - Centenas/milhares de usuários
- Dados isolados                    - Dados compartilhados com permissões
- "Funcionou no meu PC"             - Funciona em múltiplos ambientes
- Atualização quando quiser         - Atualização com rollback e migração
- Suporte via chat                  - SLA definido contratualmente
- Compliance: nenhum                - Compliance: LGPD, SOC2, ISO 27001
```

**Texto na tela:**
```
[3. Governança]
```

**Notas de direcao:**
- Secao 4 de 10. Usar exemplos praticos.

---

### Cena 5 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: Regras de Governança. TypeScript strict mode obrigatório Sem `any` — exceções revisadas em PR Lint e format automáticos (pre-commit hook) Toda feature começa com ADR se mudar arquitetura

**Visuais:**
- Slides com topicos-chave. ```text
Software de Consumo:                Software Enterprise:
- Um usuário                        - Centenas/milhares de usuários
- Dados isolados                    - Dados compartilhados com permissões
- "Funcionou no meu PC"             - Funciona em múltiplos ambientes
- Atualização quando quiser         - Atualização com rollback e migração
- Suporte via chat                  - SLA definido contratualmente
- Compliance: nenhum                - Compliance: LGPD, SOC2, ISO 27001
```

**Texto na tela:**
```
[Regras de Governança]
```

**Notas de direcao:**
- Secao 5 de 10. Usar exemplos praticos.

---

### Cena 6 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 4. Manutenibilidade. Manutenibilidade é a facilidade de **entender, modificar e estender** o sistema. Código sem manutenibilidade: ┌────────────────────────────────────────────┐ │  Feature nova         │  2 semanas         │

**Visuais:**
- Slides com topicos-chave. ```text
Software de Consumo:                Software Enterprise:
- Um usuário                        - Centenas/milhares de usuários
- Dados isolados                    - Dados compartilhados com permissões
- "Funcionou no meu PC"             - Funciona em múltiplos ambientes
- Atualização quando quiser         - Atualização com rollback e migração
- Suporte via chat                  - SLA definido contratualmente
- Compliance: nenhum                - Compliance: LGPD, SOC2, ISO 27001
```

**Texto na tela:**
```
[4. Manutenibilidade]
```

**Notas de direcao:**
- Secao 6 de 10. Usar exemplos praticos.

---

### Cena 7 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 5. Observabilidade. Observabilidade é a capacidade de **entender o estado interno do sistema** a partir de seus outputs externos. LOGS                            MÉTRICAS                    TRACING Eventos discretos               Dados agregados             Fluxo de requisições "Usuário X fez Y"              "500 requisições/segundo"   "Requisição passou por A→B→C"

**Visuais:**
- Slides com topicos-chave. ```text
Software de Consumo:                Software Enterprise:
- Um usuário                        - Centenas/milhares de usuários
- Dados isolados                    - Dados compartilhados com permissões
- "Funcionou no meu PC"             - Funciona em múltiplos ambientes
- Atualização quando quiser         - Atualização com rollback e migração
- Suporte via chat                  - SLA definido contratualmente
- Compliance: nenhum                - Compliance: LGPD, SOC2, ISO 27001
```

**Texto na tela:**
```
[5. Observabilidade]
```

**Notas de direcao:**
- Secao 7 de 10. Usar exemplos praticos.

---

### Cena 8 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 6. Segurança. Segurança em software Enterprise não é opcional — é **pré-requisito**. Não: "Vamos adicionar segurança depois" Sim: "Segurança é parte da definição de "pronto"" Camada 1: Código

**Visuais:**
- Slides com topicos-chave. ```text
Software de Consumo:                Software Enterprise:
- Um usuário                        - Centenas/milhares de usuários
- Dados isolados                    - Dados compartilhados com permissões
- "Funcionou no meu PC"             - Funciona em múltiplos ambientes
- Atualização quando quiser         - Atualização com rollback e migração
- Suporte via chat                  - SLA definido contratualmente
- Compliance: nenhum                - Compliance: LGPD, SOC2, ISO 27001
```

**Texto na tela:**
```
[6. Segurança]
```

**Notas de direcao:**
- Secao 8 de 10. Usar exemplos praticos.

---

### Cena 9 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 7. Compliance. Compliance é a **conformidade com leis e regulamentações**. | Regulamentação | Região | Foco | |---------------|--------|------| | LGPD | Brasil | Dados pessoais |

**Visuais:**
- Slides com topicos-chave. ```text
Software de Consumo:                Software Enterprise:
- Um usuário                        - Centenas/milhares de usuários
- Dados isolados                    - Dados compartilhados com permissões
- "Funcionou no meu PC"             - Funciona em múltiplos ambientes
- Atualização quando quiser         - Atualização com rollback e migração
- Suporte via chat                  - SLA definido contratualmente
- Compliance: nenhum                - Compliance: LGPD, SOC2, ISO 27001
```

**Texto na tela:**
```
[7. Compliance]
```

**Notas de direcao:**
- Secao 9 de 10. Usar exemplos praticos.

---

### Cena 10 — CONTENT

**Duracao:** 3:00

**Narracao:**
> Agora vamos falar sobre: 8. Multi-tenant. Multi-tenant é a capacidade de **atender múltiplos clientes** (tenants) com uma única instância do sistema. Database per Tenant: Prós: isolamento máximo, backup individual Contras: caro, complexo (migrations em N bancos)

**Visuais:**
- Slides com topicos-chave. ```text
Software de Consumo:                Software Enterprise:
- Um usuário                        - Centenas/milhares de usuários
- Dados isolados                    - Dados compartilhados com permissões
- "Funcionou no meu PC"             - Funciona em múltiplos ambientes
- Atualização quando quiser         - Atualização com rollback e migração
- Suporte via chat                  - SLA definido contratualmente
- Compliance: nenhum                - Compliance: LGPD, SOC2, ISO 27001
```

**Texto na tela:**
```
[8. Multi-tenant]
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
Software de Consumo:                Software Enterprise:
- Um usuário                        - Centenas/milhares de usuários
- Dados isolados                    - Dados compartilhados com permissões
- "Funcionou no meu PC"             - Funciona em múltiplos ambientes
- Atualização quando quiser         - Atualização com rollback e migração
- Suporte via chat                  - SLA definido contratualmente
- Compliance: nenhum                - Compliance: LGPD, SOC2, ISO 27001
```
```

**Notas de direcao:**
- Explicar linha por linha. Destacar pontos importantes com zoom ou realce.

---

### Cena 12 — SUMMARY

**Duracao:** 1:30

**Narracao:**
> Recapitulando: vimos 1. O que é software Enterprise?, 2. Escalabilidade, 3. Governança, Regras de Governança, 4. Manutenibilidade, 5. Observabilidade. Esses conceitos sao fundamentais para sua formacao.

**Visuais:**
- Lista resumida com icones. Transicao suave para encerramento.

**Texto na tela:**
```
✓ 1. O que é software Enterprise?
✓ 2. Escalabilidade
✓ 3. Governança
✓ Regras de Governança
✓ 4. Manutenibilidade
✓ 5. Observabilidade
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

- Texto: 'Módulo 01 '
- Cor de fundo: azul escuro (#1a2332)
- Destaque: codigo ou diagrama ao fundo
- Rosto do apresentador no canto inferior direito

---

## SEO

**Titulo:** Módulo 01 — Mentalidade Enterprise | Arquitetura Enterprise
**Descricao:** Aprenda módulo 01 — mentalidade enterprise. Nesta aula abordamos conceitos fundamentais com exemplos praticos em TypeScript.
**Tags:** arquitetura, software, enterprise, typescript, desenvolvimento
