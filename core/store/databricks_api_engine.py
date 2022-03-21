import pandas as pd
import base64
import io
from databricks_api import DatabricksAPI
from tqdm import tqdm


class DatabricksApiEngine:
    def __init__(self, hostName: str, password: str):
        self.db = DatabricksAPI(host=hostName, token=password)

    def read_large_parquet_file(self, filePathDbfs: str) -> pd.DataFrame:
        parquetBytes = b""

        def generator():
            while True:
                yield

        readIterations = 0

        for _ in tqdm(generator()):
            # max read length using dbfs api is ~1MB
            readLength = 1000000
            readOffset = readIterations * readLength
            readIterations += 1

            try:
                parquetDict = self.db.dbfs.read(filePathDbfs, offset=readOffset, length=readLength)
                parquetStringEncoded = parquetDict["data"]
                parquetBytesDecoded = base64.b64decode(parquetStringEncoded)
                parquetBytes += parquetBytesDecoded

            except Exception:
                print(" End of File Reached! ")
                break

        parquetFile = io.BytesIO(parquetBytes)
        df = pd.read_parquet(parquetFile)
        return df

    def read_coalesced_parquet_file(self, folderPathDbfs: str) -> pd.DataFrame:
        files = self.db.dbfs.list(folderPathDbfs)["files"]

        numberOfParquetFiles = len([file for file in files if str(file["path"]).endswith(".parquet")])

        if numberOfParquetFiles != 1:
            raise FileExistsError(
                "Error: Number of parquet files = {}. Coalesce these files to get only 1 parquet file.".format(
                    numberOfParquetFiles
                )
            )

        for file in files:
            filePath: str = file["path"]

            if filePath.endswith(".parquet"):
                df = self.read_large_parquet_file(filePathDbfs=filePath)
                return df
