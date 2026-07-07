"""Test that config.py paths resolve correctly."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from config import (
    PROJECT_ROOT, CURRICULUM_DIR, SOURCES_DIR, BOOKS_MANIFESTS_DIR,
    BOOKS_DIR, STATUS_PATH,
    KF_DIR, COURSES_DIR, ONLINE_COURSES_DIR,
    PIPELINE_DIR, REGISTRY_DIR, ASSETS_DIR, SCRIPTS_DIR,
    SOCIAL_DIR, NEWSLETTERS_DIR, CERTIFICATES_DIR,
)


def test_project_root_is_absolute():
    assert PROJECT_ROOT.is_absolute()


def test_project_root_exists():
    assert PROJECT_ROOT.exists()


def test_curriculum_dir():
    assert CURRICULUM_DIR == PROJECT_ROOT / "curriculum"


def test_sources_dir():
    assert SOURCES_DIR == CURRICULUM_DIR / "sources"


def test_kf_dir():
    assert KF_DIR == PROJECT_ROOT / "knowledge-factory"


def test_courses_dir():
    assert COURSES_DIR == KF_DIR / "products" / "courses"


def test_books_manifests():
    assert BOOKS_MANIFESTS_DIR == CURRICULUM_DIR / "books"


def test_books_dir():
    assert BOOKS_DIR == KF_DIR / "products" / "books"


def test_status_path():
    assert STATUS_PATH == CURRICULUM_DIR / "status.yaml"


def test_pipeline_dir():
    assert PIPELINE_DIR == KF_DIR / "pipeline"


def test_registry_dir():
    assert REGISTRY_DIR == KF_DIR / "registry"


def test_assets_dir():
    assert ASSETS_DIR == KF_DIR / "assets"


def test_scripts_dir():
    assert SCRIPTS_DIR == PROJECT_ROOT / "scripts"


EXISTENCE_PATHS = [
    CURRICULUM_DIR, SOURCES_DIR, BOOKS_MANIFESTS_DIR,
    KF_DIR, COURSES_DIR, BOOKS_DIR,
    REGISTRY_DIR, ASSETS_DIR, SCRIPTS_DIR,
    SOCIAL_DIR, NEWSLETTERS_DIR, CERTIFICATES_DIR, ONLINE_COURSES_DIR,
]


def test_all_current_paths_exist():
    failures = []
    for path in EXISTENCE_PATHS:
        if not path.exists():
            failures.append(str(path))
    assert not failures, f"Missing paths: {failures}"
