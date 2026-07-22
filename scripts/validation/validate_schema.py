#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minimaler JSON-Schema-Validator (Teilmenge Draft 2020-12).

AUCH DIESER VALIDATOR IST IN DIESEM LAUF NEU VERFASST. Die Bibliothek
`jsonschema` ist in dieser Umgebung nicht installiert (nachgewiesen:
ModuleNotFoundError). Unterstuetzt werden genau die Schluesselwoerter, die
intake-package.schema.json verwendet:
  type, required, properties, additionalProperties, items, enum, const,
  pattern, minLength, minItems, maxItems, minimum, propertyNames-frei.

Ein unbekanntes Schluesselwort wird NICHT stillschweigend ignoriert,
sondern als nicht geprueft gemeldet — sonst waere "valid" eine Scheinaussage.
"""
import json
import re
import sys

SUPPORTED = {"$schema", "$id", "title", "description", "type", "required",
             "properties", "additionalProperties", "items", "enum", "const",
             "pattern", "minLength", "minItems", "maxItems", "minimum"}

TYPES = {"object": dict, "array": list, "string": str, "integer": int,
         "number": (int, float), "boolean": bool, "null": type(None)}

errors = []
unsupported = set()


def check(inst, schema, path="$"):
    for k in schema:
        if k not in SUPPORTED:
            unsupported.add(k)

    if "type" in schema:
        t = schema["type"]
        py = TYPES[t]
        ok = isinstance(inst, py)
        if t == "integer" and isinstance(inst, bool):
            ok = False
        if t in ("string", "array", "object", "number") and isinstance(inst, bool):
            ok = False
        if not ok:
            errors.append("%s: erwartet type=%s, gefunden %s"
                          % (path, t, type(inst).__name__))
            return

    if "const" in schema and inst != schema["const"]:
        errors.append("%s: erwartet const=%r, gefunden %r" % (path, schema["const"], inst))
    if "enum" in schema and inst not in schema["enum"]:
        errors.append("%s: %r nicht in enum %r" % (path, inst, schema["enum"]))
    if "pattern" in schema and isinstance(inst, str):
        if not re.search(schema["pattern"], inst):
            errors.append("%s: %r verletzt pattern %s" % (path, inst, schema["pattern"]))
    if "minLength" in schema and isinstance(inst, str):
        if len(inst) < schema["minLength"]:
            errors.append("%s: Laenge %d < minLength %d"
                          % (path, len(inst), schema["minLength"]))
    if "minimum" in schema and isinstance(inst, (int, float)):
        if inst < schema["minimum"]:
            errors.append("%s: %r < minimum %r" % (path, inst, schema["minimum"]))

    if isinstance(inst, list):
        if "minItems" in schema and len(inst) < schema["minItems"]:
            errors.append("%s: %d Elemente < minItems %d"
                          % (path, len(inst), schema["minItems"]))
        if "maxItems" in schema and len(inst) > schema["maxItems"]:
            errors.append("%s: %d Elemente > maxItems %d"
                          % (path, len(inst), schema["maxItems"]))
        if "items" in schema:
            for i, el in enumerate(inst):
                check(el, schema["items"], "%s[%d]" % (path, i))

    if isinstance(inst, dict):
        for r in schema.get("required", []):
            if r not in inst:
                errors.append("%s: Pflichtfeld %r fehlt" % (path, r))
        props = schema.get("properties", {})
        for k, v in inst.items():
            if k in props:
                check(v, props[k], "%s.%s" % (path, k))
            else:
                ap = schema.get("additionalProperties", True)
                if ap is False:
                    errors.append("%s: unerlaubtes Zusatzfeld %r" % (path, k))
                elif isinstance(ap, dict):
                    check(v, ap, "%s.%s" % (path, k))


def main():
    schema = json.load(open(sys.argv[1], encoding="utf-8"))
    inst = json.load(open(sys.argv[2], encoding="utf-8"))
    check(inst, schema)
    print("=" * 78)
    print("SCHEMA-VALIDIERUNG")
    print("Schema:   %s   (in diesem Lauf NEU verfasst, kein vorbestehender Standard)" % sys.argv[1])
    print("Instanz:  %s" % sys.argv[2])
    print("=" * 78)
    if unsupported:
        print("NICHT GEPRUEFTE SCHLUESSELWOERTER: %s" % sorted(unsupported))
    else:
        print("Alle im Schema verwendeten Schluesselwoerter werden geprueft.")
    if errors:
        print("\nERGEBNIS: SCHEMA-VERLETZUNG — %d Fehler" % len(errors))
        for e in errors:
            print("  - %s" % e)
        return 1
    print("\nERGEBNIS: intake-package.json ist konform zu DIESEM Schema.")
    print("Das ist KEINE inhaltliche Bestaetigung und kein Standardnachweis.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
