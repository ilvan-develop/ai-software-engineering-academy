# Projeto Módulo 12 — Auditoria de Segurança

## Objetivo

Realizar uma auditoria de segurança completa em um sistema e produzir relatório com score, riscos e plano de ação.

## Contexto

Você foi contratado como Security Expert para auditar o sistema de **transferências bancárias** de um fintech.

O código encontrado:

```typescript
// app.module.ts
@Module({
  imports: [
    ThrottlerModule.forRoot([{ ttl: 60000, limit: 1000 }]),
  ],
})
export class AppModule {}

// auth.service.ts
async validateUser(email: string, password: string) {
  const user = await prisma.user.findUnique({ where: { email } });
  if (!user) return null;

  // Comparação insegura
  if (user.password === password) {
    const token = jwt.sign(
      { userId: user.id },
      'minha-chave-super-secreta',
      { expiresIn: '30d' }
    );
    return { token };
  }
  return null;
}

// transfer.controller.ts
@Post('/transfer')
@UseGuards(JwtAuthGuard)
async transfer(@Body() dto: TransferDto, @Req() req) {
  const origin = await this.accountRepo.findById(dto.fromAccountId);
  const destination = await this.accountRepo.findById(dto.toAccountId);

  if (!origin || !destination) {
    throw new NotFoundException('Conta não encontrada');
  }

  // Sem validação de saldo!
  origin.balance -= dto.amount;
  destination.balance += dto.amount;

  await this.accountRepo.save(origin);
  await this.accountRepo.save(destination);

  return { success: true };
}

// .env
DATABASE_URL=postgresql://admin:Admin123!@localhost:5432/fintech
JWT_SECRET=minha-chave-super-secreta
```

## Entregáveis

### 1. Relatório de Auditoria

Identifique todas as vulnerabilidades e classifique:

| # | Vulnerabilidade | Gravidade | Localização | Correção |
|---|----------------|-----------|-------------|----------|
| 1 | ... | ... | ... | ... |

### 2. Score Geral

Calcule o score de segurança (0-10) baseado nas dimensões:
- Autenticação
- Autorização
- Validação de entrada
- Rate limiting
- Secrets management
- Headers de segurança

### 3. Plano de Ação

Priorize as correções por gravidade.

### 4. Implementação Corrigida

Reescreva os arquivos comprometidos com as correções aplicadas.

## Critérios de avaliação

- [ ] Mínimo 8 vulnerabilidades identificadas
- [ ] Classificação correta (Blocker a Minor)
- [ ] Score calculado e justificado
- [ ] Código corrigido sem erros
- [ ] Plano de ação com prazos realistas
