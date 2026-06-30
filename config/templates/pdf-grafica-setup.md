# PDF Gráfica — Setup Manual

O formato `livro-grafica.pdf` (pronto para gráfica com sangria, marcas de corte e CMYK) requer **Pandoc + XeLaTeX**, que não puderam ser instalados automaticamente neste ambiente (rede lenta para downloads >30MB).

## Instalação

### 1. Instalar Pandoc
- Download: https://pandoc.org/installing.html
- Windows: baixar o instalador `.msi` da página de releases
- Verificar: `pandoc --version`

### 2. Instalar LaTeX (MiKTeX ou TinyTeX)
- **MiKTeX (recomendado para Windows):** https://miktex.org/download
- **TinyTeX (mais leve):** `winget install TinyTeX` ou script em https://yihui.org/tinytex/
- Verificar: `xelatex --version`

### 3. Instalar pacotes LaTeX necessários
```
geometry fontspec titling fancyhdr xcolor listings booktabs
```
No MiKTeX, os pacotes são baixados automaticamente na primeira compilação.

### 4. Template LaTeX
O template KDP está em:
```
scripts/templates/latex_kdp.tex
```

## Execução

```bash
# Via book_publisher.py (recomendado)
python scripts/book_publisher.py \
  --manifest=curriculum/books/ia-para-devs.yaml \
  --formats=pdf-print

# Ou diretamente
python scripts/build_pdf_print.py \
  --input=knowledge-factory/livros/ia-para-devs/compiled/book.md \
  --output=knowledge-factory/livros/ia-para-devs/output/livro-grafica.pdf \
  --title="IA para Desenvolvedores" \
  --author="AI Software Engineering Academy"
```
