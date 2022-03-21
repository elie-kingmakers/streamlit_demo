from enum import Enum


class Brand(Enum):

    NIGERIA = (1901, "Nigeria", "NGN", 36)
    ETHIOPIA = (1902, "Ethiopia", "ETB", 37)
    KENYA = (1903, "Kenya", "KES", 38)

    def __init__(self, brandId: int, brandName: str, currencyName: str, betagyChannelId: int):
        self.brandId = brandId
        self.brandName = brandName
        self.currencyName = currencyName
        self.betagyChannelId = betagyChannelId
