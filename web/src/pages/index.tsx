import type { NextPage } from "next";

const Home: NextPage = () => {
  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <h1 style={styles.title}>AI Software Engineering Academy</h1>
        <p style={styles.subtitle}>Conhecimento enterprise em engenharia de software com IA</p>
      </header>

      <section style={styles.section}>
        <h2>Nossos Livros</h2>
        <p style={styles.text}>
          Exploramos tópicos de engenharia de software, arquitetura enterprise,
          design de produtos e inteligência artificial aplicada.
        </p>
        <div style={styles.cardGrid}>
          {BOOKS.map((book) => (
            <a key={book.id} href={`/books/${book.id}`} style={styles.card}>
              <h3>{book.title}</h3>
              <p>{book.description}</p>
              <span style={styles.badge}>{book.chapters} capítulos</span>
            </a>
          ))}
        </div>
      </section>

      <section style={styles.section}>
        <h2>Cursos</h2>
        <div style={styles.cardGrid}>
          {COURSES.map((course) => (
            <div key={course.id} style={styles.card}>
              <h3>{course.name}</h3>
              <p>{course.description}</p>
              <span style={styles.badge}>{course.modules} módulos</span>
            </div>
          ))}
        </div>
      </section>

      <section style={styles.section}>
        <h2>Buscar Conteúdo</h2>
        <form action="/search" method="get" style={styles.searchForm}>
          <input
            type="text"
            name="q"
            placeholder="Pesquise por tópicos, tecnologias, conceitos..."
            style={styles.searchInput}
          />
          <button type="submit" style={styles.searchButton}>Buscar</button>
        </form>
      </section>

      <section style={styles.section}>
        <h2>Newsletter</h2>
        <p>Receba atualizações sobre novos conteúdos e lançamentos.</p>
        <form
          action="/api/newsletter"
          method="post"
          style={styles.searchForm}
        >
          <input
            type="email"
            name="email"
            placeholder="seu@email.com"
            required
            style={styles.searchInput}
          />
          <button type="submit" style={styles.searchButton}>Assinar</button>
        </form>
      </section>

      <footer style={styles.footer}>
        <p>AI Software Engineering Academy &copy; {new Date().getFullYear()}</p>
        <p style={styles.footerLinks}>
          <a href="/about">Sobre</a>
        </p>
      </footer>
    </div>
  );
};

const BOOKS = [
  { id: "formacao-completa", title: "Arquitetura de Software Enterprise com IA", description: "Formação completa do arquiteto enterprise moderno.", chapters: 26 },
  { id: "backend-architecture", title: "Arquitetura Backend Enterprise", description: "Padrões e práticas para sistemas backend escaláveis.", chapters: 8 },
  { id: "product-design-book", title: "Product Design Engineering", description: "Design de produtos digitais com visão enterprise.", chapters: 6 },
  { id: "ia-para-devs", title: "IA para Desenvolvedores", description: "Inteligência artificial aplicada ao ciclo de desenvolvimento.", chapters: 3 },
];

const COURSES = [
  { id: "fundamentos-enterprise", name: "Fundamentos Enterprise", description: "Base para arquitetos de software.", modules: 3 },
  { id: "product-design", name: "Product Design", description: "Design de produtos e UX.", modules: 6 },
  { id: "arquitetura-backend", name: "Arquitetura Backend", description: "Sistemas backend escaláveis.", modules: 8 },
  { id: "frontend-devops", name: "Frontend & DevOps", description: "Desenvolvimento frontend e infraestrutura.", modules: 4 },
  { id: "governanca-automacao", name: "Governança & Automação", description: "Governança de software e IA.", modules: 4 },
  { id: "capstone", name: "Projeto Final", description: "Construindo um SaaS Enterprise.", modules: 1 },
];

const styles: Record<string, React.CSSProperties> = {
  container: {
    maxWidth: 960,
    margin: "0 auto",
    padding: "0 20px",
    fontFamily: "system-ui, -apple-system, sans-serif",
    color: "#1a1a2e",
  },
  header: {
    textAlign: "center" as const,
    padding: "60px 0 40px",
    borderBottom: "2px solid #e94560",
  },
  title: { fontSize: "2.5rem", margin: 0, color: "#1a1a2e" },
  subtitle: { fontSize: "1.2rem", color: "#666", marginTop: 8 },
  section: { padding: "40px 0", borderBottom: "1px solid #eee" },
  text: { color: "#444", lineHeight: 1.6 },
  cardGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fill, minmax(280px, 1fr))",
    gap: 20,
    marginTop: 20,
  },
  card: {
    padding: 20,
    border: "1px solid #ddd",
    borderRadius: 8,
    textDecoration: "none",
    color: "inherit",
    transition: "box-shadow 0.2s",
    cursor: "pointer",
    display: "block",
  },
  badge: {
    display: "inline-block",
    padding: "4px 8px",
    background: "#e94560",
    color: "#fff",
    borderRadius: 4,
    fontSize: "0.8rem",
    marginTop: 8,
  },
  searchForm: { display: "flex", gap: 8, marginTop: 12 },
  searchInput: {
    flex: 1,
    padding: "10px 16px",
    border: "1px solid #ddd",
    borderRadius: 6,
    fontSize: "1rem",
  },
  searchButton: {
    padding: "10px 24px",
    background: "#1a1a2e",
    color: "#fff",
    border: "none",
    borderRadius: 6,
    cursor: "pointer",
    fontSize: "1rem",
  },
  footer: {
    textAlign: "center" as const,
    padding: "40px 0",
    color: "#888",
    fontSize: "0.9rem",
  },
  footerLinks: { marginTop: 8 },
};

export default Home;
