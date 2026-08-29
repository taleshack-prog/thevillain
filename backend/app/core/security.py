"""
Seguranca de sessao, anti-cheat temporal e pseudonimizacao LGPD (SSoT — TDD 4.7/4.8).

REGRA DE OURO: o ID/valor da resposta correta JAMAIS trafega ao cliente antes da
submissao final. As opcoes seguem acompanhadas apenas de um nonce aleatorio.
"""
from __future__ import annotations

import hashlib
import hmac
import secrets
import time

from app.core.config import get_settings

_settings = get_settings()


def new_nonce(n_bytes: int = 16) -> str:
    """Nonce aleatorio associado ao embaralhamento das opcoes no cliente."""
    return secrets.token_hex(n_bytes)


def sign_session(*parts: str) -> str:
    """
    Assinatura HMAC-SHA256 de uma acao de sessao (abertura de tela, consumo de
    pista, submissao). A chave e efemera e vinculada ao timestamp do servidor.
    """
    msg = "|".join(parts).encode("utf-8")
    key = _settings.session_hmac_secret.encode("utf-8")
    return hmac.new(key, msg, hashlib.sha256).hexdigest()


def verify_session(signature: str, *parts: str) -> bool:
    """Verificacao em tempo constante da assinatura de sessao."""
    expected = sign_session(*parts)
    return hmac.compare_digest(expected, signature)


def server_timestamp() -> float:
    """Timestamp autoritativo do servidor (o cliente nunca e fonte de verdade)."""
    return time.time()


def is_temporal_anomaly(time_spent_seconds: float, min_seconds: float = 3.5) -> bool:
    """TDD 4.7: resolucoes abaixo de 3.5s sao anomalia -> quarentena de pontuacao."""
    return time_spent_seconds < min_seconds


def pseudonymize(user_id: str, salt: str | None = None) -> str:
    """
    LGPD (TDD 4.8): session_hash = SHA-256(user_id + salt_rotativo). Via unica,
    irreversivel. Nenhum identificador direto e persistido em logs analiticos.
    """
    salt = salt if salt is not None else _settings.telemetry_salt
    return hashlib.sha256(f"{user_id}{salt}".encode("utf-8")).hexdigest()
