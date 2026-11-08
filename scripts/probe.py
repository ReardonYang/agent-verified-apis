#!/usr/bin/env python3
"""First-pass prober for the Agent-Verified APIs registry.

For every entry in data/apis.json, fetches the listed URL and records what is
actually observable from the response: reachability, HTTP status, latency,
whether the response carries CORS headers, and TLS use. This measures the
*listed URL*, which for many entries is the docs/homepage rather than a call
endpoint -- treat results as an L1 reachability signal. True L2 endpoint
probing needs a per-API endpoint definition (roadmap) and is never faked here.

Usage:  python3 scripts/probe.py [--only-no-auth] [--out results.json]
Etiquette: low concurrency, honest User-Agent, 10s timeout, one attempt.
"""
import argparse, concurrent.futures, json, time, urllib.request, urllib.error

UA = {"User-Agent": "agent-verified-apis/probe (+https://github.com/ReardonYang/agent-verified-apis)"}

def probe(entry):
    url = entry["url"]
    t0 = time.time()
    rec = {"name": entry["name"], "url": url, "checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    try:
        req = urllib.request.Request(url, headers=UA, method="GET")
        with urllib.request.urlopen(req, timeout=10) as r:
            rec.update(status_code=r.status, reachable=True,
                       latency_ms=round((time.time() - t0) * 1000),
                       https=url.startswith("https://"),
                       cors_header=bool(r.headers.get("Access-Control-Allow-Origin")))
    except urllib.error.HTTPError as e:
        rec.update(status_code=e.code, reachable=True,
                   latency_ms=round((time.time() - t0) * 1000),
                   https=url.startswith("https://"),
                   cors_header=bool(e.headers and e.headers.get("Access-Control-Allow-Origin")))
    except Exception as e:
        rec.update(status_code=None, reachable=False, error=type(e).__name__)
    return rec

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only-no-auth", action="store_true")
    ap.add_argument("--out", default="probe-results.json")
    args = ap.parse_args()
    data = json.load(open("data/apis.json", encoding="utf-8"))
    entries = data["apis"]
    if args.only_no_auth:
        entries = [e for e in entries if e["auth"] == "No"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
        results = list(ex.map(probe, entries))
    json.dump(results, open(args.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    ok = sum(1 for r in results if r.get("reachable"))
    print(f"probed {len(results)} entries, reachable {ok}, wrote {args.out}")

if __name__ == "__main__":
    main()
