import pandas
from pydantic import BaseModel, validator

class CustomersData(BaseModel):

    dataPath: str = 'customer_data_sample.csv'

    def load_data_pandas(self):
        data = pandas.read_csv(self.dataPath)
        return data

    def load_data(self):
        return self.load_data_pandas()

    def get_customer_data(self, df, userId):
        customerData = df.loc[df['UserId'] == userId]
        return customerData


















