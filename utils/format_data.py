from typing import Any

import pandas as pd
from datetime import datetime


def get_css_evaluation(
        value: float,
        compareWith: float,
        sign: str = "",
        resultSmaller: str = None,
        resultGreater: str = None,
        resultEqual: str = None
) -> str:
    valueFormatted = "{:.2f} {}".format(value, sign)
    valueSmaller = resultSmaller if resultSmaller is not None else valueFormatted
    valueGreater = resultGreater if resultGreater is not None else valueFormatted
    valueEqual = resultEqual if resultEqual is not None else valueFormatted

    if value < compareWith:
        comparisonResult = "<span class='highlight_red'>{}</span>".format(valueSmaller)

    elif value > compareWith:
        comparisonResult = "<span class='highlight_green'>{}</span>".format(valueGreater)

    else:
        comparisonResult = "<span class='highlight_grey'>{}</span>".format(valueEqual)

    return comparisonResult


def get_css_comparison_with_population(userValue: float, populationValue: float) -> str:
    cssEvaluation = get_css_evaluation(value=userValue, compareWith=populationValue)

    comparisonResult = " &ensp; {} &emsp; ({:.3f})".format(cssEvaluation, populationValue)
    return comparisonResult


def get_date_string(dateKey: int) -> str:
    if str(dateKey) == "N/A":
        return "N/A"

    date = datetime.strptime(str(dateKey), "%Y%m%d")

    dateString = datetime.strftime(date, "%Y-%m-%d")
    return dateString


def get_gender_string(gender: str) -> str:
    if gender == "M":
        return "Male"
    elif gender == "F":
        return "Female"
    else:
        return "Unknown"


def get_winning_status_string(winningStatus: int, colorCoded: bool = False) -> str:
    if winningStatus == 1:
        if colorCoded:
            return "<span class='highlight_red'>WINNING</span>"
        else:
            return "WINNING"
    elif winningStatus == -1:
        if colorCoded:
            return "<span class='highlight_green'>LOSING</span>"
        else:
            return "LOSING"
    else:
        if colorCoded:
            return "<span class='highlight_grey'>NEUTRAL</span>"
        else:
            return "NEUTRAL"


def get_sports_stats_dataframe(sportsStats: list, statType: str = "int") -> pd.DataFrame:
    data = []

    for sportStat in sportsStats:
        sport, stat = str(sportStat).split("__")

        sport = str(sport)

        if statType == "int":
            statFloat = float(stat)
            stat = int(statFloat)
        elif statType == "float":
            stat = float(stat)

        sportStatData = [sport, stat]
        data.append(sportStatData)

    # sanity check. should be already sorted in backend
    def sort_key(e):
        return e[1]

    data.sort(key=sort_key, reverse=True)

    pdResult = pd.DataFrame(data, columns=["Sport", "Stat"])
    return pdResult


def get_tournaments_stats_dataframe(tournamentsStats: list, statType: str = "int") -> pd.DataFrame:
    data = []

    for tournamentStat in tournamentsStats:
        tournament, stat = str(tournamentStat).split("__")

        tournament = str(tournament)

        if statType == "int":
            statFloat = float(stat)
            stat = int(statFloat)
        elif statType == "float":
            stat = float(stat)

        tournamentStatData = [tournament, stat]
        data.append(tournamentStatData)

    # sanity check. should be already sorted in backend
    def sort_key(e):
        return e[1]

    data.sort(key=sort_key, reverse=True)

    pdResult = pd.DataFrame(data, columns=["Tournament", "Stat"])
    return pdResult


def get_markets_stats_dataframe(marketsStats: list, statType: str = "int") -> pd.DataFrame:
    data = []

    for marketStat in marketsStats:
        market, stat = str(marketStat).split("__")

        market = str(market)

        if statType == "int":
            statFloat = float(stat)
            stat = int(statFloat)
        elif statType == "float":
            stat = float(stat)

        marketStatData = [market, stat]
        data.append(marketStatData)

    # sanity check. should be already sorted in backend
    def sort_key(e):
        return e[1]

    data.sort(key=sort_key, reverse=True)

    pdResult = pd.DataFrame(data, columns=["Market", "Stat"])
    return pdResult


def get_value(value: Any, dataType: str, scale: float = 1.0) -> Any:
    if dataType == "str":
        if pd.isna(value):
            return "N/A"
        return str(value)

    elif dataType == "int":
        if pd.isna(value):
            return "N/A"
        return int(value * int(scale))

    elif dataType == "float":
        if pd.isna(value):
            return "N/A"
        return float(value * scale)

    elif dataType == "list":
        if value is None:
            return list()
        return list(value)