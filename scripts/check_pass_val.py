"""Verifica se pass_val em combined_sonar_metrics.csv bate com pass@1_value
em pass_at_1_greedy_per_task.csv para cada (model, strategy, base_task).

GroundTruth é esperado como pass_val=1.0 (não está no arquivo de pass@1).
"""

import csv
import pathlib

BASE = pathlib.Path(__file__).parent / ".." / "sonar-metrics" / "new"
COMBINED = BASE / "combined_sonar_metrics.csv"
PASS_CSV = BASE / "pass_at_1_greedy_per_task.csv"

MODEL_KEY_MAP = {
    "ChatGLM": "ChatGLM",
    "GPT-3.5-Turbo": "GPT-3.5",
    "GPT-4-Turbo": "GPT-4",
    "PolyCoder-2.7B": "PolyCoder",
    "Vicuna": "Vicuna",
    "WizardCoder-15B-V1.0": "WizardCoder",
    "codegeex2-6b": "CodeGeeX",
    "incoder": "Incoder",
    "instruct-codegen-16B": "Instruct-CodeGen",
    "santacoder-1.1B": "SantaCoder",
    "starcoder-instruct-15B": "Instruct-StarCoder",
    "GroundTruth": None,
}


def load_pass_lookup() -> dict[tuple[str, str], float]:
    lookup: dict[tuple[str, str], float] = {}
    with open(PASS_CSV, newline="") as f:
        for row in csv.DictReader(f):
            lookup[(row["model"], row["task"])] = float(row["pass@1_value"])
    return lookup


def main() -> None:
    pass_lookup = load_pass_lookup()

    divergences = []
    missing_in_pass = []
    checked = 0

    seen: set[tuple[str, str, str]] = set()  # deduplica por (model, strategy, base_task)

    with open(COMBINED, newline="") as f:
        for row in csv.DictReader(f):
            model = row["model"]
            strategy = row["strategy"]
            base_task = row["base_task"]
            pass_val_str = row["pass_val"]

            dedup_key = (model, strategy, base_task)
            if dedup_key in seen:
                continue
            seen.add(dedup_key)

            if model == "GroundTruth":
                expected = 1.0
            else:
                model_key = MODEL_KEY_MAP.get(model)
                if model_key is None:
                    continue
                lookup_key = (f"{model_key}_{strategy}", base_task)
                if lookup_key not in pass_lookup:
                    missing_in_pass.append((model, strategy, base_task))
                    continue
                expected = pass_lookup[lookup_key]

            actual = float(pass_val_str) if pass_val_str != "" else None
            checked += 1

            if actual != expected:
                divergences.append((model, strategy, base_task, expected, actual))

    if missing_in_pass:
        print(f"=== Não encontrados no pass@1 ({len(missing_in_pass)}) ===")
        for model, strategy, base_task in missing_in_pass:
            print(f"  {model} / {strategy} / {base_task}")
        print()

    if divergences:
        print(f"=== pass_val divergente ({len(divergences)}) ===")
        print(f"  {'Model':<25} {'Strat':<6} {'base_task':<35} {'esperado':>10} {'atual':>10}")
        print("  " + "-" * 90)
        for model, strategy, base_task, expected, actual in divergences:
            print(f"  {model:<25} {strategy:<6} {base_task:<35} {expected:>10.1f} {str(actual):>10}")
        print()
        print(f"Total: {len(divergences)} divergências em {checked} verificados.")
    else:
        print(f"OK — todos os {checked} pass_val conferem com o pass@1.")


if __name__ == "__main__":
    main()
