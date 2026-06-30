# Prompt: Priorizar Backlog com RICE

Priorize as funcionalidades abaixo usando o framework RICE.

## Funcionalidades

| # | Funcionalidade | Reach | Impact | Confidence | Effort |
|---|----------------|-------|--------|------------|--------|
| 1 | [nome] | [usuários/mês] | [2x/1x/0.5x/0.25x] | [100%/80%/50%] | [personas-meses] |
| 2 | ... | ... | ... | ... | ... |

## Cálculo RICE

```
RICE = (Reach × Impact × Confidence) / Effort
```

- **Reach:** quantos usuários são impactados em um período
- **Impact:** 2x = massivo, 1x = alto, 0.5x = médio, 0.25x = baixo
- **Confidence:** 100% = dados concretos, 80% = dados parciais, 50% = educated guess
- **Effort:** esforço em pessoas-meses

## Saída

```markdown
## Priorização RICE

| Rank | Funcionalidade | Reach | Impact | Confidence | Effort | RICE Score |
|------|----------------|-------|--------|------------|--------|------------|
| 1    | ...            | ...   | ...    | ...        | ...    | ...        |

## Recomendações

### Fazer primeiro (P0)
- [Funcionalidade 1] — [justificativa]

### Fazer depois (P1)
- ...

### Não fazer agora (P2/P3)
- ...
```
