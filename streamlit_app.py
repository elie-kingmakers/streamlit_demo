
import streamlit as st

from databricks_api import DatabricksAPI
import pyspark.sql
# import requests
# import json

db = DatabricksAPI(
    host="adb-2820452106200483.3.azuredatabricks.net",
    token="dapi0f9b9050d21ecca66a72fe2b1155ad5e-2"
)

spark = pyspark.sql.SparkSession.builder.getOrCreate()

#***********************************************************************************************************************
#***********************************************************************************************************************
st.title('Customer Profiling')

df = spark.table('db_customerprofiling.customers_gold')

dfTable = df.limit(10).toPandas()

st.write(dfTable)




