# CVUT Starting Grant 2026 – Process Maps (yEd)

This folder contains the process maps for the **CVUT Starting Grant 2026 call**, maintained as a **single source of truth** and exported to **yEd GraphML** for editing and publication.

## What’s inside

- `source/` – **authoritative data source** (nodes + edges in one CSV table)
- `scripts/` – generator that produces yEd `.graphml` views from the CSV
- `graphml/` – exported yEd diagrams (GraphML), ready to open

## Views (audience-specific diagrams)

Generated diagrams include:

1. **Applicant view** – what should appear on the call webpage (high-level, applicant-facing)
2. **Panel view** – panel chair and members workflow (evaluation phases, rapporteurs, interviews, ranking)
3. **Host unit view** – host matching and commitments during post-selection negotiations
4. **Secretariat view** – operational workflow (eligibility checks, invitations, logistics, records, negotiation administration)

## Single source of truth

The file below is the canonical definition of the process:

- `source/CVUT_StG_2026_process_source.csv`

It contains both nodes and edges in one table with these columns:

- `kind` – `node` or `edge`
- Node rows:
  - `node_id`, `label`, `type` (`task|decision|milestone`), `role` (lane), `order`, `views`
- Edge rows:
  - `source`, `target`, `edge_label`, `views`
- `views` – `all` or comma-separated list, e.g. `applicant,panel,host,secretariat,reviewers`

### Editing rules (important)
- **Never change `node_id`** once published (treat it as a stable identifier).
- Prefer changing only `label`, `views`, and edges when refining.
- Keep `order` increasing to preserve readable left-to-right flow in generated diagrams.

## How to regenerate the yEd diagrams

From the `process-maps/` directory:

```bash
python scripts/generate_yed_views.py source/CVUT_StG_2026_process_source.csv
