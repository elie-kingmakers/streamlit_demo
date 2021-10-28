from __future__ import annotations
import numpy as np
import requests
import json
import numpy
import pandas as pd

from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils
from pyspark.sql.functions import udf, col, explode
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, ArrayType
from pyspark.sql import Row
from enum import Enum

# class Path(Enum):
#     def __getattr__(self, item):
#         if item != '_value_':
#             return getattr(self.value, item).value
#         raise AttributeError
#
#     class Raptor(Enum):
#         COUPONS = "raptor_coupons"
#         USERS = "raptor_users"
#
#     class Tps(Enum):
#         COUPONS = "tps_coupons"
#         USERS = "tps_users"
#
#
# print(Path.Raptor.COUPONS)
# print(Path.Tps.COUPONS)


# **********************************************************************************************************************
# ******************************************* DATABRICKS-CONNECT TEST **************************************************
# **********************************************************************************************************************
spark = SparkSession.builder.getOrCreate()
dbutils = DBUtils(spark)

# print(dbutils.fs.ls("dbfs:/elie"))


# **********************************************************************************************************************
# ******************************************** From Delta Lake to CSV **************************************************
# **********************************************************************************************************************
readFormat = 'delta'
writeFormat = 'csv'
loadPathDeltaDbfs = 'dbfs:/elie/customer_profiling/customer_data_sample'
savePathCsvDbfs = 'dbfs:/elie/to_local/customer_data_sample'
tableName = 'customer_data_sample'

data = spark.read.format(readFormat).load(loadPathDeltaDbfs)

data.coalesce(1).write.format(writeFormat).option('header', True).save(savePathCsvDbfs)

files = dbutils.fs.ls(savePathCsvDbfs)
csvFile = [x.path for x in files if x.path.endswith('.csv')][0]
csvFileNewPath = savePathCsvDbfs.rstrip('/') + '/' + tableName + '.csv'
dbutils.fs.mv(csvFile, csvFileNewPath)

print('\'' + csvFileNewPath + '\'')
# in terminal: dbfs cp '<csvFileNewPath>' '<local_path_to_save_file>'
# example: dbfs cp 'dbfs:/elie/to_local/customer_data_sample/customer_data_sample.csv' '/Users/elie/Desktop'


# **********************************************************************************************************************
# ************************************************* REST API ***********************************************************
# **********************************************************************************************************************

# instance_id = 'adb-2820452106200483.3.azuredatabricks.net'
# api_version = '/api/2.0'
# api_command = '/dbfs/list'
# url = f"https://{instance_id}{api_version}{api_command}"
#
# params = {
#   'path': 'dbfs:/elie/delta_testing/customer_data'
# }
#
# response = requests.get(url=url, params=params)
# responseString = json.loads(response.text)
#
# filesPaths = []
# for file in responseString['files']:
#     filePath = file['path']
#     filesPaths.append(filePath)
#
# for filePath in filesPaths:
#     instance_id = 'adb-2820452106200483.3.azuredatabricks.net'
#     api_version = '/api/2.0'
#     api_command = '/dbfs/read'
#     url = f"https://{instance_id}{api_version}{api_command}"
#
#     filePath = f'dbfs:{filePath}'
#
#     params = {'path': filePath}
#
#     response = requests.get(url=url, params=params)
#     responseString = json.loads(response.text)
#     print(responseString)

# print(json.dumps(json.loads(response.text), indent = 2))

# **********************************************************************************************************************
# ******************************************** DELTA LAKE READ *********************************************************
# **********************************************************************************************************************

# people = spark.table('default.people10m')
# people = spark.read.format('delta').load('dbfs:/elie/delta_testing/customer_data')

# df = people.groupby('gender').agg(count('gender').alias('gender_count'))
# print(people.limit(100).toPandas())























