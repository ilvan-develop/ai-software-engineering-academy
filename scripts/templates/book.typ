// Template Typst para livros da AI Software Engineering Academy
// Uso: typst compile --input title="..." --input author="..." book.typ output.pdf

#let primary = rgb("#1A237E")
#let accent = rgb("#00BFA5")
#let text-body = rgb("#212121")
#let text-muted = rgb("#757575")
#let surface-code = rgb("#263238")
#let text-code = rgb("#E0E0E0")

// Component: Chapter Title
#let chapter-title(number, title) = {
  pagebreak(weak: false)
  v(40mm)
  text(size: 28pt, weight: "bold", fill: primary)[#number]
  v(8pt)
  text(size: 22pt, weight: "bold", fill: primary)[#title]
  v(12pt)
  line(length: 60mm, stroke: 1.5pt + accent)
  v(16pt)
}

// Component: Section
#let section(title) = {
  v(16pt)
  text(size: 17pt, weight: "semibold", fill: primary)[#title]
  v(8pt)
}

// Component: Subsection
#let subsection(title) = {
  v(10pt)
  text(size: 14pt, weight: "semibold", fill: primary)[#title]
  v(6pt)
}

// Component: Paragraph
#let paragraph(body) = {
  text(size: 11pt, fill: text-body)[#body]
  v(8pt)
}

// Component: Code Block
#let code-block(lang, body) = {
  block(
    fill: surface-code,
    inset: 10pt,
    radius: 4pt,
    width: 100%,
    text(size: 9pt, fill: text-code, font: "Cascadia Code")[#raw(body, lang: lang)]
  )
  v(10pt)
}

// Component: Callout
#let callout(variant, body) = {
  let color = if variant == "warning" { rgb("#F57F17") }
              else if variant == "tip" { rgb("#2E7D32") }
              else if variant == "caution" { rgb("#C62828") }
              else { rgb("#1565C0") }
  block(
    stroke: (left: 4pt + color),
    inset: 10pt,
    width: 100%,
    text(size: 10.5pt, fill: text-body)[#body]
  )
  v(10pt)
}

// Component: Table
#let editorial-table(header-rows, body-rows) = {
  table(
    columns: header-rows.len(),
    inset: 8pt,
    stroke: 0.5pt + rgb("#BDBDBD"),
    fill: (x, y) => if y == 0 { primary } else { if calc.even(y) { rgb("#F5F5F5") } else { white } },
    align: (x, y) => if y == 0 { center + horizon } else { left + horizon },
    ..header-rows.map(h => text(size: 9.5pt, weight: "bold", fill: white)[#h]),
    ..body-rows.flatten().map(c => text(size: 9pt, fill: text-body)[#c])
  )
  v(10pt)
}

// Component: Figure
#let figure(src, caption) = {
  align(center)[#image(src, width: 90%)]
  v(4pt)
  align(center)[#text(size: 9pt, fill: text-muted)[#caption]]
  v(10pt)
}

// Main document setup
#let book(title, subtitle, author, body) = {
  set document(title: title, author: author)
  set page(
    paper: "a5",
    margin: (top: 18mm, bottom: 18mm, inside: 15mm, outside: 12mm),
    header: context [
      #text(size: 8pt, fill: text-muted)[
        #if here().page() > 1 { title }
      ]
    ],
    footer: context [
      #align(center)[#text(size: 8pt, fill: text-muted)[#here().page()]]
    ]
  )
  set text(font: "Georgia", size: 11pt, fill: text-body, lang: "pt")
  set heading(numbering: "1.")
  set par(leading: 1.6em, justify: true, first-line-indent: 1.5em)

  // Apply component styling globally
  show heading: it => {
    if it.level == 1 {
      chapter-title("", it.body)
    } else if it.level == 2 {
      section(it.body)
    } else if it.level == 3 {
      subsection(it.body)
    } else {
      it
    }
  }

  body
}
