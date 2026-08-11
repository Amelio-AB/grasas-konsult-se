# Business Rules

## BR-001 Financial calculation
Line totals, VAT totals and document totals are calculated by trusted application/database logic. The user edits inputs, never the computed final total directly.

## BR-002 Customer snapshot
When a quote/invoice is finalized or otherwise enters a defined immutable state, relevant customer data is stored with the document so later customer edits do not rewrite history.

## BR-003 Company snapshot
Finalized documents preserve relevant issuer/company data for the same reason.

## BR-004 Invoice draft
An invoice may exist as a draft without consuming a final invoice number.

## BR-005 Final invoice number
A final sequential invoice number is allocated atomically when the invoice is finalized. Browser code may never assign it.

## BR-006 Finalized invoices
A finalized invoice cannot be normally deleted or freely edited. Corrections must use an explicit correction/credit workflow defined before that feature is enabled.

## BR-007 Quote conversion
Converting a quote creates a new invoice draft and retains the original quote. The documents remain linked.

## BR-008 Status is not bookkeeping
Marking an invoice "Betald" in Engströms Admin is an internal manual workflow status unless/until a future verified integration provides payment information.

## BR-009 PDFs
Generated PDFs represent document data. The structured database record remains the source of truth.
