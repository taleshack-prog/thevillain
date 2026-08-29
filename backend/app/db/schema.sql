-- =============================================================================
-- O VILAO — Schema PostgreSQL 16 nativo (SSoT / TDD 4.2, Revisao 3.0)
-- Zero-Supabase. Particionamento por data + schema segregado pii_data (LGPD).
-- =============================================================================

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Esquema de dados privados para conformidade com LGPD (AES-256 em repouso).
CREATE SCHEMA IF NOT EXISTS pii_data;

-- 1. Temas dos Enigmas -------------------------------------------------------
CREATE TABLE IF NOT EXISTS riddle_themes (
    theme_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug VARCHAR(64) UNIQUE NOT NULL,
    title VARCHAR(128) NOT NULL,
    description TEXT NOT NULL,
    accent_color VARCHAR(7) DEFAULT '#8B5CF6',
    is_philosophical BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. Templates e Enigmas Homologados ----------------------------------------
CREATE TABLE IF NOT EXISTS riddle_templates (
    riddle_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    theme_id UUID NOT NULL REFERENCES riddle_themes(theme_id),
    difficulty_level SMALLINT CHECK (difficulty_level BETWEEN 1 AND 5),
    scenario_context TEXT NOT NULL,
    riddle_text TEXT NOT NULL,
    correct_answer VARCHAR(255) NOT NULL,       -- NUNCA trafega ao cliente
    distractors JSONB NOT NULL,                 -- Array de exatamente 3 strings
    deduction_steps JSONB NOT NULL,             -- 2 a 4 passos sequenciais
    symbolic_hash VARCHAR(64) NOT NULL,         -- Hash de integridade logica
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. Pistas Estruturadas -----------------------------------------------------
CREATE TABLE IF NOT EXISTS clues (
    clue_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    riddle_id UUID NOT NULL REFERENCES riddle_templates(riddle_id) ON DELETE CASCADE,
    tier_level SMALLINT CHECK (tier_level BETWEEN 1 AND 3),
    clue_text TEXT NOT NULL,
    score_penalty_percent NUMERIC(4,2) NOT NULL, -- 0.10 | 0.25 | 0.50
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. Desafios Criados pelos Usuarios ----------------------------------------
CREATE TABLE IF NOT EXISTS challenges (
    challenge_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    creator_user_id UUID NOT NULL,
    riddle_id UUID NOT NULL REFERENCES riddle_templates(riddle_id),
    custom_provocation VARCHAR(280),
    share_token VARCHAR(64) UNIQUE NOT NULL,
    expires_at TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. Sessoes de Tentativa (particionado por data) ---------------------------
CREATE TABLE IF NOT EXISTS riddle_attempts (
    attempt_id UUID DEFAULT gen_random_uuid(),
    challenge_id UUID NOT NULL REFERENCES challenges(challenge_id),
    solver_user_id UUID NOT NULL,
    started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    finished_at TIMESTAMPTZ,
    time_spent_seconds NUMERIC(6,2),
    clues_used SMALLINT[] DEFAULT '{}',
    is_correct BOOLEAN DEFAULT FALSE,
    session_hmac VARCHAR(64) NOT NULL,           -- HMAC-SHA256 da sessao
    created_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (attempt_id, created_at)
) PARTITION BY RANGE (created_at);

-- Particao DEFAULT garante gravacao mesmo antes das mensais serem criadas.
CREATE TABLE IF NOT EXISTS riddle_attempts_default
    PARTITION OF riddle_attempts DEFAULT;

-- 6. Resultados e Pontuacao --------------------------------------------------
CREATE TABLE IF NOT EXISTS results (
    result_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    attempt_id UUID NOT NULL,
    attempt_created_at TIMESTAMPTZ NOT NULL,     -- par com a chave particionada
    base_points INTEGER NOT NULL,
    time_bonus NUMERIC(6,2) NOT NULL,
    penalties NUMERIC(6,2) NOT NULL,
    genius_multiplier NUMERIC(3,2) DEFAULT 1.0,
    final_score INTEGER NOT NULL,
    calculated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 7. Ranking de Coortes ------------------------------------------------------
CREATE TABLE IF NOT EXISTS ranking_entries (
    entry_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    cohort_id UUID NOT NULL,
    user_id UUID NOT NULL,
    accumulated_score INTEGER DEFAULT 0,
    challenges_completed INTEGER DEFAULT 0,
    genius_awards_count INTEGER DEFAULT 0,
    rank_position INTEGER,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 8. Eventos de Telemetria (anonimizada, particionado por data) -------------
CREATE TABLE IF NOT EXISTS telemetry_events (
    event_id UUID DEFAULT gen_random_uuid(),
    session_hash VARCHAR(64) NOT NULL,           -- SHA-256(user_id + salt_rotativo)
    event_type VARCHAR(64) NOT NULL,
    payload JSONB NOT NULL,
    client_timestamp TIMESTAMPTZ NOT NULL,
    server_timestamp TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (event_id, server_timestamp)
) PARTITION BY RANGE (server_timestamp);

CREATE TABLE IF NOT EXISTS telemetry_events_default
    PARTITION OF telemetry_events DEFAULT;

-- 9. PII isolada (LGPD) — schema segregado ----------------------------------
CREATE TABLE IF NOT EXISTS pii_data.user_identities (
    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email_enc BYTEA,                 -- pgp_sym_encrypt(...) AES-256
    display_name VARCHAR(80),
    last_ip_enc BYTEA,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indices de apoio ao core loop e ranking -----------------------------------
CREATE INDEX IF NOT EXISTS idx_templates_theme       ON riddle_templates(theme_id);
CREATE INDEX IF NOT EXISTS idx_templates_active_diff ON riddle_templates(is_active, difficulty_level);
CREATE INDEX IF NOT EXISTS idx_clues_riddle_tier     ON clues(riddle_id, tier_level);
CREATE INDEX IF NOT EXISTS idx_challenges_token      ON challenges(share_token);
CREATE INDEX IF NOT EXISTS idx_ranking_cohort_score  ON ranking_entries(cohort_id, accumulated_score DESC);
