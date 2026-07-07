import type { NextPage } from "next";

const About: NextPage = () => (
  <div style={{ maxWidth: 720, margin: "0 auto", padding: "40px 20px", fontFamily: "system-ui, sans-serif", color: "#333", lineHeight: 1.8 }}>
    <h1>Sobre a AI Software Engineering Academy</h1>

    <p>
      Somos uma editora técnica nativa em IA. Produzimos conteúdo de engenharia de software
      enterprise usando um pipeline editorial composto por 42 agentes de IA especializados,
      orquestrados em 5 departamentos: Conteúdo, Editorial, Design, Publicação e QA.
    </p>

    <h2>Missão</h2>
    <p>
      Transformar conhecimento técnico em produtos educacionais de qualidade enterprise —
      livros, cursos, workshops, newsletters — com velocidade e consistência que editoras
      tradicionais não conseguem alcançar.
    </p>

    <h2>Como Funciona</h2>
    <ol>
      <li><strong>Escrita:</strong> Agentes de conteúdo produzem o material técnico com progressão pedagógica</li>
      <li><strong>Revisão:</strong> Agentes editoriais garantem clareza, consistência e aderência ao guia de estilo</li>
      <li><strong>Design:</strong> Agentes de design criam layout, diagramas e identidade visual</li>
      <li><strong>Publicação:</strong> Agentes convertem para DOCX, EPUB, PDF</li>
      <li><strong>QA:</strong> Agentes auditam qualidade contra o Book Quality Standard (BQS)</li>
    </ol>

    <h2>Nossos Números</h2>
    <ul>
      <li>42 agentes de IA especializados</li>
      <li>26 módulos de conteúdo</li>
      <li>4 livros publicados</li>
      <li>6 cursos na trilha enterprise</li>
      <li>5 departamentos editoriais</li>
    </ul>

    <p style={{ marginTop: 40 }}><a href="/">Voltar para página inicial</a></p>
  </div>
);

export default About;
