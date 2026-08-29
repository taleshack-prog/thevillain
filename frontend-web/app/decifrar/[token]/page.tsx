"use client";
import { useCallback, useEffect, useRef, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";
import PhoneFrame from "@/components/PhoneFrame";
import Lives from "@/components/Lives";
import { api, localUserId, type AttemptStart, type SubmitResult } from "@/lib/api";

function fmt(sec: number) {
  const m = Math.floor(sec / 60), s = Math.max(0, Math.floor(sec % 60));
  return `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
}

export default function DecifrarPage() {
  const { token } = useParams<{ token: string }>();
  const [att, setAtt] = useState<AttemptStart | null>(null);
  const [remaining, setRemaining] = useState(180);
  const [cluesUsed, setCluesUsed] = useState<number[]>([]);
  const [clueTexts, setClueTexts] = useState<string[]>([]);
  const [result, setResult] = useState<SubmitResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);

  useEffect(() => {
    api.startAttempt(token, localUserId()).then((a) => {
      setAtt(a); setRemaining(a.total_time_seconds);
    }).catch((e) => setError(e.message));
  }, [token]);

  useEffect(() => {
    if (!att || result) return;
    timerRef.current = setInterval(() => setRemaining((r) => (r <= 0 ? 0 : r - 1)), 1000);
    return () => { if (timerRef.current) clearInterval(timerRef.current); };
  }, [att, result]);

  const doSubmit = useCallback(async (optionId: string) => {
    if (!att || busy || result) return;
    setBusy(true); setError(null);
    try {
      const res = await api.submit(att.attempt_id, optionId);
      setResult(res);
      if (timerRef.current) clearInterval(timerRef.current);
    } catch (e: any) { setError(e.message); }
    finally { setBusy(false); }
  }, [att, busy, result]);

  async function pedirPista() {
    if (!att) return;
    const nextTier = (cluesUsed.at(-1) ?? 0) + 1;
    if (nextTier > 3) return;
    try {
      const clue = await api.consumeClue(att.attempt_id, nextTier);
      setCluesUsed((c) => [...c, nextTier]);
      setClueTexts((t) => [...t, `Pista ${clue.tier} (−${Math.round(clue.score_penalty_percent * 100)}%): ${clue.clue_text}`]);
    } catch (e: any) { setError(e.message); }
  }

  if (error && !att) return (
    <PhoneFrame><div className="grid h-full place-items-center p-8 text-center text-feedback-erro">{error}</div></PhoneFrame>
  );
  if (!att) return (
    <PhoneFrame><div className="grid h-full place-items-center text-texto-secundario">Invocando o enigma…</div></PhoneFrame>
  );

  const lowTime = remaining <= 30;

  return (
    <PhoneFrame>
      <div className="flex h-full flex-col p-5">
        {/* HUD */}
        <div className="mb-3 flex items-center justify-between">
          <Lives remaining={Math.max(0, 3 - cluesUsed.length)} />
          <span className={`font-mono text-2xl tabular-nums ${lowTime ? "text-feedback-erro" : "text-texto-primario"}`}
                style={lowTime ? { textShadow: "0 0 10px rgba(192,57,43,0.8)" } : {}}>
            {fmt(remaining)}
          </span>
          <button
            onClick={pedirPista}
            disabled={cluesUsed.length >= 3 || !!result}
            className="rounded-lg border border-dourado-primario/60 px-3 py-1 font-mono text-xs
                       uppercase text-dourado-claro transition hover:bg-dourado-primario/10 disabled:opacity-40"
          >
            Pista
          </button>
        </div>
        <div className="rune-divider mb-4" />

        {/* Cenário + Charada */}
        <p className="mb-3 text-xs italic leading-relaxed text-texto-secundario">{att.scenario_context}</p>
        <p className="mb-4 font-display text-lg leading-snug text-texto-primario">{att.riddle_text}</p>

        {clueTexts.length > 0 && (
          <div className="mb-4 space-y-1">
            {clueTexts.map((c, i) => (
              <p key={i} className="rounded-md border border-dourado-primario/30 bg-carvao-profundo p-2 text-xs text-dourado-claro">{c}</p>
            ))}
          </div>
        )}

        {/* Grade 2x2 de opções */}
        <div className="mt-auto grid grid-cols-2 gap-3">
          {att.options.map((o, idx) => (
            <button
              key={o.option_id}
              onClick={() => doSubmit(o.option_id)}
              disabled={busy || !!result}
              className="rounded-xl border border-carvao-medio bg-carvao-profundo p-4 text-left text-sm
                         text-texto-primario transition hover:border-heroi-esmeralda hover:shadow-glow-heroi
                         disabled:opacity-50"
            >
              <span className="mr-2 font-mono text-heroi-neon">{idx + 1}.</span>{o.text}
            </button>
          ))}
        </div>

        {error && <p className="mt-3 text-center text-sm text-feedback-erro">{error}</p>}
      </div>

      {/* Veredito */}
      {result && (
        <div className="absolute inset-0 z-10 grid place-items-center bg-black/80 p-6 backdrop-blur-sm">
          <div className="w-full max-w-xs rounded-2xl border border-carvao-medio bg-carvao-escuro p-6 text-center">
            <h2 className={`font-display text-2xl font-bold ${result.is_correct ? "text-heroi-neon" : "text-feedback-erro"}`}>
              {result.is_correct ? "VITÓRIA" : "DERROTA"}
            </h2>
            {result.quarantined && (
              <p className="mt-1 text-xs text-dourado-claro">Resposta rápida demais — pontuação em quarentena.</p>
            )}
            {result.score.is_genius && (
              <p className="mt-1 font-mono text-xs text-dourado-primario">★ BÔNUS DE GÊNIO ×1.5</p>
            )}
            <p className="mt-3 font-mono text-4xl tabular-nums text-texto-primario">{result.score.final_score}</p>
            <p className="font-mono text-[10px] uppercase tracking-widest text-texto-secundario">pontos</p>
            <div className="rune-divider my-4" />
            <p className="text-xs text-texto-secundario">Resposta correta</p>
            <p className="mb-3 font-display text-base text-texto-primario">{result.correct_answer}</p>
            <div className="flex flex-col gap-2">
              <Link href={`/ranking`} className="rounded-xl bg-vilao-real py-3 font-display text-sm font-semibold text-white shadow-glow-vilao">
                Ver Ranking
              </Link>
              <Link href="/curador" className="rounded-xl border border-heroi-esmeralda py-3 text-sm text-heroi-esmeralda">
                Revanche — Vire o Vilão
              </Link>
            </div>
          </div>
        </div>
      )}
    </PhoneFrame>
  );
}
