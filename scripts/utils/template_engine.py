from pathlib import Path
from jinja2 import Environment, FileSystemLoader


class TemplateEngine:
    def __init__(self, templates_dir: Path):
        self.env = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def render(self, template_name: str, **kwargs) -> str:
        template = self.env.get_template(template_name)
        return template.render(**kwargs)


def generate_frontmatter(templates_dir: Path, book_data: dict) -> dict:
    engine = TemplateEngine(templates_dir)
    frontmatter = {}

    if book_data.get("generate_preface"):
        frontmatter["preface"] = engine.render(
            "frontmatter/prefacio.md.j2",
            title=book_data["title"],
            author=book_data["author"],
            year=book_data.get("year", 2026),
            course_names=book_data.get("course_names", []),
        )

    if book_data.get("generate_copyright"):
        frontmatter["copyright"] = engine.render(
            "frontmatter/copyright.md.j2",
            title=book_data["title"],
            author=book_data["author"],
            year=book_data.get("year", 2026),
            isbn=book_data.get("isbn", ""),
            edition=book_data.get("edition", 1),
        )

    if book_data.get("generate_about"):
        frontmatter["about_author"] = engine.render(
            "frontmatter/sobre_autor.md.j2",
            author=book_data["author"],
            description=book_data.get("author_description", ""),
        )

    return frontmatter
