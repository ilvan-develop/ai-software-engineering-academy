# Post Temático — Capítulo 1: Os 5 Erros ao Usar IA para Programar

## Post Principal

Você copiou código de IA hoje? Aposto que sim.

Agora me responda: você leu **cada linha** antes de dar commit?

Se a resposta for "não", você não está sozinho. 63% dos desenvolvedores já encontraram erros inesperados em código gerado por IA (Stack Overflow Survey). E 68% têm dificuldade em integrar IA efetivamente nos workflows.

O problema não é a ferramenta. É como usamos ela.

Depois de compilar dados do GitHub Copilot, Claude Code, OpenCode e pesquisa acadêmica (arXiv 2512.05239), mapeei os **5 erros que 90% dos devs cometem**:

**1️⃣ Confiar cegamente na saída da IA**
IA erra com confiança, não com hesitação. A sintaxe pode estar perfeita e a lógica completamente errada. Exemplo clássico: validar email só com `includes('@')`.

**2️⃣ Prompts vagos sem contexto**
"Melhore esse código" não diz nada. Prompt fraco → resposta fraca em escala industrial. Sempre use Contexto + Intenção + Formato Esperado.

**3️⃣ Pular code review e testes**
Código gerado por IA não passou por controle de qualidade nenhum. Trate como rascunho de estagiário, não como produto final.

**4️⃣ Ignorar configuração do projeto (AGENTS.md)**
Sem regras configuradas, código gerado por IA tem ~40% de erro. Com 12 regras, cai para ~3%. São 5 minutos de setup que economizam horas.

**5️⃣ Tratar IA como resposta final**
A primeira resposta raramente é a melhor. Itere com feedback direcionado. Refinamento separa o mediano do excelente.

O livro completo tem exemplos reais, código e exercícios para cada um desses erros. Link nos comentários.

#IA #Desenvolvimento #PromptEngineering #CodeReview #EngenhariaDeSoftware #CarreiraTech #Qualidade

---

## Variação A/B — Versão Provocativa

**Título:** Seu código gerado por IA é uma bomba-relógio

Você confiaria em um estagiário que trabalha 10x mais rápido que qualquer sênior, mas erra 40% das vezes?

Pois é isso que você faz quando usa IA sem validação.

Os números são implacáveis:
- Sem regras → ~40% de erro
- Com 4 regras básicas → ~11%
- Com 12 regras → ~3%

A diferença entre 40% e 3% são **5 minutos de configuração**.

O capítulo 1 do livro "IA para Desenvolvedores" detalha cada erro com exemplos reais de código (TypeScript, Python, JavaScript). Não é teoria. É código que você pode testar hoje.

Seu nome está no commit. A IA não assume responsabilidade.

#IA #Desenvolvimento #DevOps #PromptEngineering #QualidadeDeCodigo

---

## Variação A/B — Formato Carrossel (5 Slides)

**Slide 1 (Capa):**
📍 Os 5 Erros ao Usar IA para Programar

**Slide 2 (Erro 1):**
🚫 Confiar cegamente na saída da IA
→ Sintaxe perfeita ≠ lógica correta
→ Exemplo: validar email com `includes('@')`
→ Solução: leia cada linha, teste casos extremos

**Slide 3 (Erro 2):**
🚫 Prompts vagos sem contexto
→ "Melhore esse código" não funciona
→ Use: Contexto + Intenção + Formato
→ Exemplo de prompt estruturado no livro

**Slide 4 (Erro 3):**
🚫 Pular code review e testes
→ IA não revisa o próprio código
→ Trate como rascunho, não como produto final
→ Sempre peça testes junto com o código

**Slide 5 (Erro 4 + 5):**
🚫 Ignorar AGENTS.md + Tratar IA como resposta final
→ 5 min de setup → de 40% erro para 3%
→ Primeira resposta é ponto de partida
→ Itere com feedback, não reescreva do zero

**Prompt para imagem (carrossel):**
```
5 slides de carrossel para LinkedIn sobre erros ao usar IA para programar. Estilo clean, tech, fundo escuro gradiente azul marinho com detalhes em coral. Cada slide tem um número grande do erro (1 a 5), título em branco e bullet points. Layout profissional, tipografia sans-serif. Proporção 1:1 (quadrado) ou 4:5. Sem fotos de pessoas. Ícones minimalistas de código, engrenagens, alerta.
```

---

## Prompt para Imagem de Capa do Post

**Prompt:**
```
Imagem profissional para post de LinkedIn sobre erros ao programar com IA. Fundo escuro gradiente (#1A1A2E para #0F3460). Destaque visual "5 ERROS" em letras grandes no centro, coral (#E94560). Elementos visuais: um cérebro humano de um lado e uma engrenagem digital do outro, conectados por linhas de código. Ícone de alerta/atenção no canto superior direito. Estilo tech, moderno, limpo. Proporção 1:1 (quadrado para LinkedIn). Sem texto em português excessivo. Tipografia sans-serif bold.
```
