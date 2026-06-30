# Guia de Estilo Editorial

Padrão de tom, voz, gramática e formatação para TODO conteúdo gerado pela AI Software Engineering Academy.

## 1. Voz e Tom

| Aspecto | Padrão |
|---------|--------|
| Pessoa | 3ª pessoa ("o desenvolvedor", "o arquiteto") |
| Tom | Tecnico e didatico — claro sem sacrificar profundidade |
| Nivel | Assumir desenvolvedores junior/intermediario |
| Pronomes | "Voce" em exemplos praticos ("Voce pode usar isso quando...") |

## 2. Idioma

- **pt-BR** (primario) — todo conteudo de curso, livros, posts
- **en-US** (secundario) — codigo, nomes de variaveis, comandos, termos tecnicos sem traducao
- **NUNCA** misture idiomas na mesma frase

### Termos que NÃO traduzir:
✅ deploy, pipeline, onboarding, discovery, workshop, framework, endpoint, schema, token, query, benchmark, dashboard, roadmap, compliance, insight, feature, milestone, code review, pull request, merge, commit, staging, production

### Termos que traduzir OBRIGATORIAMENTE:
| Ingles | Portugues |
|--------|-----------|
| software architecture | arquitetura de software |
| requirement | requisito |
| stakeholder | parte interessada |
| non-functional requirement | requisito nao funcional |
| database | banco de dados |
| front-end | frontend |
| back-end | backend |
| user experience | experiencia do usuario |
| user interface | interface do usuario |
| design system | sistema de design |
| continuous integration | integracao continua |
| continuous delivery | entrega continua |
| quality assurance | garantia de qualidade |

## 3. Gramatica e Pontuacao

- **Acentos**: OBRIGATORIOS — acao, publico, conteudo, tecnico, pratico, didatico, ultimo, epoca, voce, etc
- **Virgula**: Use a virgula serial (Oxford) em listas: "A, B e C" (nao "A, B, e C")
- **Citacoes**: Use asteriscos *em vez de aspas* para enfase. Aspas duplas " " apenas para citacoes literais
- **Travessao**: Use -- (dois hifens) para substituir parenteses. Nao use travessao Unicode
- **Ponto final**: Sempre ao final de cada bullet point completo

## 4. Formatação de Codigo

```markdown
// Use blocos de codigo com linguagem especificada:
\`\`\`typescript
const foo: string = "bar";
\`\`\`

// Referencias a nomes de funcoes/variaveis NO TEXT:
Use crases: \`calculateTotal()\` retorna o valor...

// Comandos de terminal:
\`\`\`bash
npm run dev
\`\`\`
```

**Regras:**
- Sempre especifique a linguagem no bloco de codigo
- Codigo em inglês (variaveis, funcoes, comentarios)
- 2 espacos de indentacao (TypeScript)
- Maximum line length: 80 colunas no codigo, 120 no texto corrido

## 5. Estrutura de Aula

```
# Titulo da Aula
Subtitulo / Nivel / Duracao

## Objetivos
- bullet com verbo de acao (Ao final, voce sera capaz de...)

## [Secao 1]
Conceito -> Exemplo -> Analogia -> Exercicio

## [Secao 2]
...

## Resumo
3-5 bullets com os principais aprendizados

## Desafio
1 exercicio pratico que integra todos os conceitos

## Referencias
- Links uteis
- Leituras complementares
```

## 6. Convencoes de Nomenclatura

| Item | Convencao | Exemplo |
|------|-----------|---------|
| Modulos | `module-NN-nome-curto` | `module-01-mentalidade-enterprise` |
| Agentes | `funcao-agente` | `curriculum-architect` |
| Cursos | `nome-curso` | `fundamentos-enterprise` |
| Outputs | `tipo-produto` | `slides`, `exercicios`, `quiz` |
| Status | `pt-BR` | `em_andamento`, `publicado`, `arquivado` |
| Commits | conventional commits pt-BR | `feat: adiciona modulo de seguranca` |
| Branches | `tipo/nome-em-ingles` | `feat/product-discovery-module` |

## 7. Blocos Especiais

### Dica
```
> Dica: Use isso quando voce precisa otimizar uma query N+1...
```

### Atencao (Warning)
```
> Atencao: Esse padrao pode causar vazamento de memoria se...
```

### Exemplo
```
Exemplo pratico:
- Contexto: Voce tem um sistema de e-commerce...
- Problema: O checkout esta lento...
- Solucao: Implementar cache com Redis...
```

## 8. Imagens e Diagramas

- Diagramas em ASCII dentro de blocos de codigo
- Sugestoes de diagramas entre colchetes: `[diagrama: fluxo de autenticacao JWT]`
- Prompts DALL-E/Midjourney salvos em `assets/cover-prompt.txt`
- Imagens finais (PNG) em `knowledge-factory/products/books/<id>/assets/`

## 9. Tamanhos

| Output | Tamanho maximo |
|--------|---------------|
| Aula completa | 10-20 paginas |
| Slide | 15 slides |
| Post LinkedIn | 1.200-1.800 caracteres |
| Artigo LinkedIn | 800-1.500 palavras |
| Newsletter | 5 min de leitura |
| Capitulo de livro | 15-30 paginas |
| Videoaula | 10-20 min |
| Workshop 4h | 20-30 slides + dinamicas |
| Workshop 8h | 40-50 slides + dinamicas |
| Exercicio facil | 5-10 min |
| Exercicio medio | 15-30 min |
| Exercicio dificil | 30-60 min |
| Mini-projeto | 2-4h |
| Projeto final | 40h |

## 10. Checklist de Qualidade

Antes de publicar, TODO conteudo deve passar por:

- [ ] Tom e voz consistentes com este guia
- [ ] pt-BR com acentos e gramatica corretos
- [ ] Codigo testado e funcionando
- [ ] Links validos
- [ ] Termos tecnicos em ingles com crases
- [ ] Diagramas sugeridos ou incluidos
- [ ] Exercicios com gabarito
- [ ] Quiz com alternativas plausiveis e explicacao
- [ ] Revisao por segundo agente (peer review)
- [ ] Status atualizado em curriculum/status.yaml
