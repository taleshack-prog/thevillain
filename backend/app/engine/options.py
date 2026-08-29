"""
Selagem de opcoes (SSoT — TDD 4.7, "Ocultacao Absoluta do Gabarito").

As 4 opcoes trafegam ao cliente apenas como (option_id opaco, texto). O option_id
e um HMAC-SHA256 derivado de (attempt_id, nonce, indice) — nao revela qual e a
correta e nao pode ser forjado sem o segredo do servidor. O id da opcao correta
fica retido no servidor (Redis) ate a submissao final.
"""
from __future__ import annotations

import hashlib
import hmac
import random
from dataclasses import dataclass


def _normalize(text: str) -> str:
    return " ".join(text.strip().casefold().split())


def derive_option_id(secret: str, attempt_id: str, nonce: str, index: int) -> str:
    msg = f"{attempt_id}|{nonce}|opt{index}".encode("utf-8")
    return hmac.new(secret.encode("utf-8"), msg, hashlib.sha256).hexdigest()[:16]


@dataclass(frozen=True)
class SealedOptions:
    options: list[dict]        # [{"option_id": str, "text": str}, ...] embaralhado
    correct_option_id: str     # retido no servidor — NUNCA enviado ao cliente


def build_sealed_options(
    secret: str,
    attempt_id: str,
    nonce: str,
    correct_answer: str,
    distractors: list[str],
    rng: random.Random | None = None,
) -> SealedOptions:
    """Monta e embaralha as 4 opcoes, selando cada uma com um option_id opaco."""
    if len(distractors) != 3:
        raise ValueError("Sao necessarios exatamente 3 distratores.")
    pool = [*distractors, correct_answer]
    (rng or random.SystemRandom()).shuffle(pool)

    options: list[dict] = []
    correct_id = ""
    correct_norm = _normalize(correct_answer)
    for idx, text in enumerate(pool):
        oid = derive_option_id(secret, attempt_id, nonce, idx)
        options.append({"option_id": oid, "text": text})
        if _normalize(text) == correct_norm:
            correct_id = oid
    if not correct_id:
        raise ValueError("Resposta correta ausente do conjunto de opcoes.")
    return SealedOptions(options=options, correct_option_id=correct_id)


def is_correct_submission(chosen_option_id: str, correct_option_id: str) -> bool:
    """Comparacao em tempo constante do id submetido contra o id correto retido."""
    return hmac.compare_digest(chosen_option_id, correct_option_id)
