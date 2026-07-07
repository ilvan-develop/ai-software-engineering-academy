#!/usr/bin/env node
/**
 * prebuild.js — gera catalog.json para o site estatico
 * Copia catalog.yaml como JSON para web/public/
 */
const fs = require("fs");
const path = require("path");
const yaml = require("js-yaml");

const root = path.resolve(__dirname, "..");
const catalogYaml = path.join(root, "knowledge-factory", "registry", "catalog.yaml");
const catalogJson = path.join(root, "web", "public", "catalog.json");

if (!fs.existsSync(catalogYaml)) {
  console.warn("catalog.yaml nao encontrado. Pulando geracao.");
  process.exit(0);
}

const doc = yaml.load(fs.readFileSync(catalogYaml, "utf8"));
// Simplify: keep only what the frontend needs
const simplified = {
  version: doc.version,
  items: doc.items.map((item) => ({
    id: item.id,
    type: item.type,
    title: item.title,
    taxonomy: item.taxonomy,
  })),
};

fs.writeFileSync(catalogJson, JSON.stringify(simplified, null, 2), "utf8");
console.log(`catalog.json gerado com ${simplified.items.length} items.`);
