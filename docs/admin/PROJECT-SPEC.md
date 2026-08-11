# Engströms Admin – Project Specification

Status: PHASE 0 APPROVED

## Purpose
A private, easy-to-use admin application for Engströms Konsulter AB to maintain customers, create quotes, convert quotes into invoice drafts, create/finalize invoices, generate PDFs and manually follow document/payment status.

## Intended user
A user with low technical experience. The interface must therefore be simple, Swedish, forgiving for drafts and strict around irreversible financial actions.

## Recommended production address
`admin.engstromskonsulter.se`

Rationale: broad enough for customers, quotes, invoices and future internal functions. `faktura.` would incorrectly suggest the system only handles invoicing.

## Proposed stack
- Next.js + TypeScript
- Supabase Postgres
- Supabase Auth
- Supabase Storage where needed
- Row Level Security
- Git/GitHub
- Deployment platform compatible with Next.js and custom domain

## Core modules
1. Authentication
2. Dashboard
3. Company settings
4. Customers
5. Quotes
6. Quote PDF
7. Invoices
8. Quote-to-invoice conversion
9. Invoice PDF
10. Audit/history

## Non-goals for v1
- bookkeeping ledger
- payroll
- VAT reporting/accounting declarations
- bank reconciliation
- automatic payment matching
- full Hogia replacement
- multi-tenant SaaS

## Core principle
Treat the product as a document/workflow application around structured business data, not as a PDF generator.
