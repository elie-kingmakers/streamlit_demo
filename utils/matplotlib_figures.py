import pandas as pd
import matplotlib.pyplot as plt

from core.utils.matplotlib_helpers import wrap_labels

def get_sports_stats_histogram(
        x: pd.DataFrame,
        y: pd.DataFrame,
        xLabelSize: int = 10,
        barsAnnotations: bool = False,
        barsAnnotationsHeightInc: float = 0.0,
        wrapLabels: bool = False
) -> plt.Figure:
    plt.rc('xtick', labelsize=xLabelSize)

    fig, ax = plt.subplots()

    bars = ax.bar(
        x=x,
        height=y
    )

    if barsAnnotations:
        bar_color = bars[0].get_facecolor()
        for bar in bars:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + barsAnnotationsHeightInc,
                round(bar.get_height(), 2),
                horizontalalignment='center',
                color=bar_color,
                weight='bold'
            )

    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels(x.tolist())

    if wrapLabels:
        wrap_labels(ax, 5)

    fig.tight_layout()

    return fig


def get_tournaments_stats_histogram(
        x: pd.DataFrame,
        y: pd.DataFrame,
        xLabelSize: int = 10,
        barsAnnotations: bool = False,
        barsAnnotationsHeightInc: float = 0.0,
        wrapLabels: bool = False
) -> plt.Figure:
    plt.rc('xtick', labelsize=xLabelSize)

    fig, ax = plt.subplots()

    bars = ax.bar(
        x=x,
        height=y
    )

    if barsAnnotations:
        bar_color = bars[0].get_facecolor()
        for bar in bars:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + barsAnnotationsHeightInc,
                round(bar.get_height(), 2),
                horizontalalignment='center',
                color=bar_color,
                weight='bold'
            )

    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels(x.tolist())

    if wrapLabels:
        wrap_labels(ax, 5)

    fig.tight_layout()

    return fig


def get_markets_stats_histogram(
        x: pd.DataFrame,
        y: pd.DataFrame,
        xLabelSize: int = 10,
        barsAnnotations: bool = False,
        barsAnnotationsHeightInc: float = 0.0
) -> plt.Figure:
    plt.rc('xtick', labelsize=xLabelSize)

    fig, ax = plt.subplots()

    bars = ax.bar(
        x=x,
        height=y
    )

    if barsAnnotations:
        bar_color = bars[0].get_facecolor()
        for bar in bars:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + barsAnnotationsHeightInc,
                round(bar.get_height(), 2),
                horizontalalignment='center',
                color=bar_color,
                weight='bold'
            )

    plt.xticks(rotation=90)

    # fig.tight_layout()

    return fig