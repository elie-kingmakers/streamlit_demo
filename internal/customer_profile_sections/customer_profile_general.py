import streamlit as st

from datamodel.customer_profile import CustomerProfile
from utils.format_data import get_date_string
from utils.format_data import get_winning_status_string, get_css_evaluation
from utils.layout import insert_blank


def show_customer_profile_general(customerProfile: CustomerProfile):
    st.subheader("General")

    col1, col2, col3 = st.columns(3)

    insert_blank(column=col1)
    insert_blank(column=col2)

    col1.markdown(f"<strong>Winning Status: {get_winning_status_string(winningStatus=customerProfile.winningStatus, colorCoded=True)}</strong>", unsafe_allow_html=True)

    col2.markdown(f"<strong>Margin: {get_css_evaluation(value=customerProfile.margin, compareWith=0.0, sign='%')}</strong>", unsafe_allow_html=True)

    insert_blank(column=col1)
    insert_blank(column=col2)

    col1, col2, col3 = st.columns(3)

    if customerProfile.availableBalanceTotal == "N/A":
        col1.metric(label="Available Balance", value="N/A")
    else:
        col1.metric(label="Available Balance", value="{:.2f} €".format(customerProfile.availableBalanceTotal))

    col2.metric(label="Total Nb. of Coupons", value=customerProfile.totalNumberOfCoupons)
    col3.metric(
        label="Most Recent Coupon Date", value=get_date_string(dateKey=customerProfile.mostRecentCouponDateKey)
    )

    col1.metric(label="Highest Coupon Stake", value="{:.2f} €".format(customerProfile.highestCouponStake))
    col2.metric(label="Highest Coupon Return", value="{:.2f} €".format(customerProfile.highestCouponReturn))

    if customerProfile.unsettledStake == "N/A":
        col3.metric(label="Unsettled Stake", value=0)
    else:
        col3.metric(label="Unsettled Stake", value="{:.2f} €".format(customerProfile.unsettledStake))

    # col1.metric(label='Avg. Probability Estimate KC', value='{:.2f}'.format(customerProfile.averageProbabilityEstimateKellyCriterion*100.0))
    # col2.metric(label='Avg. Bet Score', value='{:.2f}'.format(customerProfile.averageBetScore))







