# Workflow: Enterprise Architect Agent

## Fluxo de trabalho

```
1. Receber requisitos do Product Agent
2. Analisar domínios e subdomínios
3. Propor arquitetura (diagrama + justificativa)
4. Documentar decisões em ADR
5. Validar com stakeholders técnicos
6. Refinar com feedback
7. Entregar artefatos (diagramas, ADRs, especificação)
```

## Artefatos produzidos

- Diagrama de arquitetura (C4 Model)
- ADR (Architecture Decision Record) para cada decisão significativa
- Mapa de domínios e bounded contexts
- Especificação de interfaces entre módulos
- Matriz de riscos arquiteturais

## Critérios de qualidade

- [ ] Cada decisão arquitetural tem um ADR correspondente
- [ ] A arquitetura está documentada em nível C4 (Contexto, Container, Componente, Código)
- [ ] Domínios estão isolados e com dependências bem definidas
- [ ] A arquitetura suporta os requisitos não-funcionais (performance, segurança, escalabilidade)
- [ ] O custo de manutenção está estimado e aceito
