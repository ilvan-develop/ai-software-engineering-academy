import type { NextPage } from "next";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";

const SearchPage: NextPage = () => {
  const router = useRouter();
  const { q } = router.query;
  const [results, setResults] = useState<any[]>([]);
  const [catalog, setCatalog] = useState<any[]>([]);

  useEffect(() => {
    fetch("/catalog.json")
      .then((r) => r.json())
      .then((data) => {
        const items = data.items || [];
        setCatalog(items);
        if (q && typeof q === "string") {
          import("fuse.js").then(({ default: Fuse }) => {
            const fuse = new Fuse(items, {
              keys: ["title", "taxonomy.topics", "id"],
              threshold: 0.4,
            });
            setResults(fuse.search(q).map((r: any) => r.item));
          });
        }
      });
  }, [q]);

  return (
    <div style={{ maxWidth: 960, margin: "0 auto", padding: "0 20px", fontFamily: "system-ui, sans-serif" }}>
      <h1>Buscar: {q}</h1>
      {results.length === 0 && <p>Nenhum resultado encontrado.</p>}
      {results.map((item: any) => (
        <div key={item.id} style={{ padding: 16, borderBottom: "1px solid #eee" }}>
          <h3>{item.title}</h3>
          <p style={{ color: "#666", fontSize: "0.9rem" }}>{item.id}</p>
          {item.taxonomy?.topics && (
            <div>
              {item.taxonomy.topics.map((t: string) => (
                <span key={t} style={{ background: "#eee", padding: "2px 8px", borderRadius: 4, marginRight: 4, fontSize: "0.8rem" }}>{t}</span>
              ))}
            </div>
          )}
        </div>
      ))}
      <p style={{ marginTop: 20 }}><a href="/">Voltar</a></p>
    </div>
  );
};

export default SearchPage;
