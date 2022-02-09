import streamlit as st
import pandas as pd
from databricks_api import DatabricksAPI
import base64
import io
from tqdm import tqdm


db = DatabricksAPI(
    host=st.secrets["DATABRICKS_HOST"],
    token=st.secrets["DATABRICKS_TOKEN"]
)


#***********************************************************************************************************************
#***********************************************************************************************************************
st.title('Customer Profiling')


def read_large_parquet_file_using_dbfs_api(filePathDbfs: str) -> pd.DataFrame:
    parquetBytes = b''

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
            parquetDict = db.dbfs.read(filePathDbfs, offset=readOffset, length=readLength)
            parquetStringEncoded = parquetDict["data"]
            parquetBytesDecoded = base64.b64decode(parquetStringEncoded)
            parquetBytes += parquetBytesDecoded

        except Exception as e:
            print("End of File Reached!")
            readingBytes = False
            break

    parquetFile = io.BytesIO(parquetBytes)
    df = pd.read_parquet(parquetFile)
    return df


def read_coalesced_parquet_file(folderPathDbfs: str) -> pd.DataFrame:
    files = db.dbfs.list(folderPathDbfs)['files']

    numberOfParquetFiles = len([file for file in files if str(file['path']).endswith('.parquet')])

    if numberOfParquetFiles != 1:
        raise FileExistsError("Error: Number of parquet files = {}. Coalesce these files to get only 1 parquet file.".format(numberOfParquetFiles))

    for file in files:
        filePath: str = file['path']

        if filePath.endswith('.parquet'):
            df = read_large_parquet_file_using_dbfs_api(filePathDbfs=filePath)
            return df


with st.spinner("Loading Customers Table..."):
    dfCustomers = read_coalesced_parquet_file('dbfs:/mnt/datascience/customer_profiling/gold/customers_coalesced')
st.success("Customers Table Loaded Successfully!")

st.write(dfCustomers)









