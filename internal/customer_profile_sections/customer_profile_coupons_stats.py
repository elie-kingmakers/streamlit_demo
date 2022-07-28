import streamlit as st

from datamodel.customer_profile import CustomerProfile
from utils.show_data import show_data
from utils.layout import insert_blank
from utils.format_data import get_winning_status_string


def show_customer_profile_coupons_stats(customerProfile: CustomerProfile):
    st.subheader("Coupons Stats")

    col1, col2, col3, col4, _ = st.columns([2, 1, 1, 1, 2])

    insert_blank(column=col1)
    col2.write("**Pre-Match**")
    col3.write("**Live**")
    col4.write("**Total**")

    col1.write("**Total Nb. of Coupons**")
    show_data(value=customerProfile.totalNumberOfCouponsPrematch, inBold=True, column=col2)
    show_data(value=customerProfile.totalNumberOfCouponsLive, inBold=True, column=col3)
    show_data(value=customerProfile.totalNumberOfCoupons, inBold=True, column=col4)

    col1.write("**Avg. Selection Odds**")
    show_data(value=customerProfile.averageSelectionOddsPrematch, inBold=True, column=col2)
    show_data(value=customerProfile.averageSelectionOddsLive, inBold=True, column=col3)
    show_data(value=customerProfile.averageSelectionOdds, inBold=True, column=col4)

    col1.write("**Avg. Coupon Odds**")
    show_data(value=customerProfile.averageCouponOddsPrematch, inBold=True, column=col2)
    show_data(value=customerProfile.averageCouponOddsLive, inBold=True, column=col3)
    show_data(value=customerProfile.averageCouponOdds, inBold=True, column=col4)

    col1.write("**Avg. Selection Stake**")
    show_data(value=customerProfile.averageSelectionStakePrematch, sign="€", inBold=True, column=col2)
    show_data(value=customerProfile.averageSelectionStakeLive, sign="€", inBold=True, column=col3)
    show_data(value=customerProfile.averageSelectionStake, sign="€", inBold=True, column=col4)

    col1.write("**Avg. Selection Return**")
    show_data(value=customerProfile.averageSelectionReturnPrematch, sign="€", inBold=True, column=col2)
    show_data(value=customerProfile.averageSelectionReturnLive, sign="€", inBold=True, column=col3)
    show_data(value=customerProfile.averageSelectionReturn, sign="€", inBold=True, column=col4)

    col1.write("**Total Nb. of Selections**")
    show_data(value=customerProfile.totalNumberOfSelectionsPrematch, inBold=True, column=col2)
    show_data(value=customerProfile.totalNumberOfSelectionsLive, inBold=True, column=col3)
    show_data(value=customerProfile.totalNumberOfSelections, inBold=True, column=col4)

    col1.write("**Avg. Combi Length**")
    show_data(value=customerProfile.averageCouponNumberOfSelectionsPrematch, inBold=True, column=col2)
    show_data(value=customerProfile.averageCouponNumberOfSelectionsLive, inBold=True, column=col3)
    show_data(value=customerProfile.averageCouponNumberOfSelections, inBold=True, column=col4)

    col1.write("**Avg. Coupon Potential Payout**")
    show_data(value=customerProfile.averageCouponPotentialPayoutPrematch, sign="€", inBold=True, column=col2)
    show_data(value=customerProfile.averageCouponPotentialPayoutLive, sign="€", inBold=True, column=col3)
    show_data(value=customerProfile.averageCouponPotentialPayout, sign="€", inBold=True, column=col4)

    col1.write("**Avg. Coupon Stake**")
    show_data(value=customerProfile.averageCouponStakePrematch, sign="€", inBold=True, column=col2)
    show_data(value=customerProfile.averageCouponStakeLive, sign="€", inBold=True, column=col3)
    show_data(value=customerProfile.averageCouponStake, sign="€", inBold=True, column=col4)

    col1.write("**Avg. Coupon Return**")
    show_data(value=customerProfile.averageCouponReturnPrematch, sign="€", inBold=True, column=col2)
    show_data(value=customerProfile.averageCouponReturnLive, sign="€", inBold=True, column=col3)
    show_data(value=customerProfile.averageCouponReturn, sign="€", inBold=True, column=col4)

    col1.write("**Total Stake**")
    show_data(value=customerProfile.totalStakePrematch, sign="€", inBold=True, column=col2)
    show_data(value=customerProfile.totalStakeLive, sign="€", inBold=True, column=col3)
    show_data(value=customerProfile.totalStake, sign="€", inBold=True, column=col4)

    col1.write("**Total Return**")
    show_data(value=customerProfile.totalReturnPrematch, sign="€", inBold=True, column=col2)
    show_data(value=customerProfile.totalReturnLive, sign="€", inBold=True, column=col3)
    show_data(value=customerProfile.totalReturn, sign="€", inBold=True, column=col4)

    col1.write("**Net Earnings**")
    show_data(value=customerProfile.netEarningsPrematch, sign="€", negate=True, inBold=True, column=col2)
    show_data(value=customerProfile.netEarningsLive, sign="€", negate=True, inBold=True, column=col3)
    show_data(value=customerProfile.netEarnings, sign="€", negate=True, inBold=True, column=col4)

    col1.write("**Return on Stake Pct.**")
    show_data(value=customerProfile.returnOnStakePercentagePrematch, sign="%", inBold=True, column=col2)
    show_data(value=customerProfile.returnOnStakePercentageLive, sign="%", inBold=True, column=col3)
    show_data(value=customerProfile.returnOnStakePercentage, sign="%", inBold=True, column=col4)

    col1.write("**Margin**")
    show_data(value=customerProfile.marginPrematch, sign="%", inBold=True, column=col2)
    show_data(value=customerProfile.marginLive, sign="%", inBold=True, column=col3)
    show_data(value=customerProfile.margin, sign="%", inBold=True, column=col4)

    col1.write("**Winning Status**")
    show_data(value=get_winning_status_string(customerProfile.winningStatusPrematch), inBold=True, column=col2)
    show_data(value=get_winning_status_string(customerProfile.winningStatusLive), inBold=True, column=col3)
    show_data(value=get_winning_status_string(customerProfile.winningStatus), inBold=True, column=col4)

    col1.write("**Nb. of Winning Bets**")
    show_data(value=customerProfile.truePositivesPrematch, inBold=True, column=col2)
    show_data(value=customerProfile.truePositivesLive, inBold=True, column=col3)
    show_data(value=customerProfile.truePositives, inBold=True, column=col4)

    col1.write("**Nb. of Losing Bets**")
    show_data(value=customerProfile.falsePositivesPrematch, inBold=True, column=col2)
    show_data(value=customerProfile.falsePositivesLive, inBold=True, column=col3)
    show_data(value=customerProfile.falsePositives, inBold=True, column=col4)

    col1.write("**Betting Accuracy**")
    show_data(value=customerProfile.accuracyPrematch, sign="%", inBold=True, column=col2)
    show_data(value=customerProfile.accuracyLive, sign="%", inBold=True, column=col3)
    show_data(value=customerProfile.accuracy, sign="%", inBold=True, column=col4)




