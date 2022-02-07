
import streamlit as st
# import io
# import pandas as pd

from databricks_api import DatabricksAPI

db = DatabricksAPI(
    host="adb-2820452106200483.3.azuredatabricks.net",
    token="dapi0f9b9050d21ecca66a72fe2b1155ad5e-2"
)


#***********************************************************************************************************************
#***********************************************************************************************************************
st.title('Customer Profiling')

pq_bytes = db.dbfs.read('dbfs:/mnt/datascience/customer_profiling/gold/customers')

st.write(pq_bytes)
# pq_file = io.BytesIO(pq_bytes)
# df = pd.read_parquet(pq_file)




