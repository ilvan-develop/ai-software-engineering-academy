# Módulo 08 - Arquitetura: Clean Architecture, DDD e SOLID

---

## 1. Por que arquitetura importa

Arquitetura é a **estrutura fundamental** de um sistema. São as decisões que, se tomadas errado, custam caro para mudar.
### O custo de uma arquitetura ruim
Arquitetura Ruim:
┌──────────────────────────────────────────┐

## 2. SOLID — Os 5 princípios

SOLID não é uma arquitetura — é um **conjunto de princípios** que boas arquiteturas seguem.
### S — Single Responsibility Principle
> Uma classe deve ter um, e apenas um, motivo para mudar.
// ❌ Ruim: Service faz tudo

## 3. Clean Architecture — A Regra da Dependência

Clean Architecture é uma arquitetura que organiza o código em **círculos concêntricos**.
### As camadas
┌─────────────────────┐
│   ENTITIES          │

## 4. DDD — Domain-Driven Design

DDD é uma abordagem que coloca o **domínio do negócio** no centro do desenvolvimento.
### Linguagem Ubíqua
> A mesma linguagem usada pelo negócio deve ser usada no código.
Negócio: "Um cliente pode abrir um chamado"

## 5. Arquitetura Hexagonal (Ports & Adapters)

A arquitetura hexagonal é uma variação da Clean Architecture que usa o conceito de **portas** e **adaptadores**.
┌───────────────────────┐
│     DOMAIN            │
│  (core do negócio)    │

## 6. Modular Monolith vs Microservices

### Modular Monolith
Um monólito **modularizado** — código em módulos bem definidos, mas deploy único.
Prós:                     Contras:
- Simplicidade            - Escala tudo junto

---
*Este artigo faz parte da formacao Arquitetura de Software Enterprise com IA*