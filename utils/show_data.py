from typing import Any

import streamlit as st

from datamodel.constants import MAX_FULL_NUMBER


def show_data(label: str = None, value: Any = None, sign: str = None, inBold: bool = False, column: st.columns = None):
    if label is None:
        markdownString = ""
    else:
        markdownString = f"{label}:  "

    if inBold:
        markdownString += "<strong>"

    if value is not None:
        if isinstance(value, float):
            if value > MAX_FULL_NUMBER or value < -MAX_FULL_NUMBER:
                markdownString += "{:,.2e}".format(value)
            else:
                markdownString += "{:,.2f}".format(value)
        else:
            markdownString += f"{value}"

    if sign is not None:
        markdownString += f" {sign}"

    if inBold:
        markdownString += "</strong>"

    if column is None:
        st.markdown(markdownString, unsafe_allow_html=True)
    else:
        column.markdown(markdownString, unsafe_allow_html=True)
