#!/usr/bin/env python3
"""
workshop_engine.py
Gera material completo para workshop a partir de modulos.
Inclui agenda, objetivos, dinamicas, exercicios em grupo,
slides do facilitador, material do participante.
Duracao: 4h ou 8h.
"""

import argparse
import sys
import re
from pathlib import Path


def extract_title(text: str) -> str:
    for line in text.split("\n"):
        m = re.match(r"^#\s+(.+)$", line.strip())
        if m:
            return m.group(1).strip()
    return "Modulo"


def extract_sections(text: str) -> list:
    sections = []
    current_h2 = "Introducao"
    current_content = []
    for line in text.split("\n"):
        s = line.strip()
        m = re.match(r"^##\s+(.+)$", s)
        if m:
            if current_content:
                sections.append({"title": current_h2, "content": current_content})
            current_h2 = m.group(1).strip()
            current_content = []
        else:
            current_content.append(s)
    if current_content:
        sections.append({"title": current_h2, "content": current_content})
    return sections


def generate_workshop(modules_info: list, duration_h: int = 4) -> str:
    parts = []
    total_min = duration_h * 60

    # Constants for timing
    if duration_h == 4:
        blocks = [
            ("Abertura e Contextualizacao", 15),
            ("Parte 1 - Teoria", 45),
            ("Dinamica 1", 30),
            ("Intervalo", 15),
            ("Parte 2 - Pratica", 60),
            ("Dinamica 2", 45),
            ("Encerramento e Q&A", 30),
        ]
    else:  # 8h
        blocks = [
            ("Abertura e Contextualizacao", 20),
            ("Parte 1 - Teoria", 60),
            ("Dinamica 1", 40),
            ("Intervalo", 15),
            ("Parte 2 - Pratica", 75),
            ("Almoco", 60),
            ("Parte 3 - Avancado", 60),
            ("Dinamica 2", 45),
            ("Intervalo", 15),
            ("Projeto Guiado", 60),
            ("Apresentacao dos Resultados", 30),
            ("Encerramento e Q&A", 30),
        ]

    main_mod = modules_info[0] if modules_info else {"title": "Modulo"}
    topic = main_mod["title"].replace("Modulo", "").replace("—", "-").strip()

    sections_out = []
    for mod in modules_info[:3]:
        secs = [s for s in mod.get("sections", []) if s["title"] and not s["title"].startswith("Introdu")]
        sections_out.extend(secs[:4])

    # AGENDA
    agenda = "\n".join([f"| {b[0]} | {b[1]} min |" for b in blocks])

    # Build workshop document
    lines = [
        f"{'='*60}",
        f"WORKSHOP: {topic}",
        f"{'='*60}",
        "",
        f"**Duracao:** {duration_h}h",
        f"**Formato:** Presencial / Online",
        f"**Publico-alvo:** Desenvolvedores, arquitetos, tech leads",
        f"**Pre-requisitos:** Conhecimento basico em desenvolvimento de software",
        "",
        "---",
        "",
        "## Objetivos do Workshop",
        "",
        "Ao final deste workshop, os participantes serao capazes de:",
        "",
    ]
    for mod in modules_info[:3]:
        clean = mod["title"].replace("Modulo", "").replace("—", "-").strip()
        lines.append(f"- Compreender e aplicar conceitos de **{clean}**")
    lines.extend([
        "- Tomar decisoes arquiteturais fundamentadas",
        "- Aplicar os conceitos em um projeto pratico guiado",
        "",
        "---",
        "",
        "## Agenda",
        "",
        "| Atividade | Duracao |",
        "|-----------|---------|",
        agenda,
        "",
        f"**Total:** {total_min} minutos",
        "",
        "---",
        "",
        "## Material do Facilitador",
        "",
        "### Preparacao Antecipada",
        "",
        "- [ ] Slides preparados e testados",
        "- [ ] Ambiente de codigo configurado",
        "- [ ] Exemplar de codigo compilado/testado",
        "- [ ] Dinamicas ensaiadas",
        "- [ ] Material do participante impresso/digital",
        "- [ ] Backup de slides e codigo",
        "",
        "### Roteiro do Facilitador",
        "",
    ])

    # Block details
    for i, (block_name, block_dur) in enumerate(blocks):
        lines.extend([
            f"### Bloco {i+1}: {block_name} ({block_dur}min)",
            "",
        ])
        if "Abertura" in block_name:
            lines.extend([
                "**Objetivo:** Aquecer o grupo e contextualizar o tema",
                "",
                "**Roteiro:**",
                "1. Apresentacao dos facilitadores (2min)",
                '2. Icebreaker: "O que voce espera aprender hoje?" (5min)',
                "3. Agenda do dia (3min)",
                "4. Contextualizacao do problema que sera resolvido (5min)",
                "",
            ])
        elif "Teoria" in block_name:
            lines.extend([
                "**Objetivo:** Apresentar os fundamentos teoricos",
                "",
                "**Roteiro:**",
            ])
            for j, sec in enumerate(sections_out[:4], 1):
                lines.append(f"{j}. {sec['title']} (15min)")
            lines.append("")
            lines.append("**Tecnica:** Exposicao dialogada com slides + perguntas")
            lines.append("")
        elif "Dinamica" in block_name:
            lines.extend([
                "**Objetivo:** Fixar o aprendizado com atividade pratica em grupo",
                "",
                "**Dinamica:**",
                "1. Dividir em grupos de 3-4 pessoas",
                "2. Cada grupo recebe um problema para resolver",
                "3. 15min para discussao e esboco de solucao",
                "4. 10min para apresentacao ao grande grupo",
                "5. 5min de feedback do facilitador",
                "",
                "**Material necessario:** Post-its, flipchart, canetas",
                "",
            ])
        elif "Intervalo" in block_name or "Almoco" in block_name:
            lines.append("**Pausa para descanso e networking.**\n")
        elif "Pratica" in block_name or "Projeto" in block_name:
            lines.extend([
                "**Objetivo:** Aplicar conceitos em um projeto real",
                "",
                "**Roteiro:**",
                "1. Explicacao do cenario do projeto (5min)",
                "2. Setup do ambiente (5min)",
                "3. Implementacao guiada passo a passo (40min)",
                "4. Duvidas e suporte individual (10min)",
                "",
                "**Entregavel:** Projeto funcional com documentacao basica",
                "",
            ])
        elif "Apresentacao" in block_name:
            lines.extend([
                "**Objetivo:** Compartilhar resultados e aprender com os colegas",
                "",
                "**Roteiro:**",
                "1. Cada grupo apresenta sua solucao (5min cada)",
                "2. Perguntas e discussao (10min)",
                "3. Facilita destacar pontos comuns e diferencas",
                "",
            ])
        elif "Encerramento" in block_name:
            lines.extend([
                "**Objetivo:** Reforcar aprendizados e proximos passos",
                "",
                "**Roteiro:**",
                "1. Recap dos principais topicos (10min)",
                "2. Q&A aberto (10min)",
                "3. Feedback dos participantes (5min)",
                "4. Material de apoio e leitura recomendada (5min)",
                "",
            ])
        lines.append("---\n")

    # Material do participante
    lines.extend([
        "## Material do Participante",
        "",
        "### Antes do Workshop",
        "",
        "- [ ] Leia o material de introducao (enviado por email)",
        "- [ ] Instale as ferramentas necessarias (lista em anexo)",
        "- [ ] Crie uma conta no GitHub (se nao tiver)",
        "",
        "### Durante o Workshop",
        "",
        "- Caderno para anotacoes",
        "- Computador com ambiente configurado",
        "- Vontade de participar e perguntar!",
        "",
        "### Apos o Workshop",
        "",
        "- [ ] Complete o exercicio pratico individual",
        "- [ ] Leia o artigo complementar",
        "- [ ] Participe do grupo de discussao no Telegram",
        "",
        "---",
        "",
        "## Checklist de Producao",
        "",
        "- [ ] Sala reservada / link de reuniao criado",
        "- [ ] Coffee break confirmado (presencial)",
        "- [ ] Projetor/testar tela",
        "- [ ] Som e microfone testados",
        "- [ ] Material impresso (participantes)",
        "- [ ] Certificados preparados",
        "- [ ] Lista de presenca",
        "- [ ] Pesquisa de satisfacao",
        "- [ ] Grupos de 3-4 definidos antecipadamente",
        "- [ ] Backup de slides em USB/nuvem",
        "",
        "---",
        "",
        "## Recursos Adicionais",
        "",
        "### Leitura Recomendada",
        "",
        f"- Documentacao oficial dos topicos abordados",
        f"- Artigos complementares sobre {topic}",
        "",
        "### Ferramentas",
        "",
        "- VS Code / WebStorm",
        "- Node.js + TypeScript",
        "- Git + GitHub",
        "- Postman / Insomnia",
        "",
        "---",
        "",
        "## Feedback dos Participantes",
        "",
        "Por favor, avalie o workshop de 1 a 5:",
        "",
        "| Criterio | Nota (1-5) | Comentario |",
        "|----------|------------|------------|",
        "| Conteudo | | |",
        "| Facilitacao | | |",
        "| Material | | |",
        "| Pratico | | |",
        "| Geral | | |",
        "",
        "**Sugestoes de melhoria:**",
        "",
        "",
        "---",
        "",
        "*Workshop gerado automaticamente pela AI Software Engineering Academy*",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Gerador de Material de Workshop")
    parser.add_argument("--input-dir", help="Pasta raiz dos modulos (modo multi-modulo)")
    parser.add_argument("--input", help="Arquivo aula.md unico (modo modulo unico)")
    parser.add_argument("--output", required=True, help="Pasta de saida (workshop/)")
    parser.add_argument("--duration", type=int, default=4, choices=[4, 8], help="Duracao em horas")
    parser.add_argument("--max-modules", type=int, default=3, help="Maximo de modulos para agregar (apenas modo --input-dir)")
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    modules_info = []

    if args.input:
        aula_path = Path(args.input)
        if not aula_path.exists():
            print(f"Arquivo nao encontrado: {aula_path}")
            sys.exit(1)
        text = aula_path.read_text(encoding="utf-8")
        title = extract_title(text)
        sections = extract_sections(text)
        # Derive course/module_id from path parts
        rel = aula_path.relative_to(aula_path.anchor if aula_path.is_absolute() else ".")  # fallback
        parts = aula_path.parts
        try:
            src_idx = parts.index("sources")
            course = parts[src_idx + 1]
            module_id = parts[src_idx + 2]
        except (ValueError, IndexError):
            course = "unknown"
            module_id = aula_path.parent.parent.name
        modules_info.append({
            "course": course,
            "module_id": module_id,
            "title": title,
            "sections": sections,
            "path": aula_path,
        })
    elif args.input_dir:
        input_dir = Path(args.input_dir)
        for course_dir in sorted(input_dir.iterdir()):
            if not course_dir.is_dir():
                continue
            for mod_dir in sorted(course_dir.iterdir()):
                if not mod_dir.is_dir():
                    continue
                if len(modules_info) >= args.max_modules:
                    break
                aula_path = mod_dir / "aula" / "aula.md"
                if not aula_path.exists():
                    continue
                text = aula_path.read_text(encoding="utf-8")
                title = extract_title(text)
                sections = extract_sections(text)
                modules_info.append({
                    "course": course_dir.name,
                    "module_id": mod_dir.name,
                    "title": title,
                    "sections": sections,
                    "path": aula_path,
                })
            if len(modules_info) >= args.max_modules:
                break
    else:
        print("Informe --input (modulo unico) ou --input-dir (multi-modulos)")
        sys.exit(1)

    if not modules_info:
        print("Nenhum modulo encontrado")
        sys.exit(1)

    workshop = generate_workshop(modules_info, args.duration)
    filename = f"workshop-{args.duration}h.md"
    w_path = output_dir / filename
    w_path.write_text(workshop, encoding="utf-8")
    print(f"  OK Workshop: {w_path} ({args.duration}h, {len(modules_info)} modulos)")

    print(f"  [DONE] Workshop gerado com base em {len(modules_info)} modulos")


if __name__ == "__main__":
    main()
