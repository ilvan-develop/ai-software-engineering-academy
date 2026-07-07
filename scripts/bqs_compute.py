#!/usr/bin/env python3
"""
bqs_compute.py
Computa Book Quality Standard (BQS) scores para modulos e livros.
Automacao parcial (heuristica + estrutura), com suporte a override manual.
"""

import csv
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BQS_CORE = ROOT / "curriculum" / "bqs" / "bqs-core.yaml"
STATUS_PATH = ROOT / "curriculum" / "status.yaml"
METRICS_DIR = ROOT / "knowledge-factory" / "products" / "metrics"

SCORE_CSV = METRICS_DIR / "modules.csv"
REPORT_DIR = ROOT / "knowledge-factory" / "pipeline" / "reports"


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


BQS_CONFIG = load_yaml(BQS_CORE) if BQS_CORE.exists() else {"categories": []}
CATEGORIES_BY_ID = {c["id"]: c for c in BQS_CONFIG.get("categories", [])}


# ── LLM Scorer ──────────────────────────────────────────────────────────────


class LLMScorer:
    """LLM-based evaluator using OpenAI-compatible API with heuristic fallback."""

    DEFAULT_MODEL = "gpt-4o-mini"

    @classmethod
    def score(cls, text: str, cat_id: str) -> dict | None:
        cat = CATEGORIES_BY_ID.get(cat_id)
        if not cat:
            return None
        api_key = os.environ.get("OPENAI_API_KEY")
        if api_key:
            return cls._score_via_llm(text, cat, api_key)
        return None

    @classmethod
    def _score_via_llm(cls, text: str, cat: dict, api_key: str) -> dict:
        criteria = cat.get("criteria", [])
        criteria_lines = "\n".join(
            f"  - {c['id']}: {c['name']} ({c.get('weight_within', 20)}% weight): {c['description']}"
            for c in criteria
        )
        prompt = f"""You are a BQS (Book Quality Standard) evaluator. Rate the following educational content on the category "{cat['name']}".

Category description: {cat.get('description', '')}

Scoring criteria:
{criteria_lines}

For each criterion, return a score from 0-100 and a brief justification.

Content to evaluate:
---START---
{text[:8000]}
---END---

Respond ONLY with valid JSON in this exact format:
{{"category_score": <overall 0-100>, "criteria": {{"<criterion_id>": <score 0-100>, ...}}, "justifications": {{"<criterion_id>": "<brief justification>"}}}}
"""
        try:
            import urllib.request

            body = json.dumps({
                "model": cls.DEFAULT_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1,
                "response_format": {"type": "json_object"},
            }).encode()
            req = urllib.request.Request(
                "https://api.openai.com/v1/chat/completions",
                data=body,
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read())
            content = data["choices"][0]["message"]["content"]
            result = json.loads(content)
            result.setdefault("category_score", 75)
            result.setdefault("criteria", {})
            return {"category_score": round(float(result["category_score"]), 1), "criteria": result["criteria"], "llm": True}
        except Exception as e:
            return {"category_score": 75, "criteria": {}, "note": f"LLM error: {e}", "llm": False}


def extract_headings(text: str) -> list[dict]:
    headings = []
    for line in text.split("\n"):
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m:
            headings.append({"level": len(m.group(1)), "text": m.group(2).strip()})
    return headings


def extract_code_blocks(text: str) -> list[dict]:
    blocks = []
    pattern = re.compile(r"```(\w*)\n(.*?)```", re.DOTALL)
    for m in pattern.finditer(text):
        blocks.append({"lang": m.group(1), "code": m.group(2)})
    return blocks


def extract_links(text: str) -> list[str]:
    return re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)


def extract_images(text: str) -> list[dict]:
    imgs = []
    pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
    for m in pattern.finditer(text):
        imgs.append({"alt": m.group(1), "src": m.group(2)})
    return imgs


def count_words(text: str) -> int:
    return len(text.split())


def count_sentences(text: str) -> int:
    return len(re.findall(r"[.!?]+", text))


def estimate_reading_level(text: str) -> float:
    """Flesch Reading Ease adaptado para portugues (aproximacao)."""
    words = text.split()
    if len(words) < 10:
        return 100.0
    sentences = count_sentences(text)
    if sentences == 0:
        return 100.0
    syllables = sum(max(1, len(re.findall(r"[aeiou\-\u00e0-\u00fc]", w.lower()))) for w in words)
    return 206.835 - 1.015 * (len(words) / sentences) - 84.6 * (syllables / len(words))


def score_estrutura_conteudo(text: str, headings: list) -> dict:
    scores = {}
    # ec1: Hierarquia de titulos (sem saltos)
    if headings:
        levels = [h["level"] for h in headings]
        jumps = sum(1 for i in range(1, len(levels)) if levels[i] > levels[i - 1] + 1)
        scores["ec1"] = max(0, 100 - jumps * 20)
    else:
        scores["ec1"] = 0

    # ec2: Completude estrutural
    has_intro = bool(re.search(r"(introdu[cç][aã]o|objetivos|vis[aã]o\s*geral)", text[:2000], re.I))
    has_conclusion = bool(re.search(r"(conclus[aã]o|resumo|recapitulando)", text[-2000:], re.I))
    has_refs = bool(re.search(r"(refer[eê]ncias|bibliografia|recursos|links)", text[-2000:], re.I))
    present = sum([has_intro, has_conclusion, has_refs])
    scores["ec2"] = (present / 3) * 100

    # ec3: Progressao logica (heuristico: presenca de secoes numeradas)
    numbered_sections = len(re.findall(r"^\d+\.\s+", text, re.MULTILINE))
    scores["ec3"] = min(100, numbered_sections * 10 + 40) if numbered_sections > 0 else 30

    # ec4: Tamanho das secoes (entre headings, verificar variacao)
    section_sizes = []
    lines = text.split("\n")
    current_size = 0
    for line in lines:
        if re.match(r"^#{2,3}\s+", line):
            if current_size > 0:
                section_sizes.append(current_size)
            current_size = 0
        else:
            current_size += 1
    if section_sizes:
        mean_size = sum(section_sizes) / len(section_sizes)
        variance = sum(abs(s - mean_size) for s in section_sizes) / len(section_sizes)
        balance = max(0, 100 - (variance / mean_size) * 50)
        scores["ec4"] = min(100, balance)
    else:
        scores["ec4"] = 50

    # ec5: Transicoes (heuristica: palavras de transicao)
    transition_words = [
        "portanto", "alem disso", "contudo", "por outro lado",
        "primeiro", "segundo", "finalmente", "em seguida",
        "consequentemente", "por exemplo", "ou seja", "dessa forma",
    ]
    transition_count = sum(text.lower().count(w) for w in transition_words)
    # Esperado: pelo menos 1 transicao a cada 500 palavras
    word_count = count_words(text)
    expected = max(1, word_count / 500)
    scores["ec5"] = min(100, (transition_count / expected) * 100)

    total = sum(s * w for s, w in zip(scores.values(), [20, 20, 25, 15, 20])) / 100
    return {"category_score": round(total, 1), "criteria": scores}


def score_qualidade_markdown(text: str) -> dict:
    scores = {}
    # qm1: Markdown valido (basic check: unmatched fences)
    fences = len(re.findall(r"^```", text, re.MULTILINE))
    scores["qm1"] = 100 if fences % 2 == 0 else max(0, 100 - (fences % 2) * 30)

    # qm2: Code blocks com linguagem
    blocks = extract_code_blocks(text)
    if blocks:
        with_lang = sum(1 for b in blocks if b["lang"])
        scores["qm2"] = (with_lang / len(blocks)) * 100
    else:
        scores["qm2"] = 100  # no code blocks = no problem

    # qm3: Links (heuristic: check for empty or malformed)
    links = extract_links(text)
    if links:
        bad_links = sum(1 for _, url in links if not url or url.startswith("http://localhost"))
        scores["qm3"] = max(0, 100 - (bad_links / len(links)) * 100)
    else:
        scores["qm3"] = 100

    # qm4: Imagens referenciadas (heuristic)
    images = extract_images(text)
    if images:
        with_alt = sum(1 for img in images if img["alt"])
        scores["qm4"] = (with_alt / len(images)) * 100
    else:
        scores["qm4"] = 100

    # qm5: HTML bruto
    html_tags = len(re.findall(r"<[a-z]+[^>]*>", text))
    scores["qm5"] = max(0, 100 - html_tags * 5)

    total = sum(s * w for s, w in zip(scores.values(), [25, 20, 20, 15, 20])) / 100
    return {"category_score": round(total, 1), "criteria": scores}


def score_tom_legibilidade(text: str) -> dict:
    scores = {}
    words = text.split()
    sentences = count_sentences(text)

    # tl1: Tom tecnico-didatico (not computed, default 75 — needs LLM)
    scores["tl1"] = 75

    # tl2: Frases curtas
    if sentences > 0:
        avg_words = len(words) / sentences
        scores["tl2"] = max(0, 100 - abs(avg_words - 20) * 3)
    else:
        scores["tl2"] = 50

    # tl3: Voz passiva evitada
    passive_count = len(re.findall(r"\b(?:s[aã]o|foi|foram|[eé]|s[aã]o)\s+\w+(?:do|da|dos|das)\b", text.lower()))
    total_verbs = len(re.findall(r"\b\w+(?:ar|er|ir|or|ando|endo|indo)\b", text.lower()))
    passive_ratio = passive_count / max(1, total_verbs)
    scores["tl3"] = max(0, 100 - passive_ratio * 200)

    # tl4: Uniformidade de pessoa (heuristic)
    has_voce = "você" in text.lower() or "voce" in text.lower()
    has_nos = "nós" in text.lower() or "nos" in text.lower()
    scores["tl4"] = 50 if (has_voce and has_nos) else 80

    # tl5: Jargoes explicados (heuristic: presence of glossary-like phrases)
    gloss_markers = len(re.findall(r"(?:ou seja|isto [eé]|em outras palavras|tamb[eé]m conhecido)", text.lower()))
    scores["tl5"] = min(100, gloss_markers * 15 + 30)

    total = sum(s * w for s, w in zip(scores.values(), [25, 20, 20, 20, 15])) / 100
    return {"category_score": round(total, 1), "criteria": scores}


def score_acessibilidade(text: str) -> dict:
    scores = {}
    # ac1: Contraste — not computed in MD, default 75
    scores["ac1"] = 75

    # ac2: Estrutura semantica (headings hierarchy)
    headings = extract_headings(text)
    if headings:
        has_h1 = any(h["level"] == 1 for h in headings)
        has_h2 = any(h["level"] == 2 for h in headings)
        scores["ac2"] = (has_h1 * 40 + has_h2 * 40 + 20)  # 20 base for existing headings
    else:
        scores["ac2"] = 0

    # ac3: Alt text em imagens
    images = extract_images(text)
    if images:
        with_alt = sum(1 for img in images if img["alt"])
        scores["ac3"] = (with_alt / len(images)) * 100
    else:
        scores["ac3"] = 100

    # ac4: Codigo legivel (heuristic: code block length)
    blocks = extract_code_blocks(text)
    if blocks:
        long_blocks = sum(1 for b in blocks if len(b["code"].split("\n")) > 50)
        scores["ac4"] = max(0, 100 - long_blocks * 20)
    else:
        scores["ac4"] = 100

    # ac5: EPUB acessivel — not computed, default 75
    scores["ac5"] = 75

    total = sum(s * w for s, w in zip(scores.values(), [25, 20, 20, 20, 15])) / 100
    return {"category_score": round(total, 1), "criteria": scores}


def score_qualidade_tecnica(text: str) -> dict:
    scores = {}
    # qt1: Precisao factual — not computed, default 75
    scores["qt1"] = 75

    # qt2: Codigo funcional — not computed, default 75 (needs actual testing)
    scores["qt2"] = 75

    # qt3: APIs e versoes corretas — not computed, default 75
    scores["qt3"] = 75

    # qt4: Boas praticas — heuristic: check for TODO/FIXME/HACK in code blocks
    blocks = extract_code_blocks(text)
    bad_patterns = sum(
        len(re.findall(r"(TODO|FIXME|HACK|XXX|BUG)", b["code"])) for b in blocks
    )
    scores["qt4"] = max(0, 100 - bad_patterns * 20)

    # qt5: Comandos e configuracoes — heuristic
    nb = len(re.findall(r"```(?:bash|sh|shell|console|powershell|cmd)", text))
    scores["qt5"] = min(100, 50 + nb * 10)

    total = sum(s * w for s, w in zip(scores.values(), [25, 25, 20, 15, 15])) / 100
    return {"category_score": round(total, 1), "criteria": scores}


def _try_llm(text: str, cat_id: str, fallback_fn) -> dict:
    result = LLMScorer.score(text, cat_id)
    if result and result.get("llm"):
        result["note"] = "LLM evaluado"
        return result
    fallback = fallback_fn(text)
    fallback["note"] = "Heuristico (sem LLM)"
    return fallback


def score_progressao_pedagogica(text: str) -> dict:
    scores = {}
    text_lower = text.lower()
    # pp1: Objetivos de aprendizagem
    obj_patterns = r"(##\s*objetivos|##\s*learning\s*objectives|##\s*ao\s*final|##\s*you.*learn|##\*aprender)"
    has_obj = bool(re.search(obj_patterns, text, re.I))
    bloom_verbs = ["definir", "explicar", "aplicar", "analisar", "avaliar", "criar",
                   "identificar", "descrever", "demonstrar", "projetar", "implementar"]
    bloom_count = sum(text_lower.count(v) for v in bloom_verbs)
    scores["pp1"] = 70 if has_obj else 30 + min(30, bloom_count * 5)
    # pp2: Sequencia didatica
    seq_patterns = [r"##\s*conceito", r"##\s*exemplo", r"##\s*pr[áa]tica", r"##\s*aplica[cç][aã]o"]
    seq_found = sum(1 for p in seq_patterns if re.search(p, text, re.I))
    scores["pp2"] = min(100, seq_found * 25)
    # pp3: Carga cognitiva
    headings = extract_headings(text)
    scores["pp3"] = 80 if len(headings) <= 30 else max(40, 100 - (len(headings) - 30) * 3)
    # pp4: Mecanismos de retencao
    has_resumo = bool(re.search(r"(##\s*resumo|##\s*recapitulando|##\*summary)", text, re.I))
    has_revisao = bool(re.search(r"(revis[aã]o\s+espa[çc]ada|flashcard|relembre)", text_lower))
    scores["pp4"] = (60 if has_resumo else 20) + (20 if has_revisao else 0)
    # pp5: Adequacao ao publico
    has_publico = bool(re.search(r"(p[uú]blico[-\s]*alvo|pr[eé]-requisitos|n[ií]vel|intermedi[áa]rio|avan[çc]ado)", text_lower))
    scores["pp5"] = 80 if has_publico else 50
    total = sum(s * w for s, w in zip(scores.values(), [20, 25, 20, 15, 20])) / 100
    return {"category_score": round(total, 1), "criteria": scores}


def score_consistencia_terminologica(text: str) -> dict:
    scores = {}
    # ct1: Glossario uniforme
    backtick_terms = set(re.findall(r"`([^`]+)`", text))
    scores["ct1"] = min(100, len(backtick_terms) * 5 + 30) if backtick_terms else 20
    # ct2: Termos em ingles
    en_terms = re.findall(r"`([a-zA-Z][a-zA-Z.-]+)`", text)
    scores["ct2"] = min(100, len(en_terms) * 3 + 40) if en_terms else 50
    # ct3: Siglas na primeira mencao
    acronyms = re.findall(r"\b([A-Z]{2,6})\b", text)
    has_full = bool(re.findall(r"[A-Z][a-z]+[^(]*\([A-Z]{2,}\)", text))
    scores["ct3"] = 80 if has_full else (40 if len(acronyms) > 3 else 60)
    # ct4: STYLE_GUIDE compliance (heuristic: consistent formatting)
    fences = re.findall(r"^```(\w*)", text, re.MULTILINE)
    consistent_langs = len(set(fences)) <= 3 if fences else True
    scores["ct4"] = 80 if consistent_langs else 50
    total = sum(s * w for s, w in zip(scores.values(), [30, 25, 20, 25])) / 100
    return {"category_score": round(total, 1), "criteria": scores}


def score_qualidade_exemplos(text: str) -> dict:
    scores = {}
    blocks = extract_code_blocks(text)
    # qe1: Contexto realista
    context_words = ["exemplo", "example", "cenário", "cenario", "caso", "use case", "aplicação"]
    has_context = sum(text.lower().count(w) for w in context_words)
    scores["qe1"] = min(100, has_context * 5 + 30)
    # qe2: Completude
    scores["qe2"] = min(100, len(blocks) * 10 + 30) if blocks else 20
    # qe3: Codigo executavel
    if blocks:
        with_lang = sum(1 for b in blocks if b["lang"])
        scores["qe3"] = (with_lang / len(blocks)) * 100
    else:
        scores["qe3"] = 50
    # qe4: Analogias eficazes
    analogy_words = ["como se fosse", "analogia", "similar a", "comparável", "assim como", "tal qual"]
    analogy_count = sum(text.lower().count(w) for w in analogy_words)
    scores["qe4"] = min(100, analogy_count * 20 + 20)
    # qe5: Anti-exemplos
    anti_patterns = [r"n[aã]o\s+fa[çc]a", r"evite", r"anti[-\s]*exemplo", r"bad\s+practice", r"common\s+mistake"]
    has_anti = sum(1 for p in anti_patterns if re.search(p, text, re.I))
    scores["qe5"] = min(100, has_anti * 33 + 20)
    total = sum(s * w for s, w in zip(scores.values(), [25, 20, 20, 15, 20])) / 100
    return {"category_score": round(total, 1), "criteria": scores}


def score_exercicios_avaliacoes(text: str) -> dict:
    scores = {}
    text_lower = text.lower()
    # ea1: Progressao de dificuldade
    diff_markers = ["fácil", "facil", "intermediário", "intermediario", "difícil", "dificil",
                    "avançado", "avancado", "nível", "nivel", "★", "nível 1", "nível 2"]
    diff_count = sum(text_lower.count(m) for m in diff_markers)
    scores["ea1"] = min(100, diff_count * 15 + 20)
    # ea2: Cobertura do conteudo
    exercise_sections = len(re.findall(r"##\s*(?:exerc[ií]cio|atividade|desafio|pr[áa]tica)", text, re.I))
    scores["ea2"] = min(100, exercise_sections * 25)
    # ea3: Gabarito comentado
    has_gabarito = bool(re.search(r"(gabarito|resposta|solu[cç][aã]o|answer)", text_lower))
    scores["ea3"] = 80 if has_gabarito else 30
    # ea4: Quiz
    has_quiz = bool(re.search(r"(quiz|pergunta|m[ú]ltipla\s*escolha|alternativa)", text_lower))
    scores["ea4"] = 80 if has_quiz else 30
    # ea5: Criterios de correcao
    has_rubrica = bool(re.search(r"(rubrica|crit[eé]rio\s*de\s*corre[cç][aã]o|peso|pontua[cç][aã]o)", text_lower))
    scores["ea5"] = 80 if has_rubrica else 30
    total = sum(s * w for s, w in zip(scores.values(), [20, 20, 20, 20, 20])) / 100
    return {"category_score": round(total, 1), "criteria": scores}


def score_design_hierarquia_visual(text: str) -> dict:
    scores = {}
    headings = extract_headings(text)
    # dh1: Hierarquia visual
    if headings:
        levels = set(h["level"] for h in headings)
        has_h1 = 1 in levels
        has_h2 = 2 in levels
        max_depth = max(levels)
        scores["dh1"] = min(100, (has_h1 * 25 + has_h2 * 25 + max(0, 50 - abs(max_depth - 4) * 10)))
    else:
        scores["dh1"] = 0
    # dh2: Diagramas e ilustracoes
    diagram_markers = len(re.findall(r"```(?:mermaid|plantuml|graphviz|d2)", text))
    scores["dh2"] = min(100, diagram_markers * 20 + 20)
    # dh3: Blocos de destaque
    callout_markers = len(re.findall(r">\s*\*\*(?:Dica|Warning|Nota|Tip|Importante|Aten[cç][aã]o)", text, re.I))
    scores["dh3"] = min(100, callout_markers * 20 + 20)
    # dh4: Tipografia consistente
    code_blocks = extract_code_blocks(text)
    scores["dh4"] = 80 if code_blocks else 60
    # dh5: Espacamento e margens — not applicable in markdown
    scores["dh5"] = 75
    # dh6: Paleta de cores — not applicable in markdown
    scores["dh6"] = 75
    total = sum(s * w for s, w in zip(scores.values(), [20, 20, 15, 15, 15, 15])) / 100
    return {"category_score": round(total, 1), "criteria": scores}


def score_qualidade_formatos(text: str) -> dict:
    scores = {}
    # qf1-qf6: Format quality — not evaluable from raw markdown
    scores["qf1"] = 75
    scores["qf2"] = 75
    scores["qf3"] = 75
    scores["qf4"] = 75
    scores["qf5"] = 75
    scores["qf6"] = bool(re.search(r"(isbn|title:|author:|lang)", text[:500], re.I)) * 25 + 50
    total = sum(s * w for s, w in zip(scores.values(), [20, 15, 20, 15, 15, 15])) / 100
    return {"category_score": round(total, 1), "criteria": scores}


def score_identidade_visual(text: str) -> dict:
    scores = {}
    # iv1: Aderencia ao brand book — not evaluable from markdown
    scores["iv1"] = 75
    # iv2: Design tokens — not evaluable
    scores["iv2"] = 75
    # iv3: Familia visual — not evaluable
    scores["iv3"] = 75
    # iv4: Consistencia entre formatos — not evaluable
    scores["iv4"] = 75
    # iv5: Originalidade — not evaluable
    scores["iv5"] = 75
    total = sum(s * w for s, w in zip(scores.values(), [25, 25, 20, 15, 15])) / 100
    return {"category_score": round(total, 1), "criteria": scores}


def score_qualidade_tipografica(text: str) -> dict:
    scores = {}
    # tp1: Hierarquia tipografica
    headings = extract_headings(text)
    if headings:
        levels = [h["level"] for h in headings]
        has_h1 = 1 in levels
        has_h2 = 2 in levels
        has_h3 = 3 in levels
        has_h4 = 4 in levels
        depth_count = sum([has_h1, has_h2, has_h3, has_h4])
        scores["tp1"] = depth_count * 25
    else:
        scores["tp1"] = 0
    # tp2: Rhythm vertical — not evaluable
    scores["tp2"] = 75
    # tp3: Comprimento de linha — heuristic from avg line len
    lines = [l for l in text.split("\n") if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("```")]
    if lines:
        avg_len = sum(len(l) for l in lines) / len(lines)
        scores["tp3"] = max(0, 100 - abs(avg_len - 65) * 2)
    else:
        scores["tp3"] = 50
    # tp4: Tracking e leading — not evaluable
    scores["tp4"] = 75
    # tp5: Tratamento de codigo
    blocks = extract_code_blocks(text)
    if blocks:
        has_lang = sum(1 for b in blocks if b["lang"])
        scores["tp5"] = (has_lang / len(blocks)) * 100
    else:
        scores["tp5"] = 100
    total = sum(s * w for s, w in zip(scores.values(), [25, 20, 20, 15, 20])) / 100
    return {"category_score": round(total, 1), "criteria": scores}


def score_design_informacao(text: str) -> dict:
    scores = {}
    # di1: Diagramas claros
    diagrams = len(re.findall(r"```(?:mermaid|plantuml|d2|graphviz)", text))
    ascii_diagrams = len(re.findall(r"[+][-]+\+", text))
    scores["di1"] = min(100, (diagrams * 25) + (10 if ascii_diagrams > 2 else 0) + 20)
    # di2: Iconografia consistente — not evaluable
    scores["di2"] = 75
    # di3: Tabelas informativas
    tables = len(re.findall(r"^\|.+\|$", text, re.MULTILINE))
    scores["di3"] = min(100, tables * 10 + 30)
    # di4: Infograficos
    scores["di4"] = 50 if diagrams > 0 else 20
    # di5: Funciona em P&B — not evaluable from markdown
    scores["di5"] = 75
    total = sum(s * w for s, w in zip(scores.values(), [25, 15, 20, 20, 20])) / 100
    return {"category_score": round(total, 1), "criteria": scores}


def score_acessibilidade_visual(text: str) -> dict:
    scores = {}
    # av1: Contraste WCAG AA+ — not evaluable from markdown
    scores["av1"] = 75
    # av2: Daltônico-safe — not evaluable
    scores["av2"] = 75
    # av3: Font-size minimo — not evaluable
    scores["av3"] = 75
    # av4: Navegacao semantica
    headings = extract_headings(text)
    if headings:
        levels = [h["level"] for h in headings]
        jumps = sum(1 for i in range(1, len(levels)) if levels[i] > levels[i - 1] + 1)
        scores["av4"] = max(0, 100 - jumps * 20)
    else:
        scores["av4"] = 0
    # av5: Dark mode ready — not evaluable
    scores["av5"] = 75
    total = sum(s * w for s, w in zip(scores.values(), [25, 20, 20, 20, 15])) / 100
    return {"category_score": round(total, 1), "criteria": scores}


def score_consistencia_formatos(text: str) -> dict:
    scores = {}
    # cf1-cf5: Cross-format consistency — not evaluable from single markdown
    scores["cf1"] = 75
    scores["cf2"] = 75
    scores["cf3"] = 75
    scores["cf4"] = 75
    scores["cf5"] = bool(re.search(r"(title:|author:|lang|isbn)", text[:500], re.I)) * 25 + 50
    total = sum(s * w for s, w in zip(scores.values(), [25, 20, 20, 20, 15])) / 100
    return {"category_score": round(total, 1), "criteria": scores}


def score_categoria(text: str, cat_id: str, cat_weight: int) -> dict:
    """Computa score para uma categoria BQS."""
    result = {}
    if cat_id == "estrutura_conteudo":
        headings = extract_headings(text)
        result = score_estrutura_conteudo(text, headings)
    elif cat_id == "qualidade_markdown":
        result = score_qualidade_markdown(text)
    elif cat_id == "tom_legibilidade":
        result = _try_llm(text, cat_id, score_tom_legibilidade)
    elif cat_id == "acessibilidade":
        result = _try_llm(text, cat_id, score_acessibilidade)
    elif cat_id == "qualidade_tecnica":
        result = _try_llm(text, cat_id, score_qualidade_tecnica)
    elif cat_id == "progressao_pedagogica":
        result = _try_llm(text, cat_id, score_progressao_pedagogica)
    elif cat_id == "consistencia_terminologica":
        result = _try_llm(text, cat_id, score_consistencia_terminologica)
    elif cat_id == "qualidade_exemplos":
        result = _try_llm(text, cat_id, score_qualidade_exemplos)
    elif cat_id == "exercicios_avaliacoes":
        result = _try_llm(text, cat_id, score_exercicios_avaliacoes)
    elif cat_id == "design_hierarquia_visual":
        result = _try_llm(text, cat_id, score_design_hierarquia_visual)
    elif cat_id == "qualidade_formatos":
        result = _try_llm(text, cat_id, score_qualidade_formatos)
    elif cat_id == "identidade_visual":
        result = _try_llm(text, cat_id, score_identidade_visual)
    elif cat_id == "qualidade_tipografica":
        result = _try_llm(text, cat_id, score_qualidade_tipografica)
    elif cat_id == "design_informacao":
        result = _try_llm(text, cat_id, score_design_informacao)
    elif cat_id == "acessibilidade_visual":
        result = _try_llm(text, cat_id, score_acessibilidade_visual)
    elif cat_id == "consistencia_formatos":
        result = _try_llm(text, cat_id, score_consistencia_formatos)
    else:
        result = {
            "category_score": 75,
            "criteria": {},
            "note": "Score default (75). Categoria desconhecida.",
        }
    result["weight"] = cat_weight
    return result


def compute_bqs(text: str, bqs_config: dict, overrides: dict | None = None) -> dict:
    categories = bqs_config.get("categories", [])
    results = []
    total_weighted = 0
    total_weight = 0

    for cat in categories:
        cat_id = cat["id"]
        cat_weight = cat["weight"]

        # Verificar override
        if overrides and cat_id in overrides:
            cat_result = {
                "category_score": overrides[cat_id],
                "weight": cat_weight,
                "criteria": {},
                "note": "Override manual",
            }
        else:
            cat_result = score_categoria(text, cat_id, cat_weight)

        results.append({
            "id": cat_id,
            "name": cat["name"],
            "score": cat_result["category_score"],
            "weight": cat_weight,
            "criteria": cat_result.get("criteria", {}),
            "note": cat_result.get("note", ""),
        })

        total_weighted += cat_result["category_score"] * cat_weight
        total_weight += cat_weight

    overall = round(total_weighted / total_weight, 1) if total_weight > 0 else 0
    min_score = min(r["score"] for r in results)
    passed = all(r["score"] >= bqs_config.get("minimum_score", 95) for r in results)

    return {
        "overall": overall,
        "min_score": min_score,
        "passed": passed,
        "minimum_required": bqs_config.get("minimum_score", 95),
        "categories": results,
        "scoring_method": bqs_config.get("scoring_method", "weighted_average"),
    }


def load_overrides(module_id: str) -> dict:
    override_path = ROOT / "curriculum" / "bqs" / "overrides" / f"{module_id}.yaml"
    if override_path.exists():
        return load_yaml(override_path)
    return {}


def find_module_md(module_id: str) -> str | None:
    """Procura o arquivo aula.md de um modulo."""
    parts = module_id.split("/")
    if len(parts) == 2:
        course, mod = parts
        path = ROOT / "curriculum" / "sources" / course / mod / "aula" / "aula.md"
        if path.exists():
            return path.read_text(encoding="utf-8")
    return None


def find_book_md(book_id: str) -> str | None:
    path = ROOT / "knowledge-factory" / "products" / "books" / book_id / "compiled" / "book.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return None


def main():
    bqs_config = load_yaml(BQS_CORE)
    status = load_yaml(STATUS_PATH)
    METRICS_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    overrides_dir = ROOT / "curriculum" / "bqs" / "overrides"
    overrides_dir.mkdir(parents=True, exist_ok=True)

    modules = status.get("modules", {})
    books = status.get("books", {})

    results = []
    module_count = 0
    book_count = 0

    # Processar modulos
    for course_name, mods in modules.items():
        for mod_key, mod_data in mods.items():
            module_id = f"{course_name}/{mod_key}"
            print(f"[BQS] Computando modulo: {module_id}...", end=" ")
            text = find_module_md(module_id)
            if not text:
                print(f"aula.md nao encontrado, pulando")
                continue

            overrides = load_overrides(module_id)
            bqs = compute_bqs(text, bqs_config, overrides)

            results.append({
                "target_id": module_id,
                "type": "module",
                "title": mod_data.get("title", ""),
                "overall": bqs["overall"],
                "min_score": bqs["min_score"],
                "passed": bqs["passed"],
                "details": bqs,
            })
            module_count += 1
            print(f"overall={bqs['overall']}, min={bqs['min_score']}, passed={bqs['passed']}")

    # Processar livros
    for book_id, book_data in books.items():
        print(f"[BQS] Computando livro: {book_id}...", end=" ")
        text = find_book_md(book_id)
        if not text:
            print(f"book.md nao encontrado, pulando")
            continue

        overrides = load_overrides(book_id)
        bqs = compute_bqs(text, bqs_config, overrides)

        results.append({
            "target_id": book_id,
            "type": "book",
            "title": book_data.get("title", ""),
            "overall": bqs["overall"],
            "min_score": bqs["min_score"],
            "passed": bqs["passed"],
            "details": bqs,
        })
        book_count += 1
        print(f"overall={bqs['overall']}, min={bqs['min_score']}, passed={bqs['passed']}")

    # Salvar CSV
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    file_exists = SCORE_CSV.exists()
    with open(SCORE_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "target_id", "type", "title", "overall", "min_score", "passed"])
        for r in results:
            writer.writerow([
                timestamp, r["target_id"], r["type"], r["title"],
                r["overall"], r["min_score"], r["passed"],
            ])

    print(f"\n[BQS] Resumo:")
    print(f"  Modulos computados: {module_count}")
    print(f"  Livros computados: {book_count}")
    print(f"  CSV salvo: {SCORE_CSV}")
    print(f"  Timestamp: {timestamp}")

    # Gerar relatorio markdown
    report_lines = [
        f"# BQS Report — {timestamp}\n",
        f"**Modulos:** {module_count} | **Livros:** {book_count}\n",
        f"**Metodo:** {bqs_config.get('scoring_method', 'weighted_average')} | **Minimo por categoria:** {bqs_config.get('minimum_score', 95)}\n",
        "\n## Resultados\n",
        "| Target | Type | Overall | Min Score | Passed |",
        "|---|---|---|---|---|",
    ]
    for r in results:
        report_lines.append(f"| {r['target_id']} | {r['type']} | {r['overall']} | {r['min_score']} | {'✅' if r['passed'] else '❌'} |")

    # Categorias com piores scores
    report_lines.append("\n## Categorias com Scores Baixos\n")
    for r in results:
        low_cats = [c for c in r["details"]["categories"] if c["score"] < 95]
        if low_cats:
            report_lines.append(f"### {r['target_id']}\n")
            for c in low_cats:
                report_lines.append(f"- **{c['name']}** ({c['id']}): {c['score']}/100 — {c.get('note', '')}")

    report_path = REPORT_DIR / f"bqs-report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"  Relatorio salvo: {report_path}")


if __name__ == "__main__":
    main()
