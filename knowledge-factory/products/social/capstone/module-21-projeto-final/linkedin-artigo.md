==================================================
LINKEDIN — Artigo
==================================================

Titulo: Módulo 21 - Projeto Final: Enterprise SaaS de Gestão de Projetos e Tarefas: O Que Todo Arquiteto Deveria Saber


## 1. Visão Geral do Projeto

- O Projeto Final é a culminação de toda a jornada de 20 módulos. O aluno deve construir, de forma individual ou em squad de até 3 pessoas, uma plataforma **SaaS de Gestão de Projetos e Tarefas** completa — similar a um Trello/Asana/ClickUp simplificado, porém com arquitetura Enterprise real.
- O objetivo não é apenas "fazer funcionar". É demonstrar domínio sobre:
- Arquitetura limpa e modular (Módulo 08)

## 2. Escopo Completo

- Cadastro de empresas (tenants) com plano gratuito e trial de 14 dias
- Cadastro de usuários com convite por e-mail (fluxo de onboarding)
- Login com e-mail/senha + OAuth2 (Google/GitHub)

## 3. Requisitos Funcionais

- | ID | Requisito | Prioridade |
- |----|-----------|------------|
- | RF01.1 | Usuário deve se registrar com e-mail + senha | Alta |

## 4. Requisitos Não-Funcionais

- | Requisito | Meta | Medição |
- |-----------|------|---------|
- | Latência p95 de API | < 200ms | Grafana + Prometheus |

## 5. Stack Tecnológica

- | Camada | Tecnologia | Justificativa |
- |--------|-----------|---------------|
- | Backend | NestJS + TypeScript | Framework Enterprise com DI, módulos, guards, interceptors |


---

🔥 Gostou? Compartilhe e marque alguem que precisa ler isso.

#ArquiteturaDeSoftware #EngenhariaDeSoftware #CarreiraDev
