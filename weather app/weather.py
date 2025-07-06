from pprint import pprint
import requests
import os 
from dotenv import load_dotenv

load_dotenv()

def get_current_weather(city="tunisia"):
    base_url = "http://api.weatherstack.com/current"
    api_key = os.getenv("API_KEY")
    
    params = {
        "access_key": api_key,
        "query": city
    }

    weather_data = requests.get(base_url, params=params).json()
    return weather_data

if __name__ == "__main__":
    print("\n ********** Get Current Weather Conditions *****")
    city = input("\n Please enter a city name: ")
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
