function onFormSubmit(e) {
  const CONFIG = {
    PREFIX: "CVUT StG-26-",
    UPLOAD_FORM_LINK: "https://forms.gle/sDYzU2WYTvFtVZfq9",
    SUBJECT_DUPLICATE: "[CVUT StG] Duplicate submission detected",
    SUBJECT_NEW: "[CVUT StG] Your Submission ID + upload link",
    SIGNATURE: "Best regards,<br>CVUT Starting Grant Team"
  };

  const sheet = e.range.getSheet();
  const row = e.range.getRow();
  
  const headers = getHeaders(sheet);
  const columns = getColumnIndices(headers);
  
  if (!columns.email || !columns.submissionId) return;

  const email = getNormalizedEmail(sheet, row, columns.email);
  const duplicateInfo = checkForDuplicate(sheet, row, columns.email, email);

  if (duplicateInfo.isDuplicate) {
    handleDuplicateSubmission(sheet, row, columns, duplicateInfo, email, CONFIG);
  } else {
    handleNewSubmission(sheet, row, columns, email, CONFIG);
  }
}

function getHeaders(sheet) {
  return sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
}

function getColumnIndices(headers) {
  return {
    email: headers.indexOf("Email Address") + 1,
    submissionId: headers.indexOf("SubmissionID") + 1,
    dupNote: headers.indexOf("DuplicateNote") + 1
  };
}

function getNormalizedEmail(sheet, row, emailCol) {
  return String(sheet.getRange(row, emailCol).getValue()).trim().toLowerCase();
}

function checkForDuplicate(sheet, row, emailCol, email) {
  if (row <= 2) return { isDuplicate: false };

  const emailRange = sheet.getRange(2, emailCol, row - 2, 1)
    .getValues()
    .flat()
    .map(v => String(v).trim().toLowerCase());

  const firstIndex = emailRange.indexOf(email);
  
  return {
    isDuplicate: firstIndex !== -1,
    firstRow: firstIndex !== -1 ? firstIndex + 2 : null
  };
}

function handleDuplicateSubmission(sheet, row, columns, duplicateInfo, email, config) {
  const originalId = sheet.getRange(duplicateInfo.firstRow, columns.submissionId).getValue();

  sheet.getRange(row, columns.submissionId).setValue(originalId);
  
  if (columns.dupNote) {
    sheet.getRange(row, columns.dupNote).setValue("Duplicate email — reused original SubmissionID");
  }

  sendDuplicateEmail(email, originalId, config);
}

function handleNewSubmission(sheet, row, columns, email, config) {
  const seq = row - 1;
  const submissionId = config.PREFIX + String(seq).padStart(3, "0");

  sheet.getRange(row, columns.submissionId).setValue(submissionId);
  sendNewSubmissionEmail(email, submissionId, config);
}

function sendDuplicateEmail(email, originalId, config) {
  MailApp.sendEmail({
    to: email,
    subject: config.SUBJECT_DUPLICATE,
    htmlBody: `We already have a submission from this email.<br><br>
               Your Submission ID is: <b>${originalId}</b><br><br>
               If you intended to update your submission, please reply to this email.<br><br>
               ${config.SIGNATURE}`
  });
}

function sendNewSubmissionEmail(email, submissionId, config) {
  MailApp.sendEmail({
    to: email,
    subject: config.SUBJECT_NEW,
    htmlBody: `Thank you for your application.<br><br>
               Your Submission ID: <b>${submissionId}</b><br><br>
               Please upload your documents using this link:<br>
               ${config.UPLOAD_FORM_LINK}<br><br>
               In the upload form, enter your Submission ID exactly as shown above.<br><br>
               ${config.SIGNATURE}`
  });
}