# Atalhos de desenvolvimento — O Vilao
.PHONY: up down schema seed api test

up:      ; docker compose -f infra/docker-compose.yml up -d
down:    ; docker compose -f infra/docker-compose.yml down
schema:  ; psql "$$DATABASE_URL" -f backend/app/db/schema.sql
seed:    ; cd backend && python -m app.db.seed
api:     ; cd backend && uvicorn app.main:app --reload
test:    ; cd backend && pytest -q
