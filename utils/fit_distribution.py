import numpy as np
import pyspark.sql

from fitter import Fitter


def fit_distribution(df: pyspark.sql.DataFrame, columnName: str) -> None:
    data = np.array(df.select(columnName).collect()).ravel()

    f = Fitter(data)
    f.fit()

    print(f.summary())

    # plt.show(block='true')
