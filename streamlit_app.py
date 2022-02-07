
import streamlit as st

from databricks_api import DatabricksAPI
import pyspark.sql
from pyspark.dbutils import DBUtils
import requests
import json

db = DatabricksAPI(
    host="adb-2820452106200483.3.azuredatabricks.net",
    token="dapi0f9b9050d21ecca66a72fe2b1155ad5e-2"
)
#
# spark = pyspark.sql.SparkSession.builder.getOrCreate()
# dbutils = DBUtils(spark)

#***********************************************************************************************************************
#***********************************************************************************************************************
st.title('Customer Profiling')


st.write(db.dbfs.list('dbfs:/mnt/datascience/customer_profiling/gold/customers'))




