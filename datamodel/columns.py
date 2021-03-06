from aenum import Enum, skip


class Columns(Enum):
    @skip
    class CouponData(str, Enum):
        # from raw layer
        USER_ID = "IDUser"
        CLIENT_IP = "ClientIP"

        SELECTION_ID = "IDSelection"
        COUPON_ID = "IDCoupon"
        COUPON_CODE = "CouponCode"
        STAKE = "Stake"
        ODD_VALUE = "OddValue"
        MIN_WIN = "MinWin"
        MAX_WIN = "MaxWin"
        MIN_BONUS = "MinBonus"
        MAX_BONUS = "MaxBonus"
        MIN_COUPON_RETURN = "MinCouponReturn"
        MAX_COUPON_RETURN = "MaxCouponReturn"
        FORCED_STATUS = "ForcedStatus"
        COUPON_RETURN = "CouponReturn"
        EVENT_CATEGORY = "EventCategory"
        PLACEMENT_EXCHANGE_RATE = "PlacementExchangeRate"
        SETTLEMENT_EXCHANGE_RATE = "SettlementExchangeRate"
        COUPON_DATE_KEY = "CouponDateKey"
        SETTLEMENT_DATE_KEY = "SettlementDateKey"
        COUPON_TYPE_ID = "IDCouponType"
        COUPON_STATUS_ID = "IDCouponStatus"
        SETTLEMENT_STATUS_ID = "IDSettlementStatus"
        SPORT_ID = "IDSport"
        EVENT_TYPE_ID = "IDEventType"
        TOURNAMENT_NAME = "TournamentName"
        MARKET_TYPE_ID = "IDMarketType"

        # added in bronze layer
        NUMBER_OF_RELEVANT_SELECTIONS = "NumberOfRelevantSelections"
        COUPON_STAKE_IN_EUROS = "CouponStakeInEuros"
        COUPON_RETURN_IN_EUROS = "CouponReturnInEuros"
        MIN_WIN_IN_EUROS = "MinWinInEuros"
        MAX_WIN_IN_EUROS = "MaxWinInEuros"
        MIN_BONUS_IN_EUROS = "MinBonusInEuros"
        MAX_BONUS_IN_EUROS = "MaxBonusInEuros"
        MIN_COUPON_RETURN_IN_EUROS = "MinCouponReturnInEuros"
        MAX_COUPON_RETURN_IN_EUROS = "MaxCouponReturnInEuros"
        STAKE_PER_SELECTION = "StakePerSelection"
        RETURN_PER_SELECTION = "ReturnPerSelection"
        SELECTION_PROBABILITY = "SelectionProbability"

        # added in silver layer
        TOTAL_BANKROLL = "TotalBankroll"
        PROBABILITY_ESTIMATE_KELLY_CRITERION = "ProbabilityEstimateKellyCriterion"
        BET_SCORE = "BetScore"

    @skip
    class CustomerData(str, Enum):
        # from raw layer
        USER_ID = "IDUser"
        CLIENT_IP = "ClientIP"

        # from silver layer
        USER_PLATFORM_ID = "IDUserPlatform"
        USER_TYPE_ID = "IDUserType"
        USER_TYPE_NAME = "UserTypeName"
        USER_STATUS_ID = "IDUserStatus"
        USER_STATUS_NAME = "UserStatusName"
        FIRST_NAME = "FirstName"
        LAST_NAME = "LastName"
        USERNAME = "UserName"
        EMAIL = "Email"
        GENDER = "Gender"
        BIRTH_DATE_KEY = "BirthDateKey"
        USER_CURRENCY_ID = "IDCurrency"
        USER_CURRENCY_NAME = "CurrencyName"
        SUBSCRIPTION_DATE_KEY = "SubscriptionDateKey"
        VERIFICATION_LEVEL_ID = "IDVerificationLevel"
        VERIFICATION_LEVEL_NAME = "VerificationLevelName"
        STREET_ADDRESS = "StreetAddress"
        TOWN = "Town"
        ZIP_CODE = "ZipCode"
        COUNTRY_ID = "IDCountry"
        COUNTRY_NAME = "CountryName"
        PHONE = "Phone"
        MOBILE_PHONE = "MobilePhone"

        AVAILABLE_BALANCE_TOTAL_LOCAL = "AvailableBalanceTotalLocal"
        AVAILABLE_BALANCE_TOTAL = "AvailableBalanceTotal"
        UNSETTLED_STAKE = "UnsettledStake"

        # added in gold layer
        AVERAGE_SELECTION_ODDS_PREMATCH = "AverageSelectionOddsPrematch"
        AVERAGE_SELECTION_ODDS_LIVE = "AverageSelectionOddsLive"
        AVERAGE_SELECTION_ODDS = "AverageSelectionOdds"
        AVERAGE_COUPON_ODDS_PREMATCH = "AverageCouponOddsPrematch"
        AVERAGE_COUPON_ODDS_LIVE = "AverageCouponOddsLive"
        AVERAGE_COUPON_ODDS = "AverageCouponOdds"
        AVERAGE_SELECTION_STAKE_PREMATCH = "AverageSelectionStakePrematch"
        AVERAGE_SELECTION_STAKE_LIVE = "AverageSelectionStakeLive"
        AVERAGE_SELECTION_STAKE = "AverageSelectionStake"
        AVERAGE_SELECTION_RETURN_PREMATCH = "AverageSelectionReturnPrematch"
        AVERAGE_SELECTION_RETURN_LIVE = "AverageSelectionReturnLive"
        AVERAGE_SELECTION_RETURN = "AverageSelectionReturn"
        AVERAGE_PROBABILITY_ESTIMATE_KELLY_CRITERION = "AverageProbabilityEstimateKellyCriterion"
        AVERAGE_BET_SCORE = "AverageBetScore"
        TRUE_POSITIVES_PREMATCH = "TruePositivesPrematch"
        TRUE_POSITIVES_LIVE = "TruePositivesLive"
        TRUE_POSITIVES = "TruePositives"
        FALSE_POSITIVES_PREMATCH = "FalsePositivesPrematch"
        FALSE_POSITIVES_LIVE = "FalsePositivesLive"
        FALSE_POSITIVES = "FalsePositives"

        TOTAL_NUMBER_OF_COUPONS_PREMATCH = "TotalNumberOfCouponsPrematch"
        TOTAL_NUMBER_OF_COUPONS_LIVE = "TotalNumberOfCouponsLive"
        TOTAL_NUMBER_OF_COUPONS = "TotalNumberOfCoupons"
        TOTAL_NUMBER_OF_SELECTIONS_PREMATCH = "TotalNumberOfSelectionsPrematch"
        TOTAL_NUMBER_OF_SELECTIONS_LIVE = "TotalNumberOfSelectionsLive"
        TOTAL_NUMBER_OF_SELECTIONS = "TotalNumberOfSelections"
        AVERAGE_COUPON_NUMBER_OF_SELECTIONS_PREMATCH = "AverageCouponNumberOfSelectionsPrematch"
        AVERAGE_COUPON_NUMBER_OF_SELECTIONS_LIVE = "AverageCouponNumberOfSelectionsLive"
        AVERAGE_COUPON_NUMBER_OF_SELECTIONS = "AverageCouponNumberOfSelections"
        AVERAGE_COUPON_POTENTIAL_PAYOUT_PREMATCH = "AverageCouponPotentialPayoutPrematch"
        AVERAGE_COUPON_POTENTIAL_PAYOUT_LIVE = "AverageCouponPotentialPayoutLive"
        AVERAGE_COUPON_POTENTIAL_PAYOUT = "AverageCouponPotentialPayout"
        AVERAGE_COUPON_STAKE_PREMATCH = "AverageCouponStakePrematch"
        AVERAGE_COUPON_STAKE_LIVE = "AverageCouponStakeLive"
        AVERAGE_COUPON_STAKE = "AverageCouponStake"
        AVERAGE_COUPON_RETURN_PREMATCH = "AverageCouponReturnPrematch"
        AVERAGE_COUPON_RETURN_LIVE = "AverageCouponReturnLive"
        AVERAGE_COUPON_RETURN = "AverageCouponReturn"
        HIGHEST_COUPON_STAKE = "HighestCouponStake"
        HIGHEST_COUPON_RETURN = "HighestCouponReturn"
        TOTAL_STAKE_PREMATCH = "TotalStakePrematch"
        TOTAL_STAKE_LIVE = "TotalStakeLive"
        TOTAL_STAKE = "TotalStake"
        TOTAL_RETURN_PREMATCH = "TotalReturnPrematch"
        TOTAL_RETURN_LIVE = "TotalReturnLive"
        TOTAL_RETURN = "TotalReturn"
        MOST_RECENT_COUPON_DATE_KEY = "MostRecentCouponDateKey"

        NET_EARNINGS_PREMATCH = "NetEarningsPrematch"
        NET_EARNINGS_LIVE = "NetEarningsLive"
        NET_EARNINGS = "NetEarnings"
        RETURN_ON_STAKE_PERCENTAGE_PREMATCH = "ReturnOnStakePercentagePrematch"
        RETURN_ON_STAKE_PERCENTAGE_LIVE = "ReturnOnStakePercentageLive"
        RETURN_ON_STAKE_PERCENTAGE = "ReturnOnStakePercentage"
        MARGIN_PREMATCH = "MarginPrematch"
        MARGIN_LIVE = "MarginLive"
        MARGIN = "Margin"
        WINNING_STATUS_PREMATCH = "WinningStatusPrematch"
        WINNING_STATUS_LIVE = "WinningStatusLive"
        WINNING_STATUS = "WinningStatus"
        ACCURACY_PREMATCH = "AccuracyPrematch"
        ACCURACY_LIVE = "AccuracyLive"
        ACCURACY = "Accuracy"

        CASHOUT_TOTAL_NUMBER_OF_COUPONS_PREMATCH = "CashoutTotalNumberOfCouponsPrematch"
        CASHOUT_TOTAL_NUMBER_OF_COUPONS_LIVE = "CashoutTotalNumberOfCouponsLive"
        CASHOUT_TOTAL_NUMBER_OF_COUPONS = "CashoutTotalNumberOfCoupons"
        CASHOUT_TOTAL_STAKE_PREMATCH = "CashoutTotalStakePrematch"
        CASHOUT_TOTAL_STAKE_LIVE = "CashoutTotalStakeLive"
        CASHOUT_TOTAL_STAKE = "CashoutTotalStake"
        CASHOUT_TOTAL_RETURN_PREMATCH = "CashoutTotalReturnPrematch"
        CASHOUT_TOTAL_RETURN_LIVE = "CashoutTotalReturnLive"
        CASHOUT_TOTAL_RETURN = "CashoutTotalReturn"
        CASHOUT_NET_EARNINGS_PREMATCH = "CashoutNetEarningsPrematch"
        CASHOUT_NET_EARNINGS_LIVE = "CashoutNetEarningsLive"
        CASHOUT_NET_EARNINGS = "CashoutNetEarnings"
        CASHOUT_POTENTIAL_PAYOUT_PREMATCH = "CashoutPotentialPayoutPrematch"
        CASHOUT_POTENTIAL_PAYOUT_LIVE = "CashoutPotentialPayoutLive"
        CASHOUT_POTENTIAL_PAYOUT = "CashoutPotentialPayout"
        CASHOUT_MARGIN_PREMATCH = "CashoutMarginPrematch"
        CASHOUT_MARGIN_LIVE = "CashoutMarginLive"
        CASHOUT_MARGIN = "CashoutMargin"

        SINGLES_TOTAL_NUMBER_OF_COUPONS = "SinglesTotalNumberOfCoupons"
        SINGLES_PERCENTAGE_OF_TOTAL_NUMBER_OF_COUPONS = "SinglesPercentageOfTotalNumberOfCoupons"
        SINGLES_AVERAGE_COUPON_ODDS = "SinglesAverageCouponOdds"
        SINGLES_AVERAGE_COUPON_STAKE = "SinglesAverageCouponStake"
        SINGLES_AVERAGE_COUPON_RETURN = "SinglesAverageCouponReturn"
        SINGLES_TOTAL_STAKE = "SinglesTotalStake"
        SINGLES_PERCENTAGE_OF_TOTAL_STAKE = "SinglesPercentageOfTotalStake"
        SINGLES_TOTAL_RETURN = "SinglesTotalReturn"
        SINGLES_PERCENTAGE_OF_TOTAL_RETURN = "SinglesPercentageOfTotalReturn"
        SINGLES_NET_EARNINGS = "SinglesNetEarnings"
        SINGLES_PERCENTAGE_OF_NET_EARNINGS = "SinglesPercentageOfNetEarnings"
        SINGLES_RETURN_ON_STAKE_PERCENTAGE = "SinglesReturnOnStakePercentage"
        SINGLES_MARGIN = "SinglesMargin"
        SINGLES_WINNING_STATUS = "SinglesWinningStatus"
        SINGLES_TRUE_POSITIVES = "SinglesTruePositives"
        SINGLES_FALSE_POSITIVES = "SinglesFalsePositives"
        SINGLES_ACCURACY = "SinglesAccuracy"

        MULTIS_AVERAGE_SELECTION_ODDS = "MultisAverageSelectionOdds"
        MULTIS_AVERAGE_SELECTION_STAKE = "MultisAverageSelectionStake"
        MULTIS_AVERAGE_SELECTION_RETURN = "MultisAverageSelectionReturn"
        MULTIS_TRUE_POSITIVES = "MultisTruePositives"
        MULTIS_FALSE_POSITIVES = "MultisFalsePositives"
        MULTIS_TOTAL_NUMBER_OF_COUPONS = "MultisTotalNumberOfCoupons"
        MULTIS_PERCENTAGE_OF_TOTAL_NUMBER_OF_COUPONS = "MultisPercentageOfTotalNumberOfCoupons"
        MULTIS_TOTAL_NUMBER_OF_SELECTIONS = "MultisTotalNumberOfSelections"
        MULTIS_AVERAGE_COUPON_NUMBER_OF_SELECTIONS = "MultisAverageCouponNumberOfSelections"
        MULTIS_AVERAGE_COUPON_STAKE = "MultisAverageCouponStake"
        MULTIS_AVERAGE_COUPON_RETURN = "MultisAverageCouponReturn"
        MULTIS_TOTAL_STAKE = "MultisTotalStake"
        MULTIS_PERCENTAGE_OF_TOTAL_STAKE = "MultisPercentageOfTotalStake"
        MULTIS_TOTAL_RETURN = "MultisTotalReturn"
        MULTIS_PERCENTAGE_OF_TOTAL_RETURN = "MultisPercentageOfTotalReturn"
        MULTIS_AVERAGE_COUPON_ODDS = "MultisAverageCouponOdds"
        MULTIS_NET_EARNINGS = "MultisNetEarnings"
        MULTIS_PERCENTAGE_OF_NET_EARNINGS = "MultisPercentageOfNetEarnings"
        MULTIS_RETURN_ON_STAKE_PERCENTAGE = "MultisReturnOnStakePercentage"
        MULTIS_MARGIN = "MultisMargin"
        MULTIS_WINNING_STATUS = "MultisWinningStatus"
        MULTIS_ACCURACY = "MultisAccuracy"

        SPORTS_STATS_NUMBER_OF_SELECTIONS = "SportsStatsNumberOfSelections"
        SPORTS_STATS_TOTAL_STAKE = "SportsStatsTotalStake"
        SINGLES_SPORTS_STATS_NUMBER_OF_SELECTIONS = "SinglesSportsStatsNumberOfSelections"
        SINGLES_SPORTS_STATS_TOTAL_STAKE = "SinglesSportsStatsTotalStake"
        MULTIS_SPORTS_STATS_NUMBER_OF_SELECTIONS = "MultisSportsStatsNumberOfSelections"
        MULTIS_SPORTS_STATS_TOTAL_STAKE = "MultisSportsStatsTotalStake"

        TOURNAMENTS_STATS_NUMBER_OF_SELECTIONS = "TournamentsStatsNumberOfSelections"
        TOURNAMENTS_STATS_TOTAL_STAKE = "TournamentsStatsTotalStake"
        SINGLES_TOURNAMENTS_STATS_NUMBER_OF_SELECTIONS = "SinglesTournamentsStatsNumberOfSelections"
        SINGLES_TOURNAMENTS_STATS_TOTAL_STAKE = "SinglesTournamentsStatsTotalStake"
        MULTIS_TOURNAMENTS_STATS_NUMBER_OF_SELECTIONS = "MultisTournamentsStatsNumberOfSelections"
        MULTIS_TOURNAMENTS_STATS_TOTAL_STAKE = "MultisTournamentsStatsTotalStake"

        MARKETS_STATS_NUMBER_OF_SELECTIONS = "MarketsStatsNumberOfSelections"
        MARKETS_STATS_TOTAL_STAKE = "MarketsStatsTotalStake"
        SINGLES_MARKETS_STATS_NUMBER_OF_SELECTIONS = "SinglesMarketsStatsNumberOfSelections"
        SINGLES_MARKETS_STATS_TOTAL_STAKE = "SinglesMarketsStatsTotalStake"
        MULTIS_MARKETS_STATS_NUMBER_OF_SELECTIONS = "MultisMarketsStatsNumberOfSelections"
        MULTIS_MARKETS_STATS_TOTAL_STAKE = "MultisMarketsStatsTotalStake"

        CLUSTER_AVERAGE_COUPON_STAKE = "ClusterAverageCouponStake"
        CLUSTER_ACCURACY = "ClusterAccuracy"
        CLUSTER_NUMBER_OF_COUPONS = "ClusterNumberOfCoupons"
        CLUSTER_NET_EARNINGS = "ClusterNetEarnings"
        CLUSTER_MOST_RECENT_COUPON_DATE = "ClusterMostRecentCouponDate"

    @skip
    class PopulationData(str, Enum):
        TOTAL_NUMBER_OF_USERS = "TotalNumberOfUsers"
        TOTAL_NUMBER_OF_COUPONS = "TotalNumberOfCoupons"
        AVERAGE_NUMBER_OF_SELECTIONS_PER_COUPON = "AverageNumberOfSelectionsPerCoupon"
        AVERAGE_ODD_VALUE_PER_SELECTION = "AverageOddValuePerSelection"
        AVERAGE_COUPON_STAKE = "AverageCouponStake"
        AVERAGE_COUPON_RETURN = "AverageCouponReturn"
        HIGHEST_COUPON_STAKE = "HighestCouponStake"
        HIGHEST_COUPON_RETURN = "HighestCouponReturn"
        TOTAL_STAKE = "TotalStake"
        TOTAL_RETURN = "TotalReturn"
        TOTAL_NET_EARNINGS = "TotalNetEarnings"
        AVERAGE_RETURN_ON_STAKE_PERCENTAGE = "AverageReturnOnStakePercentage"
        AVERAGE_TRUE_POSITIVES = "AverageTruePositives"
        AVERAGE_FALSE_POSITIVES = "AverageFalsePositives"
        AVERAGE_ACCURACY = "AverageAccuracy"
        AVERAGE_PROBABILITY_ESTIMATE_KELLY_CRITERION = "AverageProbabilityEstimateKellyCriterion"
        AVERAGE_BET_SCORE = "AverageBetScore"
