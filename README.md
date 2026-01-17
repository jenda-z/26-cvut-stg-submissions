# CVUT Starting Grant — Submission System (Google Forms + Apps Script)

This repository contains the version-controlled implementation of the submission workflow:
- Form A (Application metadata) → Google Sheet registry
- Apps Script automation: generates Submission IDs, detects duplicate emails, sends confirmation email
- Form B (Document upload): collects files and links them to Submission ID

## Repo structure
- `apps-script/` — Apps Script project (synced via `clasp`)
- `docs/` — workflow and operations documentation
- `templates/` — email templates and text snippets (non-code)

## Updating the script
1. Edit in Apps Script editor or locally
2. Sync:
   - `clasp pull` (to pull editor changes locally)
   - `clasp push` (to push local changes to Apps Script)
3. Commit + push to GitHub
