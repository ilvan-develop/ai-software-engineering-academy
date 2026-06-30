## Introducao

# Módulo 15 — QA: Testes e Qualidade
**Código sem teste é legacy.**
---

---
## 1. Por que testar?

### O custo de não testar
Sem testes:
┌────────────────────────────────────────────┐
│  Bug em produção: 2 dias pra achar         │
│  Correção: 1 hora                          │
│  Regressão: 3 bugs novos (quebra outras    │
│             funcionalidades)               │
│  Confiança do time: baixa ("medo de mexer")│

---
## 2. Testes Unitários com Jest

### Estrutura de um teste
describe('UserService', () => {
describe('create', () => {
it('deve criar usuário com sucesso', async () => {
// Arrange — preparar dados
const dto: CreateUserDto = {
name: 'João Silva',
email: 'joao@email.com',

---
## 3. Testes de Integração com Supertest

import * as request from 'supertest';
import { Test } from '@nestjs/testing';
import { INestApplication } from '@nestjs/common';
describe('UserController (integration)', () => {
let app: INestApplication;
beforeAll(async () => {
const moduleRef = await Test.createTestingModule({
imports: [AppModule],

---
## 4. Testes E2E com Playwright

### Configuração
// playwright.config.ts
import { defineConfig } from '@playwright/test';
export default defineConfig({
testDir: './e2e',
fullyParallel: true,
retries: 1,
workers: 3,

---
## 5. Cobertura de Código

### Configuração do Jest
// jest.config.ts
export default {
collectCoverageFrom: [
'src/**/*.service.ts',
'src/**/*.use-case.ts',
'src/**/*.controller.ts',
'!src/**/*.module.ts',

---
## 6. GitHub Actions com Testes

name: CI
on: [push, pull_request]
jobs:
test:
runs-on: ubuntu-latest
services:
postgres:
image: postgres:16-alpine

---
## 7. TDD — Test-Driven Development

### Ciclo TDD
Red:   Escreva um teste que falha
Green: Faça o teste passar (código mínimo)
Refactor: Melhore o código mantendo os verdes
### Exemplo prático
// 1. RED — Escrever teste primeiro
describe('OrderService', () => {
it('não deve criar pedido com valor abaixo do mínimo', () => {

---
