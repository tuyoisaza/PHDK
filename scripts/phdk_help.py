#!/usr/bin/env python3
"""Offline, read-only rendering for conversational PHDK help. No updater or product execution."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MAX_DOC_BYTES = 16_384


def safe_read(path: Path) -> str:
    if not path.is_file() or path.is_symlink() or path.stat().st_size > MAX_DOC_BYTES:
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return ""


def normalize(value: str) -> str:
    value = re.sub(r"\s+", " ", value.strip().casefold())
    if value.startswith("phdk "):
        value = value[5:]
    if value.startswith("help "):
        value = value[5:]
    return value


def locate_catalog(root: Path) -> tuple[Path | None, Path | None]:
    for directory in (root / "phdk-standards", root):
        catalog = directory / "PHDK_COMMANDS.json"
        if catalog.is_file() and not catalog.is_symlink():
            return directory, catalog
    return None, None


def extract_goal(content: str) -> str:
    """Read a written goal, not a project name or a guessed purpose."""
    if not content:
        return ""
    lines = content.splitlines()
    titles = ("objetivo", "propósito", "purpose", "product intent", "project intent", "misión", "mission")
    for idx, line in enumerate(lines):
        heading = re.match(r"^#{1,3}\s+(.+?)\s*$", line)
        if heading and any(x in heading.group(1).casefold() for x in titles):
            for candidate in lines[idx + 1:idx + 9]:
                value = candidate.strip().lstrip(">-* ").strip()
                if value.startswith("#"):
                    break
                if len(value) >= 18 and not value.startswith("|"):
                    return re.sub(r"\s+", " ", value)[:300]
    return ""


def project_goal(root: Path) -> tuple[str, str, bool]:
    if (root / "PHDK_EVOLUTION_STANDARD.md").is_file() and (root / "PHDK_COMMANDS.json").is_file():
        return ("Mantener el sistema de estándares y comandos PHDK para entrega de software asistida por IA.",
                "PHDK_EVOLUTION_STANDARD.md", True)
    candidates = []
    index = safe_read(root / "docs" / "INDEX.md")
    # Generated docs/INDEX.md: Category | Document ID | Active baseline | Working draft.
    # Never infer the product objective from an archived version or unapproved draft.
    for line in index.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0] != "intents":
            continue
        active_link = re.search(r"\]\((intents/[A-Za-z0-9_./-]+\.md)\)", cells[2])
        if not active_link:
            continue
        # The project-intent baseline takes priority over feature-intent documents.
        if not ("project-intent" in active_link.group(1).lower() or "project_intent" in cells[1].lower()):
            continue
        candidate = root / "docs" / active_link.group(1)
        try:
            if candidate.resolve().is_relative_to(root.resolve()) and candidate not in candidates:
                candidates.append(candidate)
        except (OSError, RuntimeError, ValueError):
            continue
    # Legacy root intent is a fallback when no active versioned baseline has a goal.
    candidates.append(root / "PROJECT_INTENT.md")
    # Only explicit purpose sections are evidence. README title/branding is not a project goal.
    candidates.append(root / "README.md")
    for path in candidates:
        text = safe_read(path)
        goal = extract_goal(text)
        if goal:
            return goal, str(path.relative_to(root)).replace("\\", "/"), True
    return "no documentado / sin verificar", "sin fuente de intención confirmada", False


def suggested_action(root: Path, installed: bool, has_goal: bool) -> tuple[str, str]:
    if not installed:
        return "instalar PHDK", "falta el catálogo o la instalación local verificable"
    if not has_goal:
        return "PHDK capture", "no aparece un objetivo explícito en las fuentes revisadas"
    plan_exists = any((root / p).is_file() for p in ("MILESTONE_PLAN.md", "IMPLEMENTATION_PLAN.md"))
    if not plan_exists:
        plans = root / "docs" / "plans"
        if plans.is_dir() and not plans.is_symlink():
            try:
                plan_exists = any(
                    p.is_file() and p.suffix == ".md" and
                    ("milestone-plan" in p.name or "implementation-plan" in p.name)
                    for p in plans.iterdir()
                )
            except OSError:
                pass
    if not plan_exists:
        return "PHDK plan", "hay una intención documentada, pero no un plan de implementación visible"
    return "PHDK auto", "existen intención y plan; ejecútalo solo con un objetivo actual autorizado"


def build_report(root: Path, catalog_dir: Path, catalog: dict, *, detail: str = "", all_details: bool = False) -> dict:
    version = safe_read(catalog_dir / "VERSION").strip() or "sin verificar"
    goal, source, has_goal = project_goal(root)
    suggestion, reason = suggested_action(root, True, has_goal)
    entries = catalog["commands"]
    selected = None
    if detail:
        key = normalize(detail)
        selected = next((x for x in entries if key in [normalize(x["command"])] +
                         [normalize(a) for a in x.get("aliases", [])]), None)
        if selected is None:
            raise ValueError(f"Comando no encontrado: {detail}. Usa PHDK help para ver el catálogo.")
    if all_details:
        shown = entries
    else:
        shown = [{k: x[k] for k in ("group", "command", "summary")} for x in entries]
    return {
        "phdk_version_installed": version,
        "upstream_version": "sin verificar (sin consulta remota)",
        "purpose": catalog["purpose"],
        "project_goal": goal,
        "project_goal_source": source,
        "recommendation": suggestion,
        "recommendation_reason": reason,
        "commands": shown if not selected else [],
        "selected_command": selected,
        "read_only": True,
    }


def format_report(report: dict, *, all_details: bool = False) -> str:
    version = report["phdk_version_installed"]
    version_label = f"v{version}" if version != "sin verificar" else "sin verificar"
    lines = [f"PHDK help · {version_label}",
             f"PHDK: {report['purpose']}",
             f"Proyecto: {report['project_goal']} ({report['project_goal_source']})",
             f"Upstream: {report['upstream_version']}"]
    selected = report["selected_command"]
    if selected is not None:
        lines.extend(["", f"Comando: {selected['command']}", f"Qué hace: {selected['summary']}",
                      f"Cuándo: {selected['when']}", f"Efecto: {selected['effect']}",
                      f"Estándar: {selected['standard']}"])
        if selected["aliases"]:
            lines.append("Alias: " + ", ".join(selected["aliases"]))
    else:
        lines.extend(["", "Comandos disponibles (lista completa):"])
        grouped = {}
        for entry in report["commands"]:
            grouped.setdefault(entry["group"], []).append(entry)
        for group, entries in grouped.items():
            lines.append(f"  {group}:")
            for entry in entries:
                lines.append(f"    {entry['command']} — {entry['summary']}")
                if all_details:
                    lines.append(f"      Cuándo: {entry['when']} | Estándar: {entry['standard']}")
                    if entry["aliases"]:
                        lines.append("      Alias: " + ", ".join(entry["aliases"]))
    lines.extend(["", f"Recomendación: {report['recommendation']} — {report['recommendation_reason']}.",
                  "Solo orientación: no ejecuté comandos adicionales ni modifiqué archivos."])
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="Project or canonical PHDK root.")
    parser.add_argument("--command", default="", help='Detail for one command, e.g. "auto force".')
    parser.add_argument("--all", action="store_true", help="Expand aliases and usage for every command.")
    parser.add_argument("--json", action="store_true", help="Print the offline help result as JSON.")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    catalog_dir, catalog_path = locate_catalog(root)
    if catalog_dir is None or catalog_path is None:
        print("PHDK help: instalación/catálogo no encontrado; revisa phdk-standards/PHDK_COMMANDS.json.", file=sys.stderr)
        return 2
    try:
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        if catalog.get("schema_version") != 1 or not isinstance(catalog.get("commands"), list):
            raise ValueError("Catálogo de comandos inválido")
        report = build_report(root, catalog_dir, catalog, detail=args.command, all_details=args.all)
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
        print(f"PHDK help: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(format_report(report, all_details=args.all))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
