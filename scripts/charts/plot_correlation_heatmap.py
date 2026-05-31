"""
Gráfico 3: Heatmap de Correlação de Spearman entre Métricas de Qualidade.

Fontes:
  • sonar-metrics/combined_sonar_metrics.csv  — ncloc, sqale_index,
    cognitive_complexity, complexity, code_smells, fqs
  • sonar-metrics/raw/*.csv  — bugs, vulnerabilities,
    duplicated_lines_density, duplicated_blocks

Os raw CSVs são mesclados com o combined via (model, strategy, file)
para obter o conjunto completo de métricas por tarefa.

Apenas o triângulo inferior da matriz é exibido para evitar redundância.

Uso:
    python scripts/charts/plot_correlation_heatmap.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from utils import load_combined, load_raw_all, save_figure, setup_style

OUTPUT_NAME = "correlation_heatmap_spearman"

# Metrics to include in the correlation matrix (order controls display order)
METRIC_COLS = [
    "ncloc",
    "cognitive_complexity",
    "complexity",
    "code_smells",
    "sqale_index",
    "bugs",
    "duplicated_lines_density",
    "duplicated_blocks",
    "fqs",
]

# Publication-friendly axis labels (newlines kept short for readability)
METRIC_LABELS = {
    "ncloc":                    "NCLOC",
    "cognitive_complexity":     "Cognitive\nComplexity",
    "complexity":               "Cyclomatic\nComplexity",
    "code_smells":              "Code Smells",
    "sqale_index":              "Tech Debt\n(sqale_index)",
    "bugs":                     "Bugs",
    "vulnerabilities":          "Vulnerabilities",
    "duplicated_lines_density": "Duplication\n(%)",
    "duplicated_blocks":        "Duplicated\nBlocks",
    "fqs":                      "Quality@1\n(FQS)",
}


# ---------------------------------------------------------------------------
# Data preparation
# ---------------------------------------------------------------------------


def build_wide_df():
    """
    Merge combined_sonar_metrics with raw CSVs to obtain all metrics per task.
    The 'file' column is the join key (filename with status suffix, e.g. FooSuccess.py).
    """
    combined = load_combined()[
        ["model", "strategy", "file",
         "ncloc", "sqale_index", "cognitive_complexity",
         "complexity", "code_smells", "fqs"]
    ]

    # Extra columns only available in raw SonarQube exports
    raw_cols = ["model", "strategy", "file",
                "bugs", "vulnerabilities",
                "duplicated_lines_density", "duplicated_blocks"]
    raw = load_raw_all()[raw_cols]

    wide = combined.merge(raw, on=["model", "strategy", "file"], how="left")
    return wide


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------


def make_figure(wide_df):
    # Keep only metrics that actually exist in the merged dataframe
    metrics = [c for c in METRIC_COLS if c in wide_df.columns]
    corr = wide_df[metrics].corr(method="spearman")

    # Rename axes to friendly labels
    labels = [METRIC_LABELS.get(c, c) for c in corr.columns]
    corr.index = labels
    corr.columns = labels

    # Mask the upper triangle (redundant half)
    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(11, 9))

    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".2f",
        cmap="RdYlGn",
        vmin=-1,
        vmax=1,
        center=0,
        square=True,
        linewidths=0.5,
        linecolor="white",
        cbar_kws={"shrink": 0.75, "label": "Spearman ρ"},
        ax=ax,
        annot_kws={"size": 9},
    )

    ax.set_title(
        "Spearman Correlation Matrix of Software Quality Metrics\n"
        "(all models and strategies combined)",
        pad=14,
    )
    plt.xticks(rotation=45, ha="right", fontsize=9)
    plt.yticks(rotation=0, fontsize=9)

    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main():
    setup_style()
    wide_df = build_wide_df()
    fig = make_figure(wide_df)
    save_figure(fig, OUTPUT_NAME)
    plt.close(fig)


if __name__ == "__main__":
    main()
