# PHDK AI Admin Standard

## Conditional activation

This standard applies only when the project actually uses an LLM/AI provider.

Treat AI as present when repository evidence shows at least one of these:

- an AI provider API-key/config variable such as `AI_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, `GOOGLE_GENERATIVE_AI_API_KEY`, or an equivalent provider key/config name;
- an enabled provider selection/model configuration;
- `packages/ai` or equivalent shared AI integration code;
- an LLM provider SDK/reference used by product code;
- a product requirement or current implementation for chat, generation, extraction, classification, assistants/agents, summarization, or another model-backed workflow.

Inspect variable names, source/configuration, and requirements. Never read or expose secret values merely to determine applicability.

If none of this evidence exists and the project intent does not call for AI, mark this standard NOT APPLICABLE. Do not scaffold AI, prompts, consumption, or provider administration preemptively.

## Required super-admin capabilities

When AI is applicable, the protected super-admin area must expose AI administration. At minimum it includes:

1. **Prompts** — manage the named AI prompt/agent definitions used by the product.
2. **AI consumption** — inspect token/cost usage, model/provider attribution, and pricing metadata required by `technical_stack.md`.

These capabilities are visible only to `super_admin` unless the project explicitly grants another administrative role. Hiding UI is not authorization; all reads/writes require server-side authorization.

## Prompts menu item and route

The super-admin navigation must contain a clear menu item labeled **Prompts**.

Use a dedicated route, preferably `/admin/prompts`, unless the existing admin routing convention requires a nested equivalent such as `/admin/ai/prompts`. The label remains **Prompts** even when nested under an AI section.

The page is not a generic key/value editor. It manages one prompt/agent definition at a time.

## Required Prompts page layout

Desktop/tablet admin layout uses two primary columns:

### Left column — prompt/agent list

Show the configured prompt/agent definitions used by the application.

Each item must have a stable identifier and human-readable name. The selected item is visibly active. The list supports loading, empty, error, and permission-denied states and remains usable with long names.

Selecting an item loads that definition into the editor without changing the selected record implicitly.

### Center/main column — editable prompt definition

For the selected prompt/agent show one editable form with, in this order:

1. **Name**
   - editable text field;
   - human-readable agent/prompt name;
   - stable machine ID is separate and must not silently change when the display name changes.

2. **Personality prompt**
   - editable multiline text area;
   - defines persona, voice, role, behavioral constraints, and stable system-level identity/instructions;
   - label must make clear that this is the personality/system layer.

3. **Execution prompt**
   - editable multiline text area;
   - defines the task/workflow instructions executed for this prompt/agent;
   - dynamic user/input data is passed separately and safely delimited, not concatenated into this field as executable instructions.

4. **Output JSON schema**
   - editable JSON/code field;
   - stores the structured output contract expected from execution;
   - must parse as valid JSON and be validated before save;
   - runtime model output must be validated against this contract before application use.

The form must clearly distinguish unsaved changes, saving, save success, validation errors, and permission errors. Do not save on mere selection changes without an explicit user action or clearly established autosave product decision.

## Data model

Each managed prompt/agent definition must have at least:

```txt
id
name
personality_prompt
execution_prompt
output_schema_json
enabled
created_at
updated_at
updated_by
version/revision
```

A project may add provider/model overrides or feature metadata when its intent requires them, but provider secrets never belong in prompt records.

Prompt definitions must be persistent application data/configuration, not hardcoded source strings for runtime behavior. A safe seed/default in source is allowed only as bootstrap data and must become admin-manageable after initialization.

## Runtime contract

Every AI workflow maps to an explicit managed prompt/agent definition.

Runtime assembly keeps these concerns separate:

```txt
personality/system instructions
+
execution/task instructions
+
isolated user/domain input
→ provider/model call
→ structured output
→ schema validation
→ application use
```

Do not merge user-controlled data into system/personality/execution instructions without delimiting and injection defenses.

The output JSON schema is the standard contract for reading model results. Invalid, malformed, or schema-nonconforming output is rejected or handled as a controlled failure; never silently coerce arbitrary model text into trusted application data.

## Prompt revisions and audit

Every change to name, personality prompt, execution prompt, output schema, enabled state, or model/provider override must create auditable evidence containing:

- actor;
- timestamp;
- prompt/agent ID;
- prior revision;
- new revision;
- field-level diff or equivalent safe before/after metadata.

Do not log provider secrets or sensitive user data. The system must make the current revision identifiable so a model execution can be attributed to the prompt revision that produced it.

## AI consumption linkage

Every tracked AI call must be attributable, when applicable, to:

- prompt/agent ID;
- prompt revision;
- feature/workflow;
- provider;
- requested/response model;
- token/cost/latency/error metrics already required by `technical_stack.md`.

The super-admin consumption view and the Prompts view use the same stable prompt/agent identity so an administrator can understand which prompt definitions drive consumption.

## Validation requirements

When AI applies, source/local verification must establish:

- protected super-admin Prompts route and navigation item exist;
- only authorized admin roles can read/update definitions;
- left-side prompt/agent list and selected-state behavior are implemented;
- editable name/personality/execution/output-schema fields exist;
- output JSON is syntax-validated before persistence;
- runtime output is schema-validated before use;
- prompt changes are revisioned/audited;
- runtime calls resolve managed definitions rather than hardcoded prompt strings;
- usage records link to prompt/agent ID and revision when applicable;
- prompt injection/indirect injection defenses from `DEVSECOPS.md` remain intact.

Browser/rendered appearance remains unverified unless separately supported by the execution scope. Verify source, authorization, form/data contracts, and permitted isolated tests.

## PHDK Check integration

`PHDK check` must detect the conditional AI trigger from repository evidence.

If AI is present, absence of any required capability in this standard is a GAP/PARTIAL finding, not NOT APPLICABLE. In particular check for:

- AI provider integration centralized through `packages/ai` or equivalent;
- token/cost observability;
- super-admin AI consumption capability;
- super-admin **Prompts** menu item/route;
- managed prompt list/editor;
- separate editable name, personality prompt, execution prompt, and output JSON schema;
- authorization, validation, revisions/audit, and consumption attribution.

If only an API-key/config name exists but no product AI feature can be established, classify applicability as UNKNOWN / DECISION NEEDED rather than creating product behavior solely from an unused secret placeholder.
