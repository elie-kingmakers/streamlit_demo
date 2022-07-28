import streamlit as st

from datamodel.constants import BLANK_SPACE


def insert_blank(column: st.columns = None):
    if column is None:
        st.markdown(BLANK_SPACE, unsafe_allow_html=True)
    else:
        column.markdown(BLANK_SPACE, unsafe_allow_html=True)


def remove_whitespace_top():
    st.markdown(
        """
        <style>
           .css-18e3th9 {
                padding-top: 0rem;
                padding-bottom: 10rem;
                padding-left: 5rem;
                padding-right: 5rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def hide_menu_button():
    st.markdown(
        """
        <style>
            #MainMenu { visibility: hidden; }
            footer { visibility: hidden; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def resize_sidebar(width: int):
    st.markdown(
        f"""
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {{
            width: {width}px;
        }}
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {{
            width: {width}px;
            margin-left: -{width}px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )







