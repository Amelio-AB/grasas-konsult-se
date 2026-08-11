# Repo Architecture

Status: APPROVED FOR IMPLEMENTATION

## Goal

Behåll Engströms publika webbplats och adminverktyget i samma GitHub-repository men som två separata applikationer.

## Structure

```text
engstroms-konsulter/
├── apps/
│   ├── website/   # Astro – engstromskonsulter.se
│   └── admin/     # Next.js – admin.engstromskonsulter.se
├── docs/
│   └── admin/
└── package.json   # npm workspaces
```

## Boundaries

- `apps/website` är den publika Astro-sajten.
- `apps/admin` är den interna Next.js-applikationen.
- Adminarbete får inte ändra webbplatsen utan uttryckligt behov.
- Webbplatsarbete får inte ändra adminapplikationen utan uttryckligt behov.
- Gemensamma paket skapas först när konkret återanvändning finns; inget `packages/shared` byggs i förväg.

## Deployment targets

- `apps/website` → `engstromskonsulter.se`
- `apps/admin` → `admin.engstromskonsulter.se`

Varje app deployas som ett eget projekt med sin egen root directory.

## Database boundary

Supabase hör till adminapplikationen. Den publika Astro-sajten ska inte få adminens databasnycklar eller intern åtkomst.

## Phase gate

Den här omstruktureringen är fundamentet inför Fas 1. Efter installation ska följande verifieras innan Fas 1 godkänns:

1. Webbplatsen kan installeras och byggas från workspace-strukturen.
2. Adminappen kan installeras, typecheckas och byggas.
3. Inga hemligheter finns i Git.
4. Astro-sajtens visuella/funktionella innehåll är oförändrat.
5. Adminappen innehåller ännu ingen autentisering eller affärslogik.
