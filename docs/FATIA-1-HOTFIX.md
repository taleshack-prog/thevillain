# Fatia 1 — Hotfix (ambiente + carregamento de .env + baseline Alembic)

Correções aplicadas após o primeiro deploy local:

1. **`.env` da raiz agora é lido de qualquer diretório** (`app/core/config.py`).
   Antes, rodar `alembic`/`uvicorn` de dentro de `backend/` ignorava o `.env` e
   caía nos defaults (localhost:5432), causando `password authentication failed`.

2. **Baseline Alembic aplica o `schema.sql` statement-a-statement**
   (`migrations/versions/0001_baseline_schema.py`). O driver `asyncpg` não aceita
   múltiplos comandos numa só chamada (erro SQLAlchemy `f405`).

3. **Porta do Postgres parametrizável** (`infra/docker-compose.yml` + `.env.example`):
   `POSTGRES_HOST_PORT` evita conflito com um PostgreSQL local já ocupando a 5432.

## Recuperação (a partir do estado com erros)

```bash
cd ~/Documentos/thevillain

# (a) aplicar o hotfix por cima do repo (overlay)
ZIP=~/Downloads/thevillain-fatia1-hotfix-env-alembic-porta-v1.zip
unzip -o "$ZIP" -d /tmp/vilao_hf && rsync -a /tmp/vilao_hf/thevillain/ ./ && rm -rf /tmp/vilao_hf

# (b) criar o virtualenv e instalar as dependências (resolve jsonschema/pytest/uvicorn)
cd backend && python3 -m venv .venv && source .venv/bin/activate
pip install -U pip && pip install -e ".[dev]" && cd ..

# (c) recriar o .env a partir do exemplo já corrigido
cp .env.example .env
#     >>> troque os segredos; se a 5432 estiver ocupada, veja o passo (d).

# (d) porta 5432 ocupada? diagnostique e escolha a 5433:
ss -ltnp | grep 5432 || sudo lsof -i :5432
sed -i 's/^POSTGRES_HOST_PORT=.*/POSTGRES_HOST_PORT=5433/' .env
sed -i 's#@localhost:5432/vilao#@localhost:5433/vilao#' .env

# (e) subir infra, migrar, popular e validar
docker compose -f infra/docker-compose.yml down
docker compose -f infra/docker-compose.yml up -d
cd backend
alembic upgrade head
python -m app.db.seed
pytest -q                 # 24 passam (23 unit + 1 integração)
uvicorn app.main:app --reload
```
