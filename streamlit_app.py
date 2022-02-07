
import streamlit as st
import io
import pandas as pd
from databricks_api import DatabricksAPI
import base64

db = DatabricksAPI(
    host="adb-2820452106200483.3.azuredatabricks.net",
    token="dapi0f9b9050d21ecca66a72fe2b1155ad5e-2"
)


#***********************************************************************************************************************
#***********************************************************************************************************************
st.title('Customer Profiling')



parquetDict = db.dbfs.read("dbfs:/mnt/datascience/customer_profiling/gold/customers/part-00000-2c0cfbc6-589c-4447-b481-3093d0b163cb-c000.snappy.parquet")




parquetStringEncoded = parquetDict["data"]

parquetBytesDecoded = base64.b64decode(parquetStringEncoded)

parquetFile = io.BytesIO(parquetBytesDecoded)

df = pd.read_parquet(parquetFile)
df





