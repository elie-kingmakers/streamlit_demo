import pandas as pd
from pydantic import BaseModel
from datetime import datetime

from datamodel.columns import Columns


class CustomerProfile(BaseModel):
    userId: int = 0
    clientIP: str = ""

    platformUserId: int = 0
    userTypeId: int = 0
    userTypeName: str = ""
    userStatusId: int = 0
    userStatusName: str = ""
    firstName: str = ""
    lastName: str = ""
    username: str = ""
    email: str = ""
    gender: str = ""
    birthDateKeyUTC: int = 0
    userCurrencyId: int = 0
    userCurrencyName: str = ""
    subscriptionDateKeyUTC: int = 0
    verificationLevelId: int = 0
    verificationLevelName: str = ""
    streetAddress: str = ""
    town: str = ""
    zipCode: str = ""
    countryId: int = 0
    countryName: str = ""
    phone: str = ""
    mobilePhone: str = ""

    availableBalanceTotal: float = 0.0

    averageSelectionOddsPrematch: float = 0.0
    averageSelectionOddsLive: float = 0.0
    averageSelectionOdds: float = 0.0
    averageCouponOddsPrematch: float = 0.0
    averageCouponOddsLive: float = 0.0
    averageCouponOdds: float = 0.0
    averageSelectionStakePrematch: float = 0.0
    averageSelectionStakeLive: float = 0.0
    averageSelectionStake: float = 0.0
    averageSelectionReturnPrematch: float = 0.0
    averageSelectionReturnLive: float = 0.0
    averageSelectionReturn: float = 0.0
    averageProbabilityEstimateKellyCriterion: float = 0.0
    averageBetScore: float = 0.0
    truePositivesPrematch: int = 0
    truePositivesLive: int = 0
    truePositives: int = 0
    falsePositivesPrematch: int = 0
    falsePositivesLive: int = 0
    falsePositives: int = 0

    totalNumberOfCoupons: int = 0
    totalNumberOfSelectionsPrematch: int = 0
    totalNumberOfSelectionsLive: int = 0
    totalNumberOfSelections: int = 0
    averageCouponNumberOfSelectionsPrematch: float = 0.0
    averageCouponNumberOfSelectionsLive: float = 0.0
    averageCouponNumberOfSelections: float = 0.0
    averageCouponPotentialPayoutPrematch: float = 0.0
    averageCouponPotentialPayoutLive: float = 0.0
    averageCouponPotentialPayout: float = 0.0
    averageCouponStakePrematch: float = 0.0
    averageCouponStakeLive: float = 0.0
    averageCouponStake: float = 0.0
    averageCouponReturnPrematch: float = 0.0
    averageCouponReturnLive: float = 0.0
    averageCouponReturn: float = 0.0
    highestCouponStake: float = 0.0
    highestCouponReturn: float = 0.0
    totalStakePrematch: float = 0.0
    totalStakeLive: float = 0.0
    totalStake: float = 0.0
    totalReturnPrematch: float = 0.0
    totalReturnLive: float = 0.0
    totalReturn: float = 0.0
    mostRecentCouponDateKeyUTC: int = 0

    netEarningsPrematch: float = 0.0
    netEarningsLive: float = 0.0
    netEarnings: float = 0.0
    returnOnStakePercentagePrematch: float = 0.0
    returnOnStakePercentageLive: float = 0.0
    returnOnStakePercentage: float = 0.0
    marginPrematch: float = 0.0
    marginLive: float = 0.0
    margin: float = 0.0
    winningStatusPrematch: int = 0
    winningStatusLive: int = 0
    winningStatus: int = 0
    accuracyPrematch: float = 0.0
    accuracyLive: float = 0.0
    accuracy: float = 0.0

    clusterAverageCouponStake: str = ""
    clusterAccuracy: str = ""
    clusterNumberOfCoupons: str = ""
    clusterNetEarnings: str = ""
    clusterMostRecentCouponDate: str = ""

    @property
    def age(self) -> int:
        birthDate = datetime.strptime(str(self.birthDateKeyUTC), "%Y%m%d")
        today = datetime.today()
        return int((today - birthDate).days / 365.242199)

    @classmethod
    def from_data(cls, dfCustomer: pd.DataFrame):
        customerProfile = cls()

        customerProfile.userId = int(dfCustomer.iloc[0][Columns.CustomerData.USER_ID])
        customerProfile.clientIP = str(dfCustomer.iloc[0][Columns.CustomerData.CLIENT_IP])

        customerProfile.platformUserId = int(dfCustomer.iloc[0][Columns.CustomerData.PLATFORM_USER_ID])
        customerProfile.userTypeId = int(dfCustomer.iloc[0][Columns.CustomerData.USER_TYPE_ID])
        customerProfile.userTypeName = str(dfCustomer.iloc[0][Columns.CustomerData.USER_TYPE_NAME])
        customerProfile.userStatusId = int(dfCustomer.iloc[0][Columns.CustomerData.USER_STATUS_ID])
        customerProfile.userStatusName = str(dfCustomer.iloc[0][Columns.CustomerData.USER_STATUS_NAME])
        customerProfile.firstName = str(dfCustomer.iloc[0][Columns.CustomerData.FIRST_NAME])
        customerProfile.lastName = str(dfCustomer.iloc[0][Columns.CustomerData.LAST_NAME])
        customerProfile.username = str(dfCustomer.iloc[0][Columns.CustomerData.USERNAME])
        customerProfile.email = str(dfCustomer.iloc[0][Columns.CustomerData.EMAIL])
        customerProfile.gender = str(dfCustomer.iloc[0][Columns.CustomerData.GENDER])
        customerProfile.birthDateKeyUTC = int(dfCustomer.iloc[0][Columns.CustomerData.BIRTH_DATE_KEY_UTC])
        customerProfile.userCurrencyId = int(dfCustomer.iloc[0][Columns.CustomerData.USER_CURRENCY_ID])
        customerProfile.userCurrencyName = str(dfCustomer.iloc[0][Columns.CustomerData.USER_CURRENCY_NAME])
        customerProfile.subscriptionDateKeyUTC = int(dfCustomer.iloc[0][Columns.CustomerData.SUBSCRIPTION_DATE_KEY_UTC])
        customerProfile.verificationLevelId = int(dfCustomer.iloc[0][Columns.CustomerData.VERIFICATION_LEVEL_ID])
        customerProfile.verificationLevelName = str(dfCustomer.iloc[0][Columns.CustomerData.VERIFICATION_LEVEL_NAME])
        customerProfile.streetAddress = str(dfCustomer.iloc[0][Columns.CustomerData.STREET_ADDRESS])
        customerProfile.town = str(dfCustomer.iloc[0][Columns.CustomerData.TOWN])
        customerProfile.zipCode = str(dfCustomer.iloc[0][Columns.CustomerData.ZIP_CODE])
        customerProfile.countryId = int(dfCustomer.iloc[0][Columns.CustomerData.COUNTRY_ID])
        customerProfile.countryName = str(dfCustomer.iloc[0][Columns.CustomerData.COUNTRY_NAME])
        customerProfile.phone = str(dfCustomer.iloc[0][Columns.CustomerData.PHONE])
        customerProfile.mobilePhone = str(dfCustomer.iloc[0][Columns.CustomerData.MOBILE_PHONE])

        customerProfile.availableBalanceTotal = float(dfCustomer.iloc[0][Columns.CustomerData.AVAILABLE_BALANCE_TOTAL])

        customerProfile.averageSelectionOddsPrematch = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_ODDS_PREMATCH]
        )
        customerProfile.averageSelectionOddsLive = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_ODDS_LIVE]
        )
        customerProfile.averageSelectionOdds = float(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_ODDS])
        customerProfile.averageCouponOddsPrematch = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_ODDS_PREMATCH]
        )
        customerProfile.averageCouponOddsLive = float(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_ODDS_LIVE])
        customerProfile.averageCouponOdds = float(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_ODDS])
        customerProfile.averageSelectionStakePrematch = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_STAKE_PREMATCH]
        )
        customerProfile.averageSelectionStakeLive = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_STAKE_LIVE]
        )
        customerProfile.averageSelectionStake = float(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_STAKE])
        customerProfile.averageSelectionReturnPrematch = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_RETURN_PREMATCH]
        )
        customerProfile.averageSelectionReturnLive = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_RETURN_LIVE]
        )
        customerProfile.averageSelectionReturn = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_RETURN]
        )
        customerProfile.averageProbabilityEstimateKellyCriterion = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_PROBABILITY_ESTIMATE_KELLY_CRITERION]
        )
        customerProfile.averageBetScore = float(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_BET_SCORE])
        customerProfile.truePositivesPrematch = int(dfCustomer.iloc[0][Columns.CustomerData.TRUE_POSITIVES_PREMATCH])
        customerProfile.truePositivesLive = int(dfCustomer.iloc[0][Columns.CustomerData.TRUE_POSITIVES_LIVE])
        customerProfile.truePositives = int(dfCustomer.iloc[0][Columns.CustomerData.TRUE_POSITIVES])
        customerProfile.falsePositivesPrematch = int(dfCustomer.iloc[0][Columns.CustomerData.FALSE_POSITIVES_PREMATCH])
        customerProfile.falsePositivesLive = int(dfCustomer.iloc[0][Columns.CustomerData.FALSE_POSITIVES_LIVE])
        customerProfile.falsePositives = int(dfCustomer.iloc[0][Columns.CustomerData.FALSE_POSITIVES])

        customerProfile.totalNumberOfCoupons = int(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_NUMBER_OF_COUPONS])
        customerProfile.totalNumberOfSelectionsPrematch = int(
            dfCustomer.iloc[0][Columns.CustomerData.TOTAL_NUMBER_OF_SELECTIONS_PREMATCH]
        )
        customerProfile.totalNumberOfSelectionsLive = int(
            dfCustomer.iloc[0][Columns.CustomerData.TOTAL_NUMBER_OF_SELECTIONS_LIVE]
        )
        customerProfile.totalNumberOfSelections = int(
            dfCustomer.iloc[0][Columns.CustomerData.TOTAL_NUMBER_OF_SELECTIONS]
        )
        customerProfile.averageCouponNumberOfSelectionsPrematch = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_NUMBER_OF_SELECTIONS_PREMATCH]
        )
        customerProfile.averageCouponNumberOfSelectionsLive = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_NUMBER_OF_SELECTIONS_LIVE]
        )
        customerProfile.averageCouponNumberOfSelections = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_NUMBER_OF_SELECTIONS]
        )
        customerProfile.averageCouponPotentialPayoutPrematch = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_POTENTIAL_PAYOUT_PREMATCH]
        )
        customerProfile.averageCouponPotentialPayoutLive = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_POTENTIAL_PAYOUT_LIVE]
        )
        customerProfile.averageCouponPotentialPayout = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_POTENTIAL_PAYOUT]
        )
        customerProfile.averageCouponStakePrematch = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_STAKE_PREMATCH]
        )
        customerProfile.averageCouponStakeLive = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_STAKE_LIVE]
        )
        customerProfile.averageCouponStake = float(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_STAKE])
        customerProfile.averageCouponReturnPrematch = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_RETURN_PREMATCH]
        )
        customerProfile.averageCouponReturnLive = float(
            dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_RETURN_LIVE]
        )
        customerProfile.averageCouponReturn = float(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_RETURN])
        customerProfile.highestCouponStake = float(dfCustomer.iloc[0][Columns.CustomerData.HIGHEST_COUPON_STAKE])
        customerProfile.highestCouponReturn = float(dfCustomer.iloc[0][Columns.CustomerData.HIGHEST_COUPON_RETURN])
        customerProfile.totalStakePrematch = float(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_STAKE_PREMATCH])
        customerProfile.totalStakeLive = float(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_STAKE_LIVE])
        customerProfile.totalStake = float(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_STAKE])
        customerProfile.totalReturnPrematch = float(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_RETURN_PREMATCH])
        customerProfile.totalReturnLive = float(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_RETURN_LIVE])
        customerProfile.totalReturn = float(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_RETURN])
        customerProfile.mostRecentCouponDateKeyUTC = int(
            dfCustomer.iloc[0][Columns.CustomerData.MOST_RECENT_COUPON_DATE_KEY_UTC]
        )

        customerProfile.netEarningsPrematch = float(dfCustomer.iloc[0][Columns.CustomerData.NET_EARNINGS_PREMATCH])
        customerProfile.netEarningsLive = float(dfCustomer.iloc[0][Columns.CustomerData.NET_EARNINGS_LIVE])
        customerProfile.netEarnings = float(dfCustomer.iloc[0][Columns.CustomerData.NET_EARNINGS])
        customerProfile.returnOnStakePercentagePrematch = float(
            dfCustomer.iloc[0][Columns.CustomerData.RETURN_ON_STAKE_PERCENTAGE_PREMATCH]
        )
        customerProfile.returnOnStakePercentageLive = float(
            dfCustomer.iloc[0][Columns.CustomerData.RETURN_ON_STAKE_PERCENTAGE_LIVE]
        )
        customerProfile.returnOnStakePercentage = float(
            dfCustomer.iloc[0][Columns.CustomerData.RETURN_ON_STAKE_PERCENTAGE]
        )
        customerProfile.marginPrematch = float(dfCustomer.iloc[0][Columns.CustomerData.MARGIN_PREMATCH])
        customerProfile.marginLive = float(dfCustomer.iloc[0][Columns.CustomerData.MARGIN_LIVE])
        customerProfile.margin = float(dfCustomer.iloc[0][Columns.CustomerData.MARGIN])
        customerProfile.winningStatusPrematch = int(dfCustomer.iloc[0][Columns.CustomerData.WINNING_STATUS_PREMATCH])
        customerProfile.winningStatusLive = int(dfCustomer.iloc[0][Columns.CustomerData.WINNING_STATUS_LIVE])
        customerProfile.winningStatus = int(dfCustomer.iloc[0][Columns.CustomerData.WINNING_STATUS])
        customerProfile.accuracyPrematch = float(dfCustomer.iloc[0][Columns.CustomerData.ACCURACY_PREMATCH])
        customerProfile.accuracyLive = float(dfCustomer.iloc[0][Columns.CustomerData.ACCURACY_LIVE])
        customerProfile.accuracy = float(dfCustomer.iloc[0][Columns.CustomerData.ACCURACY])

        customerProfile.clusterAverageCouponStake = str(
            dfCustomer.iloc[0][Columns.CustomerData.CLUSTER_AVERAGE_COUPON_STAKE]
        )
        customerProfile.clusterAccuracy = str(dfCustomer.iloc[0][Columns.CustomerData.CLUSTER_ACCURACY])
        customerProfile.clusterNumberOfCoupons = str(dfCustomer.iloc[0][Columns.CustomerData.CLUSTER_NUMBER_OF_COUPONS])
        customerProfile.clusterNetEarnings = str(dfCustomer.iloc[0][Columns.CustomerData.CLUSTER_NET_EARNINGS])
        customerProfile.clusterMostRecentCouponDate = str(
            dfCustomer.iloc[0][Columns.CustomerData.CLUSTER_MOST_RECENT_COUPON_DATE]
        )

        return customerProfile
