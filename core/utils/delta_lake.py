import pyspark.sql
from pyspark.dbutils import DBUtils


def create_delta_lake_table(dataframe: pyspark.sql.DataFrame, dataPathDbfs: str, tableName: str) -> None:

    if not dataPathDbfs.startswith("dbfs:/"):
        raise ValueError(f"dataPathDbfs: {dataPathDbfs} should start with dbfs:/")

    # save dataframe to dbfs in delta format
    dataframe.write.format("delta").mode("overwrite").save(dataPathDbfs)
    # create table in delta lake
    spark = pyspark.sql.SparkSession.builder.getOrCreate()
    spark.sql("CREATE TABLE " + tableName + " USING DELTA LOCATION '" + dataPathDbfs + "'")


def delete_delta_lake_table(tableName: str, dataPathDbfs: str) -> None:

    if not dataPathDbfs.startswith("dbfs:/"):
        raise ValueError(f"dataPathDbfs: {dataPathDbfs} should start with dbfs:/")

    # delete the table
    spark = pyspark.sql.SparkSession.builder.getOrCreate()
    spark.sql("DROP TABLE " + tableName)
    # delete the saved data
    dbutils = DBUtils(spark)
    dbutils.fs.rm(dataPathDbfs, True)


def append_to_delta_lake_table(dfWithSameSchema: pyspark.sql.DataFrame, tableName: str) -> None:

    dfWithSameSchema.write.format("delta").mode("append").saveAsTable(tableName)
