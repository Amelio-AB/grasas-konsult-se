# Fas 2 – Autentisering och adminbehörighet

Status: SPECIFICERAD – EJ IMPLEMENTERAD
Ägare: Engströms Admin
Fasgrind: Fas 2 får implementeras först efter att Fas 1 är godkänd i VS Code/Codex.

## 1. Syfte

Fas 2 ska etablera en säker och enkel autentiserings- och behörighetsmodell för hela Engströms Admin.

Efter denna fas ska ingen obehörig användare kunna nå privata adminsidor eller läsa/skriva privat data genom applikationen eller direkt via Supabase-klienten.

Målet är inte avancerad enterprise-IAM. Målet är en liten, robust och lättförståelig adminlösning för Engströms Konsulter AB.

## 2. Tekniska beslut

- Supabase Auth används för identitet och session.
- Primär inloggning: e-post + lösenord.
- Next.js App Router används.
- `proxy.ts` används för sessionsuppdatering och tidiga redirects där det är lämpligt.
- Proxy får aldrig vara den enda säkerhetskontrollen.
- Server-side authorization ska verifieras när skyddad data eller skyddade operationer används.
- RLS används på alla privata tabeller.
- En applikationsprofil i `public.profiles` kopplas 1:1 till `auth.users`.
- Endast uttryckligen aktiverade användare får använda adminsystemet.
- MVP har rollen `admin`.
- Arkitekturen får stödja fler roller senare, men ingen komplex rollmotor byggs nu.

## 3. Användarflöden

### 3.1 Inloggning
1. Användaren öppnar `/login`.
2. E-post och lösenord anges.
3. Uppgifterna valideras server-side.
4. Supabase Auth autentiserar användaren.
5. Systemet verifierar att användarens profil finns och är aktiv.
6. Godkänd admin skickas till `/admin`.
7. Fel visas på begriplig svenska utan att avslöja känslig information.

### 3.2 Utloggning
1. Användaren väljer `Logga ut`.
2. Sessionen avslutas via Supabase Auth.
3. Användaren skickas till `/login`.
4. Privat cache/data får inte ligga kvar synligt i UI.

### 3.3 Glömt lösenord
1. Användaren väljer `Glömt lösenord?`.
2. Användaren anger sin e-postadress.
3. Systemet begär återställningsmail via Supabase Auth.
4. UI visar ett neutralt meddelande som inte bekräftar om kontot finns.
5. Återställningslänken går till en publik route, exempelvis `/auth/reset-password`.
6. Nytt lösenord sätts via ett separat formulär.
7. Efter lyckad återställning får användaren gå till login eller loggas in enligt valt säkert flöde.

### 3.4 Obehörig användare
- Besök på `/admin` utan giltig session -> redirect `/login`.
- Inloggad användare utan aktiv adminprofil -> nekas adminåtkomst.
- Direkt API-/databasåtkomst via browserklient ska stoppas av RLS.
- Skyddad server action/route handler ska verifiera användaren innan operation.

## 4. Datamodell

### `public.profiles`

```sql
id uuid primary key references auth.users(id) on delete cascade,
email text,
display_name text,
role text not null default 'admin',
is_active boolean not null default false,
created_at timestamptz not null default now(),
updated_at timestamptz not null default now()
```

Regler:
- `id` ska alltid motsvara `auth.users.id`.
- `role` får i MVP endast använda tillåtet värde `admin`.
- `is_active = true` krävs för åtkomst till adminsystemet.
- E-post i `profiles` är presentations-/administrationsdata. `auth.users` är källan för autentisering.
- Ingen klient får kunna uppgradera sin egen roll eller aktivera sitt eget konto.

## 5. Kontoskapande

Publik registrering ska INTE finnas i MVP.

Nya användare skapas/inbjuds av behörig administratör genom kontrollerad process, initialt via Supabase Dashboard eller dokumenterad administrativ rutin.

Det betyder:
- ingen `/signup`
- ingen knapp `Skapa konto`
- ingen automatisk profil med aktiv adminbehörighet från publik klient

## 6. Routes

Publika routes:
```text
/login
/auth/forgot-password
/auth/reset-password
/auth/callback
```

Skyddade routes:
```text
/admin
/admin/*
```

## 7. Session och server-side kontroll

Skapa separata Supabase helpers för browser och server. `proxy.ts` får användas för session-refresh och UX-redirects, men säker åtkomst till data ska dessutom kontrolleras server-side/RLS.

## 8. RLS

RLS ska aktiveras på `public.profiles` redan i denna fas.

Grundprincip:
- anonym användare: ingen läs-/skrivåtkomst
- autentiserad aktiv admin: får läsa sin egen profil
- vanlig browserklient: får inte ändra `role` eller `is_active`
- administrativ användarhantering sker genom separat säker server/admin-process

Ingen privat tabell får lämnas oskyddad tillfälligt.

## 9. UI/UX

Login ska vara extremt enkel, svensk, tangentbordsanvändbar och utan tekniskt Supabase-språk. Adminheadern ska visa namn/e-post och `Logga ut`.

## 10. Felmeddelanden

Tillåtna exempel:
- `E-post eller lösenord är fel.`
- `Du har inte behörighet till adminsystemet.`
- `Det gick inte att logga in. Försök igen.`
- `Om adressen finns registrerad skickas ett återställningsmail.`

Råa Supabase-fel, stack traces och account-enumeration får inte exponeras.

## 11. Säkerhetsregler

- Service-role/secret keys får aldrig importeras i client components.
- Ingen autentisering baserad endast på localStorage.
- Ingen klientstyrd rollkontroll får vara auktoritativ.
- Skyddade server actions ska kontrollera session och behörighet.
- RLS ska fungera även via Supabase REST/API utanför UI:t.
- Redirect-url för lösenordsåterställning ska allow-listas i Supabase.
- Produktionsdomän: `https://admin.engstromskonsulter.se`.
- Inga auth tokens, lösenord eller känsliga headers får loggas.

## 12. Lösenordspolicy

För MVP rekommenderas minst 12 tecken för administratörer. Använd Supabases inbyggda credential-hantering; bygg ingen egen lösenordsalgoritm eller credential-tabell.

## 13. Ingår i Fas 2

- Supabase Auth-konfiguration
- login/logout
- glömt lösenord och nytt lösenord
- `profiles` migration
- adminroll + aktiv/inaktiv status
- RLS för profiles
- protected `/admin`
- server-side auth helper
- sessionshantering
- auth/authorization-tester
- svenska fel-/tomlägen
- bootstrap-rutin för första admin

## 14. Ingår INTE i Fas 2

- kundregister
- företagsinställningar
- offerter
- fakturor
- PDF
- Hogia
- dokumentutskick via e-post
- publik registrering
- social login/SSO
- avancerad RBAC
- MFA
- användaradministrations-UI

## 15. Bootstrap – första admin

1. Skapa användaren i Supabase Auth via Dashboard/adminverktyg.
2. Skapa motsvarande `public.profiles`-rad.
3. Sätt `role = 'admin'`.
4. Sätt `is_active = true`.
5. Verifiera login.
6. Verifiera RLS.
7. Byt initialt lösenord om temporärt lösenord använts.

Ingen bootstrap-hemlighet får lämnas i repo:t.

## 16. Tester

Verifiera minst:
- korrekt konto kan logga in
- fel lösenord nekas
- logout avslutar session
- återställningsformulär accepterar giltig e-postsyntax
- anonym användare redirectas från `/admin`
- aktiv admin får åtkomst
- inaktiv användare nekas
- anonym klient kan inte läsa `profiles`
- användare kan inte ändra egen `role` eller `is_active`
- lint/typecheck/test/build passerar

## 17. Manuell granskning

Projektägaren ska kontrollera login desktop/mobil, fel lösenord, logout, direktlänk till `/admin`, glömt/nytt lösenord, inaktiv användare, adminheader och att inga råa tekniska fel visas.

## 18. Acceptanskriterier

- [ ] Publik signup finns inte.
- [ ] Login med e-post/lösenord fungerar.
- [ ] Logout fungerar.
- [ ] Lösenordsåterställning fungerar end-to-end.
- [ ] `/admin` och underliggande routes skyddas.
- [ ] Inaktiv/icke-admin användare nekas adminåtkomst.
- [ ] `public.profiles` finns via migration.
- [ ] RLS är aktiverat och testat på `profiles`.
- [ ] Användaren kan inte ge sig själv adminbehörighet via browser/API.
- [ ] Ingen service-role/secret exponeras i klientbundle.
- [ ] Auth-fel visas på svenska utan informationsläckage.
- [ ] Bootstrap-rutin är dokumenterad.
- [ ] Relevanta tester, lint, typecheck och production build passerar.
- [ ] Codex rapporterar filer, testresultat, risker och avvikelser.
- [ ] Codex STOPPAR efter Fas 2 och inväntar explicit godkännande i VS Code.

## 19. Definition of Done

Fas 2 är tekniskt färdig när acceptanskriterierna är uppfyllda. Den är projektmässigt GODKÄND först när projektägaren uttryckligen godkänner fasen i VS Code/Codex-flödet.

Nästa fas efter godkännande: Fas 3 – Företagsinställningar.
