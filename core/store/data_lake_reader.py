from typing import Any, Dict, List, Optional

import pyspark.sql

from core.datamodel.data_lake_path import DataLakePath


class DataLakeReader:
    def __init__(self, password: str, accountName: str = "bkadl"):
        self.accountName = accountName
        self.sparkSession = pyspark.sql.SparkSession.builder.getOrCreate()
        self.sparkSession.conf.set(key=f"fs.azure.account.key.{accountName}.dfs.core.windows.net", value=password)
        self.defaultReadOptions = {"header": True, "recursiveFileLookup": True}

    def read_multiple_files(
        self,
        containerName: str,
        relativeFilepaths: List[str],
        fileFormat: str,
        readOptions: Optional[Dict[str, Any]] = None,
    ) -> pyspark.sql.dataframe.DataFrame:
        if readOptions is None:
            readOptions = {}
        readOptions = {**self.defaultReadOptions, **readOptions}
        blobPath = [
            f"abfss://{containerName}@{self.accountName}.dfs.core.windows.net/{path}" for path in relativeFilepaths
        ]
        return (
            self.sparkSession.read.format(fileFormat)
            .options(**readOptions)
            .load(blobPath)
            .drop("LineageKey")
            .drop("RowVersionStamp")
        )

    def read_file(
        self, containerName: str, relativePath: str, fileFormat: str, readOptions: Optional[Dict[str, Any]] = None
    ) -> pyspark.sql.dataframe.DataFrame:
        if readOptions is None:
            readOptions = {}
        readOptions = {**self.defaultReadOptions, **readOptions}
        blobPath = f"abfss://{containerName}@{self.accountName}.dfs.core.windows.net/{relativePath}"
        return (
            self.sparkSession.read.format(fileFormat)
            .options(**readOptions)
            .load(blobPath)
            .drop("LineageKey")
            .drop("RowVersionStamp")
        )

    def read_path(
        self, dataLakePath: DataLakePath, readOptions: Optional[Dict[str, Any]] = None
    ) -> pyspark.sql.dataframe.DataFrame:
        return self.read_file(
            containerName=dataLakePath.containerName,
            relativePath=dataLakePath.relativePath,
            fileFormat=dataLakePath.fileFormat,
            readOptions=readOptions,
        )
