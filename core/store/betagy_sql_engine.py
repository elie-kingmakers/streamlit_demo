from typing import List, Set

from core.store.sql_engine import SQLEngine


class BetagySQLEngine(SQLEngine):
    def __init__(self, password: str, isVirtuals: bool = False, verbose: bool = False):
        self.isVirtuals = isVirtuals
        super().__init__(
            server="10.5.5.5,52002",
            database="Virtuals" if isVirtuals else "Raptor",
            username="BetkingAnalytics",
            password=password,
            verbose=verbose,
        )

    @staticmethod
    def _get_all_coupons_and_odds_query(couponReturnColumns: List[str], oddsReturnColumns: List[str]) -> str:
        returnColumnSeparator = ",\n\t\t"
        archiveCouponReturnColumns = f"{returnColumnSeparator}".join(
            [f"archiveCoupons.{col}" for col in couponReturnColumns]
        )
        archiveOddsReturnColumns = f"{returnColumnSeparator}".join([f"archiveOdds.{col}" for col in oddsReturnColumns])
        recentCouponReturnColumns = f"{returnColumnSeparator}".join(
            [f"recentCoupons.{col}" for col in couponReturnColumns]
        )
        recentOddsReturnColumns = f"{returnColumnSeparator}".join([f"recentOdds.{col}" for col in oddsReturnColumns])

        return f"""
            SELECT
                {archiveCouponReturnColumns}
                {f',{archiveOddsReturnColumns}' if len(oddsReturnColumns) > 0 else ''}
            FROM
                [Archive.Bets].Coupons AS archiveCoupons
            INNER JOIN
                [Archive.Bets].BetOdds AS archiveOdds ON archiveCoupons.IDCoupon = archiveOdds.IDCoupon
            UNION ALL
            SELECT
                {recentCouponReturnColumns}
                {f',{recentOddsReturnColumns}' if len(oddsReturnColumns) > 0 else ''}
            FROM
                Bets.Coupons AS recentCoupons
            INNER JOIN
                Bets.BetOdds AS recentOdds ON recentCoupons.IDCoupon = recentOdds.IDCoupon
        """

    def _get_table_columns(self, schema: str, tableName: str) -> Set[str]:
        columns = self.run_query(
            query=f"""
                SELECT
                    column_name
                FROM
                    information_schema.columns
               WHERE
                   table_schema = '{schema}' AND
                   table_name = '{tableName}'
            """
        )
        return set(columns["column_name"])

    def get_merged_archive_and_recent_tables_query(self, schema: str, tableName: str) -> str:
        archiveTableSchema = f"Archive.{schema}"
        cacheTableColumns = self._get_table_columns(schema=schema, tableName=tableName)
        archiveTableColumns = self._get_table_columns(schema=archiveTableSchema, tableName=tableName)
        columnsInBothSchema = cacheTableColumns.intersection(archiveTableColumns)
        columnStringRepresentation = ", ".join((v for v in columnsInBothSchema))
        return f"""
            SELECT
                {columnStringRepresentation}
            FROM
                {schema}.{tableName}
            UNION ALL
            SELECT
                {columnStringRepresentation}
            FROM
                [{archiveTableSchema}].{tableName}
        """
