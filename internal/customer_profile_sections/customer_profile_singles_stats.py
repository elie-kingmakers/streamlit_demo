import streamlit as st

from datamodel.customer_profile import CustomerProfile
from utils.show_data import show_data
from utils.layout import insert_blank
from utils.format_data import get_winning_status_string


def show_customer_profile_singles_stats(customerProfile: CustomerProfile):
    st.subheader("Singles Stats")

    col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 2, 1])

    insert_blank(column=col1)
    col2.write("**Total**")
    insert_blank(column=col3)
    insert_blank(column=col4)
    col5.write("**Total**")

    col1.write("**Singles Total Nb. of Coupons**")
    show_data(value=customerProfile.singlesTotalNumberOfCoupons, inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Singles Pct. of Total Nb. of Coupons**")
    show_data(value=customerProfile.singlesPercentageOfTotalNumberOfCoupons, sign="%", inBold=True, column=col5)

    col1.write("**Singles Avg. Coupon Odds**")
    show_data(value=customerProfile.singlesAverageCouponOdds, inBold=True, column=col2)
    insert_blank(column=col3)
    insert_blank(column=col4)
    insert_blank(column=col5)

    col1.write("**Singles Avg. Coupon Stake**")
    show_data(value=customerProfile.singlesAverageCouponStake, sign="€", inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Singles Avg. Coupon Return**")
    show_data(value=customerProfile.singlesAverageCouponReturn, sign="€", inBold=True, column=col5)

    col1.write("**Singles Total Stake**")
    show_data(value=customerProfile.singlesTotalStake, sign="€", inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Singles Pct. of Total Stake**")
    show_data(value=customerProfile.singlesPercentageOfTotalStake, sign="%", inBold=True, column=col5)

    col1.write("**Singles Total Return**")
    show_data(value=customerProfile.singlesTotalReturn, sign="€", inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Singles Pct. of Total Return**")
    show_data(value=customerProfile.singlesPercentageOfTotalReturn, sign="%", inBold=True, column=col5)

    col1.write("**Singles Net Earnings**")
    show_data(value=customerProfile.singlesNetEarnings, sign="€", negate=True, inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Singles Pct. of Net Earnings**")
    show_data(value=customerProfile.singlesPercentageOfNetEarnings, sign="%", inBold=True, column=col5)

    col1.write("**Singles Return on Stake Pct.**")
    show_data(value=customerProfile.singlesReturnOnStakePercentage, sign="%", inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Singles Margin**")
    show_data(value=customerProfile.singlesMargin, inBold=True, sign="%", column=col5)

    col1.write("**Singles Nb. of Winning Bets**")
    show_data(value=customerProfile.singlesTruePositives, inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Singles Nb. of Losing Bets**")
    show_data(value=customerProfile.singlesFalsePositives, inBold=True, column=col5)

    col1.write("**Singles Accuracy**")
    show_data(value=customerProfile.singlesAccuracy, sign="%", inBold=True, column=col2)
    insert_blank(column=col3)
    col4.write("**Singles Winning Status**")
    show_data(value=get_winning_status_string(customerProfile.singlesWinningStatus), inBold=True, column=col5)









