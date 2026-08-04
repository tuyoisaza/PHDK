#!/usr/bin/env node
// Optional build-time metadata generator.
// Writes { version, gitSha, buildTime } to src/version-generated.json (dev)
// and dist/version.json (prod). Recommendation, not a requirement.
import { readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { execSync } from "node:child_process";

const pkg = JSON.parse(readFileSync(new URL("../package.json", import.meta.url), "utf8"));

let gitSha = "unknown";
try {
  gitSha = execSync("git rev-parse --short HEAD", { encoding: "utf8" }).trim();
} catch {}

const buildTime = new Date().toISOString();
const payload = { version: pkg.version, gitSha, buildTime };

mkdirSync("src", { recursive: true });
writeFileSync("src/version-generated.json", `${JSON.stringify(payload, null, 2)}\n`);

if (existsSync("dist")) {
  writeFileSync("dist/version.json", `${JSON.stringify(payload, null, 2)}\n`);
}

console.log(`[version] generated ${payload.version} (${gitSha})`);
