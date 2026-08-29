// HUD de vidas em broches celtas verdes (identidade do Heroi).
export default function Lives({ total = 3, remaining }: { total?: number; remaining: number }) {
  return (
    <div className="flex items-center gap-1" aria-label={`Vidas: ${remaining} de ${total}`}>
      {Array.from({ length: total }).map((_, i) => {
        const alive = i < remaining;
        return (
          <span
            key={i}
            className="inline-block h-4 w-4 rounded-full border"
            style={{
              borderColor: alive ? "#39FF14" : "#2A2A2A",
              background: alive
                ? "radial-gradient(circle at 30% 30%, rgba(57,255,20,0.9), rgba(34,197,94,0.35))"
                : "transparent",
              boxShadow: alive ? "0 0 8px rgba(57,255,20,0.6)" : "none",
            }}
          />
        );
      })}
    </div>
  );
}
