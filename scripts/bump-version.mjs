#!/usr/bin/env node
// Optional pre-commit version bump.
// Uses package.json for application repos and VERSION for the PHDK standards repo.
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { execSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const pkgPath = resolve(root, "package.json");
const versionPath = resolve(root, "VERSION");

let oldVersion;
let writeVersion;

if (existsSync(pkgPath)) {
  const pkg = JSON.parse(readFileSync(pkgPath, "utf8"));
  oldVersion = pkg.version;
  writeVersion = (next) => {
    pkg.version = next;
    writeFileSync(pkgPath, `${JSON.stringify(pkg, null, 2)}\n`);
    execSync("git add package.json", { cwd: root, stdio: "inherit" });
  };
} else if (existsSync(versionPath)) {
  oldVersion = readFileSync(versionPath, "utf8").trim();
  writeVersion = (next) => {
    writeFileSync(versionPath, `${next}\n`);
    execSync("git add VERSION", { cwd: root, stdio: "inherit" });
  };
} else {
  console.error("[version] no package.json or VERSION source found");
  process.exit(1);
}

const parts = oldVersion.split(".").map((n) => Number(n));
if (parts.length !== 3 || parts.some((n) => !Number.isInteger(n) || n < 0)) {
  console.error(`[version] invalid semantic version: ${oldVersion}`);
  process.exit(1);
}

const [major, minor, patch] = parts;
const newVersion = `${major}.${minor}.${patch + 1}`;
writeVersion(newVersion);

console.log(`[version] bumped ${oldVersion} -> ${newVersion}`);
