from typing import ClassVar

import pandas as pd
import streamlit as st
from pydantic import BaseModel

from core.store.databricks_api_engine import DatabricksApiEngine
from datamodel.columns import Columns


class CustomerDataRetriever(BaseModel):
    dbEngine: ClassVar[DatabricksApiEngine] = DatabricksApiEngine(
        hostName=st.secrets["DATABRICKS_HOST"], password=st.secrets["DATABRICKS_TOKEN"]
    )

    # customersGoldPathDbfs: ClassVar[str] = "dbfs:/mnt/dsworkspace/customer_profiling/gold/customers_coalesced"
    userPlatformIdsRangesPathDbfs: ClassVar[str] = "dbfs:/mnt/dsworkspace/customer_profiling/lookups/userplatformids_ranges"
    customersSplitsPathDbfs: ClassVar[str] = "dbfs:/mnt/dsworkspace/customer_profiling/gold/customers_splits"

    @staticmethod
    def load_userplatformids_ranges() -> pd.DataFrame:
        dfUserPlatformIdsRanges = CustomerDataRetriever.dbEngine.read_coalesced_parquet_file(
            folderPathDbfs=CustomerDataRetriever.userPlatformIdsRangesPathDbfs
        )
        return dfUserPlatformIdsRanges

    @staticmethod
    def load_customer_data(userPlatformId: str) -> pd.DataFrame:

        # load table with current ranges of userId
        dfUserPlatformIdsRanges = CustomerDataRetriever.load_userplatformids_ranges()

        userPlatformIdsFrom = dfUserPlatformIdsRanges['UserPlatformIdFrom'].tolist()
        userPlatformIdsTo = dfUserPlatformIdsRanges['UserPlatformIdTo'].tolist()

        rangeIndex = -1

        # find range of userId
        for i in range(0, len(userPlatformIdsFrom)):
            if (int(userPlatformId) >= userPlatformIdsFrom[i]) and (int(userPlatformId) < userPlatformIdsTo[i]):
                rangeIndex = i
                break

        if rangeIndex == -1:
            raise ValueError("UserPlatformId not in any range of UserPlatformIdsSplits")

        customersSplitsTableName = f"{CustomerDataRetriever.customersSplitsPathDbfs}/{userPlatformIdsFrom[rangeIndex]}_{userPlatformIdsTo[rangeIndex]}"

        # load the corresponding customers split table that contains info about userId of customer
        dfCustomers = CustomerDataRetriever.dbEngine.read_coalesced_parquet_file(
            folderPathDbfs=customersSplitsTableName
        )

        # filter customers split table to get customer data
        dfUser = dfCustomers[dfCustomers[Columns.CustomerData.USER_PLATFORM_ID] == int(userPlatformId)]
        return dfUser




    # @staticmethod
    # def load_data() -> pd.DataFrame:
    #     dfCustomers = CustomerDataRetriever.dbEngine.read_coalesced_parquet_file(
    #         folderPathDbfs=CustomerDataRetriever.customersGoldPathDbfs
    #     )
    #     return dfCustomers
    #
    # @staticmethod
    # def get_user_data_from_user_id(dfCustomers: pd.DataFrame, userId: int) -> pd.DataFrame:
    #     dfUser = dfCustomers[dfCustomers[Columns.CustomerData.USER_ID] == int(userId)]
    #     return dfUser
    #
    # @staticmethod
    # def get_user_data_from_platform_id(dfCustomers: pd.DataFrame, platformUserId: str) -> pd.DataFrame:
    #     dfUser = dfCustomers[dfCustomers[Columns.CustomerData.PLATFORM_USER_ID] == str(platformUserId)]
    #     return dfUser

