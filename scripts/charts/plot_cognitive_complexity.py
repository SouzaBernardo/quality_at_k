"""
Gráfico 1: Complexidade Cognitiva Média por Modelo e Status de Execução.

Fonte: sonar-metrics/combined_sonar_metrics.csv

Mostra a média de cognitive_complexity por (model, status), agregando
todas as estratégias (H, C, I) em uma única visualização.
Modelos ordenados por média total decrescente de complexidade cognitiva.

Uso:
    python scripts/charts/plot_cognitive_complexity.py
"""

import sys
from pathlib import Path

# Allow importing utils from the same package when run as a standalone script
sys.path.insert(0, str(Path(__file__).parent))

import matplotlib.pyplot as plt
import seaborn as sns

from utils import (
    MODEL_DISPLAY,
    STATUS_COLORS,
    load_combined,
    save_figure,
    setup_style,
)

# Statuses to include (Unknown excluded — rarely meaningful for complexity analysis)
STATUSES_TO_PLOT = ["Success", "PartialSuccess", "Fail", "Error"]

OUTPUT_NAME = "cognitive_complexity_by_model_status"


# ---------------------------------------------------------------------------
# Data preparation
# ---------------------------------------------------------------------------


def prepare_data(df):
    """
    Compute mean cognitive_complexity per (model, status) across all strategies.
    Returns the aggregated DataFrame and a model ordering list (desc. complexity).
    """
    df = df[df["status"].isin(STATUSES_TO_PLOT) & (df["model"] != "GroundTruth")]
    df = df.dropna(subset=["cognitive_complexity"])

    grouped = (
        df.groupby(["model", "status"])["cognitive_complexity"]
        .mean()
        .reset_index()
        .rename(columns={"cognitive_complexity": "mean_cog_complexity"})
    )

    # Sort models by their overall mean cognitive complexity (descending)
    model_order = (
        df.groupby("model")["cognitive_complexity"]
        .mean()
        .sort_values(ascending=False)
        .index.tolist()
    )

    # Apply publication-friendly display names
    grouped["model"] = grouped["model"].map(lambda m: MODEL_DISPLAY.get(m, m))
    model_order = [MODEL_DISPLAY.get(m, m) for m in model_order]

    return grouped, model_order


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------


def make_figure(grouped_df, model_order):
    fig, ax = plt.subplots(figsize=(16, 6))

    sns.barplot(
        data=grouped_df,
        x="model",
        y="mean_cog_complexity",
        hue="status",
        palette=STATUS_COLORS,
        order=model_order,
        hue_order=STATUSES_TO_PLOT,
        ax=ax,
        edgecolor="white",
        linewidth=0.5,
    )

    ax.set_title(
        "Mean Cognitive Complexity by Model and Execution Status\n"
        "(averaged across all prompting strategies)",
        pad=12,
    )
    ax.set_xlabel("Model")
    ax.set_ylabel("Mean Cognitive Complexity")

    # Horizontal grid only for readability
    ax.yaxis.grid(True, linestyle="--", alpha=0.7)
    ax.xaxis.grid(False)
    ax.set_axisbelow(True)

    plt.xticks(rotation=30, ha="right")

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(
        handles, labels,
        title="Execution Status",
        loc="upper right",
        framealpha=0.9,
    )

    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main():
    setup_style()

    df = load_combined()
    grouped, model_order = prepare_data(df)

    fig = make_figure(grouped, model_order)
    save_figure(fig, OUTPUT_NAME)
    plt.close(fig)


if __name__ == "__main__":
    main()
