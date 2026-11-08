# Contributing

New APIs and corrections are welcome. One thing works differently here:
**a submission is the start of verification, not the end of it.** Entries land at L0
and are promoted only when the registry's own checks have measured them.

## Add an API

Open a PR adding one row per API to `data/apis.json` (and the matching README table):

- `name`, official `url` (documentation or homepage), one-line `description`
- `category` — use an existing category where one fits
- `auth` — exactly one of `No`, `apiKey`, `OAuth`
- `https_listed`, `cors_listed` — what the vendor claims (mark `Unknown` if unstated;
  these get replaced by measured values after probing)

Do not set `verify_level`, `status`, or `last_checked` yourself — the pipeline owns them.

## Report a dead or changed API

Open an issue with the entry name and what you observed (with a date).
If our probes confirm it, the entry is demoted or sunset per
[docs/VERIFICATION.md](docs/VERIFICATION.md) — thank you for the signal.

## Ground rules

- Free access must exist (a genuine free tier, not only a trial).
- No affiliate or tracking links. No SEO submissions.
- One API per PR keeps review and verification fast.
