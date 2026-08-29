# Fatia 2 — Pipeline de IA (5 estágios)

**Backend 0.3.0.** Geração procedural de enigmas com provider desacoplado.
Validado ponta a ponta (36 testes + E2E) contra PostgreSQL 16 + Redis.

## Os 5 estágios (GDD 3.6) — `app/ai/`
1. **Prompt Assembly** (`prompt.py`) — injeta tema, categoria, dificuldade e semente; exige JSON estrito.
2. **SLM Generation** (`provider.py`) — `LLMProvider` abstrato com `MockProvider` (determinístico, zero download) e `OllamaProvider` (SLM local via HTTP), trocáveis por `LLM_PROVIDER`.
3. **Validação Simbólica** (`engine/validator.py`) — Quality Gate determinístico (reusado da Fatia 0).
4. **Auditoria de Pistas** (`clue_audit.py`) — hierarquia tiers 1,2,3 sem redundância.
5. **Ingestão & Cache** (`ingestion.py`) — grava em `riddle_templates`/`clues` e pré-aquece o Redis (payload público, **sem gabarito**).

Orquestrador: `pipeline.py` (`generate_and_ingest`), com retry até 5 tentativas variando a semente se o Quality Gate reprovar.

## Endpoints novos
| Método | Rota | Descrição |
|---|---|---|
| POST | `/api/v1/riddles/generate` | Forja e ingere um enigma (FR-002). |
| POST | `/api/v1/challenges` com `"generate": true` | Curadoria forja na hora e vincula ao desafio. |

## Trocar Mock → Ollama (quando a máquina comportar)
```bash
# 1) liberar RAM e subir o Ollama (perfil "ai" do compose)
docker compose -f infra/docker-compose.yml --profile ai up -d ollama
docker exec -it vilao_ollama ollama pull qwen2.5:3b     # ~2 GB (leve)

# 2) no .env
LLM_PROVIDER=ollama
OLLAMA_MODEL=qwen2.5:3b
```
Nenhuma linha de código muda — só a configuração. O restante do pipeline
(validação, auditoria, ingestão) é idêntico para ambos os providers.
