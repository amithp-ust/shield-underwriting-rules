# Shield underwriting rules

**Application:** Policy Administration (`policy-admin`)

**Component:** `CM-UW-RULES`

**Owner:** Policy platform

`src/underwriting/rules.py` contains synthetic eligibility and pricing rules
consumed by `shield-policy-service`. No downstream service dependencies.
`contracts/underwriting-api.yaml` describes the intended API.

## Specification consumer

Canonical specs, authoring, gates, and requirement metrics live only in
[`amithp-ust/Intent-to-spec`](https://github.com/amithp-ust/Intent-to-spec).
Shared glossary, map, standards, and policy remain in
[`amithp-ust/shield-context`](https://github.com/amithp-ust/shield-context).
This repo owns `CM-UW-RULES` implementation, not spec authoring. See
[AGENTS.md](AGENTS.md) for immutable approved spec references, issue/PR traceability,
human review, and fixture-contract checks. Do not install authoring here or copy
specs; empty `specs/.gitkeep` is a legacy placeholder.

Python 3.11+, standard library only. Run `python -m unittest discover -s tests`
from this repository root; the unit-test CI runs the same command on Python 3.11.
These callable stubs do not run an HTTP server and are not production pricing.
