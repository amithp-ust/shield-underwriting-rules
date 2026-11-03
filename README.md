# Shield underwriting rules

**Application:** Policy Administration (`policy-admin`)

**Component:** `CM-UW-RULES`

**Owner:** Policy platform

`src/underwriting/rules.py` contains synthetic eligibility and pricing rules
consumed by `shield-policy-service`. No downstream service dependencies.
`contracts/underwriting-api.yaml` describes the intended API.

Shared glossary, standards, scope, and component ownership live in
`amithp-ust/shield-context`. See its `AGENTS.md` before proposing changes.
`specs/` is reserved for published specification pull requests.

Python 3.12+, standard library only. Run `python -m unittest discover -s tests`.
These callable stubs do not run an HTTP server and are not production pricing.
