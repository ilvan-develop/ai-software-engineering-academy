#!/usr/bin/env python3
"""
link_checker.py
Varre arquivos .md em busca de links quebrados (HTTP 4xx/5xx ou links internos
que apontam para arquivos inexistentes).
Retorna exit code 0 se todos os links estao ok, 1 caso contrario.
"""

import re
import sys
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import concurrent.futures
import socket

ROOT = Path(__file__).resolve().parent.parent
TIMEOUT = 10
MAX_WORKERS = 10
EXTENSIONS = ["*.md", "*.yaml", "*.yml"]
EXCLUDE_PATTERNS = [
    r"^#",        # anchor links
    r"^mailto:",
    r"^tel:",
    r"^{{.*}}$",  # template vars
    r"localhost",
    r"127\.0\.0\.1",
]


def is_excluded(url: str) -> bool:
    return any(re.match(p, url) for p in EXCLUDE_PATTERNS)


def check_external_link(url: str) -> tuple[str, bool, str]:
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=TIMEOUT) as resp:
            code = resp.status
            if 200 <= code < 400:
                return (url, True, f"HTTP {code}")
            return (url, False, f"HTTP {code}")
    except HTTPError as e:
        return (url, False, f"HTTP {e.code}")
    except URLError as e:
        return (url, False, str(e.reason))
    except socket.timeout:
        return (url, False, "timeout")
    except Exception as e:
        return (url, False, str(e))


def check_internal_link(url: str, source_file: Path) -> tuple[str, bool, str]:
    # Resolve relative links against the source file's directory
    base_dir = source_file.parent
    # Remove query strings and fragments
    clean_url = url.split("?")[0].split("#")[0]
    target = (base_dir / clean_url).resolve()
    if target.exists():
        return (url, True, "found")
    return (url, False, f"not found: {target}")


def extract_links(text: str, source_path: Path) -> list[tuple[str, str, Path]]:
    """Returns list of (url, type, source_file) where type is 'internal' or 'external'."""
    links = []
    # Markdown links: [text](url)
    for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", text):
        url = m.group(2).strip()
        if is_excluded(url):
            continue
        parsed = urlparse(url)
        if parsed.scheme in ("http", "https"):
            links.append((url, "external", source_path))
        elif not parsed.scheme and not url.startswith("//"):
            links.append((url, "internal", source_path))

    # Bare URLs: <https://...>
    for m in re.finditer(r"<(https?://[^>]+)>", text):
        url = m.group(1).strip()
        if not is_excluded(url):
            links.append((url, "external", source_path))

    # Image links: ![alt](url)
    for m in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", text):
        url = m.group(2).strip()
        if is_excluded(url):
            continue
        if url.startswith(("http://", "https://")):
            links.append((url, "external", source_path))
        else:
            links.append((url, "internal", source_path))

    return links


def main():
    md_files = []
    for ext in EXTENSIONS:
        md_files.extend(ROOT.rglob(ext))

    # Exclude .github and venv
    md_files = [
        f for f in md_files
        if not any(p.name.startswith(".") for p in f.relative_to(ROOT).parts)
        and ".git" not in f.parts
        and "__pycache__" not in f.parts
    ]

    all_links = []
    for filepath in md_files:
        try:
            text = filepath.read_text(encoding="utf-8", errors="ignore")
            links = extract_links(text, filepath)
            all_links.extend(links)
        except Exception as e:
            print(f"[WARN] Nao foi possivel ler {filepath}: {e}", file=sys.stderr)

    internal_links = [(url, src) for url, typ, src in all_links if typ == "internal"]
    external_links = [url for url, typ, _ in all_links if typ == "external"]

    print(f"Links encontrados: {len(all_links)} (ext: {len(external_links)}, int: {len(internal_links)})")

    failed = []

    # Check external links in parallel
    if external_links:
        unique_external = list(set(external_links))
        print(f"Verificando {len(unique_external)} links externos unicos...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {executor.submit(check_external_link, url): url for url in unique_external}
            for future in concurrent.futures.as_completed(futures):
                url, ok, msg = future.result()
                status = "✅" if ok else "❌"
                print(f"  {status} {url} — {msg}")
                if not ok:
                    failed.append((url, "external", msg))

    # Check internal links
    if internal_links:
        print(f"Verificando {len(internal_links)} links internos...")
        for url, src_file in internal_links:
            _, ok, msg = check_internal_link(url, src_file)
            status = "✅" if ok else "❌"
            if not ok:
                print(f"  {status} {url} (em {src_file.relative_to(ROOT)}) — {msg}")
                failed.append((url, "internal", msg))

    if failed:
        print(f"\n❌ {len(failed)} links quebrados encontrados:")
        for url, typ, msg in failed:
            print(f"  [{typ}] {url}: {msg}")
        sys.exit(1)
    else:
        print("\n✅ Todos os links estao OK!")
        sys.exit(0)


if __name__ == "__main__":
    main()
