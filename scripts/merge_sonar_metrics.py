import json
import math
import pathlib
import re

import pandas as pd

ROOT = pathlib.Path(__file__).parent.parent
SONAR_DIR = ROOT / "sonar-metrics"
PASS_AT_K_JSON = ROOT.parent / "ClassEval" / "output" / "result" / "pass_at_k_result.json"
OUTPUT_CSV = SONAR_DIR / "combined_sonar_metrics.csv"

BETA = 0.1

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
    (re.compile(r"$"), "N/A"),  # GroundTruth fallback
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
    return stem, "N/A"


def compute_fqs(status: str, sqale_index, ncloc):
    if status == "N/A":
        return None
    try:
        si = float(sqale_index)
        nl = float(ncloc)
    except (TypeError, ValueError):
        return None
    if math.isnan(si) or math.isnan(nl) or nl == 0:
        return None
    pass_binary = 1 if status == "Success" else 0
    penalty = min(1.0, BETA * si / nl)
    return pass_binary * (1.0 - penalty)


def main() -> None:
    with open(PASS_AT_K_JSON) as f:
        pass_data = json.load(f)["pass_1"]

    csv_files = sorted(SONAR_DIR.glob("sonar_metrics_*_files.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No per-file CSVs found in {SONAR_DIR}")

    frames = []

    for csv_path in csv_files:
        model, strategy = parse_filename(csv_path)

        model_key = MODEL_KEY_MAP.get(model)
        if model_key is not None and strategy != "N/A":
            json_key = f"{model_key}_{strategy}"
            pass_val = pass_data.get(json_key, {}).get("class_success")
        else:
            pass_val = None

        df = pd.read_csv(csv_path)

        rows = []
        for _, row in df.iterrows():
            filename = str(row.get("file", ""))
            base_task, status = parse_file_status(filename)

            ncloc = row.get("ncloc")
            sqale_index = row.get("sqale_index")
            cognitive_complexity = row.get("cognitive_complexity")
            complexity = row.get("complexity")
            code_smells = row.get("code_smells")

            fqs = compute_fqs(status, sqale_index, ncloc)

            rows.append({
                "model": model,
                "strategy": strategy,
                "file": filename,
                "base_task": base_task,
                "status": status,
                "ncloc": ncloc,
                "sqale_index": sqale_index,
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
