from typing import List, Tuple

import pyspark.sql
from pyspark.dbutils import DBUtils


def move_local_files_to_filestore(filesToMove: List[Tuple[str, str]]) -> None:
    for localFilePath, filestoreFolderPath in filesToMove:
        if not localFilePath.startswith("/"):
            raise ValueError(f"localFilePath: {localFilePath} should start with / (file: is being added in front)")

        if not filestoreFolderPath.startswith("dbfs:/FileStore/"):
            raise ValueError(f"filestoreSavePath: {filestoreFolderPath} should start with dbfs:/FileStore/")

        spark = pyspark.sql.SparkSession.builder.getOrCreate()
        dbutils = DBUtils(spark)

        localFilePath = "file:" + localFilePath

        dbutils.fs.mv(localFilePath, filestoreFolderPath)
        dbutils.fs.rm(localFilePath)


def get_filestore_file_url(filestoreFilePath: str) -> str:
    filestorePrefix = "dbfs:/FileStore/"

    if not filestoreFilePath.startswith(filestorePrefix):
        raise ValueError(f"filestoreFilePath: {filestoreFilePath} should start with dbfs:/FileStore/")

    filestoreFilePath = filestoreFilePath[len(filestorePrefix) :]

    databricksHostFiles = "https://adb-2820452106200483.3.azuredatabricks.net/files/"
    orgId = "?o=2820452106200483#"

    url = databricksHostFiles + filestoreFilePath + orgId
    return url


def delete_filestore_folders_content(filestoreFolderPaths: List[str]) -> None:
    for filestoreFolderPath in filestoreFolderPaths:
        if not filestoreFolderPath.startswith("dbfs:/FileStore/"):
            raise ValueError(f"filestoreFolderPath: {filestoreFolderPath} should start with dbfs:/FileStore/")

        spark = pyspark.sql.SparkSession.builder.getOrCreate()
        dbutils = DBUtils(spark)

        dbutils.fs.rm(filestoreFolderPath, True)
        dbutils.fs.mkdirs(filestoreFolderPath)
