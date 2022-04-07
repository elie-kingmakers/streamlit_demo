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

    customersGoldPathDbfs: ClassVar[str] = "dbfs:/mnt/datascience/customer_profiling/gold/customers_coalesced"

    @staticmethod
    def load_data() -> pd.DataFrame:
        dfCustomers = CustomerDataRetriever.dbEngine.read_coalesced_parquet_file(
            folderPathDbfs=CustomerDataRetriever.customersGoldPathDbfs
        )
        return dfCustomers

    @staticmethod
    def get_user_data_from_user_id(dfCustomers: pd.DataFrame, userId: int) -> pd.DataFrame:
        dfUser = dfCustomers[dfCustomers[Columns.CustomerData.USER_ID] == int(userId)]
        return dfUser

    @staticmethod
    def get_user_data_from_platform_id(dfCustomers: pd.DataFrame, platformUserId: str) -> pd.DataFrame:
        dfUser = dfCustomers[dfCustomers[Columns.CustomerData.PLATFORM_USER_ID] == str(platformUserId)]
        return dfUser


