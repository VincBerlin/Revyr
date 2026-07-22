# REVYR — Plan-PRD (Traceability: Anforderung → Plan → Release → Gate)

> **Dokumentzweck:** Die verbindliche Brücke zwischen PRD und Umsetzung. Jede Anforderung (REQ-ID aus `REVYR-Vision-Canvas-PRD.md`) ist genau den Plan-Tasks des Gesamtplans (FINAL, `2026-07-10-REVYR-GESAMTPLAN-FINAL.md`) zugeordnet, mit Zielversion, Gate und Status. Damit ist jederzeit prüfbar: *Ist jede Anforderung eingeplant? Ist jeder Task durch eine Anforderung begründet?*
> **Pflege:** Statusspalte wird während der Umsetzung aktualisiert (geplant → in Arbeit → ✅ nachgewiesen). „Nachgewiesen" heißt: Evidence-Ledger-Eintrag existiert (`docs/EVIDENCE-LEDGER.md`), Run + Bike getrennt geprüft.
> **Stand:** 2026-07-16 (Einzel-Reviere: emergente Geometrie + Übernahme a–d; Sensor-Plausibilität G-08; Sportplatz-Challenges G-12 inkl. Bahngold ✅; L-01 erweitert)

**Statuslegende:** 📋 geplant · 📝 Detailplan geschrieben · 🔨 in Arbeit · ✅ nachgewiesen (Ledger)

---

## 1. Epic H — Health (Priorität 1)

| REQ | Anforderung (Kurzform) | Plan · Task | Version | Gate | Status |
|---|---|---|---|---|---|
| H-01 | HF live/Verlauf/Ø (HealthKit, Health Connect, BLE-Gurt) | 3.1, 3.2 | v1.0 | A | 📋 |
| H-02 | Erklärbarer Belastungs-Score mit „Warum"-Sheet | 3.4 | v1.0 | A | 📋 |
| H-03 | HF-Zonen + Live-Zonen-Ansage (deaktivierbar) | 3.3, 3.8 | v1.0 | A | 📋 |
| H-04 | Stimmungs-Check-in + Korrelations-Karten | 3.5 | v1.0 | A | 📋 |
| H-05 | Einfache Steigerungs-Warnung (> 30 % vs. 4-Wochen-Ø) | 3.6 | v1.0 | A | 📋 |
| H-06 | Health-Home (Wochenzustand oben) | 3.7 | v1.0 | A | 📋 |
| H-07 | Kalorien pro Aktivität | 3.3 | v1.0 | A | 📋 |
| H-08 | Regeneration/ACWR/Hitze/Zyklus — nur nach Claims-Freigabe | 16.0–16.3, 17.3, 17.4 | v5.0 | E | 📋 |

## 2. Epic T — Tracking & Routen

| REQ | Anforderung | Plan · Task | Version | Gate | Status |
|---|---|---|---|---|---|
| T-01 | Modus A: 1-Tipp-Start, GPS, Live-Karte, Stats | **Plan 1, Tasks 1–8** | v1.0 | A | 📝 |
| T-02 | Modus B: Wegpunkt-Route / km-Ziel, verbleibende km | **Plan 1, Tasks 9–12** | v1.0 | A | 📝 |
| T-03 | Hintergrund-GPS, Crash-Recovery, Pause/Auto-Pause | 2.1, 2.2, 2.4, 2.5 | v1.0 | A | 📋 |
| T-04 | GPS-Filterung (Genauigkeit, Ausreißer) | 2.3 | v1.0 | A | 📋 |
| T-05 | Verlauf, Routen speichern/wiederverwenden, Streckenrekorde | Plan 1 Task 8 · 2.7 | v1.0 | A | 📝/📋 |
| T-06 | GPX-Export | 2.8 | v1.0 | A | 📋 |
| T-07 | Live Activity/Dynamic Island (iOS), Widget/Notification (Android) | 4.6 | v1.0 | A | 📋 |
| T-08 | Fingerskizze → Route (Spike, Verschieben zulässig) | 5.2 | v1.0* | A | 📋 |
| T-09 | Neue-Strecke-Erkennung + Empfehlungs-Post + 1-Tipp-Übernahme | 8.1, 8.2 | v2.0 | B | 📋 |

## 3. Epic M — Run/Bike-Modus & Design

| REQ | Anforderung | Plan · Task | Version | Gate | Status |
|---|---|---|---|---|---|
| M-01 | Modus-Umschalter stellt gesamte Oberfläche um | 4.2 | v1.0 | A | 📋 |
| M-02 | Effort-Normalisierung (Run 1,0/Bike 0,4; Kalibrierung per Simulation) | 10.1 (Definition ab 2.6) | v3.0 | C | 📋 |
| M-03 | Getrennte Sport-Schwellen (Sampling, Auto-Pause, Ziele) als Config | 2.6 | v1.0 | A | 📋 |
| M-04 | S/W-Design-System („Farbe muss man sich verdienen") | 4.1 | v1.0 | A | 📋 |
| M-05 | Dopamin-Basis: Reveals, Haptik, Meilenstein-Vollbild, Wochenrückblick | 4.4, 4.5 | v1.0 | A | 📋 |

## 4. Epic A — Avatare & Progression

| REQ | Anforderung | Plan · Task | Version | Gate | Status |
|---|---|---|---|---|---|
| A-01 | Basis-Avatar-Editor, Runner-/Biker-Form | 4.3 | v1.0 | A | 📋 |
| A-02 | Unlock-System (nur Leistung; Seltenheitsstufen; nichts kaufbar) | 7.2 | v2.0 | B | 📋 |
| A-03 | Team-Harness: Trikots über Teamstufen; Season-Exklusive einmalig | 9.4 (+ `team_gear`) | v3.0 | C | 📋 |

## 5. Epic S — Social & Accounts

| REQ | Anforderung | Plan · Task | Version | Gate | Status |
|---|---|---|---|---|---|
| S-01 | Auth (E-Mail/Apple/Google), Offline-first-Sync, Datenmigration | 6.2, 6.4, 6.5 (Entscheid 6.0) | v2.0 | B | 📋 |
| S-02 | Profile + Sichtbarkeit (Standard privat) | 7.1, 7.3 | v2.0 | B | 📋 |
| S-03 | Follow + Anfrage + Feed gemäß Matrix | 7.4 | v2.0 | B | 📋 |
| S-04 | Erfolgskarten: Export (v1.0) + In-App-Feiern/Reaktionen (v2.0) | 4.5 · 8.3 | v1.0/v2.0 | A/B | 📋 |
| S-05 | Account-Löschung in-App, vollständig | 6.6 | v2.0 | B | 📋 |
| S-06 | UGC-Sicherheit: Melden, Blockieren, Queue, Regeln, Wortfilter | 7.5, 8.4, 8.5 | v2.0 | B | 📋 |

## 6. Epic G — Teams, Wachstum, Wettbewerb

| REQ | Anforderung | Plan · Task | Version | Gate | Status |
|---|---|---|---|---|---|
| G-01 | Team-Gründung (Transaktion, Farbe, Logo) | 9.1 | v3.0 | C | 📋 |
| G-02 | Beitritt: Link-Lebenszyklus + QR + Deep Links | 9.2 | v3.0 | C | 📋 |
| G-03 | Teamstufen (Leistung ∧ Größe) + Gear-Unlocks | 9.4 | v3.0 | C | 📋 |
| G-04 | Mentor-Bonus nach Integration + Integrations-Quest | 9.5 | v3.0 | C | 📋 |
| G-05 | Aktiv-Definition (28 Tage) für Quoren/Kapazität | 9.3 | v3.0 | C | 📋 |
| G-06 | Team-Suche „offen für Mitglieder" | 9.6 | v3.0 | C | 📋 |
| G-07 | Radius-Rankings sport-getrennt + „✓ verifiziert" | 10.3, 10.4 | v3.0 | C | 📋 |
| G-08 | Anti-Cheat serverseitig inkl. Sensor-Plausibilität (Pace vs. Schritte/HF/Kalorien) | 10.2 (Datenerfassung 3.3) | v3.0 | C | 📋 |
| G-09 | Wochen-Challenges + idempotente Rewards + Team-Streaks | 11.2, 11.3, 11.4 | v3.0 | C | 📋 |
| G-10 | „Gemeinsame Aktivität" als pure Funktion | 11.1 | v3.0 | C | 📋 |
| G-11 | Team-Health (anonymisiert, Opt-in) | 11.6 | v3.0 | C | 📋 |
| G-12 | Sportplatz-Rundenlauf-Challenges (automatische Erkennung, goldene Flächen) + Platz-Rekorde + Bahngold-Punktesystem | 12.13, 12.14 (nutzt 12.10, 11.1, 7.2) | v4.0 | D | 📋 |
| — | Community/Team Runs & Rides planen (§19) | 11.5 | v3.0 | C | 📋 |
| — | Admin-Pinnwand + Team-Moderation | 9.7 | v3.0 | C | 📋 |

## 7. Epic R — Territory & Seasons

| REQ | Anforderung | Plan · Task | Version | Gate | Status |
|---|---|---|---|---|---|
| R-01 | Zwei Ebenen: Team-Besitz (nur gemeinsam) / Einzel-Reviere + Spuren + Local-Hero-Krone; Layer-Umschalter | 12.5, 12.7 | v4.0 | D | 📋 |
| R-02 | Eroberungsformel (Effort-Ziel ∧ Quorum; Mindestbeitrag; Einzeldeckel) | 12.1 (Simulation), 12.3 | v4.0 | D | 📋 |
| R-03 | Geschlossenheits-Bonus ×1,5 + Exklusiv-Medaille | 12.3 | v4.0 | D | 📋 |
| R-04 | Verteidigungslevel + wöchentlicher Verfall | 12.3 | v4.0 | D | 📋 |
| R-05 | Kapazität: 3 Areale × aktive Mitglieder | 12.3 (nutzt 9.3) | v4.0 | D | 📋 |
| R-06 | Server-Pipeline Track→Raster→Areal-Beiträge→Capture-Event | 12.4 | v4.0 | D | 📋 |
| R-07 | Fortschritts-UI (Areal-Detail, Beitrag, Leaderboard, Finaltreffer) | 12.6 | v4.0 | D | 📋 |
| R-08 | Seasons + `season_records` + Vereinsheim + Zeitreise + Rückblick | 12.8, 12.9 | v4.0 | D | 📋 |
| R-09 | Karten-Performance (1.000+ Arealen flüssig) | 12.5 | v4.0 | D | 📋 |
| R-10 | Einzel-Revier-Eroberung (emergent — Läufer definiert Gebiet durch seine Runde; Übernahme-Regeln a–d: größere Runde / mehr km / bessere Zeit / Teil-Übernahme mit Geometrie-Beschnitt; Startpunkt frei; getrennt von Teams) | 12.10, 12.11 (Simulation in 12.1) | v4.0 | D | 📋 |
| R-11 | Einzel-Revier-UI: Farbe/Bild, Top 3, Angriffs-Fortschritt, Live-Tracking | 12.12 (nutzt 13.2, 8.4) | v4.0 | D | 📋 |
| R-12 | Territorien-Filter + Live-Sportler-Zoom-Aggregation | 12.12 | v4.0 | D | 📋 |

## 8. Epic L — Live & Safety

| REQ | Anforderung | Plan · Task | Version | Gate | Status |
|---|---|---|---|---|---|
| L-01 | Live-Map mit bewegten Avataren + Mini-Profilkarte (km-Ziel, Einnahme-Status) + Folgen/Anfrage | 13.3 | v4.0 | D | 📋 |
| L-02 | Freigabe-Sicherheitsmodell (Opt-in, Zeitlimit, Not-Aus, alle Endpfade) | 13.1, 13.2 | v4.0 | D | 📋 |
| L-03 | Beschützer-Modus (Web-Link ohne Account) | 13.4 | v4.0 | D | 📋 |
| L-04 | Sturzerkennung (primär Bike, Assistenz-Sprache) | 13.5 | v4.0 | D | 📋 |
| L-05 | Lokale Events + Moderation + Kopplung „gemeinsame Aktivität" | 14.1–14.4 | v4.0 | D | 📋 |

## 9. Epic W — Wearables & Coach

| REQ | Anforderung | Plan · Task | Version | Gate | Status |
|---|---|---|---|---|---|
| W-01 | Watch-Companions (Apple Watch, Wear OS) | 15.1, 15.2 | v5.0 | E | 📋 |
| W-02 | Bike-Sensorik voll (Trittfrequenz, Speed, Höhenprofil) | 15.3 | v5.0 | E | 📋 |
| W-03 | Erklärbarer KI-Coach + Audio-Coach | 17.1, 17.2 | v5.0 | E | 📋 |
| W-04 | Wetter + Hitze-/Trinkwarnung + Wetterfenster | 17.3 | v5.0 | E | 📋 |
| W-05 | Wearable-Kompatibilitätsmatrix | 15.4 | v5.0 | E | 📋 |

## 10. Nicht-funktionale Anforderungen → Verankerung

| NFR | Verankerung | Nachweis |
|---|---|---|
| Distanzgenauigkeit < 3 % | 2.3 (Filter) | Referenzstrecken-Messung, Ledger |
| Batterie < 10 %/h Ziel | 2.6, 2.9 | Messlauf je Sport + Plattform |
| Kein Datenverlust (App-Kill) | 2.4 | Kill-Test im Gate A |
| Offline-first | 6.4 | Flugmodus-Test |
| Karten-Performance | 12.5 | Messwert 1.000+ Arealen |
| DSGVO/Privacy | 6.1 (EU), 6.6 (Löschung), 2.8 (Export), 7.3 (Standard privat) | Gate B |
| Security | 6.2, 6.7 | Tests + Lastprobe |
| Accessibility (WCAG AA) | 4.1 | Design-Token-Review + Screenreader-Check |
| Store-Compliance iOS/Android | Gesamtplan Abschnitt 8 (Matrix) | je Einreichung, TestFlight/Internal |
| Claims-Grenze Health | 16.0 (Whitelist + Lint) | juristische Freigabe, Gate E |

## 11. Vollständigkeits-Check (beide Richtungen)

- **PRD → Plan:** Alle 8 Epics (H, T, M, A, S, G, R, L, W) sind vollständig Tasks zugeordnet; kein REQ ohne Plan. ✔
- **Plan → PRD:** Alle Tasks der Pläne 1–17 sind durch REQs oder NFRs begründet; reine Infrastruktur-Tasks (2.1 Dev-Build, 6.0/6.1 Backend-Setup, 4.7 Onboarding) dienen jeweils den REQs ihrer Stufe. Zwei Konzept-Features ohne eigene REQ-ID (Community Runs §19, Team-Pinnwand) sind in Abschnitt 6 als „—" ergänzt und Tasks 11.5/9.7 zugeordnet. ✔
- **Blocker-Kette:** Name (→ Gate A) · Backend-Entscheid 6.0 (→ v2.0) · Karten-ADR (→ v2.0) · Claims-Freigabe 16.0 (→ H-08) · Simulationen 10.1/12.1 (→ M-02, R-02, R-10, Bahngold-Startwerte).

## 12. Arbeitsregel

Bei jeder Umsetzung eines Plans: (1) Detailplan im Muster von Plan 1 schreiben, dabei REQ-IDs je Task übernehmen · (2) nach Abschluss Status hier aktualisieren + Ledger-Eintrag verlinken · (3) ein Gate gilt erst als bestanden, wenn alle REQs seiner Version ✅ sind.
