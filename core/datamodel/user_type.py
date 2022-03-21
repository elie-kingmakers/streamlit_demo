from enum import Enum


class UserType(Enum):

    ONLINE = (2, "Online Player")
    SUB_ACCOUNT = (3, "Sub-Account Player")
    SHOP_OWNER = (49, "Shop Owner")
    CASHIER = (50, "Cashier")

    def __init__(self, userTypeId: int, userTypeName: str):
        self.userTypeId = userTypeId
        self.userTypeName = userTypeName
