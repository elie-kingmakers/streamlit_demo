from typing import Optional, List

import matplotlib.pyplot as plt
import pyspark.sql


def get_histogram(
    df: pyspark.sql.DataFrame,
    columnName: str,
    xLabel: str = "",
    yLabel: str = "",
    binsNum: int = 100,
    xScale: str = "linear",
    yScale: str = "linear",
    xTicks: Optional[List[float]] = None,
) -> plt.Figure:
    fig, ax = plt.subplots()

    bins, counts = df.select(columnName).rdd.flatMap(lambda x: x).histogram(binsNum)
    ax.hist(bins[:-1], bins=bins, weights=counts)

    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_xscale(xScale)
    ax.set_yscale(yScale)

    if xTicks is not None:
        ax.set_xticks(xTicks)

    return fig
