import requests

API_KEY = "67ee016f9c786105caf40a364be6a65b"

def get_data(location, forecast_days=5):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    data_per_time_step = data.get("list")
    num_data_points = 8*forecast_days
    filtered_data = data_per_time_step[:num_data_points]
    return filtered_data

if __name__ == '__main__':
    print(get_data("London", forecast_days=3))