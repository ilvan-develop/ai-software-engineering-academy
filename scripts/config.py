"""
config.py — Centralized path and project configuration.
All scripts should import from here instead of redefining paths.

Usage:
    from config import PROJECT_ROOT, SOURCES_DIR, COURSES_DIR, BOOKS_DIR, ...

After migration (migrate_paths.py), update ACTIVE PATHS below.
"""

from pathlib import Path

# ── Project root ──
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ── Scripts ──
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
RENDERERS_DIR = SCRIPTS_DIR / "renderers"
DIAGRAMS_SCRIPTS_DIR = SCRIPTS_DIR / "diagrams"
FACTORIES_DIR = SCRIPTS_DIR / "factories"

# ── Curriculum (source) ──
CURRICULUM_DIR = PROJECT_ROOT / "curriculum"
BOOKS_MANIFESTS_DIR = CURRICULUM_DIR / "books"
BQS_DIR = CURRICULUM_DIR / "bqs"
STATUS_PATH = CURRICULUM_DIR / "status.yaml"

# ── Knowledge-factory root ──
KF_DIR = CURRICULUM_DIR.parent / "knowledge-factory"

# ── ACTIVE PATHS (migrated to products/{format}/) ──
# After migration, all output directories live under knowledge-factory/products/.

# Source: curriculum/sources/ (formerly curriculum/cursos/)
SOURCES_DIR = CURRICULUM_DIR / "sources"

# Products output — all under knowledge-factory/products/
PRODUCTS_DIR = KF_DIR / "products"

COURSES_DIR = PRODUCTS_DIR / "courses"
BOOKS_DIR = PRODUCTS_DIR / "books"
SOCIAL_DIR = PRODUCTS_DIR / "social"
NEWSLETTERS_DIR = PRODUCTS_DIR / "newsletters"
ONLINE_COURSES_DIR = PRODUCTS_DIR / "online-courses"
CERTIFICATES_DIR = PRODUCTS_DIR / "certificates"

# ── Infrastructure paths (stable) ──
PIPELINE_DIR = KF_DIR / "pipeline"
RUNS_DIR = PIPELINE_DIR / "runs"
REPORTS_DIR = PIPELINE_DIR / "reports"
GATES_DIR = PIPELINE_DIR / "gates"

REGISTRY_DIR = KF_DIR / "registry"
CATALOG_PATH = REGISTRY_DIR / "catalog.yaml"
TAXONOMY_PATH = REGISTRY_DIR / "taxonomy.yaml"

ASSETS_DIR = KF_DIR / "assets"
DIAGRAMS_DIR = ASSETS_DIR / "diagrams"
COVERS_DIR = ASSETS_DIR / "covers"

# ── Helper: module output path ──
def module_path(course: str, module: str) -> Path:
    """Return the output directory for a module's generated content."""
    return COURSES_DIR / course / module


def book_path(book_id: str) -> Path:
    """Return the output directory for a book."""
    return BOOKS_DIR / book_id
