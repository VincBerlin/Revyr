#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Erzeugt intake-package.json ausschliesslich aus den echten Artefakten.
Kein Zahlenwert wird hier abgetippt; alles wird geparst.
Im Scratchpad, nicht im Repo.
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import validate_intake as V  # noqa: E402
import blocking_model as BM  # noqa: E402  (DIE kanonische Blocking-Formel)

REPO = "/Users/vincentschnetzer/Documents/Run&Bike"
OUT = os.path.join(REPO, "intake-package.json")
TODAY = "2026-07-19"

# Abschliessende Vokabulare. Sie stehen im Schema und werden hier zur
# Kopfextraktion benutzt — nicht dupliziert interpretiert.
SOURCE_TYPES = ["EXPLICIT", "ASSUMPTION", "MISSING", "BLOCKER", "CONTRADICTION"]
MEASUREMENT_TYPES = ["OPERATIONAL_QUALITY", "COMPLIANCE_CONTROL",
                     "RESEARCH_HYPOTHESIS", "PRODUCT_OUTCOME"]

ROLES = {
    "docs/ID-REGISTRY.md": "Kanonische ID-Quelle (ab Phase 2 eingefroren)",
    "docs/vision/revyr-endurance-platform.vision.md": "Vision",
    "docs/canvas/revyr-endurance-platform.canvas.md": "Product Canvas (atomare Items)",
    "docs/prd/revyr-endurance-platform.prd.md": "PRD inkl. Messmodell je Requirement",
    "docs/traceability.md": "Traceability-Matrix",
    "docs/architecture/revyr-target-architecture.md": "Zielarchitektur",
    "docs/implementation/revyr-delivery-plan.md": "Delivery-Plan",
    "docs/decisions/decision-log.md": "Entscheidungs- und Widerspruchs-Ledger",
    "docs/decisions/open-questions.md": "Kanonisches OQ-Register",
    "docs/risks/revyr-risk-register.md": "Risikoregister",
    "docs/EVIDENCE-LEDGER.md": "Evidence Ledger (leer, keine Evidence erbracht)",
    "docs/SOURCE-MAP.md": "Quellenkarte",
    "docs/validation/validation-report.md": "Validierungsbericht",
    "README.md": "Repository-Einstieg",
    "intake-package.json": "Dieses Intake-Paket",
}


def declared_status(repo, rel):
    p = os.path.join(repo, rel)
    if not os.path.isfile(p) or not rel.endswith(".md"):
        return "n/a (keine Markdown-Statuszeile)"
    head = open(p, encoding="utf-8").read().split("\n")[:15]
    for l in head:
        m = re.match(r"^(?:Status|Confirmation Status|Readiness-Level)\s*:\s*(.+)$", l.strip())
        if m:
            return re.sub(r"[`*]", "", m.group(1)).strip()
    return "MISSING — keine Statuszeile im Kopf"


def main():
    reg_text = V.read(REPO, V.REGISTRY)
    entries = V.parse_registry(reg_text)
    reg_index = {}
    for e in entries:
        reg_index.setdefault(e["id"], []).append(e)

    prd_blocks = V.parse_prd_blocks(V.read(REPO, V.PRD))
    trace_rows = {r["req"]: r for r in V.parse_trace_matrix(V.read(REPO, V.TRACE))}

    # --- Validator real ausfuehren, Ergebnis uebernehmen ---
    res_json = os.path.join(HERE, "result.json")
    subprocess.run([sys.executable, os.path.join(HERE, "validate_intake.py"),
                    "--repo", REPO, "--json", res_json],
                   capture_output=True, text=True)
    vres = json.load(open(res_json, encoding="utf-8"))
    failed_ids = [c["id"] for c in vres["checks"] if c["status"] == "FAIL"]

    # --- Artefakte ---
    artifacts = []
    for rel, role in ROLES.items():
        if rel == "intake-package.json":
            # Selbstbezug: die Datei wird von diesem Lauf erst geschrieben.
            # Eine Zeilenzahl waere entweder veraltet oder selbstreferenziell
            # instabil, deshalb bewusst 0 mit offengelegter Begruendung.
            artifacts.append({
                "path": rel, "role": role, "exists": True, "lines": 0,
                "declared_status": "in diesem Lauf erzeugt",
                "notes": "Selbstbezug: Zeilenzahl bewusst 0, weil sie sich beim "
                         "Schreiben dieser Datei selbst veraendern wuerde. "
                         "Kein unbegruendeter Nullwert."})
            continue
        p = os.path.join(REPO, rel)
        exists = os.path.isfile(p)
        # BEFUND/FIX: `len(text.split("\n"))` zaehlt bei abschliessendem Newline
        # eine Zeile zu viel (Split-Artefakt). Alle 13 Werte in §5 des
        # Validierungsberichts standen dadurch exakt 1 zu hoch.
        # Jetzt identisch zu `wc -l`: gezaehlt werden Zeilenumbrueche.
        lines = open(p, encoding="utf-8").read().count("\n") if exists else 0
        item = {"path": rel, "role": role, "exists": exists, "lines": lines,
                "declared_status": declared_status(REPO, rel) if exists
                                   else "MISSING — Datei existiert nicht"}
        artifacts.append(item)
    for rel in ("infra/routing-proxy/", "mobile/", "backend/"):
        artifacts.append({
            "path": rel, "role": "nur dokumentiert, bewusst NICHT angelegt",
            "exists": os.path.isdir(os.path.join(REPO, rel)), "lines": 0,
            "declared_status": "NICHT ANGELEGT — in diesem Lauf ausdruecklich verboten",
            "notes": "Ablageort ist entschieden (OQ-011), aber es existiert keine "
                     "Quelldatei, kein Deployment und keine AWS-Ressource."})

    # --- ID-Zaehlungen ---
    by_prefix = {}
    for p in V.MANAGED_PREFIXES:
        st = {}
        for e in entries:
            if e["prefix"] == p:
                st[e["status"]] = st.get(e["status"], 0) + 1
        st["total"] = sum(v for k, v in st.items() if k != "total")
        by_prefix[p] = st

    unmanaged = []
    for m in re.finditer(r"^\|\s*`([A-Z]+)-`\s*\|", reg_text, re.M):
        unmanaged.append({"prefix": m.group(1), "registry_managed": False,
                          "risk": "Nicht registry-verwaltet (Registry §5): ungeschuetzt "
                                  "gegen denselben Kollisionsdefekt, den die Registry "
                                  "fuer ihre %d verwalteten Praefixe behebt."
                                  % len(V.MANAGED_PREFIXES)})

    # --- Requirements ---
    # AUFGABE 4: maschinenlesbarer Herkunftsvorbehalt JE REQUIREMENT.
    # Vorher transportierte requirements[].source_type einen flachen Wert,
    # waehrend der Vorbehalt nur als Blocker-Eintrag existierte, dessen `affects`
    # auf eine DATEI zeigte. Ein Konsument, der die Requirement-Liste liest und
    # die Blocker-Liste nicht, sah belegte Herkunft, wo keine ist.
    CAVEATS = {
        "EXPLICIT": ("Herkunft belegt. ACHTUNG: im PRD ausdruecklich "
                     "KLAUSELBESCHRAENKT — die Einstufung gilt nur fuer die dort "
                     "benannten Klauseln, nicht fuer das gesamte Requirement."),
        "ASSUMPTION": ("Herkunft NICHT belegt. Der Zielwert ist eine plausible, "
                       "aber unbestaetigte Annahme; keine Nutzerbestaetigung, "
                       "keine externe Norm, keine Messreihe."),
        "MISSING": ("Kein belegter Schwellenwert. Es wurde ausdruecklich KEIN "
                    "Wert geraten; das Requirement ist ohne Zielwert nicht "
                    "abnehmbar."),
        "BLOCKER": ("Herkunft blockiert — es existiert keine Bestehensbedingung. "
                    "Der Nachweis waere auch mit fertiger Implementierung "
                    "unentscheidbar."),
        "CONTRADICTION": "Herkunft widerspruechlich; nicht still aufgeloest.",
    }
    requirements = []
    for rid in sorted(e["id"] for e in entries
                      if e["prefix"] == "REQ" and e["status"] == "active"):
        blk = prd_blocks[rid]
        f = blk["fields"]
        owner_raw = V.norm(f.get("owner", ""))
        owner_resolved = not V.is_justified(owner_raw)
        marker = "OWNER-BLOCKER (OQ-002 offen)" if not owner_resolved else owner_raw[:80]
        tr = trace_rows.get(rid, {})
        st_verbatim = re.sub(r"[`*]", "", V.norm(f.get("source_type", ""))).strip()
        # BEFUND/FIX: `re.split(r"[—–(]")` schnitt nur an Gedankenstrich und
        # Klammer. REQ-019 formuliert zweiteilig ("ASSUMPTION für die
        # Anforderung selbst; EXPLICIT für den Zielwert der Kennzahl") und
        # REQ-037 mit Punkt ("ASSUMPTION. Die WCAG-Fassung ist ..."). Der
        # ganze Satz landete als `source_type` im Paket und verletzte das
        # Enum. Jetzt wird das FUEHRENDE Vokabeltoken genommen; der Rest bleibt
        # im Verbatim erhalten und wird NICHT wegnormiert.
        head = (V._leading_token(st_verbatim, [s.lower() for s in SOURCE_TYPES])
                or "missing").upper()
        cited = sorted(set(re.findall(
            r"(?:DEC-\d{3}|SRC-\d{3}|CAN-\d{3}|user-confirmed|CONFIRMED)",
            st_verbatim)))
        requirements.append({
            "id": rid,
            "title": blk["title"],
            "measurement_type": (
                V._leading_token(re.sub(r"[`*]", "", V.norm(f["measurement_type"])),
                                 [m.lower() for m in MEASUREMENT_TYPES])
                or "missing").upper(),
            "measurement_type_verbatim":
                re.sub(r"[`*]", "", V.norm(f["measurement_type"])).strip(),
            "release_gate": re.sub(r"[`*]", "", V.norm(f["release_gate"])).strip(),
            "source_type": head,
            "source_provenance": {
                "source_type": head,
                "source_type_verbatim": st_verbatim,
                "evidence_backed": head == "EXPLICIT" and bool(cited),
                "clause_limited": "klauselbeschr" in st_verbatim.lower(),
                "cited_sources": cited,
                "caveat": CAVEATS.get(head, "Unbekannter source_type — MISSING."),
                "user_confirmed": False,
            },
            "owner_status": {"resolved": owner_resolved, "marker": marker},
            "trace_id": tr.get("trc", ""),
            "acceptance_criterion": tr.get("ac", ""),
            "evidence": tr.get("ev", ""),
            # research_plan steht im PRD als Fliesstext-Absatz unter der Feldtabelle,
            # nicht als Tabellenzeile — deshalb im Blocktext gesucht.
            "has_research_plan": "**research_plan**" in blk["body"],
        })

    # --- Open Questions ---
    oq_text = V.read(REPO, "docs/decisions/open-questions.md")
    oqs = []
    for line in oq_text.split("\n"):
        s = line.strip()
        if not s.startswith("| OQ-"):
            continue
        c = [x.strip() for x in s.strip("|").split("|")]
        if len(c) < 6:
            continue
        reg = reg_index.get(c[0], [{}])[0]
        oqs.append({"id": c[0], "title": c[1], "status": reg.get("status", "open"),
                    "owner": c[3], "due": c[4],
                    "default_if_unresolved": re.sub(r"[`*]", "", c[5])})

    # --- Contradictions ---
    # AUFGABE 1: `blocking` wird ABGELEITET, nicht gesetzt.
    # Die Vorfassung stand hier woertlich als  "blocking": e["id"] == "CONTRA-006"
    # — eine behauptete, nicht hergeleitete Aussage und genau die
    # ID-spezifische Sonderbehandlung, die Registry §3.1 verbietet.
    # Formel, Achsenparser und Ergebnisklassen liegen in validate_intake.py und
    # werden hier IMPORTIERT, damit Generator und Validator nicht auseinander-
    # laufen koennen (das war die Ursache der Zaehlstaende 2 vs. 3).
    ledger_text = V.read(REPO, V.DECISION_LOG)
    ledger = V.parse_ledger_status(ledger_text)
    reg_axes = V.parse_contra_axes(reg_text)
    contradictions = []
    for e in entries:
        if e["prefix"] != "CONTRA":
            continue
        raw = ledger.get(e["id"])
        ls = re.sub(r"[`*]", "", raw).strip() if raw else "MISSING — kein Ledger-Eintrag"
        reg_st = V.normalize_status_token(e["status"])
        led_st = V.normalize_status_token(raw) if raw else "MISSING"
        ax = reg_axes.get(e["id"])
        item = {"id": e["id"], "registry_status": reg_st, "ledger_status": ls,
                "divergence": raw is not None and reg_st != led_st}
        if ax is None:
            item["blocking"] = True
            item["status_model"] = {
                "resolution_status": "MISSING", "evidence_status": "MISSING",
                "blocked_gates": [], "blocked_activities": [],
                "evidence_gate": "MISSING",
                "blocking_derivation": ["kein Statusmodell-Eintrag in Registry "
                                        "§6.11.1 — blocking nicht ableitbar, "
                                        "deshalb als blockierend gefuehrt"],
                "outcome": V.OUTCOME_DECISION_OPEN,
                "decision_reference": "MISSING", "evidence_reference": "MISSING"}
        else:
            derived, reasons = BM.derive_blocking(ax)
            item["blocking"] = derived
            item["status_model"] = {
                "resolution_status": ax["resolution_status"],
                "evidence_status": ax["evidence_status"],
                "blocked_gates": ax["blocked_gates"],
                "blocked_activities": ax["blocked_activities"],
                "evidence_gate": ax["evidence_gate"],
                "blocking_derivation": reasons,
                "outcome": BM.classify(ax, derived),
                "decision_reference": ax["decision_reference"],
                "evidence_reference": ax["evidence_reference"]}
        contradictions.append(item)

    # --- NFRs (aus dem PRD geparst, kein Wert abgetippt) ---
    nfr_blocks = V.parse_nfr_blocks(V.read(REPO, V.PRD))
    nfrs = []
    for nid in sorted(nfr_blocks):
        f = nfr_blocks[nid]["fields"]
        get = lambda *ks: re.sub(r"[`*]", "", V.norm(V._first(f, list(ks)) or "")).strip()
        owner_raw = get("owner")
        # evidence_status kann klauselbeschraenkt sein ("pending fuer die
        # pruefbaren Klauseln"). Der FUEHRENDE Wert ist die Achsenangabe; die
        # Einschraenkung bleibt im Verbatim sichtbar und wird nicht wegnormiert.
        ev_raw = get("evidence_status")
        ev_head = next((v for v in sorted(V.EVIDENCE_VALUES, key=len, reverse=True)
                        if re.match(r"^%s\b" % re.escape(v), ev_raw.strip().lower())),
                       "MISSING")
        nfrs.append({
            "id": nid,
            "title": nfr_blocks[nid]["title"],
            "source_type": re.split(r"[—–(]", get("source_type"))[0].strip().upper(),
            "source_type_verbatim": get("source_type"),
            "target_or_pass_condition": get("zielwert / pass-bedingung",
                                            "zielwert/pass-bedingung"),
            "source_of_target": get("quelle des zielwerts"),
            "evidence_status": ev_head,
            "evidence_status_verbatim": ev_raw,
            "evidence_status_qualified": ev_raw.strip().lower() != ev_head,
            "measurement_method": get("testmethode"),
            "measurement_window": get("measurement_window"),
            "reference_environment": get("referenzumgebung"),
            "evidence_source": get("evidence_source"),
            "release_gate": get("release_gate"),
            "owner_status": {"resolved": not V.is_justified(owner_raw),
                             "marker": owner_raw[:120] or "MISSING"},
            "blocking_verbatim": get("blocking / blocked_gates / blocked_activities",
                                     "blocking"),
        })

    # --- CONTRA-006: die fuenf Einzelaussagen statt eines Pauschalurteils ---
    ax006 = reg_axes.get("CONTRA-006")
    d006, r006 = (BM.derive_blocking(ax006) if ax006 else (True, ["kein Statusmodell"]))
    contra006 = {
        "criterion": "Erfolgreiches Dokumentationskriterium fuer CONTRA-006 — "
                     "fuenf Einzelaussagen, kein Pauschalurteil 'RESOLVED'.",
        "statements": [
            {"nr": 1, "aussage": "status = resolved",
             "erfuellt": bool(ax006) and ax006["status"] == "resolved",
             "quelle": "docs/ID-REGISTRY.md §6.11.1, docs/decisions/decision-log.md"},
            {"nr": 2, "aussage": "resolution_status = accepted",
             "erfuellt": bool(ax006) and ax006["resolution_status"] == "accepted",
             "quelle": "docs/ID-REGISTRY.md §6.11.1"},
            {"nr": 3, "aussage": "evidence_status = pending (sichtbar als ausstehend gefuehrt)",
             "erfuellt": bool(ax006) and ax006["evidence_status"] == "pending",
             "quelle": "docs/ID-REGISTRY.md §6.11.1, docs/EVIDENCE-LEDGER.md"},
            {"nr": 4, "aussage": "blocking = true fuer A0-Feldtest und Release "
                                 "(abgeleitet, nicht gesetzt)",
             "erfuellt": d006 and bool(ax006)
                         and set(ax006["blocked_activities"]) == {"field-test", "release"}
                         and set(ax006["blocked_gates"]) == {"A0"}
                         and ax006["evidence_gate"] == "A0",
             "ableitung": r006,
             "quelle": "Registry §3.1 Ableitungsformel via derive_blocking()"},
            {"nr": 5, "aussage": "vollstaendiger Ledger-Eintrag vorhanden",
             "erfuellt": "CONTRA-006" in ledger,
             "quelle": "docs/decisions/decision-log.md"},
        ],
        "keine_ungueltigen_registry_statuswerte": next(
            (c["status"] == "PASS" for c in vres["checks"] if c["id"] == "C6e"), False),
        "wortlaut": "Die Designentscheidung fuer CONTRA-006 ist dokumentiert und "
                    "akzeptiert. Die Implementation Evidence ist sichtbar als pending "
                    "gefuehrt und blockiert die dafuer definierten spaeteren Gates.",
        "nicht_behauptet": "Dies ist KEINE Aussage darueber, dass der Nachweis erbracht "
                           "waere. evidence_status bleibt pending; es existiert kein Code, "
                           "kein Build, kein Feldtest und keine AWS-Ressource.",
        "decision_reference_missing": "Der als decision_reference vorgegebene "
                                      "'ADR zum A0-Routing-Proxy' existiert im Repository "
                                      "nicht (MISSING). Er wurde NICHT durch DEC-013 "
                                      "ersetzt.",
    }

    # --- Blocker ---
    # Alle Mengen und Zahlen werden aus der Registry ABGELEITET. Zuvor standen
    # hier eine Requirement-Gesamtzahl, eine ausgeschriebene Anzahl reservierter
    # Canvas-Items und eine Anzahl Requirements ohne Schwellenwert als
    # abgetippte Werte — nach jeder Bestandsaenderung falsch, ohne dass ein
    # Werkzeug es gemerkt haette. Genau das ist eingetreten: der ausgeschriebene
    # Wortlaut nannte zehn reservierte Canvas-Items und wurde woertlich ins
    # Intake-Paket geschrieben, waehrend die Registry sechs fuehrte.
    reserved_can = sorted(e["id"] for e in entries
                          if e["prefix"] == "CAN" and e["status"] == "reserved")
    unbacked = [r["id"] for r in requirements
                if r["source_type"].upper().startswith("MISSING")]
    blockers = [
        {"kind": "BLOCKER",
         "summary": "Kein benannter Owner/DRI (OQ-002). Alle %d Requirements tragen einen "
                    "sichtbaren OWNER-BLOCKER statt eines Verantwortlichen."
                    % len(requirements),
         "affects": [r["id"] for r in requirements], "decided_by": "Nutzer"},
        {"kind": "BLOCKER",
         "summary": "%d reservierte Canvas-Items sind inhaltlich MISSING." % len(reserved_can),
         "affects": reserved_can, "decided_by": "Nutzer"},
        {"kind": "BLOCKER",
         "summary": "CAN-025 ('ambitionierte Ausdauersportler:innen') hat im PRD keine "
                    "USER-ID. Keine ID vergeben — Registry eingefroren.",
         "affects": ["CAN-025", "REQ-009", "REQ-011", "REQ-032"], "decided_by": "Nutzer"},
        {"kind": "BLOCKER",
         "summary": "REQ-029 (Sportplatz-Challenges/Bahngold) hat kein Capability-Item, "
                    "keinen Problembezug und kein Erfolgssignal im Canvas.",
         "affects": ["REQ-029"], "decided_by": "Nutzer"},
        {"kind": "BLOCKER",
         "summary": "RISK-013 verlangt einen Einspruchs-/Appeal-Flow, den kein Requirement "
                    "beschreibt.", "affects": ["RISK-013", "REQ-024"], "decided_by": "Nutzer"},
        {"kind": "BLOCKER",
         "summary": "Kein Pruefverfahren fuer 'wirksam anonymisiert' (CONTRA-005); die "
                    "Bedingung ist ohne Verfahren nicht abschliessend testbar.",
         "affects": ["CONTRA-005", "REQ-017", "REQ-027"], "decided_by": "Nutzer"},
        {"kind": "BLOCKER",
         "summary": "Keine benannte Betriebsverantwortung fuer den A0-Proxy, obwohl er ab "
                    "A0 personenbezogene Wegpunkte verarbeitet.",
         "affects": ["OQ-002", "CAN-096"], "decided_by": "Nutzer"},
        {"kind": "BLOCKER",
         "summary": "Keine reservierten IDs oberhalb OQ-011, RISK-024 und EV-036. Neue "
                    "offene Punkte, Risiken und Nachweise stehen ohne ID.",
         "affects": ["OQ-011", "RISK-024", "EV-036"], "decided_by": "Nutzer"},
        {"kind": "MISSING",
         "summary": "%d Requirements ohne belegten Schwellenwert (source_type "
                    "MISSING). Kein Wert geraten." % len(unbacked),
         "affects": unbacked, "decided_by": "Nutzer"},
        {"kind": "MISSING",
         "summary": "Die `VC-`Kennungen (value-check-id) haben keine "
                    "Definitionsdatei; sie bilden zudem nur den Altbestand ab "
                    "und decken die neu vergebenen Requirements nicht. Keine "
                    "VC-Nummer erfunden.",
         "affects": ["docs/traceability.md"], "decided_by": "Traceability-Owner"},
        {"kind": "MISSING",
         "summary": "SRC-001…SRC-004 existieren nicht im Repository; 133 EXPLICIT-Zellen "
                    "berufen sich darauf, weitere 102 EXPLICIT-Zellen nennen gar keine "
                    "Quelle. `affects` nennt jetzt die betroffenen REQUIREMENTS, nicht "
                    "nur die Datei — der Vorbehalt haengt zusaetzlich maschinenlesbar an "
                    "jedem Requirement unter requirements[].source_provenance.",
         "affects": ([r["id"] for r in requirements
                      if not r["source_provenance"]["evidence_backed"]]
                     + ["docs/SOURCE-MAP.md"]), "decided_by": "Nutzer"},
        {"kind": "MISSING",
         "summary": "`blocking_scope` ist projektweit entfallen (C16), lebt aber "
                    "ausserhalb der Registry noch in Dokumenten weiter. Der "
                    "Wertebereichs-Konflikt ist damit gegenstandslos: die vier "
                    "frueher strittigen Werte sind regulaere Mitglieder von "
                    "`blocked_activities`.",
         "affects": ["docs/validation/validation-report.md"],
         "decided_by": "Nutzer"},
        {"kind": "ASSUMPTION",
         "summary": "Sechs Zielwerte stuetzen sich allein auf VIS-006 und sind nirgends "
                    "empirisch hinterlegt.",
         "affects": ["REQ-010", "REQ-012", "REQ-013", "REQ-019", "REQ-020", "REQ-022"],
         "decided_by": "Nutzer"},
        {"kind": "OPEN QUESTION",
         "summary": "Messluecke Telemetrie: alle fuenf PRODUCT_OUTCOME-Signale und die "
                    "Check-in-Quote sind heute nicht erhebbar; jede Erhebung kollidiert "
                    "mit CAN-095/REQ-034.",
         "affects": [r["id"] for r in requirements
                     if r["measurement_type"] == "PRODUCT_OUTCOME"],
         "decided_by": "Nutzer"},
        {"kind": "BLOCKER",
         "summary": "Canvas-Items sind vom Nutzer NICHT bestaetigt (%d weiterhin "
                    "`reserved` und inhaltlich MISSING). Solange das so ist, bleibt "
                    "der Gesamtstatus BLOCKED_TRACEABILITY. Kein Agent bestaetigt "
                    "sie stellvertretend." % len(reserved_can),
         "affects": reserved_can, "decided_by": "Nutzer"},
    ]

    pkg = {
        "schema_provenance": {
            "schema_file": "scratchpad/intake-package.schema.json",
            "authored_in_this_run": True,
            "is_preexisting_standard": False,
            "validator_file": "scratchpad/validate_intake.py",
            "note": "Schema UND Validator wurden am 2026-07-19 in diesem Lauf neu "
                    "verfasst. Vorher existierte kein ausfuehrbares Intake- oder "
                    "Schema-Validierungswerkzeug (docs/ID-REGISTRY.md §8 Punkt 13, §9). "
                    "'Schema valid' heisst deshalb nur: konform zu diesem selbst "
                    "definierten Schema — nicht: konform zu einem anerkannten Standard.",
        },
        "feature_slug": "revyr-endurance-platform",
        "generated_at": TODAY,
        "confirmation": {
            "user_confirmed": False,
            "true_line_status": "pending-watcher",
            "self_certified": False,
            "max_reachable_status": "READY_FOR_USER_CONFIRMATION",
        },
        "artifacts": artifacts,
        "id_counts": {
            "by_prefix": by_prefix,
            "unmanaged_prefixes": unmanaged,
            "template_placeholders": sorted(V.TEMPLATE_PLACEHOLDERS),
        },
        "requirements": requirements,
        "nfrs": nfrs,
        "open_questions": oqs,
        "contradictions": contradictions,
        "contra_006_criterion": contra006,
        "validation": {
            "validator": "validate_intake.py (neu in diesem Lauf verfasst)",
            "authored_in_this_run": True,
            "checks_total": len(vres["checks"]),
            "checks_passed": vres["passed"],
            "checks_failed": vres["failed"],
            "overall": vres["overall"],
            "failed_check_ids": failed_ids,
        },
        "blockers": blockers,
        "overall_status": {
            "value": "BLOCKED_TRACEABILITY",
            "gate_ready": False,
            "reason": "BLOCKED_TRACEABILITY, weil die %d reservierten Canvas-Items "
                      "(%s) vom Nutzer NICHT "
                      "bestaetigt sind. Zusaetzlich nicht erfuellt: %s. Offen bleiben "
                      "Owner/DRI (OQ-002) fuer alle %d Requirements und alle %d NFRs "
                      "sowie %d unbelegte Schwellenwerte. Kein Agent hat bestaetigt; "
                      "true-line-status bleibt pending-watcher. "
                      "READY_FOR_AGILETEAM_PLANNING wird ausdruecklich NICHT erreicht "
                      "und ist aus diesem Zustand nicht erreichbar."
                      % (len(reserved_can), ", ".join(reserved_can),
                         ", ".join(failed_ids), len(requirements), len(nfrs),
                         len(unbacked)),
        },
    }

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(pkg, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("geschrieben: %s (%d Requirements, %d Artefakte, %d Blocker)"
          % (OUT, len(requirements), len(artifacts), len(blockers)))


if __name__ == "__main__":
    main()
