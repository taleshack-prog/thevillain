-- Cria particoes mensais para riddle_attempts e telemetry_events.
-- Substitua :ano e :mes (ex.: psql -v ano=2026 -v mes=09 -f este_arquivo.sql).
-- Idempotente por mes.
DO $$
DECLARE
    ini DATE := make_date(:ano, :mes, 1);
    fim DATE := (make_date(:ano, :mes, 1) + INTERVAL '1 month')::date;
    suf TEXT := to_char(ini, 'YYYYMM');
BEGIN
    EXECUTE format(
      'CREATE TABLE IF NOT EXISTS riddle_attempts_%s PARTITION OF riddle_attempts
         FOR VALUES FROM (%L) TO (%L);', suf, ini, fim);
    EXECUTE format(
      'CREATE TABLE IF NOT EXISTS telemetry_events_%s PARTITION OF telemetry_events
         FOR VALUES FROM (%L) TO (%L);', suf, ini, fim);
END $$;
