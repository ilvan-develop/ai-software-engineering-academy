# Módulo 14 - DevOps: Docker, CI/CD e Deploy

---

## 1. Por que DevOps importa

DevOps é a ponte entre o **código funcionando na máquina do dev** e o **código funcionando em produção**.
### O problema clássico
"Funciona na minha máquina" → "Não funciona no servidor"
Causas:

## 2. Docker — Containerização

### O que é um container
┌────────────────────────────────────────┐
│  CONTAINER                             │
│  ┌──────────────────────────────────┐  │

## 3. GitHub Actions — CI/CD

### Pipeline de CI (todo push)
name: CI
on:
push:

## 4. Variáveis de Ambiente

### .env.example (commitado)
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/db
# JWT

## 5. Estratégias de Deploy

### Blue-Green Deployment
Versão Azul (atual):
┌──────────┐
│ app:v1   │ ← Load Balancer (tráfego ativo)

## 6. Docker Compose para múltiplos ambientes

### docker-compose.override.yml (dev)
services:
api:
build:

---
*Este artigo faz parte da formacao Arquitetura de Software Enterprise com IA*