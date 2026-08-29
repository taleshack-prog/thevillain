"use client";
// Seletor de dificuldade em caveiras (1 a 5), identidade do Vilao.
export default function SkullDifficulty({
  value, onChange, readOnly = false,
}: { value: number; onChange?: (v: number) => void; readOnly?: boolean }) {
  return (
    <div className="flex gap-1.5" role="group" aria-label="Dificuldade">
      {[1, 2, 3, 4, 5].map((n) => {
        const active = n <= value;
        return (
          <button
            key={n}
            type="button"
            disabled={readOnly}
            onClick={() => onChange?.(n)}
            className={`text-2xl leading-none transition-transform ${readOnly ? "" : "hover:scale-110"}`}
            style={{
              filter: active ? "drop-shadow(0 0 6px rgba(139,92,246,0.8))" : "grayscale(1) opacity(0.35)",
            }}
            aria-label={`${n} caveira${n > 1 ? "s" : ""}`}
          >
            💀
          </button>
        );
      })}
    </div>
  );
}
