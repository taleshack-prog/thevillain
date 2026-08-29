"use client";
import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import PhoneFrame from "@/components/PhoneFrame";
import SkullDifficulty from "@/components/SkullDifficulty";
import { api, type ChallengePublic } from "@/lib/api";

export default function ConvitePage() {
  const { token } = useParams<{ token: string }>();
  const router = useRouter();
  const [ch, setCh] = useState<ChallengePublic | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    api.getChallenge(token).then(setCh).catch((e) => setError(e.message));
  }, [token]);

  async function copyLink() {
    try {
      await navigator.clipboard.writeText(window.location.href);
      setCopied(true); setTimeout(() => setCopied(false), 1500);
    } catch {}
  }

  if (error) return (
    <PhoneFrame><div className="grid h-full place-items-center p-8 text-center text-feedback-erro">{error}</div></PhoneFrame>
  );

  return (
    <PhoneFrame>
      <div className="flex h-full flex-col items-center p-6">
        {/* Moldura ornamental dourada */}
        <div className="relative mt-4 w-full rounded-2xl border-2 border-dourado-primario/70
                        bg-carvao-profundo p-6 text-center shadow-glow-ouro">
          <p className="font-mono text-[10px] uppercase tracking-[0.35em] text-dourado-claro">Desafio</p>
          <div className="my-4 grid h-24 w-24 mx-auto place-items-center rounded-full
                          bg-vilao-profundo text-4xl shadow-glow-vilao">🎭</div>
          <h1 className="font-display text-2xl font-bold text-texto-primario">O VILÃO</h1>
          <p className="mt-1 font-display text-base text-dourado-claro">
            {ch?.theme_title ?? "…"}
          </p>
          <div className="my-4 flex justify-center"><SkullDifficulty value={ch?.difficulty_level ?? 0} readOnly /></div>
          <p className="mx-auto max-w-xs text-sm italic text-texto-secundario">
            “{ch?.custom_provocation ?? "Consegues decifrar o enigma ou temes o fracasso?"}”
          </p>
        </div>

        <div className="mt-auto w-full space-y-3 pt-6">
          <button
            onClick={() => router.push(`/decifrar/${token}`)}
            className="w-full rounded-xl bg-heroi-esmeralda py-4 font-display text-lg font-semibold
                       text-carvao-profundo shadow-glow-heroi transition hover:brightness-110"
          >
            ACEITAR DESAFIO
          </button>
          <button
            onClick={copyLink}
            className="w-full rounded-xl border border-carvao-medio py-3 text-sm text-texto-secundario
                       transition hover:border-dourado-primario hover:text-dourado-primario"
          >
            {copied ? "Link copiado!" : "Compartilhar convite"}
          </button>
        </div>
      </div>
    </PhoneFrame>
  );
}
