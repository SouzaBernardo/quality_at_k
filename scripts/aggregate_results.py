import pathlib
import pandas as pd

ROOT = pathlib.Path(__file__).parent.parent
COMBINED_CSV = ROOT / "output" / "results" / "combined_sonar_metrics.csv"
OUTPUT_CSV   = ROOT / "output" / "results" / "aggregated_results.csv"

df = pd.read_csv(COMBINED_CSV)

agg = (
    df.groupby(["model", "strategy", "status"], sort=False)
    .agg(
        count=("base_task", "count"),
        pass_val_mean=("pass_val", "mean"),
        fqs_mean=("fqs", "mean"),
    )
    .reset_index()
)

agg = agg.sort_values(["model", "status"]).reset_index(drop=True)

agg.to_csv(OUTPUT_CSV, index=False, float_format="%.6f")
print(agg.to_string(index=False))
print(f"\nSalvo em {OUTPUT_CSV}")
