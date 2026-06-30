#!/usr/bin/env python3
"""
video_engine.py
Gera roteiros de videoaula com storyboard, cenas, narracao e elementos visuais.
Template-based, formato de roteiro dividido em cenas com tempo estimado.
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


def extract_code_blocks(text: str) -> list:
    blocks = re.findall(r"```(\w*)\n(.*?)```", text, re.DOTALL)
    return [{"lang": lang or "text", "code": code.strip()} for lang, code in blocks]


def extract_objectives(text: str) -> list:
    in_obj = False
    objectives = []
    for line in text.split("\n"):
        s = line.strip()
        if re.match(r"^##?\s*Objetivos?", s):
            in_obj = True
            continue
        if in_obj and s.startswith("##"):
            break
        if in_obj and re.match(r"^\d+\.\s+", s):
            obj = re.sub(r"^\d+\.\s*\*\*", "", s)
            obj = obj.replace("**", "")
            objectives.append(obj)
    return objectives


def extract_key_points(lines: list, max_lines: int = 6) -> list:
    points = []
    for l in lines:
        s = l.strip()
        if s and not s.startswith("```") and not s.startswith("#"):
            clean = s.lstrip("-* ")
            if len(points) < max_lines:
                points.append(clean)
    return points


def generate_script(title: str, sections: list, objectives: list, code_blocks: list) -> str:
    total_estimated_minutes = 0
    scenes = []

    total_sections = len(sections)
    max_scenes = min(total_sections, 10)

    # Intro scene
    scenes.append({
        "id": 1,
        "duration": "1:30",
        "type": "intro",
        "narration": (
            f"Ola! Nesta aula vamos explorar: {title}. "
            f"Ao final, voce vai entender os conceitos fundamentais e como aplica-los na pratica. "
            f"Vamos la?"
        ),
        "visual": "Tela de abertura com titulo do modulo. Animacao suave com o nome do curso.",
        "onscreen": f"[TITULO] {title}",
        "notes": "Tom energico e convidativo. Apresentar o problema que sera resolvido."
    })
    total_estimated_minutes += 1.5

    # Objectives scene
    if objectives:
        obj_text = "; ".join(objectives)
        scenes.append({
            "id": 2,
            "duration": "1:00",
            "type": "objectives",
            "narration": f"Vamos cobrir {len(objectives)} objetivos principais: {obj_text}.",
            "visual": "Lista animada dos objetivos, um por vez com checkmark.",
            "onscreen": "\n".join([f"✓ {o}" for o in objectives]),
            "notes": "Falar pausadamente. Cada objetivo e uma promessa para o aluno."
        })
        total_estimated_minutes += 1.0

    scene_num = len(scenes) + 1

    # Content scenes
    for i, sec in enumerate(sections[:max_scenes]):
        sec_title = sec["title"]
        if not sec_title or sec_title.startswith("Introdu"):
            continue

        lines = sec["content"]
        points = extract_key_points(lines)

        duration = "3:00"
        total_estimated_minutes += 3.0

        narration_parts = [f"Agora vamos falar sobre: {sec_title}."]
        for p in points[:4]:
            narration_parts.append(p)

        narration = " ".join(narration_parts)

        # Find relevant code for this section
        code_display = ""
        for cb in code_blocks:
            code_lines = cb["code"].split("\n")
            if len(code_lines) <= 10:
                code_display = f"```{cb['lang']}\n{cb['code']}\n```"
                break

        scenes.append({
            "id": scene_num,
            "duration": duration,
            "type": "content",
            "narration": narration,
            "visual": f"Slides com topicos-chave. {code_display if code_display else 'Diagrama explicativo'}",
            "onscreen": f"[{sec_title}]",
            "notes": f"Secao {i+1} de {max_scenes}. Usar exemplos praticos."
        })
        scene_num += 1

    # Code scene
    if code_blocks:
        cb = code_blocks[0]
        code_lines = cb["code"].split("\n")
        code_display = "\n".join(code_lines[:12])
        scenes.append({
            "id": scene_num,
            "duration": "4:00",
            "type": "code-demo",
            "narration": f"Vamos ver na pratica como isso funciona. Observe este codigo em {cb['lang']}:",
            "visual": f"Tela dividida: editor de codigo a esquerda, terminal/output a direita.",
            "onscreen": f"```{cb['lang']}\n{code_display}\n```",
            "notes": "Explicar linha por linha. Destacar pontos importantes com zoom ou realce."
        })
        total_estimated_minutes += 4.0
        scene_num += 1

    # Summary scene
    scene_num = len(scenes) + 1
    summary_topics = [sec["title"] for sec in sections[:max_scenes] if sec["title"] and not sec["title"].startswith("Introdu")]
    summary_text = ", ".join(summary_topics[:6])
    scenes.append({
        "id": scene_num,
        "duration": "1:30",
        "type": "summary",
        "narration": f"Recapitulando: vimos {summary_text}. Esses conceitos sao fundamentais para sua formacao.",
        "visual": "Lista resumida com icones. Transicao suave para encerramento.",
        "onscreen": "✓ " + "\n✓ ".join(summary_topics[:6]),
        "notes": "Reforcar os aprendizados principais. Conectar com o proximo modulo."
    })
    total_estimated_minutes += 1.5

    # Call to action
    scene_num += 1
    scenes.append({
        "id": scene_num,
        "duration": "0:30",
        "type": "outro",
        "narration": "Na proxima aula, vamos aprofundar esses conceitos. Nao perca!",
        "visual": "Tela final com links, inscricao, e teaser da proxima aula.",
        "onscreen": "Proximo modulo: [TITULO DO PROXIMO MODULO]",
        "notes": "Chamada para acao: inscrever-se, comentar, compartilhar."
    })
    total_estimated_minutes += 0.5

    # Build script
    lines = [
        f"# Roteiro de Videoaula — {title}",
        "",
        f"**Duracao total estimada:** {int(total_estimated_minutes)} minutos",
        f"**Formato:** Videoaula gravada / Streaming",
        f"**Publico-alvo:** Desenvolvedores intermediarios",
        "",
        "---",
        "",
        "## Visao Geral do Video",
        "",
        f"| Item | Detalhe |",
        "|------|---------|",
        f"| Titulo | {title} |",
        f"| Duracao | {int(total_estimated_minutes)} min |",
        f"| Cenas | {len(scenes)} |",
        "| Formato | Expositivo com demonstracao pratica |",
        "| Nivel | Intermediario |",
        "",
        "---",
        "",
        "## Roteiro por Cena",
        "",
    ]

    for sc in scenes:
        lines.extend([
            f"### Cena {sc['id']} — {sc['type'].upper()}",
            "",
            f"**Duracao:** {sc['duration']}",
            "",
            "**Narracao:**",
            f"> {sc['narration']}",
            "",
            "**Visuais:**",
            f"- {sc['visual']}",
            "",
            "**Texto na tela:**",
            f"```",
            sc['onscreen'],
            f"```",
            "",
            "**Notas de direcao:**",
            f"- {sc['notes']}",
            "",
            "---",
            "",
        ])

    # Production checklist
    lines.extend([
        "## Checklist de Producao",
        "",
        "- [ ] Roteiro revisado",
        "- [ ] Slides preparados",
        "- [ ] Ambiente de codigo configurado",
        "- [ ] Microfone testado",
        "- [ ] Gravacao de tela configurada (1920x1080)",
        "- [ ] Exemplos de codigo testados",
        "- [ ] Legendas geradas",
        "- [ ] Thumbnail criada",
        "- [ ] Descricao e tags preenchidas",
        "- [ ] Capitulos do video marcados",
        "",
        "---",
        "",
        "## Sugestoes de Thumbnail",
        "",
        f"- Texto: '{title.split('—')[0] if '—' in title else title[:50]}'",
        "- Cor de fundo: azul escuro (#1a2332)",
        "- Destaque: codigo ou diagrama ao fundo",
        "- Rosto do apresentador no canto inferior direito",
        "",
        "---",
        "",
        "## SEO",
        "",
        f"**Titulo:** {title} | Arquitetura Enterprise",
        f"**Descricao:** Aprenda {title.lower()}. Nesta aula abordamos conceitos fundamentais com exemplos praticos em TypeScript.",
        "**Tags:** arquitetura, software, enterprise, typescript, desenvolvimento",
        "",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Gerador de Roteiros de Videoaula")
    parser.add_argument("--input", required=True, help="Caminho para aula.md")
    parser.add_argument("--output", required=True, help="Pasta de saida (videos/)")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERRO: Arquivo nao encontrado: {input_path}")
        sys.exit(1)

    text = input_path.read_text(encoding="utf-8")
    title = extract_title(text)
    sections = extract_sections(text)
    objectives = extract_objectives(text)
    code_blocks = extract_code_blocks(text)

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    script = generate_script(title, sections, objectives, code_blocks)
    script_path = output_dir / "roteiro-videoaula.md"
    script_path.write_text(script, encoding="utf-8")
    print(f"  OK Roteiro: {script_path}")

    print(f"  [DONE] Roteiro gerado para: {title}")


if __name__ == "__main__":
    main()
