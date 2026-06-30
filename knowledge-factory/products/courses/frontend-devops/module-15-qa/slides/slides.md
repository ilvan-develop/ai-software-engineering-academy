---
marp: true
theme: uncover
class:
  - lead
  - invert
---

# Módulo 15 — QA: Testes e Qualidade

## Módulo 15 - QA: Testes e Qualidade

---
## 1. Por que testar?

- Sem testes:
- ┌────────────────────────────────────────────┐
- │  Bug em produção: 2 dias pra achar         │
- │  Correção: 1 hora                          │
- │  Regressão: 3 bugs novos (quebra outras    │

---
## 2. Testes Unitários com Jest

- describe('UserService', () => {
- describe('create', () => {
- it('deve criar usuário com sucesso', async () => {
- // Arrange — preparar dados
- const dto: CreateUserDto = {

---
## 3. Testes de Integração com Supertest

- import * as request from 'supertest';
- import { Test } from '@nestjs/testing';
- import { INestApplication } from '@nestjs/common';
- describe('UserController (integration)', () => {
- let app: INestApplication;
- beforeAll(async () => {

---
## 4. Testes E2E com Playwright

- // playwright.config.ts
- import { defineConfig } from '@playwright/test';
- export default defineConfig({
- testDir: './e2e',
- fullyParallel: true,

---
## 5. Cobertura de Código

- // jest.config.ts
- export default {
- collectCoverageFrom: [
- 'src/**/*.service.ts',
- 'src/**/*.use-case.ts',

---
## 6. GitHub Actions com Testes

- name: CI
- on: [push, pull_request]
- jobs:
- test:
- runs-on: ubuntu-latest
- services:

---
## 7. TDD — Test-Driven Development

- Red:   Escreva um teste que falha
- Green: Faça o teste passar (código mínimo)
- Refactor: Melhore o código mantendo os verdes
- // 1. RED — Escrever teste primeiro

---
## Exemplo: text

```text
Sem testes:
  ┌────────────────────────────────────────────┐
  │  Bug em produção: 2 dias pra achar         │
  │  Correção: 1 hora                          │
  │  Regressão: 3 bugs novos (quebra outras    │
  │             funcionalidades)               │
  │  Confiança do time: baixa ("medo de mexer")│
  └────────────────────────────────────────────┘

Com testes:
  ┌────────────────────────────────────────────┐
  │  Bug em produção: 0 (teste pegou antes)    │
...
```

---
## Exemplo: text

```text
╱╲
         ╱  ╲        E2E (Playwright)
        ╱    ╲       Testes de fluxo completo
       ╱────────╲
      ╱          ╲   Integration (Supertest)
     ╱            ╲  Testes de API + banco
    ╱────────────────╲
   ╱                  ╲ Unitários (Jest)
  ╱                    ╲ Testes de serviço/função
 ╱──────────────────────╲
  MUITOS (rápidos)         POUCOS (lentos)
```

---
## Recap

- 1. Por que testar?
- 2. Testes Unitários com Jest
- 3. Testes de Integração com Supertest
- 4. Testes E2E com Playwright
- 5. Cobertura de Código
- 6. GitHub Actions com Testes
- 7. TDD — Test-Driven Development

---
# Obrigado!

## Perguntas?
