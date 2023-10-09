import streamlit as st

st.title("Weather Forecast For The Next Few Days")
location = st.text_input("Location: ")
days = st.slider("Days To Forecast: ", min_value=1, max_value=5, help="Select the number of days to forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"The {option} for the next {days} days in {location}")