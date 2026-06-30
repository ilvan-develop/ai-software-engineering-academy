#!/usr/bin/env python3
"""
auto_fix_code_languages.py
Detecta blocos de codigo Markdown sem especificacao de linguagem
 e adiciona a linguagem quando a inferencia e confiavel.

Uso:
  python scripts/auto_fix_code_languages.py [--dry-run]
"""

import argparse
import re
from pathlib import Path

from config import SOURCES_DIR


def is_ascii_art(code: str) -> bool:
    """Retorna True se o bloco parece diagrama ASCII (caixas Unicode/ASCII)."""
    box_chars = set("┌┐└┘│─┤├┬┴┼╔╗╚╝║═╣╠╦╩╬")
    text = code.replace(" ", "").replace("\n", "")
    if not text:
        return False
    ratio = sum(1 for ch in text if ch in box_chars) / len(text)
    return ratio > 0.05


def is_prose_block(code: str) -> bool:
    """Retorna True se o bloco for texto/markdown (callout, tabela, checklist, etc)."""
    lines = code.splitlines()
    non_empty = [ln.strip() for ln in lines if ln.strip()]
    if not non_empty:
        return False

    has_heading = any(re.match(r"^#{1,6}\s+", ln) for ln in non_empty)
    has_hrule = any(ln == "---" or re.match(r"^-{3,}\|", ln) for ln in non_empty)

    text_re = re.compile(
        r"^(?:"
        r"[A-Za-zÀ-ú\(\*\"\-–—\[]|"    # letras, parenteses, aspas, tracos, colchetes
        r"\d|"                          # qualquer numero (tabelas, metricas)
        r"[#\/\.→❌✅⚠️📋🏆□○◉•│├└▸▪★▼↻↓─|]"  # #, /, ., bullets, arrows, diagram chars, pipe
        r")"
    )
    code_re = re.compile(
        r"^(import|export|const|let|function|class|model|enum"
        r"|SELECT|INSERT|UPDATE|DELETE|CREATE|FROM|RUN|COPY|CMD|FROM"
        r"|interface|type|namespace|package|using)\b"
    )

    text_lines = sum(1 for ln in non_empty if text_re.match(ln) and not code_re.match(ln))
    ratio = text_lines / len(non_empty) if non_empty else 0

    return has_heading or has_hrule or ratio >= 0.7


def detect_language(code: str) -> str | None:
    """Retorna a linguagem inferida ou None se nao houver confianca."""
    lines = [ln.rstrip() for ln in code.splitlines() if ln.strip()]
    if not lines:
        return "text"  # empty block

    first_line = lines[0].strip()

    # Block starts with code fence -> mostra markdown como conteudo -> text
    if first_line.startswith("```"):
        return "text"

    # Nunca classificar arte ASCII ou blocos de prosa como linguagem de codigo
    if is_ascii_art(code) or is_prose_block(code):
        return "text"

    first_line = lines[0].strip()

    # Prisma (schema) — alta confianca
    prisma_markers = [
        r"^\s*model\s+\w+\s*\{",
        r"^\s*enum\s+\w+\s*\{",
        r"@\w+\s*\(",
        r"@@index",
        r"@map\s*\(",
        r"@default\s*\(",
    ]
    prisma_score = sum(1 for p in prisma_markers if re.search(p, code, re.MULTILINE))
    if prisma_score >= 2:
        return "prisma"

    # SQL
    if re.search(r"\b(SELECT|INSERT|UPDATE|DELETE|CREATE TABLE|ALTER TABLE|DROP TABLE)\b", code, re.IGNORECASE) and re.search(r"\b(FROM|INTO|VALUES|WHERE|JOIN)\b", code, re.IGNORECASE):
        return "sql"

    # Dockerfile
    if first_line.startswith("FROM ") and re.search(r"\b(RUN|COPY|CMD|ENTRYPOINT|WORKDIR)\b", code):
        return "dockerfile"

    # Bash / Shell
    shell_markers = [
        r"^\$\s+",
        r"^#\s+!/bin/",
        r"\b(npm|npx|yarn|pnpm|git|docker|docker-compose|cd|mkdir|cat|echo|export|source|psql|pg_restore|prisma migrate|curl|wget|terraform|kubectl|helm)\b",
    ]
    shell_score = sum(
        1 for pat in shell_markers if re.search(pat, code, re.MULTILINE | re.IGNORECASE)
    )
    if shell_score >= 2:
        return "bash"

    # YAML — requer indicios fortes
    yaml_markers = [
        r"^---\s*$",
        r"^version:\s*\w+",
        r"^services:\s*$",
        r"^steps:\s*$",
        r"^jobs:\s*$",
        r"^env:\s*$",
        r"^on:\s*$",
        r"^runs-on:",
        r"^uses:",
    ]
    yaml_score = sum(1 for p in yaml_markers if re.search(p, code, re.MULTILINE))
    if yaml_score >= 1 and re.search(r"^[a-zA-Z0-9_]+:\s*\w", code, re.MULTILINE):
        return "yaml"

    # JSON
    if first_line.startswith(("{", "[")) and code.count('"') > 4 and ':' in code:
        return "json"

    # TypeScript / JavaScript
    ts_markers = [
        r"\bimport\s+(?:\{[^}]+\}|\w+)\s+from\s+[\"']",
        r"\bexport\s+(class|interface|type|function|const|default)\b",
        r"\binterface\s+\w+",
        r"\btype\s+\w+\s*=",
        r"\b(const|let)\s+\w+\s*:\s*[A-Za-z]",
        r"\basync\s+\w+\s*\(",
        r"\bconsole\.log",
        r"\bnew\s+[A-Z]\w+\(",
        r"\bfunction\s+\w+\s*\(",
    ]
    ts_score = sum(1 for pat in ts_markers if re.search(pat, code))
    if ts_score >= 2:
        return "typescript"

    # LogQL
    if re.search(r"\{[a-z_]+=", code) and re.search(r"\|\=\s*[\"']", code):
        return "logql"

    return None


def process_file(path: Path, dry_run: bool) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    changed = 0
    skipped = 0
    guesses: list[tuple[int, str]] = []

    in_code = False
    code_buffer: list[str] = []
    fence_line = -1
    has_language = False

    new_lines: list[str] = []

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```") and not in_code:
            fence_line = i
            fence_info = stripped[3:].strip()
            has_language = bool(fence_info)
            new_lines.append(line)
            in_code = True
            code_buffer = []
            continue

        if in_code and stripped == "```":
            in_code = False
            if has_language:
                # Pass through unchanged
                new_lines.extend(code_buffer)
                new_lines.append(line)
            else:
                code = "".join(code_buffer)
                lang = detect_language(code)
                if lang:
                    # Replace the opening fence with labeled version
                    new_lines[fence_line] = f"```{lang}\n"
                    guesses.append((fence_line + 1, lang, _preview(code)))
                    changed += 1
                else:
                    skipped += 1
                new_lines.extend(code_buffer)
                new_lines.append(line)
            code_buffer = []
            has_language = False
            continue

        if in_code:
            code_buffer.append(line)
        else:
            new_lines.append(line)

    # Handle unclosed fence at EOF (e.g., empty block at end of file)
    if in_code and not has_language:
        code = "".join(code_buffer)
        lang = detect_language(code) or "text"
        new_lines[fence_line] = f"```{lang}\n"
        guesses.append((fence_line + 1, lang, _preview(code)))
        changed += 1
        new_lines.extend(code_buffer)
        # No closing fence to append; file ends after this

    if not dry_run and changed:
        path.write_text("".join(new_lines), encoding="utf-8")

    return {
        "path": path,
        "changed": changed,
        "skipped": skipped,
        "guesses": guesses,
    }


def _preview(code: str, max_len: int = 40) -> str:
    first = code.strip().splitlines()[0] if code.strip() else ""
    first = first.strip().replace("\t", " ")
    if len(first) > max_len:
        first = first[:max_len] + "..."
    # Sanitize for Windows cp1252 console
    return first.encode("cp1252", errors="replace").decode("cp1252")


def main():
    parser = argparse.ArgumentParser(description="Auto-detecta linguagens em blocos de codigo")
    parser.add_argument("--dry-run", action="store_true", help="Nao escreve alteracoes")
    args = parser.parse_args()

    results = []
    for aula in sorted(SOURCES_DIR.rglob("aula/aula.md")):
        results.append(process_file(aula, args.dry_run))

    total_changed = sum(r["changed"] for r in results)
    total_skipped = sum(r["skipped"] for r in results)

    print(f"Blocos inferidos: {total_changed}")
    print(f"Blocos sem confianca (nao alterados): {total_skipped}")

    if args.dry_run:
        print("\n[MODO DRY-RUN — nenhuma alteracao foi salva]")

    # Print per-file summary for files with changes
    for r in results:
        if r["changed"]:
            print(f"\n{r['path'].relative_to(SOURCES_DIR.parent)}: +{r['changed']} linguagens")
            for line_no, lang, preview in r["guesses"][:5]:
                print(f"  linha {line_no}: {lang} | {preview}")
            if len(r["guesses"]) > 5:
                print(f"  ... e mais {len(r['guesses']) - 5}")


if __name__ == "__main__":
    main()
