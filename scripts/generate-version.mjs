#!/usr/bin/env node
// Optional build-time metadata generator.
// Uses package.json when present, otherwise VERSION.
// Writes only to existing application output roots; it does not scaffold src/dist.
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { execSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const pkgPath = resolve(root, "package.json");
const versionPath = resolve(root, "VERSION");

let version;
if (existsSync(pkgPath)) {
  version = JSON.parse(readFileSync(pkgPath, "utf8")).version;
} else if (existsSync(versionPath)) {
  version = readFileSync(versionPath, "utf8").trim();
} else {
  console.error("[version] no package.json or VERSION source found");
  process.exit(1);
}

let gitSha = "unknown";
try {
  gitSha = execSync("git rev-parse --short HEAD", { cwd: root, encoding: "utf8" }).trim();
} catch {}

const payload = { version, gitSha, buildTime: new Date().toISOString() };
const srcPath = resolve(root, "src");
const distPath = resolve(root, "dist");

if (existsSync(srcPath)) {
  writeFileSync(resolve(srcPath, "version-generated.json"), `${JSON.stringify(payload, null, 2)}\n`);
}
if (existsSync(distPath)) {
  writeFileSync(resolve(distPath, "version.json"), `${JSON.stringify(payload, null, 2)}\n`);
}

console.log(`[version] ${payload.version} (${gitSha})`);
