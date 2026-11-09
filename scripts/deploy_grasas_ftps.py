#!/usr/bin/env python3
"""Publicera endast Gräsås logotyper till Inleed via krypterad FTPS.

Filerna listas uttryckligen. Vi tar aldrig bort andra filer på webbhotellet.
"""
from __future__ import annotations

import os
import ssl
import subprocess
from ftplib import FTP_TLS, error_perm
from pathlib import Path

SITE = Path("deploy/grasas")
DOMAIN = "grasaskonsult.se"
ASSET_NAMES = (
    "grasas-full-vit.svg",
    "grasas-full-vit.webp",
    "grasas-full-svart.svg",
    "grasas-full-svart.webp",
    "grasas-symbol-vit.svg",
    "grasas-symbol-vit.webp",
    "grasas-symbol-svart.svg",
    "grasas-symbol-svart.webp",
)
# Skydda redigeringar som gjorts direkt i Inleeds filhanterare.
# Den här FTP-rutinen får ENDAST ladda upp logotypfiler, ALDRIG index.html.
UPLOADS = tuple((SITE / "images" / name, f"images/{name}") for name in ASSET_NAMES)


def required_secret(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise SystemExit(f"Saknar GitHub-secret {name}. Ingen fil laddades upp.")
    return value


def choose_web_root(ftp: FTP_TLS) -> str:
    explicit = os.environ.get("FTP_REMOTE_DIR", "").strip()
    if explicit:
        ftp.cwd(explicit)
        print(f"FTP: använder angiven målmapp: {ftp.pwd()}")
        return ftp.pwd()

    start = ftp.pwd()
    candidates = (
        "public_html",
        f"domains/{DOMAIN}/public_html",
        f"{DOMAIN}/public_html",
    )
    for candidate in candidates:
        ftp.cwd(start)
        try:
            ftp.cwd(candidate)
        except error_perm:
            continue
        print(f"FTP: hittade webbplatsmappen: {ftp.pwd()}")
        return ftp.pwd()

    ftp.cwd(start)
    if start.rstrip("/").lower().endswith("/public_html"):
        print(f"FTP: kontot öppnas direkt i webbplatsmappen: {start}")
        return start

    raise SystemExit(
        "FTP-inloggningen lyckades, men public_html hittades inte. "
        "Sätt vid behov GitHub-repovariabeln FTP_REMOTE_DIR till '.', "
        "om FTP-kontot redan öppnas i webbplatsmappen."
    )


def ensure_image_folder(ftp: FTP_TLS, web_root: str) -> None:
    ftp.cwd(web_root)
    try:
        ftp.cwd("images")
    except error_perm:
        ftp.mkd("images")
        ftp.cwd("images")
    ftp.cwd(web_root)


def upload_with_curl(
    host: str, username: str, password: str, web_root: str,
    source: Path, remote_path: str,
) -> None:
    url = f"ftp://{host}/{web_root.strip('/')}/{remote_path}"
    result = subprocess.run(
        [
            "curl", "--fail", "--silent", "--show-error",
            "--ssl-reqd", "--ftp-pasv", "--ftp-skip-pasv-ip",
            "--connect-timeout", "20", "--max-time", "120",
            "--user", f"{username}:{password}",
            "--upload-file", str(source), url,
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode:
        # Skriv inte ut subprocess-undantag: deras argument kan innehålla FTP-lösenordet.
        raise SystemExit(
            f"FTPS kunde inte ladda upp {remote_path} (curl-felkod {result.returncode})."
        )
    print(f"Uppladdning klar: {remote_path} ({source.stat().st_size} byte)")


def main() -> None:
    host = required_secret("FTP_HOST")
    username = required_secret("FTP_USERNAME")
    password = required_secret("FTP_PASSWORD")

    if host != "ns14.inleed.net" or username != f"ftp@{DOMAIN}":
        raise SystemExit("FTP-målet matchar inte Görans webbhotell. Inga filer ändrades.")

    for local_file, _ in UPLOADS:
        if not local_file.is_file():
            raise SystemExit(f"Kan inte publicera: saknar {local_file}")

    with FTP_TLS(context=ssl.create_default_context(), timeout=40) as ftp:
        ftp.connect(host=host, port=21)
        ftp.login(user=username, passwd=password)
        ftp.prot_p()
        ftp.set_pasv(True)
        web_root = choose_web_root(ftp)
        ensure_image_folder(ftp, web_root)

        # Ladda upp enbart bilder; index.html på servern ska lämnas orörd.
        for local_file, remote_path in UPLOADS:
            upload_with_curl(host, username, password, web_root, local_file, remote_path)

        print("Publicering klar. Inga andra filer raderades.")


if __name__ == "__main__":
    main()
