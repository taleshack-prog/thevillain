import Link from "next/link";
import PhoneFrame from "@/components/PhoneFrame";

export default function Home() {
  return (
    <PhoneFrame>
      <div className="flex h-full flex-col items-center justify-center gap-8 p-8 text-center">
        <div>
          <h1 className="font-display text-4xl font-bold tracking-wide text-texto-primario">
            O VILÃO
          </h1>
          <p className="mt-2 font-mono text-xs uppercase tracking-[0.3em] text-vilao-neon">
            The Villain
          </p>
        </div>
        <p className="max-w-xs text-sm text-texto-secundario">
          Forje armadilhas intelectuais. Decifre sob pressão. Vingue-se.
        </p>
        <div className="flex w-full max-w-xs flex-col gap-3">
          <Link
            href="/curador"
            className="rounded-xl bg-vilao-real py-3 font-display text-lg font-semibold
                       text-white shadow-glow-vilao transition hover:bg-vilao-neon"
          >
            FORJAR DESAFIO
          </Link>
          <Link
            href="/ranking"
            className="rounded-xl border border-carvao-medio py-3 font-body text-sm
                       text-texto-secundario transition hover:border-dourado-primario hover:text-dourado-primario"
          >
            Ver Ranking da Coorte
          </Link>
        </div>
      </div>
    </PhoneFrame>
  );
}
