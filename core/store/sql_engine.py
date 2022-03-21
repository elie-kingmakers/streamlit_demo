# pylint: disable=I1101

import pandas as pd
import pyodbc

from core.utils.retry_decorator import retry

pyodbc.pooling = False


class SQLEngine:
    def __init__(
        self, server: str, database: str, username: str, password: str, verbose: bool = False, readOnly: bool = True
    ):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.verbose = verbose
        self.tableIndexes = None
        self.readOnly = readOnly

    def _get_connection(self) -> pyodbc.Connection:
        connection = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"
        )
        if self.readOnly:
            connection.execute("SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;")
        return connection

    @staticmethod
    def _get_cursor(connection: pyodbc.Connection) -> pyodbc.Cursor:
        return connection.cursor()

    def run_iterative_query(self, query: str) -> iter:
        if self.verbose:
            print(query)
        with self._get_connection() as connection:
            cursor = self._get_cursor(connection=connection)
            return cursor.execute(query)

    def run_query(self, query: str) -> pd.DataFrame:
        # TODO(Mike): figure out how to pass parameters in better way, rather than string formatting query
        if self.verbose:
            print(query)
        with self._get_connection() as connection:
            with self._get_cursor(connection=connection) as cursor:
                results = cursor.execute(query).fetchall()
                columns = [column[0] for column in cursor.description]
                return pd.DataFrame([dict(zip(columns, row)) for row in results])

    def run_statement(self, statement: str):
        # Runs sql statements rather than a query returning a table.
        if self.verbose:
            print(statement)
        with self._get_connection() as connection:
            with self._get_cursor(connection=connection) as cursor:
                cursor.execute(statement)

    @retry(numRetries=5, retryDelaySeconds=3, backoffScalingFactor=2)
    def run_query_with_retry(self, query: str) -> pd.DataFrame:
        if self.verbose:
            print(query)
        return self.run_query(query=query)

    def _populate_table_index_lookup(self) -> None:
        self.tableIndexes = self.run_query(
            query="""
                SELECT
                    schemas.name as schemaName,
                    tables.name as tableName,
                    indexes.name as indexName,
                    indexes.index_id as indexId,
                    indexColumns.index_column_id as columnId,
                    columns.name as columnName,
                    indexes.*,
                    indexColumns.*,
                    columns.*
                FROM
                    sys.indexes indexes
                INNER JOIN
                    sys.index_columns indexColumns ON
                        indexes.object_id = indexColumns.object_id AND
                        indexes.index_id = indexColumns.index_id
                INNER JOIN
                    sys.columns columns ON
                        indexColumns.object_id = columns.object_id AND
                        indexColumns.column_id = columns.column_id
                INNER JOIN
                    sys.tables tables ON indexes.object_id = tables.object_id
                INNER JOIN
                    sys.schemas schemas ON tables.schema_id = schemas.schema_id
                WHERE
                    indexes.is_primary_key = 0 AND
                    indexes.is_unique = 0 AND
                    indexes.is_unique_constraint = 0 AND
                    tables.is_ms_shipped = 0
                ORDER BY
                     tables.name, indexes.name, indexes.index_id, indexColumns.is_included_column, indexColumns.key_ordinal;
            """
        )

    def lookup_table_indexes(self, tableName: str) -> pd.DataFrame:
        if self.tableIndexes is None:
            self._populate_table_index_lookup()
        return self.tableIndexes[[tableName in v for v in self.tableIndexes["tableName"]]].reset_index(drop=True)

    def get_tables(self) -> pd.DataFrame:
        return self.run_query(
            query="""
                SELECT
                    schema_name(tables.schema_id) AS schemaName,
                    tables.name AS tableName
                FROM
                    sys.tables AS tables
                JOIN
                    sys.schemas schemas ON tables.schema_id = schemas.schema_id
                ORDER BY
                    schemaName, tableName;
            """
        )
