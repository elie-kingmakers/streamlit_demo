import streamlit as st

def local_css(file_name):
    with open(file_name) as file:
        st.markdown('<style>{}</style>'.format(file.read()), unsafe_allow_html=True)