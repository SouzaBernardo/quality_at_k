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

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "sonar-metrics")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def fetch_files(project_key):
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

    return rows


def save_csv(project_key, rows):
    output_path = os.path.join(OUTPUT_DIR, f"sonar_metrics_{project_key}_files.csv")
    fieldnames = ["file", "path"] + METRICS
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return output_path


r = requests.get(f"{BASE}/api/projects/search?ps=500", auth=AUTH)
r.raise_for_status()
projects = r.json()["components"]
print(f"Found {len(projects)} projects", file=sys.stderr)

for p in projects:
    key = p["key"]
    rows = fetch_files(key)
    path = save_csv(key, rows)
    print(f"  [{len(rows):>3} files] {key}", file=sys.stderr)

print(f"\nDone. Files saved to: {os.path.abspath(OUTPUT_DIR)}", file=sys.stderr)
