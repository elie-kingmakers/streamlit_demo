from typing import List

import pyspark.sql
import functools


def union_all(dfs: List[pyspark.sql.DataFrame], allowDuplicates: bool = True) -> pyspark.sql.DataFrame:
    dfResult = functools.reduce(lambda df1, df2: df1.union(df2.select(df1.columns)), dfs)

    if not allowDuplicates:
        dfResult = dfResult.dropDuplicates()

    return dfResult
