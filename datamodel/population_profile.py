# import pyspark.sql
# import pyspark.sql.functions as f
# from pydantic import BaseModel
#
# from datamodel.columns import Columns
#
# class PopulationProfile(BaseModel):
#     totalNumberOfUsers: int = 0
#     totalNumberOfCoupons: float = 0.0
#     averageNumberOfSelectionsPerCoupon: float = 0.0
#     averageOddValuePerSelection: float = 0.0
#     averageCouponStake: float = 0.0
#     averageCouponReturn: float = 0.0
#     highestCouponStake: float = 0.0
#     highestCouponReturn: float = 0.0
#     totalStake: float = 0.0
#     totalReturn: float = 0.0
#     totalNetEarnings: float = 0.0
#     averageReturnOnStakePercentage: float = 0.0
#     averageTruePositives: float = 0.0
#     averageFalsePositives: float = 0.0
#     averageAccuracy: float = 0.0
#     averageProbabilityEstimateKellyCriterion = 0.0
#     averageBetScore: float = 0.0
#
#     @classmethod
#     def from_data(cls, dfPopulation: pyspark.sql.DataFrame):
#         populationProfile = cls()
#
#         populationProfile.totalNumberOfUsers = dfPopulation.collect()[0][Columns.PopulationData.TOTAL_NUMBER_OF_USERS]
#         populationProfile.totalNumberOfCoupons = dfPopulation.collect()[0][Columns.PopulationData.TOTAL_NUMBER_OF_COUPONS]
#         populationProfile.averageNumberOfSelectionsPerCoupon = dfPopulation.collect()[0][Columns.PopulationData.AVERAGE_NUMBER_OF_SELECTIONS_PER_COUPON]
#         populationProfile.averageOddValuePerSelection = dfPopulation.collect()[0][Columns.PopulationData.AVERAGE_ODD_VALUE_PER_SELECTION]
#         populationProfile.averageCouponStake = dfPopulation.collect()[0][Columns.PopulationData.AVERAGE_COUPON_STAKE]
#         populationProfile.averageCouponReturn = dfPopulation.collect()[0][Columns.PopulationData.AVERAGE_COUPON_RETURN]
#         populationProfile.highestCouponStake = dfPopulation.collect()[0][Columns.PopulationData.HIGHEST_COUPON_STAKE]
#         populationProfile.highestCouponReturn = dfPopulation.collect()[0][Columns.PopulationData.HIGHEST_COUPON_RETURN]
#         populationProfile.totalStake = dfPopulation.collect()[0][Columns.PopulationData.TOTAL_STAKE]
#         populationProfile.totalReturn = dfPopulation.collect()[0][Columns.PopulationData.TOTAL_RETURN]
#         populationProfile.totalNetEarnings = dfPopulation.collect()[0][Columns.PopulationData.TOTAL_NET_EARNINGS]
#         populationProfile.averageReturnOnStakePercentage = dfPopulation.collect()[0][Columns.PopulationData.AVERAGE_RETURN_ON_STAKE_PERCENTAGE]
#         populationProfile.averageTruePositives = dfPopulation.collect()[0][Columns.PopulationData.AVERAGE_TRUE_POSITIVES]
#         populationProfile.averageFalsePositives = dfPopulation.collect()[0][Columns.PopulationData.AVERAGE_FALSE_POSITIVES]
#         populationProfile.averageAccuracy = dfPopulation.collect()[0][Columns.PopulationData.AVERAGE_ACCURACY]
#         populationProfile.averageProbabilityEstimateKellyCriterion = dfPopulation.collect()[0][Columns.PopulationData.AVERAGE_PROBABILITY_ESTIMATE_KELLY_CRITERION]
#         populationProfile.averageBetScore = dfPopulation.collect()[0][Columns.PopulationData.AVERAGE_BET_SCORE]
#
#         return populationProfile
#
#
#
#
#
#
#
#
#
#
