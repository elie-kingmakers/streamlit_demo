from typing import Any, Dict, Optional

import pyspark.sql


class DeltaLakeReader:
    def __init__(self):
        self.sparkSession = pyspark.sql.SparkSession.builder.getOrCreate()

    def read_table(self, tableName: str) -> pyspark.sql.DataFrame:
        return self.sparkSession.table(tableName)

    def read_table_from_path(
        self, tablePath: str, readFormat: str = "delta", readOptions: Optional[Dict[str, Any]] = None
    ) -> pyspark.sql.DataFrame:
        if readOptions is None:
            readOptions = {}

        return self.sparkSession.read.format(readFormat).options(**readOptions).load(tablePath)
