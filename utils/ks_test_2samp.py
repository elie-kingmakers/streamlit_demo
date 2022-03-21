import numpy as np
import pyspark.sql.functions as f

from pyspark.sql.window import Window
from scipy.stats import distributions

CDF_1 = "cdf_1"
CDF_2 = "cdf_2"
FILLED_CDF_1 = "filled_cdf_1"
FILLED_CDF_2 = "filled_cdf_2"


def get_cdf(df, variable, col_name):

    cdf = df.select(variable).na.drop().withColumn(col_name, f.cume_dist().over(Window.orderBy(variable))).distinct()

    return cdf


def ks_test_2samp(df1, var1, df2, var2):

    ksStat = (
        get_cdf(df1, var1, CDF_1)
        .join(get_cdf(df2, var2, CDF_2), on=df1[var1] == df2[var2], how="outer")
        .withColumn(
            FILLED_CDF_1,
            f.last(f.col(CDF_1), ignorenulls=True).over(
                Window.rowsBetween(Window.unboundedPreceding, Window.currentRow)
            ),
        )
        .withColumn(
            FILLED_CDF_2,
            f.last(f.col(CDF_2), ignorenulls=True).over(
                Window.rowsBetween(Window.unboundedPreceding, Window.currentRow)
            ),
        )
        .select(f.max(f.abs(f.col(FILLED_CDF_1) - f.col(FILLED_CDF_2))))
        .collect()[0][0]
    )

    # Adapted from scipy.stats ks_2samp
    n1 = df1.select(var1).na.drop().count()
    n2 = df2.select(var2).na.drop().count()
    en = np.sqrt(n1 * n2 / float(n1 + n2))
    try:
        pValue = distributions.kstwobign.sf((en + 0.12 + 0.11 / en) * ksStat)
    except Exception:
        pValue = 1.0

    return ksStat, pValue
