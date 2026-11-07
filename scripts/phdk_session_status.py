#!/usr/bin/env python3
"""Render a derived PHDK session snapshot as offline, accessible 1920x1080 SVGs.

Usage: phdk_session_status.py SNAPSHOT.json OUTPUT_DIR
Use a new or empty directory for the image set. No network or third-party packages.
"""
import argparse
from html import escape
import json
from math import ceil
from pathlib import Path
import unicodedata

BG, PANEL, EDGE = "#17191a", "#212425", "#404442"
WHITE, MUTED, ORANGE = "#fff9ed", "#babcb4", "#ff974d"
STATES = {
    "DONE": ("#7bd6a4", "#273c30", "HECHO", "DONE"),
    "IN_PROGRESS": ("#f6cf72", "#423921", "EN CURSO", "ACTIVE"),
    "PENDING": ("#ff9a90", "#402c2a", "PENDIENTE", "PENDING"),
    "BLOCKED": ("#ff9a90", "#402c2a", "BLOQUEADO", "BLOCKED"),
}
TEXT = {
    "es": ("CIERRE DE SESIÓN", "RUTA DE HITOS", "completados", "TRABAJO EN EL HITO",
           "CONFIGURACIÓN", "PRÓXIMOS PASOS", "PUBLICACIÓN", "DESPLIEGUE", "ACEPTACIÓN",
           "Sin hitos definidos", "Sin actividad registrada", "PÁG."),
    "en": ("SESSION CLOSE", "MILESTONE PLAN", "complete", "MILESTONE WORK",
           "CONFIGURATION", "NEXT STEPS", "PUBLICATION", "DEPLOYMENT", "ACCEPTANCE",
           "Milestones not defined", "No activity recorded", "PAGE"),
}


def label(value, limit, field):
    if not isinstance(value, str) or not value.strip() or len(value) > limit:
        raise ValueError(f"{field}: supply 1–{limit} characters")
    if any(unicodedata.category(c) in {"Cc", "Cs"} or c in "\ufffe\uffff" for c in value):
        raise ValueError(f"{field}: invalid control character")
    return value.strip()


def validate(data):
    if not isinstance(data, dict) or data.get("language", "en") not in TEXT:
        raise ValueError("expected a snapshot object; language must be en or es")
    for key, limit in (("project", 50), ("goal", 106), ("session", 55),
                       ("publication", 44), ("deployment", 44), ("acceptance", 44)):
        data[key] = label(data.get(key), limit, key)
    for key in ("current", "configuration", "next_steps", "milestones"):
        if not isinstance(data.get(key), list):
            raise ValueError(f"{key}: expected a list")
        if key != "milestones":
            data[key] = [label(item, 59, key) for item in data[key]]
    ids = set()
    for m in data["milestones"]:
        if not isinstance(m, dict) or m.get("status") not in STATES:
            raise ValueError("milestones: unknown status or malformed entry")
        m["id"] = label(m.get("id"), 12, "milestone ID")
        m["title"] = label(m.get("title"), 49, "milestone title")
        if m["id"] in ids:
            raise ValueError(f"duplicate milestone ID: {m['id']}")
        ids.add(m["id"])


def rect(x, y, w, h, fill, r=0, stroke="none"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"/>'


def txt(x, y, value, size=24, color=WHITE, bold=False, width=None, anchor="start"):
    # Fit unusually wide names without clipping IDs or discarding milestone text.
    if width:
        units = sum(1 if unicodedata.east_asian_width(c) in {"F", "W"} or c in "MW@%"
                    else .8 if c.isupper() else .69 for c in value)
        size = min(size, width / max(units, 1))
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size:.2f}" '
            f'font-weight="{700 if bold else 400}" fill="{color}">{escape(value)}</text>')


def line(x1, y1, x2, y2, color=EDGE, weight=1):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="{weight}"/>'


def icon(state, x, y, color):
    shapes = {
        "DONE": '<path d="m-8 0 5 5 10-11"/>',
        "IN_PROGRESS": '<circle r="7"/><circle r="2" fill="currentColor"/>',
        "PENDING": '<circle r="7"/>',
        "BLOCKED": '<path d="M-7-7 7 7 M7-7 -7 7"/>',
    }
    return (f'<g transform="translate({x} {y})" color="{color}" stroke="{color}" '
            f'stroke-width="2.5" stroke-linecap="round" fill="none">{shapes[state]}</g>')


def chunk(items, count, page):
    # Compact sections persist as context across pages. Longer lists keep their order.
    return items[:count] if len(items) <= count else items[page * count:(page + 1) * count]


def render(d, page, pages):
    lang = d.get("language", "en")
    close, plan, done, work, config, steps, pub, deploy, uat, no_plan, empty, page_word = TEXT[lang]
    ms = d["milestones"]
    progress = f"{sum(m['status'] == 'DONE' for m in ms)} / {len(ms)} {done}"
    page_label = f"{page_word} {page + 1:02} / {pages:02}"
    visible = chunk(ms, 5, page)
    summary = [d["goal"], d["session"], progress, *(
        f"{m['id']} {m['title']} ({STATES[m['status']][2 if lang == 'es' else 3]})" for m in visible)]
    for key, head in (("current", work), ("configuration", config), ("next_steps", steps)):
        summary.extend([head, *chunk(d[key], 2, page)])
    summary.extend((pub, d["publication"], deploy, d["deployment"], uat, d["acceptance"]))
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080" xml:lang="{lang}" role="img" aria-labelledby="title desc" font-family="DejaVu Sans, sans-serif">',
             f'<title id="title">{escape(d["project"])} · {close} · {page_label}</title>',
             f'<desc id="desc">{escape(". ".join(summary))}</desc>',
             rect(0, 0, 1920, 1080, BG), rect(58, 36, 8, 32, ORANGE, 2),
             txt(83, 62, "PHDK", 28, WHITE, True), line(181, 40, 181, 66),
             txt(204, 60, f"AUTO  /  {close}", 20, MUTED, True),
             txt(1861, 60, d["session"], 22, ORANGE, True, 900, "end"),
             line(58, 91, 1862, 91), txt(55, 172, d["project"], 69, WHITE, True, 1730),
             txt(60, 220, d["goal"], 30, MUTED, width=1780),
             rect(58, 258, 876, 629, PANEL, 18), txt(91, 312, plan, 23, WHITE, True),
             txt(901, 312, progress, 21, MUTED, anchor="end"), line(91, 339, 901, 339)]
    def previous_pages(count):
        lead = "Ver páginas" if lang == "es" else "See pages"
        return f"{lead} 01–{count:02}."
    if not visible:
        parts.append(txt(92, 405, previous_pages(ceil(len(ms) / 5)) if ms else no_plan, 26, MUTED))
    for i, m in enumerate(visible):
        y = 343 + 106 * i
        state = m["status"]
        color, tint, es, en = STATES[state]
        if i:
            parts.append(line(91, y, 901, y))
        if state == "IN_PROGRESS":
            parts.append(rect(69, y + 23, 4, 54, color, 2))
        parts += [txt(92, y + 32, m["id"], 18, MUTED, True, 190),
                  txt(90, y + 71, m["title"], 29, WHITE, True, 615),
                  rect(729, y + 35, 173, 40, tint, 20),
                  icon(state, 751, y + 55, color),
                  txt(772, y + 61, es if lang == "es" else en, 17, color, True, 122)]
    for n, (key, head) in enumerate((("current", work), ("configuration", config), ("next_steps", steps))):
        y = 258 + n * 217
        color = ORANGE if n == 0 else MUTED
        parts += [rect(960, y, 902, 195, "#2d2925" if n == 0 else PANEL, 18),
                  rect(992, y + 32, 38, 3, color), txt(1043, y + 40, head, 21, color, True)]
        rows = chunk(d[key], 2, page)
        if not rows:
            message = previous_pages(ceil(len(d[key]) / 2)) if d[key] else empty
            parts.append(txt(993, y + 108, message, 23, MUTED))
        for j, value in enumerate(rows):
            idx = (0 if len(d[key]) <= 2 else page * 2) + j + 1
            baseline = y + 98 + j * 51
            parts += [txt(994, baseline, f"{idx:02}", 18, color, True, 46),
                      txt(1045, baseline, value, 28, WHITE, width=775)]
    parts.append(line(58, 923, 1862, 923))
    for n, (head, key) in enumerate(((pub, "publication"), (deploy, "deployment"), (uat, "acceptance"))):
        x = 60 + n * 605
        if n:
            parts.append(line(x - 29, 952, x - 29, 1013))
        parts += [txt(x, 965, head, 18, MUTED, True), txt(x, 1003, d[key], 25, WHITE, width=549)]
    parts += [txt(1861, 1052, page_label, 16, MUTED, True, anchor="end"), "</svg>"]
    return "\n".join(parts) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.snapshot.read_text(encoding="utf-8"))
        validate(data)
        pages = max(1, ceil(len(data["milestones"]) / 5),
                    *(ceil(len(data[k]) / 2) for k in ("current", "configuration", "next_steps")))
        args.output_dir.mkdir(parents=True, exist_ok=True)
        if any(args.output_dir.iterdir()):
            raise ValueError("use a new or empty directory for the image set")
        for page in range(pages):
            target = args.output_dir / f"status-{page + 1:02}.svg"
            target.write_text(render(data, page, pages), encoding="utf-8")
            print(target)
    except (OSError, ValueError, TypeError) as exc:
        parser.exit(1, f"session status: {exc}\n")


if __name__ == "__main__":
    main()
