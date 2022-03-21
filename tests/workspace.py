from __future__ import annotations

# import sys
# from enum import Enum
# from typing import ClassVar, Union, Dict
#
# import pyspark.sql
# import requests
# import json
# import pathlib
# import shutil
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import pyspark.sql.functions as f
#
# from pydantic import BaseModel, validator
# from pyspark.sql import SparkSession
# from pyspark.dbutils import DBUtils
# from pyspark.sql.types import (
#     FloatType,
#     StructType,
#     StructField,
#     IntegerType,
#     StringType,
#     ArrayType,
#     LongType,
#     DoubleType,
# )
# from pyspark.sql.window import Window
# from pyspark.sql import Row
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import log_loss
# from scipy.stats import distributions
# from fitter import Fitter, get_common_distributions, get_distributions
# from tqdm import tqdm
# from glom import glom, Path
# from datetime import datetime
# from databricks_api import DatabricksAPI
# import streamlit as st
# from IPython.display import display
#
# from core.store.delta_lake_reader import DeltaLakeReader
# from core.utils.delta_lake import create_delta_lake_table, append_to_delta_lake_table, delete_delta_lake_table
# from core.utils.excel import write_excel_file
# from core.utils.filestore import move_local_files_to_filestore, get_filestore_file_url


# **********************************************************************************************************************
# ******************************************* DATABRICKS-CONNECT TEST **************************************************
# **********************************************************************************************************************
# spark = SparkSession.builder.getOrCreate()
# dbutils = DBUtils(spark)
#
# print(dbutils.fs.ls('dbfs:/elie'))


# **********************************************************************************************************************
# *********************************************** ENUM INSIDE ENUM *****************************************************
# **********************************************************************************************************************
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
# ****************************************** Pydantic Static Variables *************************************************
# **********************************************************************************************************************
# class Person(BaseModel):
#     name: str = 'N/A'
#     age: int = 0
#
#     expectedAge: ClassVar[int] = 100
#
#     @staticmethod
#     def get_expected_age():
#         return Person.expectedAge
#
#
# elie = Person(name='elie', age=21)
#
# print(elie.name)
# print(elie.age)
#
# print(Person.expectedAge)
# print(Person.get_expected_age())


# **********************************************************************************************************************
# ***************************************** From Delta Lake to Local CSV ***********************************************
# **********************************************************************************************************************
# readFormat = 'delta'
# writeFormat = 'csv'
# loadPathDeltaDbfs = 'dbfs:/elie/customer_profiling/customer_data_sample'
# savePathCsvDbfs = 'dbfs:/elie/to_local/customer_data_sample'
# tableName = 'customer_data_sample'
#
# data = spark.read.format(readFormat).load(loadPathDeltaDbfs)
#
# data.coalesce(1).write.format(writeFormat).option('header', True).save(savePathCsvDbfs)
#
# files = dbutils.fs.ls(savePathCsvDbfs)
# csvFile = [x.path for x in files if x.path.endswith('.csv')][0]
# csvFileNewPath = savePathCsvDbfs.rstrip('/') + '/' + tableName + '.csv'
# dbutils.fs.mv(csvFile, csvFileNewPath)
#
# print('\'' + csvFileNewPath + '\'')
# # in terminal: dbfs cp '<csvFileNewPath>' '<local_path_to_save_file>'
# # example: dbfs cp 'dbfs:/elie/to_local/customer_data_sample/customer_data_sample.csv' '/Users/elie/Desktop'


# **********************************************************************************************************************
# ************************************************* REST API ***********************************************************
# **********************************************************************************************************************

# instance_id = 'adb-2820452106200483.3.azuredatabricks.net'
# api_version = '/api/2.0'
# api_command = '/dbfs/list'
# url = f"https://{instance_id}{api_version}{api_command}"
#
# params = {
#   'path': 'dbfs:/elie/to_local/customer_data_sample'
# }
#
# response = requests.get(url=url, params=params)
# responseString = json.loads(response.text)
# print(responseString)
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
#     params = {
#         'path': filePath
#     }
#
#     response = requests.get(url=url, params=params)
#     responseString = json.loads(response.text)
#     print(responseString)
#
# print(json.dumps(json.loads(response.text), indent = 2))


# **********************************************************************************************************************
# ******************************************** DELTA LAKE READ *********************************************************
# **********************************************************************************************************************

# people = spark.table('default.people10m')
# people = spark.read.format('delta').load('dbfs:/elie/delta_testing/customer_data')

# df = people.groupby('gender').agg(count('gender').alias('gender_count'))
# print(people.limit(100).toPandas())


# **********************************************************************************************************************
# ******************************************** SKLEARN example *********************************************************
# **********************************************************************************************************************

# x = np.random.uniform(0.0, 1.0, 20)
# result = [0, 1]
# y = np.random.choice(result, 20)
#
# # data = pd.Series(x)
# # data.hist()
# #
# # plt.show(block=True)
#
#
# yPred = np.array([0.01, 0.05, 0.90, 0.85, 0.10, 0.89, 0.03, 0.04, 0.87, 0.91, 0.07, 0.99])
# y = np.array([0.00, 0.00, 1.00, 1.00, 0.00, 1.00, 0.00, 0.00, 1.00, 1.00, 0.00, 1.00])
#
# # model = LogisticRegression(solver='lbfgs')
# # model.fit(x.reshape(-1, 1), y)
#
# # yPred = model.predict_proba(x.reshape(-1, 1))[:, 1].ravel()
# loss = log_loss(y, yPred)
#
# # print('x = {}'.format(x))
# print('y = {}'.format(y))
# print('p(y) = {}'.format(np.round(yPred, 2)))
# print('Log Loss / Cross Entropy = {:.4f}'.format(loss))


# **********************************************************************************************************************
# ******************************************* Customer Profiling *******************************************************
# **********************************************************************************************************************

# def get_fraction_to_wager_kelly_criterion(winProbability, odds):
#
#     winProbability = float(winProbability)
#     odds = float(odds)
#
#     if winProbability <= 0.0 or winProbability >= 1.0:
#         raise ValueError('invalid win probability: {}'.format(winProbability))
#
#     if odds <= 1.0:
#         raise ValueError('odds cannot be <= 1.0')
#
#     lossProbability = 1.0 - winProbability
#     fractionGainedWithWin = odds - 1.0
#
#     # from kelly criterion: f = p - (q / b)   (https://en.wikipedia.org/wiki/Kelly_criterion)
#     # f = fraction of bankroll to wager
#     # p = probability of win
#     # q = probability of loss
#     # b = fraction gained with a win
#     fractionToWager = winProbability - (lossProbability / fractionGainedWithWin)
#     return fractionToWager
#
#
# def get_probability_estimate_kelly_criterion(amountWagered, totalBankroll, odds):
#
#     amountWagered = float(amountWagered)
#     totalBankroll = float(totalBankroll)
#     odds = float(odds)
#
#     if amountWagered == 0.0:
#         raise ValueError('amount wagered cannot be 0')
#
#     if totalBankroll == 0.0:
#         raise ValueError('total bankroll cannot be 0')
#
#     if odds <= 1.0:
#         raise ValueError('odds cannot be <= 1.0')
#
#     fractionWagered = amountWagered / totalBankroll
#     fractionGainedWithWin = odds - 1.0
#
#     # from Kelly Criterion: p = ((f * b) + 1) / (b + 1)
#     probabilityEstimate = ((fractionWagered * fractionGainedWithWin) + 1.0) / (fractionGainedWithWin + 1.0)
#     return probabilityEstimate
#
#
# def get_customer_score_per_selection(probability, outcome, stake):
#     customerScore = (float(outcome) - float(probability)) * stake
#     return customerScore
#
#
# # logLoss = log_loss(eventsOutcomes, probabilityEstimates)
#
# udf_get_probability_estimate_kelly_criterion = f.udf(get_probability_estimate_kelly_criterion, FloatType())
# udf_get_customer_score_per_selection = f.udf(get_customer_score_per_selection, FloatType())
#
#
#
# deltaLakeReader = DeltaLakeReader()
# tablePath = 'dbfs:/elie/customer_profiling/selection_data_sample'
# dfSelections = deltaLakeReader.read_table_from_path(tablePath=tablePath)
#
# # dfSelections = dfSelections.filter(dfSelections['UserId'] == '1981255')
#
# dfSelections = dfSelections\
#     .filter((dfSelections['ForcedStatus'] == 0.0) | (dfSelections['ForcedStatus'] == 1.0))\
#     .filter(dfSelections['OddValue'] > 1.0)
#
# totalBankRollPopulation = dfSelections.agg(f.sum('StakePerSelection').alias('TotalStake')).collect()[0]['TotalStake']
#
# dfSelections = dfSelections.withColumn(
#     'ProbabilityEstimateKellyCriterion',
#     udf_get_probability_estimate_kelly_criterion(
#         dfSelections['StakePerSelection'],
#         f.lit(totalBankRollPopulation),
#         dfSelections['OddValue']
#     )
# )
#
# dfSelections = dfSelections.withColumn(
#     'BetScore',
#     udf_get_customer_score_per_selection(
#         dfSelections['ProbabilityEstimateKellyCriterion'],
#         dfSelections['ForcedStatus'],
#         dfSelections['StakePerSelection']
#     )
# )
#
# # dfSelections.show()
#
# # bins, counts = dfSelections.select('BetScore').rdd.flatMap(lambda x: x).histogram(200)
# # plt.hist(bins[:-1], bins=bins, weights=counts)
# #
# # plt.xlabel('Bet Score')
# # plt.ylabel('Frequency')
# # plt.yscale('log')
# #
# #
# # plt.show(block='true')
#
#
# truePositivesPopulation = dfSelections.filter(dfSelections['ForcedStatus'] == 1.0).count()
# falsePositivesPopulation = dfSelections.filter(dfSelections['ForcedStatus'] == 0.0).count()
#
# accuracyPopulation = truePositivesPopulation / (truePositivesPopulation + falsePositivesPopulation)
#
# averageBetScorePopulation = dfSelections\
#     .agg(f.avg(dfSelections['BetScore']).alias('AverageBetScore'))\
#     .collect()[0]['AverageBetScore']
#
# print('')
# print('Total Bankroll Population = {}'.format(totalBankRollPopulation))
# print('True Positives Population = {}'.format(truePositivesPopulation))
# print('False Positives Population = {}'.format(falsePositivesPopulation))
# print('Accuracy Population = {}'.format(accuracyPopulation))
# print('Average Bet Score Population = {}'.format(averageBetScorePopulation))


# userId = '1981255'      # 1574497, 1578724, 1583858, 1981255, 1982164, 1982226
# dfSelectionsCustomer = dfSelections.filter(dfSelections['UserId'] == userId)
#
# totalBankRollCustomer = dfSelectionsCustomer.agg(f.sum('StakePerSelection').alias('TotalStake')).collect()[0]['TotalStake']
#
# dfSelectionsCustomer = dfSelectionsCustomer.withColumn(
#     'ProbabilityEstimateKellyCriterion',
#     udf_get_probability_estimate_kelly_criterion(
#         dfSelectionsCustomer['StakePerSelection'],
#         f.lit(totalBankRollCustomer),
#         dfSelectionsCustomer['OddValue']
#     )
# )
#
# dfSelectionsCustomer = dfSelectionsCustomer.withColumn(
#     'BetScore',
#     udf_get_customer_score_per_selection(
#         dfSelectionsCustomer['ProbabilityEstimateKellyCriterion'],
#         dfSelectionsCustomer['ForcedStatus'],
#         dfSelectionsCustomer['StakePerSelection']
#     )
# )
#
# dfSelectionsCustomer.show()
#
#
# # bins, counts = dfSelectionsCustomer.select('BetScore').rdd.flatMap(lambda x: x).histogram(50)
# # plt.hist(bins[:-1], bins=bins, weights=counts)
# #
# # plt.xlabel('Bet Score')
# # plt.ylabel('Frequency')
# #
# # plt.show(block='true')
# #
# # betsScores = np.array(dfSelectionsCustomer.select('BetScore').collect()).ravel()
# #
# # f = Fitter(betsScores)
# # f.fit()
# #
# # print(f.summary())
# # plt.show(block='true')
# #
# # # print(f.get_best(method='sumsquare_error'))
#
#
# truePositivesCustomer = dfSelectionsCustomer.filter(dfSelectionsCustomer['ForcedStatus'] == 1.0).count()
# falsePositivesCustomer = dfSelectionsCustomer.filter(dfSelectionsCustomer['ForcedStatus'] == 0.0).count()
#
# accuracyCustomer = truePositivesCustomer / (truePositivesCustomer + falsePositivesCustomer)
#
# averageBetScoreCustomer = dfSelectionsCustomer\
#     .agg(f.avg(dfSelectionsCustomer['BetScore']).alias('AverageBetScore'))\
#     .collect()[0]['AverageBetScore']
#
# print('')
# print('Total Bankroll Customer = {}'.format(totalBankRollCustomer))
# print('True Positives Customer = {}'.format(truePositivesCustomer))
# print('False Positives Customer = {}'.format(falsePositivesCustomer))
# print('Accuracy Customer = {}'.format(accuracyCustomer))
# print('Average Bet Score Customer = {}'.format(averageBetScoreCustomer))
#
#
#
# CDF_1 = 'cdf_1'
# CDF_2 = 'cdf_2'
# FILLED_CDF_1 = 'filled_cdf_1'
# FILLED_CDF_2 = 'filled_cdf_2'
#
#
# def get_cdf(df, variable, col_name):
#
#     cdf = df.select(variable).na.drop().\
#         withColumn(
#             col_name,
#             f.cume_dist().over(Window.orderBy(variable))
#         ).distinct()
#
#     return cdf
#
#
# def ks_2samp(df1, var1, df2, var2):
#
#     ksStat = get_cdf(df1, var1, CDF_1).\
#         join(
#             get_cdf(df2, var2, CDF_2),
#             on=df1[var1] == df2[var2],
#             how='outer'
#         ).\
#         withColumn(
#             FILLED_CDF_1,
#             f.last(f.col(CDF_1), ignorenulls=True).
#             over(Window.rowsBetween(Window.unboundedPreceding, Window.currentRow))
#         ).\
#         withColumn(
#             FILLED_CDF_2,
#             f.last(f.col(CDF_2), ignorenulls=True).
#             over(Window.rowsBetween(Window.unboundedPreceding, Window.currentRow))
#         ).\
#         select(
#             f.max(
#                 f.abs(
#                     f.col(FILLED_CDF_1) - f.col(FILLED_CDF_2)
#                 )
#             )
#         ).\
#         collect()[0][0]
#
#     # Adapted from scipy.stats ks_2samp
#     n1 = df1.select(var1).na.drop().count()
#     n2 = df2.select(var2).na.drop().count()
#     en = np.sqrt(n1 * n2 / float(n1 + n2))
#     try:
#         pValue = distributions.kstwobign.sf((en + 0.12 + 0.11 / en) * ksStat)
#     except:
#         pValue = 1.0
#
#     return ksStat, pValue
#
#
# # ksStat, pValue = ks_2samp(dfSelections, 'BetScore', dfSelectionsCustomer, 'BetScore')
# # print('KS Stat - BetScore - CustomervPopulation = {}'.format(ksStat))
# # print('P-Value - BetScore - CustomervPopulation = {}'.format(pValue))


# **********************************************************************************************************************
# **************************************** Save Image to FileStore *****************************************************
# **********************************************************************************************************************

# localFilePath = '/Users/elie/repos/data_science/customer_profiling/tests/test.png'
# filestoreFilePath = 'dbfs:/FileStore/elie/customer_profiling/figures/test.png'
#
# x = np.linspace(0, 10)
# y = np.exp(x)
# fig = plt.figure(1)
# plt.subplot(2, 2, 1)
# plt.plot(x, y)
# plt.subplot(2, 2, 2)
# plt.plot(x, 2*y)
# plt.subplot(2, 2, 3)
# plt.plot(x,x)
# plt.subplot(2, 2, 4)
# plt.plot(x, 2*x)
# plt.savefig(localFilePath, bbox_inches='tight')
#
# move_local_files_to_filestore(
#     filesToMove=[
#         (localFilePath, filestoreFilePath)
#     ]
# )
#
# print(get_filestore_file_url(filestoreFilePath=filestoreFilePath))

# **********************************************************************************************************************
# **********************************************************************************************************************
# **********************************************************************************************************************

# birthDateKeyUTC = 19891108
#
# dateUser = datetime.strptime(str(birthDateKeyUTC), '%Y%m%d')
# today = datetime.today()
# ageUser = int((today - dateUser).days / 365.242199)
#
# print(dateUser)
# print(today)
# print(ageUser)

# **********************************************************************************************************************
# **********************************************************************************************************************
# **********************************************************************************************************************
