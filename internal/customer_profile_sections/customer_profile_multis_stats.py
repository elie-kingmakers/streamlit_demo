import streamlit as st

from datamodel.customer_profile import CustomerProfile
from utils.show_data import show_data
from utils.layout import insert_blank
from utils.format_data import get_winning_status_string


def show_customer_profile_multis_stats(customerProfile: CustomerProfile):
    st.subheader("Multis Stats")

    col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 2, 1])

    insert_blank(column=col1)
    col2.write("**Total**")
    insert_blank(column=col3)
    insert_blank(column=col4)
    col5.write("**Total**")

    col1.write("**Multis Total Nb. of Coupons**")
    show_data(value=customerProfile.multisTotalNumberOfCoupons, inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Multis Pct. of Total Nb. of Coupons**")
    show_data(value=customerProfile.multisPercentageOfTotalNumberOfCoupons, sign="%", inBold=True, column=col5)

    col1.write("**Multis Avg. Selection Odds**")
    show_data(value=customerProfile.multisAverageSelectionOdds, inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Multis Avg. Coupon Odds**")
    show_data(value=customerProfile.multisAverageCouponOdds, inBold=True, column=col5)

    col1.write("**Multis Avg. Selection Stake**")
    show_data(value=customerProfile.multisAverageSelectionStake, sign="€", inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Multis Avg. Selection Return**")
    show_data(value=customerProfile.multisAverageSelectionReturn, sign="€", inBold=True, column=col5)

    col1.write("**Multis Total Nb. of Selections**")
    show_data(value=customerProfile.multisTotalNumberOfSelections, inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Multis Avg. Combi Length**")
    show_data(value=customerProfile.multisAverageCouponNumberOfSelections, inBold=True, column=col5)

    col1.write("**Multis Avg. Coupon Stake**")
    show_data(value=customerProfile.multisAverageCouponStake, sign="€", inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Multis Avg. Coupon Return**")
    show_data(value=customerProfile.multisAverageCouponReturn, sign="€", inBold=True, column=col5)

    col1.write("**Multis Total Stake**")
    show_data(value=customerProfile.multisTotalStake, sign="€", inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Multis Pct. of Total Stake**")
    show_data(value=customerProfile.multisPercentageOfTotalStake, sign="%", inBold=True, column=col5)

    col1.write("**Multis Total Return**")
    show_data(value=customerProfile.multisTotalReturn, sign="€", inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Multis Pct. of Total Return**")
    show_data(value=customerProfile.multisPercentageOfTotalReturn, sign="%", inBold=True, column=col5)

    col1.write("**Multis Net Earnings**")
    show_data(value=customerProfile.multisNetEarnings, sign="€", negate=True, inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Multis Pct. of Net Earnings**")
    show_data(value=customerProfile.multisPercentageOfNetEarnings, sign="%", inBold=True, column=col5)

    col1.write("**Multis Return on Stake Pct.**")
    show_data(value=customerProfile.multisReturnOnStakePercentage, sign="%", inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Multis Margin**")
    show_data(value=customerProfile.multisMargin, sign="%", inBold=True, column=col5)

    col1.write("**Multis Nb. of Winning Bets**")
    show_data(value=customerProfile.multisTruePositives, inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Multis Nb. of Losing Bets**")
    show_data(value=customerProfile.multisFalsePositives, inBold=True, column=col5)

    col1.write("**Multis Accuracy**")
    show_data(value=customerProfile.multisAccuracy, sign="%", inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Multis Winning Status**")
    show_data(value=get_winning_status_string(customerProfile.multisWinningStatus), inBold=True, column=col5)











