# Módulo 15 - QA: Testes e Qualidade

---

## 1. Por que testar?

### O custo de não testar
Sem testes:
┌────────────────────────────────────────────┐
│  Bug em produção: 2 dias pra achar         │

## 2. Testes Unitários com Jest

### Estrutura de um teste
describe('UserService', () => {
describe('create', () => {
it('deve criar usuário com sucesso', async () => {

## 3. Testes de Integração com Supertest

import * as request from 'supertest';
import { Test } from '@nestjs/testing';
import { INestApplication } from '@nestjs/common';
describe('UserController (integration)', () => {

## 4. Testes E2E com Playwright

### Configuração
// playwright.config.ts
import { defineConfig } from '@playwright/test';
export default defineConfig({

## 5. Cobertura de Código

### Configuração do Jest
// jest.config.ts
export default {
collectCoverageFrom: [

## 6. GitHub Actions com Testes

name: CI
on: [push, pull_request]
jobs:
test:

---
*Este artigo faz parte da formacao Arquitetura de Software Enterprise com IA*