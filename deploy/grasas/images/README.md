# Logotyper för Gräsås Konsult och Service AB

Detta är originalfilerna för logotypen. Bakgrunden är transparent och den gula vägen ingår i varje version.

- `grasas-full-vit.svg` – full logotyp med vit text, för mörka bakgrunder
- `grasas-full-svart.svg` – full logotyp med svart text, för ljusa bakgrunder
- `grasas-symbol-vit.svg` – enbart GK-symbolen i vitt
- `grasas-symbol-svart.svg` – enbart GK-symbolen i svart

Vid varje publicering bygger GitHub Actions automatiskt motsvarande WebP-filer
med `scripts/build_grasas_logos.py`, och laddar upp både SVG och WebP i
`/public_html/images/` hos Inleed.

## Byta logotyp i framtiden

1. Öppna `deploy/grasas/images/` i GitHub.
2. Byt ut den aktuella **SVG-filen** via GitHub eller VS Code, men behåll filnamnet.
3. Publicera ändringen på `main`. GitHub Actions skapar automatiskt ny WebP och laddar upp den.

Startsidan använder `/images/grasas-full-vit.webp` i sidhuvudet.
En fristående GK-symbol finns som favicon i två färgvarianter.

Ändra inte SVG-originalen till JPG eller bädda in vit bakgrund – transparensen behövs.
