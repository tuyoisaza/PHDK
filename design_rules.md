# DESIGN_RULES.md

## Purpose

This file defines the design standards, UI rules, and UX expectations for every product built on this stack.

Every agent doing frontend, UI, UX, or design-system work must read this file before writing or modifying a component.

---

# Brand Requirements

Every product UI must show:

- project name
- logo or icon
- version number
- copy-debug-report button next to the version

## Required Locations

Brand and version must appear in:

- top-left corner of the primary app shell
- login page
- admin panel

The project name and logo must be visually consistent across public, authenticated, and admin areas.

---

# App Shell Layout

Required app shell structure:

```txt
Top-left:     logo + project name
Near logo:    version number + copy-debug-report button
Main nav:     route-based feature navigation
Main area:    page content
Footer:       optional, project-specific
Admin area:   protected, separate navigation
```

The app shell must not hide primary navigation behind unclear icons or hover-only interactions.

---

# Design System Ownership

Design tokens must live in the shared UI package or centralized theme configuration.

Components must not create private token systems.

Use centralized tokens for:

- typography
- color
- spacing
- radius
- shadows
- motion
- z-index
- component sizing

One-off styling is allowed only when the component has a clear product-specific need.

---

# Responsive Rules

Design mobile-first.

Core flows must work on:

- phone: 320px and up
- tablet: 768px and up
- desktop: 1024px and up

## Rules

- Never build desktop-only layouts unless explicitly approved.
- Navigation must collapse gracefully on mobile.
- Touch targets must be at least 44x44px.
- Do not hardcode layout widths that break with translated labels.
- Test all core flows at mobile breakpoint before marking complete.
- Horizontal scrolling is allowed only for data tables or explicitly justified cases.

---

# State Rules

Every page and every significant UI section must define these states:

- loading state — skeleton or spinner, never blank
- empty state — honest, useful, and tells the user what to do next
- error state — clear message, stable error code, and recovery action
- success state — confirmation that the action worked
- permission denied state — clear message, no sensitive details exposed

Never fill empty states with fake metrics, placeholder charts, random values, or demo data.

---

# Navigation Rules

- Use route-based navigation for all primary features.
- Avoid hash-fragment navigation for primary features.
- Active route must be visually indicated.
- Mobile navigation must be accessible through a clear toggle.
- Admin navigation must be separate from main product navigation.
- Role-based navigation items may be hidden when not permitted.
- Hidden navigation is not authorization.
- Server-side permission checks remain mandatory.

---

# Typography Rules

Use design tokens for all typography.

## Required Typography Tokens

```txt
font-size-xs
font-size-sm
font-size-base
font-size-lg
font-size-xl
font-size-2xl
font-size-3xl
font-weight-normal
font-weight-medium
font-weight-bold
line-height-tight
line-height-normal
line-height-relaxed
```

Never use one-off font sizes outside the token system unless explicitly approved.

Text hierarchy must be clear. A page should have one primary heading and a logical heading structure.

---

# Color and Theming Rules

- Define a centralized style file with light and dark mode versions.
- Use design tokens for all colors.
- Never hardcode hex values in components.
- Provide both light and dark themes.
- Never use color as the only way to communicate meaning.

## WCAG AA Contrast Minimums

- normal text: 4.5:1 contrast ratio
- large text: 3:1 contrast ratio

## Required Color Tokens

```txt
color-background
color-surface
color-border
color-text-primary
color-text-secondary
color-text-muted
color-accent
color-accent-hover
color-destructive
color-success
color-warning
color-error
```

---

# Spacing Rules

Use a consistent spacing scale based on design tokens.

```txt
space-1   4px
space-2   8px
space-3   12px
space-4   16px
space-5   20px
space-6   24px
space-8   32px
space-10  40px
space-12  48px
space-16  64px
```

Never use arbitrary spacing values outside the scale unless explicitly approved.

---

# Component Rules

- Use shadcn/ui-compatible component structure.
- Components must be composable.
- Components must not hardcode business logic.
- Every interactive component must have visible focus states.
- Buttons must have accessible names.
- Icons must not be the only source of meaning for critical actions.
- Destructive actions require a confirmation step.
- Sensitive admin actions should require a reason field.
- New UI components must be named by purpose, not appearance.

## Naming Examples

Good:

```txt
UserRoleBadge
DebugStatusPanel
AuditLogTable
```

Bad:

```txt
BluePill
BigCard
FancyBox
```

---

# Form Rules

- Every form field must have a visible label.
- Errors must be linked to their field.
- Required fields must be indicated.
- Submission feedback must be immediate.
- Submit buttons must show loading state during submission.
- Never clear a form on error.
- Preserve user input after validation failure.
- Validate on blur for individual fields where useful.
- Validate on submit for the whole form.
- Critical forms should prevent accidental navigation loss when unsaved changes exist.

---

# Accessibility Rules

Minimum baseline for every page:

- [ ] Keyboard navigation works end to end.
- [ ] Visible focus states exist on all interactive elements.
- [ ] Buttons have accessible names.
- [ ] Form fields have labels.
- [ ] Errors are programmatically linked to fields.
- [ ] Color contrast meets WCAG AA.
- [ ] Icons are not the only meaning for critical actions.
- [ ] Images have alt text unless decorative.
- [ ] Page has a logical heading structure.
- [ ] Modals and drawers are keyboard accessible.
- [ ] Escape and close actions work where expected.

---

# Admin Design Rules

Admin pages must be clear, dense, scannable, and auditable.

Admin screens may be denser than customer-facing screens, but they must remain understandable.

Every admin page must show:

- page title
- current environment
- current version
- user role
- key actions
- audit trail where relevant
- debug state where relevant

## Admin Layout Guidance

- Use tables for operational records.
- Use cards for summaries.
- Use forms for actions.
- Use detail pages for complex records.
- Avoid hiding critical admin actions inside unclear menus.

---

# Data Table Rules

Data tables must support where applicable:

- loading state
- empty state
- error state
- pagination
- sorting
- filtering
- column labels
- accessible row actions
- clear selected-row state if selection exists

Tables must not display fake rows to make the interface look populated.

For mobile, tables must either:

- scroll horizontally with clear affordance
- collapse into cards
- provide a mobile-specific list layout

---

# Chart and Dashboard Rules

Charts and dashboards must show real data only.

If no data exists, show an empty state instead of decorative sample data.

Charts must include:

- clear title
- data source or context where useful
- timeframe if time-based
- empty state
- error state
- readable labels
- accessible summary where practical

Never show:

- fake KPIs
- random trends
- placeholder charts
- demo analytics
- decorative sample dashboards in production

---

# Modal and Drawer Rules

Modals and drawers must:

- be keyboard accessible
- have a clear title
- have a clear close action
- support Escape key where appropriate
- avoid trapping users without a valid action
- preserve form state when validation fails
- confirm before discarding unsaved critical changes

Use modals for focused, short interactions.

Use pages for complex workflows.

---

# Toast and Notification Rules

Use toasts for temporary feedback only.

Do not use toasts as the only place for critical errors.

Critical errors must also appear in the relevant page, form, or section.

Notifications should be:

- short
- specific
- action-aware where useful
- dismissible where appropriate

---

# Debug UI Rules

The debug panel must show:

- current debug mode state
- debug scope
- who enabled it and when
- expiry if applicable
- copy-debug-report button
- clear warning that sensitive values are redacted in the report

Debug UI may appear only to authorized admin or developer roles.

Debug UI must never be visible to normal customer/member roles.

---

# i18n Design Rules

Design must support:

- longer translated strings without breaking layout
- locale switching without page reload where possible
- locale-aware date formatting
- locale-aware number formatting
- locale-aware currency formatting
- future right-to-left compatibility where practical

Never hardcode layout widths that assume English string length.

Avoid text embedded inside images unless there is a translated alternative.

---

# Performance Rules

- Optimize images.
- Use Next.js Image component where applicable.
- Avoid layout shift by defining image dimensions.
- Lazy load below-the-fold content where appropriate.
- Keep bundle size controlled.
- Do not import entire libraries for single utilities.
- Core pages should be usable before full JavaScript hydration where possible.

Performance must not override correctness, security, or accessibility.

---

# UX Non-Negotiables

A user must never wonder whether the system is:

- broken
- loading
- empty
- unauthorized
- missing setup
- processing an action

The interface must always communicate which state it is in.

## Never Do These

- Never show a blank page.
- Never show a spinner with no timeout handling.
- Never show an error without a recovery path.
- Never show a dashboard with fake data.
- Never hide a primary action behind hover-only UI.
- Never use mystery icons without labels for critical actions.
- Never rely on color alone to communicate meaning.

---

# Design Completion Checklist

Before marking UI work complete, verify:

- [ ] Project name/logo placement is respected.
- [ ] Version and copy-debug-report button are present where required.
- [ ] Route-based navigation is used for primary features.
- [ ] Mobile layout works at 320px and up.
- [ ] Tablet layout works at 768px and up.
- [ ] Desktop layout works at 1024px and up.
- [ ] Loading state exists.
- [ ] Empty state exists.
- [ ] Error state exists.
- [ ] Success state exists where appropriate.
- [ ] Permission denied state exists where relevant.
- [ ] No fake data is shown as real.
- [ ] Typography uses tokens.
- [ ] Colors use tokens.
- [ ] Spacing uses tokens.
- [ ] Focus states are visible.
- [ ] Forms have labels and linked errors.
- [ ] Destructive actions require confirmation.
- [ ] Admin pages show environment, version, role, and audit/debug context where relevant.
- [ ] Tables include pagination/sorting/filtering where applicable.
- [ ] Charts show real data only.
- [ ] i18n layout impact was considered.
- [ ] Critical errors are not toast-only.
- [ ] Accessibility baseline is met.

