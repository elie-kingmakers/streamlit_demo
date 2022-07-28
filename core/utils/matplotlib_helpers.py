from typing import Optional, List

import matplotlib.pyplot as plt
import textwrap


def wrap_labels(ax, width, break_long_words=False):
    labels = []
    for label in ax.get_xticklabels():
        text = label.get_text()
        labels.append(
            textwrap.fill(
                text, width=width,
                break_long_words=break_long_words
            )
        )
    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels(labels, rotation=0)


def get_empty_figure(
        xticks: bool = True,
        xticksLabels: bool = True,
        yticks: bool = True,
        yticksLabels: bool = True,
) -> plt.Figure:
    fig, ax = plt.subplots()

    if not xticks:
        ax.set_xticks([])

    if not xticksLabels:
        ax.set_xticklabels([])

    if not yticks:
        ax.set_yticks([])

    if not yticksLabels:
        ax.set_yticklabels([])

    return fig

























