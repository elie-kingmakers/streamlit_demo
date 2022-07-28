import sys

sys.path.append(".")  # needed for streamlit to find the files

import streamlit as st

# from core.utils.histogram import get_histogram
# from core.utils.filestore import get_filestore_file_url
# from core.store.databricks_api_engine import DatabricksApiEngine
from datamodel.customer_profile import CustomerProfile
from datamodel.constants import DEFAULT_USER_PLATFORM_ID
from store.customer_data_retriever import CustomerDataRetriever
from internal.customer_profile_sections.customer_profile_general import show_customer_profile_general
from internal.customer_profile_sections.customer_profile_info import show_customer_profile_info
from internal.customer_profile_sections.customer_profile_coupons_stats import show_customer_profile_coupons_stats
from internal.customer_profile_sections.customer_profile_cashout_stats import show_customer_profile_cashout_stats
from internal.customer_profile_sections.customer_profile_singles_stats import show_customer_profile_singles_stats
from internal.customer_profile_sections.customer_profile_multis_stats import show_customer_profile_multis_stats
from internal.customer_profile_sections.customer_profile_sports_stats import show_customer_profile_sports_stats
from internal.customer_profile_sections.customer_profile_tournaments_stats import show_customer_profile_tournaments_stats
from internal.customer_profile_sections.customer_profile_markets_stats import show_customer_profile_markets_stats
from utils.load_css_file import local_css_file
from utils.query_params import QueryParams, manage_query_params
from utils.layout import hide_menu_button, remove_whitespace_top, resize_sidebar

# ***********************************************************************************************************************
# ***********************************************************************************************************************

# change webpage configuration
st.set_page_config(page_title="Customer Profile", layout="wide")

# need to specify 'customer_profiling/' for streamlit to find it
local_css_file("style.css")

# manage query parameters
queryParams = manage_query_params()
userPlatformId = queryParams[QueryParams.USER_PLATFORM_ID][0]

# layout changes
remove_whitespace_top()
# hide_menu_button()    # keep it for now to reset cache
resize_sidebar(width=210)


# ***********************************************************************************************************************
# ***********************************************************************************************************************

st.title("Customer Profile")

# ***********************************************************************************************************************
# ***********************************************************************************************************************

@st.cache
def load_customer_profile():
    dfCustomerProfile = CustomerDataRetriever.load_customer_data(userPlatformId=userPlatformId)
    return dfCustomerProfile

col1, col2, col3, col4 = st.columns(4)

userPlatformId = col1.text_input(label="User Platform ID:", value=userPlatformId)
col2.markdown("##")
getProfileButton = col2.button(label="Get Profile")

# example userPlatformIDs: 413316, 1004623
if getProfileButton or (userPlatformId != DEFAULT_USER_PLATFORM_ID):
    dfCustomer = load_customer_profile()

    if dfCustomer.empty:
        st.error('User Not Found.')
        st.warning(
            '''
            Possible Reasons:\n
            * ID Type is wrong (Please use User Platform ID)\n
            * ID is wrong\n
            * User does not have settled coupons\n
            * User is brand new (registration less than 1 day old)
            '''
            )
        st.stop()

    customerProfile = CustomerProfile.from_data(dfCustomer=dfCustomer)


if userPlatformId == DEFAULT_USER_PLATFORM_ID:
    st.stop()

# ***********************************************************************************************************************
# ***********************************************************************************************************************

def full_profile():
    show_customer_profile_general(customerProfile=customerProfile)

    st.markdown("""---""")
    show_customer_profile_info(customerProfile=customerProfile)

    st.markdown("""---""")
    show_customer_profile_coupons_stats(customerProfile=customerProfile)

    st.markdown("""---""")
    show_customer_profile_cashout_stats(customerProfile=customerProfile)

    st.markdown("""---""")
    show_customer_profile_singles_stats(customerProfile=customerProfile)

    st.markdown("""---""")
    show_customer_profile_multis_stats(customerProfile=customerProfile)

    st.markdown("""---""")
    show_customer_profile_sports_stats(customerProfile=customerProfile)

    st.markdown("""---""")
    show_customer_profile_tournaments_stats(customerProfile=customerProfile)

    st.markdown("""---""")
    show_customer_profile_markets_stats(customerProfile=customerProfile)



def general():
    show_customer_profile_general(customerProfile=customerProfile)


def info():
    show_customer_profile_info(customerProfile=customerProfile)


def coupons_stats():
    show_customer_profile_coupons_stats(customerProfile=customerProfile)


def cashout_stats():
    show_customer_profile_cashout_stats(customerProfile=customerProfile)


def singles_stats():
    show_customer_profile_singles_stats(customerProfile=customerProfile)


def multis_stats():
    show_customer_profile_multis_stats(customerProfile=customerProfile)


def sports_stats():
    show_customer_profile_sports_stats(customerProfile=customerProfile)


def tournaments_stats():
    show_customer_profile_tournaments_stats(customerProfile=customerProfile)


def markets_stats():
    show_customer_profile_markets_stats(customerProfile=customerProfile)



page_names_to_functions = {
    "Full Profile": full_profile,
    "General": general,
    "Info": info,
    "Coupons Stats": coupons_stats,
    "Cashout Stats": cashout_stats,
    "Singles Stats": singles_stats,
    "Multis Stats": multis_stats,
    "Sports Stats": sports_stats,
    "Tournaments Stats": tournaments_stats,
    "Markets Stats": markets_stats
}

selected_page = st.sidebar.radio("Select a page:", page_names_to_functions.keys())
page_names_to_functions[selected_page]()











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
