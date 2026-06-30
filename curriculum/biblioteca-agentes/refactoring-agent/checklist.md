# Checklist: Refactoring Agent

## Pré-refatoração
- [ ] Cobertura de testes existente verificada
- [ ] Testes passam antes de começar
- [ ] Escopo da refatoração definido
- [ ] Comportamento externo não será alterado

## Durante a refatoração
- [ ] Uma mudança por vez
- [ ] Testes rodam após cada mudança
- [ ] Nenhum teste existente quebrou
- [ ] Código mantém-se compilável

## Code smells a eliminar
- [ ] Funções/métodos > 20 linhas (extrair)
- [ ] Parâmetros > 3 (agrupar em objeto/value object)
- [ ] Condicionais aninhados (early return, guard clauses)
- [ ] Duplicação de código (extrair método)
- [ ] Mutações desnecessárias (preferir imutabilidade)
- [ ] `any` no TypeScript (tipar corretamente)
- [ ] Tratamento de erro genérico (try/catch vazio)

## Pós-refatoração
- [ ] Todos os testes passam
- [ ] Lint e type check passam
- [ ] Comportamento preservado (comparar input/output)
- [ ] Mudanças documentadas
