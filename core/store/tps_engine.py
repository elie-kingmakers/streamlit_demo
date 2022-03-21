from datetime import datetime
from typing import Iterable

import pandas as pd

from core.datamodel.brand import Brand
from core.datamodel.user_type import UserType
from core.store.sql_engine import SQLEngine


class TPSEngine(SQLEngine):
    def __init__(self, password: str, verbose: bool = False):
        super().__init__(
            server="10.5.5.4,51001",
            database="TPS",
            username="BetkingAnalytics",
            password=password,
            verbose=verbose,
        )

    def get_transactions(
        self,
        userType: UserType,
        brand: Brand,
        dateFrom: datetime,
        dateTo: datetime,
        transactionTypeIds: Iterable[int],
    ) -> pd.DataFrame:
        results = self.run_query(
            query=f"""
                SELECT
                    txStore.UserId,
                    users.ParentId,
                    txStore.CreatedOn,
                    txStore.TxTypeId,
                    txStore.Amount,
                    txStore.BalanceAfterTx,
                    txStore.UserTypeId,
                    txStore.UserCurrencyCode,
                    txStore.BrandId
                FROM
                    [TPS-OR].Analysis.TxStore txStore
                LEFT JOIN
                    TPS.Users.[User] users ON
                        txStore.UserId = users.Id
                WHERE
                    txStore.IsTest = 0 AND
                    txStore.TxStatusId IN (400, 500) AND
                    txStore.TxTypeId IN ({', '.join((str(v) for v in transactionTypeIds))}) AND
                    txStore.UserTypeId = {userType.userTypeId} AND
                    txStore.BrandId = {brand.brandId} AND
                    txStore.CreatedOnKey >= '{dateFrom.strftime('%Y%m%d')}' AND
                    txStore.CreatedOnKey <= '{dateTo.strftime('%Y%m%d')}'
            """
        )
        if len(results) > 0:
            results["Amount"] = results["Amount"].astype("float")
            results["BalanceAfterTx"] = results["BalanceAfterTx"].astype("float")
        return results
