import streamlit as st

from databricks_api import DatabricksAPI

# import pyspark.sql
# from pyspark.dbutils import DBUtils

db = DatabricksAPI(
    host="adb-2820452106200483.3.azuredatabricks.net",
    token="dapi0f9b9050d21ecca66a72fe2b1155ad5e-2"
)

#***********************************************************************************************************************
#***********************************************************************************************************************
st.title('Customer Profiling')


st.write(db.dbfs.list('dbfs:/eliedatabricks-api'))


# spark = pyspark.sql.SparkSession.builder.getOrCreate()
# dbutils = DBUtils(spark)
#
# st.write(dbutils.fs.ls('dbfs:/elie'))
