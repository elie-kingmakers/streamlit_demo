import pyspark.sql
import pyspark.sql.functions as f
from pyspark.sql import Window
from pyspark.sql.types import LongType
from datetime import datetime

from core.datamodel.data_lake_path import DataLakePath
from core.store.data_lake_reader import DataLakeReader


class DataLakeRetriever:
    def __init__(self, dataLakeReader: DataLakeReader):
        self.dataLakeReader = dataLakeReader

    def get_selections_view(self, startDate: datetime, endDate: datetime) -> pyspark.sql.dataframe.DataFrame:
        selectionsPath = DataLakePath.Raptor.SELECTIONS.loose_filter_by_date(startDate=startDate, endDate=endDate)
        dfSelections = (
            self.dataLakeReader.read_path(dataLakePath=selectionsPath)
            .select(
                "SelectionId",
                "MarketId",
                "SelectionStatusId",
                "MarketTypeId",
                "SelectionTypeId",
                "SelectionSpread",
                "ForcedStatus",
            )
            .dropDuplicates()
        )

        marketsPath = DataLakePath.Raptor.MARKETS.loose_filter_by_date(startDate=startDate, endDate=endDate)
        dfMarkets = (
            self.dataLakeReader.read_path(dataLakePath=marketsPath)
            .select("MarketId", "MarketTypeId", "Spread")
            .dropDuplicates()
        )

        return dfSelections.join(other=dfMarkets, on=["MarketId", "MarketTypeId"])

    def get_coupons_view(self, startDate: datetime, endDate: datetime) -> pyspark.sql.dataframe.DataFrame:
        couponsPath = DataLakePath.Raptor.COUPONS.loose_filter_by_date(startDate=startDate, endDate=endDate)
        dfCoupons = (
            self.dataLakeReader.read_path(dataLakePath=couponsPath)
            .select(
                "CouponId",
                "CouponCode",
                "CouponDateKeyUTC",
                "SettlementDateKeyUTC",
                "Stake",
                "MaxWin",
                "MinWin",
                "TotalCombinations",
                "CouponStatusId",
                "CoutonTypeId",
                "UserId",
                "Won",
                "Bonus",
                "WonCombinations",
                "NumberOfSelections",
                "IsLive",
                "CurrencyId",
                "EvalReasonId",
                "ChannelId",
                "BrandId",
                "PlaySourceId",
                "PlacementExchangeRate",
                "SettlementExchangeRate",
                "SettlementStatusId",
                "ClientIP",
                "Domain",
            )
            .withColumnRenamed(existing="CoutonTypeId", new="CouponTypeId")
            .withColumnRenamed(existing="Won", new="CouponReturn")
            .dropDuplicates()
        )

        dfCoupons = dfCoupons.filter(dfCoupons["SettlementDateKeyUTC"] >= int(startDate.strftime("%Y%m%d"))).filter(
            dfCoupons["SettlementDateKeyUTC"] <= int(endDate.strftime("%Y%m%d"))
        )

        betOddsPath = DataLakePath.Raptor.BET_ODDS.loose_filter_by_date(startDate=startDate, endDate=endDate)
        dfBetOdds = (
            self.dataLakeReader.read_path(dataLakePath=betOddsPath)
            .select("CouponId", "EventId", "OddValue", "Banker", "SelectionId", "BetOddStatusId", "EventCategory")
            .dropDuplicates()
        )

        dfSelections = self.get_selections_view(startDate=startDate, endDate=endDate)

        eventsPath = DataLakePath.Raptor.EVENTS.loose_filter_by_date(startDate=startDate, endDate=endDate)
        dfEvents = (
            self.dataLakeReader.read_path(dataLakePath=eventsPath)
            .select("EventId", "SportId", "EventName", "MPath")
            .dropDuplicates()
        )

        return (
            dfCoupons.join(other=dfBetOdds, on=["CouponId"])
            .join(other=dfEvents, on=["EventId"], how="left")
            .join(other=dfSelections, on=["SelectionId"], how="left")
        )

    def get_users_info(self) -> pyspark.sql.dataframe.DataFrame:
        dfUsers = (
            self.dataLakeReader.read_path(DataLakePath.Raptor.USERS)
            .withColumnRenamed(existing="IDUser", new="UserId")
            .withColumnRenamed(existing="IDUserType", new="UserTypeId")
            .withColumnRenamed(existing="IDUserStatus", new="UserStatusId")
            .withColumnRenamed(existing="IDCurrency", new="UserCurrencyId")
            .withColumnRenamed(existing="IDVerificationLevel", new="VerificationLevelId")
            .withColumnRenamed(existing="IDChannel", new="ChannelId")
        )

        dfUsers = dfUsers.withColumn(
            "BirthDateKeyUTC", f.date_format(f.col("BirthDate"), "yyyyMMdd").cast(LongType())
        ).withColumn("SubscriptionDateKeyUTC", f.date_format(f.col("SubscriptionDate"), "yyyyMMdd").cast(LongType()))

        dfChannelUsers = (
            self.dataLakeReader.read_path(DataLakePath.Raptor.CHANNEL_USERS)
            .withColumnRenamed(existing="IDUser", new="UserId")
            .withColumnRenamed(existing="ExternalIdUser", new="PlatformUserId")
        )

        dfUserContacts = (
            self.dataLakeReader.read_path(DataLakePath.Raptor.USER_CONTACTS)
            .withColumnRenamed(existing="IDUser", new="UserId")
            .withColumnRenamed(existing="IDCountry", new="CountryId")
        )

        dfCurrenciesLookup = (
            self.dataLakeReader.read_path(DataLakePath.Raptor.CURRENCIES_LOOKUP)
            .withColumnRenamed(existing="IDCurrency", new="UserCurrencyId")
            .withColumnRenamed(existing="CurrencyName", new="UserCurrencyName")
        )

        dfUserTypeLookup = (
            self.dataLakeReader.read_path(DataLakePath.Raptor.USER_TYPE_LOOKUP)
            .withColumnRenamed(existing="UserTypeID", new="UserTypeId")
            .withColumnRenamed(existing="Name", new="UserTypeName")
        )

        dfUserStatusLookup = (
            self.dataLakeReader.read_path(DataLakePath.Raptor.USER_STATUS_LOOKUP)
            .withColumnRenamed(existing="IDUserStatus", new="UserStatusId")
            .withColumnRenamed(existing="UserStatus", new="UserStatusName")
        )

        dfVerificationLevelsLookup = (
            self.dataLakeReader.read_path(DataLakePath.Raptor.VERIFICATION_LEVELS_LOOKUP)
            .withColumnRenamed(existing="IDVerificationLevel", new="VerificationLevelId")
            .withColumnRenamed(existing="VerificationLevel", new="VerificationLevelName")
        )

        dfCountriesLookup = self.dataLakeReader.read_path(DataLakePath.Raptor.COUNTRIES_LOOKUP).withColumnRenamed(
            existing="IDCountry", new="CountryId"
        )

        dfUsers = dfUsers.join(other=dfChannelUsers, on=["UserId"], how="left").join(
            other=dfUserContacts, on=["UserId"], how="left"
        )

        dfUsers = (
            dfUsers.join(other=dfCurrenciesLookup, on=["UserCurrencyId"], how="left")
            .join(other=dfUserTypeLookup, on=["UserTypeId"], how="left")
            .join(other=dfUserStatusLookup, on=["UserStatusId"], how="left")
            .join(other=dfVerificationLevelsLookup, on=["VerificationLevelId"], how="left")
            .join(other=dfCountriesLookup, on=["CountryId"], how="left")
        )

        return dfUsers.select(
            "UserId",
            "PlatformUserId",
            "UserTypeId",
            "UserTypeName",
            "UserStatusId",
            "UserStatusName",
            "FirstName",
            "LastName",
            "UserName",
            "Email",
            "Gender",
            "BirthDateKeyUTC",
            "UserCurrencyId",
            "UserCurrencyName",
            "SubscriptionDateKeyUTC",
            "VerificationLevelId",
            "VerificationLevelName",
            "StreetAddress",
            "Town",
            "ZipCode",
            "CountryId",
            "CountryName",
            "Phone",
            "MobilePhone",
        )

    def get_users_finance_data(self) -> pyspark.sql.dataframe.DataFrame:
        dfUsersAccounts = self.dataLakeReader.read_path(DataLakePath.Tps.USER_ACCOUNTS)

        dfAvailableBalance = dfUsersAccounts.withColumn(
            "UpdatedOnKeyUTC", f.date_format(f.col("LastUpdatedOnUTC"), "yyyyMMddhhmmss").cast(LongType())
        )

        windowUserId = Window.partitionBy("UserId")

        dfAvailableBalance = (
            dfAvailableBalance.withColumn("MaxUpdatedOnKeyUTC", f.max("UpdatedOnKeyUTC").over(windowUserId))
            .where(f.col("UpdatedOnKeyUTC") == f.col("MaxUpdatedOnKeyUTC"))
            .drop("MaxUpdatedOnKeyUTC")
        )

        dfAvailableBalance = dfAvailableBalance.groupBy("UserId").agg(
            f.sum("AvailableBalance").alias("AvailableBalanceTotal")
        )

        dfUsersFinance = dfAvailableBalance

        return dfUsersFinance
