# Projeto Módulo 01 — Diagnóstico Enterprise

## Objetivo

Analisar um sistema existente e identificar quais conceitos Enterprise estão sendo ignorados, com plano de correção.

## Contexto

Uma startup de médio porte tem um sistema de gestão de projetos que começou como MVP e nunca foi refatorado. Agora:
- 200 empresas usam (multi-tenant improvisado — uma tabela `empresa_id`)
- 3.000 usuários ativos
- Crescendo 10% ao mês
- Sem testes
- Logs no console
- Backup manual do banco uma vez por semana
- Senhas armazenadas como MD5 (herança do passado)

## Entregáveis

### 1. Diagnóstico

Para cada conceito Enterprise, identifique:
- Situação atual
- Risco (Baixo/Médio/Alto/Crítico)
- Impacto se não for corrigido

| Conceito | Situação Atual | Risco | Impacto |
|----------|---------------|-------|---------|
| Escalabilidade | ... | ... | ... |
| Governança | ... | ... | ... |
| Manutenibilidade | ... | ... | ... |
| Observabilidade | ... | ... | ... |
| Segurança | ... | ... | ... |
| Compliance | ... | ... | ... |
| Multi-tenant | ... | ... | ... |
| Alta disponibilidade | ... | ... | ... |

### 2. Plano de ação priorizado

Para cada risco identificado, proponha:
1. Ação corretiva
2. Prioridade (P0/P1/P2)
3. Esforço estimado
4. Dependências

### 3. Regras de governança

Proponha 10 regras de governança que a startup deveria adotar a partir de agora, divididas em:
- Código (4 regras)
- Processo (3 regras)
- Dados (3 regras)

## Critérios de avaliação

- [ ] Todos os 8 conceitos Enterprise foram analisados
- [ ] Riscos classificados corretamente por gravidade
- [ ] Plano de ação é realista e priorizado
- [ ] Regras de governança específicas e acionáveis
- [ ] Diagnóstico demonstra compreensão dos conceitos do módulo
