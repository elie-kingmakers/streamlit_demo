import streamlit as st
import matplotlib.pyplot as plt

from core.utils.matplotlib_helpers import get_empty_figure
from datamodel.customer_profile import CustomerProfile
from utils.matplotlib_figures import get_sports_stats_histogram
from utils.format_data import get_sports_stats_dataframe

# customerProfile = CustomerProfile()
# customerProfile.sportsStatsNumberOfSelections = ["Soccer_379",
#                                                  "Table Tennis_19",
#                                                  "Ice Hockey_1",
#                                                  "Rugby_2",
#                                                  "Basketball_120",
#                                                  "Volleyball_6",
#                                                  "Handball_2",
#                                                  "ESport Basketball_2",
#                                                  "ESport Soccer_2",
#                                                  "Tennis_23"]
#
# customerProfile.sportsStatsTotalStake = ["Soccer_63.77258604761889",
#                                          "Table Tennis_6.032",
#                                          "Ice Hockey_0.06999999999999999",
#                                          "Rugby_0.15133333333333332",
#                                          "Basketball_36.73028928571426",
#                                          "Volleyball_0.8182833333333333",
#                                          "Handball_0.355",
#                                          "ESport Basketball_0.318",
#                                          "ESport Soccer_0.1225",
#                                          "Tennis_7.623875000000001"]

def show_customer_profile_sports_stats(customerProfile: CustomerProfile):
    st.subheader("Sports Stats")

    # NUMBER OF SELECTIONS
    col1, col2, col3 = st.columns(3)

    col1.markdown("<div style='text-align: center;'>Nb. of Selections</div>", unsafe_allow_html=True)
    if customerProfile.sportsStatsNumberOfSelections:
        pdSportsStatsNumberOfSelections = get_sports_stats_dataframe(
            sportsStats=customerProfile.sportsStatsNumberOfSelections,
            statType="int"
        )
        fig = get_sports_stats_histogram(
            x=pdSportsStatsNumberOfSelections["Sport"],
            y=pdSportsStatsNumberOfSelections["Stat"],
            xLabelSize=8,
            barsAnnotations=True,
            barsAnnotationsHeightInc=0.0,
            wrapLabels=True
        )
        col1.pyplot(fig=fig)
        plt.close(fig=fig)
    else:
        fig = get_empty_figure()
        col1.pyplot(fig=fig)
        plt.close(fig=fig)

    col2.markdown("<div style='text-align: center;'>Nb. of Selections SINGLES</div>", unsafe_allow_html=True)
    if customerProfile.singlesSportsStatsNumberOfSelections:
        pdSinglesSportsStatsNumberOfSelections = get_sports_stats_dataframe(
            sportsStats=customerProfile.singlesSportsStatsNumberOfSelections,
            statType="int"
        )
        fig = get_sports_stats_histogram(
            x=pdSinglesSportsStatsNumberOfSelections["Sport"],
            y=pdSinglesSportsStatsNumberOfSelections["Stat"],
            xLabelSize=8,
            barsAnnotations=True,
            barsAnnotationsHeightInc=0.0,
            wrapLabels=True
        )
        col2.pyplot(fig=fig)
        plt.close(fig=fig)
    else:
        fig = get_empty_figure()
        col2.pyplot(fig=fig)
        plt.close(fig=fig)

    col3.markdown("<div style='text-align: center;'>Nb. of Selections MULTIS</div>", unsafe_allow_html=True)
    if customerProfile.multisSportsStatsNumberOfSelections:
        pdMultisSportsStatsNumberOfSelections = get_sports_stats_dataframe(
            sportsStats=customerProfile.multisSportsStatsNumberOfSelections,
            statType="int"
        )
        fig = get_sports_stats_histogram(
            x=pdMultisSportsStatsNumberOfSelections["Sport"],
            y=pdMultisSportsStatsNumberOfSelections["Stat"],
            xLabelSize=8,
            barsAnnotations=True,
            barsAnnotationsHeightInc=0.0,
            wrapLabels=True
        )
        col3.pyplot(fig=fig)
        plt.close(fig=fig)
    else:
        fig = get_empty_figure()
        col3.pyplot(fig=fig)
        plt.close(fig=fig)

    # TOTAL STAKE
    col1, col2, col3 = st.columns(3)

    col1.markdown("<div style='text-align: center;'>Total Stake</div>", unsafe_allow_html=True)
    if customerProfile.sportsStatsTotalStake:
        pdSportsStatsTotalStake = get_sports_stats_dataframe(
            sportsStats=customerProfile.sportsStatsTotalStake,
            statType="float"
        )
        fig = get_sports_stats_histogram(
            x=pdSportsStatsTotalStake["Sport"],
            y=pdSportsStatsTotalStake["Stat"],
            xLabelSize=8,
            barsAnnotations=True,
            barsAnnotationsHeightInc=0.0,
            wrapLabels=True
        )
        col1.pyplot(fig=fig)
        plt.close(fig=fig)
    else:
        fig = get_empty_figure()
        col1.pyplot(fig=fig)
        plt.close(fig=fig)

    col2.markdown("<div style='text-align: center;'>Total Stake SINGLES</div>", unsafe_allow_html=True)
    if customerProfile.singlesSportsStatsTotalStake:
        pdSinglesSportsStatsTotalStake = get_sports_stats_dataframe(
            sportsStats=customerProfile.singlesSportsStatsTotalStake,
            statType="float"
        )
        fig = get_sports_stats_histogram(
            x=pdSinglesSportsStatsTotalStake["Sport"],
            y=pdSinglesSportsStatsTotalStake["Stat"],
            xLabelSize=8,
            barsAnnotations=True,
            barsAnnotationsHeightInc=0.0,
            wrapLabels=True
        )
        col2.pyplot(fig=fig)
        plt.close(fig=fig)
    else:
        fig = get_empty_figure()
        col2.pyplot(fig=fig)
        plt.close(fig=fig)

    col3.markdown("<div style='text-align: center;'>Total Stake MULTIS</div>", unsafe_allow_html=True)
    if customerProfile.multisSportsStatsTotalStake:
        pdMultisSportsStatsTotalStake = get_sports_stats_dataframe(
            sportsStats=customerProfile.multisSportsStatsTotalStake,
            statType="float"
        )
        fig = get_sports_stats_histogram(
            x=pdMultisSportsStatsTotalStake["Sport"],
            y=pdMultisSportsStatsTotalStake["Stat"],
            xLabelSize=8,
            barsAnnotations=True,
            barsAnnotationsHeightInc=0.0,
            wrapLabels=True
        )
        col3.pyplot(fig=fig)
        plt.close(fig=fig)
    else:
        fig = get_empty_figure()
        col3.pyplot(fig=fig)
        plt.close(fig=fig)

    plt.close('all')







