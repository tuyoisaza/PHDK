# PHDK Design System Standard
## Applicability
Normative for React/Next.js user-facing PHDK apps, new interfaces and Designer Mode brownfield redesigns. Preserve actual product behavior, permissions, brand intent, diagnostics and user-approved exceptions. Use existing library equivalents if they satisfy the contracts; do not rewrite functional products only to change libraries.

## Canonical stack and compatibility
- React + Next.js + TypeScript strict, installed supported versions.
- Tailwind CSS at the existing major version; semantic CSS variables; one shared source of tokens. No mandatory Tailwind major upgrade.
- Locally owned shadcn/ui-compatible components in `packages/ui` (or documented shared equivalent): use its proportions, spacing, radii, states, and variant patterns while personalizing brand colors and typography. shadcn/ui is NOT restricted to monochrome.
- Radix UI primitives for dialogs, popovers, dropdowns, tooltips, selects and agreed interactive widgets, wrapped in project-owned components. Current shadcn CLI may default to Base UI: select/verify Radix-backed templates explicitly where used. Never mix Base UI and Radix parts within the same widget tree.
- Motion (`motion/react`) for justified mount/unmount, spring, layout and shared-element transitions. Prefer CSS transitions for simple color/hover/focus effects.
- `lucide-react` for icons through a consistent wrapper or registry; consistent 16/20/24-pixel roles, stroke weights and accessible labeling.
- `next-intl` with default `en`, `es`, `pt` catalog coverage for applicable products; preserve documented project locale exceptions and ensure fallback and locale-aware formatting.
- `light`, `dark`, `corporate` palette contracts with identical component DOM, geometry and tokens except semantic COLOR values by default. User-facing theme choices remain configurable.
- WCAG 2.2 AA applicable checks and accessible keyboard/focus behavior. Library provenance is not evidence of accessibility.

## Administrable theme settings

Where an administration console applies, `ADMIN_CONSOLE_STANDARD.md` requires **Configuración → Edición de templates / Visual templates** with preview, persist/rollback and selection of claro (light), oscuro (dark) and corporativo (corporate). Keep corporate visibility togglable. All shared components and screens must derive colors from the single centralized semantic token source; scan for hardcoded per-element/page hex/RGB/arbitrary color values that break switching and report/fix them in Designer readiness and `PHDK check`. A toggle that does not update actual rendered components is a GAP, not a functioning theme.

## Single source of truth
Recommended arrangement, adaptable to existing equivalent structures:
```text
packages/design-tokens/src/{tokens,themes,motion}.css
packages/ui/src/components/{button,icon-button,dialog,popover,dropdown-menu,tooltip,select,input,card,...}.tsx
packages/ui/src/{icons/index.tsx,motion/presets.ts,providers/theme-provider.tsx,index.ts}
apps/web/app/globals.css  # import shared styles, no duplicate theme definitions
apps/web/messages/{en,es,pt}.json
```
Use semantic properties `--background`, `--foreground`, `--primary`, `--primary-foreground`, `--accent`, `--muted`, `--border`, `--ring`, `--popover`, and role-specific status colors. Base tokens define spacing, radius, typography, elevation, density, icon sizes, motion durations and easing. The same components consume tokens in every theme; no copy-pasted CSS by theme. Product-specific accent palettes can be rich and colorful while preserving usable contrast. Avoid inline hardcoded brand hex values and ad hoc arbitrary Tailwind values in screens.


## Mandatory theme governance (all UI products)
The detailed, vendor-shipped contract in PHDK_THEME_STANDARD.md is normative: one central CSS palette token stylesheet, parity across light/dark/corporate, no hardcoded component palette colors, and a persisted Superadmin Configuración → Edición de templates editor with a separate corporate visibility setting. Run scripts/phdk_theme_audit.py for static evidence, then test the actual editor, security, propagation and persistence. Static-pass is never runtime compliance; existing CSS frameworks may retain equivalent selectors by declaring them in phdk-theme.config.json. Designer Mode and PHDK Check must enforce this contract.

## Component contracts
- Shared `Button`: primary/secondary/outline/ghost/destructive/link variants and sm/default/lg/icon sizes; loading, disabled, focus, pointer/keyboard states. All icon-only actions have accessible names. No page-local replacement when shared variants exist.
- Shared Radix-based `Dialog`, `Popover`, `DropdownMenu`, `Tooltip`, `Select`: focus placement/restoration, escape, portals/z-index, trigger behavior and positioning all verified. Do not hand-roll interactions already covered by primitives.
- Cards, forms, navigation, badges, tabs, tables, alerts and notifications use central components, with explicit accessible states and responsive variants.
- Icon wrappers enforce consistent size, stroke, semantic intent and aria-label/title behavior. Icons must not obscure important meaning.
- Component variants originate in the shared package, not individual pages. New patterns first extend the catalog, then pages consume them. Do not duplicate CSS reset, Tailwind setup, theme provider or component style definition across routes.

## Motion contract
Centralize presets `enter`, `exit`, `hover`, `press`, `spring`, `layout`; define duration and easing tokens. Use e.g. ease-out for entrances, ease-in for exits, ease-in-out for state transitions; spring only where meaningful. Coordinate Radix `data-state` with Motion presence carefully; ensure focus and dismissal remain correct. Respect `prefers-reduced-motion`, SSR/hydration, animations in virtualized tables and performance under lower-powered devices. Never animate everything or use motion to disguise slow behavior.

## Designer Mode readiness — mandatory BEFORE design recommendations
Upon explicit `PHDK designer mode` invocation, complete normal PHDK preflight, then **Design System Readiness**:
1. Discover installed frontend framework versions, package manager, Tailwind version/config, component sources, icon libraries, Motion dependency, Radix primitive implementation, shadcn component implementation style, CSS import graph, accessibility tooling, theme state/persistence, i18n config/catalogs, design tokens, user-facing routes and deployment/test restrictions.
2. Check the actual source/lockfile, not package names guessed from docs. Record READY / MISSING / CONFLICT / LEGACY / BLOCKED / NOT APPLICABLE for each requirement, with file/version evidence and proposed remedy.
3. Detect duplicate buttons, hardcoded colors, inconsistent radius/spacing, multiple icon libraries, ad hoc animations, duplicated theme providers, conflicting primitive engines, incomplete locales, dark/light/corporate style drift, inaccessible dialogs and mobile breakpoints.
4. Generate/update `DESIGN_SYSTEM_READINESS.md` with inventory, compatibility matrix, exact dependencies/versions, gaps, risks, priority, repair plan, deliberate exceptions and checks; show a concise status summary before design recommendations.
5. Prepare the existing project **before proposing visual redesigns**: safely normalize missing shared tokens/components, wrapper contracts and compatible dependencies when already authorized as part of the mode; otherwise mark explicit blockers and avoid incompatible proposals. Installing packages must follow existing repo/host authorization and security policy. Do not claim installed until verified.
6. Only after readiness evaluation and bounded preparation, produce `DESIGNER_BASELINE.md`, `DESIGNER_DIRECTION.md`, implement aesthetic and UX improvements using shared components, and create `DESIGNER_CHANGELOG.md`/`DESIGNER_REVIEW.md`. Browser/screenshots only in scoped UAT/UAT Fix.
7. Acceptance: no undisclosed incompatible primitive mixes, duplicate theme systems or unsupported dependency changes; automated lint/typecheck/build and focused accessible behavior tests where feasible; evidence-based remaining blockers. No fabricated render observations.

## Designer delivery gate

Apply mandatory closure and tooling failure recovery from `PHDK_DESIGNER_MODE.md` and `MAIN_DELIVERY_STANDARD.md`; readiness evidence cannot substitute for delivered changes.

## Design-system change policy
Require architecture decision for changing primitive engine, framework, adding a second design system or introducing incompatible theme architecture. Preserve documented exceptions, security restrictions, i18n and the always-visible debug/version widget required by `DEBUG_DIAGNOSTICS_STANDARD.md`. Use existing PHDK version/commit/PR/merge-to-main controls.

## References
- https://ui.shadcn.com/docs/theming
- https://ui.shadcn.com/docs/components
- https://www.radix-ui.com/primitives
- https://motion.dev/docs/react
- https://tailwindcss.com/docs/theme
- https://lucide.dev/guide/packages/lucide-react
- https://next-intl.dev/docs/getting-started/app-router
- https://www.w3.org/TR/WCAG22/
