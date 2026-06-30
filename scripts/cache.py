"""
cache.py — Content-addressed build cache for incremental pipeline execution.
Tracks file hashes to avoid regenerating unchanged outputs.

Usage:
    cache = BuildCache()
    if cache.is_stale("module-08-arquitetura", "slides"):
        # regenerate
        cache.mark_done("module-08-arquitetura", "slides", sources=["aula.md"])
"""

import hashlib
import json
from datetime import datetime
from pathlib import Path

from config import RUNS_DIR


class BuildCache:
    """Tracks which builds are stale based on source file hashes."""

    def __init__(self):
        self.cache_dir = RUNS_DIR
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache_file = self.cache_dir / "build-cache.json"
        self._cache = self._load()

    def _load(self) -> dict:
        if self.cache_file.exists():
            try:
                return json.loads(self.cache_file.read_text())
            except (json.JSONDecodeError, ValueError):
                return {}
        return {}

    def _save(self):
        self.cache_file.write_text(
            json.dumps(self._cache, indent=2, ensure_ascii=False)
        )

    def _hash_file(self, path: Path) -> str | None:
        if not path.exists():
            return None
        return hashlib.sha256(path.read_bytes()).hexdigest()[:16]

    def _hash_sources(self, sources: list[Path]) -> str:
        combined = hashlib.sha256()
        for src in sources:
            h = self._hash_file(src) or ""
            combined.update(h.encode())
        return combined.hexdigest()[:16]

    def is_stale(
        self,
        item_id: str,
        output_type: str,
        sources: list[Path] | None = None,
    ) -> bool:
        """Returns True if the output needs regeneration."""
        key = f"{item_id}:{output_type}"
        entry = self._cache.get(key)

        if entry is None:
            return True  # never built

        if sources:
            current_hash = self._hash_sources(sources)
            return entry.get("source_hash") != current_hash

        return False  # no sources to check, assume fresh

    def mark_done(
        self,
        item_id: str,
        output_type: str,
        sources: list[Path] | None = None,
    ):
        """Records a successful build."""
        key = f"{item_id}:{output_type}"
        self._cache[key] = {
            "timestamp": datetime.utcnow().isoformat(),
            "source_hash": self._hash_sources(sources) if sources else None,
        }
        self._save()

    def invalidate(self, item_id: str, output_type: str | None = None):
        """Force rebuild of an item."""
        if output_type:
            self._cache.pop(f"{item_id}:{output_type}", None)
        else:
            self._cache = {
                k: v for k, v in self._cache.items() if not k.startswith(f"{item_id}:")
            }
        self._save()

    def clear(self):
        """Invalidate entire cache."""
        self._cache = {}
        self._save()
