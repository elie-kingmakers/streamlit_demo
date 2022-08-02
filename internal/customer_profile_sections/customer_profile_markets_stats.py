import streamlit as st
import matplotlib.pyplot as plt

from core.utils.matplotlib_helpers import get_empty_figure
from datamodel.customer_profile import CustomerProfile
from utils.matplotlib_figures import get_markets_stats_histogram
from utils.format_data import get_markets_stats_dataframe


def show_customer_profile_markets_stats(customerProfile: CustomerProfile):
    st.subheader("Markets Stats")

    # NUMBER OF SELECTIONS
    col1, col2, col3 = st.columns(3)

    col1.markdown("<div style='text-align: center;'>Nb. of Selections</div>", unsafe_allow_html=True)
    if customerProfile.marketsStatsNumberOfSelections:
        pdMarketsStatsNumberOfSelections = get_markets_stats_dataframe(
            marketsStats=customerProfile.marketsStatsNumberOfSelections,
            statType="int"
        )
        fig = get_markets_stats_histogram(
            x=pdMarketsStatsNumberOfSelections["Market"],
            y=pdMarketsStatsNumberOfSelections["Stat"],
            xLabelSize=10,
            barsAnnotations=True,
            barsAnnotationsHeightInc=0.0
        )
        col1.pyplot(fig=fig)
        plt.close(fig=fig)
    else:
        fig = get_empty_figure()
        col1.pyplot(fig=fig)
        plt.close(fig=fig)

    col2.markdown("<div style='text-align: center;'>Nb. of Selections SINGLES</div>", unsafe_allow_html=True)
    if customerProfile.singlesMarketsStatsNumberOfSelections:
        pdSinglesMarketsStatsNumberOfSelections = get_markets_stats_dataframe(
            marketsStats=customerProfile.singlesMarketsStatsNumberOfSelections,
            statType="int"
        )
        fig = get_markets_stats_histogram(
            x=pdSinglesMarketsStatsNumberOfSelections["Market"],
            y=pdSinglesMarketsStatsNumberOfSelections["Stat"],
            xLabelSize=10,
            barsAnnotations=True,
            barsAnnotationsHeightInc=0.0
        )
        col2.pyplot(fig=fig)
        plt.close(fig=fig)
    else:
        fig = get_empty_figure()
        col2.pyplot(fig=fig)
        plt.close(fig=fig)

    col3.markdown("<div style='text-align: center;'>Nb. of Selections MULTIS</div>", unsafe_allow_html=True)
    if customerProfile.multisMarketsStatsNumberOfSelections:
        pdMultisMarketsStatsNumberOfSelections = get_markets_stats_dataframe(
            marketsStats=customerProfile.multisMarketsStatsNumberOfSelections,
            statType="int"
        )
        fig = get_markets_stats_histogram(
            x=pdMultisMarketsStatsNumberOfSelections["Market"],
            y=pdMultisMarketsStatsNumberOfSelections["Stat"],
            xLabelSize=10,
            barsAnnotations=True,
            barsAnnotationsHeightInc=0.0
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
    if customerProfile.marketsStatsTotalStake:
        pdMarketsStatsTotalStake = get_markets_stats_dataframe(
            marketsStats=customerProfile.marketsStatsTotalStake,
            statType="float"
        )
        fig = get_markets_stats_histogram(
            x=pdMarketsStatsTotalStake["Market"],
            y=pdMarketsStatsTotalStake["Stat"],
            xLabelSize=10,
            barsAnnotations=True,
            barsAnnotationsHeightInc=0.0
        )
        col1.pyplot(fig=fig)
        plt.close(fig=fig)
    else:
        fig = get_empty_figure()
        col1.pyplot(fig=fig)
        plt.close(fig=fig)

    col2.markdown("<div style='text-align: center;'>Total Stake SINGLES</div>", unsafe_allow_html=True)
    if customerProfile.singlesMarketsStatsTotalStake:
        pdSinglesMarketsStatsTotalStake = get_markets_stats_dataframe(
            marketsStats=customerProfile.singlesMarketsStatsTotalStake,
            statType="float"
        )
        fig = get_markets_stats_histogram(
            x=pdSinglesMarketsStatsTotalStake["Market"],
            y=pdSinglesMarketsStatsTotalStake["Stat"],
            xLabelSize=10,
            barsAnnotations=True,
            barsAnnotationsHeightInc=0.0
        )
        col2.pyplot(fig=fig)
        plt.close(fig=fig)
    else:
        fig = get_empty_figure()
        col2.pyplot(fig=fig)
        plt.close(fig=fig)

    col3.markdown("<div style='text-align: center;'>Total Stake MULTIS</div>", unsafe_allow_html=True)
    if customerProfile.multisMarketsStatsTotalStake:
        pdMultisMarketsStatsTotalStake = get_markets_stats_dataframe(
            marketsStats=customerProfile.multisMarketsStatsTotalStake,
            statType="float"
        )
        fig = get_markets_stats_histogram(
            x=pdMultisMarketsStatsTotalStake["Market"],
            y=pdMultisMarketsStatsTotalStake["Stat"],
            xLabelSize=10,
            barsAnnotations=True,
            barsAnnotationsHeightInc=0.0
        )
        col3.pyplot(fig=fig)
        plt.close(fig=fig)
    else:
        fig = get_empty_figure()
        col3.pyplot(fig=fig)
        plt.close(fig=fig)

    plt.close('all')