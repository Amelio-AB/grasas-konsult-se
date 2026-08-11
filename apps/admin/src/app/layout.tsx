import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Engströms Admin",
  description: "Internt administrationsverktyg för Engströms Konsulter AB",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="sv">
      <body>{children}</body>
    </html>
  );
}
