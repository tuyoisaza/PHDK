#!/usr/bin/env python3
"""Read-only post-UAT Export Modules gate: no UAT, cross-repo writes, or publishing.

The caller must reconcile this bounded state with the actual UAT report/handoff.
The state is an evidence *declaration*, not proof that acceptance was executed.
"""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys

MAX_STATE_BYTES = 32768
VALID_RESULTS = {"NOT_RUN", "ACCEPTED", "NOT_ACCEPTED", "ACCEPTANCE_INCOMPLETE"}
VALID_FIX = {"NOT_APPLICABLE", "VERIFIED_COMPLETE", "PENDING", "UNVERIFIED"}
REQUIRED = {
    "schema_version", "run_id", "explicit_uat", "conclusion", "tested_revision",
    "current_revision", "open_required_defects", "unverified_required_cases",
    "fix_disposition", "evidence_reference",
}
SHA = re.compile(r"[0-9a-fA-F]{40}\Z")
RUN = re.compile(r"[a-zA-Z0-9][a-zA-Z0-9._-]{0,79}\Z")


def state_from_text(text):
    if len(text.encode("utf-8")) > MAX_STATE_BYTES:
        raise ValueError("state exceeds size limit")
    data = json.loads(text)
    if not isinstance(data, dict) or set(data) != REQUIRED:
        raise ValueError("state requires exactly the documented fields")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise ValueError("unsupported schema_version")
    if not isinstance(data["run_id"], str) or not RUN.fullmatch(data["run_id"]):
        raise ValueError("invalid run_id")
    if type(data["explicit_uat"]) is not bool:
        raise ValueError("explicit_uat must be boolean")
    if (not isinstance(data["conclusion"], str) or data["conclusion"] not in VALID_RESULTS
            or not isinstance(data["fix_disposition"], str)
            or data["fix_disposition"] not in VALID_FIX):
        raise ValueError("invalid conclusion or fix_disposition")
    for key in ("tested_revision", "current_revision"):
        value = data[key]
        if value is not None and (not isinstance(value, str) or not SHA.fullmatch(value)):
            raise ValueError(f"invalid {key} (must be full Git SHA or null)")
    for key in ("open_required_defects", "unverified_required_cases"):
        if type(data[key]) is not int or not 0 <= data[key] <= 100000:
            raise ValueError(f"invalid {key}")
    ref = data["evidence_reference"]
    if not isinstance(ref, str) or not 0 < len(ref) <= 300 or any(x in ref for x in ("\n", "\r", "\x00")):
        raise ValueError("invalid evidence_reference")
    return data


def gated_status(state):
    """No source scanning unless acceptance has verified conditions, with no new UAT."""
    if not state["explicit_uat"] or state["conclusion"] == "NOT_RUN":
        return "DEFERRED_UAT_NOT_RUN"
    if state["conclusion"] == "NOT_ACCEPTED" or state["open_required_defects"]:
        return "WAITING_FOR_UAT_FIX"
    if state["conclusion"] == "ACCEPTANCE_INCOMPLETE" or state["unverified_required_cases"]:
        return "ACCEPTANCE_INCOMPLETE"
    if state["fix_disposition"] not in {"NOT_APPLICABLE", "VERIFIED_COMPLETE"}:
        return "WAITING_FOR_UAT_FIX"
    if not state["tested_revision"] or not state["current_revision"]:
        return "REVISION_UNVERIFIED"
    if state["tested_revision"].lower() != state["current_revision"].lower():
        return "STALE_ACCEPTANCE"
    return "READY_FOR_REVIEW"


def load_state(root, state_arg, stream):
    if state_arg == "-":
        return state_from_text(stream.read(MAX_STATE_BYTES + 1))
    p = Path(state_arg)
    p = p if p.is_absolute() else root / p
    # Follow no user-supplied symlink or private path escaping the named donor.
    if p.is_symlink() or not p.resolve().is_relative_to(root.resolve()):
        raise ValueError("state file must stay within donor and must not be a symlink")
    if not p.is_file() or p.stat().st_size > MAX_STATE_BYTES:
        raise ValueError("missing or oversized state file")
    return state_from_text(p.read_text(encoding="utf-8"))


def load_export_module(script_path):
    if not script_path.is_file() or script_path.is_symlink():
        raise ValueError("vendored Export Modules inventory helper unavailable")
    spec = importlib.util.spec_from_file_location("phdk_export_modules", script_path)
    if spec is None or spec.loader is None:
        raise ValueError("inventory helper cannot be loaded")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def evaluate(root, state, inventory_module=None, catalog=None):
    status = gated_status(state)
    result = {
        "schema_version": 1,
        "mode": "POST_EXPLICIT_UAT_EXPORT_REVIEW",
        "gate": status,
        "run_id": state["run_id"],
        "accepted_revision": state["tested_revision"] if status == "READY_FOR_REVIEW" else None,
        "evidence_reference": state["evidence_reference"],
        "evidence_status": "CALLER_MUST_VERIFY_UAT_REPORT",
        "publication": "NOT_AUTHORIZED_BY_REVIEW",
        "approval": "NAMED_OWNER_SELECTION_REQUIRED_FOR_EXPORT",
        "candidates": [],
        "catalog_status": "NOT_SCANNED",
        "review_key": None,
    }
    if status != "READY_FOR_REVIEW":
        return result
    if inventory_module is None:
        raise ValueError("approved local inventory helper is required after acceptance")
    entries = inventory_module.load_catalog(inventory_module.catalog_at(root, catalog))
    scan = inventory_module.report(root, entries)
    result["candidates"] = scan["candidates"]
    result["catalog_status"] = scan["catalog_status"]
    fingerprint = json.dumps(
        {"sha": state["tested_revision"].lower(), "catalog": entries, "candidates": scan["candidates"]},
        ensure_ascii=False, sort_keys=True, separators=(",", ":"),
    )
    result["review_key"] = hashlib.sha256(fingerprint.encode("utf-8")).hexdigest()
    return result


def markdown(result):
    lines = ["# PHDK Post-UAT Export Modules Review", "",
             f"**Gate:** {result['gate']}",
             "**Publishing:** NOT AUTHORIZED BY REVIEW. Owner choice required.",
             "**UAT evidence:** caller must reconcile declared status with actual report/revision.", ""]
    if result["gate"] != "READY_FOR_REVIEW":
        lines.append("No inventory executed. Preserve candidates from Auto retrospective for a later explicitly authorized accepted UAT.")
    elif not result["candidates"]:
        lines.append("No module candidates detected by the bounded inventory; this is not a full code-review proof.")
    else:
        lines += ["| Local candidate | Signal | Priority | Review decision |", "|---|---|---|---|"]
        for c in result["candidates"]:
            path = c["id"].replace("|", "\\|").replace("`", "")
            lines.append(f"| {path} | {c['category']} | {c['priority']} | NEEDS_OWNER_SELECTION |")
        lines.append("\nReview code, rights, license, secrets, tests and portability before a named export decision.")
    return "\n".join(lines) + "\n"


def main(argv=None, stream=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="authorized donor root")
    parser.add_argument("--state", required=True, help="bounded UAT evidence-state JSON path or - for stdin")
    parser.add_argument("--catalog", type=Path, default=None, help="optional local public reuse catalog")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if not root.is_dir():
        parser.error("--root must be an existing directory")
    try:
        if args.catalog is not None:
            catalog = args.catalog if args.catalog.is_absolute() else root / args.catalog
            if catalog.is_symlink() or not catalog.resolve().is_relative_to(root):
                raise ValueError("catalog must remain inside donor repository and not be a symlink")
        else:
            catalog = None
        state = load_state(root, args.state, stream if stream is not None else sys.stdin)
        module = load_export_module(Path(__file__).resolve().with_name("phdk_export_modules.py")) if gated_status(state) == "READY_FOR_REVIEW" else None
        result = evaluate(root, state, inventory_module=module, catalog=catalog)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        print(f"PHDK post-UAT export: invalid or unavailable evidence ({type(exc).__name__})", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else markdown(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
