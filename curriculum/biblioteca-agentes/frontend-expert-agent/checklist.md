# Checklist: Frontend Expert Agent

## Checklist de Qualidade Frontend

### Componentes
- [ ] Componente é Server Component (sem "use client")?
- [ ] Se precisa de interatividade, "use client" adicionado?
- [ ] Props tipadas com TypeScript?
- [ ] Loading states com Suspense?
- [ ] Erro states com Error Boundary?

### Performance
- [ ] Imagens com next/image?
- [ ] Fontes com next/font?
- [ ] Bundle splitting automático?
- [ ] Dynamic imports para componentes pesados?

### Acessibilidade
- [ ] ARIA labels em elementos interativos?
- [ ] Navegação por teclado funcional?
- [ ] Contraste de cores adequado?
- [ ] `role` correto nos componentes?

### Formulários
- [ ] Validação client-side com Zod?
- [ ] Mensagens de erro claras?
- [ ] Loading state no submit?
- [ ] Desabilitar botão durante submit?
