import streamlit as st

from databricks_api import DatabricksAPI

# import pyspark.sql
# from pyspark.dbutils import DBUtils

db = DatabricksAPI(
    host="adb-2820452106200483.3.azuredatabricks.net"
)

#***********************************************************************************************************************
#******************************************£*****************************************************************************
st.title('Customer Profiling')


st.write(db.dbfs.list('dbfs:/elie'))


# spark = pyspark.sql.SparkSession.builder.getOrCreate()
# dbutils = DBUtils(spark)
#
# st.write(dbutils.fs.ls('dbfs:/elie'))
