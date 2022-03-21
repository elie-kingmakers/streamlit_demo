from typing import ClassVar

import pyspark.sql
from pydantic import BaseModel

from core.store.delta_lake_reader import DeltaLakeReader


class PopulationDataRetriever(BaseModel):

    populationStatsTableName: ClassVar[str] = "population_stats_09_21"

    @staticmethod
    def load_data() -> pyspark.sql.DataFrame:
        deltaLakeReader = DeltaLakeReader()
        df = deltaLakeReader.read_table(PopulationDataRetriever.populationStatsTableName)
        return df

    @staticmethod
    def load_data_pandas():  # returns DataFrameLike
        df = PopulationDataRetriever.load_data()
        return df.toPandas()
