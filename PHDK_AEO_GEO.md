# PHDK AEO/GEO — Answer and Generative Discovery Stage

## Position and scope

Run **after SEO and before Check** (Integration → SEO → AEO/GEO → Check). Auto keeps UAT Prep/UAT/Fix DEFERRED — OWNER OPT-IN. AEO means answer engine optimization; GEO means generative engine optimization. Apply to public content that the owner intends to be discoverable, cited, or used as a reliable source in AI-assisted search. For private/authenticated systems with no public discovery goal mark NOT APPLICABLE, with evidence. Reuse SEO technical findings rather than inventing a second set of indexation tasks.

**No special ranking formula exists.** Google states that ordinary SEO fundamentals are relevant to AI Overviews/AI Mode, without additional required special files or schema; Bing emphasizes indexation, verified facts, clear entities and semantic content for grounding. No guarantee of citations, AI recommendations, referral traffic or model behavior. Do not treat a model's answer as proof of indexing, rank or attribution.

## Entry gate

Verify SEO handoff and report (including explicit NOT APPLICABLE) for the exact candidate. Consult existing UAT/UAT Fix history when relevant without requiring a run or making historical acceptance failure a development gate. Consume Capture audience/market/language/intent, public route map, validated SEO canonical/indexability, existing real content, source/brand provenance and owner-approved claims. AEO/GEO may be NOT APPLICABLE when SEO is NOT APPLICABLE unless a specifically confirmed public answer/discovery goal exists. If upstream SEO is BLOCKED on essential discoverability, report dependency rather than fabricate AEO/GEO success.

## Execute, don't merely advise

1. Identify user questions that actual public pages can answer, mapped to owner-confirmed audience/use cases and factual content. No fabricated prompt volumes or invented user demand.
2. Inspect content for explicit, concise answers, descriptive headings, complete context, definitions, differentiators, supporting factual references and accessibility in server-delivered/rendered text.
3. Correct entity identity/terminology and source attribution across public pages. Clarify brand/product names, factual authority, authorship and last-updated dates **only when verifiable**; do not invent qualifications, testimonials, reviews, numerical evidence or rankings.
4. Improve answer discoverability with relevant Q&A/FAQ sections **only where a real user need and supported answer exist**. Never mass-produce doorway pages or fake FAQs. Use valid structured data only when eligible and faithful to visible content; FAQ schema is not a universal visibility shortcut.
5. Reuse SEO's canonicals, internal links, HTML renderability and crawling controls. Review applicable bot/robots policies without weakening privacy or permitting unwanted collection. Do not assume `llms.txt`, special AI schema, or opening all AI crawlers is necessary; any crawler-access changes require intent/privacy review.
6. If access is available and authorized, compare a reproducible sample of relevant question prompts and retrieved AI answer references, naming engine, market, locale, date and method. These are observations, **not guarantees**; never fabricate citations or percentages. External paid model queries, production probes or browser work are not automatically authorized merely by this stage. Browser use stays limited to UAT/UAT Fix unless separately authorized.
7. Implement safe source/code/content improvements, run permitted static checks, record affected acceptance cases for later explicit UAT, and report specific before/after evidence and remaining unknowns. Substantive new marketing claims or policy changes need owner approval.

## Canonical deliverables and status

Produce `AEO_GEO_AUDIT_REPORT.md`, `AEO_GEO_REMEDIATION_REPORT.md`, and `AEO_GEO_CHECKLIST.md`; for NOT APPLICABLE create an applicability note/handoff and mark the deliverables N/A explicitly. Every applicable item must have PASS / FAIL / BLOCKED / NOT_APPLICABLE, affected URLs/templates, source evidence, changes and retest.

Check list:
- AG-01 Public answer intent and question mapping
- AG-02 Crawlable/indexable canonical source and alignment with SEO
- AG-03 Clear direct answers with useful full context
- AG-04 Explicit verifiable entities, brand and product identity
- AG-05 Transparent provenance, authorship and supporting sources where appropriate
- AG-06 Factual accuracy, dates and claim substantiation
- AG-07 Semantic content hierarchy and machine-readable HTML
- AG-08 Natural language and relevant real FAQs without fabricated demand
- AG-09 Internal link / contextual navigation paths to supporting pages
- AG-10 Accurate eligible structured data without unsupported rich-result promises
- AG-11 Localization/market/language consistency
- AG-12 Accessibility and content availability without UI-only interaction
- AG-13 Privacy, crawler and AI-access policy alignment
- AG-14 Independent answer/citation observation (only when authorized and measurable)
- AG-15 Revalidation, functional regression, residual blockers and next action

Show `NOT MEASURED` as a measurement limitation, not a fabricated success or failure. Priority: factual accuracy and crawlability before optional presentation refinements. AEO/GEO cannot be COMPLETED with unresolved confirmed critical issues; record BLOCKED/PARTIALLY DELIVERED instead. Feed relevant items into `PHDK_COMMITMENTS.md` and `PHDK_COMPLETION_AUDIT.md`.

## Historical handoff

Use `docs/phdk/lifecycle/<run-id>/67-aeo-geo/HANDOFF.md` with snapshots of the audit, checklist, remediation, test evidence and updated ledger. Check validates SEO and AEO/GEO gates or their grounded NOT APPLICABLE decisions before beginning. Preserve historical snapshots and stage status board.

## Grounding references

- Google Search Central, “Optimizing your website for generative AI features on Google Search”: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google Search Central, “AI features and your website”: https://developers.google.com/search/docs/appearance/ai-features
- Bing Webmaster Guidelines: https://www.bing.com/webmasters/help/bing-webmaster-guidelines-30fba23a
