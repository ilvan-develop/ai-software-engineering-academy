from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import os


class CoverBuilder:
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir

    def build_text_cover(
        self,
        title: str,
        subtitle: str = "",
        author: str = "",
        filename: str = "capa.png",
        width: int = 1200,
        height: int = 1800,
        background_color: str = "#1a1a2e",
        title_color: str = "#e94560",
        text_color: str = "#ffffff",
    ):
        img = Image.new("RGB", (width, height), background_color)
        draw = ImageDraw.Draw(img)

        try:
            font_title = ImageFont.truetype(
                "C:/Windows/Fonts/arialbd.ttf", 72
            )
            font_subtitle = ImageFont.truetype(
                "C:/Windows/Fonts/arial.ttf", 36
            )
            font_author = ImageFont.truetype(
                "C:/Windows/Fonts/arial.ttf", 28
            )
        except (IOError, OSError):
            font_title = ImageFont.load_default()
            font_subtitle = ImageFont.load_default()
            font_author = ImageFont.load_default()

        y = height // 3
        draw.text((width // 2, y), title, fill=title_color, font=font_title, anchor="mm")

        if subtitle:
            y += 80
            draw.text((width // 2, y), subtitle, fill=text_color, font=font_subtitle, anchor="mm")

        if author:
            y = height * 3 // 4
            draw.text((width // 2, y), author, fill=text_color, font=font_author, anchor="mm")

        # Gradient bar decoration
        for i in range(10):
            bar_y = height // 2 - 5 + i
            shade = int(255 * (1 - i / 10))
            draw.rectangle(
                [width // 4, bar_y, width * 3 // 4, bar_y + 1],
                fill=(233, 69, 96, shade),
            )

        output_path = self.output_dir / filename
        os.makedirs(str(self.output_dir), exist_ok=True)
        img.save(str(output_path))
        return output_path

    def build_prompt(self, title: str, style: str = "tech-minimalist") -> str:
        prompts = {
            "tech-minimalist": (
                f"Professional book cover for '{title}'. "
                "Technology theme, dark blue background, abstract circuit patterns. "
                "Minimalist design with white and cyan accents. "
                "High quality, 3D render style, no text. 1200x1800 portrait."
            ),
            "enterprise": (
                f"Executive book cover for '{title}'. "
                "Corporate style, deep navy, golden geometric accents. "
                "Abstract network nodes connecting. "
                "Professional, premium look. 1200x1800."
            ),
            "modern-tech": (
                f"Modern technology book cover for '{title}'. "
                "Gradient purple to blue background, floating geometric shapes. "
                "Futuristic, clean, no text. "
                "Glowing neon accents. 1200x1800."
            ),
        }
        return prompts.get(style, prompts["tech-minimalist"])
