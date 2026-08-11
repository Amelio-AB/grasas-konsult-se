# Fas 1 – Teknisk grund

Status: READY FOR IMPLEMENTATION
Phase gate: MANUELLT GODKÄNNANDE KRÄVS I VS CODE/CODEX INNAN FAS 2

## 1. Syfte
Skapa en ren, säker och reproducerbar teknisk grund för Engströms Admin utan att ännu implementera autentisering, kundregister, offerter, fakturor eller PDF-flöden. Fasen ska göra det möjligt att börja Fas 2 utan att arkitekturen behöver byggas om.

## 2. Tekniska beslut

### Frontend/fullstack
- Next.js med App Router
- TypeScript strict
- React Server Components som standard
- Client Components endast där interaktivitet kräver det
- Server Actions/Route Handlers endast när de fyller tydligt behov

### Databas/backend
- Supabase PostgreSQL
- Supabase JS
- `@supabase/ssr` för server-/cookie-baserad sessionhantering
- Supabase CLI för lokal utveckling och migrationshantering

### Styling och tooling
- Tailwind CSS
- enkel intern komponentstruktur
- npm
- Vercel-kompatibel drift
- planerad produktionsdomän: `admin.engstromskonsulter.se`

## 3. Arkitekturprinciper
1. Server-first.
2. Databasen är source of truth.
3. Ingen affärslogik i presentationskomponenter.
4. Ingen känslig miljövariabel får exponeras med `NEXT_PUBLIC_`.
5. Supabase service-role key får aldrig användas i browserkod.
6. Databasschema ändras endast genom versionshanterade migrations.
7. Fil-/mappnamn på engelska; UI på svenska.
8. Faktura-/offertberäkning ska senare centraliseras i domänlager.
9. Projektet ska gå att klona och starta från dokumenterade instruktioner.
10. Fas 1 får inte implementera produktionsfunktionalitet från senare faser.

## 4. Målstruktur

```text
engstroms-admin/
├── docs/
├── public/brand/
├── src/
│   ├── app/
│   ├── components/
│   ├── lib/env/
│   ├── lib/supabase/
│   ├── types/
│   └── utils/
├── supabase/
│   ├── config.toml
│   ├── migrations/
│   └── seed.sql
├── tests/
├── .env.example
├── .gitignore
├── AGENTS.md
├── README.md
├── package.json
├── tsconfig.json
└── vitest.config.*
```

Strukturen är ett mål. Tomma mappar ska inte skapas utan syfte och Codex får förenkla där aktuell Next.js-version motiverar det, men avvikelser ska dokumenteras.

## 5. Routes

### `/`
En enkel intern status-/landningssida under utveckling med Engströms Admin, texten `Systemet är under uppbyggnad` och länk till `/admin`.

### `/admin`
Skal för framtida dashboard med produktnamn/logotyp, navigationsskal och placeholders.

VIKTIGT: `/admin` är INTE säker i Fas 1. Skydd byggs i Fas 2 och detta ska tydligt markeras i kod och dokumentation.

## 6. Admin-layout

Desktop:
- vänster sidomeny
- huvudområde
- enkel topprad

Mobil:
- kompakt header
- enkel responsiv meny/placeholder

Framtida poster får visas disabled: Översikt, Kunder, Offerter, Fakturor, Inställningar. Ingen fake-data får presenteras som verklig data.

## 7. Visuell riktning
Adminpanelen ska vara lugn, tydlig, professionell, modern utan att kännas techig och anpassad för låg teknisk vana. Prioritera hög läsbarhet, tydliga klickytor, whitespace, få färger och Engströms accentfärg.

## 8. Supabase-grund
Fas 1 ska initialisera `/supabase`, lokal projektkonfiguration, browser/server client helpers och verifierbar anslutningsgrund. Inga verksamhetstabeller eller profil-/rolltabeller skapas ännu.

## 9. Miljövariabler
`.env.example` ska minst dokumentera:

```env
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=
```

Följ aktuell officiell Supabase-benämning om den ändrats. `.env.local` ska ignoreras av Git och inga verkliga secrets får committas.

## 10. Miljövalidering
Appen ska ge tydliga fel vid saknade obligatoriska variabler, exempelvis `Missing NEXT_PUBLIC_SUPABASE_URL`, inte diffusa runtime-fel.

## 11. Error states
Grundläggande `error.tsx`, `global-error.tsx` där relevant, `not-found.tsx` och begripliga svenska tom-/felllägen ska finnas. Stack traces ska inte visas för slutanvändaren i produktion.

## 12. Kodkvalitet
- TypeScript strict
- undvik onödiga `any`
- ESLint
- konsekvent importstruktur
- inga secrets
- inga onödiga create-next-app-exempel
- inga odokumenterade warnings

## 13. Tester
Konfigurera test-runner och minst ett relevant smoke-test. Vitest rekommenderas. E2E väntar tills riktiga flöden finns.

## 14. Scripts
`package.json` ska minst ha motsvarigheter till `dev`, `build`, `start`, `lint`, `typecheck` och `test`.

## 15. README
README ska dokumentera projektet, förutsättningar, installation, miljövariabler, lokal utveckling, Supabase lokalt, tester, build, fasmodell/godkännande och produktionssubdomänen.

## 16. Ingår INTE i Fas 1
Codex får inte implementera login/logout/password reset, route protection, roller, verksamhets-RLS, företagsinställningar, kunder, offerter, fakturor, fakturanummer, PDF, e-post, Hogia, dashboard-KPI:er eller audit log. Behov för senare fas dokumenteras men implementeras inte.

## 17. Acceptanskriterier
- [ ] ren clone kan installeras
- [ ] `npm run dev` startar
- [ ] `/` och `/admin` renderas
- [ ] admin-layout fungerar desktop/mobil
- [ ] Supabase client/server helpers finns
- [ ] lokalt Supabase-upplägg är dokumenterat
- [ ] `.env.example` finns utan secrets
- [ ] saknad env ger begripligt fel
- [ ] TypeScript strict aktivt
- [ ] `npm run typecheck` passerar
- [ ] `npm run lint` passerar
- [ ] `npm run test` passerar
- [ ] `npm run build` passerar
- [ ] inga senare faser implementerade
- [ ] README uppdaterad
- [ ] ändrade filer och risker/avvikelser rapporterade

## 18. Manuell granskning
Projektägaren kontrollerar README-start, desktop/mobil, terminal/browser console, scope-disciplin, onödig komplexitet och samtliga quality scripts.

Godkännandefras: `GODKÄND FAS 1`

Codex får inte börja Fas 2 före detta godkännande i VS Code/Codex.

## 19. Exit report
Codex ska rapportera Fas 1-resultat, ändrade filer, verifiering för dev/typecheck/lint/test/build, avvikelser, kända risker och manuell kontroll.

### Gate
STOPP. Inväntar `GODKÄND FAS 1`.
