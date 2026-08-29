"use client";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import PhoneFrame from "@/components/PhoneFrame";
import SkullDifficulty from "@/components/SkullDifficulty";
import { api, localUserId, type Theme } from "@/lib/api";

export default function CuradorPage() {
  const router = useRouter();
  const [themes, setThemes] = useState<Theme[]>([]);
  const [themeId, setThemeId] = useState<string>("");
  const [difficulty, setDifficulty] = useState(2);
  const [provocation, setProvocation] = useState("Ousas decifrar meu enigma?");
  const [generate, setGenerate] = useState(true);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    api.listThemes().then((t) => {
      setThemes(t);
      if (t.length) setThemeId(t[0].theme_id);
    }).catch((e) => setError(e.message));
  }, []);

  const theme = themes.find((t) => t.theme_id === themeId);

  async function forjar() {
    setLoading(true); setError(null);
    try {
      const res = await api.createChallenge({
        creator_user_id: localUserId(),
        theme_id: themeId,
        difficulty,
        provocation,
        generate,
      });
      router.push(`/c/${res.share_token}`);
    } catch (e: any) {
      setError(e.message); setLoading(false);
    }
  }

  return (
    <PhoneFrame>
      <div className="flex h-full flex-col p-6">
        <header className="mb-5 flex items-center gap-3">
          <div className="grid h-11 w-11 place-items-center rounded-full bg-vilao-profundo
                          text-lg shadow-glow-vilao">🎭</div>
          <div>
            <p className="font-mono text-[10px] uppercase tracking-widest text-vilao-neon">O Vilão</p>
            <h1 className="font-display text-xl font-semibold text-texto-primario">Curador</h1>
          </div>
        </header>

        <label className="mb-2 font-mono text-[11px] uppercase tracking-widest text-texto-secundario">
          Tema Gótico
        </label>
        <div className="mb-4 flex gap-2 overflow-x-auto pb-1">
          {themes.map((t) => {
            const on = t.theme_id === themeId;
            return (
              <button
                key={t.theme_id}
                onClick={() => setThemeId(t.theme_id)}
                className={`shrink-0 rounded-lg border px-3 py-2 text-sm transition ${
                  on ? "border-vilao-neon bg-vilao-profundo/40 text-texto-primario"
                     : "border-carvao-medio text-texto-secundario"}`}
                style={on ? { boxShadow: "0 0 12px rgba(139,92,246,0.4)" } : {}}
              >
                {t.title}
              </button>
            );
          })}
          {!themes.length && <span className="text-xs text-texto-secundario">Carregando temas…</span>}
        </div>

        <label className="mb-2 font-mono text-[11px] uppercase tracking-widest text-texto-secundario">
          Dificuldade
        </label>
        <div className="mb-5"><SkullDifficulty value={difficulty} onChange={setDifficulty} /></div>

        <label className="mb-2 font-mono text-[11px] uppercase tracking-widest text-texto-secundario">
          Provocação
        </label>
        <textarea
          value={provocation}
          onChange={(e) => setProvocation(e.target.value.slice(0, 280))}
          rows={2}
          className="mb-4 resize-none rounded-lg border border-carvao-medio bg-carvao-profundo
                     p-3 text-sm text-texto-primario outline-none focus:border-vilao-neon"
        />

        <label className="mb-5 flex items-center gap-2 text-sm text-texto-secundario">
          <input type="checkbox" checked={generate} onChange={(e) => setGenerate(e.target.checked)} />
          Forjar enigma novo (pipeline de IA)
        </label>

        {theme?.description && (
          <p className="mb-4 rounded-lg border border-carvao-medio bg-carvao-profundo p-3 text-xs italic text-texto-secundario">
            {theme.description}
          </p>
        )}

        {error && <p className="mb-3 text-sm text-feedback-erro">{error}</p>}

        <div className="mt-auto">
          <button
            onClick={forjar}
            disabled={loading || !themeId}
            className="w-full rounded-xl bg-gradient-to-r from-vilao-profundo to-vilao-real py-4
                       font-display text-lg font-semibold text-white shadow-glow-vilao
                       transition hover:from-vilao-real hover:to-vilao-neon disabled:opacity-50"
          >
            {loading ? "FORJANDO…" : "FORJAR DESAFIO & PROVOCAR"}
          </button>
        </div>
      </div>
    </PhoneFrame>
  );
}
