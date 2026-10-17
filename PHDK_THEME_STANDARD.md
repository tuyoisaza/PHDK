# PHDK Theme Tokens & Template Editor Standard

## Applicability and authority
Normative for every PHDK-managed product with a user-facing interface, including brownfield applications. API-only and genuinely non-visual projects document NOT APPLICABLE with source evidence. The authority model follows ADMIN_CONSOLE_STANDARD.md: multi-tenant super_admin manages global templates, while single-tenant admin manages application templates; never invent a redundant superadmin role. This supplements PHDK_DESIGN_SYSTEM.md, PHDK_UX_UI.md, CRUD_STANDARD.md, PHDK_DESIGNER_MODE.md and PHDK_CHECK.md without changing execution or browser permissions.

## Invariants: one palette contract, three presets
- A single canonical CSS token stylesheet contains the light, dark and corporate preset color values. Teams may keep layout/component CSS modular, but may not redefine brand/semantic theme palettes in route-specific styles, component files, inline styles, or independent second token sources.
- Use semantic names at least --background, --foreground, --primary, --primary-foreground, --accent, --muted, --border, --ring and --popover, with any role/status tokens the product needs. Each preset defines the same token contract; shared components use var(...) or framework aliases that resolve to these tokens. Theme switching must not require rebuilding or hand-editing screens.
- Framework-specific selectors (such as :root, .dark, or [data-theme="corporate"]) are allowed when declared in the repository's phdk-theme.config.json and proven to apply to the same component tree. Do not mandate a Tailwind migration.
- No hardcoded visual palette values in in-scope component CSS, JSX/TSX inline style literals, Tailwind arbitrary-color utilities or route overrides. Exception: essential non-theme data visualization colors, third-party assets, user-generated brand colors, SVG artwork, and similar documented cases. Every exception has a precise path/value and reason; broad ignores are forbidden.
- Corporate is a complete editable preset even when hidden from ordinary users. The corporate visibility flag only controls availability in user-facing theme selection. It must not delete corporate values or hide the preset from authorized platform administrators. When disabling corporate, choose a deterministic safe fallback for sessions currently using it; persist the user's valid light/dark choice.
- Preserve accessibility and brand: WCAG 2.2 AA contrast for applicable controls/text/states, keyboard interactions, focus visibility, reduced motion behavior and color independence of meaning; check all three presets across their actual applicable surfaces.

## Mandatory platform administrator feature
Every administered UI product with an authenticated authorized platform administrator must expose **Configuración → Edición de templates** (localized equivalents allowed). It includes:
1. Clearly separated **Claro**, **Oscuro** and **Corporativo** presets with previews based on real shared components.
2. Editing semantic color values, controlled save, server-side validated values, persisted revisions, cancel/reset to safe defaults, and meaningful success/error feedback. Updating a preset propagates to all consuming screens without code edits. Do not implement separate per-page color fields.
3. Explicit **Mostrar tema corporativo** toggle. Disabling hides the option in the ordinary theme selector while keeping it editable to the authorized platform administrator, and provides deterministic fallback for existing corporate sessions.
4. Server-enforced platform-admin-only mutation permissions and tenant scoping where applicable; server-side schema validation, safe CSS value handling (reject arbitrary CSS injection), audit of changes and non-secret history. Do not rely on hiding the route/client button for authorization.
5. Atomic persistence, cache revalidation and hydration-safe application; a reload/new authorized session must reflect saved colors and visibility without a flash of a different theme. Respect deployed tenancy, accessibility and existing security restrictions.

For an intentional UI product without an authenticated administrative surface, classify applicability and request a product/authorization decision; do not silently create a privileged role or claim full compliance. Static sites with no mutable back end require a documented decision on editor/persistence architecture before implementation, not a fake form.

## Concrete project contract
The project root owns phdk-theme.config.json, an auditable inventory (not a permission grant), including:
- token_css: relative path to the one canonical CSS palette stylesheet.
- selectors: exact selector per light, dark and corporate preset (e.g. :root, .dark and [data-theme="corporate"]).
- editor_route: authorized administrator navigation route for template editing.
- editor_source: source file that implements the real editor.
- runtime_source: source file implementing theme loading/application and corporate availability.
- corporate_visibility_setting: actual persisted setting key, for example theme.corporate.enabled.
- tests: paths named switching, persistence, visibility, authorization to executable, meaningful test cases.
- exceptions (optional): narrowly scoped objects with file, value and reason for legitimate fixed visual colors.

Example (adapt paths to the actual project):

    {
      "token_css": "src/styles/theme-tokens.css",
      "selectors": {"light": ":root", "dark": "[data-theme='dark']", "corporate": "[data-theme='corporate']"},
      "editor_route": "/admin/settings/templates",
      "editor_source": "src/app/admin/settings/templates/page.tsx",
      "runtime_source": "src/providers/theme-provider.tsx",
      "corporate_visibility_setting": "theme.corporate.enabled",
      "tests": {
        "switching": "tests/themes/switching.test.tsx",
        "persistence": "tests/themes/persistence.test.tsx",
        "visibility": "tests/themes/visibility.test.tsx",
        "authorization": "tests/themes/authorization.test.ts"
      },
      "exceptions": []
    }

The source paths/test names must refer to real files. A config file, selectors, placeholder components, or present-but-unexecuted tests alone are not functional proof.

## Enforceable scan and validation
Run the vendored script from the project root:

    python phdk-standards/scripts/phdk_theme_audit.py --root . --json

- The script checks presence and declared parity of light/dark/corporate semantic CSS tokens, editor and runtime source paths, the corporate visibility key and required test paths. It searches application source for obvious fixed colors outside the canonical token CSS and reports file:line evidence. Its findings are minimum signals, NOT a complete CSS/AST audit: indirect hardcodes, custom properties, compiled CSS, dynamic runtime behavior and visual contrast require further review.
- Resolve findings at their shared-token/component origin before manually patching pages. If truly exempt, use an exact file+value+reason exception; do not globally turn off the scan or mass-exempt legitimate debt.
- During implementation/Designer, run the static scan and the actual product's test suite. During scoped UAT/UAT Fix exercise three-theme switching, representative public/app/admin routes, saved colors after reload, corporate hide/show and fallbacks, authorization denial, bad-value rejection, cross-tenant protection, and contrast/focus states. Record test command/result, files, paths, rendered evidence if permitted and residual gaps.
- During PHDK Check, run or read equivalent scanner evidence and inspect the actual source + executable tests. Classify missing centralization, editor, setting, privilege checks, persistence, selector propagation or tests as GAP/PARTIAL according to evidence. UNVERIFIED is not COMPLIANT; a static pass or checkmark is not proof of functional behavior. Audit stage is read-only and must not modify the product without the user-approved remediation phase.
- For legacy apps, inventory current hardcoded colors and duplicated palettes and migrate incrementally to the same semantic contract. Mark incomplete or blocked work explicitly; never call all three themes compliant merely because their names appear in code.

## Acceptance matrix
A theme feature is COMPLETE only when source scan, real backend/editor permission tests, persistence tests, user theme switching and corporate visibility/fallback verification pass for the current candidate, and permitted visual accessibility checks are documented. A known missing test or unavailable browser remains UNVERIFIED/BLOCKED rather than fabricated PASS.
