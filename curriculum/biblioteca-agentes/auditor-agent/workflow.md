# Workflow: Auditor Agent

## Fluxo de auditoria

```
1. Receber acesso ao código/sistema
2. Escolher tipo(s) de auditoria
3. Executar checklists automatizados
4. Analisar resultados
5. Atribuir scores
6. Classificar riscos por gravidade
7. Gerar relatório completo
8. Entregar plano de ação priorizado
9. (Opcional) Re-auditar após correções
```

## Critérios de Score

| Score | Significado |
|-------|-------------|
| 9-10 | Excelente — sem riscos significativos |
| 7-8 | Bom — riscos menores, correções opcionais |
| 5-6 | Regular — riscos médios, correções necessárias |
| 3-4 | Ruim — riscos altos, correções urgentes |
| 0-2 | Crítico — riscos graves, parar para corrigir |

## Classificação de Riscos

| Gravidade | Definição | Ação |
|-----------|-----------|------|
| **Blocker** | Impede deploy ou quebra funcionalidade crítica | Corrigir imediatamente |
| **Critical** | Vulnerabilidade grave ou perda de dados | Corrigir em até 24h |
| **Major** | Boa prática não seguida, risco moderado | Corrigir em até 1 semana |
| **Minor** | Sugestão de melhoria, baixo risco | Agenda de refatoração |
