"""
Camada de inferencia desacoplada (Estagio 2 do pipeline — GDD 3.6).

`LLMProvider` e a interface; `MockProvider` gera enigmas deterministicos sem
dependencia externa (para dev/CI/maquinas sem RAM), e `OllamaProvider` chama um
SLM local via HTTP. A troca e feita por configuracao (LLM_PROVIDER), sem alterar
o restante do pipeline.
"""
from __future__ import annotations

import abc
import hashlib
import json
import random
from typing import Any

import httpx


class LLMProvider(abc.ABC):
    """Contrato: recebe um prompt e devolve um payload de enigma (dict) em JSON."""

    name: str = "base"

    @abc.abstractmethod
    async def generate_riddle(self, prompt: str, *, seed: int) -> dict[str, Any]:
        ...


# ----------------------------------------------------------------------------
# Mock deterministico — nao baixa modelo, ideal para desenvolvimento e testes.
# ----------------------------------------------------------------------------
class MockProvider(LLMProvider):
    """
    Gera um enigma logico-dedutivo valido e deterministico a partir da seed.
    Constroi um problema simples ("qual selo/bau/cofre") cuja resposta e unica,
    com 3 distratores distintos, 2-4 passos e exatamente 3 pistas hierarquicas.
    Passa no Quality Gate por construcao.
    """

    name = "mock"

    _NOUNS = ["Selo", "Bau", "Cofre", "Portao", "Calice", "Grimorio"]
    _MATERIALS = ["de Prata", "de Bronze", "de Chumbo", "de Ebano", "de Ossos", "de Ambar"]
    _SCENES = [
        "Na cripta esquecida sob a abadia, quatro relicarios repousam sob a poeira dos seculos.",
        "No salao do trono em ruinas, sombras densas envolvem quatro artefatos ancestrais.",
        "Diante do altar profanado, quatro objetos aguardam o olhar atento do decifrador.",
    ]

    async def generate_riddle(self, prompt: str, *, seed: int) -> dict[str, Any]:
        rng = random.Random(seed)
        noun = rng.choice(self._NOUNS)
        mats = rng.sample(self._MATERIALS, 4)
        correct = f"{noun} {mats[0]}"
        distractors = [f"{noun} {m}" for m in mats[1:]]
        scene = rng.choice(self._SCENES)
        return {
            "scenario": scene + " Apenas um deles guarda a verdade sem contradizer o testamento.",
            "riddle": (
                f"Entre os quatro, somente o {correct} mantem a inscricao coerente. "
                "Qual objeto o decifrador deve escolher?"
            ),
            "correct_answer": correct,
            "distractors": distractors,
            "deduction_steps": [
                "Regra mestra: no maximo uma inscricao diz a verdade.",
                f"Somente o {correct} deixa as demais inscricoes falsas ao mesmo tempo.",
                "As outras escolhas gerariam duas verdades simultaneas, violando a regra.",
            ],
            "clues": [
                {"tier": 1, "text": "Se duas inscricoes concordam num cenario, ele so vale se ambas forem falsas."},
                {"tier": 2, "text": "Elimine os objetos cujas inscricoes se tornam verdadeiras juntas."},
                {"tier": 3, "text": f"Procure o unico objeto onde tudo e mentira, exceto ele: o {correct}."},
            ],
        }


# ----------------------------------------------------------------------------
# Ollama — SLM local via HTTP. Plugavel; so exige o servico e o modelo baixados.
# ----------------------------------------------------------------------------
class OllamaProvider(LLMProvider):
    """Chama /api/generate do Ollama em modo JSON estrito. Requer o servico ativo."""

    name = "ollama"

    def __init__(self, base_url: str, model: str, timeout: float = 120.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout

    async def generate_riddle(self, prompt: str, *, seed: int) -> dict[str, Any]:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "format": "json",     # forca saida JSON
            "stream": False,
            "options": {"seed": seed, "temperature": 0.7},
        }
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            resp = await client.post(f"{self.base_url}/api/generate", json=payload)
            resp.raise_for_status()
            data = resp.json()
        raw = data.get("response", "").strip()
        return json.loads(raw)   # pode levantar JSONDecodeError -> tratado no pipeline


def build_provider(name: str, *, base_url: str, model: str) -> LLMProvider:
    """Fabrica o provider conforme LLM_PROVIDER ('mock' | 'ollama')."""
    key = (name or "mock").lower()
    if key == "ollama":
        return OllamaProvider(base_url=base_url, model=model)
    return MockProvider()
