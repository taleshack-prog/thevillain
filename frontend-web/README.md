# frontend-web — O Vilão (Next.js 14)

As 4 telas do core loop (mobile 9:16), com a identidade **Dark Fantasy Chiaroscuro**,
consumindo a API FastAPI. Deploy 1 clique na Vercel.

## Telas
- `/curador` — Tela 1: seleção de tema, dificuldade (caveiras) e forja do desafio (FR-001/002).
- `/c/[token]` — Tela 3: card de convite compartilhável (FR-005).
- `/decifrar/[token]` — Tela 2: gameplay com cronômetro, vidas, pistas e veredito (FR-006/007/008).
- `/ranking` — Tela 4: ranking por coorte com pódio (FR-010/013).

## Rodar em desenvolvimento
```bash
cd frontend-web
cp .env.local.example .env.local     # aponta para a API (default http://localhost:8000)
npm install
npm run dev                          # http://localhost:3000
```
> A API (backend) precisa estar rodando. O CORS já libera http://localhost:3000.

## Build de produção / deploy
```bash
npm run build && npm start           # local
```
Na **Vercel**: importe o repositório, defina o **Root Directory** como `frontend-web`
e a variável `NEXT_PUBLIC_API_URL` apontando para a URL pública da sua API.

## Design
Tokens (cores/tipografia) em `tailwind.config.ts`, derivados da SSoT. Fontes
Cinzel/Inter/Roboto Mono carregadas via Google Fonts. Container 9:16 em `components/PhoneFrame.tsx`.
