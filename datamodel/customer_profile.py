import pandas as pd
from pydantic import BaseModel
from datetime import datetime

from datamodel.columns import Columns
from utils.format_data import get_value


class CustomerProfile(BaseModel):
    userId: int = 0
    clientIP: str = ""

    userPlatformId: int = 0
    userTypeId: int = 0
    userTypeName: str = ""
    userStatusId: int = 0
    userStatusName: str = ""
    firstName: str = ""
    lastName: str = ""
    username: str = ""
    email: str = ""
    gender: str = ""
    birthDateKey: int = 0
    userCurrencyId: int = 0
    userCurrencyName: str = ""
    subscriptionDateKey: int = 0
    verificationLevelId: int = 0
    verificationLevelName: str = ""
    streetAddress: str = ""
    town: str = ""
    zipCode: str = ""
    countryId: int = 0
    countryName: str = ""
    phone: str = ""
    mobilePhone: str = ""

    availableBalanceTotalLocal: float = 0.0
    availableBalanceTotal: float = 0.0
    unsettledStake: float = 0.0

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

    totalNumberOfCouponsPrematch: int = 0
    totalNumberOfCouponsLive: int = 0
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
    mostRecentCouponDateKey: int = 0

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

    cashoutTotalNumberOfCouponsPrematch: int = 0
    cashoutTotalNumberOfCouponsLive: int = 0
    cashoutTotalNumberOfCoupons: int = 0
    cashoutTotalStakePrematch: float = 0.0
    cashoutTotalStakeLive: float = 0.0
    cashoutTotalStake: float = 0.0
    cashoutTotalReturnPrematch: float = 0.0
    cashoutTotalReturnLive: float = 0.0
    cashoutTotalReturn: float = 0.0
    cashoutNetEarningsPrematch: float = 0.0
    cashoutNetEarningsLive: float = 0.0
    cashoutNetEarnings: float = 0.0
    cashoutPotentialPayoutPrematch: float = 0.0
    cashoutPotentialPayoutLive: float = 0.0
    cashoutPotentialPayout: float = 0.0
    cashoutMarginPrematch: float = 0.0
    cashoutMarginLive: float = 0.0
    cashoutMargin: float = 0.0

    singlesTotalNumberOfCoupons: int = 0
    singlesPercentageOfTotalNumberOfCoupons: float = 0.0
    singlesAverageCouponOdds: float = 0.0
    singlesAverageCouponStake: float = 0.0
    singlesAverageCouponReturn: float = 0.0
    singlesTotalStake: float = 0.0
    singlesPercentageOfTotalStake: float = 0.0
    singlesTotalReturn: float = 0.0
    singlesPercentageOfTotalReturn: float = 0.0
    singlesNetEarnings: float = 0.0
    singlesPercentageOfNetEarnings: float = 0.0
    singlesReturnOnStakePercentage: float = 0.0
    singlesMargin: float = 0.0
    singlesWinningStatus: int = 0
    singlesTruePositives: int = 0
    singlesFalsePositives: int = 0
    singlesAccuracy: float = 0.0

    multisAverageSelectionOdds: float = 0.0
    multisAverageSelectionStake: float = 0.0
    multisAverageSelectionReturn: float = 0.0
    multisTruePositives: int = 0
    multisFalsePositives: int = 0
    multisTotalNumberOfCoupons: int = 0
    multisPercentageOfTotalNumberOfCoupons: float = 0.0
    multisTotalNumberOfSelections: int = 0
    multisAverageCouponNumberOfSelections: float = 0.0
    multisAverageCouponStake: float = 0.0
    multisAverageCouponReturn: float = 0.0
    multisTotalStake: float = 0.0
    multisPercentageOfTotalStake: float = 0.0
    multisTotalReturn: float = 0.0
    multisPercentageOfTotalReturn: float = 0.0
    multisAverageCouponOdds: float = 0.0
    multisNetEarnings: float = 0.0
    multisPercentageOfNetEarnings: float = 0.0
    multisReturnOnStakePercentage: float = 0.0
    multisMargin: float = 0.0
    multisWinningStatus: int = 0
    multisAccuracy: float = 0.0

    sportsStatsNumberOfSelections: list = []
    sportsStatsTotalStake: list = []
    singlesSportsStatsNumberOfSelections: list = []
    singlesSportsStatsTotalStake: list = []
    multisSportsStatsNumberOfSelections: list = []
    multisSportsStatsTotalStake: list = []

    tournamentsStatsNumberOfSelections: list = []
    tournamentsStatsTotalStake: list = []
    singlesTournamentsStatsNumberOfSelections: list = []
    singlesTournamentsStatsTotalStake: list = []
    multisTournamentsStatsNumberOfSelections: list = []
    multisTournamentsStatsTotalStake: list = []

    marketsStatsNumberOfSelections: list = []
    marketsStatsTotalStake: list = []
    singlesMarketsStatsNumberOfSelections: list = []
    singlesMarketsStatsTotalStake: list = []
    multisMarketsStatsNumberOfSelections: list = []
    multisMarketsStatsTotalStake: list = []

    clusterAverageCouponStake: str = ""
    clusterAccuracy: str = ""
    clusterNumberOfCoupons: str = ""
    clusterNetEarnings: str = ""
    clusterMostRecentCouponDate: str = ""

    @property
    def age(self) -> int:

        if str(self.birthDateKey) == "N/A":
            return 0

        birthDate = datetime.strptime(str(self.birthDateKey), "%Y%m%d")
        today = datetime.today()
        return int((today - birthDate).days / 365.242199)

    @classmethod
    def from_data(cls, dfCustomer: pd.DataFrame):
        customerProfile = cls()

        customerProfile.userId = get_value(dfCustomer.iloc[0][Columns.CustomerData.USER_ID], "int")
        customerProfile.clientIP = get_value(dfCustomer.iloc[0][Columns.CustomerData.CLIENT_IP], "str")

        customerProfile.userPlatformId = get_value(dfCustomer.iloc[0][Columns.CustomerData.USER_PLATFORM_ID], "int")
        customerProfile.userTypeId = get_value(dfCustomer.iloc[0][Columns.CustomerData.USER_TYPE_ID], "int")
        customerProfile.userTypeName = get_value(dfCustomer.iloc[0][Columns.CustomerData.USER_TYPE_NAME], "str")
        customerProfile.userStatusId = get_value(dfCustomer.iloc[0][Columns.CustomerData.USER_STATUS_ID], "int")
        customerProfile.userStatusName = get_value(dfCustomer.iloc[0][Columns.CustomerData.USER_STATUS_NAME], "str")
        customerProfile.firstName = get_value(dfCustomer.iloc[0][Columns.CustomerData.FIRST_NAME], "str")
        customerProfile.lastName = get_value(dfCustomer.iloc[0][Columns.CustomerData.LAST_NAME], "str")
        customerProfile.username = get_value(dfCustomer.iloc[0][Columns.CustomerData.USERNAME], "str")
        customerProfile.email = get_value(dfCustomer.iloc[0][Columns.CustomerData.EMAIL], "str")
        customerProfile.gender = get_value(dfCustomer.iloc[0][Columns.CustomerData.GENDER], "str")
        customerProfile.birthDateKey = get_value(dfCustomer.iloc[0][Columns.CustomerData.BIRTH_DATE_KEY], "int")
        customerProfile.userCurrencyId = get_value(dfCustomer.iloc[0][Columns.CustomerData.USER_CURRENCY_ID], "int")
        customerProfile.userCurrencyName = get_value(dfCustomer.iloc[0][Columns.CustomerData.USER_CURRENCY_NAME], "str")
        customerProfile.subscriptionDateKey = get_value(dfCustomer.iloc[0][Columns.CustomerData.SUBSCRIPTION_DATE_KEY], "int")
        customerProfile.verificationLevelId = get_value(dfCustomer.iloc[0][Columns.CustomerData.VERIFICATION_LEVEL_ID], "int")
        customerProfile.verificationLevelName = get_value(dfCustomer.iloc[0][Columns.CustomerData.VERIFICATION_LEVEL_NAME], "str")
        customerProfile.streetAddress = get_value(dfCustomer.iloc[0][Columns.CustomerData.STREET_ADDRESS], "str")
        customerProfile.town = get_value(dfCustomer.iloc[0][Columns.CustomerData.TOWN], "str")
        customerProfile.zipCode = get_value(dfCustomer.iloc[0][Columns.CustomerData.ZIP_CODE], "str")
        customerProfile.countryId = get_value(dfCustomer.iloc[0][Columns.CustomerData.COUNTRY_ID], "int")
        customerProfile.countryName = get_value(dfCustomer.iloc[0][Columns.CustomerData.COUNTRY_NAME], "str")
        customerProfile.phone = get_value(dfCustomer.iloc[0][Columns.CustomerData.PHONE], "str")
        customerProfile.mobilePhone = get_value(dfCustomer.iloc[0][Columns.CustomerData.MOBILE_PHONE], "str")

        customerProfile.availableBalanceTotalLocal = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVAILABLE_BALANCE_TOTAL_LOCAL], "float")
        customerProfile.availableBalanceTotal = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVAILABLE_BALANCE_TOTAL], "float")
        customerProfile.unsettledStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.UNSETTLED_STAKE], "float")

        customerProfile.averageSelectionOddsPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_ODDS_PREMATCH], "float")
        customerProfile.averageSelectionOddsLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_ODDS_LIVE], "float")
        customerProfile.averageSelectionOdds = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_ODDS], "float")
        customerProfile.averageCouponOddsPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_ODDS_PREMATCH], "float")
        customerProfile.averageCouponOddsLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_ODDS_LIVE], "float")
        customerProfile.averageCouponOdds = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_ODDS], "float")
        customerProfile.averageSelectionStakePrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_STAKE_PREMATCH], "float")
        customerProfile.averageSelectionStakeLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_STAKE_LIVE], "float")
        customerProfile.averageSelectionStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_STAKE], "float")
        customerProfile.averageSelectionReturnPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_RETURN_PREMATCH], "float")
        customerProfile.averageSelectionReturnLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_RETURN_LIVE], "float")
        customerProfile.averageSelectionReturn = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_SELECTION_RETURN], "float")
        customerProfile.averageProbabilityEstimateKellyCriterion = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_PROBABILITY_ESTIMATE_KELLY_CRITERION], "float")
        customerProfile.averageBetScore = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_BET_SCORE], "float")
        customerProfile.truePositivesPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.TRUE_POSITIVES_PREMATCH], "int")
        customerProfile.truePositivesLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.TRUE_POSITIVES_LIVE], "int")
        customerProfile.truePositives = get_value(dfCustomer.iloc[0][Columns.CustomerData.TRUE_POSITIVES], "int")
        customerProfile.falsePositivesPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.FALSE_POSITIVES_PREMATCH], "int")
        customerProfile.falsePositivesLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.FALSE_POSITIVES_LIVE], "int")
        customerProfile.falsePositives = get_value(dfCustomer.iloc[0][Columns.CustomerData.FALSE_POSITIVES], "int")

        customerProfile.totalNumberOfCouponsPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_NUMBER_OF_COUPONS_PREMATCH], "int")
        customerProfile.totalNumberOfCouponsLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_NUMBER_OF_COUPONS_LIVE], "int")
        customerProfile.totalNumberOfCoupons = get_value(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_NUMBER_OF_COUPONS], "int")
        customerProfile.totalNumberOfSelectionsPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_NUMBER_OF_SELECTIONS_PREMATCH], "int")
        customerProfile.totalNumberOfSelectionsLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_NUMBER_OF_SELECTIONS_LIVE], "int")
        customerProfile.totalNumberOfSelections = get_value(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_NUMBER_OF_SELECTIONS], "int")
        customerProfile.averageCouponNumberOfSelectionsPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_NUMBER_OF_SELECTIONS_PREMATCH], "float")
        customerProfile.averageCouponNumberOfSelectionsLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_NUMBER_OF_SELECTIONS_LIVE], "float")
        customerProfile.averageCouponNumberOfSelections = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_NUMBER_OF_SELECTIONS], "float")
        customerProfile.averageCouponPotentialPayoutPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_POTENTIAL_PAYOUT_PREMATCH], "float")
        customerProfile.averageCouponPotentialPayoutLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_POTENTIAL_PAYOUT_LIVE], "float")
        customerProfile.averageCouponPotentialPayout = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_POTENTIAL_PAYOUT], "float")
        customerProfile.averageCouponStakePrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_STAKE_PREMATCH], "float")
        customerProfile.averageCouponStakeLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_STAKE_LIVE], "float")
        customerProfile.averageCouponStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_STAKE], "float")
        customerProfile.averageCouponReturnPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_RETURN_PREMATCH], "float")
        customerProfile.averageCouponReturnLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_RETURN_LIVE], "float")
        customerProfile.averageCouponReturn = get_value(dfCustomer.iloc[0][Columns.CustomerData.AVERAGE_COUPON_RETURN], "float")
        customerProfile.highestCouponStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.HIGHEST_COUPON_STAKE], "float")
        customerProfile.highestCouponReturn = get_value(dfCustomer.iloc[0][Columns.CustomerData.HIGHEST_COUPON_RETURN], "float")
        customerProfile.totalStakePrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_STAKE_PREMATCH], "float")
        customerProfile.totalStakeLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_STAKE_LIVE], "float")
        customerProfile.totalStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_STAKE], "float")
        customerProfile.totalReturnPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_RETURN_PREMATCH], "float")
        customerProfile.totalReturnLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_RETURN_LIVE], "float")
        customerProfile.totalReturn = get_value(dfCustomer.iloc[0][Columns.CustomerData.TOTAL_RETURN], "float")
        customerProfile.mostRecentCouponDateKey = get_value(dfCustomer.iloc[0][Columns.CustomerData.MOST_RECENT_COUPON_DATE_KEY], "int")

        customerProfile.netEarningsPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.NET_EARNINGS_PREMATCH], "float")
        customerProfile.netEarningsLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.NET_EARNINGS_LIVE], "float")
        customerProfile.netEarnings = get_value(dfCustomer.iloc[0][Columns.CustomerData.NET_EARNINGS], "float")
        customerProfile.returnOnStakePercentagePrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.RETURN_ON_STAKE_PERCENTAGE_PREMATCH], "float")
        customerProfile.returnOnStakePercentageLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.RETURN_ON_STAKE_PERCENTAGE_LIVE], "float")
        customerProfile.returnOnStakePercentage = get_value(dfCustomer.iloc[0][Columns.CustomerData.RETURN_ON_STAKE_PERCENTAGE], "float")
        customerProfile.marginPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.MARGIN_PREMATCH], "float")
        customerProfile.marginLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.MARGIN_LIVE], "float")
        customerProfile.margin = get_value(dfCustomer.iloc[0][Columns.CustomerData.MARGIN], "float")
        customerProfile.winningStatusPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.WINNING_STATUS_PREMATCH], "int")
        customerProfile.winningStatusLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.WINNING_STATUS_LIVE], "int")
        customerProfile.winningStatus = get_value(dfCustomer.iloc[0][Columns.CustomerData.WINNING_STATUS], "int")
        customerProfile.accuracyPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.ACCURACY_PREMATCH], "float")
        customerProfile.accuracyLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.ACCURACY_LIVE], "float")
        customerProfile.accuracy = get_value(dfCustomer.iloc[0][Columns.CustomerData.ACCURACY], "float")

        customerProfile.cashoutTotalNumberOfCouponsPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_TOTAL_NUMBER_OF_COUPONS_PREMATCH], "int")
        customerProfile.cashoutTotalNumberOfCouponsLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_TOTAL_NUMBER_OF_COUPONS_LIVE], "int")
        customerProfile.cashoutTotalNumberOfCoupons = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_TOTAL_NUMBER_OF_COUPONS], "int")
        customerProfile.cashoutTotalStakePrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_TOTAL_STAKE_PREMATCH], "float")
        customerProfile.cashoutTotalStakeLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_TOTAL_STAKE_LIVE], "float")
        customerProfile.cashoutTotalStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_TOTAL_STAKE], "float")
        customerProfile.cashoutTotalReturnPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_TOTAL_RETURN_PREMATCH], "float")
        customerProfile.cashoutTotalReturnLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_TOTAL_RETURN_LIVE], "float")
        customerProfile.cashoutTotalReturn = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_TOTAL_RETURN], "float")
        customerProfile.cashoutNetEarningsPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_NET_EARNINGS_PREMATCH], "float")
        customerProfile.cashoutNetEarningsLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_NET_EARNINGS_LIVE], "float")
        customerProfile.cashoutNetEarnings = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_NET_EARNINGS], "float")
        customerProfile.cashoutPotentialPayoutPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_POTENTIAL_PAYOUT_PREMATCH], "float")
        customerProfile.cashoutPotentialPayoutLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_POTENTIAL_PAYOUT_LIVE], "float")
        customerProfile.cashoutPotentialPayout = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_POTENTIAL_PAYOUT], "float")
        customerProfile.cashoutMarginPrematch = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_MARGIN_PREMATCH], "float")
        customerProfile.cashoutMarginLive = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_MARGIN_LIVE], "float")
        customerProfile.cashoutMargin = get_value(dfCustomer.iloc[0][Columns.CustomerData.CASHOUT_MARGIN], "float")

        customerProfile.singlesTotalNumberOfCoupons = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_TOTAL_NUMBER_OF_COUPONS], "int")
        customerProfile.singlesPercentageOfTotalNumberOfCoupons = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_PERCENTAGE_OF_TOTAL_NUMBER_OF_COUPONS], "float")
        customerProfile.singlesAverageCouponOdds = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_AVERAGE_COUPON_ODDS], "float")
        customerProfile.singlesAverageCouponStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_AVERAGE_COUPON_STAKE], "float")
        customerProfile.singlesAverageCouponReturn = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_AVERAGE_COUPON_RETURN], "float")
        customerProfile.singlesTotalStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_TOTAL_STAKE], "float")
        customerProfile.singlesPercentageOfTotalStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_PERCENTAGE_OF_TOTAL_STAKE], "float")
        customerProfile.singlesTotalReturn = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_TOTAL_RETURN], "float")
        customerProfile.singlesPercentageOfTotalReturn = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_PERCENTAGE_OF_TOTAL_RETURN], "float")
        customerProfile.singlesNetEarnings = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_NET_EARNINGS], "float")
        customerProfile.singlesPercentageOfNetEarnings = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_PERCENTAGE_OF_NET_EARNINGS], "float")
        customerProfile.singlesReturnOnStakePercentage = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_RETURN_ON_STAKE_PERCENTAGE], "float")
        customerProfile.singlesMargin = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_MARGIN], "float")
        customerProfile.singlesWinningStatus = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_WINNING_STATUS], "int")
        customerProfile.singlesTruePositives = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_TRUE_POSITIVES], "int")
        customerProfile.singlesFalsePositives = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_FALSE_POSITIVES], "int")
        customerProfile.singlesAccuracy = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_ACCURACY], "float")

        customerProfile.multisAverageSelectionOdds = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_AVERAGE_SELECTION_ODDS], "float")
        customerProfile.multisAverageSelectionStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_AVERAGE_SELECTION_STAKE], "float")
        customerProfile.multisAverageSelectionReturn = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_AVERAGE_SELECTION_RETURN], "float")
        customerProfile.multisTruePositives = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_TRUE_POSITIVES], "int")
        customerProfile.multisFalsePositives = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_FALSE_POSITIVES], "int")
        customerProfile.multisTotalNumberOfCoupons = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_TOTAL_NUMBER_OF_COUPONS], "int")
        customerProfile.multisPercentageOfTotalNumberOfCoupons = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_PERCENTAGE_OF_TOTAL_NUMBER_OF_COUPONS], "float")
        customerProfile.multisTotalNumberOfSelections = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_TOTAL_NUMBER_OF_SELECTIONS], "int")
        customerProfile.multisAverageCouponNumberOfSelections = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_AVERAGE_COUPON_NUMBER_OF_SELECTIONS], "float")
        customerProfile.multisAverageCouponStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_AVERAGE_COUPON_STAKE], "float")
        customerProfile.multisAverageCouponReturn = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_AVERAGE_COUPON_RETURN], "float")
        customerProfile.multisTotalStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_TOTAL_STAKE], "float")
        customerProfile.multisPercentageOfTotalStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_PERCENTAGE_OF_TOTAL_STAKE], "float")
        customerProfile.multisTotalReturn = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_TOTAL_RETURN], "float")
        customerProfile.multisPercentageOfTotalReturn = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_PERCENTAGE_OF_TOTAL_RETURN], "float")
        customerProfile.multisAverageCouponOdds = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_AVERAGE_COUPON_ODDS], "float")
        customerProfile.multisNetEarnings = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_NET_EARNINGS], "float")
        customerProfile.multisPercentageOfNetEarnings = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_PERCENTAGE_OF_NET_EARNINGS], "float")
        customerProfile.multisReturnOnStakePercentage = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_RETURN_ON_STAKE_PERCENTAGE], "float")
        customerProfile.multisMargin = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_MARGIN], "float")
        customerProfile.multisWinningStatus = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_WINNING_STATUS], "int")
        customerProfile.multisAccuracy = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_ACCURACY], "float")

        customerProfile.sportsStatsNumberOfSelections = get_value(dfCustomer.iloc[0][Columns.CustomerData.SPORTS_STATS_NUMBER_OF_SELECTIONS], "list")
        customerProfile.sportsStatsTotalStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.SPORTS_STATS_TOTAL_STAKE], "list")
        customerProfile.singlesSportsStatsNumberOfSelections = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_SPORTS_STATS_NUMBER_OF_SELECTIONS], "list")
        customerProfile.singlesSportsStatsTotalStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_SPORTS_STATS_TOTAL_STAKE], "list")
        customerProfile.multisSportsStatsNumberOfSelections = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_SPORTS_STATS_NUMBER_OF_SELECTIONS], "list")
        customerProfile.multisSportsStatsTotalStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_SPORTS_STATS_TOTAL_STAKE], "list")

        customerProfile.tournamentsStatsNumberOfSelections = get_value(dfCustomer.iloc[0][Columns.CustomerData.TOURNAMENTS_STATS_NUMBER_OF_SELECTIONS], "list")
        customerProfile.tournamentsStatsTotalStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.TOURNAMENTS_STATS_TOTAL_STAKE], "list")
        customerProfile.singlesTournamentsStatsNumberOfSelections = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_TOURNAMENTS_STATS_NUMBER_OF_SELECTIONS], "list")
        customerProfile.singlesTournamentsStatsTotalStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_TOURNAMENTS_STATS_TOTAL_STAKE], "list")
        customerProfile.multisTournamentsStatsNumberOfSelections = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_TOURNAMENTS_STATS_NUMBER_OF_SELECTIONS], "list")
        customerProfile.multisTournamentsStatsTotalStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_TOURNAMENTS_STATS_TOTAL_STAKE], "list")

        customerProfile.marketsStatsNumberOfSelections = get_value(dfCustomer.iloc[0][Columns.CustomerData.MARKETS_STATS_NUMBER_OF_SELECTIONS], "list")
        customerProfile.marketsStatsTotalStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.MARKETS_STATS_TOTAL_STAKE], "list")
        customerProfile.singlesMarketsStatsNumberOfSelections = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_MARKETS_STATS_NUMBER_OF_SELECTIONS], "list")
        customerProfile.singlesMarketsStatsTotalStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.SINGLES_MARKETS_STATS_TOTAL_STAKE], "list")
        customerProfile.multisMarketsStatsNumberOfSelections = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_MARKETS_STATS_NUMBER_OF_SELECTIONS], "list")
        customerProfile.multisMarketsStatsTotalStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.MULTIS_MARKETS_STATS_TOTAL_STAKE], "list")

        customerProfile.clusterAverageCouponStake = get_value(dfCustomer.iloc[0][Columns.CustomerData.CLUSTER_AVERAGE_COUPON_STAKE], "str")
        customerProfile.clusterAccuracy = get_value(dfCustomer.iloc[0][Columns.CustomerData.CLUSTER_ACCURACY], "str")
        customerProfile.clusterNumberOfCoupons = get_value(dfCustomer.iloc[0][Columns.CustomerData.CLUSTER_NUMBER_OF_COUPONS], "str")
        customerProfile.clusterNetEarnings = get_value(dfCustomer.iloc[0][Columns.CustomerData.CLUSTER_NET_EARNINGS], "str")
        customerProfile.clusterMostRecentCouponDate = get_value(dfCustomer.iloc[0][Columns.CustomerData.CLUSTER_MOST_RECENT_COUPON_DATE], "str")

        return customerProfile
