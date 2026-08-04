#!/usr/bin/env node
// Optional prepare-commit-msg hook: prefix the commit message with the current version.
// Recommendation, not a requirement. Skip or adapt if it does not fit the project.
import { readFileSync, writeFileSync } from "node:fs";

const [messageFile, source] = process.argv.slice(2);
if (!messageFile) process.exit(0);
if (source === "merge" || source === "squash") process.exit(0);

const pkg = JSON.parse(readFileSync(new URL("../package.json", import.meta.url), "utf8"));
const version = pkg.version;

const message = readFileSync(messageFile, "utf8").trim();
if (/^v?\d+\.\d+\.\d+\b/.test(message)) process.exit(0);

writeFileSync(messageFile, `v${version} ${message}\n`);
process.exit(0);
