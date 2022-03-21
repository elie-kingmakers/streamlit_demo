from typing import Any

import streamlit as st


def show_data(label: str = None, value: Any = None, inBold: bool = False, column: st.columns = None):
    if label is None:
        markdownString = ""
    else:
        markdownString = f"{label}:  "

    if inBold:
        markdownString += "<strong>"

    if value is not None:
        if isinstance(value, float):
            markdownString += "{:.2f}".format(value)
        else:
            markdownString += f"{value}"

    if inBold:
        markdownString += "</strong>"

    if column is None:
        st.markdown(markdownString, unsafe_allow_html=True)
    else:
        column.markdown(markdownString, unsafe_allow_html=True)
