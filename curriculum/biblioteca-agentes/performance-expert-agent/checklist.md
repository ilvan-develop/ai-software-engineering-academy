# Checklist: Performance Expert Agent

## Frontend
- [ ] LCP < 2.5s (Largest Contentful Paint)
- [ ] FID < 100ms (First Input Delay)
- [ ] CLS < 0.1 (Cumulative Layout Shift)
- [ ] Imagens otimizadas (WebP, lazy loading)
- [ ] Fontes com next/font (auto-otimizadas)
- [ ] Bundle size < 200KB (gzip)
- [ ] Code splitting ativo
- [ ] Suspense para componentes pesados

## Backend
- [ ] Response time < 200ms (p95)
- [ ] Queries N+1 eliminadas
- [ ] Cache (Redis) implementado onde apropriado
- [ ] Conexões com pool configurado
- [ ] Timeouts configurados

## Banco
- [ ] Query time < 100ms
- [ ] Index hit ratio > 99%
- [ ] Conexões simultâneas < 80% do pool
- [ ] Queries lentas identificadas (EXPLAIN ANALYZE)
- [ ] Paginação cursor-based (não offset)
