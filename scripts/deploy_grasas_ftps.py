#!/usr/bin/env python3
"""Publicera endast Gräsås startsida via Inleeds FTPS (explicit TLS, port 21).

Säkerhetsprinciper:
- Inga lösenord i GitHub-repot eller i loggarna.
- Inga kommandon som tar bort andra filer på servern.
- Ingen gissning om FTP-hemkatalogen om public_html inte kan hittas.
"""
from __future__ import annotations

import os
import ssl
from ftplib import FTP_TLS, error_perm, error_temp
import subprocess
from pathlib import Path

LOCAL_FILE = Path("deploy/grasas/index.html")
DOMAIN = "gräsåskonsult.se"


def required_secret(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise SystemExit(f"Saknar GitHub-secret {name}. Publiceringen avbröts.")
    return value


def choose_web_root(ftp: FTP_TLS) -> str:
    explicit = os.environ.get("FTP_REMOTE_DIR", "").strip()
    if explicit:
        ftp.cwd(explicit)
        print(f"FTP: använder angiven målmapp: {ftp.pwd()}")
        return ftp.pwd()

    start = ftp.pwd()
    ascii_domain = DOMAIN.encode("idna").decode("ascii")
    candidates = [
        "public_html",
        f"domains/{DOMAIN}/public_html",
        f"domains/{ascii_domain}/public_html",
        f"{DOMAIN}/public_html",
        f"{ascii_domain}/public_html",
    ]
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
        "Kontot kan redan vara begränsat till public_html. "
        "Sätt då GitHub-repovariabeln FTP_REMOTE_DIR till '.' "
        "och kör om arbetsflödet. Ingen fil laddades upp."
    )



def upload_with_curl(host: str, username: str, password: str, remote_dir: str) -> None:
    """libcurl återanvänder TLS-sessionen där servrar kräver det på datakanalen."""
    url = f"ftp://{host}/{remote_dir.strip('/')}/index.html"
    print("FTP: testar alternativ FTPS-datakanal med curl (fortfarande TLS-krypterad).")
    subprocess.run(
        [
            "curl", "--fail", "--silent", "--show-error",
            "--ssl-reqd", "--ftp-pasv", "--ftp-skip-pasv-ip",
            "--connect-timeout", "20", "--max-time", "120",
            "--user", f"{username}:{password}",
            "--upload-file", str(LOCAL_FILE),
            url,
        ],
        check=True,
    )


def main() -> None:
    host = required_secret("FTP_HOST")
    username = required_secret("FTP_USERNAME")
    password = required_secret("FTP_PASSWORD")
    if not LOCAL_FILE.is_file():
        raise SystemExit(f"Filen saknas: {LOCAL_FILE}")

    context = ssl.create_default_context()
    with FTP_TLS(context=context, timeout=40) as ftp:
        ftp.connect(host=host, port=21)
        ftp.login(user=username, passwd=password)
        ftp.prot_p()  # Kryptera även själva filöverföringen.
        ftp.set_pasv(True)
        remote_dir = choose_web_root(ftp)
        try:
            with LOCAL_FILE.open("rb") as infile:
                ftp.storbinary("STOR index.html", infile)
        except error_temp as exc:
            if not str(exc).startswith("425"):
                raise
            upload_with_curl(host, username, password, remote_dir)
        print(
            f"Uppladdning klar: {remote_dir.rstrip('/')}/index.html "
            f"({LOCAL_FILE.stat().st_size} byte). Inga andra filer ändrades."
        )


if __name__ == "__main__":
    main()
