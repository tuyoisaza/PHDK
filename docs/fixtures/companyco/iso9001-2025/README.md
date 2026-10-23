# Company Co quality-management importer corpus

Optional fictional sample documents for testing a document importer. The business content is in Spanish (`es-CO`), dated as of **2025-12-31**, and based on PHDK's [canonical Company Co reference](https://github.com/tuyoisaza/PHDK/blob/b3c39ee4b918ea3a6015005d621a9dae5469c4cf/USE_COMPANY_CO_INFO_FOR_DEMOS.md).

The dossier uses the historical reference **ISO 9001:2015 with Amendment 1:2024**. It is a simulation, not evidence of actual certification or a copy of the ISO standard. The files are sample content, not agent instructions or PHDK policy.

## Start here

| Input route | Contents | Use |
|---|---|---|
| [Individual PDFs](01_PDF_para_importar/) | 35 documents; 81 pages | Recommended first import; preserves document identities and cross-references. |
| [Editable Word documents](02_Word_editables/) | The same 35 logical documents | Alternative input or editing source. |
| [Consolidated Word](03_Consolidado/CompanyCo_Expediente_SGC_2025.docx) / [PDF](03_Consolidado/CompanyCo_Expediente_SGC_2025.pdf) | One 83-page dossier with all 35 documents | Single-file import and review. |
| [Additional cases](04_Casos_adicionales/) | Obsolete procedure and image-only scan | Version resolution, OCR and duplicate detection. |
| [Evaluator material](90_Control_del_evaluador/) | Guide, manifests, expected cases/relationships and synthetic staff | Expected results; keep outside business-document inputs. |

Choose **one primary input route**. Loading the PDF, Word and consolidated routes together intentionally introduces duplicates. The OCR variant repeats document `CC-RG-02` revision `01`; the obsolete `CC-PR-01` revision `02` does not replace current revision `03`.

The evaluator's [guide](90_Control_del_evaluador/Guia_del_importador.pdf) explains ten cases, including mixed date formats, a missing accent, an old revision citation, blank approval/closure fields, temporary responsibility, incomplete-year data and empty templates versus completed records. See [expected cases](90_Control_del_evaluador/casos_esperados.json) and the [document manifest](90_Control_del_evaluador/manifest_documentos.json) for machine-readable expectations.

## Coverage

- Quality manual, policy/scope, context and risk matrix, objectives/indicators, organization and master document list.
- 17 process descriptions and five procedures for document control, risks/changes, internal audits, nonconformities/corrective action and competence/knowledge.
- Completed sales/design, purchasing/receiving, installation/after-sales, audit, training and management-review records, plus two empty forms.
- A connected project example from quotation through equipment serials and an after-sales ticket; 200 fictional employee records preserve the canonical staff baseline without email addresses.

The complete published folder contains **86 original files plus this index**: 39 PDFs, 38 DOCX files, five JSON files, two CSV files and two TXT files. Consolidated versions and special cases are deliberate alternatives. No separate ZIP or second copy of the consolidated files is committed.

## Provenance and validation

The corporate source is pinned to PHDK commit `b3c39ee4b918ea3a6015005d621a9dae5469c4cf`. Existing Company Co identifiers and figures were retained. Detailed processes, events, records and narrative were generated for this simulation. **100% of the newly written narrative was generated with AI**; the AI authorship percentage of the pre-existing repository source is unknown and cannot be established from its text.

Before publication, the 35 unique document identities, 70 PDF/Word paths and SHA-256 values, revision filenames, internal document references and page counts were checked. All 172 PDF pages across the supplied alternatives were visually reviewed. The scan was confirmed to contain images with no text layer. The [verification record](90_Control_del_evaluador/Verificacion_del_conjunto.txt) records those file checks.

These checks do not establish importer behavior. **No importer execution or runtime UAT is claimed.** Expected cases are assertions for a future authorized run, not passed test results.

## Distribution

This is optional repository material. It is not listed in `PHDK_MANIFEST.txt` and is not automatically copied by `PHDK upgrade`. Links in the vendored README and Company Co reference use canonical GitHub URLs so they remain valid without a local copy of this folder. Publishing this corpus does not provision accounts, execute imports, start UAT or change any execution permission.
