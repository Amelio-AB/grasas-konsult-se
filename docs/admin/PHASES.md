# Engströms Admin – Fasplan

## Fas 0 – Projektspecifikation
Status: GODKÄND

Syfte: Låsa mål, avgränsning, användarflöden, affärsregler och arkitekturprinciper innan kodning.

## Fas 1 – Teknisk grund
Syfte: Skapa stabil kodbas, miljöhantering, routing, UI-skal och Supabase-klient.

Ingår:
- Next.js med TypeScript
- App Router
- Supabase client/server setup
- miljövariabler via .env.local och .env.example
- grundläggande layout för admin
- felgränser och tomma states
- lint, typecheck, build

Ingår inte:
- kundregister
- offerter
- fakturor
- PDF

Acceptanskriterier:
- projektet startar lokalt utan fel
- typecheck/lint/build passerar
- Supabase-anslutning verifierad
- skyddade routes kan införas i nästa fas utan ombyggnad

## Fas 2 – Autentisering och behörighet
Syfte: Endast godkända användare ska kunna nå systemet.

Ingår:
- e-post + lösenord via Supabase Auth
- login/logout
- lösenordsåterställning
- skyddade routes
- admin-roll
- RLS för alla privata tabeller

Acceptanskriterier:
- ej inloggad användare når ingen admin-data
- inloggad admin når endast tillåtna resurser
- direkt URL till skyddad sida blockeras

## Fas 3 – Företagsinställningar
Syfte: Central källa för Engströms företagsuppgifter.

Ingår:
- företagsnamn
- org.nr
- momsregistreringsnr
- adress
- e-post/telefon
- bank-/betalningsuppgifter
- standardmoms
- betalningsvillkor
- offertens giltighetstid
- logotyp
- nummerserieinställningar

Acceptanskriterier:
- ändring slår igenom på nya dokument
- gamla slutställda dokument påverkas inte retroaktivt

## Fas 4 – Kundregister
Syfte: Enkelt kundkort återanvänt i offert/faktura.

Ingår:
- skapa/redigera/arkivera kund
- organisationsnummer
- fakturaadress
- kontaktperson
- e-post
- telefon
- referens
- kundanteckning
- sökning

Acceptanskriterier:
- kund kan skapas på under en minut
- kund kan väljas från offert/faktura
- historiska dokument behåller snapshot av kunduppgifter

## Fas 5 – Offerter
Syfte: Skapa tydliga offerter med fria arbetsrader.

Ingår:
- utkast
- automatiskt offertnummer enligt definierad regel
- kundval
- offertdatum/giltighet
- referens
- rubrik/beskrivning
- dynamiska rader: benämning, antal/timmar, enhet, à-pris, moms
- automatisk summa
- anteckning/villkor
- status: utkast, skickad, accepterad, avböjd, utgången

Acceptanskriterier:
- beräkningar är deterministiska och testade
- användaren kan lägga till/ta bort/ordna rader
- offerthistorik sparas

## Fas 6 – Offert-PDF
Syfte: Konsekvent professionell PDF från strukturerad data.

Ingår:
- fast mall
- logotyp/företagsdata
- kunddata
- rader och summering
- villkor
- offertnummer
- förhandsgranskning
- nedladdning

Acceptanskriterier:
- samma data ger samma layout
- lång offert hanteras över flera sidor
- svenska tecken fungerar

## Fas 7 – Fakturor
Syfte: Skapa fakturaunderlag med säkra status- och nummerregler.

Ingår:
- fakturautkast
- kundval
- fakturadatum
- förfallodatum
- referens
- rader
- moms och total
- status: utkast, slutställd, skickad, förfallen, betald, krediterad
- markera betald manuellt

Viktig regel:
- slutligt fakturanummer tilldelas atomärt när fakturan slutställs
- slutförd faktura får inte raderas eller fritt redigeras

Acceptanskriterier:
- inga duplicerade fakturanummer kan uppstå vid samtidiga anrop
- utkast kan redigeras
- slutställd faktura är låst

## Fas 8 – Offert till faktura
Syfte: Minimera dubbelarbete.

Ingår:
- skapa fakturautkast från offert
- kopiera kundsnapshot och rader
- behålla relation mellan dokumenten
- originaloffert ändras aldrig

Acceptanskriterier:
- en offert kan konverteras utan att data skrivs över
- kopplingen mellan offert och faktura är spårbar

## Fas 9 – Faktura-PDF
Syfte: Skapa konsekvent faktura-PDF.

Ingår:
- fakturanummer
- fakturadatum/förfallodatum
- företags- och kunduppgifter
- rader
- moms
- total
- betalningsinformation
- PDF-snapshot/version

Acceptanskriterier:
- PDF motsvarar den låsta fakturans data
- tidigare PDF kan återhämtas

## Fas 10 – Dashboard
Syfte: Göra systemets startsida till en enkel arbetsyta.

Ingår:
- skapa ny offert
- skapa ny faktura
- lägg till kund
- pågående/skickade offerter
- obetalda/förfallna fakturor
- nyligen skapade dokument
- tydlig statusöversikt

Ingår inte i MVP:
- avancerad ekonomi/statistik
- bokföringsrapporter

Acceptanskriterier:
- viktigaste uppgifterna nås inom 1–2 klick
- ingen teknisk terminologi krävs

## Fas 11 – Säkerhet, test och dataintegritet
Syfte: Säkerställa att systemet kan användas med verklig kund- och fakturadata.

Ingår:
- RLS-granskning
- validering server-side
- CSRF/XSS/URL- och inputgranskning relevant för stacken
- behörighetstest
- nummersekvenstest
- kalkyltester
- PDF-regressionstest
- audit log för kritiska händelser
- testdata

Acceptanskriterier:
- inga privata tabeller saknar RLS
- kritiska regler kan inte kringgås från webbläsaren
- manuellt testprotokoll passerat

## Fas 12 – Backup, deployment och drift
Syfte: Produktionssätta systemet kontrollerat.

Rekommenderad subdomän: admin.engstromskonsulter.se

Ingår:
- produktionsmiljö
- DNS/subdomän
- HTTPS
- Supabase production project
- backupstrategi
- Storage-backupstrategi
- fel/loggövervakning
- releasechecklista
- återställningsrutin
- README för drift

Acceptanskriterier:
- produktion kräver autentisering
- backup och restore-rutin är dokumenterad
- miljöhemligheter finns inte i Git
- deployment kan reproduceras

## Fas 13 – Överlämning och kundacceptans
Syfte: Säkerställa att systemet fungerar för en mycket oteknisk användare.

Ingår:
- slutlig användartestning
- kort manual
- test: skapa kund → offert → PDF → faktura → PDF → markera betald
- korrigera UX-friktion

Acceptanskriterier:
- kunden kan genomföra kärnflödet utan teknisk hjälp
- inga blockerande fel finns
- projektet märks som v1.0

## Senare funktioner – inte MVP
- skicka dokument via e-post från systemet
- automatiska påminnelser
- Hogia-integration/export
- e-faktura/Peppol
- artikel-/tjänstregister
- flera roller/användare
- rapportering
- återkommande fakturor
