#!/usr/bin/env python3
"""
remediate_markdown.py
Escaneia e corrige violacoes estruturais de Markdown nos modulos.
Dry-run por padrao. Use --apply para escrever as correcoes.

Correcoes:
  1. Code fences sem language tag -> infere linguagem ou usa "text"
  2. Headings skipping levels -> reequilibra (H4 apos H2 vira H3)
  3. Trailing whitespace em linhas
  4. Linhas vazias em excesso (>2 consecutivas) -> reduz para 2
  5. Relatorio diff no final
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "curriculum" / "sources"


def infer_language(code: str) -> str:
    code_stripped = code.strip()
    if not code_stripped:
        return ""
    # Detect by content patterns
    first_lines = code_stripped.split("\n")[:5]
    joined = "\n".join(first_lines)

    # TypeScript/JavaScript
    if re.search(r"(?:import|export|interface|type|const |let |function|=>|console\.)", joined):
        if re.search(r":\s*\w+[;=]|interface\s+\w+|type\s+\w+\s*=", joined):
            return "typescript"
        return "javascript"
    # Python
    if re.search(r"(?:def |class |import |from |print\(|if __name__)", joined):
        return "python"
    # YAML
    if re.search(r"^[\w-]+:", joined, re.MULTILINE) and ":" in joined:
        return "yaml"
    # SQL
    if re.search(r"(?:SELECT|INSERT|UPDATE|DELETE|CREATE TABLE|ALTER)", joined, re.I):
        return "sql"
    # Bash
    if re.search(r"(?:#!/bin/|apt |npm |curl |git |docker |kubectl)", joined):
        return "bash"
    # JSON
    if joined.strip().startswith("{") or joined.strip().startswith("["):
        return "json"
    # HTML
    if re.search(r"<!DOCTYPE|<html|<div|<span|<p>", joined, re.I):
        return "html"
    # CSS
    if re.search(r"{\s*[\w-]+\s*:", joined) and ":" in joined:
        return "css"
    # Markdown
    if re.search(r"^#|^\[|^!\[", joined, re.MULTILINE):
        return "markdown"
    # HCL/Terraform
    if re.search(r'resource\s+"[\w_]+"|variable\s+"[\w_]+"|terraform\s*{', joined):
        return "hcl"
    # Dockerfile
    if re.search(r"^FROM |^RUN |^COPY |^CMD ", joined, re.MULTILINE):
        return "dockerfile"
    # Prisma
    if re.search(r"model\s+\w+\s*{", joined):
        return "prisma"
    # INI/conf
    if re.search(r"^\[.+\]$", joined, re.MULTILINE):
        return "ini"
    # LogQL / PromQL
    if re.search(r"(?:rate\(|sum\(|count_over_time|avg_over_time)", joined):
        return "logql"
    return ""


def fix_language_tags(text: str, dry_run: bool, changes: list, path: str) -> str:
    lines = text.split("\n")
    new_lines = []
    i = 0
    fence_start = -1
    fence_lines = []

    def is_fence(line: str) -> bool:
        return re.match(r"^```", line.strip())

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if is_fence(line):
            lang = stripped[3:].strip()
            if not lang:
                # No language tag: peek ahead to infer
                content_lines = []
                j = i + 1
                while j < len(lines) and not is_fence(lines[j]):
                    content_lines.append(lines[j])
                    j += 1
                code = "\n".join(content_lines)
                inferred = infer_language(code) or "text"
                if not dry_run:
                    new_lines.append(f"```{inferred}")
                else:
                    new_lines.append(line)
                changes.append(f"{path}:{i+1}  ``` -> ```{inferred}")
                i += 1
                continue
            else:
                new_lines.append(line)
                i += 1
                continue
        else:
            new_lines.append(line)
            i += 1

    return "\n".join(new_lines)


def fix_heading_hierarchy(text: str, dry_run: bool, changes: list, path: str) -> str:
    lines = text.split("\n")
    new_lines = []
    prev_level = 0
    for i, line in enumerate(lines):
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m:
            level = len(m.group(1))
            if level > prev_level + 1 and prev_level > 0:
                new_level = prev_level + 1
                if not dry_run:
                    new_lines.append(f"{'#' * new_level} {m.group(2)}")
                else:
                    new_lines.append(line)
                changes.append(f"{path}:{i+1}  {'#' * level} -> {'#' * new_level} heading skip fix")
            else:
                new_lines.append(line)
            prev_level = len(re.match(r"^(#+)", line).group(1))
        else:
            new_lines.append(line)
            if line.strip() == "":
                prev_level = 0

    return "\n".join(new_lines)


def fix_trailing_whitespace(text: str, dry_run: bool, changes: list, path: str) -> str:
    new_lines = []
    for i, line in enumerate(text.split("\n")):
        stripped = line.rstrip()
        if line != stripped and stripped:
            if not dry_run:
                new_lines.append(stripped)
            else:
                new_lines.append(line)
            if line != stripped:
                pass  # too verbose for report
        else:
            new_lines.append(line)
    return "\n".join(new_lines)


def fix_excessive_blank_lines(text: str, dry_run: bool, changes: list, path: str) -> str:
    result = re.sub(r"\n{3,}", "\n\n", text)
    blank_reduction = text.count("\n\n\n") - result.count("\n\n\n")
    if blank_reduction > 0 and not dry_run:
        changes.append(f"{path}:  removidas {blank_reduction} linhas vazias extras")
    return result


def remediate_file(md_path: Path, dry_run: bool) -> list:
    changes = []
    text = md_path.read_text(encoding="utf-8")
    rel = str(md_path.relative_to(ROOT))

    # Apply fixes
    text = fix_language_tags(text, dry_run, changes, rel)
    text = fix_heading_hierarchy(text, dry_run, changes, rel)
    text = fix_excessive_blank_lines(text, dry_run, changes, rel)

    if not dry_run and changes:
        md_path.write_text(text, encoding="utf-8")

    return changes


def main():
    parser = argparse.ArgumentParser(description="Remediacao automatizada de Markdown")
    parser.add_argument("--apply", action="store_true", help="Aplica as correcoes (padrao: dry-run)")
    parser.add_argument("--path", default=str(SOURCES), help="Diretorio raiz dos modulos")
    args = parser.parse_args()

    dry_run = not args.apply
    mode = "DRY-RUN" if dry_run else "APPLY"
    target = Path(args.path)
    print(f"[remediate] Modo: {mode}")
    print(f"[remediate] Alvo: {target}")
    print()

    md_files = sorted(target.rglob("*.md"))
    total_changes = 0
    changed_files = 0

    for md in md_files:
        rel = str(md.relative_to(ROOT))
        changes = remediate_file(md, dry_run)
        if changes:
            changed_files += 1
            total_changes += len(changes)
            print(f"  {rel}")
            for c in changes[:10]:
                print(f"    {c}")
            if len(changes) > 10:
                print(f"    ... +{len(changes)-10} more")
            print()

    print(f"[remediate] Resumo:")
    print(f"  Arquivos com mudancas: {changed_files}")
    print(f"  Total de correcoes:    {total_changes}")
    if dry_run and total_changes > 0:
        print(f"\n  Execute com --apply para aplicar as correcoes.")

    return 0 if total_changes == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
