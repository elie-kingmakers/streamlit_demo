import streamlit as st
import matplotlib.pyplot as plt

from core.utils.matplotlib_helpers import get_empty_figure
from datamodel.customer_profile import CustomerProfile
from utils.matplotlib_figures import get_tournaments_stats_histogram
from utils.format_data import get_tournaments_stats_dataframe


def show_customer_profile_tournaments_stats(customerProfile: CustomerProfile):
    st.subheader("Tournaments Stats")

    # NUMBER OF SELECTIONS
    col1, col2, col3 = st.columns(3)

    col1.markdown("<div style='text-align: center;'>Nb. of Selections</div>", unsafe_allow_html=True)
    if customerProfile.tournamentsStatsNumberOfSelections:
        pdTournamentsStatsNumberOfSelections = get_tournaments_stats_dataframe(
            tournamentsStats=customerProfile.tournamentsStatsNumberOfSelections,
            statType="int"
        )
        fig = get_tournaments_stats_histogram(
            x=pdTournamentsStatsNumberOfSelections["Tournament"],
            y=pdTournamentsStatsNumberOfSelections["Stat"],
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
    if customerProfile.singlesTournamentsStatsNumberOfSelections:
        pdSinglesTournamentsStatsNumberOfSelections = get_tournaments_stats_dataframe(
            tournamentsStats=customerProfile.singlesTournamentsStatsNumberOfSelections,
            statType="int"
        )
        fig = get_tournaments_stats_histogram(
            x=pdSinglesTournamentsStatsNumberOfSelections["Tournament"],
            y=pdSinglesTournamentsStatsNumberOfSelections["Stat"],
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
    if customerProfile.multisTournamentsStatsNumberOfSelections:
        pdMultisTournamentsStatsNumberOfSelections = get_tournaments_stats_dataframe(
            tournamentsStats=customerProfile.multisTournamentsStatsNumberOfSelections,
            statType="int"
        )
        fig = get_tournaments_stats_histogram(
            x=pdMultisTournamentsStatsNumberOfSelections["Tournament"],
            y=pdMultisTournamentsStatsNumberOfSelections["Stat"],
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
    if customerProfile.tournamentsStatsTotalStake:
        pdTournamentsStatsTotalStake = get_tournaments_stats_dataframe(
            tournamentsStats=customerProfile.tournamentsStatsTotalStake,
            statType="float"
        )
        fig = get_tournaments_stats_histogram(
            x=pdTournamentsStatsTotalStake["Tournament"],
            y=pdTournamentsStatsTotalStake["Stat"],
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
    if customerProfile.singlesTournamentsStatsTotalStake:
        pdSinglesTournamentsStatsTotalStake = get_tournaments_stats_dataframe(
            tournamentsStats=customerProfile.singlesTournamentsStatsTotalStake,
            statType="float"
        )
        fig = get_tournaments_stats_histogram(
            x=pdSinglesTournamentsStatsTotalStake["Tournament"],
            y=pdSinglesTournamentsStatsTotalStake["Stat"],
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
    if customerProfile.multisTournamentsStatsTotalStake:
        pdMultisTournamentsStatsTotalStake = get_tournaments_stats_dataframe(
            tournamentsStats=customerProfile.multisTournamentsStatsTotalStake,
            statType="float"
        )
        fig = get_tournaments_stats_histogram(
            x=pdMultisTournamentsStatsTotalStake["Tournament"],
            y=pdMultisTournamentsStatsTotalStake["Stat"],
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















