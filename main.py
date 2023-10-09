import streamlit as st
import plotly.express as px
from backend import get_data

images = {
    "Clear": "images/clear.png",
    "Clouds": "images/cloud.png",
    "Rain": "images/rain.png",
    "Snow": "images/snow.png"
}

st.title("Weather Forecast For The Next Few Days")
location = st.text_input("Location: ")
days = st.slider("Days To Forecast: ", min_value=1, max_value=5, help="Select the number of days to forecast")
category = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"The {category} for the next {days} days in {location}")

if location:
    filtered_data = get_data(location, days)

    dates = [i.get("dt") for i in filtered_data]
    if category == "Temperature":
        filtered_data = [i.get("main").get("temp") for i in filtered_data]
        figure = px.line(x=dates, y=filtered_data, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)
    if category == "Sky":
        filtered_data = [i.get("weather")[0].get("main") for i in filtered_data]
        image_paths = [images.get(j) for j in filtered_data]
        st.image(image_paths, width=115)

