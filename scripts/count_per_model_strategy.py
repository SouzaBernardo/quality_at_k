"""Count total rows per (model, strategy) in combined_sonar_metrics.csv."""

import csv
import pathlib
from collections import defaultdict

CSV_PATH = pathlib.Path(__file__).parent / ".." / "sonar-metrics" / "new" / "combined_sonar_metrics.csv"


def main() -> None:
    counts: dict[tuple[str, str], int] = defaultdict(int)

    with open(CSV_PATH, newline="") as f:
        for row in csv.DictReader(f):
            counts[(row["model"], row["strategy"])] += 1

    for (model, strategy), total in sorted(counts.items()):
        print(f"modelo {model} estratégia {strategy}: {total} linhas")


if __name__ == "__main__":
    main()
