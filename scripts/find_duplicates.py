"""Find rows in combined_sonar_metrics.csv where the same base class appears
more than once for a given (model, strategy) pair — regardless of status.

Example: GPT-4 / strategy I having both ChatSuccess and ChatError counts as a duplicate
because they share the same base_task "Chat".
"""

import csv
import pathlib
from collections import defaultdict

CSV_PATH = pathlib.Path(__file__).parent / ".." / "sonar-metrics" / "new" / "combined_sonar_metrics.csv"


def find_duplicates() -> dict[tuple[str, str], list[tuple[str, list[str]]]]:
    """Returns {(model, strategy): [(base_task, [statuses, ...]), ...]} for groups with duplicates."""
    # (model, strategy, base_task) -> [status, ...]
    groups: dict[tuple[str, str, str], list[str]] = defaultdict(list)

    with open(CSV_PATH, newline="") as f:
        for row in csv.DictReader(f):
            key = (row["model"], row["strategy"], row["base_task"])
            groups[key].append(row["status"])

    results: dict[tuple[str, str], list[tuple[str, list[str]]]] = defaultdict(list)
    for (model, strategy, base_task), statuses in sorted(groups.items()):
        if len(statuses) > 1:
            results[(model, strategy)].append((base_task, sorted(statuses)))

    return dict(results)


def main() -> None:
    duplicates = find_duplicates()

    if not duplicates:
        print("No duplicates found.")
        return

    print(f"{'Model':<35} {'Strategy':<10} {'Base task':<35} {'Statuses'}")
    print("-" * 110)
    for (model, strategy), entries in sorted(duplicates.items()):
        for i, (base_task, statuses) in enumerate(entries):
            model_col = model if i == 0 else ""
            strat_col = strategy if i == 0 else ""
            print(f"{model_col:<35} {strat_col:<10} {base_task:<35} {', '.join(statuses)}")
        print()

    total_groups = len(duplicates)
    total_classes = sum(len(v) for v in duplicates.values())
    print(f"Summary: {total_groups} (model, strategy) group(s) affected, {total_classes} duplicate base task(s) total.")


if __name__ == "__main__":
    main()
