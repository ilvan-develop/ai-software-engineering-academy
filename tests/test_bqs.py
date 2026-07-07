"""Test BQS scoring functions."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from bqs_compute import (
    score_categoria,
    score_progressao_pedagogica,
    score_consistencia_terminologica,
    score_qualidade_exemplos,
    score_exercicios_avaliacoes,
    score_design_hierarquia_visual,
    score_qualidade_formatos,
    score_identidade_visual,
    score_qualidade_tipografica,
    score_design_informacao,
    score_acessibilidade_visual,
    score_consistencia_formatos,
    _try_llm,
)

SAMPLE_TEXT = """# Test Module

## Objetivos

Ao final deste modulo voce sera capaz de projetar e implementar sistemas.

## Conceito

Isso e um conceito fundamental sobre arquitetura enterprise.
`bounded context` e `domain event` sao termos tecnicos.

## Exemplo

```python
def process(order):
    return order.total * 0.1
```

Curtiu? Salve e compartilhe! 🚀

## Pratica

Implemente o exemplo acima.

## Resumo

Recapitulando: vimos conceitos, exemplos e pratica.

## Exercicios

Facil: faca X.
Intermediario: faca Y.
Dificil: faca Z.

Gabarito: a resposta e X.

Referencias: [docs](https://example.com)
"""


def test_score_categoria_routes_all_known_ids():
    ids = [
        "progressao_pedagogica",
        "consistencia_terminologica",
        "qualidade_exemplos",
        "exercicios_avaliacoes",
        "design_hierarquia_visual",
        "qualidade_formatos",
        "identidade_visual",
        "qualidade_tipografica",
        "design_informacao",
        "acessibilidade_visual",
        "consistencia_formatos",
        "estrutura_conteudo",
        "qualidade_markdown",
        "tom_legibilidade",
        "acessibilidade",
        "qualidade_tecnica",
    ]
    for cat_id in ids:
        r = score_categoria(SAMPLE_TEXT, cat_id, 5)
        assert "category_score" in r, f"{cat_id} missing category_score"
        assert 0 <= r["category_score"] <= 100, f"{cat_id} score out of range: {r['category_score']}"
        assert r["weight"] == 5, f"{cat_id} weight not set"


def test_score_progressao_pedagogica():
    r = score_progressao_pedagogica(SAMPLE_TEXT)
    assert 0 <= r["category_score"] <= 100
    assert "pp1" in r["criteria"]
    assert "pp2" in r["criteria"]


def test_score_consistencia_terminologica():
    r = score_consistencia_terminologica(SAMPLE_TEXT)
    assert 0 <= r["category_score"] <= 100
    assert "ct1" in r["criteria"]
    assert "ct2" in r["criteria"]


def test_score_qualidade_exemplos():
    r = score_qualidade_exemplos(SAMPLE_TEXT)
    assert 0 <= r["category_score"] <= 100
    assert "qe1" in r["criteria"]
    assert "qe2" in r["criteria"]


def test_score_exercicios_avaliacoes():
    r = score_exercicios_avaliacoes(SAMPLE_TEXT)
    assert 0 <= r["category_score"] <= 100
    assert "ea1" in r["criteria"]


def test_score_design_hierarquia_visual():
    r = score_design_hierarquia_visual(SAMPLE_TEXT)
    assert 0 <= r["category_score"] <= 100
    assert "dh1" in r["criteria"]


def test_score_qualidade_tipografica():
    r = score_qualidade_tipografica(SAMPLE_TEXT)
    assert 0 <= r["category_score"] <= 100
    assert "tp1" in r["criteria"]


def test_score_design_informacao():
    r = score_design_informacao(SAMPLE_TEXT)
    assert 0 <= r["category_score"] <= 100
    assert "di1" in r["criteria"]


def test_try_llm_fallback():
    r = _try_llm(SAMPLE_TEXT, "progressao_pedagogica", score_progressao_pedagogica)
    assert 0 <= r["category_score"] <= 100
    assert "note" in r


def test_score_qualidade_formatos_default():
    r = score_qualidade_formatos(SAMPLE_TEXT)
    assert 0 <= r["category_score"] <= 100


def test_score_identidade_visual_default():
    r = score_identidade_visual(SAMPLE_TEXT)
    assert 0 <= r["category_score"] <= 100


def test_score_acessibilidade_visual():
    r = score_acessibilidade_visual(SAMPLE_TEXT)
    assert 0 <= r["category_score"] <= 100


def test_score_consistencia_formatos():
    r = score_consistencia_formatos(SAMPLE_TEXT)
    assert 0 <= r["category_score"] <= 100


def test_empty_text_does_not_crash():
    r = score_categoria("", "progressao_pedagogica", 8)
    assert 0 <= r["category_score"] <= 100
