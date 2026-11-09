"""Sort a CSV by (model, strategy, file), with strategies ordered H→C→I→GT.

Usage:
  python3 sort_csv.py <input.csv> [output.csv]

If output.csv is omitted, the input file is overwritten.
"""

import sys
import pathlib
import pandas as pd

STRATEGY_ORDER = {"H": 0, "C": 1, "I": 2, "GT": 3, "N/A": 4}


def sort_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["_strategy_order"] = df["strategy"].map(STRATEGY_ORDER).fillna(99)
    df.sort_values(
        by=["model", "_strategy_order", "file"],
        key=lambda col: (
            col.str.lower() if pd.api.types.is_string_dtype(col.dtype) else col
        ),
        inplace=True,
        ignore_index=True,
    )
    df.drop(columns=["_strategy_order"], inplace=True)
    return df


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 sort_csv.py <input.csv> [output.csv]", file=sys.stderr)
        sys.exit(1)

    input_path = pathlib.Path(sys.argv[1])
    output_path = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else input_path

    df = pd.read_csv(input_path)
    sorted_df = sort_df(df)
    sorted_df.to_csv(output_path, index=False)
    print(f"Sorted {len(sorted_df)} rows → {output_path}")


if __name__ == "__main__":
    main()
