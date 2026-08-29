# O Vilão — The Villain

> *"Wordle encontra Sherlock Holmes na corte de um lorde gótico-futurista."*

Jogo social **assíncrono** de duelos intelectuais e dedução lógica sob a estética
**Dark Fantasy Chiaroscuro**. O jogador alterna entre **Vilão** (arquiteto do dilema)
e **Herói** (decifrador sob pressão de tempo).

Este repositório segue como **Fonte Única de Verdade (SSoT)** os documentos de
`docs/` (PRD/GDD/TDD — Revisão 3.0). Nenhuma implementação pode violar a paleta,
a tipografia, o core loop de 6 etapas, a anatomia de 5 camadas do enigma, o motor
de pontuação com Bônus de Gênio ou o stack oficial.

## Stack oficial (TDD)

| Camada        | Tecnologia                                                        |
|---------------|-------------------------------------------------------------------|
| Frontend Web  | Next.js 14 (App Router)                                            |
| Mobile        | React Native + Expo                                               |
| API/Gateway   | FastAPI (Python 3.11 · AsyncIO · Uvicorn)                          |
| Banco         | PostgreSQL 16 nativo (particionamento + schema `pii_data`)         |
| Cache/Fila    | Redis 7 · Celery                                                   |
| Inferência IA | Ollama (SLM 3B / Mistral-7B-Instruct, GGUF INT4)                   |

### Metas não-funcionais
- Latência **P95 < 250 ms** em endpoints críticos.
- Custo de inferência **< R$ 0,001** por enigma.
- **Zero-Supabase**: persistência 100% em PostgreSQL nativo.
- **LGPD**: PII isolada em schema `pii_data` (AES-256 via `pgcrypto`); telemetria
  pseudonimizada com `SHA-256(user_id + salt_rotativo)`.

## Estrutura do monorepo

```
thevillain/
├── backend/          FastAPI + motores de validação e pontuação (P0 implementado)
├── frontend-web/     Next.js 14 — telas PC 16:9 (Sprint P1+)
├── mobile/           Expo — telas mobile 9:16 do core loop (Sprint P0+)
├── design-system/    Tokens de cor/tipografia derivados da SSoT (compartilhados)
├── assets/           Pipeline de arte (turnarounds, key art, mockups)
├── infra/            docker-compose, scripts de bootstrap
└── docs/             PRD / GDD / TDD / Pipeline (SSoT — somente leitura)
```

## Como subir o ambiente (dev)

```bash
cp .env.example .env                    # ajuste os segredos
docker compose -f infra/docker-compose.yml up -d   # Postgres 16 + Redis 7
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
psql "$DATABASE_URL" -f app/db/schema.sql          # aplica o schema
python -m app.db.seed                              # popula temas + enigmas-exemplo
uvicorn app.main:app --reload                      # API em http://localhost:8000
pytest                                             # testes (scoring + validador)
```

## Status por sprint (ver `docs/`)
- **P0 (dias 1–5):** core loop nas 4 telas mobile + endpoints FastAPI.
  - ✅ Fatia 0 — fundação (motores, schema, design system, infra)
  - ✅ Fatia 1 — persistência (SQLAlchemy 2.0 async + Alembic) + API do core loop
  - ✅ Fatia 2 — pipeline de IA (5 estágios; Mock + Ollama plugável)
  - ⬜ Fatia 3 — mobile Expo (4 telas 9:16)
  - ⬜ Fatia 4 — web Next.js (telas PC 16:9)
- **P1 (dias 6–10):** telemetria (FR-011) + particionamento PostgreSQL 16.
- **P2 (dias 11–15):** teste de estresse (coorte alfa 30) + calibração do Bônus de Gênio.

---
Hack Tech Farm · Documentação homologada em 29/08/2026.
