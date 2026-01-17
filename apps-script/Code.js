function onFormSubmit(e) {
  const PREFIX = "CVUT StG-26-"; 
  const uploadFormLink = "https://forms.gle/sDYzU2WYTvFtVZfq9";

  const sheet = e.range.getSheet();

  // debug
  console.log("Triggered. Row: " + e.range.getRow());

  const row = e.range.getRow();
  
  // Header row is row 1; first response row is row 2 -> sequence starts at 1
  const seq = row - 1;
  const submissionId = PREFIX + String(seq).padStart(3, "0");

  // Identify columns by header names
  const headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];

  const emailCol = headers.indexOf("Email Address") + 1; // for "Collect email addresses"
  const submissionIdCol = headers.indexOf("SubmissionID") + 1;
  const dupNoteCol = headers.indexOf("DuplicateNote") + 1;

  if (!emailCol || !submissionIdCol) return;

  const email = String(sheet.getRange(row, emailCol).getValue()).trim().toLowerCase();

  // Duplicate check: search email in previous rows
  const emailRange = sheet.getRange(2, emailCol, Math.max(0, row - 2), 1).getValues().flat()
    .map(v => String(v).trim().toLowerCase());

  const firstIndex = emailRange.indexOf(email); // 0-based within emailRange
  const isDuplicate = firstIndex !== -1;

  if (isDuplicate) {
    const firstRow = firstIndex + 2; // because emailRange starts at row 2
    const originalId = sheet.getRange(firstRow, submissionIdCol).getValue();

    sheet.getRange(row, submissionIdCol).setValue(originalId);
    if (dupNoteCol) sheet.getRange(row, dupNoteCol).setValue("Duplicate email — reused original SubmissionID");

    MailApp.sendEmail({
      to: email,
      subject: "CVUT Starting Grant 2026 — Duplicate submission detected",
      htmlBody: `We already have a submission from this email.<br><br>
                 Your Submission ID is: <b>${originalId}</b><br><br>
                 If you intended to update your submission, please reply to this email.`
    });
    return;
  }

  // First submission: write ID and email it
  sheet.getRange(row, submissionIdCol).setValue(submissionId);

  MailApp.sendEmail({
    to: email,
    subject: "CVUT Starting Grant 2026 — Your Submission ID + upload link",
    htmlBody: `Thank you for your application.<br><br>
               Your Submission ID: <b>${submissionId}</b><br><br>
               Please upload your documents here:<br>
               ${uploadFormLink}<br><br>
               Enter your Submission ID in the upload form.`
  });
}