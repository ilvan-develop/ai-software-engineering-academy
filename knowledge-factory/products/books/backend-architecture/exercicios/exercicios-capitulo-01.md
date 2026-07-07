# Exercícios — Capítulo 1: Fundamentos de Arquitetura

> **Progressão:** Fácil → Médio → Difícil  
> **Total:** 4 exercícios

---

## Exercício 1 — Fácil: Identifique o Princípio SOLID

**Tema:** Reconhecimento dos 5 princípios SOLID

Para cada cenário abaixo, identifique qual princípio SOLID está sendo **violado**:

| # | Cenário | Princípio Violado |
|---|---------|-------------------|
| 1 | A classe `RelatorioService` cuida de gerar dados, formatar HTML, enviar email e logar acesso. | ? |
| 2 | Para adicionar um novo método de pagamento, é preciso modificar a classe `PagamentoProcessor` com um novo `if`. | ? |
| 3 | Uma classe `Passaro` tem método `voar()`. A subclasse `Pinguim` herda de `Passaro` e lança exceção em `voar()`. | ? |
| 4 | Um serviço de pedidos instancia diretamente `new PrismaOrderRepository()` em vez de receber uma interface. | ? |

**Resposta:** 1-SRP, 2-OCP, 3-LSP, 4-DIP

---

## Exercício 2 — Médio: Implemente uma Porta e Adaptador

**Tema:** Arquitetura Hexagonal — Ports & Adapters

Você tem a seguinte interface de repositório no domínio:

```typescript
export interface UsuarioRepository {
  findById(id: string): Promise<Usuario | null>;
  save(usuario: Usuario): Promise<void>;
  delete(id: string): Promise<void>;
}
```

**Tarefa:** Implemente um adaptador concreto `PrismaUsuarioRepository` que:
- Implementa a interface `UsuarioRepository`
- Usa o Prisma ORM para persistência
- Faz a conversão entre o modelo de domínio (`Usuario`) e o modelo de persistência do Prisma
- Inclui tratamento de erro para "não encontrado"

---

## Exercício 3 — Médio: Clean Architecture — Organize as Camadas

**Tema:** Clean Architecture — Regra da Dependência

Dado o seguinte código, indique em qual camada da Clean Architecture cada arquivo deve ficar:

```typescript
// Arquivo A
export class CriarPedidoUseCase {
  constructor(private repo: PedidoRepository) {}
  async execute(input: CriarPedidoInput): Promise<Pedido> {
    const pedido = Pedido.criar(input.clienteId, input.itens);
    return this.repo.save(pedido);
  }
}

// Arquivo B
export class Pedido {
  private constructor(
    readonly id: string,
    readonly clienteId: string,
    readonly itens: Item[],
    readonly status: StatusPedido,
  ) {}
  static criar(clienteId: string, itens: Item[]): Pedido { /* ... */ }
  cancelar(): void { /* com regras de negócio */ }
}

// Arquivo C
@Controller('/pedidos')
export class PedidoController {
  constructor(private criarPedido: CriarPedidoUseCase) {}
  @Post()
  async criar(@Body() dto: CriarPedidoDto) {
    return this.criarPedido.execute(dto);
  }
}
```

**Opções:** Entities | Use Cases | Controllers/Adaptadores | Frameworks

---

## Exercício 4 — Difícil: Refatore para DDD

**Tema:** Domain-Driven Design na prática

O código abaixo viola múltiplos princípios de DDD e Clean Architecture:

```typescript
class UserService {
  async createUser(data: any) {
    const hashedPassword = await bcrypt.hash(data.password, 10);
    const user = await prisma.user.create({
      data: {
        name: data.name,
        email: data.email,
        password: hashedPassword,
        role: 'USER',
        active: true,
      },
    });
    await sendEmail(user.email, 'Bem-vindo!');
    return user;
  }
}
```

**Tarefa:** Refatore seguindo DDD + Clean Architecture:
1. Crie uma entidade `Usuario` com regras de negócio (validação de email, nome não vazio)
2. Crie um Value Object `Email`
3. Crie uma interface `UsuarioRepository`
4. Crie um Use Case `CriarUsuarioUseCase`
5. O controller deve chamar o use case, não o service diretamente
