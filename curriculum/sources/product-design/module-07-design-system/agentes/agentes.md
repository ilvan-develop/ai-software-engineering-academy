# Agentes para o Módulo 07

## Agentes envolvidos

| Agente | Função no módulo |
|--------|------------------|
| Curriculum Architect | Estruturar os conceitos de Design System para devs |
| Technical Writer | Explicar cada conceito com exemplos de código reais |
| UI Designer | Revisar fidelidade visual e tokens |
| Reviewer | Validar precisão técnica e boas práticas |

## Instruções específicas

### Curriculum Architect

Ao planejar este módulo:
- Conectar cada conceito ao problema real: "como evitar que cada squad tenha seu próprio jeito de fazer botão?"
- Mostrar que Design System é sobre **processo e governança**, não só sobre componentes
- Garantir que o aluno saia capaz de **criar um DS mínimo** (React + Storybook + tokens)
- Enfatizar que DS é **produto**, não projeto — tem backlog, versionamento, manutenção

### Technical Writer

Ao escrever este módulo:
- Tom direto e prático — evitar jargão acadêmico
- Todo conceito teórico deve vir acompanhado de **código real** (TypeScript, React, CSS)
- Usar exemplos de Design Systems conhecidos (Shopify Polaris, Material UI, Adobe Spectrum) como referência
- Incluir códigos de componentes completos (Button, Input, Modal, Table, Select) com TypeScript
- Demonstrar configuração real de Storybook com stories tipados
- Mostrar exemplos de package.json com exports para tree-shaking

### UI Designer

Ao revisar este módulo:
- Os tokens de cor, tipografia e spacing seguem boas práticas de design?
- Os componentes implementados respeitam os tokens definidos?
- As escolhas de design (variantes, cores, tamanhos) são coerentes?
- A documentação visual (tabelas de variantes, exemplos) está clara?

### Reviewer

Ao revisar este módulo:
- Os componentes React estão corretos e seguem boas práticas (forwardRef, tipos, a11y)?
- O versionamento SemVer está explicado corretamente?
- As estratégias de tree-shaking e theming estão precisas?
- O migration guide example está correto e útil?
- A configuração do Storybook e Vite está funcional?
