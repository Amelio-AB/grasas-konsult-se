# Codex Start Prompt

You are implementing Engströms Admin from the repository documentation.

Read in this order before changing code:
1. PROJECT-SPEC.md
2. BUSINESS-RULES.md
3. PHASES.md
4. AGENTS.md
5. the Markdown specification for the current phase

Treat those documents as authoritative unless they conflict with security, data integrity, or an explicit newer project-owner instruction.

Start with Phase 1 only. Do not implement Phase 2 or later even if it would be convenient.

For Phase 1:
- establish the approved Next.js/TypeScript project foundation,
- establish the Supabase client/server boundaries and environment-variable pattern,
- create the reusable admin application shell without business modules,
- create quality scripts for lint/typecheck/build/tests as appropriate,
- keep secrets out of Git,
- document local setup.

At completion, do not continue automatically. Provide:
- files changed,
- commands/tests run and results,
- unresolved issues,
- architectural decisions made,
- manual verification steps.
Then stop for approval.
