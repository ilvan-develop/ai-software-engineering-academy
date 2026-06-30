#!/usr/bin/env python3
"""
build_epub.py
Converte Markdown para EPUB (ebooklib).
"""

import argparse
import sys
import re
import logging
from pathlib import Path
from ebooklib import epub
import markdown as md_lib


def slugify(text: str) -> str:
    return re.sub(r"[^\w\s-]", "", text.lower()).replace(" ", "-")


def _preprocess_callouts(md_text: str) -> str:
    """Convert > **[TIPO]** callouts to styled HTML divs for EPUB."""
    callout_re = re.compile(
        r'^>\s*\*\*\[(DICA|ATENCAO|CUIDADO|DEFINICAO|INFO|RECAPITULANDO|TIP)\]\*\*\s*(.*?)$',
        re.IGNORECASE | re.MULTILINE
    )
    callout_type_map = {
        "DICA": ("tip", "DICA"),
        "TIP": ("tip", "DICA"),
        "ATENCAO": ("warning", "ATENCAO"),
        "CUIDADO": ("warning", "CUIDADO"),
        "DEFINICAO": ("definition", "DEFINICAO"),
        "INFO": ("info", "INFO"),
        "RECAPITULANDO": ("recap", "RECAPITULANDO"),
    }
    def _replace(m):
        marker = m.group(1).upper()
        variant, label = callout_type_map.get(marker, ("info", marker))
        text = m.group(2).strip()
        return f'<div class="callout callout-{variant}"><span class="callout-title">{label}:</span> {text}</div>'
    return callout_re.sub(_replace, md_text)


def build_epub(input_path: Path, output_path: Path, title: str, author: str, language: str = "pt"):
    logging.getLogger("ebooklib").setLevel(logging.ERROR)

    book = epub.EpubBook()
    book_id = slugify(title) or "book"
    book.set_identifier(book_id)
    book.set_title(title)
    book.set_language(language)
    book.add_author(author)
    book.add_metadata('DC', 'description', 'Guia pratico para desenvolvedores usarem inteligencia artificial de forma produtiva, evitando os erros mais comuns. Cobre desde fundamentos de prompt engineering ate automacao de pipelines com CI/CD, agentes especializados e infraestrutura como codigo.')
    book.add_metadata('DC', 'language', 'pt-BR')
    book.add_metadata('DC', 'rights', 'CC BY-NC-SA 4.0')
    book.add_metadata('DC', 'subject', 'Inteligencia Artificial; Desenvolvimento de Software; Programacao')
    book.add_metadata('DC', 'identifier', '978-65-992345-00-0', {'id': 'isbn'})

    css = ":root { --primary: #1A237E; --secondary: #0D47A1; --accent: #00BFA5; --body: #212121; --muted: #757575; --code-bg: #F5F5F5; --code-text: #212121; --table-alt-row: #F5F5F5; --link-color: #1976D2; }"
    css += "@media (prefers-color-scheme: dark) { :root { --primary: #5C6BC0; --secondary: #7986CB; --accent: #4DB6AC; --body: #E0E0E0; --muted: #9E9E9E; --code-bg: #263238; --code-text: #EEFFFF; --callout-info-bg: #1A237E; --callout-info-border: #5C6BC0; --callout-warning-bg: #3E2723; --callout-warning-border: #F57F17; --callout-tip-bg: #1B5E20; --callout-tip-border: #4DB6AC; --table-header-bg: #0D47A1; --table-alt-row: #263238; --link-color: #90CAF9; } }"
    css += "body { font-family: Georgia, 'Times New Roman', serif; line-height: 1.6; color: var(--body); max-width: 720px; margin: 0 auto; padding: 16px; }"
    css += "h1, h2, h3, h4 { font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; }"
    css += "h1 { color: var(--primary); border-bottom: 2px solid var(--accent); padding-bottom: 5px; font-size: 1.8em; }"
    css += "h2 { color: var(--primary); font-size: 1.4em; } h3 { color: var(--secondary); font-size: 1.15em; } h4 { color: var(--body); font-size: 1em; }"
    css += "code { font-family: 'Cascadia Code', 'Fira Code', Consolas, monospace; background: var(--code-bg); color: var(--code-text); padding: 2px 6px; border-radius: 3px; font-size: 0.85em; }"
    css += "pre { background: var(--code-bg); color: var(--code-text); padding: 12px; border-radius: 4px; overflow-x: auto; font-size: 0.85em; line-height: 1.5; }"
    css += "pre { position: relative; }"
    css += "pre::before { content: attr(data-lang); position: absolute; top: 0; right: 0; background: #37474F; color: #E0E0E0; font-size: 0.75em; padding: 2px 6px; border-radius: 0 3px 0 3px; }"
    css += "pre code[class*=\"language-\"] { background: none; padding: 0; }"
    css += "code[class*=\"language-\"]::before { display: none; }"
    css += "blockquote { border-left: 4px solid var(--accent); padding: 8px 15px; margin: 8px 0; }"
    css += ".callout { border-left: 4px solid; padding: 8px 12px; margin: 8px 0; border-radius: 3px; page-break-inside: avoid; }"
    css += ".callout-tip { background: #E8F5E9; border-left-color: #2E7D32; }"
    css += ".callout-warning { background: #FFF8E1; border-left-color: #F57F17; }"
    css += ".callout-info { background: #E3F2FD; border-left-color: #1565C0; }"
    css += ".callout-caution { background: #FFEBEE; border-left-color: #C62828; }"
    css += ".callout-definition { background: #F3E5F5; border-left-color: #7B1FA2; }"
    css += ".callout-recap { background: #F5F5F5; border-left-color: #1A237E; }"
    css += ".callout-title { font-weight: bold; font-size: 0.9em; }"
    css += "table { border-collapse: collapse; width: 100%; margin: 8px 0; }"
    css += "th, td { border: 1px solid #BDBDBD; padding: 6px; text-align: left; }"
    css += "th { background: var(--table-header-bg, #0D47A1); color: #FFFFFF; font-weight: bold; }"
    css += "tr:nth-child(even) td { background: var(--table-alt-row, #F5F5F5); }"

    css_item = epub.EpubItem(
        uid="style_nav",
        file_name="style/nav.css",
        media_type="text/css",
        content=css,
    )
    book.add_item(css_item)

    content = input_path.read_text(encoding="utf-8")
    content = _preprocess_callouts(content)
    html_body = md_lib.markdown(
        content,
        extensions=[
            "markdown.extensions.fenced_code",
            "markdown.extensions.tables",
        ],
    )

    full_html = (
        '<html xmlns="http://www.w3.org/1999/xhtml">\n'
        f"<head><title>{title}</title>\n"
        '<link rel="stylesheet" type="text/css" href="style/nav.css"/>'
        "</head>\n"
        f"<body><div>{html_body}</div></body>\n"
        "</html>"
    )

    chapter = epub.EpubHtml(
        title=title,
        file_name="chap1.xhtml",
        lang=language,
    )
    chapter.content = full_html
    chapter.add_item(css_item)
    book.add_item(chapter)

    book.toc = [(epub.Section("Book"), [chapter])]
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ["nav", chapter]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    epub.write_epub(str(output_path), book)
    print(f"  OK EPUB salvo: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Build EPUB from Markdown")
    parser.add_argument("--input", required=True, help="Arquivo Markdown de entrada")
    parser.add_argument("--output", required=True, help="Arquivo EPUB de saida")
    parser.add_argument("--title", default="", help="Titulo do livro")
    parser.add_argument("--author", default="AI Software Engineering Academy", help="Autor")
    parser.add_argument("--language", default="pt", help="Idioma")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERRO: Arquivo nao encontrado: {input_path}")
        sys.exit(1)

    title = args.title or input_path.stem
    print(f"  Convertendo {input_path.name} -> EPUB...")
    build_epub(input_path, Path(args.output), title, args.author, args.language)


if __name__ == "__main__":
    main()
