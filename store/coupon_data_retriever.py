# from typing import ClassVar
#
# import pyspark.sql
# from pydantic import BaseModel
#
# from core.store.delta_lake_reader import DeltaLakeReader
# from datamodel.columns import Columns
#
# class CouponDataRetriever(BaseModel):
#
#     couponFinalTableName: ClassVar[str] = 'coupon_final_09_21'
#     couponSampleTableName: ClassVar[str] = 'coupon_sample_09_21'
#
#     @staticmethod
#     def load_data() -> pyspark.sql.DataFrame:
#         deltaLakeReader = DeltaLakeReader()
#         df = deltaLakeReader.read_table(CouponDataRetriever.couponFinalTableName)
#         return df
#
#     @staticmethod
#     def load_data_sample(): # returns DataFrameLike
#         deltaLakeReader = DeltaLakeReader()
#         df = deltaLakeReader.read_table(CouponDataRetriever.couponSampleTableName)
#         return df.toPandas()
#
#     @staticmethod
#     def get_user_data(dfCoupons: pyspark.sql.DataFrame, userId: str) -> pyspark.sql.DataFrame:
#         dfUser = dfCoupons.filter(dfCoupons[Columns.CouponData.USER_ID] == userId)
#         return dfUser
