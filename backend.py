import requests

API_KEY = "67ee016f9c786105caf40a364be6a65b"

def get_data(location, forecast_days=5, category="Temperature"):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    data_per_time_step = data.get("list")
    num_data_points = 8*forecast_days
    filtered_data = data_per_time_step[:num_data_points]
    dates = [i.get("dt") for i in filtered_data]
    if category == "Temperature":
        filtered_data = [i.get("main").get("temp") for i in filtered_data]
    if category == "Sky":
        filtered_data = [i.get("weather")[0].get("main") for i in filtered_data]
    return dates, filtered_data

if __name__ == '__main__':
    print(get_data("London", forecast_days=3, category="Temperature"))