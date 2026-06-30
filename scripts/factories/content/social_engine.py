#!/usr/bin/env python3
"""
social_engine.py
Gera conteudo para redes sociais a partir de aula.md:
- LinkedIn (post + artigo)
- Instagram (carrossel)
- YouTube (descricao + capitulos)
- Twitter/X (thread)
Gera tambem prompts DALL-E/Midjourney para artes.
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


def extract_key_points(lines: list, max_lines: int = 5) -> list:
    points = []
    for l in lines:
        s = l.strip()
        if s and not s.startswith("```") and not s.startswith("#"):
            clean = s.lstrip("-* ")
            if len(clean) > 20 and len(points) < max_lines:
                points.append(clean)
    return points


def generate_linkedin_post(title: str, sections: list) -> str:
    topic = title.replace("Modulo", "").replace("—", "-").strip()
    key_sections = [s for s in sections if s["title"] and not s["title"].startswith("Introdu")]
    points = []
    for s in key_sections[:4]:
        kp = extract_key_points(s["content"], 1)
        if kp:
            points.append(f"  {kp[0][:100]}")
        else:
            points.append(f"  {s['title']}")

    return f"""{'='*50}
LINKEDIN — Post
{'='*50}

💡 {topic}

{"".join(points)}

Se voce e dev e quer elevar o nivel dos seus projetos, esse conteudo e pra voce.

#ArquiteturaDeSoftware #Enterprise #TypeScript #CarreiraTech

🔗 Comente "QUERO" para receber mais conteudos como este.
"""


def generate_linkedin_article(title: str, sections: list) -> str:
    topic = title.replace("Modulo", "").replace("—", "-").strip()
    key_sections = [s for s in sections if s["title"] and not s["title"].startswith("Introdu")]

    body = ""
    for s in key_sections[:5]:
        kp = extract_key_points(s["content"], 3)
        body += f"\n## {s['title']}\n\n"
        for p in kp:
            body += f"- {p}\n"

    return f"""{'='*50}
LINKEDIN — Artigo
{'='*50}

Titulo: {topic}: O Que Todo Arquiteto Deveria Saber

{body}

---

🔥 Gostou? Compartilhe e marque alguem que precisa ler isso.

#ArquiteturaDeSoftware #EngenhariaDeSoftware #CarreiraDev
"""


def generate_instagram_carousel(title: str, sections: list) -> str:
    topic = title.replace("Modulo", "").replace("—", "-").strip()
    key_sections = [s for s in sections if s["title"] and not s["title"].startswith("Introdu")]

    slides_text = f"Slide 1: {topic}\n"
    for i, s in enumerate(key_sections[:5], 2):
        kp = extract_key_points(s["content"], 1)
        bullet = kp[0][:80] if kp else s["title"]
        slides_text += f"Slide {i}: {s['title']} — {bullet}\n"

    return f"""{'='*50}
INSTAGRAM — Carrossel (5-8 slides)
{'='*50}

Estrategia visual:
- Fundo: gradiente azul escuro (#1a2332 -> #0d47a1)
- Fonte: bold, branca, com destaque amarelo para numeros
- Icones minimalistas no topo

Conteudo por slide:
{slides_text}
Ultimo slide: CTA "Salve para ler depois"

Prompt DALL-E para capa:
"Professional tech background with blue gradient, minimalist code snippets floating, modern corporate style, no text, 16:9"
"""


def generate_youtube(title: str, sections: list) -> str:
    topic = title.replace("Modulo", "").replace("—", "-").strip()
    key_sections = [s for s in sections if s["title"] and not s["title"].startswith("Introdu")]

    chapters = ""
    time = 0
    for s in key_sections[:8]:
        minutes = time // 60
        secs = time % 60
        chapters += f"{minutes:02d}:{secs:02d} - {s['title']}\n"
        time += 180

    return f"""{'='*50}
YOUTUBE — Descricao
{'='*50}

Titulo: {topic}

Neste video voce vai aprender os conceitos fundamentais de {topic.lower()} com exemplos praticos.

📌 CAPITULOS:
{chapters}

🔗 Links e recursos:
- Repositorio: [link]
- Documentacao oficial: [link]

👍 Se inscreva para mais conteudos de arquitetura!

#Arquitetura #Dev #Tutorial

Prompt thumbnail:
"'{topic}' text overlay, dark blue background with glowing code, arrow pointing to key concept, professional style"
"""


def generate_twitter_thread(title: str, sections: list) -> str:
    topic = title.replace("Modulo", "").replace("—", "-").strip()
    key_sections = [s for s in sections if s["title"] and not s["title"].startswith("Introdu")]

    tweets = [f"🧵 {topic}\n\nUma thread para voce dominar esse conceito."]
    for s in key_sections[:6]:
        kp = extract_key_points(s["content"], 2)
        tweet = f"{s['title']}:\n"
        for p in kp:
            tweet += f"→ {p[:100]}\n"
        tweets.append(tweet)
    tweets.append("Curtiu? Salve e compartilhe! 🚀")

    return f"""{'='*50}
TWITTER/X — Thread
{'='*50}

{"\n\n".join(tweets)}

#DevTips #Arquitetura
"""


def main():
    parser = argparse.ArgumentParser(description="Gerador de Conteudo para Redes Sociais")
    parser.add_argument("--input", required=True, help="Caminho para aula.md")
    parser.add_argument("--output", required=True, help="Pasta de saida (social/)")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERRO: Arquivo nao encontrado: {input_path}")
        sys.exit(1)

    text = input_path.read_text(encoding="utf-8")
    title = extract_title(text)
    sections = extract_sections(text)

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    outputs = {
        "linkedin-post": generate_linkedin_post,
        "linkedin-artigo": generate_linkedin_article,
        "instagram-carrossel": generate_instagram_carousel,
        "youtube-descricao": generate_youtube,
        "twitter-thread": generate_twitter_thread,
    }

    for name, gen_fn in outputs.items():
        content = gen_fn(title, sections)
        (output_dir / f"{name}.md").write_text(content, encoding="utf-8")
        print(f"  OK {name}")

    print(f"  [DONE] Social media gerado para: {title}")


if __name__ == "__main__":
    main()
