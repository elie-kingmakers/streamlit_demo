from __future__ import annotations
from datetime import datetime
from itertools import groupby
from typing import List
from aenum import Enum, skip

RAPTOR_PATH = "raw/raptor"
RAPTOR_LOOKUP_PATH = "raw/raptor/lookups"

TPS_PATH = "raw/tps"
TPS_LOOKUP_PATH = "raw/tps/lookups"

VIRTUALS_PATH = "raw/virtuals"
VIRTUALS_LOOKUP_PATH = "raw/virtuals/lookups"


class DataLakePath(Enum):
    @skip
    class Raptor(Enum):

        COUPONS = ("bi-analytics", f"{RAPTOR_PATH}/betcoupons", "{year}/{month}/{day}/", "parquet")
        BET_ODDS = ("bi-analytics", f"{RAPTOR_PATH}/betodds", "{year}/{month}/{day}/", "parquet")
        SELECTIONS = ("bi-analytics", f"{RAPTOR_PATH}/selection", "{year}/{month}/{day}/", "parquet")
        EVENTS = ("bi-analytics", f"{RAPTOR_PATH}/events", "*", "parquet")
        MARKETS = ("bi-analytics", f"{RAPTOR_PATH}/markets", "{year}/{month}/{day}/", "parquet")

        USERS = ("bi-analytics", f"{RAPTOR_PATH}/users", "Raptor Users*", "parquet")
        CHANNEL_USERS = ("bi-analytics", f"{RAPTOR_PATH}/users", "Raptor ChannelUsers*", "parquet")
        USER_CONTACTS = ("bi-analytics", f"{RAPTOR_PATH}/users", "Raptor UserContacts*", "parquet")

        COUPON_ESTIMATES = ("bi-analytics", f"{RAPTOR_PATH}/raptor-or/dailycoupondetailestimates", "{year}/", "parquet")
        COUPON_DETAIL_ESTIMATES = (
            "bi-analytics",
            f"{RAPTOR_PATH}/raptor-or/dailycouponestimates",
            "{year}/",
            "parquet",
        )

        CATEGORY_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK Category*", "parquet")
        CHANNELS_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK Channels*", "parquet")
        CHANNEL_STATUS_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK ChannelStatuses*", "parquet")
        COUNTRIES_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK Countries*", "parquet")
        COUPON_SETTLEMENT_STATUS_LOOKUP = (
            "bi-analytics",
            f"{RAPTOR_LOOKUP_PATH}",
            "Raptor LK CouponSettlementStatus*",
            "parquet",
        )
        COUPON_STATUS_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK CouponStatus*", "parquet")
        COUPON_TYPES_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK CouponTypes*", "parquet")
        CURRENCIES_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK Currencies*", "parquet")
        EVAL_REASONS_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK EvalReasons*", "parquet")
        EVENT_CATEGORY_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK EventCategory*", "parquet")
        EVENT_STATUS_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK EventStatuses*", "parquet")
        EVENT_TYPE_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK EventTypes*", "parquet")
        MARKET_STATUSES_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK MarketStatuses*", "parquet")
        MARKET_TYPE_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK MarketTypes*", "parquet")
        MARKET_TYPE_STATUS_LOOKUP = (
            "bi-analytics",
            f"{RAPTOR_LOOKUP_PATH}",
            "Raptor LK MarketTypeStatuses*",
            "parquet",
        )
        ODDS_STATUS_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK OddStatuses*", "parquet")
        PLAY_SOURCES_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK PlaySources*", "parquet")
        SELECTION_STATUS_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK SelectionStatuses*", "parquet")
        SELECTION_TYPE_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK SelectionTypes*", "parquet")
        SPORTS_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK Sports*", "parquet")
        TEAMS_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK Teams*", "parquet")
        TEAM_TYPE_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK TeamTypes*", "parquet")
        TOURNAMENT_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK Tournament*", "parquet")
        USER_STATUS_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK UserStatus*", "parquet")
        USER_TYPE_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK UserType*", "parquet")
        USER_TYPES_LOOKUP = ("bi-analytics", f"{RAPTOR_LOOKUP_PATH}", "Raptor LK UserTypes*", "parquet")
        VERIFICATION_LEVELS_LOOKUP = (
            "bi-analytics",
            f"{RAPTOR_LOOKUP_PATH}",
            "Raptor LK VerificationLevels*",
            "parquet",
        )

        def __init__(self, containerName: str, folder: str, path: str, fileFormat: str):
            self.containerName = containerName
            self.folder = folder
            self.path = path
            self.fileFormat = fileFormat
            self.yearFilter = None
            self.monthFilter = None
            self.dayFilter = None

        @property
        def relativePath(self):
            concretePath = self.path.format(
                year=self.yearFilter or "*", month=self.monthFilter or "*", day=self.dayFilter or "*"
            )
            return f"{self.folder}/{concretePath}"

        @staticmethod
        def _get_spark_number_representation(integers: List[int]) -> str:
            paddedIntegers = [tuple(str(integer).zfill(2)) for integer in integers]
            groupedIntegers = groupby(paddedIntegers, lambda x: x[0])
            positionIdentifierInfo = []
            for position1Number, integersWithPosition1 in groupedIntegers:
                integersWithPosition1 = list(integersWithPosition1)
                position0Minimum = min((month[1] for month in integersWithPosition1))
                position0Maximum = max((month[1] for month in integersWithPosition1))
                positionIdentifierInfo.append((position1Number, position0Minimum, position0Maximum))
            individualPathReprs = [
                f"{position1Number}[{position0Min}-{position0Max}]"
                if position0Min != position0Max
                else f"{position1Number}{position0Min}"
                for position1Number, position0Min, position0Max in positionIdentifierInfo
            ]
            return f"{{{','.join(individualPathReprs)}}}"

        def loose_filter_by_date(self, startDate: datetime, endDate: datetime) -> DataLakePath:
            if startDate > endDate:
                raise ValueError("startDate cannot be later than end date")
            numYears = (endDate.year - startDate.year) + 1
            self.yearFilter = f"{{{','.join((str(year) for year in [startDate.year + i for i in range(numYears)]))}}}"
            numMonths = (endDate.month - startDate.month) + 1
            if numYears > 1:
                self.monthFilter = "*"
            else:
                if numMonths == 1:
                    self.monthFilter = str(startDate.month).zfill(2)
                else:
                    # This is weird because spark has trouble working out [03-12]
                    # it needs something like {0[3-9], 1[0-2]} in the file path instead
                    # https://dev.to/sridharanprasanna/using-wildcards-for-folder-path-with-spark-dataframe-load-4jo7
                    months = [startDate.month + i for i in range(numMonths)]
                    self.monthFilter = self._get_spark_number_representation(integers=months)
            if numYears > 1 or numMonths > 1:
                self.dayFilter = "*"
            else:
                numDays = (endDate.day - startDate.day) + 1
                days = [startDate.day + i for i in range(numDays)]
                self.dayFilter = self._get_spark_number_representation(integers=days)
            return self

    @skip
    class Tps(Enum):

        USER_ACCOUNTS = ("bi-analytics", f"{TPS_PATH}/useraccount", "{year}/{month}/{day}/", "parquet")
        TX_STORE = ("bi-analytics", f"{TPS_PATH}/txstore", "{year}/{month}/{day}/", "parquet")

        TRANSACTION_TYPES = ("bi-analytics", f"{TPS_LOOKUP_PATH}", "TPS LK TransactionType*", "parquet")
        TX_TYPE_CATEGORY = ("bi-analytics", f"{TPS_LOOKUP_PATH}", "TPS LK TxTypeTxCategory*", "parquet")
        TRANSACTION_CATEGORY = ("bi-analytics", f"{TPS_LOOKUP_PATH}", "TPS LK LK_TransactionCategory*", "parquet")

        def __init__(self, containerName: str, folder: str, path: str, fileFormat: str):
            self.containerName = containerName
            self.folder = folder
            self.path = path
            self.fileFormat = fileFormat
            self.yearFilter = None
            self.monthFilter = None
            self.dayFilter = None

        @property
        def relativePath(self):
            concretePath = self.path.format(
                year=self.yearFilter or "*", month=self.monthFilter or "*", day=self.dayFilter or "*"
            )
            return f"{self.folder}/{concretePath}"

        @staticmethod
        def _get_spark_number_representation(integers: List[int]) -> str:
            paddedIntegers = [tuple(str(integer).zfill(2)) for integer in integers]
            groupedIntegers = groupby(paddedIntegers, lambda x: x[0])
            positionIdentifierInfo = []
            for position1Number, integersWithPosition1 in groupedIntegers:
                integersWithPosition1 = list(integersWithPosition1)
                position0Minimum = min((month[1] for month in integersWithPosition1))
                position0Maximum = max((month[1] for month in integersWithPosition1))
                positionIdentifierInfo.append((position1Number, position0Minimum, position0Maximum))
            individualPathReprs = [
                f"{position1Number}[{position0Min}-{position0Max}]"
                if position0Min != position0Max
                else f"{position1Number}{position0Min}"
                for position1Number, position0Min, position0Max in positionIdentifierInfo
            ]
            return f"{{{','.join(individualPathReprs)}}}"

        def loose_filter_by_date(self, startDate: datetime, endDate: datetime) -> DataLakePath:
            if startDate > endDate:
                raise ValueError("startDate cannot be later than end date")
            numYears = (endDate.year - startDate.year) + 1
            self.yearFilter = f"{{{','.join((str(year) for year in [startDate.year + i for i in range(numYears)]))}}}"
            numMonths = (endDate.month - startDate.month) + 1
            if numYears > 1:
                self.monthFilter = "*"
            else:
                if numMonths == 1:
                    self.monthFilter = str(startDate.month).zfill(2)
                else:
                    # This is weird because spark has trouble working out [03-12]
                    # it needs something like {0[3-9], 1[0-2]} in the file path instead
                    # https://dev.to/sridharanprasanna/using-wildcards-for-folder-path-with-spark-dataframe-load-4jo7
                    months = [startDate.month + i for i in range(numMonths)]
                    self.monthFilter = self._get_spark_number_representation(integers=months)
            if numYears > 1 or numMonths > 1:
                self.dayFilter = "*"
            else:
                numDays = (endDate.day - startDate.day) + 1
                days = [startDate.day + i for i in range(numDays)]
                self.dayFilter = self._get_spark_number_representation(integers=days)
            return self

    @skip
    class Virtuals(Enum):
        def __init__(self, containerName: str, folder: str, path: str, fileFormat: str):
            self.containerName = containerName
            self.folder = folder
            self.path = path
            self.fileFormat = fileFormat
            self.yearFilter = None
            self.monthFilter = None
            self.dayFilter = None

        @property
        def relativePath(self):
            concretePath = self.path.format(
                year=self.yearFilter or "*", month=self.monthFilter or "*", day=self.dayFilter or "*"
            )
            return f"{self.folder}/{concretePath}"

        @staticmethod
        def _get_spark_number_representation(integers: List[int]) -> str:
            paddedIntegers = [tuple(str(integer).zfill(2)) for integer in integers]
            groupedIntegers = groupby(paddedIntegers, lambda x: x[0])
            positionIdentifierInfo = []
            for position1Number, integersWithPosition1 in groupedIntegers:
                integersWithPosition1 = list(integersWithPosition1)
                position0Minimum = min((month[1] for month in integersWithPosition1))
                position0Maximum = max((month[1] for month in integersWithPosition1))
                positionIdentifierInfo.append((position1Number, position0Minimum, position0Maximum))
            individualPathReprs = [
                f"{position1Number}[{position0Min}-{position0Max}]"
                if position0Min != position0Max
                else f"{position1Number}{position0Min}"
                for position1Number, position0Min, position0Max in positionIdentifierInfo
            ]
            return f"{{{','.join(individualPathReprs)}}}"

        def loose_filter_by_date(self, startDate: datetime, endDate: datetime) -> DataLakePath:
            if startDate > endDate:
                raise ValueError("startDate cannot be later than end date")
            numYears = (endDate.year - startDate.year) + 1
            self.yearFilter = f"{{{','.join((str(year) for year in [startDate.year + i for i in range(numYears)]))}}}"
            numMonths = (endDate.month - startDate.month) + 1
            if numYears > 1:
                self.monthFilter = "*"
            else:
                if numMonths == 1:
                    self.monthFilter = str(startDate.month).zfill(2)
                else:
                    # This is weird because spark has trouble working out [03-12]
                    # it needs something like {0[3-9], 1[0-2]} in the file path instead
                    # https://dev.to/sridharanprasanna/using-wildcards-for-folder-path-with-spark-dataframe-load-4jo7
                    months = [startDate.month + i for i in range(numMonths)]
                    self.monthFilter = self._get_spark_number_representation(integers=months)
            if numYears > 1 or numMonths > 1:
                self.dayFilter = "*"
            else:
                numDays = (endDate.day - startDate.day) + 1
                days = [startDate.day + i for i in range(numDays)]
                self.dayFilter = self._get_spark_number_representation(integers=days)
            return self

    @skip
    class DataScience(Enum):

        # Note: cannot use * in path when reading files in delta format

        COUPONS_BRONZE = (
            "datascience",
            "datascience/customer_profiling/bronze/coupons",
            "{year}/{month}/{day}/",
            "parquet",
        )
        COUPONS_SILVER = ("datascience", "datascience/customer_profiling/silver/coupons", "", "delta")
        CUSTOMERS_GOLD = ("datascience", "datascience/customer_profiling/gold/customers", "", "delta")

        def __init__(self, containerName: str, folder: str, path: str, fileFormat: str):
            self.containerName = containerName
            self.folder = folder
            self.path = path
            self.fileFormat = fileFormat
            self.yearFilter = None
            self.monthFilter = None
            self.dayFilter = None

        @property
        def relativePath(self):
            concretePath = self.path.format(
                year=self.yearFilter or "*", month=self.monthFilter or "*", day=self.dayFilter or "*"
            )
            return f"{self.folder}/{concretePath}"

        @staticmethod
        def _get_spark_number_representation(integers: List[int]) -> str:
            paddedIntegers = [tuple(str(integer).zfill(2)) for integer in integers]
            groupedIntegers = groupby(paddedIntegers, lambda x: x[0])
            positionIdentifierInfo = []
            for position1Number, integersWithPosition1 in groupedIntegers:
                integersWithPosition1 = list(integersWithPosition1)
                position0Minimum = min((month[1] for month in integersWithPosition1))
                position0Maximum = max((month[1] for month in integersWithPosition1))
                positionIdentifierInfo.append((position1Number, position0Minimum, position0Maximum))
            individualPathReprs = [
                f"{position1Number}[{position0Min}-{position0Max}]"
                if position0Min != position0Max
                else f"{position1Number}{position0Min}"
                for position1Number, position0Min, position0Max in positionIdentifierInfo
            ]
            return f"{{{','.join(individualPathReprs)}}}"

        def loose_filter_by_date(self, startDate: datetime, endDate: datetime) -> DataLakePath:
            if startDate > endDate:
                raise ValueError("startDate cannot be later than end date")
            numYears = (endDate.year - startDate.year) + 1
            self.yearFilter = f"{{{','.join((str(year) for year in [startDate.year + i for i in range(numYears)]))}}}"
            numMonths = (endDate.month - startDate.month) + 1
            if numYears > 1:
                self.monthFilter = "*"
            else:
                if numMonths == 1:
                    self.monthFilter = str(startDate.month).zfill(2)
                else:
                    # This is weird because spark has trouble working out [03-12]
                    # it needs something like {0[3-9], 1[0-2]} in the file path instead
                    # https://dev.to/sridharanprasanna/using-wildcards-for-folder-path-with-spark-dataframe-load-4jo7
                    months = [startDate.month + i for i in range(numMonths)]
                    self.monthFilter = self._get_spark_number_representation(integers=months)
            if numYears > 1 or numMonths > 1:
                self.dayFilter = "*"
            else:
                numDays = (endDate.day - startDate.day) + 1
                days = [startDate.day + i for i in range(numDays)]
                self.dayFilter = self._get_spark_number_representation(integers=days)
            return self
