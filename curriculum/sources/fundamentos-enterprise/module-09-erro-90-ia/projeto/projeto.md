# Projeto — Módulo 09

**Título:** Auditoria de Código Gerado por IA

**Duração:** 2-3 horas

**Formato:** Individual ou em duplas

---

## Cenário

Você é o **Tech Lead** de um time de 5 desenvolvedores júnior. Eles começaram a usar IA para programar e o código está sendo commitado com problemas. Sua missão é criar um **processo de qualidade** para código gerado por IA.

---

## Entregáveis

### 1. Política de Uso de IA (IA_USAGE.md)

Crie um documento que todo desenvolvedor deve ler antes de usar IA. Inclua:

- **Regras obrigatórias** (mínimo 5)
- **O que NÃO fazer** (anti-patterns)
- **Fluxo de aprovação** (quem revisa o que)
- **Checklist pré-commit** (5-7 itens)
- **Consequências** de violação

### 2. Template de AGENTS.md

Crie um template reutilizável de AGENTS.md para novos projetos. Deve incluir seções para:

- Stack tecnológica
- Regras de código (nomenclatura, estrutura, imports)
- Padrões de teste
- Padrões de commit
- Links para documentação do projeto

### 3. CI Check de Qualidade de IA

Crie uma especificação para um script/linter que:

1. Detecta funções geradas por IA (critérios: ausência de comentários, padrões repetitivos, nomes genéricos)
2. Verifica uso de algoritmos inseguros (MD5, SHA1, eval, etc.)
3. Valida que arquivos alterados têm testes correspondentes
4. Bloqueia commits que não passarem nos checks

### 4. Exemplo de Code Review de IA

Documente um exemplo real de revisão de código gerado por IA, mostrando:

- O código original (com erros)
- Os erros identificados e classificação (1-5)
- O código corrigido
- O que o desenvolvedor deveria ter perguntado no prompt

---

## Critérios de Avaliação

| Critério | Peso |
|----------|------|
| Documento IA_USAGE.md claro e acionável | 25% |
| Template AGENTS.md reutilizável | 20% |
| Especificação do CI check com critérios objetivos | 25% |
| Exemplo de code review realista e completo | 20% |
| Clareza, formatação e profissionalismo | 10% |

---

## Exemplo Parcial de IA_USAGE.md

```markdown
# IA Usage Policy

## Regras Obrigatórias
1. TODO código gerado por IA DEVE ser revisado linha a linha
2. TODO código gerado por IA DEVE ter testes automatizados
3. PROMPTS DEVEM seguir o formato Contexto + Intenção + Formato
4. NENHUM código gerado por IA pode ser commitado sem aprovação
5. TODO commit com código de IA DEVE ser identificado na mensagem
```text
