# Submission workflow (Google Workspace)

## Goal
Accept external applications with required email, generate a unique Submission ID, and collect files via a separate upload form.

## Components
### Form A — Application (metadata)
- Collects applicant details + **Email Address (required)**
- Responses are stored in **Google Sheet A**

### Google Sheet A — Submission registry
- Stores Form A responses and system-managed fields:
  - `SubmissionID`
  - `DuplicateNote` (optional)

### Apps Script (bound to Sheet A)
Trigger: **On form submit** (from spreadsheet)

Logic:
1. Read the submitted email (normalized to lowercase).
2. Check whether this email already exists in prior rows.
3. If duplicate:
   - reuse the original `SubmissionID`
   - record `DuplicateNote`
   - email applicant a “duplicate submission detected” notice
4. If new:
   - generate `SubmissionID` (e.g., `CVUT StG-26-004`)
   - write it into the response row
   - email applicant:
     - Submission ID
     - link to Form B (uploads)
     - instructions to enter Submission ID in Form B

### Form B — Upload documents
- Uses **File upload** questions (requires Google sign-in by Google design)
- Contains required fields:
  - Email address (verified recommended)
  - Submission ID (from email)

## Applicant journey
1. Submit Form A.
2. Receive email with Submission ID + Form B link.
3. Upload documents via Form B and enter Submission ID.

## Operational notes
- “Duplicate submission” is detected using **email as the unique key**.
- Keep code and documentation in GitHub; do not store applicant data in the repo.