// Container 9:16 centralizado (mockup de celular) para as telas mobile do core loop.
export default function PhoneFrame({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen w-full flex items-center justify-center p-4">
      <div
        className="chiaroscuro relative w-full max-w-[420px] overflow-hidden rounded-[28px]
                   border border-carvao-medio bg-carvao-escuro shadow-2xl"
        style={{ aspectRatio: "9 / 16", maxHeight: "92vh" }}
      >
        <div className="absolute inset-0 overflow-y-auto">{children}</div>
      </div>
    </div>
  );
}
