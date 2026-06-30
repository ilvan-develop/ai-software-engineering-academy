==================================================
TWITTER/X — Thread
==================================================

🧵 Módulo 12 - Segurança

Uma thread para voce dominar esse conceito.

1. Por que segurança é o requisito mais importante:
→ Segurança não é uma feature — é um **pré-requisito**. Um sistema inseguro é um passivo, não um ativo
→ Falha de segurança típica:


2. OWASP Top 10 (2021):
→ As 10 vulnerabilidades mais críticas em aplicações web.
→ > Usuário acessa recursos que não deveria.


3. Autenticação com JWT:
→ 1. Usuário envia email + senha
→ 2. Servidor valida credenciais


4. Autorização com CASL (RBAC):
→ export type Action = 'manage' | 'create' | 'read' | 'update' | 'delete';
→ export type Subject = 'User' | 'Order' | 'Product' | 'Report' | 'all';


5. Rate Limiting:
→ Protege contra brute force, DDoS e abuso.
→ ThrottlerModule.forRoot([{


6. Headers de Segurança (Helmet + CSP):
→ import helmet from 'helmet';
→ // Configura automaticamente:


Curtiu? Salve e compartilhe! 🚀

#DevTips #Arquitetura
