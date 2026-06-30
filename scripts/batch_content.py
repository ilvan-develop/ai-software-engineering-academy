#!/usr/bin/env python3
"""
batch_content.py
Processa exercicios + quizzes para todos os modulos pendentes.
Le o status.yaml, encontra modulos com exercicios pendentes,
e dispara exercise_engine.py + quiz_engine.py para cada um.
Usa cache incremental para pular modulos inalterados.
"""

import sys
import subprocess
import yaml
from pathlib import Path

from config import PROJECT_ROOT, SCRIPTS_DIR, STATUS_PATH, SOURCES_DIR, COURSES_DIR
from cache import BuildCache


def load_status() -> dict:
    with open(STATUS_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_status(data: dict):
    with open(STATUS_PATH, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)


def run_engine(script: str, input_path: Path, output_dir: Path) -> bool:
    output_dir.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, str(script), f"--input={input_path}", f"--output={output_dir}"]
    print(f"  $ {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ERRO: {result.stderr}")
        return False
    for line in result.stdout.split("\n"):
        if line.strip():
            print(f"    {line}")
    return True


def main():
    data = load_status()
    modules = data.get("modules", {})
    engine_dir = SCRIPTS_DIR / "factories" / "content"
    exercise_script = engine_dir / "exercise_engine.py"
    quiz_script = engine_dir / "quiz_engine.py"
    cache = BuildCache()

    total = 0
    ok_exercises = 0
    ok_quizzes = 0
    skipped_exercises = 0
    skipped_quizzes = 0

    print(f"{'='*60}")
    print(f"  BATCH: Gerando exercicios e quizzes para modulos pendentes")
    print(f"{'='*60}\n")

    for course_name, mods in modules.items():
        for mod_id, mod in mods.items():
            outputs = mod.get("outputs", {})
            should_run_ex = outputs.get("exercicios", "raw") in ("pendente", "raw")
            should_run_qz = outputs.get("quiz", "raw") in ("pendente", "raw")

            if not should_run_ex and not should_run_qz:
                continue

            aula_path = SOURCES_DIR / course_name / mod_id / "aula" / "aula.md"
            if not aula_path.exists():
                print(f"  AVISO: aula.md nao encontrado para {course_name}/{mod_id}")
                continue

            total += 1
            title = mod.get("title", mod_id)
            print(f"\n[{total}] {course_name}/{mod_id}: {title}")

            ex_out = COURSES_DIR / course_name / mod_id / "exercicios"
            qz_out = COURSES_DIR / course_name / mod_id / "quiz"
            item_id = f"{course_name}/{mod_id}"

            if should_run_ex:
                if not cache.is_stale(item_id, "exercicios", sources=[aula_path]):
                    skipped_exercises += 1
                    print(f"  >> Exercicios: cache valido, pulando")
                else:
                    print(f"  >> Exercicios...")
                    if run_engine(exercise_script, aula_path, ex_out):
                        outputs["exercicios"] = "gerado"
                        cache.mark_done(item_id, "exercicios", sources=[aula_path])
                        ok_exercises += 1

            if should_run_qz:
                if not cache.is_stale(item_id, "quiz", sources=[aula_path]):
                    skipped_quizzes += 1
                    print(f"  >> Quiz: cache valido, pulando")
                else:
                    print(f"  >> Quiz...")
                    if run_engine(quiz_script, aula_path, qz_out):
                        outputs["quiz"] = "gerado"
                        cache.mark_done(item_id, "quiz", sources=[aula_path])
                        ok_quizzes += 1

    print(f"\n{'='*60}")
    print(f"  RESUMO:")
    print(f"  Modulos processados: {total}")
    print(f"  Exercicios gerados: {ok_exercises}")
    print(f"  Quizzes gerados: {ok_quizzes}")
    if skipped_exercises:
        print(f"  Exercicios em cache (pulados): {skipped_exercises}")
    if skipped_quizzes:
        print(f"  Quizzes em cache (pulados): {skipped_quizzes}")
    print(f"{'='*60}\n")

    save_status(data)
    print(f"  Status atualizado em: {STATUS_PATH}")


if __name__ == "__main__":
    main()
