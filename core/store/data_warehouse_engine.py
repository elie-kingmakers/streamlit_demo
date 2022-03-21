from core.store.sql_engine import SQLEngine


class DataWarehouseEngine(SQLEngine):
    def __init__(self, password: str, username: str = "DSDev", verbose: bool = False):
        super().__init__(
            server="bkng-it-enterprisedw.database.windows.net",
            database="BKNG-EnterpriseDW",
            username=username,
            password=password,
            verbose=verbose,
        )
