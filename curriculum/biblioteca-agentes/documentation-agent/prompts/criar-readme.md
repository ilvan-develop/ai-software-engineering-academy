# Prompt: Criar README.md

Crie um README.md completo para o projeto abaixo.

## Projeto

- **Nome:** [nome]
- **Descrição:** [1-2 frases]
- **Stack:** [tecnologias]
- **Público-alvo:** [desenvolvedores, designers, etc.]

## Seções obrigatórias

```markdown
# [Nome do Projeto]

## Descrição
[Breve descrição]

## Stack
| Tecnologia | Versão |
|------------|--------|

## Pré-requisitos
- Node.js 20+
- Docker
- PostgreSQL 16

## Setup
```bash
git clone ...
npm install
cp .env.example .env
docker compose up -d
npm run dev
```

## Comandos
| Comando | Descrição |
|---------|-----------|
| npm run dev | Iniciar dev |
| npm run build | Build produção |
| npm run test | Rodar testes |

## Estrutura
```

## Regras

- README deve permitir setup em < 5 minutos
- Links funcionais e atualizados
- Português (para formação) ou inglês (para código)
- Badges no topo (build, coverage, license)
