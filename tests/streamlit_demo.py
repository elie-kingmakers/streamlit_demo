import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import time


# ***********************************************************************************************************************
# ***********************************************************************************************************************

st.markdown("""---""")
st.markdown("""---""")

chart_data = pd.DataFrame(
    {
        "letter": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"],
        "score": [10, 41, 56, 72, 78, 38, 90, 62, 78, 25, 64, 78, 21, 8, 11, 98],
    }
)

st.write(chart_data)

score_to_filter = st.slider("score", 0, 100, 50)

filteredData = chart_data[chart_data["score"] <= score_to_filter]

st.write(filteredData)

# ***********************************************************************************************************************
# ***********************************************************************************************************************
st.markdown("""---""")

st.line_chart(chart_data["score"])

# ***********************************************************************************************************************
# ***********************************************************************************************************************
st.markdown("""---""")

option = st.sidebar.selectbox("Which letter do you like best?", chart_data["letter"])

st.write(f"You selected: {option}")

# ***********************************************************************************************************************
# ***********************************************************************************************************************
st.markdown("""---""")

left_column, middle_column, right_column = st.columns(3)
pressed = left_column.button("button column 1")
if pressed:
    middle_column.write("column 2")
    right_column.write("column 3")

# ***********************************************************************************************************************
# ***********************************************************************************************************************
st.markdown("""---""")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

# ***********************************************************************************************************************
# ***********************************************************************************************************************
st.markdown("""---""")

long_computation = st.button("start long computation")

if long_computation:
    st.write("Starting a long computation...")

    # Add a placeholder
    iterationText = st.empty()
    bar = st.progress(0)

    time.sleep(2)

    for i in range(100):
        # Update the progress bar with each iteration.
        iterationText.text(f"Progress: {i+1}%")  # so it ends with 100 instead of 99
        bar.progress(i + 1)
        time.sleep(0.1)

    st.write("...and now we're done!")

# ***********************************************************************************************************************
# ***********************************************************************************************************************
st.markdown("""---""")

form = st.form(key="my_form")

text_input = form.text_input(label="Enter your name")
submit_button = form.form_submit_button(label="Submit")

if submit_button:
    st.write(text_input)

startChartDemo = st.button("Start Chart Demo")

if startChartDemo:
    progress_bar = st.progress(0)
    status_text = st.empty()
    y = []
    chart = st.line_chart(y)

    for i in range(100):
        # Update progress bar.
        progress_bar.progress(i + 1)

        newY = np.random.randn(1)
        y.append(newY)

        # Update status text.
        status_text.text("The latest random number is: %s" % newY[0])

        # Append data to the chart.
        chart.add_rows(newY)

        # Pretend we're doing some computation that takes time.
        time.sleep(0.1)

    status_text.text("Done!")

    x = np.arange(start=0, stop=100, step=1)
    fig = plt.figure()
    plt.plot(x, y)

    st.pyplot(fig)

# ***********************************************************************************************************************
# ***********************************************************************************************************************
st.markdown("""---""")

st.text("This will appear first")
# Appends some text to the app.

my_slot1 = st.empty()
# Appends an empty slot to the app. We'll use this later.

my_slot2 = st.empty()
# Appends another empty slot.

st.text("This will appear last")
# Appends some more text to the app.

my_slot1.text("This will appear second")
# Replaces the first empty slot with a text string.


# ***********************************************************************************************************************
# ***********************************************************************************************************************
st.markdown("""---""")
st.title("State with callbacks")

if "count" not in st.session_state:
    st.session_state.count = 0


def increment_counter(value):
    st.session_state.count += value


def decrement_counter(value):
    st.session_state.count -= value


increment_value = st.number_input("Increment Value", value=0, step=1)
increment = st.button("Increment", on_click=increment_counter, args=(increment_value,))

decrement_value = st.number_input("Decrement", value=0, step=1)
decrement = st.button("Decrement", on_click=decrement_counter, args=(decrement_value,))

st.write("Count = ", st.session_state.count)

if "celsius" not in st.session_state:
    # set the initial default value of the slider widget
    st.session_state.celsius = 50.0

st.slider(
    "Temperature in Celsius", min_value=-100.0, max_value=100.0, key="celsius"  # same name as session state variable
)

# This will get the value of the slider widget
st.write(st.session_state.celsius)
