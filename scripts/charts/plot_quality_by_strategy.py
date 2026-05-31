"""
Gráfico 4: Quality@K (FQS) por Modelo e Estratégia de Prompting.

Fonte: sonar-metrics/fqs_aggregated.csv

Barras agrupadas por estratégia (H / C / I), modelos ordenados por FQS
médio decrescente. O GroundTruth é exibido como linha horizontal de
referência em vez de barra — por não ter estratégia de prompting.

Para alterar K no futuro, ajuste a coluna de interesse (fqs_mean ou
fqs_mean_all) e o título do eixo Y.

Uso:
    python scripts/charts/plot_quality_by_strategy.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import matplotlib.pyplot as plt
import seaborn as sns

from utils import (
    MODEL_DISPLAY,
    STRATEGY_COLORS,
    STRATEGY_LABELS,
    load_aggregated,
    save_figure,
    setup_style,
)

# Change to "fqs_mean_all" for the conservative estimate (NaN treated as 0)
FQS_COLUMN = "fqs_mean"

OUTPUT_NAME = "quality_fqs_by_model_strategy"


# ---------------------------------------------------------------------------
# Data preparation
# ---------------------------------------------------------------------------


def prepare_data(df):
    """
    Separate GroundTruth from LLM entries.
    Sort models by their mean FQS across all three strategies (descending).
    """
    gt = df[df["strategy"] == "GT"].copy()
    others = df[df["strategy"].isin(["H", "C", "I"])].copy()

    others["model_display"] = others["model"].map(lambda m: MODEL_DISPLAY.get(m, m))

    model_order = (
        others.groupby("model_display")[FQS_COLUMN]
        .mean()
        .sort_values(ascending=False)
        .index.tolist()
    )

    gt_fqs = float(gt[FQS_COLUMN].iloc[0]) if not gt.empty else None
    return others, model_order, gt_fqs


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------


def make_figure(df, model_order, gt_fqs):
    fig, ax = plt.subplots(figsize=(16, 6))

    bp = sns.barplot(
        data=df,
        x="model_display",
        y=FQS_COLUMN,
        hue="strategy",
        palette=STRATEGY_COLORS,
        order=model_order,
        hue_order=["H", "C", "I"],
        ax=ax,
        edgecolor="white",
        linewidth=0.5,
    )

    # Value labels above each bar
    for container in ax.containers:
        ax.bar_label(
            container,
            fmt="%.2f",
            fontsize=7,
            padding=2,
            label_type="edge",
        )

    # GroundTruth reference line
    if gt_fqs is not None:
        ax.axhline(
            gt_fqs,
            color="black",
            linestyle="--",
            linewidth=1.4,
            alpha=0.75,
            zorder=5,
        )
        # Anchor label to the right edge
        ax.text(
            len(model_order) - 0.45,
            gt_fqs + 0.006,
            f"GroundTruth  {gt_fqs:.2f}",
            fontsize=8.5,
            color="black",
            ha="right",
            va="bottom",
            alpha=0.85,
        )

    # Axis limits — leave room above bars for value labels
    max_val = df[FQS_COLUMN].max()
    ax.set_ylim(0, min(1.0, max_val * 1.22))

    ax.set_title(
        "Quality@1 (FQS) by Model and Prompting Strategy",
        pad=12,
    )
    ax.set_xlabel("Model")
    ax.set_ylabel("Quality@1 (FQS)")

    ax.yaxis.grid(True, linestyle="--", alpha=0.7)
    ax.xaxis.grid(False)
    ax.set_axisbelow(True)

    plt.xticks(rotation=30, ha="right")

    # Replace strategy codes with full names in the legend
    handles, labels = ax.get_legend_handles_labels()
    labels = [STRATEGY_LABELS.get(lb, lb) for lb in labels]
    ax.legend(handles, labels, title="Strategy", loc="upper right", framealpha=0.9)

    # Explicit margins: bottom for rotated labels, top for bar value labels
    fig.subplots_adjust(bottom=0.22, top=0.88, left=0.07, right=0.97)
    return fig


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main():
    setup_style()
    df = load_aggregated()
    data, model_order, gt_fqs = prepare_data(df)
    fig = make_figure(data, model_order, gt_fqs)
    save_figure(fig, OUTPUT_NAME)
    plt.close(fig)


if __name__ == "__main__":
    main()
