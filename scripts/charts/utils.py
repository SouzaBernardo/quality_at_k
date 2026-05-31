"""
Shared utilities for all visualization scripts.

Run any plot script from the project root:
    python scripts/charts/plot_*.py
"""

import re
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ---------------------------------------------------------------------------
# Paths (resolved relative to this file's grandparent = project root)
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = ROOT / "sonar-metrics"
FIGURES_DIR = ROOT / "figures"

# ---------------------------------------------------------------------------
# Consistent visual constants shared across all scripts
# ---------------------------------------------------------------------------

STATUS_COLORS = {
    "Success": "#2ca02c",
    "PartialSuccess": "#ff7f0e",
    "Fail": "#d62728",
    "Error": "#7f7f7f",
    "Unknown": "#c7c7c7",
}

STRATEGY_COLORS = {"H": "#1f77b4", "C": "#ff7f0e", "I": "#2ca02c"}
STRATEGY_MARKERS = {"H": "o", "C": "s", "I": "^"}
STRATEGY_LABELS = {"H": "Holistic", "C": "Compositional", "I": "Incremental"}

# Display names for models (raw CSV names → publication-friendly labels)
MODEL_DISPLAY = {
    "ChatGLM": "ChatGLM",
    "GPT-3.5-Turbo": "GPT-3.5-Turbo",
    "GPT-4-Turbo": "GPT-4-Turbo",
    "PolyCoder-2.7B": "PolyCoder-2.7B",
    "Vicuna": "Vicuna",
    "WizardCoder-15B-V1.0": "WizardCoder-15B",
    "codegeex2-6b": "CodeGeeX-6B",
    "incoder": "InCoder",
    "instruct-codegen-16B": "Instruct-CodeGen-16B",
    "santacoder-1.1B": "SantaCoder-1.1B",
    "starcoder-instruct-15B": "StarCoder-Instruct-15B",
    "GroundTruth": "GroundTruth",
}

# ---------------------------------------------------------------------------
# Raw CSV filename → (model, strategy) parser  (mirrors merge_sonar_metrics.py)
# ---------------------------------------------------------------------------

_STRATEGY_PATTERNS = [
    (re.compile(r"_class_H_greedy$"), "H"),
    (re.compile(r"_method_C_greedy$"), "C"),
    (re.compile(r"_method_I_greedy$"), "I"),
    (re.compile(r"_100_c_t0$"), "H"),
    (re.compile(r"_100_m_dire$"), "C"),
    (re.compile(r"_100_m_iter$"), "I"),
    (re.compile(r"$"), "GT"),   # GroundTruth fallback (matches everything)
]


def _parse_raw_filename(csv_path: Path) -> tuple[str, str]:
    stem = csv_path.stem                          # sonar_metrics_GPT-4-Turbo_class_H_greedy_files
    stem = re.sub(r"^sonar_metrics_", "", stem)  # GPT-4-Turbo_class_H_greedy_files
    stem = re.sub(r"_files$", "", stem)          # GPT-4-Turbo_class_H_greedy
    for pattern, strategy in _STRATEGY_PATTERNS:
        m = pattern.search(stem)
        if m:
            model = stem[: m.start()] if m.start() > 0 else stem
            return model, strategy
    return stem, "N/A"

# ---------------------------------------------------------------------------
# Data loaders
# ---------------------------------------------------------------------------


def load_combined() -> pd.DataFrame:
    """Load deduplicated per-task metrics (combined_sonar_metrics.csv)."""
    return pd.read_csv(DATA_DIR / "combined_sonar_metrics.csv")


def load_aggregated() -> pd.DataFrame:
    """Load per-(model, strategy) aggregated FQS metrics (fqs_aggregated.csv)."""
    return pd.read_csv(DATA_DIR / "fqs_aggregated.csv")


def load_raw_all() -> pd.DataFrame:
    """
    Concatenate all raw SonarQube CSVs from sonar-metrics/raw/.
    Adds 'model' and 'strategy' columns derived from each filename.
    Includes extra columns not present in combined: bugs, vulnerabilities,
    duplicated_lines_density, duplicated_blocks, comment_lines_density.
    """
    raw_dir = DATA_DIR / "raw"
    frames = []
    for csv_path in sorted(raw_dir.glob("sonar_metrics_*_files.csv")):
        model, strategy = _parse_raw_filename(csv_path)
        df = pd.read_csv(csv_path)
        df["model"] = model
        df["strategy"] = strategy
        frames.append(df)
    if not frames:
        raise FileNotFoundError(f"No raw CSVs found in {raw_dir}")
    return pd.concat(frames, ignore_index=True)

# ---------------------------------------------------------------------------
# Style & I/O helpers
# ---------------------------------------------------------------------------


def setup_style() -> None:
    """Apply a clean, publication-ready style (seaborn paper + custom rcParams)."""
    sns.set_theme(style="whitegrid", context="paper")
    matplotlib.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "axes.titlesize": 13,
        "axes.labelsize": 12,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.dpi": 150,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.linestyle": "--",
        "grid.alpha": 0.6,
    })


def save_figure(fig: matplotlib.figure.Figure, name: str) -> None:
    """Save a figure as PNG (300 dpi) and PDF into the figures/ directory."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    for ext, kwargs in [("png", {"dpi": 300}), ("pdf", {})]:
        out = FIGURES_DIR / f"{name}.{ext}"
        fig.savefig(out, bbox_inches="tight", **kwargs)
        print(f"Saved: {out}")
