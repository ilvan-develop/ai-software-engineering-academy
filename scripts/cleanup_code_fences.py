#!/usr/bin/env python3
"""
cleanup_code_fences.py
Corrige blocos de codigo onde a linguagem ficou na fence de fechamento
em vez da de abertura (bug de auto-fix anterior).

Uso:
  python scripts/cleanup_code_fences.py
"""

from pathlib import Path
from config import SOURCES_DIR


def cleanup_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    fences = []
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("```"):
            fences.append((i, s))

    # Pair fences
    pairs = []
    stack = []
    for i, s in fences:
        if not stack:
            stack.append((i, s))
        else:
            pairs.append((stack.pop(), (i, s)))

    changes = 0
    new_lines = list(lines)
    for (open_i, open_s), (close_i, close_s) in pairs:
        open_lang = open_s[3:].strip()
        close_lang = close_s[3:].strip()
        if not open_lang and close_lang:
            # Move language from closing to opening
            new_lines[open_i] = f"```{close_lang}\n"
            new_lines[close_i] = "```\n"
            changes += 1

    if changes:
        path.write_text("".join(new_lines), encoding="utf-8")

    return changes


def main():
    total = 0
    for aula in sorted(SOURCES_DIR.rglob("aula/aula.md")):
        n = cleanup_file(aula)
        if n:
            print(f"  {aula.relative_to(SOURCES_DIR.parent)}: corrigidos {n} blocos")
            total += n
    print(f"\nTotal corrigido: {total} blocos")


if __name__ == "__main__":
    main()
