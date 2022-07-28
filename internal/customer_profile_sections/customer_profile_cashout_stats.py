import streamlit as st

from datamodel.customer_profile import CustomerProfile
from utils.show_data import show_data
from utils.layout import insert_blank


def show_customer_profile_cashout_stats(customerProfile: CustomerProfile):
    st.subheader("Cashout Stats")

    col1, col2, col3, col4, _ = st.columns([2, 1, 1, 1, 2])

    insert_blank(column=col1)
    col2.write("**Pre-Match**")
    col3.write("**Live**")
    col4.write("**Total**")

    col1.write("**Cashout Total Nb. of Coupons**")
    show_data(value=customerProfile.cashoutTotalNumberOfCouponsPrematch, inBold=True, column=col2)
    show_data(value=customerProfile.cashoutTotalNumberOfCouponsLive, inBold=True, column=col3)
    show_data(value=customerProfile.cashoutTotalNumberOfCoupons, inBold=True, column=col4)

    col1.write("**Cashout Total Stake**")
    show_data(value=customerProfile.cashoutTotalStakePrematch, sign="€", inBold=True, column=col2)
    show_data(value=customerProfile.cashoutTotalStakeLive, sign="€", inBold=True, column=col3)
    show_data(value=customerProfile.cashoutTotalStake, sign="€", inBold=True, column=col4)

    col1.write("**Cashout Total Return**")
    show_data(value=customerProfile.cashoutTotalReturnPrematch, sign="€", inBold=True, column=col2)
    show_data(value=customerProfile.cashoutTotalReturnLive, sign="€", inBold=True, column=col3)
    show_data(value=customerProfile.cashoutTotalReturn, sign="€", inBold=True, column=col4)

    col1.write("**Cashout Potential Payout**")
    show_data(value=customerProfile.cashoutPotentialPayoutPrematch, sign="€", inBold=True, column=col2)
    show_data(value=customerProfile.cashoutPotentialPayoutLive, sign="€", inBold=True, column=col3)
    show_data(value=customerProfile.cashoutPotentialPayout, sign="€", inBold=True, column=col4)

    col1.write("**Cashout Net Earnings**")
    show_data(value=customerProfile.cashoutNetEarningsPrematch, sign="€", negate=True, inBold=True, column=col2)
    show_data(value=customerProfile.cashoutNetEarningsLive, sign="€", negate=True, inBold=True, column=col3)
    show_data(value=customerProfile.cashoutNetEarnings, sign="€", negate=True, inBold=True, column=col4)

    col1.write("**Cashout Margin**")
    show_data(value=customerProfile.cashoutMarginPrematch, sign="%", inBold=True, column=col2)
    show_data(value=customerProfile.cashoutMarginLive, sign="%", inBold=True, column=col3)
    show_data(value=customerProfile.cashoutMargin, sign="%", inBold=True, column=col4)












