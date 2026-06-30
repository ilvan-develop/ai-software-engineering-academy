# Relatório de Revisão: O erro que 90% das pessoas cometem usando IA para programar

**Nota geral:** 7/10
**Resumo:** Conteúdo bem estruturado, didático e relevante, com progressão lógica sólida e exemplos práticos eficazes. Porém, contém um erro técnico grave (regex rotulada como "RFC 5322" sem sê-lo) e inconsistências de fontes e formatação que comprometem a credibilidade. Com correções, está pronto para publicação.

## Issues

### [Blocker] Regex apresentada como "RFC 5322" não é compatível com RFC 5322
- **Localização:** Seção 5 (Erro 4 — "Exemplo concreto", linha 373) e Seção "Recursos didáticos sugeridos" (linha 375)
- **Descrição:** O prompt na linha 373 diz *"Valide email com regex RFC 5322, retorne booleano"*, mas a regex gerada (`^[^\s@]+@[^\s@]+\.[^\s@]+$`) é uma validação superficial que está longe de implementar a RFC 5322 — um padrão de mais de 200 páginas que cobre comentários, aspas, domain literals, caracteres especiais etc. O aluno que acreditar que essa regex é "RFC 5322" terá uma falsa sensação de segurança.
- **Sugestão:** Remova a menção "RFC 5322" do prompt. Use algo como *"Valide email com regex básica de formato"* ou *"Valide email seguindo boas práticas comuns"*. Se quiser manter a ambição de RFC 5322, aponte que a regex completa é complexa (centenas de caracteres) e que, na prática, usa-se validação por biblioteca ou envio de confirmação.

### [Major] Fonte do dado "~40% de erro" é imprecisa e mal atribuída
- **Localização:** Seção 1 (linhas 53-54) e Seção "Erro 4" (linha 251)
- **Descrição:** O dado central do artigo — que código gerado por IA tem ~40% de erro sem regras e ~3% com 12 regras — é atribuído a "Claude Code Pro Pack" (linha 54) e depois a "Claude Code Pro Pack Research (DEV.to)" (linha 251). Não há referência direta a um artigo específico do DEV.to. Para um conteúdo didático, esse dado é o pilar da argumentação; sem fonte verificável, o artigo perde credibilidade.
- **Sugestão:** Inclua o link direto para o artigo do DEV.to que documenta essa pesquisa. Se não existir, substitua por dados de fontes verificáveis (GitHub Copilot Metrics, estudos acadêmicos como arXiv 2512.05239, ou pesquisas da Microsoft/Google).

### [Major] Inconsistência no fator de melhoria (~10x vs. ~13,3x)
- **Localização:** Seção 1 (linha 54) e Seção "Erro 4" (linha 249)
- **Descrição:** Na introdução, a melhoria é descrita como "~10x". Na seção Erro 4, o mesmo dado é calculado como "~13,3x". 40/3 = 13,33, então 13,3x é o correto. A discrepância confunde o leitor atento.
- **Sugestão:** Unifique o valor para ~13x (arredondado) ou ~13,3x (exato) em ambas as ocorrências.

### [Major] Credenciais de banco de dados hardcoded no código corrigido
- **Localização:** Seção "Desafio final" (linhas 472-473)
- **Descrição:** O código corrigido contém `host="localhost", user="app", password="senha", database="appdb"` hardcoded. Para um módulo que ensina boas práticas com IA, ensinar código com credenciais fixas é contraditório. Um aluno pode copiar o exemplo sem perceber o problema.
- **Sugestão:** Substitua por variáveis de ambiente (`os.getenv("DB_HOST", "localhost")`) ou um arquivo de configuração. Adicione um comentário didático sobre boas práticas de segurança.

### [Major] Exemplo de validação de email "refinada" ainda é frágil
- **Localização:** Seção "Erro 5" (linhas 308-313)
- **Descrição:** A regex `^[^\s@]+@[^\s@]+\.[^\s@]+$` aceita domínios inválidos como `user@a..b` (ponto duplo) e `user@.com` (TLD sem domínio). Além disso, rejeita emails válidos como `user@sub.domínio.com` se houver caractere especial. É melhor que `includes('@')`, mas ainda é uma validação frágil.
- **Sugestão:** Troque por uma regex ligeiramente melhor como `/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/`, ou melhor ainda, use um exemplo que mostre o princípio sem fingir ser uma solução de produção. Adicione uma nota: *"Para validação real, prefira bibliotecas especializadas."*

### [Minor] HTML table misturado com Markdown
- **Localização:** Seção "Erro 2" (linhas 144-173)
- **Descrição:** A comparação entre prompt vago e estruturado usa HTML `<table>` com `<tr>` e `<td>`. Todas as outras tabelas do documento usam Markdown puro. A inconsistência de formato pode quebrar em alguns visualizadores de Markdown e destoa visualmente.
- **Sugestão:** Converta para Markdown ou use uma tabela Markdown padrão com duas colunas. Se o layout lado a lado for essencial, considere manter o HTML mas justifique a exceção.

### [Minor] Citação "TechTudo" sem referência completa
- **Localização:** Múltiplas seções (linhas 75, 136, 200, 291)
- **Descrição:** Quatro citações são atribuídas ao "TechTudo", mas apenas a referência principal (linha 491) aparece nas Leituras complementares. O leitor não sabe se são todas do mesmo artigo ou de artigos diferentes.
- **Sugestão:** Adicione o link do artigo específico ao lado de cada citação, ou use a mesma nota de rodapé. Se são citações do mesmo artigo (linha 491), mencione isso claramente.

### [Minor] Seção "Recursos didáticos sugeridos" está solta
- **Localização:** Linhas 363-381
- **Descrição:** Essa seção aparece entre a conclusão e o exercício prático, mas o conteúdo (código, diagrama, exercício mental) é essencialmente material complementar. O fluxo de leitura seria melhor servido se esse conteúdo fosse integrado ao exercício final ou movido para depois do desafio.
- **Sugestão:** Remova a seção autônoma e distribua o conteúdo: o código de validação pode ficar como parte do exercício prático; a sugestão de diagrama pode virar nota na conclusão; o mini-exercício mental pode abrir o exercício prático.

### [Minor] Prompt do exercício usa linguagem informal "Faz aí"
- **Localização:** Seção "Exercício prático" (linha 395)
- **Descrição:** O prompt "Faz aí uma função de login pra mim" é intencionalmente ruim para demonstrar o erro 2. Porém, o tom extremamente informal pode distrair alunos mais sérios ou não refletir prompts reais que desenvolvedores usam (que costumam ser mais técnicos, só que vagos).
- **Sugestão:** Considere um prompt ruim mais realista como *"Cria uma função de login em Node.js"* — que parece bom mas ainda é vago (falta definição de sucesso, tratamento de erros). O contraste com o prompt corrigido seria igualmente didático.

### [Minor] Diagrama fluxo usa arte ASCII pouco explicada
- **Localização:** Seção "Conclusão" (linhas 351-355)
- **Descrição:** O diagrama ASCII mostra o fluxo ideal, mas a seta de iteração (`↑` e `└─`) pode não ser clara para todos os leitores, especialmente em terminais ou visualizadores com fonte monoespaçada irregular.
- **Sugestão:** Adicione uma legenda: *"A seta de retorno indica que o refinamento pode gerar um novo ciclo de prompt → revisão → teste."* Ou, simplifique: use uma representação bullet-point do ciclo.

## Recomendação
- [ ] Aprovar
- [X] Aprovar com correções
- [ ] Revisar novamente

**Observação final:** O conteúdo é sólido e bem didático. Os problemas são localizados e de correção rápida. Prioridade máxima: corrigir a falsa atribuição RFC 5322 (blocker) e a inconsistência das fontes dos dados centrais (major). Feito isso, publique.
