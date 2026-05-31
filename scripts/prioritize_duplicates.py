"""
Remove duplicate base_task entries within each (model, strategy) group,
keeping the record with the highest-priority status.

Priority (highest → lowest): Success > PartialSuccess > Fail > Error > Unknown
"""

import pathlib
import pandas as pd

ROOT = pathlib.Path(__file__).parent.parent
SONAR_DIR = ROOT / "sonar-metrics"
INPUT_CSV = SONAR_DIR / "combined_sonar_metrics.csv"

STATUS_PRIORITY = {
    "Success":        0,
    "PartialSuccess": 1,
    "Fail":           2,
    "Error":          3,
    "Unknown":        4,
}


def deduplicate(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["_priority"] = df["status"].map(STATUS_PRIORITY).fillna(99)

    df.sort_values("_priority", inplace=True)
    df.drop_duplicates(subset=["model", "strategy", "base_task"], keep="first", inplace=True)
    df.drop(columns=["_priority"], inplace=True)

    df.sort_values(
        by=["model", "base_task"],
        key=lambda col: col.str.lower(),
        inplace=True,
        ignore_index=True,
    )
    return df


def main() -> None:
    df = pd.read_csv(INPUT_CSV)
    before = len(df)

    dups_before = df.duplicated(subset=["model", "strategy", "base_task"], keep=False).sum()

    df = deduplicate(df)

    after = len(df)
    print(f"Linhas antes : {before}")
    print(f"Duplicatas   : {dups_before} ({dups_before // 2} pares)")
    print(f"Linhas depois: {after}  (removidas: {before - after})")

    df.to_csv(INPUT_CSV, index=False)
    print(f"Salvo em {INPUT_CSV}")


if __name__ == "__main__":
    main()
