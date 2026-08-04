#!/usr/bin/env node
// Optional pre-commit hook: auto-increment the patch version in package.json.
// Recommendation, not a requirement. Skip or adapt if it does not fit the project.
import { readFileSync, writeFileSync } from "node:fs";
import { execSync } from "node:child_process";

const pkgUrl = new URL("../package.json", import.meta.url);
const pkg = JSON.parse(readFileSync(pkgUrl, "utf8"));

const [major, minor, patch] = pkg.version.split(".").map((n) => Number(n) || 0);
const oldVersion = pkg.version;
const newVersion = `${major}.${minor}.${patch + 1}`;

pkg.version = newVersion;
writeFileSync(pkgUrl, `${JSON.stringify(pkg, null, 2)}\n`);

execSync("git add package.json", { stdio: "inherit" });
console.log(`[version] bumped ${oldVersion} -> ${newVersion}`);
process.exit(0);
