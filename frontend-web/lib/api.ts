// Cliente da API do backend O Vilao. O gabarito nunca chega aqui antes do submit.
const BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";
const V1 = `${BASE}/api/v1`;

async function req<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${V1}${path}`, {
    headers: { "Content-Type": "application/json" },
    cache: "no-store",
    ...init,
  });
  if (!res.ok) {
    let detail = res.statusText;
    try { detail = (await res.json()).detail ?? detail; } catch {}
    throw new Error(typeof detail === "string" ? detail : "Erro na requisicao");
  }
  return res.json() as Promise<T>;
}

export type Theme = {
  theme_id: string; slug: string; title: string; description: string;
  accent_color: string; is_philosophical: boolean;
};
export type Option = { option_id: string; text: string };
export type AttemptStart = {
  attempt_id: string; riddle_id: string; difficulty_level: number;
  scenario_context: string; riddle_text: string; options: Option[];
  total_time_seconds: number; session_signature: string; nonce: string; started_at: string;
};
export type ChallengePublic = {
  challenge_id: string; share_token: string; theme_title: string; accent_color: string;
  difficulty_level: number; custom_provocation: string | null; expires_at: string;
};
export type Score = {
  base_points: number; time_bonus: number; penalties: number;
  genius_multiplier: number; is_genius: boolean; final_score: number;
};
export type SubmitResult = {
  is_correct: boolean; quarantined: boolean; time_spent_seconds: number;
  score: Score; correct_answer: string | null; deduction_steps: string[];
};
export type Clue = { tier: number; clue_text: string; score_penalty_percent: number };
export type RankRow = {
  rank_position: number; user_id: string; accumulated_score: number;
  challenges_completed: number; genius_awards_count: number;
};

export const api = {
  listThemes: () => req<Theme[]>("/themes"),
  createChallenge: (body: {
    creator_user_id: string; theme_id: string; difficulty: number;
    provocation?: string | null; generate?: boolean; category?: string | null;
  }) => req<{ challenge_id: string; share_token: string; share_path: string; expires_at: string }>(
    "/challenges", { method: "POST", body: JSON.stringify(body) }),
  getChallenge: (token: string) => req<ChallengePublic>(`/challenges/${token}`),
  startAttempt: (token: string, solver_user_id: string) =>
    req<AttemptStart>(`/challenges/${token}/attempts`, {
      method: "POST", body: JSON.stringify({ solver_user_id }) }),
  consumeClue: (attemptId: string, tier: number) =>
    req<Clue>(`/attempts/${attemptId}/clues/${tier}`, { method: "POST" }),
  submit: (attemptId: string, chosen_option_id: string) =>
    req<SubmitResult>(`/attempts/${attemptId}/submit`, {
      method: "POST", body: JSON.stringify({ chosen_option_id }) }),
  ranking: (token: string) => req<RankRow[]>(`/challenges/${token}/ranking`),
};

// Identificador de jogador local (pseudo). Em producao viria da autenticacao.
export function localUserId(): string {
  if (typeof window === "undefined") return "00000000-0000-0000-0000-000000000000";
  const k = "vilao_user_id";
  let id = window.localStorage.getItem(k);
  if (!id) { id = crypto.randomUUID(); window.localStorage.setItem(k, id); }
  return id;
}
