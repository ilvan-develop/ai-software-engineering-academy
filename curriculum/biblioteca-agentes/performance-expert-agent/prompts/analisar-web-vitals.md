# Prompt: Analisar Core Web Vitals

Analise e otimize os Core Web Vitals da página abaixo.

## URL/Componente

[URL ou código do componente]

## Métricas atuais (se disponíveis)

- LCP: [valor]
- FID/INP: [valor]
- CLS: [valor]

## Análise esperada

Para cada métrica abaixo do ideal:

1. **Causa raiz** — o que está causando o problema
2. **Solução** — como corrigir
3. **Impacto esperado** — melhoria estimada

### Possíveis causas comuns

| Métrica | Causas Comuns | Soluções |
|---------|---------------|----------|
| LCP alto | Imagens grandes, render blocking resources | next/image, lazy load, preload |
| CLS alto | Layout shift sem espaço reservado | Skeleton loading, dimensões fixas |
| FID alto | Long tasks, JavaScript pesado | Code splitting, web workers |

## Saída

```markdown
## Diagnóstico

### LCP: [melhoria necessária]
- Causa: ...
- Solução: ...
- Impacto esperado: ...

### CLS: [ok/melhoria]
...

### FID/INP: [ok/melhoria]
...
```
