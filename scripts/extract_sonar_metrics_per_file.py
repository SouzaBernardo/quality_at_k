import requests
import csv
import sys
import os
import math

BASE = "http://localhost:9000"
AUTH = ("admin", "sonarLike@21")

METRICS = [
    "ncloc", "lines", "functions",
    "bugs", "vulnerabilities", "code_smells", "violations",
    "complexity", "cognitive_complexity",
    "duplicated_lines_density", "duplicated_blocks",
    "comment_lines_density",
    "sqale_index",
]

if len(sys.argv) < 2:
    print("Usage: python3 extract_sonar_metrics_per_file.py <project_key> [output_dir]", file=sys.stderr)
    sys.exit(1)

project_key = sys.argv[1]
output_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(__file__), "..")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, f"sonar_metrics_{project_key}_files.csv")

rows = []
page = 1
total_pages = None

while True:
    r = requests.get(
        f"{BASE}/api/measures/component_tree",
        params={
            "component": project_key,
            "qualifiers": "FIL",
            "metricKeys": ",".join(METRICS),
            "ps": 500,
            "p": page,
        },
        auth=AUTH,
    )
    r.raise_for_status()
    data = r.json()

    if total_pages is None:
        paging = data["paging"]
        total_pages = math.ceil(paging["total"] / paging["pageSize"])
        print(f"Project: {project_key} — {paging['total']} files", file=sys.stderr)

    for component in data["components"]:
        row = {
            "file": component["name"],
            "path": component["path"],
        }
        for m in component.get("measures", []):
            row[m["metric"]] = m.get("value", "")
        rows.append(row)

    if page >= total_pages:
        break
    page += 1

fieldnames = ["file", "path"] + METRICS
with open(output_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)

print(f"Saved {len(rows)} rows to {os.path.abspath(output_path)}", file=sys.stderr)
