# Fatia 3 — Front Web das 4 Telas do Core Loop (Next.js 14)

Optamos por **web-first (Next.js)** em vez de Expo: as 4 telas mobile 9:16 rodam
no navegador, com deploy 1 clique na Vercel — sem `node_modules` de React Native
nem emulador. O empacotamento nativo (Expo) fica como fatia futura opcional.

Validado: `npm run build` compila as 6 rotas e todas servem HTTP 200.

## Telas (`frontend-web/app/`)
| Rota | Tela | FR |
|---|---|---|
| `/curador` | 1 — Curador: tema, dificuldade (caveiras), forja | FR-001/002 |
| `/c/[token]` | 3 — Card de convite compartilhável | FR-005 |
| `/decifrar/[token]` | 2 — Gameplay: cronômetro, vidas, pistas, veredito | FR-006/007/008 |
| `/ranking` | 4 — Ranking por coorte com pódio | FR-010/013 |

Identidade **Dark Fantasy Chiaroscuro**: tokens em `tailwind.config.ts`, fontes
Cinzel/Inter/Roboto Mono, container 9:16 (`PhoneFrame`), HUD de vidas em broche
celta e dificuldade em caveiras. O gabarito só aparece no veredito (pós-submit).

## Rodar
```bash
cd frontend-web
cp .env.local.example .env.local     # NEXT_PUBLIC_API_URL=http://localhost:8000
npm install
npm run dev                          # http://localhost:3000  (backend precisa estar no ar)
```

## Deploy Vercel
Importe o repo, **Root Directory = frontend-web**, e defina `NEXT_PUBLIC_API_URL`
com a URL pública da API. `npm run build` já foi validado.

## Nota
A tela de ranking cria um desafio efêmero para consultar a coorte semanal (a rota
de ranking é vinculada a um `share_token`). Em produção o app já teria um token de
contexto; é um atalho consciente do MVP, documentado no código.
