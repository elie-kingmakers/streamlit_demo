import sys

sys.path.append(".")  # needed for streamlit to find the files

import streamlit as st
import pandas as pd

# from core.utils.histogram import get_histogram
# from core.utils.filestore import get_filestore_file_url
# from core.store.databricks_api_engine import DatabricksApiEngine
from datamodel.customer_profile import CustomerProfile
from datamodel.constants import DEFAULT_USER_PLATFORM_ID
from store.customer_data_retriever import CustomerDataRetriever
from utils.load_css_file import local_css_file
from utils.query_params import QueryParams, manage_query_params
from utils.layout import insert_blank, remove_whitespace_top, hide_menu_button
from utils.format_data import get_date_string, get_gender_string, get_winning_status_string
from utils.show_data import show_data


# ***********************************************************************************************************************
# ***********************************************************************************************************************

# change webpage configuration
st.set_page_config(page_title="Customer Profile", layout="wide")

# need to specify 'customer_profiling/' for streamlit to find it
local_css_file("style.css")

# manage query parameters
queryParams = manage_query_params()
# userPlatformId = queryParams[QueryParams.PLATFORM_USER_ID][0]

userPlatformId = 0

# layout changes
remove_whitespace_top()
# hide_menu_button() # keep it for now to reset cache


# ***********************************************************************************************************************
# ***********************************************************************************************************************

st.title("Customer Profile")

# ***********************************************************************************************************************
# ***********************************************************************************************************************

# with st.spinner("Loading Customers Table..."):
#
#     @st.cache
#     def load_customers_table():
#         return CustomerDataRetriever.load_data()
#
#     dfCustomers = load_customers_table()

# ***********************************************************************************************************************
# ***********************************************************************************************************************

form = st.form(key="customer_profile")

# col1, col2 = form.columns([1, 5])
#
# userIdType = col1.radio(
#      label="ID Type:",
#      options=('User ID', 'Platform ID')
# )

userPlatformId = form.text_input(label="User Platform ID:", value=userPlatformId)

getProfileButton = form.form_submit_button(label="Get Profile")

# losing = 330677 (413316)
# winning = 900563 (1004623)
if getProfileButton or (userPlatformId != DEFAULT_USER_PLATFORM_ID):

    # if userIdType == 'User ID':
    #     # dfCustomer = CustomerDataRetriever.load_customer_data(userId=userId)
    #     dfCustomer = None
    #     st.text('W.I.P.')
    #     st.stop()
    # elif userIdType == 'Platform ID':
    #     dfCustomer = CustomerDataRetriever.load_customer_data(userPlatformId=userPlatformId)
    # else:
    #     dfCustomer = None
    #     st.warning('Please pick a valid ID type (Platform ID).')
    #     st.stop()

    dfCustomer = CustomerDataRetriever.load_customer_data(userPlatformId=userPlatformId)

    if dfCustomer.empty:
        st.error('User Not Found.')
        st.warning('''
            Possible Reasons:\n
            * ID Type is wrong (Please use User Platform ID)\n
            * ID is wrong\n
            * User does not have settled coupons\n
            * User is brand new (registration less than 1 day old)
            ''')
        st.stop()

    customerProfile = CustomerProfile.from_data(dfCustomer=dfCustomer)

    # ***********************************************************************************************************************
    # DETAILS

    st.subheader("Details")

    col1, col2, col3 = st.columns(3)

    show_data(label="User ID", value=customerProfile.userId, inBold=True, column=col1)
    show_data(label="User Platform ID", value=customerProfile.userPlatformId, inBold=True, column=col2)
    insert_blank(column=col3)

    show_data(label="First Name", value=customerProfile.firstName, inBold=True, column=col1)
    show_data(label="Last Name", value=customerProfile.lastName, inBold=True, column=col2)
    show_data(label="User Type", value=customerProfile.userTypeName, inBold=True, column=col3)

    show_data(label="Username", value=customerProfile.username, inBold=True, column=col1)
    show_data(label="Email", value=customerProfile.email, inBold=True, column=col2)
    show_data(label="Verification Level", value=customerProfile.verificationLevelName, inBold=True, column=col3)

    show_data(
        label="Subscription Date",
        value=get_date_string(dateKey=customerProfile.subscriptionDateKey),
        inBold=True,
        column=col1,
    )
    show_data(label="Country", value=customerProfile.countryName, inBold=True, column=col2)
    show_data(label="Currency", value=customerProfile.userCurrencyName, inBold=True, column=col3)

    show_data(label="Gender", value=get_gender_string(gender=customerProfile.gender), inBold=True, column=col1)
    show_data(
        label="Birth Date", value=get_date_string(dateKey=customerProfile.birthDateKey), inBold=True, column=col2
    )
    show_data(label="Age", value=customerProfile.age, inBold=True, column=col3)

    show_data(label="Street Address", value=customerProfile.streetAddress, inBold=True, column=col1)
    show_data(label="Town", value=customerProfile.town, inBold=True, column=col2)
    show_data(label="Zip Code", value=customerProfile.zipCode, inBold=True, column=col3)

    show_data(label="Phone", value=customerProfile.phone, inBold=True, column=col1)
    show_data(label="Mobile Phone", value=customerProfile.mobilePhone, inBold=True, column=col2)
    show_data(label="IP Address", value=customerProfile.clientIP, inBold=True, column=col3)


    # ***********************************************************************************************************************
    # INFO

    st.markdown("""---""")

    st.subheader("Info")

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


    # ***********************************************************************************************************************
    # TOTAL COUPON STATS

    st.markdown("""---""")

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


    # ***********************************************************************************************************************
    # CASHOUT STATS

    st.markdown("""---""")

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

    # ***********************************************************************************************************************
    # SINGLES STATS

    st.markdown("""---""")

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





    # ***********************************************************************************************************************
    # MULTIS STATS

    st.markdown("""---""")

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





    # show_data(label='', value=customerProfile., inBold=True, column=col2)
    # show_data(label='', value=customerProfile., inBold=True, column=col3)
    # show_data(label='', value=customerProfile., inBold=True, column=col4)











# # ------------------------------------------------------------------------------------------------------------------
# st.markdown("""---""")
#
# # legend
# st.markdown("<strong>Number in parentheses is population average</strong>", unsafe_allow_html=True)
# st.markdown(
#     "<strong><span class='highlight_green'>Green</span> means more than population average</strong>",
#     unsafe_allow_html=True
# )
# st.markdown(
#     "<strong><span class='highlight_red'>Red</span> means less than population average</strong>",
#     unsafe_allow_html=True
# )
#
#     # ------------------------------------------------------------------------------------------------------------------
#     st.markdown("""---""")
#
#     # customer ID
#     st.markdown(f'Customer ID:  <strong>{customerProfile.userId}</strong>', unsafe_allow_html=True)
#
#     # total number of users
#     st.markdown(f'Total Number of Users:  <strong>{populationProfile.totalNumberOfUsers}</strong>', unsafe_allow_html=True)
#
#     # total number of coupons
#     totalNumberOfCoupons = get_css_comparison_with_population(
#         userValue=customerProfile.totalNumberOfCoupons,
#         populationValue=populationProfile.totalNumberOfCoupons/populationProfile.totalNumberOfUsers
#     )
#     st.markdown(f"Total Number of Coupons: {totalNumberOfCoupons}", unsafe_allow_html=True)
#
#     # average number of selections per coupon
#     averageNumberOfSelectionPerCoupon = get_css_comparison_with_population(
#         userValue=customerProfile.averageNumberOfSelectionsPerCoupon,
#         populationValue=populationProfile.averageNumberOfSelectionsPerCoupon
#     )
#     st.markdown(f"Average Number of Selections Per Coupon: {averageNumberOfSelectionPerCoupon}", unsafe_allow_html=True)
#
#     # average odd value per selection
#     averageOddValuePerSelection = get_css_comparison_with_population(
#         userValue=customerProfile.averageOddValuePerSelection,
#         populationValue=populationProfile.averageOddValuePerSelection
#     )
#     st.markdown(f"Average Odd Value Per Selection: {averageOddValuePerSelection}", unsafe_allow_html=True)
#
#     # average coupon stake
#     averageCouponStake = get_css_comparison_with_population(
#         userValue=customerProfile.averageCouponStake,
#         populationValue=populationProfile.averageCouponStake
#     )
#     st.markdown(f"Average Coupon Stake: {averageCouponStake}", unsafe_allow_html=True)
#
#     # average coupon return
#     averageCouponReturn = get_css_comparison_with_population(
#         userValue=customerProfile.averageCouponReturn,
#         populationValue=populationProfile.averageCouponReturn
#     )
#     st.markdown(f"Average Coupon Return: {averageCouponReturn}", unsafe_allow_html=True)
#
#     # highest coupon stake
#     st.markdown(f"Highest Coupon Stake:  <strong>{customerProfile.highestCouponStake}</strong>", unsafe_allow_html=True)
#
#     # highest coupon return
#     st.markdown(f"Highest Coupon Return:  <strong>{customerProfile.highestCouponReturn}</strong>", unsafe_allow_html=True)
#
#     # true positives
#     truePositives = get_css_comparison_with_population(
#         userValue=customerProfile.truePositives,
#         populationValue=populationProfile.averageTruePositives
#     )
#     st.markdown(f"True Positives: {truePositives}", unsafe_allow_html=True)
#
#     # false positives
#     falsePositives = get_css_comparison_with_population(
#         userValue=customerProfile.falsePositives,
#         populationValue=populationProfile.averageFalsePositives
#     )
#     st.markdown(f"False Positives: {falsePositives}", unsafe_allow_html=True)
#
#     # accuracy
#     accuracy = get_css_comparison_with_population(
#         userValue=customerProfile.accuracy,
#         populationValue=populationProfile.averageAccuracy
#     )
#     st.markdown(f"Accuracy (Strike Rate): {accuracy}", unsafe_allow_html=True)
#
#     # average probability estimate kelly criterion
#     averageProbabilityEstimateKellyCriterion = get_css_comparison_with_population(
#         userValue=customerProfile.averageProbabilityEstimateKellyCriterion,
#         populationValue=populationProfile.averageProbabilityEstimateKellyCriterion
#     )
#     st.markdown(f"Average Probability Estimate Kelly Criterion: {averageProbabilityEstimateKellyCriterion}", unsafe_allow_html=True)
#
#     # average bet score
#     averageBetScore = get_css_comparison_with_population(
#         userValue=customerProfile.averageBetScore,
#         populationValue=populationProfile.averageBetScore
#     )
#     st.markdown(f"Average Bet Score: {averageBetScore}", unsafe_allow_html=True)
#
#     # total stake
#     totalStake = get_css_comparison_with_population(
#         userValue=customerProfile.totalStake,
#         populationValue=populationProfile.totalStake / populationProfile.totalNumberOfUsers
#     )
#     st.markdown(f"Total Stake: {totalStake}", unsafe_allow_html=True)
#
#     # total return
#     totalReturn = get_css_comparison_with_population(
#         userValue=customerProfile.totalReturn,
#         populationValue=populationProfile.totalReturn / populationProfile.totalNumberOfUsers
#     )
#     st.markdown(f"Total Return: {totalReturn}", unsafe_allow_html=True)
#
#     # return on stake percentage
#     returnOnStakePercentage = get_css_comparison_with_population(
#         userValue=customerProfile.returnOnStakePercentage,
#         populationValue=populationProfile.averageReturnOnStakePercentage
#     )
#     st.markdown(f"Return on Stake Percentage: {returnOnStakePercentage}", unsafe_allow_html=True)
#
#     # net earnings
#     netEarnings = get_css_comparison_with_population(
#         userValue=customerProfile.netEarnings,
#         populationValue=populationProfile.totalNetEarnings / populationProfile.totalNumberOfUsers
#     )
#     st.markdown(f"Net Earnings: {netEarnings}", unsafe_allow_html=True)
#
#     # ------------------------------------------------------------------------------------------------------------------
#     st.markdown("""---""")
#
#     # winning status
#     winningStatus = get_css_evaluation(
#         value=customerProfile.winningStatus,
#         compareWith=0.0,
#         resultGreater="WINNING",
#         resultSmaller="LOSING",
#         resultEqual="NEUTRAL"
#     )
#     st.markdown(f"Winning Status: {winningStatus}", unsafe_allow_html=True)
#
#     # ------------------------------------------------------------------------------------------------------------------
#     st.markdown("""---""")
#
#     # distributions of probability estimates
#
#     st.write("Distribution of Probability Estimate:")
#
#     colUser, colPopulation = st.columns(2)
#
#     colUser.write("User:")
#     colPopulation.write("Population:")
#
#     with st.spinner("Loading distributions of Probability Estimate..."):
#         figProbabilityEstimateUser = get_histogram(
#             df=dfCouponsUser,
#             columnName='ProbabilityEstimateKellyCriterion',
#             xLabel='Probability Estimates',
#             yLabel='Count',
#             binsNum=100,
#             xScale='linear',
#             yScale='log',
#             xTicks=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
#         )
#         colUser.pyplot(fig=figProbabilityEstimateUser)
#
#         colPopulation.image(get_filestore_file_url('dbfs:/FileStore/elie/customer_profiling/figures/figProbabilityEstimatePopulation.png'))
#
#     # ------------------------------------------------------------------------------------------------------------------
#     st.markdown("""---""")
#
#     # distributions of bet scores
#
#     st.write("Distribution of Bet Score:")
#
#     colUser, colPopulation = st.columns(2)
#
#     colUser.write("User:")
#     colPopulation.write("Population:")
#
#     with st.spinner("Loading Distributions of Bet Score..."):
#         figBetScoreUser = get_histogram(
#             df=dfCouponsUser,
#             columnName='BetScore',
#             xLabel='Bet Scores',
#             yLabel='Count',
#             binsNum=100,
#             xScale='linear',
#             yScale='log'
#         )
#         colUser.pyplot(fig=figBetScoreUser)
#
#         colPopulation.image(get_filestore_file_url('dbfs:/FileStore/elie/customer_profiling/figures/figBetScorePopulation.png'))
#
#     # ------------------------------------------------------------------------------------------------------------------
#     st.markdown("""---""")
#
#     st.success("Customer Profile Complete")
