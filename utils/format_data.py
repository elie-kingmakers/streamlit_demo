from typing import Any

import pandas as pd
from datetime import datetime


def get_css_evaluation(
    value: float, compareWith: float, resultSmaller: str = None, resultGreater: str = None, resultEqual: str = None
) -> str:
    valueFormatted = "{:.3f}".format(value)
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


def get_winning_status_string(winningStatus: int) -> str:
    if winningStatus == 1:
        return "WINNING"
    elif winningStatus == -1:
        return "LOSING"
    else:
        return "NEUTRAL"


def get_value(value: Any, dataType: str, scale: float = 1.0) -> Any:
    if pd.isna(value):
        return "N/A"

    if dataType == "str":
        return str(value)
    elif dataType == "int":
        return int(value * int(scale))
    elif dataType == "float":
        return float(value * scale)