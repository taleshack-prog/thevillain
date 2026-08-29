# Fatia 1 — Persistência + API do Core Loop

**Versão do backend:** 0.2.0 · Validada contra PostgreSQL 16 + Redis 7 reais (24 testes, E2E incluso).

## O que entra
- **Persistência**: SQLAlchemy 2.0 async (`app/db/base.py`, `app/db/models.py`) mapeada 1:1 ao schema congelado; Alembic com baseline que aplica o `schema.sql` (`migrations/`).
- **Sessões efêmeras** de tentativa em Redis (`app/core/redis.py`).
- **API do core loop** (6 etapas) sob `/api/v1`:

| Método | Rota | Etapa / FR |
|---|---|---|
| GET  | `/themes` | Curadoria — catálogo (FR-001) |
| POST | `/challenges` | Curadoria — forja o desafio (FR-001) |
| GET  | `/challenges/{token}` | Convite — preview público **sem enigma/gabarito** (FR-005) |
| POST | `/challenges/{token}/attempts` | Decifração — inicia, entrega opções seladas (FR-006/008) |
| POST | `/attempts/{id}/clues/{tier}` | Pistas progressivas 1–3 (FR-007) |
| POST | `/attempts/{id}/submit` | Veredito + score + gabarito revelado (FR-008/013) |
| GET  | `/challenges/{token}/ranking` | Ranking da coorte semanal (FR-010) |
| POST | `/attempts/{id}/rematch` | Revanche — inverte papéis (FR-009) |

## Regra de ouro (TDD 4.7) — verificada em teste
O texto/ID da resposta correta **nunca** trafega ao cliente antes da submissão.
As 4 opções vão como `{option_id, text}`, onde `option_id = HMAC-SHA256(segredo, attempt|nonce|índice)`.
O `correct_option_id` fica retido no Redis; o veredito compara em tempo constante.
Anti-cheat: submissões < 3,5 s vão para quarentena (score 0, fora do ranking).

## Como aplicar as migrações (recomendado)
```bash
cd backend && alembic upgrade head     # aplica o schema.sql via baseline 0001
python -m app.db.seed                   # popula temas + enigmas homologados
```
(O `psql -f app/db/schema.sql` continua válido como alternativa direta.)

## Rodar os testes
```bash
cd backend && pytest -q                 # 24 passam; o E2E se auto-pula sem DB/Redis
```
