#!/usr/bin/env python3
"""Portable, synchronous test orchestrator for PHDK-managed repositories.

This tool is NOT a sandbox or permission grant. Commands and test ownership must
be inspected under the current repository's PHDK and owner policies first.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

DEFAULT_MANIFEST = "tests/phdk-tests.json"
FORBIDDEN_TOOLS = {
    "bash", "sh", "zsh", "fish", "cmd", "cmd.exe", "powershell", "pwsh",
    "docker", "podman", "kubectl", "railway", "curl", "wget", "psql",
    "pg_restore", "pg_dump", "ssh", "scp", "rsync", "terraform", "git",
}
LOCAL_KINDS = {"static", "lint", "typecheck", "build", "security", "unit", "contract", "integration"}
UAT_KINDS = {"api", "browser", "functional", "integration", "acceptance"}
REDACTION = re.compile(
    r"(?i)(\b(?:authorization|password|passwd|token|secret|api[_-]?key)\b\s*[:=]\s*)([^\s,;]+)"
    r"|(\bBearer\s+)([A-Za-z0-9._~+/=-]+)"
)


def safe_path(root: Path, value: str) -> Path:
    path = (root / value).resolve()
    if not path.is_relative_to(root) or path == root and value not in (".", ""):
        raise ValueError(f"path escapes repository: {value}")
    return path


def redacted(value: str) -> str:
    return REDACTION.sub(lambda m: (m.group(1) or m.group(3)) + "[REDACTED]", value)


def safe_command(argv: object, profile: str) -> list[str]:
    if not isinstance(argv, list) or not argv or not all(isinstance(a, str) and a for a in argv):
        raise ValueError("argv must be a nonempty array of arguments")
    tool = Path(argv[0].replace("\\", "/")).name.casefold()
    if tool in FORBIDDEN_TOOLS:
        raise ValueError(f"forbidden command executable: {tool}")
    if profile == "local" and any(a.lower().startswith(("http://", "https://")) for a in argv):
        raise ValueError("local checks must not pass remote HTTP targets")
    return argv


def load_checks(root: Path, manifest: str) -> list[dict]:
    path = safe_path(root, manifest)
    if not path.is_file() or path.is_symlink():
        raise ValueError(f"missing test manifest: {manifest}")
    if path.stat().st_size > 128_000:
        raise ValueError("test manifest exceeds 128KB")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or not isinstance(data.get("checks"), list):
        raise ValueError("manifest needs schema_version=1 and checks[]")
    ids: set[str] = set()
    for check in data["checks"]:
        if not isinstance(check, dict):
            raise ValueError("every check must be an object")
        name = check.get("id")
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}", name):
            raise ValueError("check id must be a safe, short identifier")
        if name in ids:
            raise ValueError(f"duplicate check id: {name}")
        ids.add(name)
        profile = check.get("profile")
        if profile not in ("local", "uat"):
            raise ValueError(f"{name}: profile must be local or uat")
        kinds = LOCAL_KINDS if profile == "local" else UAT_KINDS
        if check.get("kind") not in kinds:
            raise ValueError(f"{name}: unsupported {profile} check kind")
        safe_command(check.get("argv"), profile)
        timeout = check.get("timeout_sec", 90)
        if isinstance(timeout, bool) or not isinstance(timeout, int) or not 1 <= timeout <= 600:
            raise ValueError(f"{name}: timeout_sec must be 1..600")
        cwd = safe_path(root, check.get("cwd", "."))
        if not cwd.is_dir():
            raise ValueError(f"{name}: missing working directory")
        if profile == "local" and check.get("mutates", False):
            raise ValueError(f"{name}: local test cannot mutate external/application data")
        if check.get("mutates", False):
            if profile != "uat" or not check.get("run_owned_data"):
                raise ValueError(f"{name}: UAT mutations require run_owned_data=true")
            safe_command(check.get("cleanup_argv"), "uat")
    return data["checks"]


def child_env(profile: str, run_id: str | None, target: str | None) -> dict[str, str]:
    env = os.environ.copy()
    if profile == "local":
        secret_name = re.compile(r"(?i)(token|secret|password|api.?key|credential|database_url|private_key)")
        env = {k: v for k, v in env.items() if not secret_name.search(k)}
    env["PHDK_TEST_PROFILE"] = profile
    if run_id:
        env["PHDK_UAT_RUN_ID"] = run_id
    if target:
        env["PHDK_UAT_TARGET"] = target
    env["CI"] = "1"
    return env


def run_command(argv: list[str], cwd: Path, env: dict[str, str], timeout: int) -> tuple[str, int | None, str]:
    try:
        completed = subprocess.run(
            argv, cwd=cwd, env=env, stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, errors="replace", timeout=timeout, check=False,
        )
        return ("PASS" if completed.returncode == 0 else "FAIL", completed.returncode,
                completed.stdout or "")
    except subprocess.TimeoutExpired as exc:
        out = exc.stdout or b""
        if isinstance(out, bytes):
            out = out.decode("utf-8", errors="replace")
        return "FAIL", None, out + f"\nTIMEOUT after {timeout}s"
    except (OSError, ValueError) as exc:
        return "BLOCKED", None, f"Unable to start executable: {exc}"


def git_sha(root: Path) -> str | None:
    try:
        r = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root,
                           capture_output=True, text=True, timeout=3, check=False)
        sha = r.stdout.strip()
        return sha if r.returncode == 0 and re.fullmatch(r"[0-9a-f]{40}", sha) else None
    except (OSError, subprocess.TimeoutExpired):
        return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="PHDK bounded test runner")
    parser.add_argument("--root", default=".")
    parser.add_argument("--manifest", default=DEFAULT_MANIFEST)
    parser.add_argument("--profile", choices=("local", "uat"), default="local")
    parser.add_argument("--max-seconds", type=int, default=300)
    parser.add_argument("--output-dir", default=".phdk-test-results")
    parser.add_argument("--validate", action="store_true", help="inspect manifest without executing checks")
    parser.add_argument("--continue-on-failure", action="store_true")
    parser.add_argument("--uat-authorized", action="store_true", help="assert a current explicit PHDK uat mandate")
    parser.add_argument("--uat-run-id")
    parser.add_argument("--uat-target", help="existing production HTTPS target, never staging")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    if not root.is_dir() or not 1 <= args.max_seconds <= 3600:
        parser.error("root must exist and max-seconds must be within 1..3600")
    if args.profile == "uat" and not args.validate:
        target = urlparse(args.uat_target or "")
        if (not args.uat_authorized or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{5,95}", args.uat_run_id or "")
                or target.scheme != "https" or not target.hostname or target.username or target.password):
            parser.error("UAT requires explicit owner mandate, unique run ID and production HTTPS target")
        if target.hostname in ("localhost", "127.0.0.1"):
            parser.error("UAT cannot target localhost")
    try:
        checks = load_checks(root, args.manifest)
        selected = [c for c in checks if c["profile"] == args.profile]
        safe_path(root, args.output_dir)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"BLOCKED: {exc}", file=sys.stderr)
        return 2
    if not selected:
        print(f"BLOCKED: no {args.profile} checks declared; do not claim PASS", file=sys.stderr)
        return 2
    if args.validate:
        print(f"VALID: {len(selected)} {args.profile} checks configured; NOT RUN")
        return 0

    started = time.monotonic()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report_dir = safe_path(root, args.output_dir) / f"{stamp}-{args.profile}-{os.getpid()}"
    report_dir.mkdir(parents=True, exist_ok=False)
    results: list[dict] = []
    env = child_env(args.profile, args.uat_run_id, args.uat_target)
    stop = False
    for check in selected:
        item = {"id": check["id"], "kind": check["kind"], "status": "NOT_RUN", "seconds": 0.0}
        if stop:
            item["reason"] = "earlier failure or execution budget exhausted"
            results.append(item)
            continue
        remaining = args.max_seconds - (time.monotonic() - started)
        if remaining <= 0:
            item["reason"] = "run-wide time budget exhausted"
            results.append(item)
            stop = True
            continue
        cwd = safe_path(root, check.get("cwd", "."))
        timeout = min(check.get("timeout_sec", 90), max(1, int(remaining)))
        tick = time.monotonic()
        status, exit_code, output = run_command(check["argv"], cwd, env, timeout)
        log_lines = [output]
        if check.get("mutates", False):
            cleanup_status, cleanup_rc, cleanup_output = run_command(
                check["cleanup_argv"], cwd, env, min(60, max(1, int(args.max_seconds - (time.monotonic() - started)))))
            log_lines += ["\n--- CLEANUP ---\n", cleanup_output]
            item["cleanup_status"] = cleanup_status
            item["cleanup_exit_code"] = cleanup_rc
            if cleanup_status != "PASS":
                status = "FAIL"
                item["reason"] = "run-owned fixture cleanup not confirmed; manual incident review required"
        item.update(status=status, exit_code=exit_code, seconds=round(time.monotonic() - tick, 2))
        log_text = redacted("".join(log_lines))[-96_000:]
        logfile = report_dir / f"{check['id']}.log"
        logfile.write_text(log_text, encoding="utf-8")
        item["log"] = logfile.name
        results.append(item)
        if status != "PASS" and not args.continue_on_failure:
            stop = True
    totals = {key: sum(r["status"] == key for r in results)
              for key in ("PASS", "FAIL", "BLOCKED", "NOT_RUN")}
    status = "FAIL" if totals["FAIL"] else "BLOCKED" if totals["BLOCKED"] else "NOT_RUN" if totals["NOT_RUN"] else "PASS"
    report = {
        "schema_version": 1, "profile": args.profile, "status": status,
        "observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_sha": git_sha(root), "uat_run_id": args.uat_run_id if args.profile == "uat" else None,
        "uat_target": args.uat_target if args.profile == "uat" else None,
        "seconds": round(time.monotonic() - started, 2), "counts": totals,
        "excluded_other_profile": len(checks) - len(selected), "checks": results,
        "limits": "Commands are project-owned; runner is not a sandbox or UAT authorization proof.",
    }
    (report_dir / "report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md = [f"# PHDK test result: {status}", "", f"Profile: {args.profile}",
          f"Git SHA: {report['git_sha'] or 'UNVERIFIED'}", f"Duration: {report['seconds']}s", "",
          "| Check | Result | Seconds | Evidence |", "|---|---|---:|---|"]
    md += [f"| {r['id']} | {r['status']} | {r['seconds']} | {r.get('log', r.get('reason', '-'))} |" for r in results]
    (report_dir / "report.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{status}: {totals['PASS']}/{len(results)} passed, {report['seconds']}s; report={report_dir / 'report.json'}")
    if status != "PASS":
        for result in results:
            if result["status"] != "PASS":
                print(f"  {result['id']}: {result['status']} ({result.get('reason', result.get('log', 'no log'))})")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
