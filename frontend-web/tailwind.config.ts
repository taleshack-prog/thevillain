import type { Config } from "tailwindcss";

// Tokens derivados da SSoT (Dark Fantasy Chiaroscuro, Rev. 3.0).
const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        carvao: { profundo: "#1A1A1A", escuro: "#121212", medio: "#2A2A2A" },
        vilao: { real: "#6A3FA0", profundo: "#3D1F6E", neon: "#8B5CF6" },
        heroi: { esmeralda: "#22C55E", neon: "#39FF14" },
        dourado: { primario: "#D4AF37", claro: "#F0D98C" },
        texto: { primario: "#F5F5F5", secundario: "#9E9E9E" },
        feedback: { sucesso: "#27AE60", erro: "#C0392B" },
      },
      fontFamily: {
        display: ["Cinzel", "serif"],
        body: ["Inter", "system-ui", "sans-serif"],
        mono: ["Roboto Mono", "ui-monospace", "monospace"],
      },
      boxShadow: {
        "glow-vilao": "0 0 18px rgba(139,92,246,0.45)",
        "glow-heroi": "0 0 18px rgba(57,255,20,0.35)",
        "glow-ouro": "0 0 16px rgba(212,175,55,0.4)",
      },
    },
  },
  plugins: [],
};
export default config;
