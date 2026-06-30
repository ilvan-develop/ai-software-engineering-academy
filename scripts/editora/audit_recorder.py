#!/usr/bin/env python3
"""
audit_recorder.py
Registra cada execução do pipeline com timestamp, agente, score e decisão.
Log é append-only com hash SHA256 para garantir imutabilidade.
"""
import hashlib
import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
LOGS_DIR = PROJECT_ROOT / "logs" / "audit"


class AuditTrail:
    """Audit trail com verificação de integridade (hash chain)"""

    def __init__(self, book_id: str):
        self.book_id = book_id
        self.log_dir = LOGS_DIR / book_id
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.log_path = self.log_dir / f"audit-trail-{book_id}.log"
        self._ensure_log_exists()

    def _ensure_log_exists(self):
        if not self.log_path.exists():
            with open(self.log_path, "w", encoding="utf-8") as f:
                f.write(f"# Audit Trail — Book: {self.book_id}\n")
                f.write(f"# Created: {datetime.now().isoformat()}\n")
                f.write(f"# Format: [timestamp] [agent] [action] [score] [decision] [hash]\n")
                f.write(f"{'─'*120}\n")

    def _get_last_hash(self) -> str:
        """Lê o último hash do arquivo de log"""
        try:
            with open(self.log_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            for line in reversed(lines):
                if line.strip() and not line.startswith("#") and not line.startswith("─"):
                    parts = line.strip().split("|")
                    if len(parts) >= 6:
                        return parts[5].strip()
        except Exception:
            pass
        return "0" * 64  # Genesis hash

    def _compute_hash(self, entry: str, previous_hash: str) -> str:
        """Calcula SHA256 da entrada + hash anterior"""
        content = f"{previous_hash}\n{entry}"
        return hashlib.sha256(content.encode()).hexdigest()

    def register(self, agent: str, action: str, score: float = None,
                 decision: str = None, metadata: dict = None) -> dict:
        """Registra uma entrada no audit trail"""
        timestamp = datetime.now().isoformat()
        previous_hash = self._get_last_hash()

        entry_data = {
            "timestamp": timestamp,
            "agent": agent,
            "action": action,
            "score": score,
            "decision": decision,
            "metadata": metadata or {}
        }

        # Formato legível
        score_str = f"{score:.1f}" if score is not None else "-"
        decision_str = decision if decision else "-"
        entry_text = f"{timestamp} | {agent:<25} | {action:<20} | {score_str:>6} | {decision_str:<12}".rstrip()

        # Compute hash
        entry_hash = self._compute_hash(entry_text, previous_hash)
        entry_text += f" | {entry_hash}"

        # Append to log
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(entry_text + "\n")

        # Also save structured JSON for programmatic use
        entry_data["hash"] = entry_hash
        entry_data["previous_hash"] = previous_hash

        json_path = self.log_dir / f"entry-{timestamp.replace(':', '-')}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(entry_data, f, ensure_ascii=False, indent=2)

        return entry_data

    def verify_integrity(self) -> dict:
        """Verifica a integridade de todo o audit trail"""
        with open(self.log_path, "r", encoding="utf-8") as f:
            raw_lines = f.readlines()

        lines = [l.rstrip("\n\r") for l in raw_lines
                 if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("─")]

        previous_hash = "0" * 64
        entries_verified = 0
        entries_failed = 0

        for line in lines:
            idx = line.rfind("|")
            if idx == -1:
                entries_failed += 1
                continue

            stored_hash = line[idx + 1:].strip()
            entry_text = line[:idx].rstrip()

            expected_hash = hashlib.sha256(
                f"{previous_hash}\n{entry_text}".encode()
            ).hexdigest()

            if expected_hash == stored_hash:
                entries_verified += 1
                previous_hash = stored_hash
            else:
                entries_failed += 1

        return {
            "log_path": str(self.log_path),
            "total_entries": len(lines),
            "verified": entries_verified,
            "failed": entries_failed,
            "intact": entries_failed == 0
        }

    def get_summary(self) -> dict:
        """Retorna resumo do audit trail"""
        entries = []
        with open(self.log_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() and not line.startswith("#") and not line.startswith("─"):
                    parts = line.strip().split(" | ")
                    if len(parts) >= 4:
                        entries.append({
                            "timestamp": parts[0],
                            "agent": parts[1],
                            "action": parts[2],
                            "score": parts[3],
                            "decision": parts[4] if len(parts) > 4 else "-"
                        })

        scores = [e["score"] for e in entries if e["score"] != "-"]
        decisions = [e["decision"] for e in entries if e["decision"] != "-"]

        return {
            "book_id": self.book_id,
            "total_entries": len(entries),
            "agents_involved": list(set(e["agent"] for e in entries)),
            "actions": list(set(e["action"] for e in entries)),
            "last_entry": entries[-1] if entries else None,
            "integrity": self.verify_integrity()
        }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Audit Trail Recorder — Pipeline Editorial")
    parser.add_argument("--book-id", required=True, help="ID do livro")
    parser.add_argument("command", choices=["register", "verify", "summary"])
    parser.add_argument("--agent", help="Nome do agente (para register)")
    parser.add_argument("--action", help="Ação executada (para register)")
    parser.add_argument("--score", type=float, help="Score (para register)")
    parser.add_argument("--decision", help="Decisão (para register)")

    args = parser.parse_args()
    audit = AuditTrail(args.book_id)

    if args.command == "register":
        if not args.agent or not args.action:
            print("ERRO: --agent e --action são obrigatórios para register")
            sys.exit(1)
        entry = audit.register(args.agent, args.action, args.score, args.decision)
        print(f"✅ Registrado: {entry['timestamp']} | {entry['agent']} | {entry['action']} | hash: {entry['hash'][:16]}...")

    elif args.command == "verify":
        result = audit.verify_integrity()
        status = "✅ ÍNTEGRO" if result["intact"] else "❌ VIOLADO"
        print(f"\nAudit Trail: {result['log_path']}")
        print(f"Entradas: {result['total_entries']}")
        print(f"Verificadas: {result['verified']}")
        print(f"Falhas: {result['failed']}")
        print(f"Status: {status}")

    elif args.command == "summary":
        summary = audit.get_summary()
        integrity = summary["integrity"]
        status = "✅ ÍNTEGRO" if integrity["intact"] else "❌ VIOLADO"
        print(f"\n📋 Audit Trail Summary — {summary['book_id']}")
        print(f"   Entradas: {summary['total_entries']}")
        print(f"   Agentes: {', '.join(summary['agents_involved'])}")
        print(f"   Status: {status}")
        if summary["last_entry"]:
            print(f"   Última: {summary['last_entry']['timestamp']} | {summary['last_entry']['agent']} | {summary['last_entry']['action']}")


if __name__ == "__main__":
    import sys
    main()
