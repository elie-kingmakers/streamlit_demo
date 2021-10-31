import pandas

from pydantic import BaseModel
from typing import ClassVar

class CustomersData(BaseModel):

    dataPath: ClassVar[str] = 'customer_data_sample.csv'

    @staticmethod
    def load_data():
        data = pandas.read_csv(CustomersData.dataPath)
        return data

    @staticmethod
    def get_customer_data(df, userId):
        customerData = df.loc[df['UserId'] == userId]
        return customerData


















