# REVYR — GESAMTPLAN (FINAL)

> **Dokumentzweck:** Der eine, endgültige und verbindliche Plan für die gesamte App — Produktidentität, Design, alle Kernsysteme als Spezifikation, Release-Stufen, Arbeitspakete, Store-Anforderungen (iOS + Android), Nachweisregeln und Risiken.
> **Ersetzt und löscht:** Gesamtplan v1/v2 und MVP-Roadmap (entfernt — dieses Dokument ist der einzige gültige Plan-Stand).
> **Gültige Begleitdokumente:** Konzept (`RUNNING_CYCLING_APP_KONZEPT_CHAT_ZUSAMMENFASSUNG.md`, §-Verweise) · `docs/REVYR-Vision-Canvas-PRD.md` · `docs/REVYR-Plan-PRD.md` (Traceability) · Plan 1 in TDD-Tiefe (`2026-07-10-tracking-and-planned-routes.md`) · HTML-Übersicht (Artifact „REVYR — App-Übersicht").
> **Detailpläne:** Alle weiteren Pläne (2–17) werden unmittelbar vor Umsetzungsbeginn nach dem Muster von Plan 1 detailliert.

**Stand:** 2026-07-16 (Einzel-Reviere: emergente Geometrie + Übernahme a–d; Sensor-Plausibilität; Sportplatz-Challenges G-12 inkl. Bahngold ✅) · **Status:** Endgültiger Planungsstand, keine Umsetzung begonnen

---

# 0. App-Name: REVYR (Vorschlag)

**REVYR** — abgeleitet vom deutschen Wort **„Revier"**: das eigene Gebiet, der Heimatgrund, das Territorium, das man kennt, pflegt und verteidigt.

- **Territory:** „Das ist unser Revier" — die Areal-Eroberung ist im Namen angelegt
- **Lokal:** Ein Revier ist immer *hier* — passt zum Ziel realer lokaler Sportnetzwerke
- **Beide Sportarten:** Läufer und Radfahrer haben gleichermaßen ihr Revier
- **Markenfähig:** kurz, aussprechbar (RE-VIER / re-VYRE), Wortmarke + Icon-Monogramm „R"

Claim: **„REVYR — Dein Revier. Deine Community."** / englisch „Own your ground."

**Ehrlicher Prüfvermerk (aktualisiert 2026-07-17, Vorrecherche):** Die Kollisionslage hat sich gegenüber dem Stand 2026-07-10 deutlich verschärft:

- **„Veyr" (veyr.fit)** ist seit 2026 eine aktive **Fitness-App** (iOS + Android, „Fitness Intelligence Engine") — phonetische Fast-Identität in **derselben Produktkategorie** (Nice-Klassen 9/41/42) = gravierendster Konflikt, Verwechslungsgefahr plausibel.
- **„Revyr" (revyr.ai):** aktive Software-Firma (UAE, Call-Recording mit eigener Android-App, Crunchbase-Profil) — identischer Name, Software-Klassenüberlappung.
- **„Revyr" (revyr.de):** aktive deutsche Marke für Jagdreisen-Vermittlung (Smyvia GmbH) — identischer Name im deutschen Markt, besetzt zudem bereits das „Revier"-Wortspiel.
- **„Revry":** Streaming-App, visuell nur ein Buchstabendreher.
- Domains: revyr.com vergeben (seit 2007), revyr.de (Jagdreisen), revyr.io registriert 03/2026; **revyr.app vermutlich frei** (kein Whois-Eintrag, keine DNS-Auflösung).
- **Beide Reserven ebenfalls belastet:** TERRIO — gleichnamige App im App Store + „TERRIO Therapy-Fitness" (US-Fitness-Firma seit 1998) · AREVO — Arevo Inc., 3D-gedruckte Carbon-Bikes („Superstrata"), direkte Bike-Nähe.

**Konsequenz:** REVYR ist als Marke hochriskant. Vor Beauftragung der (weiterhin zwingenden) professionellen Recherche (DPMA/EUIPO/USPTO) muss die Namensfindung um neue Kandidaten erweitert werden — Geld erst in die juristische Prüfung eines tragfähigen Kandidaten stecken. Bis dahin bleibt REVYR reiner Arbeitstitel.

---

# 1. Produktidentität

## 1.1 Was REVYR ist

**REVYR ist eine Health-App** — die erste, die Gesundheit, Wettkampf und echte lokale Gemeinschaft zu einem Spiel verbindet:

> Die Health-App für Läufer und Radfahrer, die dein Training versteht, dich mit deiner lokalen Sport-Community verbindet — und deine Stadt zum Spielfeld macht.

**Prioritätenordnung (verbindlich):**
1. **Health zuerst** — Tracking + verständliche Belastungsanalyse, vollwertig ab v1.0
2. **Challenges & Spiel** — Fortschritt, Seasons, Areale als Motivationsmaschine
3. **Social & Live** — Verbinden, Folgen, Live-Map mit Avataren, Teams, reale Treffen

## 1.2 Die USPs

| USP | Kurzbeschreibung | Kein Wettbewerber hat |
|---|---|---|
| **Erklärbarer Health-Score ohne Abo/Hardware** | Jeder Wert zeigt auf Tipp das *Warum* | Whoop/Garmin: Blackbox + Abo |
| **Areale + Seasons** | Teams erobern reale Stadtgebiete auf der Karte; Einzeluser erobern eigene Runden-Reviere und sammeln Spuren + Local-Hero-Kronen | Strava: nur Segmente |
| **Team-Wachstums-Loop** | Teamgröße = Spielbrett-Größe; Wachstum ist Spielmechanik | niemand |
| **Reale Treffen als Ziel** | Gemeinsame Aktivitäten, Events, Geschlossenheits-Boni | alle rein digital |
| **Avatar-Identität nur durch Leistung** | Jedes Element ist ein Leistungsbeweis, nichts kaufbar | Kosmetik sonst = Kaufware |
| **Mind & Body** | Stimmungs-Check-in + Trainings-Korrelation | keine Sport-App |
| **Beschützer-Modus & Sturzerkennung** | Live-Sicherheit ohne Zusatzhardware | Garmin: nur mit Gerät |
| **Zwei vollwertige Oberflächen** | Run- und Bike-Modus mit eigener Logik, Metrik, Skalierung | Bike sonst Anhängsel |

## 1.3 Zielgruppen (§2)

- **Runner/Jogger:** tracken, Leistung verstehen, Strecken entdecken, lokal vergleichen, gemeinsam laufen
- **Radfahrer/Rennradfahrer:** längere Distanzen, feste Stammstrecken, Sensorik, Gruppenausfahrten
- Beide erhalten **durchgehend getrennte** Aktivitätsarten, Statistiken, Rankings, Challenges, Rekorde und Oberflächen — bei identischer Produktlogik.

---

# 2. Design-System: Schwarz-Weiß, futuristisch, sportlich-spielerisch

**Designprinzip: „Farbe muss man sich verdienen."** Die App ist konsequent monochrom — Farbe existiert nur, wo sie Bedeutung trägt: Teamfarben auf der Karte, der Health-Status und die Feier-Momente. Jede Farbe wirkt dadurch wie eine Belohnung.

## 2.1 Farbwelt

| Ebene | Definition |
|---|---|
| **Dark Mode (Standard)** | Echtes Schwarz `#000000` (OLED), Weiß `#FFFFFF`, 4 Graustufen (`#8A8A8E`, `#3A3A3C`, `#1C1C1E`, `#0D0D0D`) |
| **Light Mode** | Weiß `#FFFFFF`, Tiefschwarz `#0A0A0A`, gespiegelte Graustufen |
| **Bedeutungsfarben (einzige Ausnahmen)** | Teamfarben (kuratierte, farbenblind-sichere 12er-Palette) nur auf Karte/Trikots/Avataren · Einzel-Revier-Farben (frei wählbare Nutzerfarbe bzw. Bild, nur auf der Karte) · **Gold** exklusiv für Sportplatz-Challenges (erkannte Sportanlagen als goldene Flächen, nur auf der Karte) · Health-Ampel (dezente Grün/Gelb/Rot-Punkte) · Feier-Momente (Vollfarb-Konfetti als bewusster Kontrastbruch) |
| **Run-/Bike-Modus** | bleibt monochrom; unterscheidet sich durch Ikonografie + Typo-Akzent, **nicht** durch Farbe |

**Implementierungs-Regel (aus dem HTML-Mockup gelernt):** Transparente Farbflächen immer über `fill-opacity`/`rgba`-Werte lösen, nie über `color-mix()` o.ä. — CSS-Farbmischfunktionen rendern nicht überall und ließen die Karten-Areale unsichtbar werden. Gilt für alle Web-Auskopplungen (Erfolgskarten-Renderer, Beschützer-Web-Link, Marketing-Seiten).

## 2.2 Typografie & Ikonografie

- Moderne Grotesk (Variable Font; finale Wahl im Design-Task); **riesige Tabular-Ziffern** — die Zahl ist der Held jedes Screens
- Ikonen: einheitliches Outline-Set, 2px-Strich, monochrom
- Layout: großzügiger Schwarz-/Weißraum, Karten-Container 12–16px-Radius — „Schweizer Plakat trifft Sport-HUD"

## 2.3 Motion & Haptik

- Micro-Interactions: Balken füllen federnd, Zahlen zählen hoch
- **Haptik-Vokabular** (expo-haptics): Tick = Fortschritt, Doppel-Impuls = Meilenstein, kräftiges Muster = Eroberung/Level-Up
- Lottie für Feier-Momente (Konfetti, Medaillen, Areal-Umfärbung)
- Avatare als einzige dauerhaft verspielte Elemente in der strengen Monochromie

## 2.4 Accessibility & Plattformkonventionen

- WCAG-AA-Kontraste, Dynamic Type/Font Scaling, VoiceOver/TalkBack-Labels
- Teamfarben nie einziger Informationsträger (immer + Logo/Name auf dem Areal)
- iOS: Live Activities/Dynamic Island, Haptik-Konventionen · Android: Widgets, saubere Foreground-Notification

---

# 3. Die zwei Oberflächen: Run-Modus & Bike-Modus

Home-Screen oben: Umschalter **🏃 RUN | 🚴 BIKE** — er stellt die gesamte App um. Eine Architektur, zwei Erlebnisse.

## 3.1 Was der Modus umschaltet

| Element | RUN | BIKE |
|---|---|---|
| Kernmetrik | **Pace (min/km)** | **Geschwindigkeit (km/h)** |
| Sekundärmetriken | Distanz, Zeit, HF, Kalorien | + **Trittfrequenz, Höhenmeter, Steigung** |
| Avatar | Runner-Form | Biker-Form (auf dem Rad) |
| Routing-Profil | foot-walking | cycling-regular |
| Routenplaner-Maßstab | ~5 km Umkreis, Ziele 3–25 km | ~15 km Umkreis, Ziele 15–150 km |
| Rankings/Challenges/Rekorde | nur Run | nur Bike |
| Auto-Pause | < 2 km/h für 10 s | < 4 km/h für 10 s |
| GPS-Sampling | distanceInterval 5 m | 10–15 m |
| Wochenrückblick/Home-Stats | Run-Daten | Bike-Daten |

## 3.2 Bike-spezifische Logik (verbindlich)

Radfahrer legen die 2,5–4-fache Distanz zurück — **jede km-Mechanik braucht Sport-Skalierung:**

1. **Effort-Normalisierung:** `Effort = Meter × Sportfaktor` — Start **Run 1,0 / Bike 0,4**, final kalibriert in der Pflicht-Simulation (12.1). Rein sportinterne Wertungen bleiben in echten km.
2. **Getrennte Schwellen überall:** Challenge-Ziele („25 km laufen" / „80 km fahren"), Meilensteine, Avatar-Unlocks, Areal-Mindestbeiträge (Run 300 m / Bike 800 m).
3. **Stammstrecken-Realität:** Bike-Modus stellt gespeicherte Routen + Streckenrekorde prominenter dar.
4. **Sensorik:** Trittfrequenz-/Speed-Sensoren (BLE) sind Bike-Kernfeatures; Höhenprofil ist Bike-Standardansicht.
5. **Sicherheit:** Sturzerkennung primär Bike.

## 3.3 Technische Umsetzung

- Globaler `sport-mode-store` + **Konfigurationsobjekt je Sportart** — Screens lesen Config, keine doppelten Screens
- Modus wird gemerkt; Onboarding fragt Hauptsport; Datentrennung `'run' | 'ride'` zieht sich bis in die Oberfläche

---

# 4. Kernsysteme (verbindliche Spezifikationen)

## 4.1 Tracking & Health (Fundament, ab v1.0)

**Tracking (§3, §6):** Modus A (*Einfach starten*) und Modus B (*Geplante Route/km-Ziel*) — Plan 1. Robustheit (Hintergrund-GPS, Crash-Recovery, Pause/Auto-Pause, GPS-Filter, GPX-Export) — Plan 2.

**Health-Basis ab v1.0:**
- **Herzfrequenz** live + Verlauf + Ø (HealthKit / Health Connect / BLE-Gurt), **Kalorien**, Intensität
- **Erklärbarer Belastungs-Score:** Score aus HF-Zonen × Dauer × Dichte. **Pflicht: Jeder Score ist antippbar und nennt seine Gründe** („Hoch, weil: 3 intensive Einheiten in 4 Tagen; Ø-HF 12 über deinem Normal"). Der Health-USP und zugleich die Claims-Absicherung.
- **HF-Zonen-Coaching:** Zonen geschätzt, manuell korrigierbar; optionale Live-Ansage („Zone 4 — für deinen lockeren Lauf zu schnell"), deaktivierbar
- **Stimmungs-Check-in:** 1 Emoji-Tap nach jeder Aktivität; ab ~4 Wochen Korrelations-Karten
- **Einfache Steigerungs-Warnung:** Wochen-km vs. 4-Wochen-Ø, > 30 % → Hinweis (Orientierung)
- **Home = Health-Screen:** Wochenzustand oben, Start darunter

**Später (Stufe E):** Regenerations-/Schlafempfehlungen (§8) nach juristischer Claims-Freigabe · Team-Health (Stufe C) · Hitze-/Trinkwarnung · Zyklus (Opt-in) · volle ACWR-Warnung.

**Harte Grenzen:** Alles als *Orientierung* (freigegebene Sprachliste, 16.0). Health-Daten nie für Werbung/Dritt-Analytics, lokal wo möglich.

## 4.2 Routen & Empfehlungen (§4, §21–25)

- **Planen:** Wegpunkt-Tippen oder km-Ziel (Plan 1); Fingerskizze als Spike (Plan 5) mit Wegpunkt-Fallback; Audio-Navigation deaktivierbar (§5)
- **Neue-Strecke-Erkennung:** Track-Abgleich mit Historie → „Neue Strecke für dich!"
- **Empfehlungs-Flow:** Favorit ⭐ → optional Empfehlung posten: **Besonderheiten-Chips** (Natur, See, Wald, flach, hügelig, beleuchtet, ruhig, Stadt, Aussicht, Wildlife …) + Freitext. Chips sind Schreibhilfen, gespeichert wird Text — konzepttreu zu §24
- **Verbreitung:** Post an Follower (Kartenbild, Distanz, Höhenmeter, Fotos); ansehen, liken, kommentieren, favorisieren, **mit einem Tipp übernehmen**; Team-Streckenpool (§22)
- **Bike:** Empfehlungen mit Höhenprofil + Belagshinweisen

## 4.3 Avatare & Progression

**Grundgesetz: Jedes Avatar-Element ist ein Beweis echter Leistung — nichts ist kaufbar** (mind. bis v3.0; Änderung nur als bewusste Entscheidung mit Store-Prüfung).

- **Start (v1.0):** Standard-Avatare (Basisfiguren; Hautton, Frisur frei) — je **Runner-Form** und **Biker-Form**, wechselt mit Modus
- **Unlocks (ab v2.0):** Rangstufen/Diamantgrade schalten Avatar-Stufen frei; konkrete Erfolge → konkrete Items: 21,1 km → Halbmarathon-Medaille · 52-Wochen-Streak → goldene Schuhe (Run)/Felgen (Bike) · 1.000 Rad-km → Ärmelstreifen · Local-Hero-Krone → tragbare Season-Krone
- **Team-Harness:** Teamstufen (§16) schalten **Team-Trikots** (Teamfarbe + Logo) für alle Mitglieder frei; **Season-Sieger-Designs kommen nie wieder**
- **Seltenheit:** Standard / Selten / Episch / **Season-exklusiv**
- **Technik:** geschichtete 2D-Assets, zur Laufzeit komponiert; `avatar_items (slot, rarity, sport_form, unlock_trigger)` + `user_unlocks`; kein 3D

## 4.4 Teams: Gründung, Beitritt, Wachstum (§14–17)

**Gründung (technisch):** Client- **und** Server-Validierung (Name: Länge, Eindeutigkeit, Wortfilter) → **eine Transaktion** legt `teams` + `team_members (role:'admin')` an — nie ein Team ohne Admin → sofort erster Einladungs-Token.

```
teams          (id, name, logo_url, color, admin_user_id, level, created_at)
team_members   (team_id, user_id, role: 'admin'|'member', joined_at)
team_invites   (id, team_id, token, active, expires_at?, created_by)
```

**Beitritt:** Link `https://revyr.app/join/<token>` als Universal/App Link → Join-Screen; **QR-Code** = gerenderter Link; Admin kann Token deaktivieren/neu erzeugen/befristen (§15). NFC/BLE bewusst verschoben.

**Wachstums-Maschine („ein größeres Reich braucht mehr Bürger"):**

| Mechanik | Regel |
|---|---|
| **Kapazitätsregel** | Team hält max. `3 Areale × aktive Mitglieder` — Revier ausdehnen ⇒ wachsen. „Aktiv" = ≥ 1 Aktivität/28 Tage ⇒ Karteileichen bringen nichts |
| **Verfalls-Druck** | Areale ohne Verteidigung verfallen langsam — viel Fläche braucht viele Beine |
| **Teamstufen-Doppelbedingung** (§16) | Nächste Stufe = Leistung **und** Mitgliederzahl (5→8→10→12…); schaltet Trikots, Kartenbanner, Challenge-Slots frei |
| **Mentor-Bonus** (§17) | Werber-Bonus erst, wenn der Neue **3 Aktivitäten** + **1× gemeinsam** trainiert hat |
| **Integrations-Quest** | Neues Mitglied startet automatisch „Nehmt X mit auf eine gemeinsame Aktivität" |
| **Team-Suche** | „Offen für Mitglieder" → lokale Suche (Ø-Pace, Trainingstage, Revier) |

**Team-Kommunikation:** v3.0 nur Admin-Pinnwand + Feier-Feed; kein Chat.

## 4.5 Territory: Areale & Seasons (§20 — das Herzstück)

### Was ein Areal ist (verbindliche Darstellungs-Spezifikation)

**Areale sind reale Stadtgebiete auf der echten Karte** — ein Park, ein Viertel, ein Uferabschnitt. Für Nutzer gibt es keine sichtbaren Zellen oder Hexagons:

- **Anzeige:** Auf der Stadtkarte (Straßen, Fluss, Park sichtbar) liegt das Areal als zusammenhängende Fläche in **Teamfarbe** — halbtransparente Füllung (~35 %) mit Vollfarbrand, **Teamname/Logo als Label direkt auf dem Areal**, Level und Verteidigungsstatus auf Tipp.
- **Umkämpfte Areale** werden gestrichelt umrandet und zeigen den Eroberungs-Fortschritt in % direkt auf der Karte („STADTPARK · 68 %").
- **Local-Hero-Krone** sitzt als Marker auf dem Areal des aktivsten Einzelsportlers.
- **Interne Berechnung:** Unter der Haube arbeitet ein H3-Hexagon-Raster (gleiche Flächengrößen, effiziente Track-Zuordnung). Rasterzellen werden entlang realer Grenzen (Straßenzüge, Fluss, Parkränder) zu benannten Arealen gruppiert. **Das Raster ist reine Recheneinheit und für Nutzer niemals sichtbar** — Nutzer sehen und erobern Areale.

### Zwei getrennte Ebenen (verbindlich)

- **Team-Ebene = Areal-Besitz.** Nur Teams nehmen Areale ein und verteidigen sie — und nur gemeinsam (Quorum).
- **Einzeluser-Ebene:** (a) **Einzel-Reviere:** eigene Runden-Territorien (Spezifikation unten) — strikt getrennt von den Team-Arealen. (b) **Persönliche Spuren:** „meine erlaufenen/erfahrenen Gebiete" — nur für mich + Follower. (c) **Local-Hero-Krone:** aktivster Einzelsportler pro Areal und Season, getrennt Run/Bike.
- **Karten-Layer:** *Team-Areale* / *Einzel-Reviere* / *Sportplatz-Challenges (gold)* / *Meine Gebiete* / *Local Heroes* / *Live-Sportler*. Alle Territorien-Layer sind per **Filter vollständig abschaltbar** — dann zeigt die Karte nur die Live-Sportler mit aktiver Freigabe; beim Herauszoomen werden mehr Live-Sportler über die gesamte Karte sichtbar (Cluster-Aggregation); Einschalten des Revier-Filters bringt die Farben zurück. Die Team-Ebene bleibt der **Gründungs-Funnel**: Solo-Nutzer sehen überall Teamfarben — „Gründe ein Team und nimm dieses Areal ein."

### Einzel-Reviere: Runden-Territorien einzelner Sportler (verbindlich)

Auch ein einzelner Runner/Biker kann Territorium einnehmen — aber nur die Fläche, die er tatsächlich **umrundet**. **Grundgesetz: Einzel-Reviere sind emergent — es gibt keine vordefinierten Einzel-Gebiete.** Der Läufer definiert sein Revier selbst: Die Geometrie ist exakt die Fläche, die seine Runde umschließt, und verändert sich ausschließlich durch tatsächlich gelaufene Runden (wachsen, verschmelzen, angeschnitten werden). Nur Team-Areale sind vordefinierte reale Stadtgebiete. Das System ist vollständig getrennt von den Team-Arealen: eigene Karten-Ebene, eigene Wertung, kein Einfluss auf Team-Besitz.

```
Einzel-Revier eingenommen, wenn ALLES erfüllt:
1. Ziel-Bindung:  Aktivität mit vorab festgelegtem Ziel gestartet (km-Ziel oder
                  geplante Runde, Modus B) — das Ziel ist NIE ein fester Ort;
                  Start- und Zielpunkt liegen nirgendwo fest; spontane Tracks zählen nicht
2. Runden-Regel:  Track bildet eine geschlossene Runde und umschließt eine Fläche
                  – Start-/Endpunkt ≤ 200 m auseinander
                  – umschlossene Fläche ≥ Mindestfläche (Run 0,03 km² / Bike 0,15 km²*)
                  – gerade Linie hin und zurück umschließt nichts → zählt NIE
3. Unberührtes Gebiet: noch nie umrundet → gehört dem Läufer
                  (Σ Runden-Effort ≥ Basis-Schwelle, sport-normalisiert)

Übernahme fremder Reviere — der Herausforderer sieht das Gebiet in Besitzerfarbe
auf seiner Karte und kann es beanspruchen:
a) GRÖSSERE RUNDE:  die eigene Runde umschließt das fremde Revier komplett und hat
                    mehr Runden-km als die Verteidigungs-Runde des Besitzers*
                    → Revier wechselt komplett und verschmilzt mit dem eigenen Gebiet
b) MEHR KM ODER BESSERE ZEIT im selben Feld: mehr Runden-km im Revier als der
                    Besitzer (laufende Season) ODER dessen beste Runden-Pace
                    unterbieten (bei vergleichbarer Distanz) → Revier wechselt
c) NACHBAR-REVIERE: eine Runde kann mehrere angrenzende Reviere zugleich
                    umschließen → alle werden gemeinsam übernommen (Regel a je Revier)
d) TEIL-ÜBERNAHME:  die eigene Runde dringt in ein fremdes Revier ein und
                    vergrößert das eigene angrenzende Revier mit einem größeren
                    Lauf* → nur die überlappte Teilfläche wechselt den Besitzer;
                    das fremde Revier wird beschnitten — fällt sein Rest unter
                    die Mindestfläche, fällt es komplett

Geometrie:    Reviere sind dynamische Flächen — sie wachsen, verschmelzen und werden
              angeschnitten, ausschließlich durch tatsächlich gelaufene Runden.
Verteidigung: Der Besitzer hält/vergrößert sein Revier durch eigene Runden (km
              nachlegen, Bestzeit verbessern); ohne Aktivität verfällt sein
              km-Vorsprung wöchentlich.
Wettbewerb:   Rangliste (Top 3) je Revier nach Runden-km + Bestzeit; die Historie
              wandert bei Übernahmen mit der Fläche.
Seasons:      gelten auch für Einzel-Reviere — Reset nur des Spielbretts,
              Archiv im persönlichen Trophäenschrank (season_records).
* „größer" = mehr Runden-km als die letzte einnehmende/verteidigende Runde des
  Besitzers — Startwerte, final kalibriert in der Pflicht-Simulation (12.1)
```

- **Startpunkt-Freiheit (Übernahme-Fairness):** Der Startpunkt ist **nie** Teil der Wertung — jeder startet, wo er will (die meisten vor der eigenen Haustür). Es zählt allein die **umschlossene Fläche**; Anfahrts- und Rückwege zählen nicht zur Runde, gewertet werden nur Runden-km im umrundeten Gebiet. Bei jeder Übernahme wandert die Revier-Historie (Top-3-Rangliste, Rekorde) mit der Fläche; vollständig absorbierte Reviere werden im Trophäenschrank des alten Besitzers archiviert. Nicht überlappende Rest-Flächen einer Runde bilden ein eigenes neues Revier, wenn sie selbst die Mindestfläche erfüllen.
- **Sensor-Plausibilität (Anti-Täuschung):** Für alle Revier- und Rekord-Wertungen vergleicht das System durchgehend Pace mit **Schritt-Kadenz (Pedometer), Herzfrequenz und Kalorienverbrauch**. Lauf-Tempo ohne Schritte, ohne plausible HF/Kalorien (Rad statt Lauf, Auto) → **Täuschungsversuch**: Aktivität wird `verified=false` markiert und zählt nirgends. Fehlende Sensoren allein sind kein Betrug, senken aber die Beweiskraft (Details + Schwellen in 10.2).
- **Darstellung:** individuelle Revier-Farbe (frei wählbar, nicht aus der Team-Palette) **oder ein Bild** als Füllung. Bilder sind UGC → Moderations-Pipeline (8.4) ist Voraussetzung; bis dahin nur Farbe.
- **Revier-Detail (Tipp aufs Revier):** Besitzer (Avatar + Name gemäß Sichtbarkeit) · **Top-3-Rangliste** je Revier (Runden-km + Bestzeit) · Fortschritt laufender Angriffe („noch 500 m bis zur Einnahme") · **Live-Tracking:** aktuell dort aktive Sportler als bewegte Avatare — ausschließlich mit aktiver Live-Freigabe (13.1/13.2), nie ohne Opt-in.
- **Sichtbarkeit & Privacy:** pro Nutzer wählbar (öffentlich/Follower/privat), **Standard: Follower**. Der serverseitige Wettbewerb läuft unabhängig von der Sichtbarkeit; nicht sichtbare Besitzer erscheinen Dritten anonymisiert („eingenommen"). Runden-Reviere verraten Wohngebiet/Routine → Pflicht-Aufnahme ins Threat-Model (13.1); Start-/Endpunkt-Unschärfe gilt auch hier.

### Eroberungs-Mechanik (kein Zeitdruck — es zählen Kilometer)

```
Areal erobert, wenn BEIDES erfüllt:
1. Effort-Ziel:   Team sammelt X Effort IM Areal
                  X = Basis × (1 + Verteidigungslevel × 0,5)
                  Effort = Meter im Areal × Sportfaktor (Run 1,0 / Bike 0,4*)
2. Beteiligung:   ≥ Q verschiedene Mitglieder haben beigetragen
                  Q = max(2; 30 % der aktiven Mitglieder; Deckel 8)

Zusatzregeln:
- Mindestbeitrag pro Aktivität & Areal: Run ≥ 300 m / Bike ≥ 800 m   (kein „Antippen")
- Einzeldeckel: max. 40 % des Areal-Ziels von einer Person            (kein Solo-Carry)
- GESCHLOSSENHEITS-BONUS: ALLE aktiven Mitglieder tragen bei
  → ×1,5 auf den Effort + exklusive Team-Medaille
- Verteidigung: Besitzer-Effort im eigenen Areal erhöht das Verteidigungslevel
- Verfall: ohne Verteidigung sinkt das Level wöchentlich
- Mehrere Angreifer: Live-Leaderboard pro Areal („Rennen um den Stadtpark")
- Beiträge bleiben beim Team, auch wenn ein Mitglied geht
- Offline-Aktivitäten zählen mit Original-Zeitstempel innerhalb der Season
* Startwerte — final kalibriert in der Pflicht-Simulation (12.1)
```

### Tracking-Pipeline (kein neues Tracking — reine Server-Auswertung)

```
Aktivität gesynct → [1] Anti-Cheat (nur verifizierte zählen)
→ [2] Gefilterter Track wird dem Raster zugeordnet, Rasterzellen → Areal-Beiträge
→ [3] territory_contributions (activity_id, user_id, team_id, areal_id, season_id, meters, ts)
→ [4] Aggregation: Σ Effort + COUNT(DISTINCT user) pro Areal/Team/Season
→ [5] Schwelle + Quorum erreicht? → Capture-Event: Areal färbt sich um,
      Push an beide Teams, Einnahme-Animation + Erfolgskarte
```

### Fortschritt sichtbar (Motivations-Pflicht)

Areal-Detail: „68 / 100 Effort · 4 / 5 Mitglieder" + Beitragsliste (der 2-km-Beitrag wird genauso gewürdigt wie der 20-km-Beitrag) · Nachbereitungs-Screen: „Deine 6,2 km → 3,8 zur Eroberung des Stadtparks" mit animiertem Balken · Team-Feed-Anstupser „Noch 12 km — wer macht sie voll?" · Finaltreffer bekommt einen Extra-Moment.

### Seasons (Quartalsrhythmus)

- Reset betrifft **nur das Spielbrett** — **Geschichte wird nie gelöscht**
- **`season_records`**: unveränderlicher Snapshot je Team/User (Kartenbild + Areal-Liste, Peak, Platzierung, Medaillen, Stats, Exklusiv-Items)
- **Vereinsheim (Teamprofil):** Season-Banner-Galerie („Season 3 · 14 Areale · Platz 2 in München · 2.180 Team-km") für immer · Meilenstein-Chronik (Gründung, Gründungsmitglieder, Wachstumskurve, erste Eroberung) · Season-Trikots ewig tragbar
- **Zeitreise:** Kartenmodus „Season 1…N" — Lokalgeschichte zum Durchblättern
- **Season-Finale:** Countdown-Woche → animierter **Season-Rückblick** (Wrapped-Stil) je Team und Nutzer mit Erfolgskarten-Export — der stärkste virale Moment, 4× jährlich
- **Einzeluser:** persönlicher Trophäenschrank (archivierte Kronen, Season-Stats)

## 4.6 Challenges, Punkte & Dopamin-Design (§12, §27–28)

**Punkte:** Effort-basiert (sport-normalisiert), getrennte Pfade Einzel/Team; Meilensteine, Sterne, Medaillen, Rangstufen/Diamantgrade; Formeln dokumentiert + simuliert (10.1), Vergabe idempotent.

**Wochen-Challenges (§27):** Einzel/Team × Run/Bike × Distanz/Aktivitätstage/Konstanz; sport-getrennte Ziele; Areal-Aufgaben („Nehmt den Stadtpark ein") speisen sich aus `territory_contributions` — nichts doppelt getrackt.

**Sportplatz-Rundenlauf-Challenges:** Die App erkennt Sportanlagen **automatisch auf der Karte** (OSM: Tartan-/Laufbahn, Fußballplätze, um die man herumlaufen kann). Sportplätze sind die bewusste Ausnahme vom Emergenz-Prinzip der Einzel-Reviere: **systemseitig vordefinierte Challenge-Orte**, keine Läufer-definierten Gebiete. Auf der Karte erscheinen sie als **goldene Challenge-Flächen** — der Sportplatz ist golden ausgefüllt und dadurch in der Realität sofort als Challenge-Ort erkennbar (Gold ist die dafür reservierte Bedeutungsfarbe, 2.1; gilt für alle Sportplätze). Die **Rundenlauf-Challenge startet am Sportplatz** (Geofence); gezählt werden vollständige Runden um Bahn/Platz. Die meisten Runden gelten als Extra-Challenge mit eigenen **Platz-Rekorden** (meiste Runden, schnellste Runde) und Leaderboard je Sportplatz — so entstehen echte Rekorde an realen Plätzen und Leute challengen sich beim Umrunden. Diese Runden fließen in das eigene Punktesystem **Bahngold** (✅ entschieden 2026-07-16). Strikt getrennt von Einzel-Revieren und Team-Arealen; Sensor-Plausibilität gilt auch hier.

```
BAHNGOLD — das Sportplatz-Punktesystem (eigene Währung, geschlossenes System):

Quellen:   Basispunkte je vollständige Runde (sport-getrennt) · degressiv ab
           Runde N pro Tag (Anti-Grind + Gesundheitsschutz) · Entdecker-Bonus
           beim ersten Besuch eines Platzes · Bonus für persönliche Bestzeit ·
           großer Bonus + Vollbild-Feier bei Platzrekord (meiste Runden /
           schnellste Runde) · DUELL-BONUS ×1,5, wenn andere zeitgleich am
           selben Platz laufen (belohnt reale Treffen)

Schaltet frei:
           Platz-Ränge je Sportplatz (Stammläufer → Platzmeister → PLATZKÖNIG =
           Season-Führender, Kronen-Marker auf der goldenen Fläche) · Bahn-Liga
           (Season-Leaderboard je Platz + stadtweite Liga, Run/Bike getrennt) ·
           exklusive Avatar-Items nur über Bahngold-Meilensteine (goldene
           Spikes, Bahn-Trikot — nie kaufbar) · Wochen-Bahn-Challenges
           (speisen sich aus platz_runden, nichts doppelt getrackt)

Grenzen:   Bahngold beeinflusst NIE Effort-Rankings, Reviere oder Team-Areale ·
           nur verified-Aktivitäten + Sensor-Plausibilität + physiologische
           Mindest-Rundenzeit je Anlage · Season-Reset für Bahngold und
           Platz-Ränge; schnellste-Runde-Platzrekorde bleiben ewig
           (Platz-Chronik) · Startwerte kalibriert in Pflicht-Simulation (12.1)
```

**Dopamin-Prinzipien (ab v1.0):**
1. **Einnahme-/Meilenstein-Moment:** Vollbild — Karte zoomt, Areal färbt sich live um, Konfetti (Vollfarbe als Kontrastbruch), Haptik, Sound, Erfolgskarte
2. **Progression im Reveal:** Balken füllen sich **erst beim Öffnen der App** — der Grund, sie zu öffnen
3. **Wochenrückblick** sonntags, **Season-Rückblick** quartalsweise — beide teilbar
4. **Erfolgskarten:** automatisch bei jedem Meilenstein — **„In der App feiern"** (Feed, 👏🔥🏅) + **„Teilen"** (Bild/Video extern, Gratis-Marketing). v1.0: Bild-Export; ab v2.0: + Feed
5. **Ethik:** echte Leistung feiern — kein Streak-Terror, keine Kauf-Boosts, keine Glücksspiel-Mechanik

## 4.7 Profile, Social & Live (§9–11, §19, §26)

### Profil-Logik (verbindlich, v2.0)

Jedes Profil besteht aus **verdienten Elementen**: Avatar (statt Foto-Zwang — Privacy-Vorteil), eindeutiger wortgefilterter Benutzername, Hauptsport, Rangstufe/Diamantgrad mit Fortschritt, **Run-/Bike-Statistiken getrennt**, Medaillen, Trophäenschrank (archivierte Kronen + Season-Stats), Teamzugehörigkeit mit Vereinsheim-Link. **Standard ist privat.**

**Sichtbarkeits-Matrix (Testtabelle in Plan 7):**

| Profil-Inhalt | Öffentlich | Nur Follower | Privat (Standard) |
|---|---|---|---|
| Name, Avatar, Hauptsport, Team-Badge | ✓ | ✓ | ✓ |
| Rangstufe, Medaillen, Trophäenschrank | ✓ | ✓ | — |
| Aktivitäten & km-Statistiken (Run/Bike getrennt) | ✓ | ✓ | — |
| Geteilte Routen-Empfehlungen | ✓ | ✓ | — |
| Persönliche Spuren-Karte | — | ✓ | — |
| Live-Position | nur per Opt-in je Aktivität — nie über das Profil-Level hinaus; Start-/Endpunkte immer unscharf | | |

**Follow-Flow:** öffentliches Profil → „Folgen" wirkt sofort · privates Profil → „Follower-Anfrage" mit Annehmen/Ablehnen (bis dahin nur Name/Avatar/Team) · **Blockieren** wirkt beidseitig sofort überall (Feed, Suche, Rankings, Live-Map, Kommentare) · **Melden** auf jedem Profil/jeder Route/jedem Kommentar → Moderations-Queue.

### Live & Safety

- **Live-Map mit Avataren (§11):** Freigebende erscheinen als **bewegter Mini-Avatar**; Antippen → Mini-Profilkarte (Avatar, Name, Pace/Speed, gelaufene km, **km-Ziel/geplante Distanz** — nie die geplante Route selbst, Team-Trikot, **Einnahme-Status**: „nimmt gerade Revier/Areal X ein · noch 500 m") mit **Folgen/Anfrage**. Der Einnahme-Status ist Teil derselben Live-Freigabe (gleiches Opt-in). Opt-in pro Aktivität, erzwungenes Zeitlimit, Sichtbarkeitsstufen (alle in der Nähe/Follower/Team), Indikator, Not-Aus, Start-/Endpunkt-Unschärfe
- **Beschützer-Modus:** Vertraute Person (ohne Account, Web-Link) sieht Live-Standort + „gut angekommen" — unabhängig von der öffentlichen Live-Map
- **Sturzerkennung (primär Bike):** Beschleunigungsmuster → Countdown → Notfallkontakt + Standort; Assistenz-Sprache, nie Garantie
- **Gemeinsame Aktivität (§36 #7):** gleiche Zeit ±, räumliche Nähe über ≥ X % der Aktivität, ≥ 2 Teammitglieder — pure, getestete Funktion
- **Community/Team Runs & Rides (§19), lokale Events (§26):** planen (Zeit, Treffpunkt, Route, Teilnehmer), entdecken, teilnehmen, Erinnerungs-Push; Event-Teilnahme zählt als gemeinsame Aktivität; Moderation inklusive
- **UGC-Sicherheit (Store-Pflicht):** Melden + Blockieren auf jedem Element, Moderations-Queue mit Admin-Interface, Community-Regeln mit Erst-Zustimmung, Wortfilter

---

# 5. Zielarchitektur

## 5.1 App

- **Stack:** Expo (React Native, TypeScript strict), expo-router, zustand, Jest/jest-expo/Testing Library; Dateien < 500 Zeilen; unveränderliche Updates; Validierung an Systemgrenzen; keine Secrets; deutsche UI (i18n-vorbereitet)
- **Modulschnitt:** `app/` Screens · `src/domain/` pure Logik (**alle** Formeln: Distanz, Pace, Effort, Punkte, Areale, Zonen, Belastung — testbar & simulierbar) · `src/services/` GPS/Routing/Backend/Health/BLE · `src/db/` lokale Persistenz + Sync-Queue · `src/state/` Stores · `src/config/` Sport-Konfigurationen, Design-Tokens
- **Plattform:** Live Activities + Dynamic Island (iOS), Foreground-Service + Widgets (Android), Universal/App Links, Haptik, Lottie

## 5.2 Backend (Entscheid in Plan 6.0)

Anforderungen: Auth (E-Mail/Apple/Google), Postgres-artig mit **Geo-Queries** (Radius-Rankings, Areal-Zuordnung), Realtime (Live-Map, Areal-Rennen), Push, Storage, EU-Region/DSGVO, Row-Level-Security. Kandidaten: **Supabase** (Prüf-Empfehlung: PostGIS), Firebase, Eigenbau. Entscheid per Prototyp: „Ranking im 10-km-Radius" + „Sign in with Apple" müssen laufen → ADR.

## 5.3 Datenmodell (Zielbild)

```
users, auth_identities, devices(push_tokens)
activities (sport, startedAt, duration, distance, points[], hf[], steps, kcal, plannedDistance?, verified)
mood_checkins · health_baselines (ruhe_hf, zonen)
routes, route_posts (beschreibung, chips_text[], fotos), route_saves, likes, comments
follows (status: accepted|requested) · blocks · reports · moderation_queue
avatar_items (slot, rarity, sport_form, unlock_trigger) · user_unlocks · team_gear
teams, team_members, team_invites, team_quests, team_announcements
seasons
areale (areal_id, name, geometry, raster_cells[], season_id,
        owner_team_id, color, level, points, last_defended_at)
territory_contributions (activity_id, user_id, team_id, areal_id, season_id, meters, ts)
einzel_reviere (id, user_id, geometry, color|image_url, level, season_id,
                points, last_defended_at, visibility)
einzel_revier_contributions (activity_id, user_id, revier_id, season_id, effort, ts)
sportplaetze (osm_id, name, geometry, typ: bahn|platz)
platz_runden (activity_id, user_id, platz_id, season_id, runden, beste_runde_s)
bahngold_vergaben (activity_id, user_id, platz_id, season_id, punkte, quelle)
season_records (season_id, owner_type, owner_id, territory_snapshot, peak, rank,
                medals[], stats, exclusive_items[])
challenges, challenge_progress · rankings (materialisiert je Radius/Sport)
events (typ, zeit, treffpunkt, route_id) · event_participants
live_sessions (activity_id, visibility, expires_at) · guardians · emergency_events
```

## 5.4 Karten & Routing

Stufe A: react-native-maps (Apple Maps iOS / Google Android) + OpenRouteService (foot-walking / cycling-regular). **Anbieter-Review vor Stufe B** (Kosten: Google-Preise, ORS-Limits; Alternativen Mapbox, MapLibre+OSM) → ADR. **Areal-Rendering:** Polygon-Overlays der Areal-Geometrien nur im Viewport; bei niedrigen Zoomstufen Aggregation benachbarter Areale desselben Teams (Messkriterium: flüssig bei 1.000+ Arealen).

---

# 6. Release-Fahrplan

| Version | Stufe | Kern | Pläne |
|---|---|---|---|
| **v1.0** | A — Health-Tracker | Tracking robust + **Health-Basis** + Run/Bike-Oberflächen + S/W-Design + Basis-Avatare + Dopamin-Basis + Erfolgskarten-Export | 1–5 |
| **v2.0** | B — Plattform | Accounts, Profile (inkl. Sichtbarkeits-Matrix) + Avatar-Unlocks, Follow, Routen-Empfehlungen, Feed + In-App-Feiern, UGC-Safety | 6–8 |
| **v3.0** | C — Gemeinschaft | Teams + Wachstums-Maschine, Punkte/Rankings + Anti-Cheat, Challenges, gemeinsame Aktivitäten, Team-Health | 9–11 |
| **v4.0** | D — Spielfeld | Areale + Seasons + Vereinsheim, Live-Map + Avatare, Beschützer-Modus, Sturzerkennung, Events | 12–14 |
| **v5.0** | E — Begleiter | Wearables/Watch, Regeneration (nach Claims-Freigabe), KI-Coach, Wetter/Hitze, Zyklus (Opt-in) | 15–17 |

Keine Stufe beginnt vor dem Evidence-Gate der vorherigen (Abschnitt 9). §33-Visionen (AR, Smart Glasses, virtuelle Rennen) liegen außerhalb dieses Plans.

---

# 7. Arbeitspakete Plan 1–17

## Stufe A — Health-Tracker (v1.0)

### Plan 1: Tracking + geplante Routen + Verlauf ✔ geschrieben
TDD-Detailplan liegt vor (`2026-07-10-tracking-and-planned-routes.md`, 12 Tasks): Modus A, Modus B, Verlauf. Bleibt unverändert gültig.

### Plan 2: Robustes Tracking *(braucht Expo Dev-Build)*

| Task | Inhalt | Abnahme |
|---|---|---|
| 2.1 | EAS-Dev-Build; iOS Background Mode `location`; Android Foreground-Service | Build auf echtem iPhone + Android |
| 2.2 | Hintergrund-Tracking (expo-task-manager) in denselben Session-Store | 30 min, Bildschirm gesperrt, lückenlos |
| 2.3 | GPS-Filter `src/domain/gps-filter.ts` (Genauigkeitsschwelle, Ausreißer) | Unit-Tests mit Drift-/Sprung-Fixtures |
| 2.4 | Crash-Recovery: periodische Persistenz, „Aktivität fortsetzen?" | App-Kill ohne Punktverlust |
| 2.5 | Pause/Resume + Auto-Pause (sport-spezifisch, 3.1) | Pausenzeit nicht in Pace/Speed |
| 2.6 | Sport-Konfigurationsobjekte (`src/config/sport.ts`) | beide Modi nutzen Config, kein Hardcoding |
| 2.7 | Routen speichern/benennen/favorisieren, erneut starten; **Streckenrekord-Vergleich** | Route wiederverwendet, Vergleich angezeigt |
| 2.8 | GPX-Export (Share Sheet) | Fremd-App öffnet Datei |
| 2.9 | Batterie-Messlauf 1 h je Sport + Plattform | Ledger mit Messwerten |

### Plan 3: Health-Basis

| Task | Inhalt | Abnahme |
|---|---|---|
| 3.1 | HealthKit/Health Connect: HF lesen, Workout schreiben; Berechtigungen einzeln begründet | HF-Verlauf echter Aktivität, iOS + Android |
| 3.2 | BLE-Brustgurt (HF live) | realer Gurt aufgezeichnet |
| 3.3 | HF-Zonen `src/domain/health/zones.ts` + Kalorien + Schritt-/Kadenz-Erfassung (Pedometer) je Aktivität | Unit-Tests; Schritte echter Aktivität plausibel |
| 3.4 | **Erklärbarer Belastungs-Score** + „Warum?"-Sheet | jeder Score nennt Gründe; Formeln dokumentiert |
| 3.5 | Stimmungs-Check-in + Korrelations-Karten | Check-in < 2 s; Korrelation korrekt (Fixtures) |
| 3.6 | Steigerungs-Warnung (> 30 %, Orientierungssprache) | Testtabelle |
| 3.7 | Health-Home (Wochenzustand oben) | zeigt echte Woche |
| 3.8 | Zonen-Live-Ansage (expo-speech), deaktivierbar | Kopfhörer-Test, Schalter wirkt |

### Plan 4: Identität & Erlebnis (Design, Modus, Avatare, Dopamin)

| Task | Inhalt | Abnahme |
|---|---|---|
| 4.1 | Design-System `src/config/theme.ts`: S/W-Token, Dark (echtes Schwarz) + Light, Typo, Ikonen; **keine CSS-Farbmischfunktionen in Web-Auskopplungen** | alle Screens auf Token, beide Modi |
| 4.2 | **Run/Bike-Umschalter** + `sport-mode-store` | Umschalt-Tabelle 3.1 als Checkliste erfüllt |
| 4.3 | Basis-Avatare: Editor, Runner-/Biker-Form, lokal | Avatar auf Home + Aktivität |
| 4.4 | Dopamin-Basis: animierte Balken, Haptik-Vokabular, Meilenstein-Vollbild (Lottie) | Gerätetest fühlbar |
| 4.5 | Wochenrückblick + **Erfolgskarten-Bildexport** | Karte in Fremd-App geteilt |
| 4.6 | Live Activity/Dynamic Island (iOS), Notification-Design + Widget (Android) | Sperrbildschirm zeigt Live-Metriken |
| 4.7 | Onboarding: Hauptsport, Health-Erklärscreens, Avatar | Erstlauf < 2 min |

### Plan 5 (optional vor v1.0): Audio + Fingerskizzen-Spike

| Task | Inhalt | Abnahme |
|---|---|---|
| 5.1 | Audio-Ansagen (km, verbleibend, „Route verlassen" via `off-route.ts`), deaktivierbar | Kopfhörer-Gerätetest |
| 5.2 | **Spike (Timebox 2 Wochen):** Fingerskizze → Wegpunktkette → Routing-API; 10 reale Skizzen | Entscheidung shippen/verbessern/verschieben — Verschieben zulässig |

**→ GATE A → Store-Einreichung v1.0** (Name markenrechtlich geklärt)

## Stufe B — Plattform (v2.0)

### Plan 6: Backend-Fundament + Auth

| Task | Inhalt | Abnahme |
|---|---|---|
| 6.0 | **Backend-Entscheid** per Prototyp (Geo-Query + Apple-Login) → ADR | Ledger + ADR |
| 6.1 | Dev/Prod-Umgebungen, EU-Region, Secrets | getrennte Umgebungen |
| 6.2 | Auth: E-Mail + **Sign in with Apple** + Google; Token/Refresh | beide Plattformen |
| 6.3 | Schema v1 + versionierte Migrationen | Migrationen laufen |
| 6.4 | Offline-first-Sync (lokal = Wahrheit, Upload-Queue) | Flugmodus-Aktivität synct nach |
| 6.5 | Bestandsdaten-Migration (v1.0 → Account) | Alt-Aktivitäten im Account |
| 6.6 | **Account-Löschung in-App**, vollständig | keine Daten mehr abrufbar (Nachweis) |
| 6.7 | Rate Limiting + serverseitige Validierung | Tests + Lastprobe |

### Plan 7: Profile, Avatar-Unlocks, Follow, Push

| Task | Inhalt | Abnahme |
|---|---|---|
| 7.1 | Profile: eindeutiger Name (Wortfilter), Avatar, Hauptsport, **Run-/Bike-Stats getrennt**, Rang + Fortschritt | Anlegen/Ändern beide Plattformen |
| 7.2 | **Avatar-Freischaltsystem**: `avatar_items`/`user_unlocks`, Trigger, Seltenheit, Unlock-Vollbild | definierter Erfolg → definiertes Item |
| 7.3 | **Sichtbarkeits-Matrix aus 4.7 implementieren** (öffentlich/Follower/privat, Standard privat) | Matrix als Testtabelle, jede Zeile geprüft |
| 7.4 | Follow (öffentlich sofort) + Follower-Anfrage (privat, annehmen/ablehnen) + Feed-Grundgerüst | Feed zeigt nur Erlaubtes |
| 7.5 | **Blockieren** beidseitig sofort überall | Blockierter findet Nutzer nirgends |
| 7.6 | Push: Tokens, Opt-in je Kategorie | Push beidseitig, Opt-out wirkt |

### Plan 8: Routen-Empfehlungen, Feed-Feiern, UGC-Safety

| Task | Inhalt | Abnahme |
|---|---|---|
| 8.1 | Neue-Strecke-Erkennung | nur bei echter Neuheit |
| 8.2 | Empfehlungs-Flow: Chips + Freitext, Post an Follower | Follower übernimmt Route mit 1 Tipp |
| 8.3 | Likes, Kommentare, Sport-Reaktionen; **In-App-Feiern** im Feed | Reaktionen live |
| 8.4 | **Melden** + Moderations-Queue + Admin-Interface | Meldung → Bearbeitung → Wirkung |
| 8.5 | Community-Regeln + Erst-Zustimmung + Wortfilter | Zustimmung gespeichert, Filter greift |
| 8.6 | Streckenpool-Datenmodell generisch (`route_shares`) | deckt User→öffentlich + Team |

**→ GATE B → v2.0**

## Stufe C — Gemeinschaft (v3.0)

### Plan 9: Teams + Wachstums-Maschine

| Task | Inhalt | Abnahme |
|---|---|---|
| 9.1 | Team-CRUD (Transaktion), Farbe aus Palette, Logo | nie Team ohne Admin |
| 9.2 | Token-Lebenszyklus + Universal/App Links + QR | 2. Gerät scannt → Beitritt; Deaktivierung wirkt |
| 9.3 | Aktiv-Definition (28 Tage) + Zählung | Testtabelle |
| 9.4 | Teamstufen (Leistung + Größe) + `team_gear`-Unlocks | Stufenlogik 5→8→10→12 |
| 9.5 | Mentor-Bonus (3 Aktivitäten + 1 gemeinsame) + Integrations-Quest | Bonus erst nach Integration |
| 9.6 | Team-Suche „offen für Mitglieder" | fremdes Team gefunden + beigetreten |
| 9.7 | Admin-Pinnwand + Team-Moderation | Fälle durchgespielt |

### Plan 10: Punkte, Rankings, Anti-Cheat

| Task | Inhalt | Abnahme |
|---|---|---|
| 10.1 | **Effort-/Punkteformel** `src/domain/scoring/` + Simulation (inkl. Run-vs-Bike-Balance) | Bericht: keine Ausnutzung, Faktoren kalibriert |
| 10.2 | **Anti-Cheat serverseitig** (Maxspeed je Sport, Teleports, **Sensor-Plausibilität:** Pace vs. Schritt-Kadenz/HF/Kalorien — Lauf-Tempo ohne Schritte = Täuschungsversuch; fehlende Sensoren allein ≠ Betrug) → `verified=false` | Auto-GPS wird aussortiert; Rad-Track als „Lauf" wird aussortiert (Fixture) |
| 10.3 | Radius-Rankings (5/10/25/50 km, Stadt), sport-getrennt | deterministisch auf Fixtures |
| 10.4 | Ranking-UI + „✓ verifiziert"-Badge | 2 Testaccounts konsistent |
| 10.5 | Meilensteine/Medaillen/Ränge + Avatar-Unlock-Anbindung, idempotent | kein Doppel-Reward |

### Plan 11: Challenges, gemeinsame Aktivitäten, Team-Health

| Task | Inhalt | Abnahme |
|---|---|---|
| 11.1 | **„Gemeinsame Aktivität"** als pure Funktion | 2 echte Geräte: erkannt/nicht erkannt |
| 11.2 | Wochen-Challenges (sport-getrennte Ziele), serverkonfigurierbar | Fortschritt korrekt |
| 11.3 | Belohnungspfade Einzel/Team, idempotent | Testtabelle |
| 11.4 | Team-Streak (2/4/8/12/26/52 Wochen) + Reset (§18) | Übergangs-Testtabelle |
| 11.5 | Community/Team Runs & Rides planen (§19) | Mitglied sagt zu, Aktivität verknüpft |
| 11.6 | **Team-Health** (anonymisiert, Opt-in, nie Einzelwerte) | keine Person identifizierbar |

**→ GATE C → v3.0**

## Stufe D — Spielfeld (v4.0)

### Plan 12: Areale + Seasons + Vereinsheim

| Task | Inhalt | Abnahme |
|---|---|---|
| 12.1 | **Pflicht-Simulation** der Eroberungsformel (Raster→Areale; Quorum, Deckel, Geschlossenheits-Bonus, Verfall, Sportfaktoren, Kapazität) — Szenarien: 2er vs. 50er-Team, Run- vs. Bike-Team, Karteileichen, **Einzel-Revier-Szenarien (Mindestflächen, Runden-Regel, Übernahmen a–d inkl. Teil-Übernahme-Geometrie, Schummelrunden)** | Bericht: „Masse allein gewinnt nicht", Werte fixiert (inkl. Einzel-Revier-Startwerte) |
| 12.2 | **Areal-Definition:** Rasterzellen entlang realer Grenzen (Straßen, Fluss, Park) zu benannten Arealen gruppieren; Areal-Namen (OSM-Ortsnamen + Fallback) | Areale einer Teststadt geschnitten + benannt |
| 12.3 | Territory-Domain `src/domain/territory/` (alle Regeln aus 4.5, pur) | vollständig unit-getestet |
| 12.4 | Server-Pipeline: Track→Raster→Areal-Beiträge→Aggregation→Capture-Event; nur `verified` | Fixture-Track erobert erwartete Areale |
| 12.5 | **Areal-Rendering auf echter Stadtkarte:** halbtransparente Teamfarbe (~35 %) + Vollfarbrand, Teamname/Logo-Label auf dem Areal, umkämpfte Areale gestrichelt mit %-Anzeige, Local-Hero-Krone als Marker; Layer-Umschalter Team-Areale/Einzel-Reviere/Sportplatz-Challenges (gold)/Meine Gebiete/Local Heroes/Live-Sportler; Viewport-Loading + Zoom-Aggregation | Karte zeigt reale Areale statt Zellen; flüssig bei 1.000+ Arealen |
| 12.6 | Fortschritts-UI: Areal-Detail (Effort + Quorum + Beiträge), Nachbereitungs-Beitrag, Areal-Leaderboard, Finaltreffer-Moment | Gerätetest 2 Accounts |
| 12.7 | Persönliche Spuren + Local-Hero-Kronen (je Sport) | Krone wechselt korrekt |
| 12.8 | Seasons: Rhythmus, Finale-Countdown, `season_records`-Snapshot, Karten-Reset | Snapshot unveränderlich, Karte neutral |
| 12.9 | **Vereinsheim** + Trophäenschrank + Zeitreise + Season-Rückblick (Wrapped) mit Export | Historie nach 2 Test-Seasons vollständig |
| 12.10 | **Runden-/Flächen-Erkennung** `src/domain/territory/loop.ts`: geschlossene Runde, umschlossene Fläche, Mindestfläche, Ziel-Bindung; „Linie hin und zurück" wird abgelehnt | pure Funktion, Unit-Tests mit Runden-/Linien-/Drift-Fixtures |
| 12.11 | **Einzel-Revier-Logik + Server-Pipeline:** Einnahme (unberührtes Gebiet), **Übernahme-Regeln a–d (größere Runde / km / Zeit / Teil-Übernahme)**, dynamische Geometrie (Wachsen, Verschmelzen, Anschneiden, Mindestflächen-Kollaps), Verteidigung/Verfall, Season-Reset; strikt getrennt von Team-Arealen; nur `verified`-Aktivitäten | Fixture-Runde erobert Gebiet; Übernahme-Testtabelle a–d; Teil-Übernahme beschneidet Geometrie korrekt (Geo-Fixtures); Team-Areale nachweislich unbeeinflusst |
| 12.12 | **Einzel-Revier-UI:** Rendering in Nutzerfarbe/Bild (Bild → Moderation 8.4), Farb-/Bild-Editor, Revier-Detail (Top-3-Rangliste, Angriffs-Fortschritt, Live-Tracking nur mit Freigabe), Territorien-Filter + Live-Sportler-Zoom-Aggregation | Gerätetest 2 Accounts; Filter-Umschaltung flüssig |
| 12.13 | **Sportplatz-Rundenlauf-Challenges:** automatische Erkennung der Sportanlagen aus OSM (Laufbahn/Fußballplatz), **Darstellung als goldene Challenge-Flächen auf der Karte**, Geofence-Start am Platz, Runden-Zählung um die Anlage (nutzt 12.10), Platz-Rekorde (meiste Runden, schnellste Runde) + Leaderboard je Platz | Plätze erscheinen golden auf der Karte; Runden am realen Testplatz korrekt gezählt (Gerätetest); Rekordliste je Platz |
| 12.14 | **Bahngold-System:** Vergabe-Engine (Basispunkte je Runde, Tages-Degression, Entdecker-/Bestzeit-/Rekord-Boni, Duell-Bonus nutzt Nähe-Logik 11.1), Platz-Ränge + Platzkönig-Krone, Bahn-Liga (Platz + Stadt), exklusive Avatar-Items (idempotent, nutzt 7.2), physiologische Mindest-Rundenzeit | Vergabe deterministisch auf Fixtures; kein Doppel-Reward; Platzkönig wechselt korrekt; Duell-Bonus mit 2 echten Geräten |

### Plan 13: Live-Map, Beschützer-Modus, Sturzerkennung

| Task | Inhalt | Abnahme |
|---|---|---|
| 13.1 | **Threat-Model Standortfreigabe** + Sicherheitsmodell (Opt-in/Aktivität, Zeitlimit erzwungen, Stufen, Unschärfe, Not-Aus) | Dokument extern gegengeprüft |
| 13.2 | Live-Freigabe im Tracking + Indikator; endet in **allen** Pfaden (auch App-Kill) | Nachweis aller Endpfade |
| 13.3 | Live-Map mit **bewegten Avataren**; Tipp → Mini-Profilkarte (Pace/Speed, km, **km-Ziel**, Team, **Einnahme-Status**) → Folgen/Anfrage; Blockieren wirkt | Blockierter sieht nichts; Karte zeigt km-Ziel + Einnahme-Status |
| 13.4 | **Beschützer-Modus**: Web-Link (ohne Account) + „gut angekommen" | Link live, endet automatisch |
| 13.5 | **Sturzerkennung** (primär Bike): Muster → Countdown → Notfallkontakt + Standort | Falltest + Fehlalarmquote dokumentiert |
| 13.6 | Realtime-Kanäle je Region; Batterie/Daten gemessen | Messwerte im Ledger |

### Plan 14: Lokale Events

| Task | Inhalt | Abnahme |
|---|---|---|
| 14.1 | Event-CRUD (Nutzer/Team): Typ, Zeit, Treffpunkt, Route | Event in Umkreissuche |
| 14.2 | Entdecken + Zu-/Absage + Teilnehmer + Erinnerungs-Push | Fremdaccount nimmt teil |
| 14.3 | Event-Moderation (nutzt 8.4) | gesperrtes Event verschwindet |
| 14.4 | Event ↔ gemeinsame Aktivität (nutzt 11.1) → Boni/Streaks | Event-Lauf zählt (2 Geräte) |

**→ GATE D → v4.0**

## Stufe E — Begleiter (v5.0)

### Plan 15: Wearables & Sensoren
15.1 Apple-Watch-Companion (Start/Stopp, HF, Kernmetriken) · 15.2 Wear OS · 15.3 Bike-Sensorik voll (Trittfrequenz, Speed; Höhenprofil-Standardansicht) · 15.4 Kompatibilitätsmatrix (§36 #16). Abnahmen: echte Geräte, Ledger.

### Plan 16: Regeneration & Verletzungsprävention (Claims-gebunden)
16.0 **Juristische Claims-Prüfung** → freigegebene Sprachliste (Blocker) · 16.1 Regenerations-Auswertung (§8) nur in freigegebener Sprache + Lint-Check · 16.2 Volle ACWR-Warnung mit Quellen-Doku · 16.3 Morgens-Check-in (optional) + Trend.

### Plan 17: KI-Coach, Wetter, Zyklus
17.1 Regelbasierte, **erklärbare** Trainingsvorschläge (§29) · 17.2 Audio-Coach (deaktivierbar, §30) · 17.3 Wetter: Anbieter-Entscheid, Wetter vor Start, **Hitze-/Trinkwarnung**, Wetterfenster-Push (§31) · 17.4 **Zyklus-bewusst** (Opt-in, sensibelste Datenklasse, eigene Privacy-Prüfung) · 17.5 Lernende Pläne nur bei nachgewiesener Nutzung von 17.1.

**→ GATE E → v5.0**

---

# 8. Store Readiness — iOS & Android je Stufe

| Anforderung | Stufe/Plan | iOS konkret | Android konkret |
|---|---|---|---|
| Standort Foreground | A/1 | `NSLocationWhenInUseUsageDescription` (deutsch, ehrlich) | Runtime-Permission; Ablehnung → erklärender Zustand |
| Standort Background | A/2 | Background Mode `location` + „Always"-Begründung | **Foreground-Service** mit Notification; Play-Standort-Formular — häufigster Ablehnungsgrund, früh Testeinreichung |
| Health-Daten | **A/3** | HealthKit: jede Leseart einzeln begründet; nie Analytics/Werbung | Health Connect: Deklaration + Play-Health-Policy-Formular |
| Live Activity / Widgets | A/4 | ActivityKit-Richtlinien (nur aktive Session) | Foreground-Notification policy-konform |
| Privacy Policy + Terms | A | App Privacy Labels korrekt (Health!, Standort) | Data-Safety-Formular korrekt |
| Datenexport | A/2.8 | GPX-Export erfüllt Portabilität | dito |
| Altersfreigabe/Metadaten | A | Rating-Fragebogen, Screenshots | dito + Zielgruppen-Deklaration |
| Sign in with Apple | B/6.2 | **Pflicht**, da Google-Login angeboten | — |
| Account-Löschung in-App | B/6.6 | Guideline 5.1.1(v) | Play-Pflicht + Web-Link |
| UGC-Vollpaket | B/8 | Guideline 1.2: Melden+Blockieren+Moderation+Regeln | UGC-Policy identisch |
| Push | B/7.6 | Opt-in je Kategorie | Notification-Runtime-Permission (13+) |
| Belohnungssysteme | C | keine Glücksspiel-Mechanik, nichts kaufbar | dito |
| Live Location Safety | D/13 | Threat-Model dokumentiert; Zeitlimit erzwungen | dito + Service-Deklaration |
| Notfall-/Sturzfunktion | D/13.5 | Assistenz-Formulierung, keine Rettungs-Versprechen | dito |
| Zyklus-Daten | E/17.4 | sensitivste Kategorie: lokal bevorzugt, explizites Opt-in | Health-Policy-Sonderprüfung |
| Review-Risiko-Check | jede Einreichung | TestFlight-Vorabtest bei neuen Berechtigungen | Internal Testing Track |

---

# 9. Evidence Ledger — Nachweisregeln

**Regel:** Kein Task ist fertig ohne Ledger-Eintrag (`docs/EVIDENCE-LEDGER.md`, neueste oben). Reales Verhalten auf echter Hardware zählt. **Run und Bike werden getrennt nachgewiesen.**

```markdown
## [Datum] Plan X · Task Y: <Name>
| Nachweis | Ergebnis |
|---|---|
| Unit-/Component-Tests | ✅ `npm test` — N grün / ❌ + Grund |
| Smoke Test (Expo Go / Dev-Build) | ✅ was geklickt / ❌ / n.a. |
| Echtes Gerät | ✅ Modell + OS / ❌ |
| GPS real (Soll/Ist draußen) | ✅ / n.a. |
| Route real gezeichnet | ✅ / n.a. |
| Aktivität gespeichert (nach Neustart) | ✅ / n.a. |
| **Run-Modus geprüft** | ✅ / ❌ / n.a. |
| **Bike-Modus geprüft** | ✅ / ❌ / n.a. |
| iOS geprüft | ✅ Version / ❌ |
| Android geprüft | ✅ Version / ❌ |
**Offen/Auffällig:** <ehrliche Restpunkte>
```

**Eskalation:** 2× hintereinander ❌ in derselben Spalte → Stopp, Lücke schließen.

**Stufen-Gates (Sammel-Einträge):**
- **GATE A:** je Sport 1 Aktivität ≥ 30 min mit gesperrtem Bildschirm korrekt (iOS **und** Android) · HF real · Belastungs-Score erklärt sich · verbleibende km korrekt · App-Kill ohne Verlust · Batteriemessung · Live Activity/Widget live · Store-Zeilen A erledigt · **Name markenrechtlich geklärt**
- **GATE B:** Flow Registrierung→Aktivität→Empfehlung→fremde Route übernehmen (beide Plattformen) · Account-Löschung vollständig · Melde-Flow endet in bearbeitbarem Eintrag · Sichtbarkeits-Matrix vollständig getestet · Avatar-Unlock feuert korrekt
- **GATE C:** gemeinsame Aktivität mit 2 echten Geräten erkannt · Rankings deterministisch · Effort-Formel simuliert (Run-vs-Bike belegt) · Anti-Cheat sortiert Testbetrug aus (inkl. Rad-als-Lauf via Sensor-Plausibilität) · Mentor-Bonus nur nach Integration
- **GATE D:** Areal-Simulation belegt Fairness (klein vs. groß, Run vs. Bike) · **Karte zeigt reale Areale mit Teamfarben/Labels, kein sichtbares Raster** · **Einzel-Revier: Runde wird erkannt, Linie hin/zurück abgelehnt, Einnahme + Top-3-Detail auf echtem Gerät, Team-Areale nachweislich unbeeinflusst** · Territorien-Filter aus/an + Live-Sportler-Zoom geprüft · Sportplatz-Challenge: Runden am realen Platz korrekt gezählt, Bahngold-Vergabe deterministisch (Duell-Bonus mit 2 Geräten geprüft) · Live-Freigabe endet in allen Pfaden · Safety-Modell extern geprüft · Season-Snapshot unveränderlich, Vereinsheim vollständig · Fehlalarmquote Sturzerkennung dokumentiert
- **GATE E:** Claims juristisch freigegeben · Analyse-Modelle mit Quellen · Store-Review mit Health-/Zyklus-Berechtigungen bestanden

---

# 10. Technische Risiken

| # | Risiko | Stufe | Gegenmaßnahme (verankert in) |
|---|---|---|---|
| 1 | Hintergrund-GPS gedrosselt/gekillt; Expo Go kann es nicht | A | Dev-Build früh (2.1), Services/Background Modes (2.2), Recovery (2.4), Feldtest im Gate |
| 2 | GPS-Drift + Batterie (Bike: hohes Tempo) | A | Filter (2.3), sport-spezifisches Sampling (2.6), Messlauf (2.9) |
| 3 | **Run-vs-Bike-Unwucht** in km-Mechaniken | A–D | Effort-Normalisierung + getrennte Schwellen (3.2), Simulationen (10.1, 12.1) |
| 4 | Fingerskizze = ungelöstes Map-Matching | A | Timebox-Spike (5.2), Wegpunkt-Fallback |
| 5 | Karten-/Routing-Kosten bei Skalierung | A→B | Anbieter-ADR vor Stufe B (5.4) |
| 6 | Backend-Fehlentscheid trägt alles | B | Prototyp-Entscheid Geo+Auth (6.0) |
| 7 | Health-Claims als Medizinprodukt wertbar | A/E | v1.0 nur beschreibend + erklärbarer Score; Empfehlungen erst nach Freigabe (16.0) |
| 8 | Gefälschte Tracks zerstören Rankings/Areale | C/D | Anti-Cheat vor Freischaltung (10.2), nur `verified` (12.4) |
| 9 | Areal-Unfairness (klein vs. groß) | D | Ebenen-Trennung + Quorum/Deckel/Kapazität + Pflicht-Simulation (12.1) + Seasons |
| 10 | **Areal-Schnitt wirkt willkürlich** (falsche Grenzen, seltsame Namen) | D | Schnitt entlang realer Grenzen + OSM-Namen (12.2); Testabnahme an realer Stadt |
| 11 | Live Location = Stalking-Risiko | D | Threat-Model, Zeitlimit, Not-Aus, externe Prüfung (13.1–13.2) |
| 12 | Sturzerkennung: Fehlalarme / falsche Sicherheit | D | Assistenz-Sprache, Countdown, Fehlalarmquote im Gate (13.5) |
| 13 | Store-Ablehnung (Background-Location, Health, UGC, Live) | alle | Matrix Abschnitt 8, TestFlight/Internal je Einreichung |
| 14 | Einladungs-Farming | C | Mentor-Bonus erst nach Integration, Aktiv-Definition (9.3, 9.5) |
| 15 | Namens-/Markenkollision — Vorrecherche 2026-07-17: „Veyr" ist aktive Fitness-App (gleiche Klasse!), „Revyr" doppelt vergeben (revyr.ai Software, revyr.de Jagdreisen), Reserven TERRIO/AREVO belastet | A | Namensfindung mit neuen Kandidaten + professionelle Recherche vor GATE A (Abschnitt 0) |
| 16 | Scope-Kriechen (§33-Visionen) | alle | dieser Plan ist die Grenze |
| 17 | Karten-Performance (1.000+ Areale) | D | Viewport-Loading + Zoom-Aggregation, Messkriterium (12.5) |
| 18 | Unsichtbare Transparenz-Farben in Web-Auskopplungen | B+ | keine CSS-Farbmischfunktionen; `fill-opacity`/`rgba` (2.1-Regel im Design-System) |
| 19 | Einzel-Revier-Schummel (Mini-Runden, GPS-Drift-„Flächen", Pendel-Tracks) | D | Runden-Regel + Mindestfläche + Ziel-Bindung (4.5), Anti-Cheat (10.2), Simulations-Szenarien (12.1) |
| 20 | Einzel-Reviere verraten Wohngebiet/Lauf-Routine | D | Sichtbarkeit Standard Follower, Anonymisierung für Dritte, Start-/End-Unschärfe, Threat-Model 13.1 erweitert |
| 21 | Bild-Füllungen der Einzel-Reviere = UGC-Missbrauchsfläche | D | Bild erst nach Moderations-Pipeline (8.4); Fallback nur Farbe |
| 22 | Sensor-Plausibilität nutzt Gesundheitsdaten (HF/Kalorien) serverseitig | C | Datensparsamkeit: nur aggregierte Plausibilitäts-Signale (Ø-Kadenz, HF-Band) zum Server, nie Rohverläufe; DSGVO-Prüfung in 10.2 |
| 23 | OSM-Datenqualität Sportplätze (fehlend/falsch geschnitten) | D | Kuratierung + Community-Meldung („Platz fehlt"); Testabnahme an realen Plätzen (12.13) |
| 24 | Dynamische Revier-Geometrie (Polygon-Union/-Beschnitt) komplex und fehleranfällig | D | PostGIS-Operationen serverseitig, Geo-Fixtures-Testsuite (12.11), Grenzfälle in Pflicht-Simulation (12.1) |

---

# 11. Entscheidungsstatus

| Entscheidung | Status |
|---|---|
| MVP-Grenze, Stufenmodell | ✅ dieses Dokument |
| Tech-Stack App | ✅ Expo/React Native/TypeScript |
| Health-Priorität | ✅ Stufe A, Health-App-Positionierung |
| **Territory-Darstellung** | ✅ **Areale = reale Stadtgebiete auf echter Karte; H3-Raster nur interne Recheneinheit, nie sichtbar** |
| Territory-Modell | ✅ Teams=Areal-Besitz (nur gemeinsam) / Einzeluser=Einzel-Reviere (Runden-Regel, strikt getrennt) + Spuren + Krone; Formel-Startwerte fixiert, Kalibrierung 12.1 |
| Team-Wachstum | ✅ Kapazität, Mentor-Bonus, Quests, Doppelbedingung |
| Seasons + Historie | ✅ Quartals-Seasons, `season_records`, Vereinsheim, Zeitreise |
| Profil-Logik | ✅ Sichtbarkeits-Matrix (Standard privat), Follow/Anfrage, Blockieren überall |
| Avatare | ✅ nur durch Leistung; Basis in A, Unlocks ab B; Team-Harness über Teamstufen |
| Run/Bike-Oberflächen | ✅ Modus-Umschalter, eine Architektur, Effort-Normalisierung |
| Design | ✅ Schwarz-Weiß, „Farbe muss man sich verdienen"; keine color-mix-Farben in Web-Auskopplungen |
| **App-Name** | 🔶 REVYR nach Vorrecherche 2026-07-17 **hochriskant** („Veyr" = aktive Fitness-App gleicher Klasse; Reserven ebenfalls belastet) → Namensfindung erweitern, dann professionelle Recherche vor GATE A (Prüfvermerk in Abschnitt 0) |
| Backend | 🔶 Entscheid in 6.0 (Prototyp) |
| Karten-/Routinganbieter | 🔶 ADR vor Stufe B |
| Gesundheitsclaims-Grenze | 🔶 juristische Prüfung in 16.0 |
| Monetarisierung | 🔶 nach Produktvalidierung (frühestens vor v3.0); nie kaufbare Leistung/Avatare |
| Sportplatz-Punktesystem | ✅ **Bahngold** (Spez. in 4.6): eigene Währung nur an Sportplätzen; degressive Tagespunkte, Entdecker-/Bestzeit-/Rekord-/Duell-Boni; Platzkönig, Bahn-Liga, exklusive Items; nie Einfluss auf Effort/Reviere; Startwerte in 12.1 |

---

# 12. Reihenfolge (Einseiter)

```
Plan 1 ✔ → Plan 2 → Plan 3 → Plan 4 → [Plan 5] → GATE A → v1.0 (Health-Tracker, REVYR-Launch)
→ Entscheidungen: Name final, Backend, Karten-ADR
→ Plan 6 → 7 → 8 → GATE B → v2.0 (Plattform)
→ Plan 9 → 10 → 11 → GATE C → v3.0 (Gemeinschaft)
→ Plan 12 → 13 → 14 → GATE D → v4.0 (Spielfeld: Areale/Seasons/Live)
→ Plan 15 → 16 → 17 → GATE E → v5.0 (Begleiter)
```

Jeder Plan wird vor Umsetzung in einen TDD-Detailplan überführt (Muster: Plan 1). Jeder Task endet mit Evidence-Ledger-Eintrag, Run und Bike getrennt. Jedes Gate ist ein Sammel-Nachweis inkl. Store-Readiness-Zeilen seiner Stufe.
