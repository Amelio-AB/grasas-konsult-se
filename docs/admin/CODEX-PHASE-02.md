# Codex Prompt – Fas 2: Autentisering och adminbehörighet

Implementera ENDAST Fas 2 i Engströms Admin.

Läs först och följ dessa filer i denna ordning:
1. `docs/admin/AGENTS.md`
2. `docs/admin/PROJECT-SPEC.md`
3. `docs/admin/BUSINESS-RULES.md`
4. `docs/admin/DECISIONS.md`
5. `docs/admin/PHASES.md`
6. `docs/admin/PHASE-01.md`
7. `docs/admin/PHASE-02.md`

## Uppdrag

Bygg autentiserings- och behörighetsgrunden enligt `PHASE-02.md` med Next.js App Router, TypeScript och Supabase.

Implementationen ska minst omfatta:
- e-post/lösenord med Supabase Auth
- login/logout
- glömt lösenord och reset-password
- sessionhantering enligt aktuell Supabase SSR-metod
- `proxy.ts` där lämpligt för session-refresh/redirect
- server-side authorization utöver Proxy
- skydd av `/admin` och `/admin/*`
- `public.profiles` via migration
- adminroll och `is_active`
- RLS för profiles
- säker bootstrap-dokumentation för första admin
- relevanta auth/authorization-tester

## Begränsningar

Bygg INTE kunder, företagsinställningar, offerter, fakturor, PDF, statistik, Hogia, publik signup, social login, MFA, avancerad rollmotor eller användaradministrationssida.

Lägg framtida idéer i `docs/admin/BACKLOG.md` i stället för att implementera dem.

## Säkerhetskrav

- Lita aldrig endast på UI eller `proxy.ts` för behörighet.
- Verifiera användaren server-side vid privata resurser.
- RLS måste vara aktivt på privata tabeller.
- Klienten får inte kunna höja sin roll eller aktivera sig själv.
- Service-role/secret key får aldrig importeras i browserkod.
- Logga aldrig lösenord, auth tokens eller känsliga headers.
- Använd aktuella officiella API:er; använd inte deprecated Supabase Auth Helpers.

## UX

UI ska vara på svenska och anpassat för låg teknisk vana. Login ska vara enkelt och fel ska visas som begriplig svensk användartext.

## Migreringar

Alla databasändringar ska ligga som reproducerbara Supabase migrations i repo:t. Gör inga manuella schemaändringar utan migrationsfil.

## Innan fasen föreslås som klar

Kör och rapportera relevanta tester, lint, typecheck, production build och migrationsvalidering där möjligt.

Kontrollera särskilt anonym/aktiv/inaktiv access, RLS för profiles, att role/is_active inte kan manipuleras från klienten, logout och lösenordsåterställning.

## Slutrapport

Rapportera Implementerat, Ändrade filer, Databasmigreringar, Tester, Manuell kontroll, Risker/avvikelser och Nästa steg.

STOPPA därefter och invänta projektägarens godkännande. Implementera INTE Fas 3.
