# Codex Prompt – Implementera Fas 1

Du arbetar i projektet Engströms Admin.

Läs först, i denna ordning:
1. `AGENTS.md`
2. `docs/00-project/PROJECT-SPEC.md`
3. `docs/00-project/BUSINESS-RULES.md`
4. `docs/00-project/PHASES.md`
5. `docs/phases/PHASE-01.md`

Implementera därefter ENDAST Fas 1 – Teknisk grund.

## Viktiga krav

- Följ aktuell stabil Next.js App Router-struktur.
- TypeScript strict.
- Använd Supabase officiella SSR-upplägg för klient/server helpers.
- Initialisera Supabase CLI-struktur och migrationsmapp, men skapa inga verksamhetstabeller.
- Skapa ett rent, responsivt admin-skal på svenska.
- `/admin` ska uttryckligen vara en oskyddad placeholder i Fas 1. Autentisering byggs först i Fas 2.
- Inga fake-kunder, offerter eller fakturor.
- Inga secrets i Git.
- Håll arkitekturen enkel.

## Scope gate

Implementera INTE:
- auth
- user roles
- protected routes
- customers
- quotes
- invoices
- PDFs
- email
- Hogia
- dashboard KPIs

Om du upptäcker att något behöver beslutas för en senare fas: lägg det i dokumentation/backlog, bygg det inte nu.

## Verifiering före stopp

Kör och rapportera:
- npm run typecheck
- npm run lint
- npm run test
- npm run build

Kontrollera även att dev-servern kan startas.

Uppdatera README med reproducerbara lokala instruktioner.

När allt är klart ska du lämna exit report enligt `PHASE-01.md` och STOPPA.

Fortsätt inte till Fas 2 förrän projektägaren uttryckligen skriver:

`GODKÄND FAS 1`
