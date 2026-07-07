import type { NextPage } from "next";
import type { GetStaticProps } from "next/types";
import fs from "fs";
import path from "path";

import {
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Radar,
  Legend,
  Tooltip,
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
} from "recharts";

interface CategoryInfo {
  name: string;
  score: number;
  weight: number;
}

interface Target {
  target_id: string;
  type: string;
  title: string;
  overall: number;
  min_score: number;
  passed: boolean;
  categories: Record<string, CategoryInfo>;
}

interface Props {
  timestamp: string;
  modules: Target[];
  books: Target[];
  categoryIds: string[];
  categoryLabels: Record<string, string>;
}

export const getStaticProps: GetStaticProps<Props> = async () => {
  const jsonPath = path.join(process.cwd(), "public", "bqs-data.json");
  if (!fs.existsSync(jsonPath)) {
    return { props: { timestamp: "", modules: [], books: [], categoryIds: [], categoryLabels: {} } };
  }
  const raw = JSON.parse(fs.readFileSync(jsonPath, "utf-8"));
  const allTargets: Target[] = raw.targets || [];
  const modules = allTargets.filter((t: Target) => t.type === "module");
  const books = allTargets.filter((t: Target) => t.type === "book");

  const categoryIds = modules.length > 0 ? Object.keys(modules[0].categories) : [];
  const categoryLabels: Record<string, string> = {};
  if (modules.length > 0) {
    for (const [id, info] of Object.entries(modules[0].categories)) {
      categoryLabels[id] = info.name;
    }
  }

  return { props: { timestamp: raw.timestamp || "", modules, books, categoryIds, categoryLabels } };
};

const MIN_SCORE = 95;

const RadarCard: React.FC<{ target: Target; catIds: string[]; labels: Record<string, string> }> = ({
  target,
  catIds,
  labels,
}) => {
  const data = catIds.map((id) => ({
    category: labels[id] || id,
    score: target.categories[id]?.score ?? 0,
    fullMark: 100,
  }));

  return (
    <div
      style={{
        border: "1px solid #ddd",
        borderRadius: 8,
        padding: 16,
        background: target.passed ? "#f0fdf4" : "#fff",
      }}
    >
      <h3 style={{ margin: "0 0 4px", fontSize: "1rem" }}>
        {target.title || target.target_id}
      </h3>
      <p style={{ margin: "0 0 8px", fontSize: "0.85rem", color: "#666" }}>
        Overall: <strong>{target.overall}</strong> | Min:{" "}
        <span style={{ color: target.min_score >= MIN_SCORE ? "green" : "red" }}>
          {target.min_score}
        </span>{" "}
        | {target.passed ? "✅" : "❌"}
      </p>
      <ResponsiveContainer width="100%" height={280}>
        <RadarChart data={data}>
          <PolarGrid />
          <PolarAngleAxis dataKey="category" fontSize={10} />
          <PolarRadiusAxis angle={30} domain={[0, 100]} fontSize={10} />
          <Radar dataKey="score" stroke="#e94560" fill="#e94560" fillOpacity={0.3} />
          <Tooltip />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
};

const BQSPage: NextPage<Props> = ({ timestamp, modules, books, categoryIds, categoryLabels }) => {
  const sortedModules = [...modules].sort((a, b) => a.overall - b.overall);
  const barData = sortedModules.map((m) => ({
    name: m.target_id.split("/").pop() || m.target_id,
    overall: m.overall,
    min: m.min_score,
  }));

  const avgPerCategory = categoryIds.map((id) => {
    const scores = modules.map((m) => m.categories[id]?.score ?? 0);
    const avg = scores.reduce((a, b) => a + b, 0) / scores.length;
    return { category: categoryLabels[id] || id, score: Math.round(avg * 10) / 10 };
  });

  return (
    <div
      style={{
        maxWidth: 1200,
        margin: "0 auto",
        padding: "40px 20px",
        fontFamily: "system-ui, -apple-system, sans-serif",
        color: "#1a1a2e",
      }}
    >
      <header style={{ marginBottom: 32 }}>
        <h1 style={{ fontSize: "2rem", margin: 0 }}>BQS Dashboard</h1>
        <p style={{ color: "#666", margin: "4px 0 0" }}>
          Book Quality Standard — Última execução: {timestamp || "N/A"} | Mínimo por categoria:{" "}
          {MIN_SCORE}
        </p>
        <a href="/" style={{ fontSize: "0.9rem" }}>
          ← Voltar
        </a>
      </header>

      <section style={{ marginBottom: 40 }}>
        <h2>Média por Categoria (todos os módulos)</h2>
        <p style={{ fontSize: "0.85rem", color: "#666" }}>
          Scores médios de cada categoria BQS nos {modules.length} módulos
        </p>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={avgPerCategory}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="category" fontSize={10} angle={-30} textAnchor="end" height={80} />
            <YAxis domain={[0, 100]} />
            <Tooltip />
            <Bar dataKey="score" fill="#1a1a2e" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </section>

      <section style={{ marginBottom: 40 }}>
        <h2>Overview por Módulo</h2>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart data={barData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" fontSize={10} angle={-45} textAnchor="end" height={100} />
            <YAxis domain={[0, 100]} />
            <Tooltip />
            <Bar dataKey="overall" fill="#e94560" name="Overall" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </section>

      <section style={{ marginBottom: 40 }}>
        <h2>Radar por Módulo</h2>
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill, minmax(350px, 1fr))",
            gap: 20,
          }}
        >
          {sortedModules.map((m) => (
            <RadarCard key={m.target_id} target={m} catIds={categoryIds} labels={categoryLabels} />
          ))}
        </div>
      </section>

      {books.length > 0 && (
        <section>
          <h2>Radar por Livro</h2>
          <div
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(auto-fill, minmax(350px, 1fr))",
              gap: 20,
            }}
          >
            {books.map((b) => (
              <RadarCard key={b.target_id} target={b} catIds={categoryIds} labels={categoryLabels} />
            ))}
          </div>
        </section>
      )}

      <footer style={{ textAlign: "center", padding: "40px 0", color: "#888", fontSize: "0.85rem" }}>
        AI Software Engineering Academy © 2026 — BQS v2.0
      </footer>
    </div>
  );
};

export default BQSPage;
