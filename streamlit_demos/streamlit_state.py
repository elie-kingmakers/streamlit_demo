import streamlit as st
import numpy as np
import pandas as pd


st.title('State with callbacks')

if 'count' not in st.session_state:
    st.session_state.count = 0


def increment_counter(value):
    st.session_state.count += value


def decrement_counter(value):
    st.session_state.count -= value


increment_value = st.number_input('Increment Value', value=0, step=1)
increment = st.button('Increment', on_click=increment_counter, args=(increment_value, ))

decrement_value = st.number_input('Decrement', value=0, step=1)
decrement = st.button('Decrement', on_click=decrement_counter, args=(decrement_value, ))

st.write('Count = ', st.session_state.count)

if "celsius" not in st.session_state:
    # set the initial default value of the slider widget
    st.session_state.celsius = 50.0

st.slider(
    "Temperature in Celsius",
    min_value=-100.0,
    max_value=100.0,
    key="celsius" # same name as session state variable
)

# This will get the value of the slider widget
st.write(st.session_state.celsius)






