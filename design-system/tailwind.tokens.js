/**
 * Fragmento de tema Tailwind derivado da SSoT (Rev. 3.0).
 * Uso: import destes tokens no tailwind.config.js do frontend-web e do mobile.
 */
module.exports = {
  colors: {
    carvao: { profundo: "#1A1A1A", escuro: "#121212", medio: "#2A2A2A" },
    vilao:  { real: "#6A3FA0", profundo: "#3D1F6E", neon: "#8B5CF6" },
    heroi:  { esmeralda: "#22C55E", neon: "#39FF14" },
    dourado:{ primario: "#D4AF37", claro: "#F0D98C" },
    texto:  { primario: "#F5F5F5", secundario: "#9E9E9E" },
    feedback: { sucesso: "#27AE60", erro: "#C0392B" },
  },
  fontFamily: {
    display: ["Cinzel", "serif"],
    body: ["Inter", "system-ui", "sans-serif"],
    mono: ["Roboto Mono", "ui-monospace", "monospace"],
  },
};
