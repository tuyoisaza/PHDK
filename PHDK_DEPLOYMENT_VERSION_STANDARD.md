# PHDK Deployment Version Endpoint Standard

## Purpose and applicability

For every PHDK-managed HTTP application or API with an existing reachable production hostname, expose a lightweight, source-backed `GET /health/version` endpoint. It tells an agent which **application artifact is actually being served**, without opening Railway, launching a browser, following UI journeys, or guessing from a GitHub merge. This is a deployment-revision check, **not** an acceptance test or a substitute for `/health` readiness, provider deployment state, or explicit `PHDK uat`.

This is a product implementation requirement applied during relevant Plan/implementation/Auto and audited by Check. PHDK itself is a standards repository, not an HTTP server. For a non-HTTP application, record NOT_APPLICABLE. For a public static SPA, implement a real JSON route using the existing host's supported static-file/route mapping; an HTML fallback is not compliant. Do not create a backend, public ingress, extra service, environment, new provider integration, or paid infrastructure merely to satisfy this standard. Report a genuine hosting limitation as GAP/DECISION REQUIRED.

## Required HTTP contract

- Method/path: **`GET /health/version`** on the real production application hostname. No authentication, cookies, query parameters, database access, login redirects, debug mode, or user/tenant context.
- Response: **HTTP 200**, `Content-Type: application/json`, `Cache-Control: no-store` (include `max-age=0` if supported). Keep the response tiny, deterministic, constant-cost, and non-mutating. No SPA `index.html`, fake success page, cached prior release, or response assembled from GitHub `main` at request time.
- JSON: use the following field names and types. Versions are strings in `MAJOR.MINOR.PATCH` form without a display-only `v`; unknown metadata is explicit `null`, never an invented value.

~~~json
{
  "version": "1.4.2",
  "phdkVersion": "2.72.0",
  "commitSha": "0123456789abcdef0123456789abcdef01234567",
  "builtAt": "2026-10-27T23:00:00Z"
}
~~~

The values above are **illustrative**, not actual deployment evidence.

- `version`: the application/service's existing authoritative release version (`package.json`, root `VERSION`, or its documented equivalent), identical to the version shown by its user-facing diagnostics widget. Never substitute the PHDK standards version.
- `phdkVersion`: the exact vendored `phdk-standards/VERSION` used by the built application, if installed; otherwise `null`. It is **not** necessarily the newest canonical upstream PHDK version.
- `commitSha`: the **full 40-character Git commit SHA that built the running artifact**, not the current branch tip fetched after deployment. On Railway GitHub-triggered deployments, `RAILWAY_GIT_COMMIT_SHA` is an appropriate provenance source when available. For a built static artifact, inject this at build time; for a server, read immutable deployment/build metadata, not source control at request time. If unavailable, use `null` and classify the exact revision UNVERIFIED.
- `builtAt`: an ISO 8601 UTC timestamp captured once at build/artifact creation; use `null` if unavailable. Do not return the request time as a build time. This field is informative, not proof of the deployed revision.

Use a single immutable version/provenance source per deploy, compatible with the project's build pipeline and runtime. Exclude environment-variable dumps, credentials, auth headers, branch credentials, stack traces, database identifiers, internal endpoints, tenant/user data and private logs. The response must be safe to expose publicly; do not rely on a browser-only or privileged diagnostics endpoint.

## Integration by application architecture

- For Express/Nest/Fastify or another backend, mount the exact route before SPA catch-all and auth/tenant middleware, while retaining ordinary perimeter protections. The route must never query a database or costly external service.
- For Next.js/other SSR frameworks, use a server route handler that returns the same contract and no-store headers; do not render an HTML page.
- For Vite/static sites, generate immutable version JSON during the build and serve it at the exact path through existing host routing. If the host cannot expose the extensionless path without an unapproved provider change, report the limitation instead of pretending `/health/version` works.
- For separately deployed public web/API services, each service's reachable hostname must identify **its own** artifact. Do not have one service claim the other service's version.
- Update the existing diagnostics report to display the same application version and SHA; the compact visible widget remains **only `vX.Y.Z`** without SHA/date, per `DEBUG_DIAGNOSTICS_STANDARD.md`.

## Cheap post-merge verification (non-UAT)

After an **authorized** value-milestone merge and the existing GitHub-connected autodeploy, or after a specific owner request to check the deployed version, an agent may make **one bounded, unauthenticated, read-only GET** to the already-known production URL:

~~~sh
curl -fsS --max-time 8 -H 'Accept: application/json' 'https://example.com/health/version'
~~~

Use the actual known domain, not the example. Verify HTTP 200, JSON content type, field/schema validity, non-cache headers, and compare `version` plus **full** `commitSha` with the expected released source version and the commit actually selected for that service's deployment. For a monorepo/service watch-path skip, compare against the commit expected for **that service**, not automatically the latest unrelated `main` SHA.

- **DEPLOYED_REVISION_CONFIRMED**: the live response matches the expected version and exact deployment commit. This proves only the revision answering this request; it does not prove full system health, all replicas, deployment-provider completion, UX, or UAT.
- **STALE_OR_DIFFERENT_REVISION**: valid response but version or SHA differs. Do not claim the new publication is live. An in-progress swap or a failed latest deployment may still serve the previous revision.
- **DEPLOYMENT_UNVERIFIED**: missing/null SHA, bad JSON, missing route, redirect to login, HTML fallback, non-200, network/TLS failure, unavailable domain, or unverified expected SHA. Record the concrete reason; GitHub merge alone is only PUBLISHED.
- If independent, already-authorized provider status later confirms the new deploy completed, **at most one additional GET** is permitted in this foreground task to resolve a transient stale result. No blind retries, polling, watchers, scheduled jobs, background tests, or browser navigation.
- Keep provider metadata, source merge, endpoint revision confirmation, `/health` readiness, and explicitly authorized UAT results as **separate evidence**. A successful GET does not start UAT Prep, UAT, UAT Fix, or any product journey.

This narrow probe permission is governed by `EXECUTION_SCOPE.md` and `PHDK_PRODUCTION_VERIFICATION.md`. It does **not** permit arbitrary application traffic or other health/API endpoints, local runtime tests, credential retrieval, provider writes, additional deployment attempts, new infrastructure, or recurring monitoring. Respect current owner exclusions and actual host restrictions.

## Source review and Check expectations

Plan/Auto must map the application's version source and deploy-SHA provenance before implementation; implement the route in the existing stack and add appropriate source tests for JSON/header, no-store, auth bypass without sensitive disclosure, missing SHA, stale revision and SPA-fallback behavior. Static/source checks are allowed; do not run local behavioral/API tests. Check audits route implementation, build provenance, source tests, schema, header and delivery evidence. For an authorized release, use the bounded GET above; a bare read-only `PHDK check` does not independently authorize live probing absent a current deployment/version check request. Record `IMPLEMENTED`, `PUBLISHED`, `DEPLOYED_REVISION_CONFIRMED` or `UNVERIFIED`, and `ACCEPTED` separately.
