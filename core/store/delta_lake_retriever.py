import pyspark.sql
import pyspark.sql.functions as f
from pyspark.sql.types import StringType, LongType, DoubleType
from pyspark.sql import Window
from datetime import datetime

from core.datamodel.data_lake_path import DataLakePath
from core.store.data_lake_reader import DataLakeReader

# from core.datamodel.delta_lake_path import DeltaLakePath
from core.store.delta_lake_reader import DeltaLakeReader


class DeltaLakeRetriever:
    def __init__(self, deltaLakeReader: DeltaLakeReader, dataLakeReader: DataLakeReader):
        self.deltaLakeReader = deltaLakeReader
        self.dataLakeReader = dataLakeReader

    def get_selections_view(self) -> pyspark.sql.dataframe.DataFrame:
        dfSelections = (
            self.deltaLakeReader.read_table("db_bronze_sportsbook.program_selections")
            .select(
                "IDSelection",
                "IDMarket",
                "IDSelectionStatus",
                "IDMarketType",
                "IDSelectionType",
                "SelectionSpread",
                "ForcedStatus"
            )
        )

        dfMarkets = (
            self.deltaLakeReader.read_table("db_bronze_sportsbook.program_markets")
            .select(
                "IDMarket",
                "IDMarketType",
                "Spread"
            )
        )

        return dfSelections.join(other=dfMarkets, on=["IDMarket", "IDMarketType"])

    def get_coupons_view(self, startDate: datetime, endDate: datetime) -> pyspark.sql.dataframe.DataFrame:
        dfCoupons = (
            self.deltaLakeReader.read_table("db_bronze_sportsbook.bets_coupons")
            .select(
                "IDCoupon",
                "CouponCode",
                "CouponDateKey",
                "SettlementDateKey",
                "Stake",
                "MaxWin",
                "MinWin",
                "MinBonus",
                "MaxBonus",
                "TotalCombinations",
                "IDCouponStatus",
                "IDCouponType",
                "IDUser",
                "Won",
                "Bonus",
                "WonCombinations",
                "NumberOfSelections",
                "IsLive",
                "IDCurrency",
                "IDEvalReason",
                "IDChannel",
                "IDBrand",
                "PlaySourceId",
                "PlacementExchangeRate",
                "SettlementExchangeRate",
                "IDSettlementStatus",
                "ClientIP",
                "Domain",
            )
            .withColumnRenamed(existing="Won", new="CouponReturn")
        )

        dfCoupons = dfCoupons\
            .filter(dfCoupons["SettlementDateKey"] >= int(startDate.strftime("%Y%m%d")))\
            .filter(dfCoupons["SettlementDateKey"] <= int(endDate.strftime("%Y%m%d")))

        dfBetOdds = (
            self.deltaLakeReader.read_table("db_bronze_sportsbook.bets_betodds")
        )

        dfBetOdds = dfBetOdds \
            .filter(dfBetOdds["SettlementDateKey"] >= int(startDate.strftime("%Y%m%d"))) \
            .filter(dfBetOdds["SettlementDateKey"] <= int(endDate.strftime("%Y%m%d")))

        dfBetOdds = dfBetOdds.select(
            "IDCoupon",
            "IDEvent",
            "OddValue",
            "Banker",
            "IDSelection",
            "IDBetOddStatus",
            "EventCategory"
        )

        dfSelections = self.get_selections_view()

        dfEvents = (
            self.deltaLakeReader.read_table("db_bronze_sportsbook.program_events")
            .select(
                "IDEvent",
                "IDSport",
                "EventName",
                "MPath"
            )
        )

        return (
            dfCoupons.join(other=dfBetOdds, on=["IDCoupon"])
            .join(other=dfEvents, on=["IDEvent"], how="left")
            .join(other=dfSelections, on=["IDSelection"], how="left")
        )

    def get_users_info(self) -> pyspark.sql.dataframe.DataFrame:
        dfUsers = self.deltaLakeReader.read_table("db_bronze_sportsbook.accounts_users")

        dfUsers = dfUsers \
            .withColumn("BirthDateKey", f.date_format(f.col("BirthDate"), "yyyyMMdd").cast(LongType())) \
            .withColumn("SubscriptionDateKey", f.date_format(f.col("SubscriptionDate"), "yyyyMMdd").cast(LongType()))

        dfChannelUsers = (
            self.deltaLakeReader.read_table("db_bronze_sportsbook.channelmanagement_channelusers")
            .withColumnRenamed(existing="ExternalIDUser", new="IDUserPlatform")
        )

        dfUserContacts = (
            self.deltaLakeReader.read_table("db_bronze_sportsbook.accounts_usercontacts")
        )

        dfCurrenciesLookup = (
            self.deltaLakeReader.read_table("db_bronze_sportsbook.settings_currencies")
        )

        dfUserTypeLookup = (
            self.deltaLakeReader.read_table("db_bronze_sportsbook.accounts_usertype")
            .withColumnRenamed(existing="UserTypeID", new="IDUserType")
            .withColumnRenamed(existing="Name", new="UserTypeName")
        )

        dfUserStatusLookup = (
            self.deltaLakeReader.read_table("db_bronze_sportsbook.accounts_userstatus")
            .withColumnRenamed(existing="UserStatus", new="UserStatusName")
        )

        dfVerificationLevelsLookup = (
            self.deltaLakeReader.read_table("db_bronze_sportsbook.accounts_verificationlevels")
            .withColumnRenamed(existing="VerificationLevel", new="VerificationLevelName")
        )

        dfCountriesLookup = self.deltaLakeReader.read_table("db_bronze_sportsbook.settings_countries")

        dfUsers = dfUsers \
            .join(other=dfChannelUsers, on=["IDUser"], how="left") \
            .join(other=dfUserContacts, on=["IDUser"], how="left")

        dfUsers = (
            dfUsers.join(other=dfCurrenciesLookup, on=["IDCurrency"], how="left")
            .join(other=dfUserTypeLookup, on=["IDUserType"], how="left")
            .join(other=dfUserStatusLookup, on=["IDUserStatus"], how="left")
            .join(other=dfVerificationLevelsLookup, on=["IDVerificationLevel"], how="left")
            .join(other=dfCountriesLookup, on=["IDCountry"], how="left")
        )

        return dfUsers.select(
            "IDUser",
            "IDUserPlatform",
            "IDUserType",
            "UserTypeName",
            "IDUserStatus",
            "UserStatusName",
            "FirstName",
            "LastName",
            "UserName",
            "Email",
            "Gender",
            "BirthDateKey",
            "IDCurrency",
            "CurrencyName",
            "SubscriptionDateKey",
            "IDVerificationLevel",
            "VerificationLevelName",
            "StreetAddress",
            "Town",
            "ZipCode",
            "IDCountry",
            "CountryName",
            "Phone",
            "MobilePhone",
        )

    def get_users_finance_data(self) -> pyspark.sql.dataframe.DataFrame:
        dfUsersAccounts = self.dataLakeReader.read_path(DataLakePath.Tps.USER_ACCOUNTS)

        dfAvailableBalance = dfUsersAccounts.withColumn(
            "UpdatedOnKey", f.date_format(f.col("LastUpdatedOn"), "yyyyMMddhhmmss").cast(LongType())
        )

        windowUserId = Window.partitionBy("UserId")

        dfAvailableBalance = (
            dfAvailableBalance.withColumn("MaxUpdatedOnKey", f.max("UpdatedOnKey").over(windowUserId))
            .where(f.col("UpdatedOnKey") == f.col("MaxUpdatedOnKey"))
            .drop("MaxUpdatedOnKey")
        )

        dfAvailableBalance = dfAvailableBalance.groupBy("UserId").agg(
            f.sum("AvailableBalance").alias("AvailableBalanceTotal")
        )

        dfUsersFinance = dfAvailableBalance.withColumn("UserId", f.col("UserId").cast(StringType()))
        dfUsersFinance = dfUsersFinance.withColumn(
            "AvailableBalanceTotal",
            f.col("AvailableBalanceTotal").cast(DoubleType())
        )
        dfUsersFinance = dfUsersFinance.withColumnRenamed(existing="UserId", new="IDUserPlatform")

        return dfUsersFinance
