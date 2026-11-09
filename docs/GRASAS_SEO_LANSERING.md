# Gräsås – lansering och indexering

## Produktionskälla

- Domän och kanonisk adress: https://grasaskonsult.se/
- GitHub-repo: Amelio-AB/grasas-konsult-se
- Startsida: `deploy/grasas/index.html`
- Sitemap: `deploy/grasas/sitemap.xml` (endast startsidan)
- Robots: `deploy/grasas/robots.txt`
- Logotypfiler: `deploy/grasas/images/`
- Publicering: GitHub Actions via FTPS, endast till Görans Inleed på ns14.inleed.net

Sedan kundens manuella DirectAdmin-version synkroniserats till GitHub ska framtida ändringar ske i GitHub/VS Code. **Ändra inte produktionsfilen separat i Inleeds filhanterare**, annars kan den skrivas över nästa gång GitHub publicerar.

## Tekniska indexeringssignaler

- Inget `noindex`-metatag i startsidan
- `rel=canonical` till https://grasaskonsult.se/
- `robots.txt` tillåter crawl och hänvisar till sitemap
- `sitemap.xml` innehåller endast den kanoniska startsidan
- HTML-kontaktvägar med Görans bekräftade telefonnummer och e-post
- Grundläggande sociala metataggar och Organization JSON-LD

Publiceringsskriptet kontrollerar före uppladdning att indexering inte blockeras och att kontaktvägarna finns. Det tar inte bort övriga filer på servern. Efter uppladdning testar GitHub Actions de publika filerna.

## Google Search Console – kräver kontoägare

1. Gå till https://search.google.com/search-console/
2. Lägg till en domänegendom: `grasaskonsult.se` (hela domänen, utan https).
3. Google visar en unik verifieringspost (TXT). Lägg den på **Görans registrerade domän** hos Inleed under DNS / namnservrar. Ta inte bort befintliga SPF-, DKIM-, DMARC- eller MX-poster.
4. Klicka på Verifiera i Search Console när TXT-posten har blivit synlig.
5. Öppna **Webbplatskartor / Sitemaps** och skicka in `https://grasaskonsult.se/sitemap.xml`.
6. Använd **Granska webbadress / URL Inspection** för `https://grasaskonsult.se/`, och välj **Begär indexering**.
7. Följ upp under Indexering > Sidor. Indexering kan ta dagar eller veckor och garanteras inte.

## Efter lansering

- Kontrollera även `https://www.grasaskonsult.se/` och `http://grasaskonsult.se/`. Välj vid behov 301-omdirigering till den kanoniska HTTPS-adressen i Inleed, först efter kontroll av SSL.
- Om den äldre domänen `gräsåskonsult.se` ska pekas om, gör det separat i Inleed så att dess eventuella mejlinställningar inte påverkas.
- Fortsätt använda huvudadressen `grasaskonsult.se` konsekvent på visitkort och andra profiler.

**OBS:** En sitemap och en indexerbar sida garanterar inte Google-placering. Verifiera i Search Console efter lansering.
