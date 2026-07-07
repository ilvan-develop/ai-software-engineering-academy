# Módulo 08 — Exercícios

## Exercício 1: Identificando violações SOLID

Para cada código, identifique qual princípio SOLID está sendo violado e proponha a correção.

**Código A:**
```typescript
class UserService {
  createUser(data: any) { /* valida + salva + email */ }
  updateUser(id: string, data: any) { /* valida + salva + log */ }
  generateReport() { /* SQL + formata + exporta */ }
  sendNewsletter() { /* seleciona + envia */ }
}
```text

**Código B:**
```typescript
class DiscountCalculator {
  calculate(type: string, value: number) {
    if (type === 'black-friday') return value * 0.5;
    if (type === 'christmas') return value * 0.7;
    if (type === 'clearance') return value * 0.3;
  }
}
```text

**Código C:**
```typescript
class MySQLUserRepository {
  async findById(id: string): Promise<User> {
    return await mysql.query('SELECT * FROM users WHERE id = ?', [id]);
  }
}

class UserService {
  private repo = new MySQLUserRepository(); // dependência concreta
}
```markdown

---

## Exercício 2: Modelando com DDD

Modele o domínio abaixo usando DDD:

> "Um sistema de **gestão de pedidos** onde clientes criam pedidos com múltiplos itens, cada item tem produto, quantidade e preço. Pedidos podem ter descontos. Clientes têm limite de crédito. O sistema deve validar o limite antes de confirmar."

Identifique:
1. **Entities** (com IDs)
2. **Value Objects** (imutáveis, sem ID)
3. **Aggregates** (qual a raiz?)
4. **Repositories** (interfaces)
5. **Domain Services** (se necessário)
6. **Regras de negócio** em cada entidade

---

## Exercício 3: Estrutura hexagonal

Dado o seguinte requisito:

> "Sistema de **notificações** que pode enviar email, SMS e push notification. O sistema deve permitir adicionar novos canais sem modificar o código existente."

Projete a estrutura hexagonal:

1. **Porta** (interface) — defina a interface NotificationService
2. **Adaptadores** — implemente EmailNotification, SMSNotification, PushNotification
3. **Use Case** — implemente NotifyUserUseCase que recebe o canal via injeção
4. **Teste** — mostre como testar o use case com um adaptador mock

---

## Exercício 4: Monolith vs Microservices

Para cada cenário, recomende Modular Monolith ou Microservices e justifique:

| Cenário | Recomendação | Justificativa |
|---------|-------------|---------------|
| Startup com 3 devs, MVP em 3 meses | | |
| SaaS com 10 engenheiros, 2 domínios (vendas + logística) | | |
| Sistema global com 50 engenheiros, 5 times separados | | |
| API de processamento de pagamentos (precisa de certificação PCI) | | |
| Sistema interno de RH para 200 funcionários | | |

---

## Exercício 5: Refatorando para Clean Architecture

O código abaixo é um "macarrão" típico. Refatore seguindo Clean Architecture + DDD.

```typescript
// app.ts — TUDO misturado
import express from 'express';
import { PrismaClient } from '@prisma/client';

const app = express();
const prisma = new PrismaClient();

app.post('/users', async (req, res) => {
  const { name, email } = req.body;

  if (!email.includes('@')) {
    return res.status(400).json({ error: 'Email inválido' });
  }

  const exists = await prisma.user.findUnique({ where: { email } });
  if (exists) {
    return res.status(409).json({ error: 'Email já existe' });
  }

  const user = await prisma.user.create({
    data: { name, email, createdAt: new Date() }
  });

  await sendEmail(email, 'Bem-vindo!');

  return res.status(201).json(user);
});

app.listen(3000);
```text

Refatore criando:
1. `domain/entities/user.ts`
2. `domain/value-objects/email.ts`
3. `domain/repositories/user.repository.ts`
4. `application/use-cases/create-user.use-case.ts`
5. `infrastructure/persistence/prisma-user.repository.ts`
6. `presentation/controllers/user.controller.ts`
