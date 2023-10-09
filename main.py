import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast For The Next Few Days")
location = st.text_input("Location: ")
days = st.slider("Days To Forecast: ", min_value=1, max_value=5, help="Select the number of days to forecast")
category = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"The {category} for the next {days} days in {location}")

d, t = get_data(location, days, category)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)