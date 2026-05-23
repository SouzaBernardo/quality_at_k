import requests
import csv
import sys
import os

BASE = "http://localhost:9000"
AUTH = ("admin", "sonarLike@21")

METRICS = [
    "ncloc", "lines", "files", "classes", "functions",
    "bugs", "vulnerabilities", "code_smells", "violations",
    "complexity", "cognitive_complexity",
    "coverage", "line_coverage",
    "duplicated_lines_density", "duplicated_blocks",
    "comment_lines_density",
    "sqale_rating", "reliability_rating", "security_rating",
    "sqale_index",
]

OUTPUT = os.path.join(os.path.dirname(__file__), "..", "sonar_metrics.csv")

resp = requests.get(f"{BASE}/api/projects/search?ps=500", auth=AUTH)
resp.raise_for_status()
projects = resp.json()["components"]
print(f"Found {len(projects)} projects", file=sys.stderr)

rows = []
for p in projects:
    key = p["key"]
    r = requests.get(
        f"{BASE}/api/measures/component",
        params={"component": key, "metricKeys": ",".join(METRICS)},
        auth=AUTH,
    )
    r.raise_for_status()
    measures = r.json().get("component", {}).get("measures", [])
    row = {"project": key}
    for m in measures:
        row[m["metric"]] = m.get("value", "")
    rows.append(row)
    print(f"  {key}", file=sys.stderr)

fieldnames = ["project"] + METRICS
with open(OUTPUT, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)

print(f"Saved {len(rows)} rows to {os.path.abspath(OUTPUT)}", file=sys.stderr)
