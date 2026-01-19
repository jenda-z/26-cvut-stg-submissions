# Form A — “CVUT Starting Grant 2026: Application metadata (Form A)”

**Purpose:** online application form for metadata (portal component #1). 

## Form settings (recommended)

* **Do not** enable “Edit after submit” (clean audit trail).
* If you use “Collect email addresses”: keep it **ON** (reduces one input field), but still keep the explicit email field below if you expect applicants might submit under a different Google account than their preferred correspondence address.

## Section A0 — Intro (Description field, no questions)

**Paste as Form description:**

> This form collects minimal metadata for the CVUT Starting Grant 2026 submission portal. Full scientific content is submitted via Form B (document upload) and recommendation letters are submitted directly by referees via Form C.
> A proposal is considered submitted only after Form B is received and the portal issues an automatic confirmation with a timestamp.

(Submission definition requirement.)

## Section A1 — Applicant identity (minimal)

**Q1. Full name**

* Type: Short answer
* Required: Yes
* Help text: “As it should appear in official correspondence.”
* Validation: none

**Q2. Email for correspondence**

* Type: Short answer (email validation)
* Required: Yes
* Help text: “We will send your Submission ID and the official confirmation here.”
* Validation: Response validation → Text → Email address

**Q3. Phone (incl. country code)**

* Type: Short answer
* Required: No
* Help text: “Optional; used only if we cannot reach you by email.”
* Validation: none

## Section A2 — Proposal routing

**Q4. Project title**

* Type: Short answer
* Required: Yes
* Help text: “Must match the title in your uploaded proposal PDF.”
* Validation: none
  (Title is part of the submission package “as entered in the portal”.)

**Q5. Thematic area (organisational routing only)**

* Type: Multiple choice
* Required: Yes
* Options (exact):

  * ENG: Engineering and Technology
  * MIN: Mathematics, Informatics, and Natural Sciences
  * ASH: Arts, Social Sciences, and Humanities
* Help text: “Used only to allocate rapporteurs/expertise; it does not constrain eligible scope.”

**Q6. Intended host unit (faculty / institute)**

* Type: Dropdown
* Required: Yes
* Options: *(your maintained list)*
* Help text: “The host unit environment is described in your uploaded ‘Host environment statement’ (Form B).”
* Validation: none

**Q7. Keywords (3–5)**

* Type: Short answer
* Required: No
* Help text: “Optional; helps route external reviewers. Example: ‘robotics; corrosion; topology optimisation’.”
* Validation: Optional: response validation → Regular expression to encourage semicolons/commas (not required)

------

## Section A3 — Eligibility anchors (only what can’t be reliably inferred from PDFs)

**Q8. Date of award of your first PhD (or equivalent)**

* Type: Date
* Required: Yes
* Help text: “Used to check the 8-year eligibility window (career breaks may extend it).”
* Validation: Date must be **on or before** call deadline (optional; admin convenience)

**Q9. Do you claim an eligibility extension due to career break(s)?**

* Type: Multiple choice
* Required: Yes
* Options: “No” / “Yes”
* Help text: “If yes, you will be asked for minimal dates here and upload supporting documents in Form B.”

### Section A3b — Career breaks (conditional)

**Form logic:** If Q9 = “Yes” → go to Section A3b; else skip to Section A4.

**Q10. Career break type**

* Type: Checkbox (allow multiple)
* Required: Yes
* Options: “Maternity leave”, “Parental leave (non-maternity)”, “Other circumstances (e.g., long-term illness/injury, compulsory service)”
* Help text: “Select all that apply.”

**Q11. Total documented duration to be excluded (months)**

* Type: Short answer (number)
* Required: Yes
* Help text: “Enter the total months of career break(s) you claim. You will upload supporting documents in Form B.”
* Validation: Response validation → Number → ≥ 0 and ≤ 120 (or your preference)

## Section A4 — Required declarations (checkboxes; auditable)

**Q13. Submission limits (tick all)**

* Type: Checkboxes
* Required: Yes (use “Require a response in each row” style by splitting into separate required checkboxes if you prefer stricter enforcement)
* Items (paste exactly):

  * “I act as PI in at most one proposal in this call.”
  * “I have not previously received support under the CVUT Starting Grant.”
  * “I am not, at the time of submission, a member of the evaluation panel for this call.”

**Q14. Principles-based conditions (confirm as applicable; evidence is in uploaded docs)**

* Type: Checkboxes
* Required: Yes
* Items (paste):

  * “My PI profile documents the required international experience (as defined in the Principles).”
  * “I will be employed by CTU for project implementation at an FTE enabling effective implementation (normally 1.0), subject to grant agreement negotiations where justified.”

## Section A5 — Referees (to enable direct submission via Form C)

**Q15. Referee 1 email**

* Type: Short answer (email validation)
* Required: Yes
* Help text: “Letters must be submitted directly by referees via the dedicated link; letters uploaded by the applicant are not accepted.”
* Validation: Email address

**Q16. Referee 1 name (optional)**

* Type: Short answer
* Required: No
* Help text: “Optional; helps us address the invitation.”
* Validation: none

**Q17. Referee 2 email**

* Type: Short answer (email validation)
* Required: Yes
* Help text: *(same as Q15)*
* Validation: Email address

**Q18. Referee 2 name (optional)**

* Type: Short answer
* Required: No

**Q19. Consent / acknowledgement**

* Type: Checkbox
* Required: Yes
* Text: “I confirm the information provided is accurate and I understand that the portal will contact my referees using the emails provided.”
* Validation: none

---

# Form B — “CVUT Starting Grant 2026: Proposal upload (Form B)”

**Purpose:** secure document upload area for the full proposal and annexes (portal component #2). 

## Form settings (recommended)

* **File upload**: ON (requires sign-in).
* Store uploads in a dedicated Drive folder (CTU tenant).
* Consider enabling “Limit to 1 response” = OFF (in case applicant needs to resubmit; your script should mark latest as authoritative and log timestamps).

## Section B0 — Intro (Description field, no questions)

**Paste as description:**

> Upload the mandatory proposal package. Narrative documents must be in English and uploaded as PDF; they must comply with Annex B limits and formatting. The proposal package must include the items listed in Annexes B–D. The portal will issue the official timestamped confirmation after you submit this form.
> (English + compliance + submission definition.)

## Section B1 — Link to your application

**Q1. Submission ID**

* Type: Short answer
* Required: Yes
* Help text: “Paste the Submission ID you received after Form A (e.g., CVUT StG-26-004).”
* Validation: Response validation → Regular expression (optional): `^CVUT StG-26-\d{3}$`

## Section B2 — Mandatory uploads (Annex B–C)

*(Each is a separate file-upload question; required.)*
(Required package list.)

**Q2. Scientific project description (PDF)**

* Type: File upload
* Required: Yes
* Help text: “Max 6 A4 pages (+ references up to 2 additional pages). Use Annex B headings.”
* Validation: Allow only PDF; max 1 file

**Q3. PI profile — ERC ‘CV and Track Record’ (PDF)**

* Type: File upload
* Required: Yes
* Help text: “ERC format (Part B1), max 4 pages, use most recent ERC template applicable at call opening.”
* Validation: PDF only; 1 file

**Q4. Running projects / grant applications list (PDF)**

* Type: File upload
* Required: Yes
* Help text: “Max 1 A4 page.”
* Validation: PDF only; 1 file

**Q5. Team plan (PDF)**

* Type: File upload
* Required: Yes
* Help text: “Max 1 A4 page.”
* Validation: PDF only; 1 file

**Q6. Intended host environment statement (PDF)**

* Type: File upload
* Required: Yes
* Help text: “Max 1 A4 page.”
* Validation: PDF only; 1 file

**Q7. Budget (Annex C Excel template)**

* Type: File upload
* Required: Yes
* Help text: “Upload the completed Annex C budget template (.xlsx).”
* Validation: Allow only `.xlsx`; 1 file

## Section B3 — Supporting documents (conditional)

**Q8. Career-break supporting documentation (only if claimed in Form A)**

* Type: File upload
* Required: No
* Help text: “Only if you claimed an eligibility extension. Supporting documents must match dates listed in your ERC CV/Track Record.”
* Validation: Allow PDF/images; multiple files allowed (optional)

## Section B4 — Minimal compliance confirmations

**Q9. Format compliance**

* Type: Checkbox
* Required: Yes
* Text: “I confirm all narrative items are in English and comply with Annex templates/limits and minimum formatting; files are uploaded as PDF.”

---

# Form C — “CVUT Starting Grant 2026: Referee letter upload (Form C)”

**Purpose:** dedicated referee link for recommendation letters; **exactly two letters required**; applicant uploads not accepted. 

## Form settings (recommended)

* File upload: ON (sign-in required).
* **Prefilled link** contains SubmissionID + Token + Referee email (your Apps Script verifies; Form can’t truly “lock” fields, so verification must be server-side).

## Section C0 — Intro (Description field)

**Paste:**

> Thank you for providing a recommendation letter for the CVUT Starting Grant 2026. Exactly two letters are required and must be submitted directly by referees via this link. Letters uploaded by the applicant are not accepted. Please follow the Annex D structure (max 1–2 pages).

## Section C1 — Hidden/technical fields (prefilled)

**Q1. Submission ID**

* Type: Short answer
* Required: Yes
* Help text: “Prefilled by the system.”
* Validation: regex optional (same as Form B)

**Q2. Token**

* Type: Short answer
* Required: Yes
* Help text: “Prefilled by the system (do not change).”
* Validation: optional regex (e.g., 20–40 chars)

**Q3. Referee email**

* Type: Short answer (email validation)
* Required: Yes
* Help text: “Prefilled by the system.”
* Validation: Email address

## Section C2 — Minimal referee identity

**Q4. Referee full name**

* Type: Short answer
* Required: Yes
* Help text: “As it should appear in the letter header.”
* Validation: none

## Section C3 — COI + confidentiality (required checkboxes)

**Q5. Conflict of interest declaration**

* Type: Checkbox
* Required: Yes
* Text (paste):

  > “I confirm I have no conflict of interest that could reasonably raise doubt about impartiality (e.g., close collaboration, same organisational unit, close personal relationship, dependence/supervision, strong competition).”

## Section C4 — Upload

**Q7. Recommendation letter (PDF)**

* Type: File upload
* Required: Yes
* Help text: “Upload your letter as PDF (max 1–2 pages) following Annex D headings.”
* Validation: PDF only; 1 file