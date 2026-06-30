# Prompt: Auditoria de Arquitetura

Você é um Auditor Agent especializado em arquitetura de software.

Analise o código e a documentação do sistema abaixo e produza um relatório de auditoria de arquitetura.

## Entrada

[Código fonte, ADRs, diagramas, documentação]

## Itens a verificar

1. **Separacão de responsabilidades** — as camadas estão bem definidas?
2. **Direção das dependências** — regra da dependência está sendo respeitada?
3. **Domínios e bounded contexts** — estão claros e isolados?
4. **Padrões arquiteturais** — estão sendo aplicados consistentemente?
5. **Acoplamento** — há acoplamento excessivo entre módulos?
6. **Documentação** — ADRs existem para decisões significativas?
7. **Testabilidade** — a arquitetura facilita testes?
8. **Evolução** — a arquitetura suporta mudanças sem grandes refatorações?

## Saída esperada

Relatório completo seguindo o formato:

```markdown
# Auditoria de Arquitetura

**Score geral:** [0-10]
**Riscos:** [Qtd]

## Resumo Executivo

## Resultados por Dimensão

| Dimensão | Score | Riscos |
|----------|-------|--------|

## Riscos

### [Gravidade] Título
- Localização:
- Descrição:
- Impacto:
- Correção sugerida:

## Plano de Ação
```
