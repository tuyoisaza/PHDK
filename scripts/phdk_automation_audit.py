#!/usr/bin/env python3
"""Read-only static evidence for PHDK Check's automation/cost hygiene gate.

This tool never reads provider secrets or asserts that a workflow is enabled.
The live GitHub/Railway metadata inspection remains mandatory when applicable.
"""

import argparse
import json
import os
import re
from pathlib import Path

SKIP = {
    ".git",
    "node_modules",
    ".next",
    "dist",
    "build",
    "coverage",
    ".venv",
    "venv",
    "__pycache__",
    "phdk-standards",
    ".turbo",
}
MAX_BYTES = 512 * 1024
WATCH = re.compile(
    r"\b(?:nodemon|ts-node-dev|pm2\b[^\n]*--watch|webpack\b[^\n]*--watch)\b", re.I
)
SCHEDULE = re.compile(r"(?m)^\s*schedule\s*:")
PHDK = re.compile(
    r"\bphdk(?:[-_\s]+(?:auto|agent|bot|sync|update|workflow|maintenance))?\b", re.I
)


def finding(code, severity, path, line, message):
    return {
        "code": code,
        "severity": severity,
        "path": path,
        "line": line,
        "message": message,
    }


def line_at(content, needle):
    pos = content.find(needle)
    return content.count("\n", 0, max(pos, 0)) + 1


def iter_files(root):
    for base, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP)
        for filename in sorted(files):
            path = Path(base) / filename
            rel = path.relative_to(root).as_posix()
            if (
                (
                    rel.startswith(".github/workflows/")
                    and path.suffix in {".yml", ".yaml"}
                )
                or (
                    rel.startswith(".github/agents/")
                    and path.suffix in {".md", ".yaml", ".yml", ".json"}
                )
                or filename
                in {
                    "dependabot.yml",
                    "dependabot.yaml",
                    "renovate.json",
                    "renovate.json5",
                    ".renovaterc",
                    ".renovaterc.json",
                    "railway.json",
                    "railway.toml",
                    "package.json",
                    "Procfile",
                }
                or (
                    filename.startswith("railway.")
                    and path.suffix in {".toml", ".json"}
                )
            ):
                try:
                    if path.stat().st_size <= MAX_BYTES:
                        yield path, rel
                except OSError:
                    continue


def railway_values(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key in {"cronSchedule", "restartPolicyType", "restartPolicyMaxRetries"}:
                yield key, value
            yield from railway_values(value)
    elif isinstance(data, list):
        for value in data:
            yield from railway_values(value)


def scan(root):
    root = Path(root).resolve()
    issues = []
    if not root.is_dir():
        raise ValueError(f"Not a directory: {root}")
    for path, rel in iter_files(root):
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            continue
        if rel.startswith(".github/workflows/"):
            issues.append(
                finding(
                    "WORKFLOW_REVIEW",
                    "REVIEW_REMOTE",
                    rel,
                    1,
                    "Check GitHub enabled state, events, required checks and run history",
                )
            )
            match = SCHEDULE.search(content)
            if match:
                issues.append(
                    finding(
                        "SCHEDULED_ACTION",
                        "HIGH",
                        rel,
                        line_at(content, match.group(0)),
                        "Scheduled GitHub Action: establish owner, use and cost",
                    )
                )
            if PHDK.search(content):
                issues.append(
                    finding(
                        "PHDK_WORKFLOW",
                        "HIGH",
                        rel,
                        line_at(content, PHDK.search(content).group(0)),
                        "Workflow references PHDK: verify this is not a legacy PHDK runner",
                    )
                )
            if re.search(r"\b(workflow_run|repository_dispatch)\s*:", content):
                m = re.search(r"\b(workflow_run|repository_dispatch)\s*:", content)
                issues.append(
                    finding(
                        "CHAINED_ACTION",
                        "REVIEW_REMOTE",
                        rel,
                        line_at(content, m.group(0)),
                        "Review chained/remote dispatches for loops and ownership",
                    )
                )
        elif rel.startswith(".github/agents/"):
            issues.append(
                finding(
                    "AGENT_CONFIG",
                    "REVIEW_REMOTE",
                    rel,
                    1,
                    "Agent configuration alone is not proof of execution; verify remote runs",
                )
            )
        elif path.name.startswith(("renovate.", ".renovaterc")) or (
            rel.startswith(".github/") and path.name.startswith("dependabot.")
        ):
            issues.append(
                finding(
                    "DEPENDENCY_BOT",
                    "REVIEW_REMOTE",
                    rel,
                    1,
                    "Verify bot app or update PR activity and owner",
                )
            )
        elif path.name.startswith("railway.") and path.suffix == ".json":
            try:
                data = json.loads(content)
            except json.JSONDecodeError:
                issues.append(
                    finding(
                        "RAILWAY_PARSE",
                        "REVIEW_REMOTE",
                        rel,
                        1,
                        "Could not parse Railway JSON; inspect manually",
                    )
                )
                continue
            vals = list(railway_values(data))
            for key, value in vals:
                if key == "cronSchedule" and value:
                    issues.append(
                        finding(
                            "RAILWAY_CRON",
                            "HIGH",
                            rel,
                            line_at(content, '"cronSchedule"'),
                            "Railway scheduled execution: prove product requirement",
                        )
                    )
                if key == "restartPolicyType" and str(value).upper() == "ALWAYS":
                    issues.append(
                        finding(
                            "RAILWAY_RESTART",
                            "REVIEW_REMOTE",
                            rel,
                            line_at(content, '"restartPolicyType"'),
                            "ALWAYS restart policy: inspect crashes, retry bounds and usage",
                        )
                    )
        elif path.name.startswith("railway.") and path.suffix == ".toml":
            for line, value in enumerate(content.splitlines(), 1):
                if re.search(r"^\s*cronSchedule\s*=\s*['\"][^'\"]+", value):
                    issues.append(
                        finding(
                            "RAILWAY_CRON",
                            "HIGH",
                            rel,
                            line,
                            "Railway scheduled execution: prove product requirement",
                        )
                    )
                if re.search(
                    r"^\s*restartPolicyType\s*=\s*['\"]ALWAYS['\"]", value, re.I
                ):
                    issues.append(
                        finding(
                            "RAILWAY_RESTART",
                            "REVIEW_REMOTE",
                            rel,
                            line,
                            "ALWAYS restart policy: inspect crashes and retry bounds",
                        )
                    )
        elif path.name == "package.json":
            try:
                scripts = json.loads(content).get("scripts", {})
            except (json.JSONDecodeError, AttributeError):
                continue
            if isinstance(scripts, dict):
                for name in (
                    "start",
                    "serve",
                    "production",
                    "deploy",
                    "worker",
                    "postinstall",
                ):
                    cmd = scripts.get(name)
                    if isinstance(cmd, str) and WATCH.search(cmd):
                        issues.append(
                            finding(
                                "PRODUCTION_WATCH",
                                "HIGH",
                                rel,
                                line_at(content, f'"{name}"'),
                                f"Potential persistent watcher in {name} command",
                            )
                        )
        elif path.name == "Procfile":
            for line, value in enumerate(content.splitlines(), 1):
                if WATCH.search(value):
                    issues.append(
                        finding(
                            "PRODUCTION_WATCH",
                            "HIGH",
                            rel,
                            line,
                            "Potential persistent watcher in Procfile",
                        )
                    )
    return {
        "root": str(root),
        "remote_state": "UNVERIFIED",
        "remote_requirements": [
            "GitHub workflow state/runs/checks/bots",
            "Railway triggers/Wait for CI/cron/restarts/usage if connected",
        ],
        "findings": issues,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=".")
    ap.add_argument("--format", choices=("json", "text"), default="text")
    ap.add_argument(
        "--strict",
        action="store_true",
        help="exit 2 when HIGH-risk source signals exist (not a provider-state check)",
    )
    args = ap.parse_args()
    try:
        report = scan(args.root)
    except ValueError as exc:
        ap.error(str(exc))
    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print("PHDK automation static audit — remote state UNVERIFIED")
        for issue in report["findings"]:
            print(
                f"{issue['severity']}: {issue['path']}:{issue['line']} "
                f"[{issue['code']}] {issue['message']}"
            )
        print(
            "Next: inspect GitHub and Railway provider metadata without modifications."
        )
    if args.strict and any(x["severity"] == "HIGH" for x in report["findings"]):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
