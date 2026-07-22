# Validation Report

Readiness-Level: `BLOCKED_CONTRADICTION`

## Structural Results

- Canonical PRD count: 36 Requirements.
- Acceptance Criteria count: 36.
- Evidence count: 36.
- Traceability rows: 36.
- Duplicate uploaded PRDs: byte-identical; one canonical copy retained.
- Nonexistent IDs `REQ-037`–`REQ-039`: not used.
- User confirmation: not simulated.

## Validator

Command:

```text
python validate_intake_package.py intake-package.json --json
```

Exit code: `0`

```json
{
  "ok": true,
  "errors": [],
  "warnings": []
}
```

## Interpretation

The JSON package is structurally valid. Its readiness remains intentionally blocked because the Background-Tracking implementation conflicts with `REQ-003` and required A0 evidence is missing.
