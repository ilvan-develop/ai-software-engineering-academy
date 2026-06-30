from pathlib import Path
import re
import markdown as md_lib


class InlineSegment:
    def __init__(self, text, bold=False, italic=False, code=False):
        self.text = text
        self.bold = bold
        self.italic = italic
        self.code = code

    def __repr__(self):
        return f"InlineSegment({self.text!r}, bold={self.bold}, italic={self.italic}, code={self.code})"


def parse_inline(text):
    segments = []
    pattern = r'(\*\*(.+?)\*\*)|(\*(.+?)\*)|(`(.+?)`)'
    last_end = 0
    for m in re.finditer(pattern, text):
        if m.start() > last_end:
            segments.append(InlineSegment(text[last_end:m.start()]))
        if m.group(1):
            segments.append(InlineSegment(m.group(2), bold=True))
        elif m.group(3):
            segments.append(InlineSegment(m.group(4), italic=True))
        elif m.group(5):
            segments.append(InlineSegment(m.group(6), code=True))
        last_end = m.end()
    if last_end < len(text):
        segments.append(InlineSegment(text[last_end:]))
    return segments


class BlockType:
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    CODE = "code"
    LIST = "list"
    LIST_ITEM = "list_item"
    HR = "hr"
    BLOCKQUOTE = "blockquote"
    TABLE = "table"
    TIP = "tip"
    WARNING = "warning"
    DEFINICAO = "definition"
    INFO = "info"
    RECAPITULANDO = "recap"
    MERMAID = "mermaid"


class MdBlock:
    def __init__(self, type_, content, level=0, language=None, items=None):
        self.type = type_
        self.content = content
        self.level = level
        self.language = language
        self.items = items or []

    def __repr__(self):
        return f"MdBlock({self.type}, lvl={self.level}, {self.content[:50] if self.content else ''})"


class MdDocument:
    def __init__(self, title="", blocks=None):
        self.title = title
        self.blocks = blocks or []

    @property
    def headings(self):
        return [b for b in self.blocks if b.type == BlockType.HEADING]


CALLOUT_MARKER_RE = re.compile(
    r'^\s*\*\*\[(DICA|ATENCAO|CUIDADO|DEFINICAO|INFO|RECAPITULANDO)\]\*\*\s*(.*)',
    re.IGNORECASE
)
GITHUB_CALLOUT_RE = re.compile(
    r'^\s*\[!(TIP|NOTE|WARNING|CAUTION|IMPORTANT|INFO)\]',
    re.IGNORECASE
)

CALLOUT_TYPE_MAP = {
    "DICA": BlockType.TIP,
    "TIP": BlockType.TIP,
    "NOTE": BlockType.TIP,
    "ATENCAO": BlockType.WARNING,
    "CUIDADO": BlockType.WARNING,
    "WARNING": BlockType.WARNING,
    "CAUTION": BlockType.WARNING,
    "IMPORTANT": BlockType.WARNING,
    "DEFINICAO": BlockType.DEFINICAO,
    "INFO": BlockType.INFO,
    "RECAPITULANDO": BlockType.RECAPITULANDO,
}


def _parse_callout(text_content: str):
    m = CALLOUT_MARKER_RE.match(text_content)
    if m:
        marker = m.group(1).upper()
        first_line = m.group(2).strip()
        remaining = text_content[m.end():].lstrip("\n").strip()
        if remaining:
            clean = first_line + "\n" + remaining
        else:
            clean = first_line
        return CALLOUT_TYPE_MAP.get(marker, BlockType.BLOCKQUOTE), clean

    m = GITHUB_CALLOUT_RE.match(text_content)
    if m:
        marker = m.group(1).upper()
        clean = text_content[m.end():].strip()
        return CALLOUT_TYPE_MAP.get(marker, BlockType.BLOCKQUOTE), clean

    return None, text_content


def parse_markdown(text: str) -> MdDocument:
    lines = text.split("\n")
    blocks = []
    title = ""
    i = 0

    while i < len(lines):
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        if line.startswith("# "):
            title = line[2:].strip()
            blocks.append(MdBlock(BlockType.HEADING, line[2:].strip(), level=1))
            i += 1

        elif line.startswith("## "):
            blocks.append(MdBlock(BlockType.HEADING, line[3:].strip(), level=2))
            i += 1

        elif line.startswith("### "):
            blocks.append(MdBlock(BlockType.HEADING, line[4:].strip(), level=3))
            i += 1

        elif line.startswith("#### "):
            blocks.append(MdBlock(BlockType.HEADING, line[5:].strip(), level=4))
            i += 1

        elif line.startswith("```"):
            lang = line[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1
            code_content = "\n".join(code_lines)
            if lang.lower() == "mermaid":
                blocks.append(MdBlock(BlockType.MERMAID, code_content, language=lang))
            else:
                blocks.append(MdBlock(BlockType.CODE, code_content, language=lang))

        elif line.startswith("> "):
            quote_lines = []
            while i < len(lines) and lines[i].startswith("> "):
                quote_lines.append(lines[i][2:])
                i += 1
            text_content = "\n".join(quote_lines)
            block_type, clean = _parse_callout(text_content)
            if block_type:
                blocks.append(MdBlock(block_type, clean))
            else:
                blocks.append(MdBlock(BlockType.BLOCKQUOTE, text_content))

        elif line.startswith("---"):
            blocks.append(MdBlock(BlockType.HR, "---"))
            i += 1

        elif line.startswith("- ") or line.startswith("* "):
            items = []
            while i < len(lines) and (lines[i].startswith("- ") or lines[i].startswith("* ")):
                items.append(lines[i][2:].strip())
                i += 1
            blocks.append(MdBlock(BlockType.LIST, "", items=items))

        elif re.match(r'^\d+[.)]\s', line):
            items = []
            while i < len(lines) and re.match(r'^\d+[.)]\s', lines[i]):
                items.append(re.sub(r'^\d+[.)]\s', '', lines[i]).strip())
                i += 1
            blocks.append(MdBlock(BlockType.LIST, "", items=items))

        elif "|" in line and line.strip().startswith("|"):
            table_lines = []
            while i < len(lines) and line.strip().startswith("|"):
                table_lines.append(line.strip())
                i += 1
                if i < len(lines):
                    line = lines[i]
                else:
                    break
            blocks.append(MdBlock(BlockType.TABLE, "\n".join(table_lines)))

        else:
            para_lines = []
            while i < len(lines) and line.strip() and not line.startswith("#") and not line.startswith("```") and not line.startswith(">") and not line.startswith("- ") and not line.startswith("* ") and not line.startswith("|") and not line.startswith("---") and not re.match(r'^\d+[.)]\s', line):
                para_lines.append(line.rstrip())
                i += 1
                if i < len(lines):
                    line = lines[i]
                else:
                    break
            if not para_lines:
                para_lines.append(line.rstrip())
                i += 1
            blocks.append(
                MdBlock(BlockType.PARAGRAPH, "\n".join(para_lines).strip())
            )
            if i >= len(lines):
                break

    return MdDocument(title=title, blocks=blocks)


def md_to_html(text: str) -> str:
    extensions = [
        "markdown.extensions.fenced_code",
        "markdown.extensions.tables",
        "markdown.extensions.nl2br",
    ]
    return md_lib.markdown(text, extensions=extensions)
