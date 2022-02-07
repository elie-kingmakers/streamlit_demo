import streamlit as st
import pyspark.sql
from pyspark.dbutils import DBUtils


#***********************************************************************************************************************
#***********************************************************************************************************************
st.title('Customer Profiling')

spark = pyspark.sql.SparkSession.builder.getOrCreate()
dbutils = DBUtils(spark)

st.write(dbutils.fs.ls('dbfs:/elie'))
