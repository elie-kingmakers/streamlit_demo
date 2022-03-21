from enum import Enum


class TransactionCategory(Enum):

    DEPOSIT = (1, "All Deposits")
    WITHDRAWAL = (2, "All Withdrawals")

    def __init__(self, transactionCategoryID: int, transactionCategoryName: str):
        self.transactionCategoryID = transactionCategoryID
        self.transactionCategoryName = transactionCategoryName
