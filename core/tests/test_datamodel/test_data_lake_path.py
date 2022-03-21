from datetime import datetime
from unittest import TestCase

from core.datamodel.data_lake_path import DataLakePath, RAPTOR_PATH


class TestDataLakePath(TestCase):
    def __init__(self, methodName="runTest"):
        super().__init__(methodName=methodName)

    def test_loose_filter_by_date_different_years(self):
        startDate = datetime.strptime("20210102", "%Y%m%d")
        endDate = datetime.strptime("20220102", "%Y%m%d")
        path = DataLakePath.Raptor.BET_ODDS.loose_filter_by_date(startDate=startDate, endDate=endDate)
        self.assertEqual(path.relativePath, f"{RAPTOR_PATH}/betodds/{{2021,2022}}/*/*/")

    def test_loose_filter_by_date_different_months(self):
        startDate = datetime.strptime("20210802", "%Y%m%d")
        endDate = datetime.strptime("20211102", "%Y%m%d")
        path = DataLakePath.Raptor.BET_ODDS.loose_filter_by_date(startDate=startDate, endDate=endDate)
        self.assertEqual(path.relativePath, f"{RAPTOR_PATH}/betodds/{{2021}}/{{0[8-9],1[0-1]}}/*/")

    def test_loose_filter_by_date_different_days(self):
        startDate = datetime.strptime("20211009", "%Y%m%d")
        endDate = datetime.strptime("20211021", "%Y%m%d")
        path = DataLakePath.Raptor.BET_ODDS.loose_filter_by_date(startDate=startDate, endDate=endDate)
        self.assertEqual(path.relativePath, f"{RAPTOR_PATH}/betodds/{{2021}}/10/{{09,1[0-9],2[0-1]}}/")

    def test_loose_filter_by_date_bad_dates(self):
        startDate = datetime.strptime("20211009", "%Y%m%d")
        endDate = datetime.strptime("20210821", "%Y%m%d")
        self.assertRaises(ValueError, DataLakePath.Raptor.BET_ODDS.loose_filter_by_date, startDate, endDate)
