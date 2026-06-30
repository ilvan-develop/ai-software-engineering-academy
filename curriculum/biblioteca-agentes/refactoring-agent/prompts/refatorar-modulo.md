# Prompt: Refatorar Módulo

Refatore o módulo abaixo mantendo o comportamento externo.

## Arquivo

[caminho/arquivo.ts]

## Problemas identificados (opcional)

- [lista de code smells, se conhecidos]

## Regras da refatoração

1. Preservar API pública (mesma assinatura de funções exportadas)
2. Uma mudança por vez, verificar testes após cada uma
3. Aplicar, nesta ordem:
   - Extrair funções longas
   - Substituir condicionais aninhados por guard clauses
   - Eliminar duplicação
   - Tipar corretamente (eliminar `any`)
   - Melhorar nomes de variáveis
4. Documentar mudanças significativas

## Saída esperada

```markdown
## Mudanças aplicadas

### 1. [Extraído método X]
- **Arquivo:** ...
- **Antes:** ...
- **Depois:** ...

### 2. [Eliminado `any`]
- **Arquivo:** ...
- **Antes:** `any` → `TipoEspecifico`

## Status dos testes
- [ ] Todos passam
```
