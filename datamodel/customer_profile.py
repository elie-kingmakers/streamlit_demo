from pydantic import BaseModel, validator

class CustomerProfile(BaseModel):
    userId: int
    averageOddValuePerSelection: float = 0.0
    totalNumberOfCouspons: float = 0.0
    averageNumberOfSelectionsPerCoupon: float = 0.0
    averageCouponStake: float = 0.0
    averageCouponReturn: float = 0.0
    highestCouponStake: float = 0.0
    highestCouponReturn: float = 0.0
    totalStake: float = 0.0
    totalReturn: float = 0.0
    netEarnings: float = 0.0
    percentageReturnOnStake: float = 0.0
    winningStatus: float = 0.0
















