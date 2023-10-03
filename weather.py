import requests
import json

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def display_weather(data):
    if data is not None:
        city = data["name"]
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        print(f"Weather in {city}:")
        print(f"Description: {weather_desc}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found. Please check the city name.")

if __name__ == "__main__":
    api_key = "c732db63b040588787982fe368aeec94"
    city_name = input("Enter the name of the city: ")

    weather_data = get_weather(api_key, city_name)

    if weather_data:
        display_weather(weather_data)
