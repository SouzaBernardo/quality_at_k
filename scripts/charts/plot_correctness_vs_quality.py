"""
Gráfico 2: Corretude Funcional vs Qualidade do Código (Scatter).

Fonte: sonar-metrics/fqs_aggregated.csv

Cada ponto = um par (model, strategy).
  • Cor    → modelo  (paleta tab20, 12 cores distintas)
  • Marcador → estratégia  (H=circle, C=square, I=triangle)
  • Linha pontilhada y=x: qualidade igual à corretude funcional (referência ideal)

Labels próximos a cada ponto com nome do modelo + estratégia.
Com 33 pontos em espaço reduzido, alguma sobreposição é esperada;
instale `adjustText` para reposicionamento automático:
    pip install adjustText

Uso:
    python scripts/charts/plot_correctness_vs_quality.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

from utils import (
    MODEL_DISPLAY,
    STRATEGY_LABELS,
    STRATEGY_MARKERS,
    load_aggregated,
    save_figure,
    setup_style,
)

OUTPUT_NAME = "correctness_vs_quality_scatter"

# Vertical offset (in data units) per strategy to partially separate
# labels that share the same model cluster
_LABEL_DY = {"H": +0.018, "C": -0.018, "I": +0.004}
_LABEL_DX = 0.008


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _model_color_map(models):
    """Map each unique model name to a color from tab20."""
    unique = sorted(set(models))
    cmap = plt.cm.tab20
    return {m: cmap(i / max(len(unique) - 1, 1)) for i, m in enumerate(unique)}


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------


def make_figure(df):
    gt_mask = df["strategy"] == "GT"
    others = df[~gt_mask].copy()
    gt = df[gt_mask].copy()

    others["model_display"] = others["model"].map(lambda m: MODEL_DISPLAY.get(m, m))
    model_colors = _model_color_map(others["model_display"].unique())

    fig, ax = plt.subplots(figsize=(11, 9))

    # --- Reference line y = x ---
    ref = np.linspace(0, 1, 200)
    ax.plot(ref, ref, linestyle="--", color="gray", alpha=0.45,
            linewidth=1.2, zorder=1, label="y = x  (ideal)")

    # --- LLM points ---
    texts = []   # collect for adjustText if available
    for _, row in others.iterrows():
        mdisplay = row["model_display"]
        strat = row["strategy"]
        ax.scatter(
            row["pass_rate"],
            row["fqs_mean"],
            color=model_colors[mdisplay],
            marker=STRATEGY_MARKERS[strat],
            s=85,
            zorder=3,
            edgecolors="white",
            linewidths=0.6,
        )
        lx = row["pass_rate"] + _LABEL_DX
        ly = row["fqs_mean"] + _LABEL_DY.get(strat, 0)
        t = ax.annotate(
            f"{mdisplay} ({strat})",
            xy=(row["pass_rate"], row["fqs_mean"]),
            xytext=(lx, ly),
            fontsize=6.5,
            alpha=0.88,
            ha="left",
            va="center",
        )
        texts.append(t)

    # --- Try adjustText for non-overlapping labels (optional dependency) ---
    try:
        from adjustText import adjust_text
        adjust_text(texts, ax=ax, arrowprops=dict(arrowstyle="-", color="gray",
                                                   lw=0.5, alpha=0.6))
    except ImportError:
        pass  # fallback: labels with fixed offsets (some overlap possible)

    # --- Axes ---
    ax.set_xlim(-0.03, 1.06)
    ax.set_ylim(-0.03, 1.06)
    ax.set_xlabel("Functional Correctness Rate (Pass@1)")
    ax.set_ylabel("Code Quality Score — Quality@1 (FQS)")
    ax.set_title(
        "Functional Correctness vs. Code Quality\nby Model and Prompting Strategy",
        pad=12,
    )
    ax.set_axisbelow(True)

    # --- Legend: strategies (marker shapes) ---
    strategy_handles = [
        mlines.Line2D(
            [], [], color="gray",
            marker=STRATEGY_MARKERS[s], linestyle="None",
            markersize=9, label=STRATEGY_LABELS[s],
        )
        for s in ["H", "C", "I"]
    ]
    # reference line
    strategy_handles.append(
        mlines.Line2D([], [], color="gray", linestyle="--",
                      linewidth=1.2, label="y = x (ideal)")
    )

    # --- Legend: model colors ---
    model_handles = [
        mpatches.Patch(color=model_colors[m], label=m)
        for m in sorted(model_colors)
    ]

    leg1 = ax.legend(
        handles=strategy_handles,
        title="Strategy",
        loc="upper left",
        framealpha=0.9,
        fontsize=9,
    )
    ax.add_artist(leg1)
    ax.legend(
        handles=model_handles,
        title="Model",
        loc="lower right",
        framealpha=0.9,
        fontsize=8,
        ncol=2,
    )

    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main():
    setup_style()
    df = load_aggregated()
    fig = make_figure(df)
    save_figure(fig, OUTPUT_NAME)
    plt.close(fig)


if __name__ == "__main__":
    main()
