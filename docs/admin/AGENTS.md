# Codex / AI Development Rules – Engströms Admin

## Mission
Build a very simple, safe Swedish admin tool for Engströms Konsulter AB for customers, quotes and invoice preparation.

## Phase gate
Never implement a later phase while working on an earlier phase.
When a phase is implemented:
1. run tests/typecheck/lint/build,
2. summarize changed files,
3. list deviations and risks,
4. stop and await the project owner's explicit approval inside the VS Code/Codex workflow.

## Product principles
- Optimize for a non-technical end user.
- Prefer fewer choices and obvious Swedish labels.
- Do not introduce accounting features outside the agreed scope.
- Never silently change financial data.
- Financial calculations must be deterministic and centralized.
- Do not trust client-side validation for security or financial rules.

## Data principles
- PostgreSQL/Supabase is the source of truth for structured data.
- PDFs are representations/snapshots, not the primary data store.
- Historical finalized documents must preserve their own company/customer snapshots.
- Do not make finalized invoices depend on mutable customer/company records.

## Security
- Every private Supabase table must use RLS.
- Service-role credentials must never reach browser code.
- Secrets must never be committed.
- Authorization must be enforced server-side/database-side, not only hidden in UI.

## Invoice numbering
- Draft invoices do not consume final invoice numbers.
- Final invoice numbers must be allocated atomically by the database/server transaction.
- Never calculate the next number in browser JavaScript.

## UX
- Swedish UI.
- Large obvious actions.
- Confirm destructive/irreversible operations.
- Prefer archive over delete where records have history.
- Provide useful empty states and validation errors.

## Engineering quality
Before a phase can be proposed as complete:
- typecheck passes
- lint passes
- production build passes
- relevant automated tests pass
- migrations are committed
- documentation for the phase is updated

## Scope discipline
Do not add speculative features because they seem useful.
Add them to BACKLOG.md instead.
