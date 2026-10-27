#!/usr/bin/env python3
"""Audited historical and per-milestone Git branch cleanup.

Requires recent, independently obtained GitHub PR evidence for every deletion.
Default inventory never writes. Apply never discards unknown local content.
"""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

SHA = re.compile(r"^[0-9a-fA-F]{40}$")
SAFE_BRANCH = re.compile(r"^(?!-)[A-Za-z0-9][A-Za-z0-9_./-]*$")
REPO = re.compile(r"github\.com[:/]([^/:]+)/([^/]+?)(?:\.git)?/?$")
MAX_AGE_MINUTES = 30
PROTECTED = {"main", "master", "develop", "development", "staging", "production"}

def git(*args, cwd=None, required=True):
    cmd = ["git", *(["-C", str(cwd)] if cwd else []), *args]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=45)
    if required and proc.returncode:
        raise RuntimeError("Git command failed: " + " ".join(cmd[:3]) + " :: " +
                           (proc.stderr.strip() or proc.stdout.strip())[-700:])
    return proc.stdout.strip()

def rev(repo, ref):
    return git("rev-parse", "--verify", ref, cwd=repo, required=False)

def ancestor(repo, older, newer):
    return subprocess.run(["git", "-C", str(repo), "merge-base",
                           "--is-ancestor", older, newer],
                          capture_output=True, timeout=45).returncode == 0

def remote_head(repo, remote, branch):
    output = git("ls-remote", "--heads", remote, "refs/heads/" + branch, cwd=repo)
    matches = [line.split() for line in output.splitlines() if line.strip()]
    if not matches:
        return None
    if len(matches) != 1 or matches[0][1] != "refs/heads/" + branch:
        raise RuntimeError("ambiguous remote branch ref")
    return matches[0][0]

def iso(value):
    if not isinstance(value, str):
        raise ValueError("missing ISO 8601 timestamp")
    parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timezone is required")
    return parsed.astimezone(dt.timezone.utc)

def branch_valid(repo, branch, target):
    if not isinstance(branch, str) or branch in PROTECTED or branch == target or not SAFE_BRANCH.fullmatch(branch):
        return False
    return subprocess.run(["git", "-C", str(repo), "check-ref-format", "--branch", branch],
                          capture_output=True, timeout=45).returncode == 0

def repo_identity(repo, remote):
    url = git("remote", "get-url", remote, cwd=repo)
    found = REPO.search(url)
    if not found:
        raise RuntimeError("cannot verify GitHub repository identity")
    return found.group(1).lower() + "/" + found.group(2).lower()

def inventory(repo, remote, target):
    branches = git("for-each-ref", "--format=%(refname:short)%09%(objectname)",
                   "refs/heads", cwd=repo).splitlines()
    worktrees = git("worktree", "list", "--porcelain", cwd=repo).splitlines()
    remote_refs = git("ls-remote", "--heads", remote, cwd=repo).splitlines()
    remote_branches = []
    for line in remote_refs:
        items = line.split()
        if len(items) != 2 or not items[1].startswith("refs/heads/"):
            continue
        branch = items[1][len("refs/heads/"):]
        if branch_valid(repo, branch, target):
            remote_branches.append({"branch": branch, "sha": items[0]})
    names = []
    for record in branches:
        if not record.strip():
            continue
        branch, head = record.split("\t", 1)
        if not branch_valid(repo, branch, target):
            continue
        names.append({"branch": branch, "local_sha": head,
                      "ancestor_of_local_main": bool(rev(repo, "refs/heads/" + target) and
                                                     ancestor(repo, head, "refs/heads/" + target)),
                      "verified_merged_pr": "NOT_CHECKED"})
    return {"mode": "INVENTORY_READ_ONLY", "repo": repo_identity(repo, remote),
            "target": target, "local_main_sha": rev(repo, "refs/heads/" + target) or None,
            "local_branches": names, "worktree_lines": worktrees,
            "remote_branch_heads": remote_branches,
            "remote_branch_count": len(remote_refs), "remote_snapshot": "LIVE_LS_REMOTE",
            "next_step": "Fetch recent merged/open PR metadata for exact candidates; no deletions by ancestry alone"}

def validate_proof(repo, remote, target, entry, reported_repo, now, historical):
    branch = entry.get("branch")
    if not branch_valid(repo, branch, target):
        return "INVALID_OR_PROTECTED_BRANCH"
    head_sha, merged_sha = entry.get("head_sha"), entry.get("merge_sha")
    if not (isinstance(head_sha, str) and SHA.fullmatch(head_sha) and
            isinstance(merged_sha, str) and SHA.fullmatch(merged_sha)):
        return "MISSING_FULL_SHA"
    if (entry.get("merged") is not True or entry.get("state") != "closed"
            or entry.get("base") != target or entry.get("head") != branch
            or entry.get("open_pr_count") != 0):
        return "PR_NOT_EXCLUSIVELY_MERGED_TO_TARGET"
    expected_prefix = "https://github.com/" + reported_repo + "/pull/"
    url = str(entry.get("pr_url", ""))
    if not url.lower().startswith(expected_prefix) or not url[len(expected_prefix):].isdigit():
        return "PR_REPOSITORY_OR_URL_MISMATCH"
    try:
        merged = iso(entry.get("merged_at"))
    except (ValueError, TypeError):
        return "INVALID_MERGED_TIMESTAMP"
    if merged > now + dt.timedelta(minutes=5):
        return "FUTURE_MERGE_TIMESTAMP"
    if historical and now - merged < dt.timedelta(hours=24):
        return "RECENT_MERGE_NOT_HISTORICAL"
    if not ancestor(repo, merged_sha, "refs/remotes/" + remote + "/" + target):
        return "MERGE_SHA_NOT_IN_TARGET"
    return None

def audit_path(repo):
    path = Path(git("rev-parse", "--path-format=absolute", "--git-common-dir", cwd=repo))
    return path / "phdk" / "git-hygiene-state.json"

def save_state(repo, report):
    path = audit_path(repo)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(".tmp")
    if path.exists() and "historical_inventory" not in report:
        try:
            previous = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(previous, dict) and "historical_inventory" in previous:
                report["historical_inventory"] = previous["historical_inventory"]
        except (ValueError, OSError):
            pass
    temp.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temp.replace(path)
    return str(path)

def apply(repo, remote, target, evidence, max_candidates, allow_generated_ignored=False):
    identity = repo_identity(repo, remote)
    if (evidence.get("schema_version") != 1 or
        str(evidence.get("repository", "")).lower() != identity or
        evidence.get("target") != target or evidence.get("remote") != remote):
        raise RuntimeError("evidence repository/target/remote/schema mismatch")
    now = dt.datetime.now(dt.timezone.utc)
    observed = iso(evidence.get("observed_at_utc"))
    if observed > now + dt.timedelta(minutes=5) or now - observed > dt.timedelta(minutes=MAX_AGE_MINUTES):
        raise RuntimeError("GitHub proof is stale or future-dated")
    scope = evidence.get("scope")
    if scope not in ("historical", "milestone"):
        raise RuntimeError("scope must be historical or milestone")
    entries = evidence.get("candidates")
    if not isinstance(entries, list) or not 1 <= len(entries) <= max_candidates:
        raise RuntimeError("candidate count must be between 1 and --max-candidates")
    git("fetch", "--no-tags", remote, target, cwd=repo)
    main_sha = rev(repo, "refs/remotes/" + remote + "/" + target)
    if not main_sha:
        raise RuntimeError("remote target is missing")
    report = {"mode": "APPLY", "scope": scope, "repository": identity,
              "target": target, "observed_main_sha": main_sha,
              "processed_at_utc": now.isoformat(), "results": [],
              "local_main": "UNVERIFIED"}
    seen = set()
    closeout = Path(__file__).with_name("phdk_git_closeout.py")
    if not closeout.is_file():
        raise RuntimeError("vendored phdk_git_closeout.py is missing")
    for entry in entries:
        branch = entry.get("branch", "")
        record = {"branch": branch, "local": "NOT_ATTEMPTED",
                  "remote": "NOT_ATTEMPTED"}
        report["results"].append(record)
        if branch in seen:
            record["reason"] = "DUPLICATE_BRANCH_EVIDENCE"
            continue
        seen.add(branch)
        proof_problem = validate_proof(repo, remote, target, entry, identity, now,
                                       scope == "historical")
        if proof_problem:
            record["reason"] = proof_problem
            continue
        head_sha = entry["head_sha"].lower()
        live_remote_sha = remote_head(repo, remote, branch)
        local_sha = rev(repo, "refs/heads/" + branch)
        if live_remote_sha and live_remote_sha.lower() != head_sha:
            record["reason"] = "REMOTE_SHA_CHANGED_SINCE_PR"
            continue
        if local_sha and local_sha.lower() != head_sha:
            record["reason"] = "LOCAL_SHA_DIFFERS_FROM_MERGED_PR"
            continue
        if not live_remote_sha and not local_sha:
            record.update(local="ALREADY_ABSENT", remote="ALREADY_ABSENT")
            continue
        cmd = [sys.executable, str(closeout), "--apply", "--remote", remote,
               "--target", target, "--merged-sha", entry["merge_sha"]]
        if local_sha:
            cmd += ["--branch", branch, "--pr-head-sha", entry["head_sha"]]
            if allow_generated_ignored:
                cmd.append("--allow-generated-ignored")
        step = subprocess.run(cmd, cwd=repo, capture_output=True, text=True, timeout=45)
        try:
            details = json.loads(step.stdout if step.stdout else step.stderr)
        except json.JSONDecodeError:
            details = {"error": "closeout did not produce JSON"}
        record["local"] = details.get("branch_cleanup", details.get("local_main", "BLOCKED"))
        record["local_main"] = details.get("local_main", "UNVERIFIED")
        if step.returncode or details.get("local_main") != "SYNCED":
            record["reason"] = "LOCAL_CLOSEOUT_RETAINED"
            continue
        report["local_main"] = "SYNCED"
        if not live_remote_sha:
            record["remote"] = "ALREADY_ABSENT"
            continue
        # Deletion-only compare-and-swap lease: no force update or history rewrite.
        ref = "refs/heads/" + branch
        deletion = subprocess.run(
            ["git", "-C", str(repo), "push",
             "--force-with-lease=" + ref + ":" + head_sha, remote, "--delete", ref],
            capture_output=True, text=True, timeout=45)
        if deletion.returncode:
            record["remote"] = "RETAINED_PUSH_REJECTED"
            record["reason"] = (deletion.stderr or deletion.stdout).strip()[-600:]
        elif remote_head(repo, remote, branch) is None:
            record["remote"] = "DELETED_VERIFIED"
        else:
            record["remote"] = "RETAINED_REMOTE_STILL_EXISTS"
    report["pending"] = sum(1 for x in report["results"] if x["remote"] not in
                            ("DELETED_VERIFIED", "ALREADY_ABSENT") or
                            x["local"] not in ("REMOVED_VERIFIED_BRANCH", "ALREADY_ABSENT", "NOT_REQUESTED"))
    report["history_batch_complete"] = scope == "historical" and report["pending"] == 0
    report["history_complete"] = bool(scope == "historical" and
                                      evidence.get("inventory_exhaustive") is True and
                                      evidence.get("out_of_scope_count") == 0 and
                                      report["pending"] == 0)
    report["state_path"] = save_state(repo, report)
    return report

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--record-inventory", action="store_true",
                        help="only in an authorized local Auto/Force run: save an audit checkpoint under .git")
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--target", default="main")
    parser.add_argument("--max-candidates", type=int, default=25)
    parser.add_argument("--allow-generated-ignored", action="store_true",
                        help="only after independently verifying that ignored contents are disposable")
    args = parser.parse_args()
    try:
        root = Path(git("rev-parse", "--show-toplevel")).resolve()
        if not 1 <= args.max_candidates <= 100:
            raise RuntimeError("max candidates must be between 1 and 100")
        if args.apply:
            if not args.evidence:
                raise RuntimeError("--apply requires --evidence with GitHub PR observations")
            report = apply(root, args.remote, args.target,
                           json.loads(args.evidence.read_text(encoding="utf-8")),
                           args.max_candidates, args.allow_generated_ignored)
            print(json.dumps(report, indent=2, sort_keys=True))
            return 0 if report["pending"] == 0 else 3
        found = inventory(root, args.remote, args.target)
        if args.record_inventory:
            marker = {"schema_version": 1, "historical_inventory": found,
                      "history_complete": False,
                      "observed_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}
            found["state_path"] = save_state(root, marker)
        print(json.dumps(found, indent=2, sort_keys=True))
        return 0
    except (RuntimeError, OSError, ValueError, KeyError, subprocess.TimeoutExpired) as err:
        print(json.dumps({"status": "BLOCKED", "error": str(err)}), file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
