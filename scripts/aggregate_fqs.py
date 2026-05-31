"""
Computes per-(model, strategy) aggregated Quality@1 metrics from
combined_sonar_metrics.csv and writes the result to fqs_aggregated.csv.

Columns produced:
  model, strategy
  n_tasks          — total tasks in the group
  n_success        — tasks with status=Success
  n_fqs_valid      — tasks where fqs is not NaN
  pass_rate        — n_success / n_tasks
  fqs_mean         — mean fqs over valid (non-NaN) tasks only
  fqs_mean_all     — mean fqs treating NaN as 0 (conservative, full denominator)
"""

import pathlib
import pandas as pd

ROOT = pathlib.Path(__file__).parent.parent
SONAR_DIR = ROOT / "sonar-metrics" / "new"
INPUT_CSV  = SONAR_DIR / "combined_sonar_metrics.csv"
OUTPUT_CSV = SONAR_DIR / "fqs_aggregated.csv"


def aggregate(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (model, strategy), group in df.groupby(["model", "strategy"], sort=False):
        n_tasks     = len(group)
        n_success   = (group["status"] == "Success").sum()
        n_fqs_valid = group["fqs"].notna().sum()

        pass_rate     = n_success / n_tasks if n_tasks else None
        fqs_mean      = group["fqs"].mean()                       # NaN excluded
        fqs_mean_all  = group["fqs"].fillna(0).mean()             # NaN treated as 0

        rows.append({
            "model":        model,
            "strategy":     strategy,
            "n_tasks":      n_tasks,
            "n_success":    n_success,
            "n_fqs_valid":  n_fqs_valid,
            "pass_rate":    round(pass_rate, 4) if pass_rate is not None else None,
            "fqs_mean":     round(fqs_mean, 6)    if pd.notna(fqs_mean)    else None,
            "fqs_mean_all": round(fqs_mean_all, 6),
        })

    result = pd.DataFrame(rows)

    gt = result[result["model"] == "GroundTruth"]
    others = result[result["model"] != "GroundTruth"].sort_values(
        by=["fqs_mean", "model"],
        ascending=[False, True],
        key=lambda col: col.str.lower() if col.dtype == object else col,
    )
    return pd.concat([gt, others], ignore_index=True)


def main() -> None:
    df = pd.read_csv(INPUT_CSV)
    result = aggregate(df)
    result.to_csv(OUTPUT_CSV, index=False)

    print(result.to_string(index=False))
    print(f"\nEscrito: {len(result)} grupos → {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
