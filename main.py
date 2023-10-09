import streamlit as st
import plotly.express as px

st.title("Weather Forecast For The Next Few Days")
location = st.text_input("Location: ")
days = st.slider("Days To Forecast: ", min_value=1, max_value=5, help="Select the number of days to forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"The {option} for the next {days} days in {location}")

def get_data(days):
    dates = ['2022-10-25', '2022-10-26', '2022-10-27']
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)