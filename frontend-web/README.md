# frontend-web — Next.js 14 (App Router)

Telas **PC 16:9** da SSoT (Sprint P1+):
- Tela 5 — Construtor Avancado de Enigmas (FR-002/003/004)
- Tela 6 — Dashboard de Telemetria (FR-011)
- Tela 7 — Painel do Tier Filosofico (FR-016)

## Bootstrap (quando iniciar a fatia web)
```bash
npx create-next-app@14 . --ts --app --tailwind --eslint
```
Importe os tokens de `../design-system/tailwind.tokens.js` no `tailwind.config.js`
e as fontes **Cinzel / Inter / Roboto Mono**. Consuma a API em `NEXT_PUBLIC_API_URL`.
