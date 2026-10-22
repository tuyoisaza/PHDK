# PHDK SEO — Public Discoverability Stage

## Placement and activation

Run **SEO after Integration and before Check** in `PHDK auto`; UAT Prep/UAT/Fix remain DEFERRED — OWNER OPT-IN. SEO is a full lifecycle stage with a required historical handoff, not an optional suggestion. It is **APPLICABLE** when the product has public pages intended for search discovery (marketing site, public catalog, documentation, articles or public landing pages). For an entirely private/authenticated product without intended public indexable content mark **NOT APPLICABLE**, state evidence and create a minimal SEO applicability record without fabricating SEO work. Mixed applications: evaluate public routes only. Do not noindex public pages merely because the application also has private routes.

The SEO stage may repair relevant code/config within the already authorized lifecycle goal. For a standalone `PHDK seo` request, the current user's explicit command authorizes scoped SEO diagnosis and repository-local remediations, not unrelated features, provider administration or production publishing. Preserve Capture intent, UAT acceptance criteria, and the owner-confirmed commitment ledger. Material new editorial/product decisions must be returned to the owner; an SEO recommendation alone is not authority to change product claims.

## Mandatory inputs

- Current integration candidate revision, Capture's audience/market/language/intent, Plan architecture, confirmed commitments, available UAT/UAT Fix history, if any, without requiring acceptance to run.
- Public route inventory, deployment/build method, relevant pages/templates, rendering model (SSR/SSG/SPA/WordPress/etc.), robots/sitemap/canonical and currently available local diagnostics.
- Current SEO measurements, if legitimately available; Search Console or production data only through authorized read-only access. Do not ask for credentials or inspect secrets.

Validate SEO source/configuration against the current integration candidate using permitted static evidence. Auto records UAT NOT RUN; absent or historical failed acceptance does not gate SEO or reopen development. Preserve known defects as evidence and fix only those within the current development scope. After SEO changes, refresh affected static checks and candidate evidence. Functional/UAT regressions run only within a separately explicitly initiated UAT; otherwise retain their cases and unverified status for that optional run. Apply `PHDK_LIFECYCLE.md` to genuinely invalidated authorized handoffs.

## Workflow

1. **Inventory**: inspect source, route definitions, templates and indexation intent. Maintain public indexable vs private/nonindexable routes and per-language variants.
2. **Baseline**: inspect title/head, descriptions, H1 hierarchy, canonicals, robots, sitemap, links, status/redirects and structured data. Use existing authorized non-destructive tooling only. Run mobile-priority Lighthouse and browser observations only when available **within the scoped UAT browser exception or separately explicitly authorized for SEO**; SEO does not initiate UAT or extend browser rights. Search Console and field CWV require real authorized evidence. Write N/D otherwise.
3. **Fix**: implement minimal, reusable changes in code, respecting public URL continuity, content accuracy, accessibility, conversions, brand, analytics and localization. Never invent business claims, reviews, prices, authors, links, search volumes or rankings. Do not add keyword stuffing, cloaking, doorway pages or bought links. Do not make production DNS/CDN/provider changes.
4. **Validate**: rerun permitted safe builds, static source/template checks and route-definition review; where authorized, rerun same-condition performance/crawl scans. Record before/after separately, never declare a field metric improved without comparable data. Record affected acceptance cases for later explicit UAT; Auto does not execute them.
5. **Report**: create `SEO_AUDIT_REPORT.md`, `SEO_REMEDIATION_REPORT.md` (or explicit zero-change statement), and `SEO_CHECKLIST.md` with 25 rows, each status, evidence, action and retest. Include URLs/templates sampled, revision, tool/environment/method, modified paths, remaining risks, external prerequisites and one most important next action. Snapshot in the stage handoff and update `PHDK_COMMITMENTS.md` if confirmed SEO commitments are affected.

## 25 technical SEO controls

Each control must be **PASS / FAIL / BLOCKED / NOT_APPLICABLE** with evidence and relevant URL/template. No inferred PASS; missing field data is BLOCKED/NOT MEASURED as appropriate, not fabricated FAIL.

| ID | Check | Expected validation and safe remediation |
|---|---|---|
| SEO-01 | robots.txt | Correct syntax/status; no accidental disallow for indexable pages; robots is not a substitute for noindex |
| SEO-02 | Indexability | Intended pages accessible/indexable, no conflicting noindex or X-Robots-Tag; preserve intentional private noindex |
| SEO-03 | XML sitemap | Absolute canonical 200/indexable URLs, correct exclusions and robots reference |
| SEO-04 | Canonical | Absolute coherent canonical per indexable page, aligned with sitemap/redirects |
| SEO-05 | HTTP/redirects | Fix internal 4xx/5xx, redirect loops/chains and permanent moves without redirecting everything home |
| SEO-06 | Search intent | Helpful, truthful purpose by page; mark unverified editorial strategy for decision |
| SEO-07 | Query terminology | Natural descriptive terms without forced density or invented volumes |
| SEO-08 | Title | Distinct meaningful per-page titles, no arbitrary universal character limit |
| SEO-09 | Meta description | Unique useful descriptions on priority pages; no promise of ranking or snippet selection |
| SEO-10 | Headings | Descriptive semantic H1/H2/H3, no arbitrary single-H1 dogma |
| SEO-11 | Original useful content | Detect thin/duplicate pages; substantive editorial changes require approval |
| SEO-12 | Trust/authors/sources | Genuine responsible entity, contacts/authors/sources where relevant; no fake credentials |
| SEO-13 | LCP | Field p75 target <= 2.5s when measured; optimize likely bottlenecks without false field claims |
| SEO-14 | INP | Field p75 target <= 200ms when measured; reduce costly JavaScript/main-thread tasks |
| SEO-15 | CLS | Field p75 target <= 0.1 when measured; reserve dimensions/space |
| SEO-16 | Mobile | Viewport, parity, navigation, readability and usability |
| SEO-17 | HTTPS | HTTPS/mixed-content verification, no unauthorized infrastructure writes |
| SEO-18 | Interstitials | Avoid intrusive mobile overlays while preserving mandatory notices |
| SEO-19 | Internal links | Crawlable descriptive links and legitimate contextual connections |
| SEO-20 | Information architecture | Coherent routes/navigation/breadcrumbs preserving existing URLs or justified redirects |
| SEO-21 | Images | Meaningful alt (empty decorative alt), modern sizing/compression, avoid lazy loading LCP hero |
| SEO-22 | Structured data | Accurate eligible JSON-LD matching visible content; validate syntax, do not promise rich results |
| SEO-23 | Rendering | Ensure important content, metadata and links accessible to crawlers in actual architecture |
| SEO-24 | Search Console | Use real connected coverage/queries where authorized; otherwise BLOCKED, no invented data |
| SEO-25 | Links/reputation | Only real sourced link/mention evidence; no fabricated backlink profile or paid spam |

These controls are an **engineering checklist**, not 25 official Google ranking factors and not a score that predicts search placement. Prioritize accidental indexation blockers, essential metadata/content, navigation, then performance and optional opportunities. Prefer Core Web Vitals field p75 over synthetic lab results, clearly distinguish them.

## Completion and handoff

The SEO exit gate requires: applicability decided; checklist complete with evidenced classifications; significant fixable in-scope defects addressed or itemized as blockers; permitted regressions/build checked; no new functional regressions known; before/after and evidence limits recorded; handoff snapshots committed. **FAILED or BLOCKED critical indexation defects prevent SEO success**, and may block full Auto completion under `PHDK_COMMITMENT_STANDARD.md`; nonapplicable and externally unavailable measurements must not be mislabeled PASS. SEO never claims guaranteed ranking, Lighthouse 100, Search Console validation or production indexation without real evidence.

Stage archive: `docs/phdk/lifecycle/<run-id>/65-seo/` with `HANDOFF.md` and snapshots of `SEO_AUDIT_REPORT.md`, `SEO_CHECKLIST.md`, `SEO_REMEDIATION_REPORT.md` and affected candidate/ledger evidence. Check must verify this handoff (or documented NOT APPLICABLE) before its audit.

## Reference and provenance

Adapted from the owner-supplied “SEO EXECUTOR — Agent Skill / Instrucciones operativas” (25 checks). Public technical references: Google Search Central SEO Starter Guide / Search Essentials, Google structured data and Core Web Vitals documentation, Chrome Lighthouse documentation. This standard does not represent the 25 controls as Google's ranking formula.
