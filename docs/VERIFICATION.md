# Verification Standard

This registry's only claim to exist is that its facts are *measured*, not declared.
This document is the binding standard for how entries are checked, labelled and demoted.
If the data and this document disagree, the data is wrong.

## Verification levels

| Level | Name | What is actually done | Applies to |
|---|---|---|---|
| L0 | Listed | Entry transcribed from a source list. Nothing checked. | All new entries |
| L1 | Document-checked | Documentation, pricing and status pages fetched and parsed by an agent; free-tier claims backed by stored page evidence (URL + fetch time + extracted quote). | All entries |
| L2 | Endpoint-probed | The API endpoint itself is called without credentials; HTTP status, latency and a response sample are recorded. CORS and HTTPS are recorded from the *actual response*, not the docs. | `auth = No` entries |
| L3 | Account-tested | A real API key is used; quota and rate limits confirmed against the live account. | Opt-in, per-API only |

Rules:

- A level is claimed only for checks actually performed. "The vendor says it is free" is L1 evidence, never L2.
- No bulk account sign-ups for L3. Ever. L3 happens per-API, through the normal front door.
- Every measured field carries `last_checked` (UTC) and an evidence reference.

## Status lifecycle

`unverified → live → changed → sunset`

- **live** — last check passed at the entry's claimed level.
- **changed** — a material fact changed (pricing, quota, auth, endpoint, terms). The change is appended to the entry's change log with before/after evidence.
- **sunset** — the API is gone, shut down, or no longer offers any free access. Sunset entries are removed from the default registry views and kept in the archive with their sunset date. Nothing dead is ever presented as usable.

## Freshness and demotion

- No-auth entries are probed daily; auth-required entries get an L1 document check weekly.
- Three consecutive failed probes, or a documented shutdown/paywall announcement, moves an entry to the alert queue for a human decision — agents demote, humans confirm sunsets.
- Scores shown publicly: freshness (age of last check), reliability (90-day probe success rate), free-tier truth (does measured free access match the listing claim).

## Probe etiquette

Daily cadence, low concurrency, honest `User-Agent` identifying this project.
No load testing, no quota exhaustion, no circumvention of paywalls or access controls.
If a vendor asks us to stop probing, we stop and mark the entry L1-max.
