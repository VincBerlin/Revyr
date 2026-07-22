#!/usr/bin/env bash
# Reproduzierbares Pruefkommando fuer die aktive REVYR-Validatorkette.
#
# Aufruf:   scripts/validation/run_all.sh
# Ergebnis: je Werkzeug eine Zeile NAME + ERGEBNIS, danach eine Zusammenfassung.
#           Exit-Code != 0, sobald irgendein Werkzeug FAIL meldet.
#
# Der Repo-Pfad wird AUS DEM SKRIPTORT aufgeloest (zwei Ebenen aufwaerts von
# scripts/validation/), nicht hartkodiert. Ueberschreibbar mit REVYR_REPO.
# Damit laeuft das Skript aus jedem Klon.
#
# ACHTUNG: Der Repo-Pfad enthaelt ein kaufmaennisches Und ("Run&Bike").
# Jede Pfadverwendung ist deshalb in Anfuehrungszeichen gesetzt.
#
# Dieses Skript faellt KEIN Gate-Verdikt. Der Gesamtstatus bleibt
# BLOCKED_TRACEABILITY. Ein gruener Lauf waere keine Freigabe.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="${REVYR_REPO:-$(cd "$HERE/../.." && pwd)}"
export REVYR_REPO="$REPO"

PY="${PYTHON:-python3}"
PASS=0; FAIL=0; INFO=0
FAILED_TOOLS=()

line() { printf '%s\n' "------------------------------------------------------------"; }

# report NAME VERDICT DETAIL
report() {
  printf '%-24s %-6s %s\n' "$1" "$2" "${3:-}"
  if   [ "$2" = "PASS" ]; then PASS=$((PASS+1))
  elif [ "$2" = "FAIL" ]; then FAIL=$((FAIL+1)); FAILED_TOOLS+=("$1")
  else INFO=$((INFO+1)); fi
}

# run_rc NAME -- CMD...   : Verdikt aus dem Exit-Code des Werkzeugs.
run_rc() {
  local name="$1"; shift; shift
  local out rc
  out="$("$@" 2>&1)" && rc=0 || rc=$?
  printf '%s\n' "$out" > "$LOGDIR/$name.log"
  if [ "$rc" -eq 0 ]; then report "$name" "PASS" "rc=0"
  else report "$name" "FAIL" "rc=$rc  (siehe $LOGDIR/$name.log)"; fi
}

LOGDIR="${TMPDIR:-/tmp}/revyr-validation-$$"
mkdir -p "$LOGDIR"

echo "REVYR Validatorkette"
echo "Repo:      $REPO"
echo "Werkzeuge: $HERE"
echo "Logs:      $LOGDIR"
echo "Python:    $($PY --version 2>&1)"
line

# --- 1. Registry-Modell (informativ; blocking_model.py ist reine Bibliothek
#        ohne __main__ und wird deshalb nicht einzeln aufgerufen) -----------
run_rc "registry_model.py" -- "$PY" "$HERE/registry_model.py" "$REPO"

# --- 2. Schema-Konformitaet des Intake-Pakets ----------------------------
run_rc "validate_schema.py" -- "$PY" "$HERE/validate_schema.py" \
       "$HERE/intake-package.schema.json" "$REPO/intake-package.json"

# --- 3. Hauptvalidator ---------------------------------------------------
run_rc "validate_intake.py" -- "$PY" "$HERE/validate_intake.py" --repo "$REPO"

# --- 4. Traceability -----------------------------------------------------
run_rc "validate_trace.py" -- "$PY" "$HERE/validate_trace.py" "$REPO"

# --- 5. PRD --------------------------------------------------------------
run_rc "check_prd.py" -- "$PY" "$HERE/check_prd.py" "$REPO"

# --- 6. xcheck.py: setzt KEINEN Exit-Code. Verdikt aus dem JSON-Inhalt:
#        PASS nur, wenn alle vier Abweichungslisten leer sind. ------------
XOUT="$("$PY" "$HERE/xcheck.py" 2>&1)" || true
printf '%s\n' "$XOUT" > "$LOGDIR/xcheck.py.log"
if printf '%s' "$XOUT" | "$PY" -c 'import json,sys
d=json.load(sys.stdin)
k=["active_in_registry_missing_from_canvas","in_canvas_but_not_active_in_registry",
   "reserved_mismatch","deprecated_leaking_into_canvas_defs"]
sys.exit(0 if all(not d[x] for x in k) else 1)' 2>/dev/null; then
  report "xcheck.py" "PASS" "alle Abweichungslisten leer (kein eigener Exit-Code)"
else
  report "xcheck.py" "FAIL" "Abweichungen im JSON (siehe $LOGDIR/xcheck.py.log)"
fi

# --- 7. verify.py: setzt KEINEN Exit-Code (kein sys.exit). Verdikt aus der
#        Zeile "FAILS: N". Aktenkundig: N=1 durch einen WERKZEUGdefekt
#        (hartkodiertes claim-Literal), nicht durch einen Dokumentfehler.
#        Siehe README.md, Abschnitt "Bekannte Werkzeugdefekte". ----------
VOUT="$("$PY" "$HERE/verify.py" 2>&1)" || true
printf '%s\n' "$VOUT" > "$LOGDIR/verify.py.log"
VN="$(printf '%s\n' "$VOUT" | sed -n 's/^FAILS: \([0-9][0-9]*\)$/\1/p' | tail -1)"
if [ -z "$VN" ]; then
  report "verify.py" "FAIL" "Zeile 'FAILS: N' nicht gefunden"
elif [ "$VN" -eq 0 ]; then
  report "verify.py" "PASS" "FAILS=0 (kein eigener Exit-Code)"
else
  report "verify.py" "FAIL" "FAILS=$VN (kein eigener Exit-Code; bekannter Werkzeugdefekt)"
fi

# --- 8. Canvas -----------------------------------------------------------
run_rc "verify_canvas.py" -- "$PY" "$HERE/verify_canvas.py"

# --- 9. Open Questions ---------------------------------------------------
run_rc "oq_check.py" -- "$PY" "$HERE/oq_check.py"

# --- 10. AUDIT_points.py: reines Berichtswerkzeug ohne Bestehensbegriff
#         und ohne Exit-Code. Wird als INFO gefuehrt, nicht als Gate. -----
APOUT="$("$PY" "$HERE/AUDIT_points.py" 2>&1)" || true
printf '%s\n' "$APOUT" > "$LOGDIR/AUDIT_points.py.log"
report "AUDIT_points.py" "INFO" "Bericht ohne Bestehensbegriff (siehe Log)"

# --- 11. Selbsttest der Werkzeugschaerfe (langsam, ~5 min).
#         Mit REVYR_SKIP_SELFTEST=1 ueberspringbar; das Ueberspringen wird
#         sichtbar als SKIP gemeldet, nicht stillschweigend. --------------
if [ "${REVYR_SKIP_SELFTEST:-0}" = "1" ]; then
  report "selftest_validator.py" "SKIP" "uebersprungen via REVYR_SKIP_SELFTEST=1"
else
  run_rc "selftest_validator.py" -- "$PY" "$HERE/selftest_validator.py"
fi

line
echo "ZUSAMMENFASSUNG: PASS=$PASS  FAIL=$FAIL  INFO/SKIP=$INFO"
if [ "$FAIL" -gt 0 ]; then
  echo "FEHLGESCHLAGEN: ${FAILED_TOOLS[*]}"
  echo "Gesamtstatus bleibt BLOCKED_TRACEABILITY. Dieser Lauf ist keine Freigabe."
  exit 1
fi
echo "Alle Werkzeuge ohne FAIL. Das ist KEINE Freigabe und kein Gate-Verdikt;"
echo "der Gesamtstatus bleibt BLOCKED_TRACEABILITY."
exit 0
