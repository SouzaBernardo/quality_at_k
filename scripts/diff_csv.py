"""Diff pass_val e fqs entre sonar_metrics_consolidated_master.csv e combined_sonar_metrics.csv.

Key: (model, strategy, file)
Linhas únicas em cada arquivo são resumidas por modelo (contagem).
O detalhe completo é mostrado apenas para linhas em comum com pass_val ou fqs divergentes.
"""

import csv
import pathlib
from collections import defaultdict

BASE = pathlib.Path(__file__).parent / ".." / "sonar-metrics" / "new"
MASTER = BASE / "sonar_metrics_consolidated_master.csv"
COMBINED = BASE / "combined_sonar_metrics.csv"

KEY = ("model", "strategy", "file")
COMPARE_FIELDS = ("pass_val", "fqs")


def load(path: pathlib.Path) -> dict[tuple, dict]:
    with open(path, newline="") as f:
        return {tuple(r[k] for k in KEY): r for r in csv.DictReader(f)}


def count_by_model(keys: list[tuple]) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for model, strategy, _ in keys:
        counts[f"{model}/{strategy}"] += 1
    return dict(sorted(counts.items()))


def main() -> None:
    master = load(MASTER)
    combined = load(COMBINED)

    only_master = sorted(set(master) - set(combined))
    only_combined = sorted(set(combined) - set(master))
    common = sorted(set(master) & set(combined))

    changed = []
    for key in common:
        diffs = {
            field: (master[key][field], combined[key][field])
            for field in COMPARE_FIELDS
            if master[key][field] != combined[key][field]
        }
        if diffs:
            changed.append((key, diffs))

    # --- linhas únicas: só contagem por modelo ---
    if only_master:
        print(f"=== Apenas em master ({len(only_master)} linhas) ===")
        for model_strat, count in count_by_model(only_master).items():
            print(f"  {model_strat}: {count}")
        print()

    if only_combined:
        print(f"=== Apenas em combined ({len(only_combined)} linhas) ===")
        for model_strat, count in count_by_model(only_combined).items():
            print(f"  {model_strat}: {count}")
        print()

    # --- valores divergentes: detalhe completo ---
    if changed:
        print(f"=== pass_val / fqs divergentes ({len(changed)} linhas) ===")
        print(f"  {'Model/Strategy':<30} {'file':<40} {'campo':<10} {'master':>15} {'combined':>15}")
        print("  " + "-" * 115)
        for (model, strategy, file_), diffs in changed:
            for field, (v_master, v_combined) in diffs.items():
                print(f"  {model+'/'+strategy:<30} {file_:<40} {field:<10} {v_master:>15} {v_combined:>15}")
        print()
    else:
        print("OK — pass_val e fqs idênticos em todas as linhas comuns.")

    print(
        f"Resumo: {len(only_master)} só no master | "
        f"{len(only_combined)} só no combined | "
        f"{len(changed)} com valores diferentes"
    )


if __name__ == "__main__":
    main()
