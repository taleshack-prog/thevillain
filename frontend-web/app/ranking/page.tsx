"use client";
import { useEffect, useState } from "react";
import Link from "next/link";
import PhoneFrame from "@/components/PhoneFrame";
import { api, localUserId, type RankRow } from "@/lib/api";

export default function RankingPage() {
  const [rows, setRows] = useState<RankRow[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const me = typeof window !== "undefined" ? localUserId() : "";

  // Ranking e por coorte; usamos um token existente para consultar a coorte semanal.
  // Como a rota exige um share_token, criamos um desafio efemero apenas para leitura
  // se nenhum estiver em cache — na pratica o app ja teria contexto de token.
  useEffect(() => {
    async function load() {
      try {
        const themes = await api.listThemes();
        const res = await api.createChallenge({
          creator_user_id: localUserId(), theme_id: themes[0].theme_id, difficulty: 2,
        });
        const r = await api.ranking(res.share_token);
        setRows(r);
      } catch (e: any) { setError(e.message); }
      finally { setLoading(false); }
    }
    load();
  }, []);

  return (
    <PhoneFrame>
      <div className="flex h-full flex-col p-6">
        <header className="mb-4">
          <p className="font-mono text-[10px] uppercase tracking-widest text-dourado-claro">Coorte semanal</p>
          <h1 className="font-display text-2xl font-bold text-texto-primario">Ranking</h1>
        </header>

        {loading && <p className="text-sm text-texto-secundario">Reunindo os rivais…</p>}
        {error && <p className="text-sm text-feedback-erro">{error}</p>}

        {!loading && rows.length === 0 && (
          <p className="mt-6 text-center text-sm text-texto-secundario">
            Nenhuma pontuação nesta coorte ainda. Seja o primeiro a decifrar.
          </p>
        )}

        {rows[0] && (
          <div className="mb-4 rounded-2xl border-2 border-dourado-primario/70 bg-carvao-profundo p-4 text-center shadow-glow-ouro">
            <p className="text-2xl">👑</p>
            <p className="font-display text-lg text-dourado-claro">Líder da Coorte</p>
            <p className="font-mono text-2xl tabular-nums text-texto-primario">{rows[0].accumulated_score}</p>
            <p className="font-mono text-[10px] text-texto-secundario">{rows[0].user_id.slice(0, 8)}…</p>
          </div>
        )}

        <div className="flex-1 space-y-2 overflow-y-auto">
          {rows.map((r) => {
            const mine = r.user_id === me;
            return (
              <div
                key={r.user_id}
                className={`flex items-center justify-between rounded-lg border p-3 ${
                  mine ? "border-heroi-esmeralda bg-heroi-esmeralda/5 shadow-glow-heroi"
                       : "border-carvao-medio bg-carvao-profundo"}`}
              >
                <div className="flex items-center gap-3">
                  <span className="w-6 font-mono text-sm text-texto-secundario">{r.rank_position}.</span>
                  <span className="font-mono text-sm text-texto-primario">
                    {mine ? "VOCÊ" : `${r.user_id.slice(0, 8)}…`}
                  </span>
                  {r.genius_awards_count > 0 && <span title="Bônus de Gênio" className="text-dourado-primario">★{r.genius_awards_count}</span>}
                </div>
                <span className="font-mono tabular-nums text-texto-primario">{r.accumulated_score}</span>
              </div>
            );
          })}
        </div>

        <Link href="/curador" className="mt-4 rounded-xl bg-vilao-real py-3 text-center font-display font-semibold text-white shadow-glow-vilao">
          Forjar novo desafio
        </Link>
      </div>
    </PhoneFrame>
  );
}
