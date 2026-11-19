#!/usr/bin/env python3
"""Offline, dependency-free baseline validation for PHDK ULEDS event v1.

This is a conservative structural/privacy gate, NOT a complete JSON Schema
implementation, production ingestion endpoint, or permission to retrieve logs.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import json
from pathlib import Path
import re
import sys

CHANNELS = {"client", "backend_deployment", "support", "contextual_feedback"}
ENVIRONMENTS = {"production", "staging", "development", "test"}
SEVERITIES = {"DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"}
OUTCOMES = {"success", "failure", "degraded", "requested", "unknown"}
TOP_KEYS = {"specversion", "id", "source", "type", "time", "datacontenttype",
            "subject", "data"}
DATA_KEYS = {"schema_version", "project_id", "environment", "service",
             "channel", "severity", "outcome", "received_at", "product_version",
             "git_sha", "deployment_id", "location", "actor", "action",
             "fingerprint", "correlation", "privacy", "evidence_refs"}
NULLABLE = ("product_version", "git_sha", "deployment_id", "fingerprint")
EVENT_TYPE = re.compile(
    r"^phdk\.(?:client|backend|build|deployment|runtime|security|support|feedback)"
    r"\.[a-z][a-z0-9_.-]*$"
)
ORIGIN = re.compile(r"^https://[A-Za-z0-9.-]+(?::[0-9]{1,5})?$")
ROUTE = re.compile(r"^/(?!/)[A-Za-z0-9/_{}.-]*$")
SHA = re.compile(r"^[0-9a-f]{40}$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:[+-][A-Za-z0-9.-]+)?$")
TRACE = re.compile(r"^[0-9a-f]{32}$")
SPAN = re.compile(r"^[0-9a-f]{16}$")


def _object(value, keys, path, errors, allowed=None):
    """Reject undeclared fields; schema v1 forbids additional properties."""
    if not isinstance(value, dict):
        errors.append(f"{path}: expected object")
        return False
    for key in keys - value.keys():
        errors.append(f"{path}.{key}: missing")
    for key in value.keys() - (allowed if allowed is not None else keys):
        errors.append(f"{path}.{key}: unexpected field")
    return True


def _text(value, key, errors, maximum=256, allow_none=False):
    if value is None and allow_none:
        return
    if not isinstance(value, str) or not (1 <= len(value) <= maximum):
        errors.append(f"{key}: must be nonempty text (max {maximum})")


def _utc(value, key, errors):
    if not isinstance(value, str) or not value.endswith("Z"):
        errors.append(f"{key}: UTC Z timestamp required")
        return
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        errors.append(f"{key}: invalid ISO-8601 timestamp")


def validate(event):
    """Return list of human-readable violations; no IO or side effects."""
    errors = []
    if not _object(event, TOP_KEYS, "event", errors):
        return errors
    if event.get("specversion") != "1.0":
        errors.append("specversion: expected CloudEvents 1.0")
    if event.get("datacontenttype") != "application/json":
        errors.append("datacontenttype: expected application/json")
    for key, limit in (("id", 128), ("source", 256), ("subject", 200)):
        _text(event.get(key), key, errors, limit)
    typ = event.get("type")
    if not isinstance(typ, str) or not EVENT_TYPE.fullmatch(typ):
        errors.append("type: invalid PHDK taxonomy")
    _utc(event.get("time"), "time", errors)
    data = event.get("data")
    if not _object(data, DATA_KEYS, "data", errors,
                   DATA_KEYS | {"error", "feedback", "extensions"}):
        return errors
    if data.get("schema_version") != "1.0":
        errors.append("data.schema_version: expected 1.0")
    for key in ("project_id", "service", "action"):
        _text(data.get(key), "data." + key, errors, 128)
    for key, choices in (("environment", ENVIRONMENTS), ("channel", CHANNELS),
                         ("severity", SEVERITIES), ("outcome", OUTCOMES)):
        if not isinstance(data.get(key), str) or data.get(key) not in choices:
            errors.append(f"data.{key}: invalid value")
    _utc(data.get("received_at"), "data.received_at", errors)
    for key in NULLABLE:
        _text(data.get(key), "data." + key, errors, allow_none=True)
    product_version = data.get("product_version")
    if product_version is not None and (
        not isinstance(product_version, str)
        or not SEMVER.fullmatch(product_version)
    ):
        errors.append("data.product_version: invalid SemVer")
    sha = data.get("git_sha")
    if sha is not None and (not isinstance(sha, str) or not SHA.fullmatch(sha)):
        errors.append("data.git_sha: full 40-char lowercase SHA or null required")
    location = data.get("location")
    if _object(location, {"origin", "route", "screen_id", "component_id"},
               "data.location", errors):
        for key in ("screen_id", "component_id"):
            _text(location.get(key), "data.location." + key, errors, 128, True)
        for key, regex in (("origin", ORIGIN), ("route", ROUTE)):
            item = location.get(key)
            if item is not None and (not isinstance(item, str)
                                     or len(item) > 250
                                     or not regex.fullmatch(item)):
                errors.append(f"data.location.{key}: unsafe unnormalized URL/route")
    actor = data.get("actor")
    if _object(actor, {"role", "tenant_ref", "actor_ref"}, "data.actor", errors):
        for key in ("role", "tenant_ref", "actor_ref"):
            _text(actor.get(key), "data.actor." + key, errors, 128, True)
    corr = data.get("correlation")
    corr_keys = {"trace_id", "span_id", "request_id", "session_id",
                 "incident_id", "conversation_id"}
    if _object(corr, corr_keys, "data.correlation", errors):
        for key in corr_keys:
            _text(corr.get(key), "data.correlation." + key, errors, 128, True)
        for key, regex in (("trace_id", TRACE), ("span_id", SPAN)):
            item = corr.get(key)
            if item is not None and (not isinstance(item, str)
                                     or not regex.fullmatch(item)):
                errors.append(f"data.correlation.{key}: invalid trace identifier")
    privacy = data.get("privacy")
    if _object(privacy, {"classification", "redacted", "consent_ref"},
               "data.privacy", errors):
        if not isinstance(privacy.get("classification"), str) or privacy.get("classification") not in {"public", "internal", "restricted"}:
            errors.append("data.privacy.classification: invalid")
        if privacy.get("redacted") is not True:
            errors.append("data.privacy.redacted: must be true before persistence")
        _text(privacy.get("consent_ref"), "data.privacy.consent_ref",
              errors, 128, True)
    refs = data.get("evidence_refs")
    if not isinstance(refs, list) or len(refs) > 10 or any(
        not isinstance(ref, str) or not (1 <= len(ref) <= 256) for ref in refs
    ):
        errors.append("data.evidence_refs: expected up to 10 safe references")
    err = data.get("error")
    if err is not None:
        if _object(err, {"code", "safe_message", "fingerprint"}, "data.error", errors,
                   {"code", "safe_message", "fingerprint", "safe_stack_ref"}):
            for key, size in (("code", 100), ("safe_message", 512), ("fingerprint", 128)):
                _text(err.get(key), "data.error." + key, errors, size)
    feedback = data.get("feedback")
    if feedback is not None:
        if _object(feedback, {"kind", "summary", "ticket_ref"}, "data.feedback", errors):
            if not isinstance(feedback.get("kind"), str) or feedback.get("kind") not in {"bug", "improvement", "question", "security"}:
                errors.append("data.feedback.kind: invalid")
            _text(feedback.get("summary"), "data.feedback.summary", errors, 500)
            _text(feedback.get("ticket_ref"), "data.feedback.ticket_ref",
                  errors, 128, True)
    if isinstance(typ, str) and EVENT_TYPE.fullmatch(typ):
        category = typ.split(".")[1]
        expected = {
            "client": "client",
            "backend": "backend_deployment",
            "build": "backend_deployment",
            "deployment": "backend_deployment",
            "runtime": "backend_deployment",
            "security": "backend_deployment",
            "support": "support",
            "feedback": "contextual_feedback",
        }[category]
        if data.get("channel") != expected:
            errors.append("data.channel: does not match event type")
        if typ.rsplit(".", 1)[-1] in {"error", "failed", "exception"} and err is None:
            errors.append("data.error: required for failure event type")
    extensions = data.get("extensions")
    if extensions is not None and (
        not isinstance(extensions, dict) or len(extensions) > 10 or any(
            not isinstance(key, str) or not isinstance(val, (str, int, float, bool, type(None)))
            for key, val in extensions.items()
        )
    ):
        errors.append("data.extensions: invalid scalar extension values")
    if data.get("channel") == "contextual_feedback" and (
        not isinstance(location, dict) or not location.get("component_id")
    ):
        # Deliberately permit route-only fallback: route is the minimum safe anchor.
        if not isinstance(location, dict) or not location.get("route"):
            errors.append("contextual feedback: component_id or route required")
    if isinstance(data.get("channel"), str) and data.get("channel") in {"support", "contextual_feedback"} and feedback is None:
        errors.append("support/feedback: feedback object required")
    try:
        if len(json.dumps(event, ensure_ascii=False).encode("utf-8")) > 16 * 1024:
            errors.append("event: exceeds 16 KiB limit")
    except (TypeError, ValueError):
        errors.append("event: cannot serialize as JSON")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args(argv)
    failed = False
    for path in args.files:
        try:
            if path.stat().st_size > 16 * 1024:
                raise ValueError("event exceeds the 16 KiB limit")
            event = json.loads(path.read_text(encoding="utf-8"))
            errors = validate(event)
        except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
            errors = [str(exc)]
        if errors:
            failed = True
            print(f"FAIL {path}: " + "; ".join(errors), file=sys.stderr)
        else:
            print(f"PASS {path} (ULEDS v1 baseline)")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
