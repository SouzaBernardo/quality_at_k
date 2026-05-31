import pathlib
import re

from compute_fqs import compute_fqs

import pandas as pd

ROOT = pathlib.Path(__file__).parent.parent
SONAR_DIR = ROOT / "sonar-metrics"
PASS_AT_K_CSV = SONAR_DIR / "pass_at_greedy_value.csv"
OUTPUT_CSV = SONAR_DIR / "combined_sonar_metrics.csv"

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

STRATEGY_ORDER = {"H": 0, "C": 1, "I": 2, "N/A": 3}

# Matches the strategy/sampling suffix from the middle of the filename
_STRATEGY_PATTERNS = [
    (re.compile(r"_class_H_greedy$"), "H"),
    (re.compile(r"_method_C_greedy$"), "C"),
    (re.compile(r"_method_I_greedy$"), "I"),
    (re.compile(r"_100_c_t0$"), "H"),
    (re.compile(r"_100_m_dire$"), "C"),
    (re.compile(r"_100_m_iter$"), "I"),
    (re.compile(r"$"), "GT"),  # GroundTruth fallback
]


def parse_filename(csv_path: pathlib.Path) -> tuple[str, str]:
    stem = csv_path.stem  # e.g. sonar_metrics_GPT-4-Turbo_class_H_greedy_files
    stem = re.sub(r"^sonar_metrics_", "", stem)
    stem = re.sub(r"_files$", "", stem)  # e.g. GPT-4-Turbo_class_H_greedy

    for pattern, strategy in _STRATEGY_PATTERNS:
        m = pattern.search(stem)
        if m:
            model = stem[: m.start()] if m.start() > 0 else stem
            return model, strategy

    return stem, "N/A"


def parse_file_status(filename: str) -> tuple[str, str]:
    stem = pathlib.Path(filename).stem
    for suffix in ["PartialSuccess", "Success", "Fail", "Error", "Unknown"]:
        if stem.endswith(suffix):
            return stem[: -len(suffix)], suffix
    return stem, "Success" # GroundTruth fallback


def main() -> None:
    pass_df = pd.read_csv(PASS_AT_K_CSV)
    pass_lookup = {
        (r["model"], r["task"]): r["pass@1_value"]
        for _, r in pass_df.iterrows()
    }

    csv_files = sorted((SONAR_DIR / "raw").glob("sonar_metrics_*_files.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No per-file CSVs found in {SONAR_DIR}")

    frames = []

    for csv_path in csv_files:
        model, strategy = parse_filename(csv_path)

        model_key = MODEL_KEY_MAP.get(model)
        model_strategy_key = f"{model_key}_{strategy}" if model_key is not None and strategy != "N/A" else None
        is_ground_truth = (model == "GroundTruth")

        df = pd.read_csv(csv_path)

        rows = []
        for _, row in df.iterrows():
            filename = str(row.get("file", ""))
            base_task, status = parse_file_status(filename)

            if is_ground_truth:
                pass_val = 1.0
            else:
                pass_val = pass_lookup.get((model_strategy_key, base_task)) if model_strategy_key else None

            ncloc = row.get("ncloc")
            sqale_index = row.get("sqale_index")
            cognitive_complexity = row.get("cognitive_complexity")
            complexity = row.get("complexity")
            code_smells = row.get("code_smells")

            if status == "N/A" or pass_val is None:
                fqs = None
            elif status != "Success":
                fqs = 0.0
            else:
                nl = 0.0 if pd.isna(ncloc) else float(ncloc)
                si = 0.0 if pd.isna(sqale_index) else float(sqale_index)
                if nl == 0:
                    fqs = float(pass_val)
                else:
                    fqs = compute_fqs(float(pass_val), si, nl)

            rows.append({
                "model": model,
                "strategy": strategy,
                "file": filename,
                "base_task": base_task,
                "status": status,
                "ncloc": 0.0 if pd.isna(ncloc) else float(ncloc),
                "sqale_index": 0.0 if pd.isna(sqale_index) else float(sqale_index),
                "cognitive_complexity": cognitive_complexity,
                "complexity": complexity,
                "code_smells": code_smells,
                "pass_val": pass_val,
                "fqs": fqs,
            })

        frames.append(pd.DataFrame(rows))

    combined = pd.concat(frames, ignore_index=True)

    combined["_strategy_order"] = combined["strategy"].map(STRATEGY_ORDER).fillna(99)
    combined.sort_values(
        by=["model", "_strategy_order", "file"],
        key=lambda col: col.str.lower() if col.dtype == object else col,
        inplace=True,
        ignore_index=True,
    )
    combined.drop(columns=["_strategy_order"], inplace=True)

    combined.to_csv(OUTPUT_CSV, index=False)
    print(f"Wrote {len(combined)} rows to {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
