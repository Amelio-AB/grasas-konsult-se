# Architecture & Project Decisions

## DEC-001 – Product scope
Decision: Engströms Admin byggs först som en single-company implementation för Engströms Konsulter AB.
Reason: Minimera komplexitet och få ett välfungerande verkligt system innan eventuell generalisering.
Status: APPROVED

## DEC-002 – Accounting boundary
Decision: Hogia är fortsatt bokförings-/ekonomisystem. Engströms Admin fokuserar initialt på offert och fakturaunderlag/dokumentflöde.
Reason: Vi ska inte oavsiktligt bygga ett eget bokföringssystem.
Status: APPROVED

## DEC-003 – Production hostname
Decision: `admin.engstromskonsulter.se` används som planerad produktionssubdomän.
Reason: Systemet omfattar mer än fakturor och kan växa med fler interna adminfunktioner.
Status: APPROVED

## DEC-004 – Application framework
Decision: Next.js App Router + TypeScript.
Reason: Ger server-first fullstackstruktur, tydlig routing och bra stöd för Supabase SSR.
Status: APPROVED

## DEC-005 – Backend/database
Decision: Supabase PostgreSQL + Auth + Storage där respektive fas kräver det.
Reason: Samlad databas/auth/storage med PostgreSQL, RLS och bra stöd för Next.js.
Status: APPROVED

## DEC-006 – Database change management
Decision: Databasschema ändras genom versionshanterade Supabase migrations.
Reason: Reproducerbar lokal/test/produktion och spårbara schemaändringar.
Status: APPROVED

## DEC-007 – Dependency strategy
Decision: Undvik tunga abstraktionslager och ORM i första versionen om de inte löser ett konkret problem.
Reason: Supabase/Postgres är redan datalagret; extra lager kan skapa onödig komplexitet i ett litet system.
Status: APPROVED

## DEC-008 – Admin UX
Decision: Svenska användartexter, få val, stora tydliga handlingar och server-first formulärflöden.
Reason: Primär användare ska inte behöva teknisk vana.
Status: APPROVED

## DEC-009 – Supabase Auth som enda identitetskälla
Decision: Supabase Auth används för autentisering. Ingen egen lösenords- eller credential-tabell byggs.
Reason: Minskar säkerhetsrisk, kodmängd och ansvar för credential-hantering.
Status: APPROVED

## DEC-010 – Ingen publik registrering
Decision: Engströms Admin har ingen publik signup i MVP. Användare provisioneras genom kontrollerad administrativ rutin.
Reason: Systemet är ett internt verktyg med få användare. Publik registrering skapar onödig attackyta och UX-komplexitet.
Status: APPROVED

## DEC-011 – Profiles + aktiv admin
Decision: `public.profiles` kopplas 1:1 till `auth.users`. Adminåtkomst kräver både giltig Auth-session och en aktiv profil med tillåten roll.
Reason: Separerar identitet från applikationsbehörighet och gör det möjligt att spärra en användare utan att bygga egen autentisering.
Status: APPROVED

## DEC-012 – Proxy är inte authorization boundary
Decision: Next.js Proxy används för sessionsuppdatering och redirects, men skyddad data verifieras även server-side och genom PostgreSQL RLS.
Reason: Proxy är användbart för routing/UX men ska inte vara enda säkerhetslagret.
Status: APPROVED
