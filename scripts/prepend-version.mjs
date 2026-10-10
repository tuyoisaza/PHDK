#!/usr/bin/env node
// Optional prepare-commit-msg hook: prefix with the repository's current version.
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";

const [messageFile, source] = process.argv.slice(2);
if (!messageFile) process.exit(0);
if (source === "merge" || source === "squash") process.exit(0);

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

const message = readFileSync(messageFile, "utf8").trim();
if (/^v?\d+\.\d+\.\d+\b/.test(message)) process.exit(0);

writeFileSync(messageFile, `v${version} ${message}\n`);
